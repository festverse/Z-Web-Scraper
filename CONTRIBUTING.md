# Contributing to Z-Web-Scraper

Thank you for your interest in contributing!

---

## Ways to Contribute

### 🐛 Report Bugs
[Open an Issue](https://github.com/festverse/Z-Web-Scraper/issues) with steps to reproduce, expected vs actual behavior, and your environment.

### 💡 Suggest Features
[Start a Discussion](https://github.com/festverse/Z-Web-Scraper/issues) with what problem it solves and how it should work.

### 🔀 Submit Code
1. **Fork** the repository
2. **Clone**: `git clone https://github.com/YOUR_USERNAME/Z-Web-Scraper.git`
3. **Branch**: `git checkout -b feature/your-feature`
4. **Make changes** and test in Colab
5. **Commit**: `git commit -m "feat: description"`
6. **Push** and open a **Pull Request**

---

## Development Setup

```bash
git clone https://github.com/festverse/Z-Web-Scraper.git
cd Z-Web-Scraper
pip install -r requirements.txt
```

## Code Style

- Follow existing `src/` module patterns
- Use shared UI helpers from `src/ui.py`
- Add docstrings to all public functions
- Add section markers (`# ---- SECTION NAME ----`)
- Keep `__all__` exports updated in `__init__.py`
- Update `CHANGELOG.md` with every change (newest at top)

## Commit Messages

- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation only
- `refactor:` — code restructure

## Testing

Test all changes in Google Colab before submitting:
1. Open the notebook
2. Run all 3 cells with a test URL
3. Verify HTML capture, metadata, and export work
4. Check both light and dark mode rendering
