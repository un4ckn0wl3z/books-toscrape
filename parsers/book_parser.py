from bs4 import BeautifulSoup
import re

from locators.book_locators import BookLocators


class BookParser:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+])'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        return rating_classes[0]
