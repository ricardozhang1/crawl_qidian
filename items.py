# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


class QidianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def add_http(value):
    return 'https:'+value

class qidianBookListTtem(scrapy.Item):
    novelId = scrapy.Field()
    novelDetailUrl = scrapy.Field(
        input_processor = MapCompose(add_http)
    )
    novelName = scrapy.Field()
    novelAllList = scrapy.Field()
    novelProcess = scrapy.Field()
    novelImageUrl = scrapy.Field()








