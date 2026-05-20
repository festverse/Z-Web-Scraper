# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.5] - 2026-05-17

### Fixed
- Auto-scroll now detects new DOM elements (img, a, video) instead of just scrollHeight change
- Stops after 3 consecutive scrolls with no new elements (was breaking on infinite-scroll sites)
- Increased pause between scrolls to 1.5s for lazy content to load

### Changed
- Timeout max increased to 300s (was 120s)
- Wait after load max increased to 60s (was 30s)
- Notebook now uses repo src/ modules directly (zero code duplication)
- Cell 2 calls scrape_url() from src/scraper.py with progress callback
- Repo auto-pulls latest on re-run (git pull)
- Upgraded notebook header with capsule-render banner, gradient cards, hover effects, dark mode
- src/scraper.py: added callback parameter for progress events
- src/scraper.py: exported _build_driver() for notebook Selenium test

## [1.0.4] - 2026-05-17

### Changed
- Rewrote GUIDE.md to match ZImagePro style — beginner-friendly, step-by-step format
- Added "What Is This?" section with plain English explanations (Notebook, Colab, Selenium)
- Added "What You Need" requirements table with "you do NOT need" callout
- Added "Getting Started" with direct Colab link
- Added detailed Step 1/2/3 walkthroughs with "What You'll See" output examples
- Added "All Settings Explained" with detailed parameter tables
- Added "Site Type Guide" with per-site-type settings recommendations
- Added "Common Custom JS Examples" table
- Added "Where Are My Files?" with Colab file browser paths
- Added FAQ with <details> blocks
- Added "Common Problems & Fixes" with cause + fix for each error
- Added footer with GitHub and Telegram badges

## [1.0.3] - 2026-05-17

### Fixed
- Removed unused imports: `expected_conditions`, `urlparse`, `MAX_PAGE_SIZE_MB` from scraper.py
- Fixed fragile User-Agent extraction — now uses `USER_AGENT` constant directly from config
- Fixed `html` module import order in notebook — imported at top of Cell 2, not inside conditional block
- Fixed `_build_driver` timeout — now accepts `timeout` parameter instead of using only default
- Removed unused constants `DEFAULT_HTML_FILE` and `DEFAULT_JSON_FILE` from config.py

### Changed
- Notebook now imports all UI functions from `src/ui.py` — zero code duplication across cells
- Added `show_meta_tags()` to `src/ui.py` — meta tag display is now a shared function
- Added `__all__` exports to `src/scraper.py`, `src/ui.py`, and `src/__init__.py`
- Added `webdriver-manager` to `requirements.txt` for portable driver setup
- Removed `*.html` from `.gitignore` — only `*.zip` blocked now
- All 3 notebook cells now import from `src/` package via repo clone
- Notebook clones repo at startup for `src/` package availability

## [1.0.2] - 2026-05-17

### Changed
- README footer: added AniPay banner, Telegram/Instagram/Gmail badges, copyright notice
- CONTRIBUTING.md: added commit message conventions, code style guidelines, testing section
- SECURITY.md: added supported versions table, response timeline, scope details

## [1.0.1] - 2026-05-17

### Fixed
- Auto-detect Chromium and ChromeDriver paths for Colab — scans multiple known paths
- Falls back to `shutil.which()` and `find` command for driver discovery
- Saves detected paths to `/tmp` for Step 2 re-use
- Quick Selenium verification test in Step 1

## [1.0.0] - 2026-05-17

### Added
- Initial release of Z-Web-Scraper
- Full-page web scraper using Selenium + headless Chromium
- `notebook/Z-Web-Scraper.ipynb` — 3-cell Colab notebook with inline-styled UI
- `src/config.py` — constants, Chrome options, UI theme tokens
- `src/scraper.py` — core scraping engine with auto-scroll, metadata extraction
- `src/ui.py` — theme-safe Colab UI components (cards, stats, tables)
- JavaScript-heavy site support (Next.js, React, Vue, Angular, Nuxt)
- Auto-scroll for lazy-loaded content
- Custom JavaScript execution after page load
- Configurable timeout and wait-after-load settings
- HTML preview with syntax highlighting
- Link extraction with text and resolved URLs
- Image extraction with alt text and dimensions
- Meta tag extraction (Open Graph, Twitter Cards, description, keywords)
- Metadata export as JSON alongside HTML
- ZIP download for all scraped files
- Content hash for deduplication
- Redirect detection and reporting
- Comprehensive README with architecture, badges, FAQ
- CHANGELOG.md — version history tracking
- CONTRIBUTING.md — contribution guidelines
- GUIDE.md — beginner-friendly user guide
- SECURITY.md — vulnerability reporting policy
- .github/ISSUE_TEMPLATE/ — bug report and feature request templates
- .github/PULL_REQUEST_TEMPLATE.md — PR checklist
- .gitignore — Python, Jupyter, output files, OS artifacts
- requirements.txt — core dependencies
- LICENSE — MIT license
