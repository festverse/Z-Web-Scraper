# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Active support  |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT** open a public GitHub issue
2. Email the maintainer directly or use GitHub's private vulnerability reporting
3. Include a detailed description and steps to reproduce

## Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial assessment**: Within 1 week
- **Fix or mitigation**: Within 2 weeks

## Scope

This policy covers the Z-Web-Scraper repository, the Colab notebook, and the `src/` package.

### What We Don't Do

- Store credentials or tokens
- Make outbound network requests (beyond the target URL)
- Execute arbitrary code from scraped pages
- Persist data beyond the Colab session

## Best Practices for Users

- Only scrape websites you have permission to scrape
- Respect robots.txt and terms of service
- Do not use this tool for unauthorized data collection
- Be mindful of rate limiting and server load

Thank you for helping keep Z-Web-Scraper secure!
