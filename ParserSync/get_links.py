import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re


def get_last_page_number(url: str, headers: dict) -> int:
    request = requests.get(url=url, headers=headers)
    html = request.text
    soup = BeautifulSoup(html, 'lxml')
    last_page_number = soup.find('ul', class_='UXnXg').find_all('li')[-2].text
    return int(last_page_number)


def get_links_from_page(url: str, headers: dict) -> list[str]:
    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme

    request = requests.get(url=url, headers=headers)

    html = request.text
    soup = BeautifulSoup(html, 'lxml')

    vehicle_links_list = []
    vehicle_articles = soup.find_all('div', class_='_2uapD')
    for article in vehicle_articles:
        link = f'{scheme}://{netloc}{article.find("a").get("href")}'
        vehicle_links_list.append(link)
    return vehicle_links_list


def parse_vehicle_page(url: str, headers: dict) -> dict:
    request = requests.get(url=url, headers=headers)

    html = request.text
    soup = BeautifulSoup(html, 'lxml')

    vehicle_info_dict = {}

    try:
        vehicle_title = soup.find('div', class_='_32c5u').text
        vehicle_info_dict['title'] = vehicle_title.strip()
    except AttributeError:
        vehicle_info_dict['title'] = 'No title'

    try:
        vehicle_price = soup.find('div', class_='_2izCF').text
        vehicle_price = re.sub(r'\D', '', vehicle_price)
        vehicle_info_dict['price'] = vehicle_price.strip()
    except AttributeError:
        vehicle_info_dict['price'] = 'Unknown price'

    vehicle_card = soup.find_all('div', class_='heJ1W')
    for category in vehicle_card:
        vehicle_info_dict[list(category.children)[0].text] = list(category.children)[1].text.strip()
    return vehicle_info_dict
