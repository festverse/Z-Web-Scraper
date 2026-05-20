# 📖 Z-Web-Scraper — User Guide

> **Everything you need to know to use Z-Web-Scraper, step by step.**
> Written for beginners — no coding experience required.

---

## 📑 Table of Contents

| Section | What You'll Learn |
|---------|-------------------|
| [🤔 What Is This?](#-what-is-this) | Basic overview in plain English |
| [💻 What You Need](#-what-you-need) | Requirements before starting |
| [🚀 Getting Started](#-getting-started) | Opening the notebook in Google Colab |
| [🔧 Step 1 — Setup](#-step-1--setup) | Installing Chromium and dependencies |
| [🕷️ Step 2 — Scrape](#️-step-2--scrape) | Capturing rendered HTML from any website |
| [💾 Step 3 — Export](#-step-3--export) | Downloading your scraped files |
| [🎛️ All Settings Explained](#️-all-settings-explained) | Every parameter in detail |
| [📐 Site Type Guide](#-site-type-guide) | Choosing the right settings per site |
| [📂 Where Are My Files?](#-where-are-my-files) | Finding scraped HTML and metadata |
| [❓ FAQ](#-faq) | Answers to common questions |
| [🐛 Common Problems & Fixes](#-common-problems--fixes) | Troubleshooting guide |

---

## 🤔 What Is This?

**Z-Web-Scraper** is a tool that captures the **full rendered HTML** from any website. It runs a real browser behind the scenes, so it works on JavaScript-heavy sites like React, Vue, Angular, and Next.js apps — not just static pages.

Here's the simple version of how it works:

```
You paste a URL → Browser opens the page → JavaScript runs → Full HTML captured → You download it
```

**What makes it special:**
- **Real browser** — Uses headless Chromium, so JavaScript frameworks execute fully before capture
- **Auto-scroll** — Scrolls to the bottom of the page to trigger lazy-loaded images and infinite scroll
- **Custom JS** — You can inject your own JavaScript (click buttons, expand menus, trigger modals)
- **Free** — Runs on Google Colab, no installation needed, no GPU required
- **Metadata extraction** — Automatically pulls title, Open Graph tags, Twitter cards, links, and images

### What Is a "Notebook"?

A **notebook** (also called a Jupyter notebook or Colab notebook) is an interactive document that contains code. Think of it like a step-by-step recipe:

1. You run **Cell 1** → it installs Chromium and Selenium
2. You run **Cell 2** → it scrapes your target website
3. You run **Cell 3** → it downloads the results as a ZIP

Each cell is a box of code. You click the **▶ Play button** on each cell to run it, one at a time, in order.

### What Is Google Colab?

**Google Colab** (short for "Colaboratory") is a free service from Google that lets you run code in your browser. It gives you:
- A **free computer in the cloud** — no installation on your machine
- **Python** pre-installed — no setup needed
- **Temporary storage** — files last for the session

Think of it as a free computer in the cloud that you access through your browser.

### What Is Selenium?

**Selenium** is a tool that controls a real web browser programmatically. Instead of just downloading the raw HTML (which might be an empty shell for SPAs), Selenium:
1. Opens a real Chromium browser
2. Navigates to your URL
3. Waits for all JavaScript to execute
4. Captures the fully rendered page — exactly what a human would see

This is why Z-Web-Scraper works on Next.js, React, Vue, and other frameworks that build their content with JavaScript.

---

## 💻 What You Need

| Requirement | Details |
|-------------|---------|
| **A Google account** | Free — sign up at [accounts.google.com](https://accounts.google.com) |
| **A web browser** | Chrome, Firefox, Edge, Safari — any modern browser |
| **Internet connection** | Stable connection for installing Chromium (~200 MB) |
| **A URL to scrape** | Any public website URL |

> ⚠️ **You do NOT need:**
> - A graphics card on your own computer
> - Python installed
> - Any coding knowledge
> - Any paid software
> - A GPU (this runs on CPU)

---

## 🚀 Getting Started

### Opening the Notebook

1. **Click this link** (or the "Open in Colab" button in the README):

   👉 [Open Z-Web-Scraper in Google Colab](https://colab.research.google.com/github/festverse/Z-Web-Scraper/blob/main/notebook/Z-Web-Scraper.ipynb)

2. **Sign in** with your Google account if prompted.

3. You'll see the notebook open in Google Colab. It looks like a document with boxes (cells) of code.

> 💡 **No GPU needed!** Unlike image generation tools, Z-Web-Scraper runs entirely on CPU. You do NOT need to change the runtime type. The default "CPU" runtime works perfectly.

---

## 🔧 Step 1 — Setup

### What This Step Does

This cell prepares everything behind the scenes:

1. **Clones the Z-Web-Scraper repo** — downloads the shared code modules
2. **Installs system packages** — Chromium browser, ChromeDriver, fonts, and libraries
3. **Installs Python packages** — Selenium, BeautifulSoup, requests, lxml
4. **Detects browser paths** — finds Chromium and ChromeDriver on the system
5. **Verifies Selenium** — runs a quick test to confirm everything works

| Package | What It Does |
|---------|-------------|
| **Chromium** | Headless browser that renders JavaScript |
| **ChromeDriver** | Bridge between Selenium and Chromium |
| **Selenium** | Python library that controls the browser |
| **BeautifulSoup** | Parses HTML to extract links, images, meta tags |
| **lxml** | Fast HTML parser (used by BeautifulSoup) |

### How to Run It

1. **Click on the first code cell** — it's labeled "🔧 Step 1 — Setup"
2. **Click the ▶ Play button** on the left side of the cell (or press `Ctrl+Enter`)
3. **Wait** — you'll see text output showing progress. This takes about **30–60 seconds** the first time.
4. **Wait for the green checkmark** ✅ — it appears when the cell finishes successfully

### What You'll See

```
🔧 Setup
  Installing Chromium, Selenium & dependencies

🔹 Installing system packages...
✅ System packages installed
🔹 Installing Python packages...
✅ Python packages installed
🔹 Detecting browser paths...
✅ Chromium: /usr/bin/chromium-browser
✅ ChromeDriver: /usr/lib/chromium-browser/chromedriver
✅ Version: Chromium 131.0.6778.204
🔹 Verifying Selenium connection...
✅ Selenium connection verified
✅ Output directory: /content/Z-Web-Scraper_output
✅ Setup complete!
ℹ️ ➡️ Run the next cell to scrape a website
```

> ⚠️ **If you see a warning about restarting the runtime:**
> Click "Cancel" — you don't need to restart. The notebook will work fine.

> 💡 **Second run is faster!** System packages are cached. If you run Cell 1 again in a new session, it only needs to re-detect paths (~10s) instead of reinstalling (~60s).

---

## 🕷️ Step 2 — Scrape

### What This Step Does

This is the main part! This cell:

1. **Launches headless Chromium** — opens a browser in the background
2. **Navigates to your URL** — loads the page
3. **Waits for JavaScript** — waits for `document.readyState === "complete"`
4. **Settles** — extra wait time for JS-heavy frameworks to finish
5. **Auto-scrolls** — scrolls to bottom to trigger lazy-loaded content
6. **Captures HTML** — grabs the fully rendered page source
7. **Extracts metadata** — title, Open Graph tags, Twitter cards, links, images
8. **Displays results** — stats, preview, link table, meta tags
9. **Saves files** — HTML file + metadata JSON to output directory

### Filling In the Settings

Before running, you'll see several fields to fill in. Here's what each one means:

#### URL Field

| Field | What to Type | Example |
|-------|-------------|---------|
| **url** | The website to scrape | `https://example.com` |

#### Timing Settings

| Field | Default | What It Does |
|-------|---------|-------------|
| **timeout** | 30 | Max seconds to wait for the page to load |
| **wait_after_load** | 3 | Extra seconds for JavaScript to settle after page reports "complete" |
| **auto_scroll** | True | Scroll to bottom to trigger lazy-loaded images and infinite scroll |
| **custom_js** | *(empty)* | JavaScript to execute after page loads (e.g., click buttons) |

#### Output Settings

| Field | Default | What It Does |
|-------|---------|-------------|
| **save_html_file** | True | Save the captured HTML to a file |
| **show_preview** | True | Display a syntax-highlighted HTML preview |
| **show_links** | True | Extract and display all links found on the page |

### Running the Scrape

1. **Paste a URL** into the `url` field
2. **Adjust settings** if needed (the defaults work well for most sites)
3. **Click the ▶ Play button** on the "🕷️ Step 2 — Scrape" cell
4. **Wait** — you'll see real-time progress messages
5. **Results appear!** — stats, preview, links, and meta tags

### What You'll See

```
🕷️ Scraping
  https://example.com

🔹 Launching headless Chromium...
✅ Chromium launched
🔹 Loading page (timeout: 30s)...
✅ Page loaded (2.3s)
🔹 Waiting 3s for JS to settle...
🔹 Scrolling to load lazy content...
✅ Scrolled 3 times
🔹 Capturing rendered HTML...
✅ Captured 125,000 characters (122.1 KB)
🔹 Extracting metadata...
✅ Found 42 links, 15 images, 8 scripts, 3 stylesheets

[Stats row: Characters | Size | Links | Images | Load Time | Scrolls]
[HTML Preview]
[Links Table]
[Meta Tags Table]

✅ Done!
  Scraped Example Domain in 8.45s
ℹ️ 🔄 Run this cell again with a different URL to scrape more pages
```

### Running Again

Want to scrape another page? Just change the **url** field and click ▶ again. Each run creates new files in the output directory. You can scrape multiple pages and export them all together in Step 3.

> 💡 **Tip:** For heavy SPAs (Next.js, Nuxt), increase `wait_after_load` to 5–8 seconds to ensure all JavaScript finishes executing.

---

## 💾 Step 3 — Export

### What This Step Does

This cell packages all your scraped files into a `.zip` file and downloads it to your computer.

### How to Run It

1. **Click the ▶ Play button** on the "💾 Step 3 — Export" cell
2. **A download dialog appears** — choose where to save on your computer
3. **Done!** Your HTML and metadata files are in the zip

> 💡 **If the download doesn't start automatically:**
> - Check your browser's download bar
> - Or find the file at `/content/Z-Web-Scraper_export_*.zip` in Colab's file browser (folder icon on the left sidebar)

### What's in the ZIP?

| File | Contents |
|------|----------|
| `domain_timestamp.html` | Full rendered HTML — the complete page |
| `domain_timestamp_meta.json` | Metadata — title, tags, stats, links, hash |

---

## 🎛️ All Settings Explained

### URL Settings

| Setting | Type | Default | Explanation |
|---------|------|---------|-------------|
| `url` | Text | *(empty)* | **The website to scrape.** Paste any URL. If you omit `https://`, it's added automatically. |

### Timing Settings

| Setting | Type | Default | Range | Explanation |
|---------|------|---------|-------|-------------|
| `timeout` | Slider | 30 | 10–120 | **Max wait time** for the page to load. Increase for slow servers or heavy SPAs. |
| `wait_after_load` | Slider | 3 | 0–30 | **Extra settle time** after the page reports "complete". JavaScript frameworks may still be initializing. Increase for Next.js/Nuxt (5–8s). |
| `auto_scroll` | Checkbox | True | — | **Scroll to bottom** to trigger lazy-loaded images, infinite scroll, and deferred content. Disable if you only need above-the-fold content. |
| `custom_js` | Text | *(empty)* | Any JS | **JavaScript to execute** after the page loads. Useful for clicking expand buttons, triggering modals, or dismissing cookie banners. |

### Output Settings

| Setting | Type | Default | Explanation |
|---------|------|---------|-------------|
| `save_html_file` | Checkbox | True | **Save the HTML** to a file in the output directory. Always recommended. |
| `show_preview` | Checkbox | True | **Display a preview** of the HTML source with syntax highlighting (first 5000 chars). |
| `show_links` | Checkbox | True | **Extract all links** and display them in a table with text and URLs. |

---

## 📐 Site Type Guide

Different websites need different settings. Use this guide:

| Site Type | Timeout | Wait After | Auto-Scroll | Custom JS | Speed |
|:---------:|:-------:|:----------:|:-----------:|:---------:|:-----:|
| **Static HTML / Blog** | 15s | 1s | Optional | — | ⚡⚡⚡ |
| **React / Vue SPA** | 30s | 3–5s | Yes | — | ⚡⚡ |
| **Next.js / Nuxt (SSR)** | 60s | 5–8s | Yes | — | ⚡ |
| **Heavy Media Site** | 90–120s | 5–10s | Yes | — | 🐢 |
| **Infinite Scroll** | 60s | 3s | Yes | — | ⚡ |
| **Cookie Wall / Modal** | 30s | 3s | Yes | `document.querySelector('.accept').click()` | ⚡⚡ |

### Common Custom JS Examples

| What to Do | JavaScript |
|-----------|-----------|
| Click cookie accept button | `document.querySelector('[class*="accept"]').click()` |
| Click "Load More" button | `document.querySelector('.load-more').click()` |
| Dismiss a modal | `document.querySelector('.modal-close').click()` |
| Scroll to a specific element | `document.getElementById('content').scrollIntoView()` |
| Wait and click | `setTimeout(() => document.querySelector('.btn').click(), 2000)` |

---

## 📂 Where Are My Files?

### In Google Colab

| What | Where | How to Find |
|------|-------|-------------|
| **Scraped HTML files** | `/content/Z-Web-Scraper_output/` | 📁 File browser → content → Z-Web-Scraper_output |
| **Metadata JSON** | `/content/Z-Web-Scraper_output/` | Same folder as HTML files |
| **Exported ZIP** | `/content/Z-Web-Scraper_export_*.zip` | 📁 File browser → content |
| **Z-Web-Scraper repo** | `/content/Z-Web-Scraper/` | 📁 File browser → content → Z-Web-Scraper |

### Opening the File Browser

1. Click the **📁 folder icon** on the left sidebar in Google Colab
2. Navigate through the folders to find your files
3. Right-click any file to download it to your computer

> ⚠️ **Important:** Colab storage is **temporary**. When your session ends, all files are deleted. Always download your scraped files using Step 3 before closing!

---

## ❓ FAQ

<details>
<summary><b>Does it work on Next.js / React / Vue sites?</b></summary>

Yes! Selenium runs a real Chromium browser, so all JavaScript frameworks execute fully before the HTML is captured. You get what the user sees, not what the server initially sends.
</details>

<details>
<summary><b>Can I scrape pages behind login?</b></summary>

Not directly. You could inject cookies via `custom_js`, but there's no built-in auth flow. For login-gated sites, consider using browser extensions or dedicated scraping services.
</details>

<details>
<summary><b>Why not just use `requests` or `urllib`?</b></summary>

Those only get the initial server response — no JavaScript execution. SPAs (Single Page Applications) return an empty shell that gets filled by JS. Selenium renders the full page in a real browser first.
</details>

<details>
<summary><b>Is GPU required?</b></summary>

No! Z-Web-Scraper runs entirely on CPU. Chromium doesn't need GPU acceleration for web scraping. The default Colab CPU runtime works perfectly.
</details>

<details>
<summary><b>Can I scrape multiple URLs?</b></summary>

Yes! Run Step 2 multiple times with different URLs. All files accumulate in the output directory. When you're done, run Step 3 once to export everything together.
</details>

<details>
<summary><b>How big can the HTML be?</b></summary>

There's no hard limit. Very large pages (10+ MB HTML) may slow down the preview display, but the full HTML is always saved to file regardless of size.
</details>

<details>
<summary><b>Is it really free?</b></summary>

Yes. Google Colab's free tier provides everything you need. No GPU required, no paid software, no API keys.
</details>

<details>
<summary><b>What happens if Colab disconnects?</b></summary>

Your session ends and temporary files are deleted. Always download your scraped files using Step 3 before closing the browser tab. You can re-run all cells to start fresh.
</details>

---

## 🐛 Common Problems & Fixes

### `Chromium not found` or `ChromeDriver not found`

**What it means:** The browser or driver wasn't installed properly.

**Fix:** Re-run **Cell 1 (Setup)**. Make sure it completes with all green checkmarks. If it still fails, try **Runtime → Restart runtime**, then re-run Cell 1.

---

### `TimeoutException`

**What it means:** The page took longer to load than the timeout allows.

**Fixes:**
- Increase `timeout` to 60–120 seconds
- Check if the URL is correct and the site is online
- The site might be blocking automated browsers — try a different URL

---

### Empty or incomplete HTML

**What it means:** JavaScript didn't finish executing before capture.

**Fixes:**
- Increase `wait_after_load` to 5–10 seconds
- Enable `auto_scroll` if the site uses lazy loading
- Use `custom_js` to trigger any required interactions

---

### Missing lazy-loaded images

**What it means:** The page loads images as you scroll, but scrolling didn't happen.

**Fix:** Make sure `auto_scroll` is enabled (it's on by default). The scraper scrolls to the bottom to trigger all lazy loaders.

---

### `WebDriverException` or driver crash

**What it means:** Chromium crashed or the driver connection was lost.

**Fixes:**
- **Runtime → Restart runtime**, then re-run all cells from scratch
- Make sure you're not running other heavy notebooks simultaneously
- Try reducing the number of concurrent Colab sessions

---

### `ConnectionRefused` or site blocks bots

**What it means:** The target website detected automated access and blocked it.

**Fixes:**
- Some sites block headless browsers — this is a limitation of automated scraping
- Try adding a longer `wait_after_load` (sometimes helps)
- Check the site's `robots.txt` and terms of service

---

### Scraped HTML is different from what I see in my browser

**What it means:** The site may serve different content to headless browsers.

**Fixes:**
- The notebook uses a standard Chrome user agent — most sites serve the same content
- Some A/B testing sites may show a different variant
- Try running again — the site might serve a different version

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Made with 🕷️ by [Utsav Vasava](https://github.com/festverse)**

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/festverse/Z-Web-Scraper)
[![Telegram](https://img.shields.io/badge/-Telegram-2CA5E0?style=for-the-badge&logo=Telegram&logoColor=white)](https://telegram.me/festverse)

</div>
