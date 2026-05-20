"""
Z-Web-Scraper — Scraper engine.
Uses Selenium + headless Chromium to fully render any page (including SPAs).
"""

import os
import time
import json
import hashlib
from datetime import datetime, timezone
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

from .config import DEFAULT_TIMEOUT, DEFAULT_WAIT_AFTER_LOAD, CHROME_OPTIONS, USER_AGENT

__all__ = [
    "scrape_url",
    "save_html",
    "save_metadata",
    "extract_text",
    "extract_links",
    "extract_images",
]


def _build_driver(chrome_bin: str | None = None, timeout: int = DEFAULT_TIMEOUT) -> webdriver.Chrome:
    """Create a headless Chrome WebDriver (auto-detects chromedriver from PATH)."""
    opts = Options()
    for arg in CHROME_OPTIONS:
        opts.add_argument(arg)
    if chrome_bin:
        opts.binary_location = chrome_bin
    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(timeout)
    return driver


def _auto_scroll(driver, max_scrolls: int = 100, pause: float = 1.5) -> int:
    """Scroll to bottom to trigger lazy-loading. Returns scroll count."""
    count = 0
    no_new_streak = 0

    for _ in range(max_scrolls):
        prev_count = len(driver.find_elements("css selector", "img, a[href], video"))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        count += 1

        new_count = len(driver.find_elements("css selector", "img, a[href], video"))
        if new_count == prev_count:
            no_new_streak += 1
            if no_new_streak >= 3:
                break
        else:
            no_new_streak = 0

    driver.execute_script("window.scrollTo(0, 0);")
    return count


def scrape_url(
    url: str,
    timeout: int = DEFAULT_TIMEOUT,
    wait_after: int = DEFAULT_WAIT_AFTER_LOAD,
    scroll: bool = True,
    execute_js: str | None = None,
    chrome_bin: str | None = None,
    callback=None,
) -> dict:
    """
    Scrape a URL and return full rendered HTML + metadata.

    Args:
        url: Website URL to scrape.
        timeout: Max seconds to wait for page load.
        wait_after: Extra seconds for JS to settle.
        scroll: Whether to auto-scroll for lazy content.
        execute_js: Optional JavaScript to run after load.
        chrome_bin: Path to chromium binary (auto-detects if None).
        callback: Optional function called with (event, message) for progress updates.

    Returns:
        dict with keys: url, final_url, title, html, char_count, link_count,
        image_count, meta_tags, headers, scraped_at, load_time_s,
        scroll_count, file_size_bytes, content_hash
    """
    def _emit(event, msg):
        if callback:
            callback(event, msg)

    start = time.time()
    driver = None

    try:
        _emit("step", "Launching headless Chromium...")
        driver = _build_driver(chrome_bin, timeout)
        _emit("ok", "Chromium launched")

        _emit("step", f"Loading page (timeout: {timeout}s)...")
        driver.get(url)

        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        load_so_far = round(time.time() - start, 1)
        _emit("ok", f"Page loaded ({load_so_far}s)")

        if wait_after > 0:
            _emit("step", f"Waiting {wait_after}s for JS to settle...")
            time.sleep(wait_after)

        scroll_count = 0
        if scroll:
            _emit("step", "Scrolling to load lazy content...")
            scroll_count = _auto_scroll(driver)
            _emit("ok", f"Scrolled {scroll_count} times")

        if execute_js:
            _emit("step", "Executing custom JavaScript...")
            try:
                driver.execute_script(execute_js)
                time.sleep(1)
                _emit("ok", "Custom JS executed")
            except Exception as e:
                _emit("warn", f"JS error: {str(e)[:100]}")

        _emit("step", "Capturing rendered HTML...")
        html = driver.page_source
        final_url = driver.current_url
        title = driver.title

        size_kb = len(html.encode("utf-8")) / 1024
        _emit("ok", f"Captured {len(html):,} chars ({size_kb:.1f} KB)")

    finally:
        if driver:
            driver.quit()

    # ── Parse metadata ──
    _emit("step", "Extracting metadata...")
    soup = BeautifulSoup(html, "html.parser")

    meta_tags = {}
    for tag in soup.find_all("meta"):
        name = tag.get("name") or tag.get("property") or tag.get("http-equiv")
        content = tag.get("content")
        if name and content:
            meta_tags[name] = content

    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            href = urljoin(final_url, href)
        links.append({"text": a.get_text(strip=True)[:120], "url": href})

    images = []
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src and not src.startswith(("data:", "http://", "https://")):
            src = urljoin(final_url, src)
        images.append({"src": src, "alt": img.get("alt", "")})

    scripts = len(soup.find_all("script"))
    stylesheets = len(soup.find_all("link", rel="stylesheet"))
    load_time = round(time.time() - start, 2)
    content_hash = hashlib.sha256(html.encode("utf-8")).hexdigest()[:16]

    _emit("ok", f"Found {len(links)} links, {len(images)} images, {scripts} scripts, {stylesheets} stylesheets")

    return {
        "url": url,
        "final_url": final_url,
        "title": title,
        "html": html,
        "char_count": len(html),
        "link_count": len(links),
        "image_count": len(images),
        "meta_tags": meta_tags,
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "load_time_s": load_time,
        "scroll_count": scroll_count,
        "file_size_bytes": len(html.encode("utf-8")),
        "content_hash": content_hash,
        "links": links,
        "images": images,
        "scripts": scripts,
        "stylesheets": stylesheets,
    }


def save_html(html: str, path: str) -> str:
    """Save HTML to file. Returns path."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


def save_metadata(meta: dict, path: str) -> str:
    """Save metadata dict as JSON (excludes html). Returns path."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    compact = {k: v for k, v in meta.items() if k != "html"}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(compact, f, indent=2, ensure_ascii=False)
    return path


def extract_text(html: str) -> str:
    """Extract readable text from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)


def extract_links(html: str, base_url: str = "") -> list[dict]:
    """Extract all links with text and resolved URLs."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if base_url and not href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            href = urljoin(base_url, href)
        links.append({"text": a.get_text(strip=True)[:120], "url": href})
    return links


def extract_images(html: str, base_url: str = "") -> list[dict]:
    """Extract all images with src, alt, and dimensions."""
    soup = BeautifulSoup(html, "html.parser")
    images = []
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if base_url and src and not src.startswith(("data:", "http://", "https://")):
            src = urljoin(base_url, src)
        images.append({
            "src": src,
            "alt": img.get("alt", ""),
            "width": img.get("width"),
            "height": img.get("height"),
        })
    return images
