#!/usr/bin/env python3
"""
Module for authenticated web scraping with login.
"""
import requests
import bs4


def login_and_scrape(login_url, user, pwd):
    """
    Logs in and scrapes quotes visible only after authentication.

    This function uses a session to persist cookies, extracts a CSRF token
    from the login form, posts credentials, and scrapes the protected
    quotes page after successful authentication.

    Args:
        login_url (str): The login page URL
        user (str): Username for authentication
        pwd (str): Password for authentication

    Returns:
        list: A list of quote dicts, each with keys text, author, and tags
    """
    session = requests.Session()

    response = session.get(login_url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    csrf_input = soup.find('input', {'name': 'csrf_token'})
    csrf_token = csrf_input['value'] if csrf_input else ''

    login_data = {
        'username': user,
        'password': pwd,
        'csrf_token': csrf_token
    }

    login_response = session.post(login_url, data=login_data)
    login_response.raise_for_status()

    base_url = login_url.rsplit('/', 1)[0]
    quotes_url = base_url + '/'

    quotes_response = session.get(quotes_url)
    quotes_response.raise_for_status()

    quotes_soup = bs4.BeautifulSoup(quotes_response.text, 'html.parser')

    quotes = []
    quote_blocks = quotes_soup.find_all('div', class_='quote')

    for block in quote_blocks:
        text_elem = block.find('span', class_='text')
        author_elem = block.find('small', class_='author')
        tag_elems = block.find_all('a', class_='tag')

        if text_elem and author_elem:
            text = text_elem.get_text()
            author = author_elem.get_text()
            tags = [tag.get_text() for tag in tag_elems]

            quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })

    return quotes
