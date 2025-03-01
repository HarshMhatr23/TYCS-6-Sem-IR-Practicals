import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://www.Amazon.in"

visited_urls = set()

urls_to_visit = [base_url]

def crawl_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content,"html.parser")

        links = []
        for link in soup.find_all("a",href= True):
            next_url = urljoin(url,link["href"])
            links.append(next_url)

        return links

    except requests.exceptions.RequestException as e:
         print(f"Error crawling {url}:{e}")
         return []

while urls_to_visit:
    current_url = urls_to_visit.pop(0)

    if current_url in visited_urls:
        continue
    print(f"Crawling: {current_url}")

    new_links = crawl_page(current_url)
    visited_urls.add(current_url)
    urls_to_visit.extend(new_links)
print("Crawling Finished")
