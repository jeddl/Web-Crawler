# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebwithinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nbaNewsTitle = scrapy.Field()
    nbaNewsContent = scrapy.Field()

class NbaNews:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def getTitle(self):
        return self.title

    def getContent(self):
        return self.content

