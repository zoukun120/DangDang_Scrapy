# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DangdangScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    detail = scrapy.Field()
    book_name = scrapy.Field()
    comment_num = scrapy.Field()
    author = scrapy.Field()
    release = scrapy.Field()
    price_n = scrapy.Field()
    price_s = scrapy.Field()
    discount = scrapy.Field()
