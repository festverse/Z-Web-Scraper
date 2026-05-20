"""Z-Web-Scraper — Full-page web scraper for Google Colab."""

from .config import DEFAULT_TIMEOUT, DEFAULT_WAIT_AFTER_LOAD, DEFAULT_OUTPUT_DIR, USER_AGENT
from .ui import (
    show_header, show_ok, show_warn, show_err, show_info, show_step,
    show_stats, show_html_preview, show_links_table, show_meta_tags,
)


def __getattr__(name):
    """Lazy-load scraper functions only when accessed (requires selenium)."""
    if name in (
        "scrape_url", "save_html", "save_metadata",
        "extract_text", "extract_links", "extract_images",
    ):
        from . import scraper
        return getattr(scraper, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "DEFAULT_TIMEOUT", "DEFAULT_WAIT_AFTER_LOAD", "DEFAULT_OUTPUT_DIR", "USER_AGENT",
    "show_header", "show_ok", "show_warn", "show_err", "show_info", "show_step",
    "show_stats", "show_html_preview", "show_links_table", "show_meta_tags",
    "scrape_url", "save_html", "save_metadata",
    "extract_text", "extract_links", "extract_images",
]
