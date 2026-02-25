#!/usr/bin/env python3
scrape_product_detail = __import__(
    '7-product_detail').scrape_product_detail
url = "https://webscraper.io/test-sites/e-commerce/static/product/31"
detail = scrape_product_detail(url)
print(f"Product details: {detail}")
