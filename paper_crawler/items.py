# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    abstraction = scrapy.Field()

    # 크롬 관리자 모드에서 보면 title + authors가 d_block으로 묶여 있다.
    # d_block = scrapy.Field()
    pass
