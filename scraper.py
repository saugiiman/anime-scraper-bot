import requests
from bs4 import BeautifulSoup
import json

def scrape_anime_episodes(anime_url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(anime_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        episode_tags = soup.find_all("a", class_="episode-link")  # Change this based on real site

        episodes = []
        for tag in episode_tags:
            title = tag.get_text(strip=True)
            link = tag.get("href")
            episodes.append({
                "title": title,
                "link": link
            })

        return episodes

    except Exception as e:
        print("Error:", e)
        return []

# 📝 Replace this URL with a real anime site
anime_url = "https://exampleanime.com/anime/naruto"
episodes = scrape_anime_episodes(anime_url)

# Save result
with open("episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes, f, indent=2, ensure_ascii=False)

print("Scraped episodes:")
for ep in episodes:
    print(f"{ep['title']}: {ep['link']}")
