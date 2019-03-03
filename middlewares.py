# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import requests


class LalalaDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        ua = spider.settings.get('USER_AGENTS')
        print('代理正在运行')
        print(self.a)
        print(self.a)
        # UA = random.choice(USER_AGENTS)
        request.headers['User-Agent'] =random.choice(ua)
        print(request.headers['User-Agent'])


class Proxy_Middleware():

    def process_request(self, request, spider):

        try:
            xdaili_url = spider.settings.get('XDAILI_URL')

            r = requests.get(xdaili_url)
            proxy_ip_port = r.text
            request.meta['proxy'] = 'https://' + proxy_ip_port
        except requests.exceptions.RequestException:
            print('获取讯代理ip失败！')
            spider.logger.error('获取讯代理ip失败！')
