#!/usr/bin/env python3
"""
Module for scraping static product pages using Selenium.
"""
import time
from selenium import webdriver


def scrape_products(url):
    """
    Opens a static product category page and returns product data.

    This function uses Selenium WebDriver to scrape product information
    from a static e-commerce page, extracting title, price, description,
    and rating for each product.

    Args:
        url (str): The product category page URL

    Returns:
        list: A list of product dicts with keys title, price,
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

        products = []

        product_elements = driver.find_elements('class name',
                                                'product-wrapper')

        for product in product_elements:
            title_elem = product.find_element('class name', 'title')
            title = title_elem.get_attribute('title')

            price_elem = product.find_element('class name', 'price')
            price = price_elem.text

            desc_elem = product.find_element('class name', 'description')
            description = desc_elem.text

            ratings_div = product.find_element('class name', 'ratings')
            rating_p = ratings_div.find_element('css selector',
                                                'p[data-rating]')
            rating = int(rating_p.get_attribute('data-rating'))

            products.append({
                'title': title,
                'price': price,
                'description': description,
                'rating': rating
            })

    finally:
        driver.quit()

    return products
