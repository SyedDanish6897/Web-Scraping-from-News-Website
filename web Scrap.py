
import requests
from bs4 import BeautifulSoup

# Website to scrape (Times of India Briefs)
url = "https://timesofindia.indiatimes.com/briefs"

# Pretend to be a real browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Get the page
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find actual headlines (inside div.brief_box > h2 > a)
    headline_tags = soup.select("div.brief_box h2 a")
    
    # only 10 headlines
    headlines = [tag.get_text(strip=True) for tag in headline_tags[:10]]
    
    # Save to file
    with open("news_headlines.txt", "w", encoding="utf-8") as file:
        for news in headlines:
            file.write(news + "\n")
    
    # Show result
    print(" Headlines found:")
    for news in headlines:
        print("-", news)
    
    print("\n 10 headlines saved to news_headlines.txt")
else:
    print(" Failed to fetch the website")
