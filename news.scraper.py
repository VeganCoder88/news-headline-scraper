import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML from a news site (example: Hindustan Times)
url = "https://www.hindustantimes.com/latest-news"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Find all news headline tags (adjust as per site structure)
    headlines = soup.find_all('h3')  # Try h2, h3, or headline class

    # Step 3: Extract and clean text
    news_list = []
    for i, headline in enumerate(headlines[:10]):  # Top 10
        title = headline.get_text(strip=True)
        news_list.append(f"{i + 1}. {title}")

    # Step 4: Save to .txt file
    with open("headlines.txt", "w", encoding='utf-8') as file:
        file.write("\n".join(news_list))

    print("✅ Headlines successfully saved to headlines.txt")
else:
    print("❌ Failed to fetch the webpage.")
