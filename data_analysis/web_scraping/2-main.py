#!/usr/bin/env python3
scrape_paginated = __import__('2-scrape_paginated').scrape_paginated

url = "https://quotes.toscrape.com/"
try:
    data = scrape_paginated(url)
    if data:
        quote = data[0]
        output = f"'text': {repr(quote['text'])}, 'author': {repr(quote['author'])}, 'tags': {quote['tags']}"
    else:
        output = "No quotes found."
    print(output)
except Exception as e:
    print(str(e))
