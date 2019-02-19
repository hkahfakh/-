# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianzhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # test git
    url = scrapy.Field()
    name = scrapy.Field()
    Company = scrapy.Field()
    Salary = scrapy.Field()
    location = scrapy.Field()
    Educational = scrapy.Field()
    experience = scrapy.Field()
    pass
