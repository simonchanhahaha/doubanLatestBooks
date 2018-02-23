# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DbbookPipeline(object):
    def __init__(self):
        self.filename = open("./books.json",'w')
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(data)
        return item

    def close_spider(self):
        self.filename.close()
