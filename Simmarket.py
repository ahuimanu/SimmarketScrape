import random
import requests
import time
from bs4 import BeautifulSoup, Tag, NavigableString

# helpful links:
# Tutorial: https://www.dataquest.io/blog/web-scraping-tutorial-python/
# BS4 Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
# W3Schools Python docs: https://www.w3schools.com/python/default.asp
# Python standard library docs: https://docs.python.org/3.7/library/index.html
# Psycopg PostgreSQL adapter for Python: http://initd.org/psycopg/docs/install.html


class SimmarketP3DV4SceneryEntry:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def __str__(self):
        return 'Name: {} - URL: {}'.format(self.name, self.url)


class SimmarketP3DV4SceneryParser:

    def __init__(self):
        self.sceneries = []
        self.page_extension = '.chtml'
        self.page_prefix = 'https://secure.simmarket.com/prepar3d-v4-scenery-page-'
        self.last_page = 12

    def parse_sceneries(self):

        for page_num in range(1, self.last_page + 1):

            # wait between 1/2 second and 2 1/2 seconds
            time.sleep(random.uniform(0.5, 2.5))

            # specify the url
            quote_page = self.page_prefix + \
                         str(page_num) + \
                         self.page_extension

            print('getting: {}'.format(quote_page))
            page = requests.get(quote_page)

            # parse the html using beautiful soup and store in variable `soup`
            soup = BeautifulSoup(page.content, 'html.parser')
            rows = soup.select('div.new_product_name a')

            for row in rows:
                name = row.contents[0]
                url = row['href']
                scenery = SimmarketP3DV4SceneryEntry(url, name)
                self.sceneries.append(scenery)

            page_num = page_num + 1

    def print_sceneries(self):
        # Printing all sceneries
        print('printing {} sceneries'.format(self.sceneries.__len__()))
        for scenery in self.sceneries:
            print(scenery)


    # Parse single product page
    def parse_product(self, product_page):
        # Page
        page = requests.get(product_page)

        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page.content, 'html.parser')
        rows = soup.select('div.new_product_name a')

