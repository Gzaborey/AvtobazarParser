import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_links_from_page(url: str, headers: dict) -> list[str]:
    netloc = urlparse(url).netloc
    scheme = urlparse(url).scheme

    request = requests.get(url, headers=headers)

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

    vehicle_title = soup.find('div', class_='_32c5u').text
    vehicle_info_dict['title'] = vehicle_title

    vehicle_price = soup.find('div', class_='_2izCF').text
    vehicle_info_dict['price'] = vehicle_price

    vehicle_location = soup.find('span', class_='_27p5n').text
    vehicle_info_dict['location'] = vehicle_location

    vehicle_card = soup.find_all('div', class_='heJ1W')
    for category in vehicle_card:
        vehicle_info_dict[list(category.children)[0].text] = list(category.children)[1].text

    return vehicle_info_dict
