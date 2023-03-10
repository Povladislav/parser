import requests
from bs4 import BeautifulSoup

from db_management.db_commands import insert_cloth_into_db

base_url = "https://www.lamoda.by"


def building_base_url():
    response = requests.get("https://www.lamoda.by/men-home/").text
    main_soup = BeautifulSoup(response, "lxml")
    a_links = main_soup.find_all("a", {"class": "d-header-topmenu-category__link"})[1:4]
    return a_links


async def parsing_through_pages_cloths():
    links = building_base_url()
    custom_url = base_url + links[0].get("href")
    response_from_first_category = requests.get(custom_url).text
    category_soup = BeautifulSoup(response_from_first_category, "lxml")
    category = category_soup.find("a", class_="x-link x-link__badgeForeground").text
    catalog = category_soup.find("div", class_="grid__catalog")
    a_s = catalog.find_all("a")
    for a in a_s:
        response_from_detail_information = requests.get(base_url + a.get("href")).text
        detail_soup = BeautifulSoup(response_from_detail_information, "lxml")

        object = detail_soup.find(
            "div", class_="x-premium-product-title__model-name"
        ).text
        price = detail_soup.find("span", class_="x-premium-product-prices__price").text
        cloth = {
            "category": category,
            "name": object,
            "price": price,
        }
        await insert_cloth_into_db(cloth)
