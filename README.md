# Book Price Scraper

A Python web scraper that extracts book titles, prices, and ratings 
from an e-commerce-style site, handling pagination across all pages 
automatically.

## Features
- Scrapes all pages via pagination (tested on 1000+ items across 50 pages)
- Retry logic for failed requests (handles timeouts, connection errors)
- Graceful handling of malformed/missing data per item
- Exports clean, structured CSV output
- Rate-limited requests (polite to target servers)

## Tech stack
Python, Requests, BeautifulSoup4, pandas

## Usage
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 scraper.py
\`\`\`
