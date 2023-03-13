import requests
from bs4 import BeautifulSoup

from db_management.db_commands import insert_cloth_into_db

base_url = "https://www.lamoda.by"


def building_base_url():
    response = requests.get("https://www.lamoda.by/men-home/").text
    main_soup = BeautifulSoup(response, "lxml")
    a_links = main_soup.find_all("a", {"class": "d-header-topmenu-category__link"})[1:4]
    return a_links


# def building_custom_url():
#     links = building_base_url()
#     page = 1
#     custom_url = base_url + links[0].get("href") + "sitelink=2" + f'page={page}'
#     response_from_first_category = requests.get(custom_url).text
#     category_soup = BeautifulSoup(response_from_first_category, "lxml")
#     category = category_soup.find("a", class_="x-link x-link__badgeForeground").text
#     items = category_soup.find_all("div", class_="x-product-card-description")
#     whole_count = int(category_soup.find_all("span", class_="x-tree-view-catalog-navigation__found")[1].text)
#     if whole_count % len(items) > 0:
#         count_of_pages = whole_count // len(items)
#     else:
#         count_of_pages = whole_count // len(items) + 1
#     return count_of_pages


def build_custom_url(page):
    links = building_base_url()
    custom_url = base_url + links[0].get("href") + "sitelink=2" + f"page={page}"
    return custom_url


async def parsing_through_pages_cloths():
    page = 1
    custom_url = build_custom_url(page)
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
    for i in range(page, count_of_pages):
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
            await insert_cloth_into_db(cloth)
        page += 1
        custom_url = build_custom_url(page)
        response_from_first_category = requests.get(custom_url).text
        category_soup = BeautifulSoup(response_from_first_category, "lxml")
        category = category_soup.find("a", class_="x-link x-link__badgeForeground").text
        items = category_soup.find_all("div", class_="x-product-card-description")


parsing_through_pages_cloths()
