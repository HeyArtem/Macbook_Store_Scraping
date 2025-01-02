import requests
from curl import cookies, headers
import os
from bs4 import BeautifulSoup
import json
import csv
import random
import time

"""
    Парсинг магазина Ноутбуки Apple Macbook
    https://mac77.ru/shop/
    (Air, Pro, 12)
"""


def get_data():
    print("\n[INFO] Data collection started!")

    response = requests.get('https://mac77.ru/product-category/macbook/', cookies=cookies, headers=headers)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/index.html", "w") as file:
        file.write(response.text)

    with open(file="data/index.html") as file:
        src = file.read()

    # Создаю объект BeautifulSoup
    soup = BeautifulSoup(src, "lxml")

    # # Переменные для записи в json & csv
    # all_data_json = []
    # all_data_csv = []

    # Собираю url-ссылки на главы (Air, Pro, 12)
    all_chapter = soup.find("ul", class_="products columns-3").find_all("li")
    all_chapter_dict = {}
    for item in all_chapter:
        chapter_item_url = item.find("a").get("href")
        chapter_item_title = item.find("img")["alt"]
        print(chapter_item_title)
        print(chapter_item_url)

        # Запрос к главе
        response = requests.get(url=f"https://mac77.ru/{chapter_item_url}", cookies=cookies, headers=headers)

        # Сохраняю каждую страницу (главу)
        with open(file=f"data/{chapter_item_title}.html", mode="w+") as file:
            file.write(response.text)
        print('[INFO] save! Pause.')

        # пауза между страницами
        time.sleep(random.randrange(2, 4))



    # # Открываю сохраненную главу (вправо сдвинь)
    # with open(file="data/Ноутбуки Macbook Air.html") as file:
    # # with open(file=f"data/{chapter_item_title}.html") as file:
    #     src = file.read()
    #
    # # Создаю объект BeautifulSoup
    # soup = BeautifulSoup(src, "lxml")
    #
    # # Cards
    # all_cards = soup.find("ul", class_="products columns-3")
    # for card in all_cards:
    #     try:
    #         url = card.find('a').get('href')
    #         url_name = str(url).replace("/", "_")
    #         print(url)
    #         print(url_name)
    #
    #     except Exception as ex:
    #         url = None
    #
    #
    #     if url != None:
    #         url_card = f"https://mac77.ru/{url}"
    #
    #         # Иду в карточку
    #         response = requests.get(url=url_card, cookies=cookies, headers=headers)
    #
    #         # Сохраняю карточку
    #         with open(f"data/{url_name}.html", mode="w+") as file:
    #             file.write(response.text)
    #
    #         # пауза между страницами
    #         time.sleep(random.randrange(2, 4))
    #
    #         print('Ok:', url_card)
    #
    #         # # Потрошу карточку
    #         # soup = BeautifulSoup(src, "lxml")









    print("\n[INFO] Data collection and recording completed!")
    return "Hello Python!"


if __name__ == "__main__":
    get_data()
