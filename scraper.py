import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

base_url = "http://books.toscrape.com/"
url = base_url
data = []
max_retries = 3

while url:
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # raises an error if status is 4xx/5xx
            break  # success, exit retry loop
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for {url}: {e}")
            if attempt == max_retries - 1:
                print(f"Giving up on {url} after {max_retries} attempts.")
                url = None  # stop the whole scrape
                break
            time.sleep(2)  # wait before retrying

    if url is None:
        break

    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")

    books = soup.find_all("article", class_="product_pod")
    for book in books:
        try:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating_tag = book.find("p", class_="star-rating")
            rating = rating_tag["class"][1]
            data.append({"title": title, "price": price, "rating": rating})
        except (AttributeError, IndexError, TypeError) as e:
            print(f"Skipping a malformed book entry: {e}")
            continue  # skip this one book, keep going with the rest

    next_link = soup.find("li", class_="next")
    if next_link:
        next_href = next_link.a["href"]
        url = urljoin(url, next_href)
    else:
        url = None

    print(f"Scraped {len(books)} books, total so far: {len(data)}")
    time.sleep(0.5)  # small delay between requests, polite to the server

df = pd.DataFrame(data)
df.to_csv("books_all_pages.csv", index=False)
print(f"Done. Saved {len(df)} books to books_all_pages.csv")