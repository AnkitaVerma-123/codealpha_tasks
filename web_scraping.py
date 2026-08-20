import requests
from bs4 import BeautifulSoup
import csv

# ==========================================
# CODEALPHA TASK 1 - WEB SCRAPING
# ==========================================

base_url = "https://quotes.toscrape.com/page/{}/"

all_data = []

# Scrape multiple pages
for page in range(1, 6):

    url = base_url.format(page)

    print(f"Scraping Page {page}...")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Could not access Page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote containers
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:

        text = quote.find(
            "span",
            class_="text"
        ).get_text(strip=True)

        author = quote.find(
            "small",
            class_="author"
        ).get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote.find_all(
                "a",
                class_="tag"
            )
        ]

        all_data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })


# ==========================================
# SAVE SCRAPED DATA
# ==========================================

with open(
    "scraped_quotes.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "Quote",
        "Author",
        "Tags"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(all_data)


# ==========================================
# FINAL RESULTS
# ==========================================

print("\n" + "=" * 50)
print("WEB SCRAPING COMPLETED")
print("=" * 50)

print("Pages Scraped:", 5)
print("Total Quotes Scraped:", len(all_data))
print("Dataset Created: scraped_quotes.csv")

print("\nSample Data:")

for row in all_data[:5]:
    print("\nQuote:", row["Quote"])
    print("Author:", row["Author"])
    print("Tags:", row["Tags"])

print("\n" + "=" * 50)