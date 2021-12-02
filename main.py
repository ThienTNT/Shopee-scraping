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


def run_main(search_term):
    driver = webdriver.Chrome()
    records = []        # For future development
    count = 0           # Count the number of products
    url = get_url(search_term)

    for page in range(2):
        driver.get(url.format(page))
        driver.execute_script("document.body.style.zoom='25%'")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(15)      # Wait for page to load
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'class': 'col-xs-2-4 shopee-search-item-result__item'})
        print(len(results))

        for item in results:
            record = extract_record(item)
            count += 1
            if record:
                with open('ShopeeText.txt', 'a', encoding='utf-8') as f:
                    f.write(f"Product's name: \t{record[0]}\n")
                    f.write(f"Product's price: \t{record[1]}\n")
                    f.write(f"Product's sale: \t{record[2]}\n")
                    f.write(f"Product's location: \t{record[3]}\n")
                    f.write(f"Product's url: \t{record[4]}\n")
                    f.write(f"Print {count} time.\n\n")
                records.append(extract_record(item))
    driver.close()


print("Code done!!!")
