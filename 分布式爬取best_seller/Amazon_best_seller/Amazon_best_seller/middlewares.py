# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import logging
import time

from fake_useragent import UserAgent
from scrapy import signals


class AmazonBestSellerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)






'''使用动态版隧道'''
proxyServer = "http://http-dyn.abuyun.com:9020"
proxyUser = "HIX9H33N87639FSD"
proxyPass = "580D452C7B02267E"

# proxyServer = "http://http-cla.abuyun.com:9030"
# proxyUser = "H7V9P9Q694L32B5C"
# proxyPass = "52F8CF6FBAE70F68"
#  proxyServer = "http://http-pro.abuyun.com:9010"
# 代理隧道验证信息


proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         request.meta["proxy"] = proxyServer
#
#         request.headers["Proxy-Authorization"] = proxyAuth





class AmazonBestSellerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called




        ua = UserAgent()
        USER_AGENT = ua.random # 任意头文件
        request.headers['User-Agent'] = USER_AGENT


        '''增加阿布云代理'''
        request.meta["proxy"] = proxyServer
        print("正常增加IP", proxyAuth)
        request.headers["Proxy-Authorization"] = proxyAuth

        logging.debug('Using Proxy:%s' % proxyServer)
        print('request.header',request.headers)

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

        print('DownloaderMiddleware返回状态码：', response.status)
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        print('代理%s，访问 %s 出现异常:%s' % (request.meta['proxy'], request.url, exception))

        time.sleep(1)

        ua = UserAgent()
        USER_AGENT = ua.chrome  # 任意头文件
        print(USER_AGENT)
        request.headers['User-Agent'] = USER_AGENT

        request.meta["proxy"] = proxyServer
        print("正常增加IP", proxyAuth)
        request.headers["Proxy-Authorization"] = proxyAuth
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
