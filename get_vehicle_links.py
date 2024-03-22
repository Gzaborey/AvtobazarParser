import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urlparse
import time
import numpy as np
import csv


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

vehicle_links = []

for page_num in range(1, 501):
    print(f'Iteration #{page_num}')
    url = f'https://avtobazar.ua/uk/avto/?capacityUnit=1&currency=usd&make=-1&page={page_num}&powerUnit=1&transport=1'

    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme

    request = requests.get(url, headers=headers)
    html = request.text

    soup = BeautifulSoup(html, 'lxml')

    vehicle_articles = soup.find_all('div', class_='_2uapD')

    for article in vehicle_articles:
        title = article.find('div', class_='_1SHqv').find_next(string=True)
        link = f'{scheme}://{netloc}{article.find("a").get("href")}'
        vehicle_links.append(
            {
                'vehicle_title': title,
                'article_link': link
            }
        )

    time.sleep(np.random.randint(2, 4))

with open('vehicle_links.json', 'a', encoding='utf-8') as f:
    json.dump(vehicle_links, f, indent=4, ensure_ascii=False)


def get_links(url: str) -> list[str]:
    url = url

    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme

    request = requests.get(url, headers=headers)
    html = request.text

    soup = BeautifulSoup(html, 'lxml')

    vehicle_articles = soup.find_all('div', class_='_2uapD')

    for article in vehicle_articles:
        title = article.find('div', class_='_1SHqv').find_next(string=True)
        link = f'{scheme}://{netloc}{article.find("a").get("href")}'
        vehicle_links.append(
            {
                'vehicle_title': title,
                'article_link': link
            }
        )

    return
