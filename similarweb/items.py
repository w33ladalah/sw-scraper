# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopItem(scrapy.Item):
    # define the fields for your item here like:
	website = scrapy.Field()
	world_rank = scrapy.Field()
	website_popularity = scrapy.Field()
	direct = scrapy.Field()
	referrals = scrapy.Field()
	search = scrapy.Field()
	social = scrapy.Field()
	mail = scrapy.Field()
	display = scrapy.Field()
	social_details = scrapy.Field()
