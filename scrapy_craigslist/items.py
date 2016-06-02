# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCraigslistItem(scrapy.Item):
    title = scrapy.Field()
    post_date = scrapy.Field()
    post_date_specific = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    ad_url = scrapy.Field()
