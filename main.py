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



print("Code done!!!")
