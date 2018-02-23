# -*- coding: utf-8 -*-
import scrapy
from dbbook.items import DbbookItem
from scrapy_redis.spiders import RedisSpider


# from bs4 import BeautifulSoup as bs

class DoubanSpider(RedisSpider):
    name = 'douban'
    # allowed_domains = ['book.douban.com']
    # start_urls = ['http://book.douban.com/']

    redis_key = "douban:start_urls"


    def __init(self,*args,**kwargs):
        domain = kwargs.pop('domain','')
        self.allow_domains = filter(None,domain.split(','))
        super(DoubanSpider,self).__init__(*args,**kwargs)

    def parse(self, response):

        # book_urls = response.xpath('//div[@class="title"]/a/@href').re('https://book.douban.com/subject/\d+')
        # for book_url in book_urls:
        #     yield scrapy.Request(url=book_url, callback=self.book_parse)

        lists = response.xpath('//ul[@class="list-col list-col5 list-express slide-item"]/li')
        for list in lists:
            item={}
            item['book_name'] = list.xpath('.//div[@class="title"]/a/text()').extract()[0]
            item['book_url'] = list.xpath('.//div[@class="title"]/a/@href').re('https://book.douban.com/subject/\d+')[0]
            item['book_author'] = list.xpath('.//div[@class="author"]/text()').extract()[0].replace('&nbsp','').strip()
            item['book_publisher'] = list.xpath('.//div[@class="more-meta"]/p/span[@class="publisher"]/text()').extract()[0].strip()
            item['book_pub_time'] = list.xpath('.//div[@class="more-meta"]/p/span[@class="year"]/text()').extract()[0].strip()
            yield scrapy.Request(url=item['book_url'],callback=self.book_parse,meta={'data':item})

    def book_parse(self, response):
        data = response.meta['data']
        item = DbbookItem()

        item['book_url'] = response.url
        item['book_name'] = data['book_name']
        item['book_id'] = response.url.split('/')[-1]
        item['book_author'] = data['book_author']
        item['book_publisher'] = data['book_publisher']
        item['book_pub_time'] = data['book_pub_time']
        p_lists = response.xpath('//span[@class="all hidden"]//div[@class="intro"][1]/p').extract()
        info =""
        for p in p_lists:
            info +=p

        # item['book_price'] = scrapy.Field()
        # item['book_ISBN'] = scrapy.Field()
        item['book_info'] = info
        yield item

