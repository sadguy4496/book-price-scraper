# Book Price Scraper

A Python scraper that collects book titles, prices, and ratings from an
e-commerce-style site and exports them to a clean CSV. Useful for price
monitoring, building datasets, or tracking changes over time.

Built against [books.toscrape.com](https://books.toscrape.com), a practice
site made for scraping.

## Features
- Scrapes every page via pagination (tested on 1000+ items across 50 pages)
- Retry logic for timeouts and connection errors
- Skips or flags malformed and missing data per item without crashing
- Exports structured CSV output
- Rate-limited requests to stay polite to servers

## Sample output

| title | price | rating |
|-------|-------|--------|
| A Light in the Attic | 51.77 | 3 |
| Tipping the Velvet | 53.74 | 1 |
| Soumission | 50.10 | 1 |

(Replace these rows with your real output, or add a screenshot.)

## Tech stack
Python, Requests, BeautifulSoup4, pandas

## Usage
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 scraper.py
```

Results are saved to `books.csv`.

## Possible extensions
Price-change alerts, Excel export, scheduled runs, and delivery by email or
Google Sheets.
