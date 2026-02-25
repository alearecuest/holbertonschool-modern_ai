#!/usr/bin/env python3
"""
Module for scraping infinite-scroll pages using Selenium.
"""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Scrolls and extracts all products from a JS-rendered infinite-scroll page.

    This function scrolls to the bottom repeatedly until no more content loads,
    then extracts all unique products from the page.

    Args:
        url (str): The infinite-scroll page URL
        scroll_pause (float): Seconds to wait between scrolls (default: 2.0)

    Returns:
        list: A list of unique product dicts with keys title, price,
              description, and rating
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    service = webdriver.chrome.service.Service(
        executable_path='/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)

        time.sleep(scroll_pause)

        last_height = driver.execute_script(
            "return document.body.scrollHeight")

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(scroll_pause)

            new_height = driver.execute_script(
                "return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        products = []
        seen = set()

        product_elements = driver.find_elements('class name', 'thumbnail')

        for product in product_elements:
            title_elem = product.find_element('class name', 'title')
            title = title_elem.get_attribute('title')

            price_elem = product.find_element('class name', 'price')
            price = price_elem.text

            key = (title, price)
            if key in seen:
                continue
            seen.add(key)

            desc_elem = product.find_element('class name', 'description')
            description = desc_elem.text

            ratings_div = product.find_element('class name', 'ratings')
            stars = ratings_div.find_elements('css selector',
                                              'span.ws-icon-star')
            rating = len(stars)

            products.append({
                'title': title,
                'price': price,
                'description': description,
                'rating': rating
            })

    finally:
        driver.quit()

    return products
