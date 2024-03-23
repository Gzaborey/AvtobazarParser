import json
import csv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from tqdm import tqdm
from get_links import parse_vehicle_page
from get_links import get_links_from_page
from IPython.display import clear_output


headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"""
}


def main():
    vehicle_data = []
    for page_number in range(1, 3):
        print(f'Iteration: {page_number} started')

        url = f'https://avtobazar.ua/uk/avto/?page={page_number}'
        vehicle_links_on_page = get_links_from_page(url=url, headers=headers)
        print(f'Links collected: {len(vehicle_links_on_page)}')

        for link in tqdm(vehicle_links_on_page, desc='Parsing vehicle pages'):
            vehicle_info = parse_vehicle_page(url=link, headers=headers)
            vehicle_data.append(vehicle_info)

        clear_output(wait=True)

    with open('vehicle_data.json', 'w', encoding='utf-8') as f:
        json.dump(vehicle_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
