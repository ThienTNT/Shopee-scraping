# First install bs4 and selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def get_url(search_term):
    template = 'https://shopee.vn/search?keyword={}'
    search_term = search_term.replace(' ', '%20')

    # Add term query to url
    url = template.format(search_term)

    # Add page query placeholder
    url += '&page={}'

    return url


def extract_record(item):
    # Description and url
    price_limit = '-1'      # For future development
    try:
        description = item.find('div', {'class': '_10Wbs- _5SSWfi UjjMrh'}).text.strip()
        url = 'https://shopee.vn' + item.a.get('href')
    except AttributeError:
        description = 'No Name'
        url = 'No link'

    # Price
    prices = item.find_all('span', {'class': '_1d9_77'})
    if len(prices) == 2:
        price_limit = prices[0].text        # For future development
        price = prices[0].text + ' - ' + prices[1].text
    elif len(prices) == 1:
        price_limit = prices[0].text        # For future development
        price = prices[0].text
    else:
        # price_limit = ''
        price = 'Zero'

    # Sale and location
    try:
        sale = item.find('div', {'class': '_2VIlt8'}).text
        location = item.find('div', {'class': '_1w5FgK'}).text
        if sale == '':
            sale = 'none'
    except AttributeError:
        sale = 'none'
        location = 'Unknown'

    result = (description, price, sale, location, url, price_limit)
    return result


print("Code done!!!")
