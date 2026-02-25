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

    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    service = Service('/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)

        products = []

        product_elements = driver.find_elements(
            By.CLASS_NAME, 'product-wrapper')

        for product in product_elements:
            title_elem = product.find_element(By.CLASS_NAME, 'title')
            title = title_elem.get_attribute('title')

            price_elem = product.find_element(By.CLASS_NAME, 'price')
            price = price_elem.text

            desc_elem = product.find_element(By.CLASS_NAME, 'description')
            description = desc_elem.text

            ratings_div = product.find_element(By.CLASS_NAME, 'ratings')
            rating_p = ratings_div.find_element(
                By.CSS_SELECTOR, 'p[data-rating]')
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
