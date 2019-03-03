# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
需要定义__init__函数

'''
class LalalaPipeline(object):
    def __init__(self,a):
        self.a = a

    def process_item(self, item, spider):
        print('你哈')
        print(self.a)
        print(item)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(a=crawler.settings.get('BOT_NAME'))

