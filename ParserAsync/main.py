import numpy as np
from ParserSync.get_links import get_last_page_number
import asyncio
import time
import json
from get_links import get_vehicle_data


def main():
    headers = {
        "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36""",
        "Accept": "*/*"
    }
    url = f'https://avtobazar.ua/uk/avto/?page=1&period=month'
    last_page_number = get_last_page_number(url=url, headers=headers)

    for page_number in range(1, last_page_number + 1):
        print(f'Iteration: {page_number} started')

        try:
            url = f'https://avtobazar.ua/uk/avto/?page={page_number}&period=month'
            vehicle_data = asyncio.run(get_vehicle_data(url=url, headers=headers))
        except AttributeError:
            print('Something went wrong on this iteration!')
            continue

        with open(f'D:/Projects/Programming/AvtobazarParser/data/vehicle_data_last_month/vehicle_data_page{page_number}.json',
                  'w', encoding='utf-8') as f:
            json.dump(vehicle_data, f, indent=4, ensure_ascii=False)

        time.sleep(np.random.randint(2, 4))


if __name__ == '__main__':
    start_time = time.time()
    main()
    finish_time = time.time() - start_time
    print(f'Time spent: {finish_time}')
