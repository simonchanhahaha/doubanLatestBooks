# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbbookItem(scrapy.Item):
    #基本信息
    book_name = scrapy.Field()
    book_id = scrapy.Field()
    book_url = scrapy.Field()

    #图书信息
    book_author = scrapy.Field()
    book_country = scrapy.Field()
    book_publisher = scrapy.Field()
    book_pub_time = scrapy.Field()
    book_price = scrapy.Field()
    book_ISBN = scrapy.Field()

    #内容简介
    book_info = scrapy.Field()