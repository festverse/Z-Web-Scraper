"""
Z-Web-Scraper — Configuration and constants.
"""

# ── Defaults ──
DEFAULT_TIMEOUT = 30          # seconds to wait for page load (max: 300)
DEFAULT_WAIT_AFTER_LOAD = 3   # extra seconds for JS to settle (max: 60)
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)

# ── Chromium / Selenium ──
CHROMIUM_VERSION = "131.0.6778.204"
CHROME_OPTIONS = [
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--single-process",
    "--no-zygote",
    "--window-size=1920,1080",
    f"--user-agent={USER_AGENT}",
]

# ── Output ──
DEFAULT_OUTPUT_DIR = "/content/Z-Web-Scraper_output"

# ── UI Theme (matches ZImageUpscaler style) ──
BG_CARD = "#f4f5f7"
BG_INNER = "#ffffff"
BORDER = "#dde1e8"
TEXT = "#2c2c3a"
TEXT_DIM = "#6b7280"
TEXT_MUTED = "#9ca3af"
FONT = "font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif"
MONO = "font-family:'SF Mono',SFMono-Regular,Consolas,monospace"
C_OK = ("#16a34a", "#f0fdf4", "#15803d")
C_WARN = ("#d97706", "#fffbeb", "#92400e")
C_ERR = ("#dc2626", "#fef2f2", "#991b1b")
C_INFO = ("#2563eb", "#eff6ff", "#1e40af")
C_STEP = ("#7c3aed", "#f5f3ff", "#5b21b6")
