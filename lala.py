# -*- coding: utf-8 -*-
import scrapy.middleware
from ..items import LalalaItem
scrapy
'''
参考，不运行
'''

class LalaSpider(scrapy.Spider):
    name = 'lala'
    allowed_domains = ['http://example.webscraping.com']
    start_urls = ['http://example.webscraping.com/user/profile/']

    def parse(self, response):
        print('你a ')
        '''
        也可以直接使用self.settings.get('name')获取设置数据
        '''
        print(self.settings.get('ROBOTSTXT_OBEY'))
        a = LalalaItem()
        a['name']=122
        '''
        要有数据流向pipeline才能执行pipeline文件，如yield a
        '''
        yield a
        # pass
        # print('你好')
        # print(self.la)
    '''
    不需要定义__init__函数
    '''

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     return cls(la=crawler.settings.get('BOT_NAME'))
