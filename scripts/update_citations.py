import requests
from bs4 import BeautifulSoup
import yaml
import os

# Scholar Profile URL (수정 필요)
SCHOLAR_URL = "https://scholar.google.com/citations?user=YOUR_USER_ID"
DATA_FILE = "_data/citations.yml"

def get_citation_count_for_title(title, url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    citation_counts = soup.find_all('a', class_='gsc_a_ac')

    titles = soup.find_all('a', class_='gsc_a_at')
    
    for t, count in zip(titles, citation_counts):
        if title.lower() in t.text.lower():
            return count.text.strip() if count.text.strip() != '' else '0'
    return '0'

def update_citations():
    # Load data
    if not os.path.exists(DATA_FILE):
        print(f"Data file {DATA_FILE} not found.")
        return

    with open(DATA_FILE, "r") as file:
        data = yaml.safe_load(file)

    # Update citation counts
    for pub in data["publications"]:
        title = pub["title"]
        citation_count = get_citation_count_for_title(title, SCHOLAR_URL)
        pub["citation_count"] = citation_count
        print(f"Updated {title}: {citation_count} citations")

    # Save updated data
    with open(DATA_FILE, "w") as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    update_citations()
