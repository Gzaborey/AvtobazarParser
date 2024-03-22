import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_links_from_page(url: str, headers: dict) -> list[dict]:
    url = url
    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme

    request = requests.get(url, headers=headers)
    html = request.text

    soup = BeautifulSoup(html, 'lxml')

    vehicle_articles = soup.find_all('div', class_='_2uapD')
    vehicle_links = []

    for article in vehicle_articles:
        title = article.find('div', class_='_1SHqv').find_next(string=True)
        link = f'{scheme}://{netloc}{article.find("a").get("href")}'
        vehicle_links.append(
            {
                'vehicle_title': title,
                'article_link': link
            }
        )
    return vehicle_links
