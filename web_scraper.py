import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://news.ycombinator.com/"

# Fetch the HTML content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines
    headlines = []
    for item in soup.find_all("a", class_="storylink"):
        headlines.append(item.text)

    # Save data to a CSV file
    df = pd.DataFrame({"Headline": headlines})
    df.to_csv("news_headlines.csv", index=False)
    print("Data scraped and saved to news_headlines.csv")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
