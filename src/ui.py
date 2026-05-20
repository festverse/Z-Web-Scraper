"""
Z-Web-Scraper — UI helpers for Colab notebook.
Theme-safe inline-styled HTML components (works in both dark/light mode).
"""

from IPython.display import display, HTML
from .config import (
    BG_CARD, BG_INNER, BORDER, TEXT, TEXT_DIM, TEXT_MUTED,
    FONT, MONO, C_OK, C_WARN, C_ERR, C_INFO, C_STEP,
)

__all__ = [
    "show_header",
    "show_ok",
    "show_warn",
    "show_err",
    "show_info",
    "show_step",
    "show_stats",
    "show_html_preview",
    "show_links_table",
    "show_meta_tags",
]


# ── Internal helpers ──

def _card(inner: str) -> str:
    return (
        f'<div style="background:{BG_CARD};border:1px solid {BORDER};'
        f'border-radius:16px;padding:2px;margin:14px 0">'
        f'<div style="background:{BG_INNER};border-radius:14px;padding:24px">{inner}</div></div>'
    )


def _header(icon: str, title: str, sub: str = "") -> str:
    sub_h = (
        f'<div style="{FONT};font-size:12.5px;color:{TEXT_DIM};margin-top:2px">{sub}</div>'
        if sub else ""
    )
    return (
        f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;'
        f'padding-bottom:14px;border-bottom:2px solid {BORDER}">'
        f'<div style="width:44px;height:44px;display:flex;align-items:center;justify-content:center;'
        f'background:linear-gradient(135deg,#667eea,#764ba2);border-radius:12px;font-size:22px">{icon}</div>'
        f'<div><div style="{FONT};font-size:20px;font-weight:700;color:{TEXT}">{title}</div>{sub_h}</div></div>'
    )


def _row(msg: str, colors: tuple, icon: str = "") -> str:
    b, bg, t = colors
    return (
        f'<div style="display:flex;align-items:center;gap:10px;padding:10px 14px;margin:6px 0;'
        f'border-radius:10px;border-left:3px solid {b};background:{bg};color:{t};'
        f'{MONO};font-size:13.5px">{icon} {msg}</div>'
    )


def _stat_card(icon: str, label: str, value: str, color: str = "#667eea") -> str:
    return (
        f'<div style="text-align:center;padding:16px 12px;background:{BG_INNER};'
        f'border:1px solid {BORDER};border-radius:12px;min-width:120px;flex:1">'
        f'<div style="font-size:24px;margin-bottom:6px">{icon}</div>'
        f'<div style="{FONT};font-size:22px;font-weight:700;color:{color}">{value}</div>'
        f'<div style="{FONT};font-size:11px;color:{TEXT_MUTED};margin-top:2px">{label}</div></div>'
    )


def _escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ── Public API ──

def show_header(icon: str, title: str, sub: str = ""):
    """Show a styled section header card."""
    display(HTML(_card(_header(icon, title, sub))))


def show_ok(msg: str, icon: str = "✅"):
    display(HTML(_row(msg, C_OK, icon)))


def show_warn(msg: str, icon: str = "⚠️"):
    display(HTML(_row(msg, C_WARN, icon)))


def show_err(msg: str, icon: str = "❌"):
    display(HTML(_row(msg, C_ERR, icon)))


def show_info(msg: str, icon: str = "ℹ️"):
    display(HTML(_row(msg, C_INFO, icon)))


def show_step(msg: str, icon: str = "🔹"):
    display(HTML(_row(msg, C_STEP, icon)))


def show_stats(stats: list[tuple]):
    """Show a row of stat cards. Each tuple: (icon, label, value, color)."""
    cards = "".join(_stat_card(*s) for s in stats)
    display(HTML(
        f'<div style="display:flex;gap:10px;flex-wrap:wrap;margin:14px 0">{cards}</div>'
    ))


def show_html_preview(html: str, max_chars: int = 5000):
    """Show a truncated preview of the HTML source."""
    truncated = len(html) > max_chars
    preview = html[:max_chars]
    if truncated:
        preview += f"\n\n<!-- ... truncated ({len(html):,} total chars) ... -->"

    escaped = _escape(preview)
    display(HTML(
        f'<div style="margin:14px 0">'
        f'<div style="{FONT};font-size:13px;font-weight:600;color:{TEXT};margin-bottom:8px">'
        f'📄 HTML Preview {"(truncated)" if truncated else "(full)"}</div>'
        f'<pre style="background:#1e1e2e;color:#d4d4d4;padding:16px;border-radius:12px;'
        f'overflow-x:auto;font-size:12px;max-height:400px;overflow-y:auto">'
        f'<code>{escaped}</code></pre></div>'
    ))


def show_links_table(links: list[dict], max_rows: int = 30):
    """Show links in a compact table."""
    if not links:
        show_info("No links found")
        return

    rows = ""
    for i, lnk in enumerate(links[:max_rows]):
        text = _escape(lnk["text"] or "(no text)")
        url = _escape(lnk["url"])
        rows += (
            f'<tr style="border-bottom:1px solid {BORDER}">'
            f'<td style="padding:6px 10px;font-size:12px;color:{TEXT_DIM}">{i+1}</td>'
            f'<td style="padding:6px 10px;font-size:12px;color:{TEXT};max-width:200px;'
            f'overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{text}</td>'
            f'<td style="padding:6px 10px;font-size:11px;{MONO};color:#2563eb;'
            f'max-width:350px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'
            f'<a href="{url}" target="_blank">{url}</a></td></tr>'
        )

    extra = (
        f"<div style='{FONT};font-size:11px;color:{TEXT_MUTED};margin-top:6px'>"
        f"... and {len(links) - max_rows} more links</div>"
        if len(links) > max_rows else ""
    )

    display(HTML(
        f'<div style="margin:14px 0">'
        f'<div style="{FONT};font-size:13px;font-weight:600;color:{TEXT};margin-bottom:8px">'
        f'🔗 Links ({len(links)} found)</div>'
        f'<div style="overflow-x:auto">'
        f'<table style="width:100%;border-collapse:collapse;border:1px solid {BORDER};border-radius:8px">'
        f'<thead><tr style="background:{BG_CARD}">'
        f'<th style="padding:8px 10px;text-align:left;font-size:11px;color:{TEXT_MUTED}">#</th>'
        f'<th style="padding:8px 10px;text-align:left;font-size:11px;color:{TEXT_MUTED}">Text</th>'
        f'<th style="padding:8px 10px;text-align:left;font-size:11px;color:{TEXT_MUTED}">URL</th>'
        f'</tr></thead><tbody>{rows}</tbody></table></div>{extra}</div>'
    ))


def show_meta_tags(meta_tags: dict, important_keys: list[str] | None = None):
    """Show key meta tags in a table."""
    if not meta_tags:
        return

    if important_keys is None:
        important_keys = [
            "og:title", "og:description", "og:image", "og:url", "og:type",
            "twitter:card", "twitter:title", "twitter:description",
            "description", "keywords", "author", "viewport", "robots",
        ]

    shown = {k: v for k, v in meta_tags.items() if k in important_keys}
    if not shown:
        return

    rows = ""
    for k, v in shown.items():
        rows += (
            f'<tr style="border-bottom:1px solid {BORDER}">'
            f'<td style="padding:6px 10px;font-size:12px;{MONO};color:#7c3aed;font-weight:600">'
            f'{_escape(k)}</td>'
            f'<td style="padding:6px 10px;font-size:12px;color:{TEXT};max-width:400px;'
            f'overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'
            f'{_escape(v[:200])}</td></tr>'
        )

    display(HTML(
        f'<div style="margin:14px 0">'
        f'<div style="{FONT};font-size:13px;font-weight:600;color:{TEXT};margin-bottom:8px">'
        f'🏷️ Key Meta Tags</div>'
        f'<table style="width:100%;border-collapse:collapse;border:1px solid {BORDER};border-radius:8px">'
        f'<thead><tr style="background:{BG_CARD}">'
        f'<th style="padding:8px 10px;text-align:left;font-size:11px;color:{TEXT_MUTED}">Tag</th>'
        f'<th style="padding:8px 10px;text-align:left;font-size:11px;color:{TEXT_MUTED}">Value</th>'
        f'</tr></thead><tbody>{rows}</tbody></table></div>'
    ))
