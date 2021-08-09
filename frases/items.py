# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FrasesItem(scrapy.Item):
    phrase = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
