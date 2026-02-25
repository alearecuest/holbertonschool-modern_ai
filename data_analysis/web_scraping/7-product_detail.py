#!/usr/bin/env python3
"""
Module for scraping product detail pages using Selenium.
"""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """
    Opens a detail page for one product and returns product data.

    This function uses Selenium WebDriver to scrape a single product's
    detail page, waiting for the specified delay before extraction.

    Args:
        url (str): The product detail page URL
        delay (float): Seconds to wait before scraping (default: 2.0)

    Returns:
        dict: A product dict with keys title, price, description, and rating
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

        time.sleep(delay)

        caption = driver.find_element('class name', 'caption')

        h4_elements = caption.find_elements('tag name', 'h4')
        title = h4_elements[1].text

        price_elem = caption.find_element('css selector', 'h4.price')
        price = price_elem.text

        desc_elem = driver.find_element('class name', 'description')
        description = desc_elem.text

        ratings_div = driver.find_element('class name', 'ratings')
        stars = ratings_div.find_elements('css selector',
                                          'span.ws-icon-star')
        rating = len(stars)

        return {
            'title': title,
            'price': price,
            'description': description,
            'rating': rating
        }

    finally:
        driver.quit()
