#!/usr/bin/env python3
"""
Module for API-based web scraping.
"""
import json


fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """
    Fetches quote data from all Quotes API pages.

    This function iterates through paginated API endpoints, starting from
    page 1, and extracts quote information from JSON responses. It continues
    until no more quotes are available.

    Args:
        base_url (str): The root URL of the site

    Returns:
        list: A list of quote dicts, each with keys text, author, and tags
    """
    all_quotes = []
    page = 1
    has_next = True

    while has_next:
        api_url = f"{base_url}/api/quotes?page={page}"

        response = fetch_html(api_url)

        data = json.loads(response)

        quotes = data.get('quotes', [])

        if not quotes:
            has_next = False
        else:
            for quote in quotes:
                all_quotes.append({
                    'text': quote.get('text', ''),
                    'author': quote.get('author', {}).get('name', ''),
                    'tags': quote.get('tags', [])
                })

            has_next = data.get('has_next', False)
            page += 1

    return all_quotes
