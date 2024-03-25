import json
from tqdm import tqdm
from ParserSync.get_links import parse_vehicle_page
from ParserSync.get_links import get_links_from_page
from ParserSync.get_links import get_last_page_number
from IPython.display import clear_output
import time


def main():
    headers = {
        "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36""",
        "Accept": "*/*"
    }
    url = f'https://avtobazar.ua/uk/avto/?page=1'

    vehicle_data = []
    last_page_number = get_last_page_number(url=url, headers=headers)
    for page_number in range(1, last_page_number + 1):
        print(f'Iteration: {page_number} started')

        try:
            url = f'https://avtobazar.ua/uk/avto/?page={page_number}'
            vehicle_links_on_page = get_links_from_page(url=url, headers=headers)
            print(f'Links collected: {len(vehicle_links_on_page)}')
        except AttributeError:
            print('Something went wrong on this iteration!')
            continue

        for link in tqdm(vehicle_links_on_page, desc='Parsing vehicle pages'):
            vehicle_info = parse_vehicle_page(url=link, headers=headers)
            vehicle_data.append(vehicle_info)

        clear_output(wait=True)

    with open('D:/Projects/Programming/AvtobazarParser/data/vehicle_data.json',
              'w', encoding='utf-8') as f:
        json.dump(vehicle_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    start_time = time.time()
    main()
    finish_time = time.time() - start_time
    print(f'Time spent: {finish_time}')
