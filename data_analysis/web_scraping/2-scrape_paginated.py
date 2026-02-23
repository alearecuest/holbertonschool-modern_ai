#!/usr/bin/env python3
"""
Module for handling paginated web scraping.
"""
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin


fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """
    Follows Next links on quotes.toscrape.com until no more pages remain.

    This function scrapes all pages by detecting and following the next
    page link dynamically. It implements polite delays between requests
    and combines results from all pages.

    Args:
        base_url (str): The first page URL

    Returns:
        list: The full list of quote dicts from all pages,
              same format as scrape_basic
    """
    all_quotes = []
    current_url = base_url

    while current_url:
        quotes = scrape_basic(current_url)
        all_quotes.extend(quotes)

        html = fetch_html(current_url)
        soup = BeautifulSoup(html, 'html.parser')

        next_li = soup.find('li', class_='next')

        if next_li:
            next_link = next_li.find('a')
            if next_link and next_link.get('href'):
                next_href = next_link.get('href')
                current_url = urljoin(base_url, next_href)
                time.sleep(1)
            else:
                current_url = None
        else:
            current_url = None

    return all_quotes
