#!/usr/bin/env python3
"""
Module for extracting quotes from JSON-LD structured data.
"""
import json
import bs4


fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """
    Pulls quotes from embedded JSON-LD on a page.

    This function fetches HTML content, locates all script blocks with
    type application/ld+json, parses each as JSON, and extracts quote
    information from objects with @type Quote.

    Args:
        url (str): The Quotes List endpoint URL

    Returns:
        list: A list of quote dicts, each with keys text, author, and tags
    """

    html = fetch_html(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    quotes = []

    scripts = soup.find_all('script', type='application/ld+json')

    for script in scripts:
        try:
            data = json.loads(script.string)

            if data.get('@type') == 'Quote':
                text = data.get('text', '')
                author_data = data.get('author', {})
                author = author_data.get('name', '') if isinstance(
                    author_data, dict) else author_data

                keywords = data.get('keywords', [])
                if isinstance(keywords, str):
                    tags = [tag.strip() for tag in keywords.split(',')]
                else:
                    tags = keywords

                quotes.append({
                    'text': text,
                    'author': author,
                    'tags': tags
                })

        except (json.JSONDecodeError, AttributeError):
            continue

    return quotes
