# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnnNews(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class Fundrazr(scrapy.Item):
	title = scrapy.Field()
	currentAmount = scrapy.Field()
	goal = scrapy.Field()
	currencyType = scrapy.Field()
	endDate = scrapy.Field()
	contributors = scrapy.Field()
	story = scrapy.Field()
	url = scrapy.Field()


