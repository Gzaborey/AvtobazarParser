import json
import csv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from get_links import parse_vehicle_page


headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
    (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"""
}


def main():
    url = 'https://avtobazar.ua/uk/honda-accord-2014-ivano-frankovsk-1-11223014-1.html'
    vehicle_info = parse_vehicle_page(url=url, headers=headers)
    print(vehicle_info)


if __name__ == '__main__':
    main()
