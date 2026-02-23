#!/usr/bin/env python3
"""
Module for fetching HTML content from web pages.
"""
import requests


def fetch_html(url, headers=None, timeout=10):
    """
    Fetches a web page and returns its HTML as text.

    Args:
        url (str): The page URL to retrieve
        headers (dict, optional): HTTP headers dictionary. Defaults to None.
        timeout (int, optional): Seconds to wait before aborting. Defaults to 10.

    Returns:
        str: The full HTML of the response as a string

    Raises:
        requests.exceptions.HTTPError: If HTTP status >= 400
        requests.exceptions.RequestException: For other request-related errors
    """
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raises HTTPError for status >= 400
        return response.text
    except requests.exceptions.HTTPError as e:
        raise e
    except requests.exceptions.RequestException as e:
        raise e