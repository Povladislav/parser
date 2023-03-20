import requests
from bs4 import BeautifulSoup

from db_management.db_commands import insert_boots_into_db, insert_cloth_into_db
from models.cloth import Cloth

import asyncio
import aiohttp

base_url = "https://www.lamoda.by"


async def get_page_data(session, page, link):
    async with session.get(f"{base_url}{link}&page={page}") as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, "lxml")
        items = soup.find_all("div", class_="x-product-card-description")
        category = soup.find("a", class_="x-link x-link__badgeForeground").text
        for item in items:
            price = item.find(
                "span", class_="x-product-card-description__price-WEB8507_price_no_bold"
            ).text
            name = (
                    item.find("div", class_="x-product-card-description__brand-name").text
                    + item.find(
                "div", class_="x-product-card-description__product-name"
            ).text)

            cloth = {
                "category": category,
                "name": name,
                "price": price,
            }
            validated_object = dict(Cloth.parse_obj(cloth))
            await insert_boots_into_db(validated_object)


async def gather_data():
    page = 1
    tasks = []
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://www.lamoda.by/men-home/")
        main_soup = BeautifulSoup(await response.text(), "lxml")
        for i in range(1, 3):
            link_cloths = main_soup.find_all("a", {"class": "d-header-topmenu-category__link"})[i]
            href = link_cloths.get('href')
            response_from_category = await session.get(f"{base_url}{link_cloths.get('href')}")
            category_soup = BeautifulSoup(await response_from_category.text(), "lxml")
            items = category_soup.find_all("div", class_="x-product-card-description")
            whole_count = int(
                category_soup.find_all("span", class_="x-tree-view-catalog-navigation__found")[
                    1
                ].text)
            if whole_count % len(items) > 0:
                count_of_pages = whole_count // len(items)
            else:
                count_of_pages = whole_count // len(items) + 1
            count_of_pages = 30  # for test
            for page in range(1, count_of_pages + 1):
                task = asyncio.create_task(get_page_data(session, page, href))
                tasks.append(task)
        await  asyncio.gather(*tasks)


def building_base_url():
    response = requests.get("https://www.lamoda.by/men-home/").text
    main_soup = BeautifulSoup(response, "lxml")
    a_links = main_soup.find_all("a", {"class": "d-header-topmenu-category__link"})[1:4]
    return a_links


def build_custom_url_for_boots(page):
    links = building_base_url()
    custom_url = base_url + links[1].get("href") + "sitelink=3" + f"page={page}"
    return custom_url


async def parsing_through_pages_boots():
    page = 1
    custom_url = build_custom_url_for_boots(page)
    response_from_first_category = requests.get(custom_url).text
    category_soup = BeautifulSoup(response_from_first_category, "lxml")
    category = category_soup.find("a", class_="x-link x-link__badgeForeground").text
    items = category_soup.find_all("div", class_="x-product-card-description")
    whole_count = int(
        category_soup.find_all("span", class_="x-tree-view-catalog-navigation__found")[
            1
        ].text
    )
    if whole_count % len(items) > 0:
        count_of_pages = whole_count // len(items)
    else:
        count_of_pages = whole_count // len(items) + 1
    count_of_pages = 3
    for i in range(page, count_of_pages + 1):
        for item in items:
            price = item.find(
                "span", class_="x-product-card-description__price-WEB8507_price_no_bold"
            ).text
            name = (
                    item.find("div", class_="x-product-card-description__brand-name").text
                    + item.find(
                "div", class_="x-product-card-description__product-name"
            ).text
            )
            cloth = {
                "category": category,
                "name": name,
                "price": price,
            }
            validated_object = dict(Cloth.parse_obj(cloth))
            await insert_boots_into_db(validated_object)
            page += 1
            custom_url = build_custom_url_for_boots(page)
            response_from_first_category = requests.get(custom_url).text
            category_soup = BeautifulSoup(response_from_first_category, "lxml")
            category = category_soup.find("a", class_="x-link x-link__badgeForeground").text
            items = category_soup.find_all("div", class_="x-product-card-description")
