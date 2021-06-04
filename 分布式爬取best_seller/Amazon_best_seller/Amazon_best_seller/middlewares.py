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
# proxyServer = "http://http-pro.abuyun.com:9010"  #专业版
proxyUser = "H80CZ30131P8579D"
proxyPass = "C46CF65B0A2952B7"  #表格的

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
        USER_AGENT = ua.chrome # 任意头文件
        request.headers['User-Agent'] = USER_AGENT


        '''增加阿布云代理'''

        # request.meta["proxy"] = proxyServer
        # print("正常增加IP", proxyAuth)
        # request.headers["Proxy-Authorization"] = proxyAuth

        # logging.debug('Using Proxy:%s' % proxyServer)


        '''添加cookie的方式'''
        # request.cookies = {
        #     'session-id': '135-0566866-8036011',
        #     'aws-ubid-main': '714-0170331-1671842',
        #     'session-id-time': '2082787201l'
        # }

        # 添加登录  复制过来的cookie
        # cookie = 'ubid-main=130-4322001-3836260; session-id=135-0566866-8036011; aws-ubid-main=714-0170331-1671842; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjU5OWJkZmRiLWM4NTUtNGM4NS04Nzc5LTQzZWM4ZGU5ZWZjNCJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiMEpucHMrNGlcL25jTjl5NkV6MTZHXC96TUY1QlB6RllpeW9RUFRtSVpEK2gwPSIsImFybiI6ImFybjphd3M6aWFtOjoyNzA4OTA3ODc4NDU6cm9vdCIsInVzZXJuYW1lIjoiamV2dnlfMTQ2In0.lvtu3nvHSpL-s9XvtrK6_7k6-w0WaXpp1k-PfoXei3Mvc_NZk97UswOE2_Cx0ZK3kWKbPk0pz7nj8CNAokwMS-aB6DDhJcwePS8T0-nzyRVpmTLNOIZ-c6fKcuRonhGo; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A270890787845%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22jevvy_146%22%2C%22keybase%22%3A%220Jnps%2B4i%2FncN9y6Ez16G%2FzMF5BPzFYiyoQPTmIZD%2Bh0%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; regStatus=registered; s_fid=00D3D665F6DC0739-2AA806735DA11512; s_dslv_s=First%20Visit; s_vn=1635988253127%26vn%3D1; s_invisit=true; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1604452397084-993838.38_0; s_depth=12; s_dslv=1604454981070; s_nr=1604454981076-New; lc-main=en_US; x-main=PDFJSYrnuCYjEzykZAe5pM1HhUIZHH3Zo1CbFckSRjYHEndMSDeytCSxK5cHbIw2; at-main=Atza|IwEBIEOrxOAFE2gZTF6OTrO4vuvFwqHVLpoYK7NreUFUnb0Wt4jKe8-5y7WfSPk7XzxIYbTqIvajC89miBUcVBoIdEMFfGse_5bqJBbmsYyYIKSszk8RudWdxL77g_86hJvTBh6e0u1wZLaBiEo4O0pMSV5XBYgke4LrLyNFB1NXHmQPNglKRvdxRVptM8rro51jj71LeRCgStfXeJG-wC5u5vHKiJ3IdMwwb6nZIilvqG-M3A; sess-at-main="wZaDyCybtaIFTbA8Rgtk3uaQr3WYqCX6OrN3XradE7g="; sst-main=Sst1|PQFtaaMvOOOJqvtNxbi65aVACXmzO5qF-EQ367fRU_7O1R5wy8C-XK9ZGdC1SSsbzJNdtnht-tS5H9REr2utQVh4sHapXK3el5ceh9Dpf_BewAGq1DbsUQejl93wyqIDVGOGU6HMD-sfG6JZ0YZAZkFkv22jkQZD1LGqcegA6tWu-BEBMYytZP_3ujm_f-MVeBPRIxJgDLp837Te7y7qbffHq4RQkHBVrCITvpOEWAwNBa4qfdnaLUCs4aWn65gZ3OUzfdmLJL42BLfgza0euZ_EmpQtxeTo9TmB1rlOrBfWGn4; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; session-token="BMN0DhKF7ph3sJV1s5GaRktyBaPOG/G2/D4ByIEO6mqJfP5wTJp33btlzSA+HKNPazbpIqaKnBWZPQJo5g5akE++pOjaIK/LWkvixsQk25JIIGEzL4d4+a5JOpzH8CVLnJRpKnjQpRPBPAa2BzdDzO/Rnzyuwzek/absl7u29fGSa9s06dDsYYOVW9MKYXBWkCrqtO3Rxlc5N5o4EQvo3e8jso7mtDvkYfWkDI+F7hC9Hvy6Z1HOxV+f8OTF7nIBpjkYAKWw7aw9gSXXrH3gaQ=="; csm-hit=tb:TFA2JKW7Y3PG9ZTZRAG4+s-TFA2JKW7Y3PG9ZTZRAG4|1606095411431&t:1606095411431&adb:adblk_no'
        #
        # cookie_dict = {each.split('=')[0]: each.split('=')[1] for each in cookie.split('; ')}
        # request.cookies = cookie_dict

        print('request.header', request.headers)
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

        '''代理位置'''
        # request.meta["proxy"] = proxyServer
        # print("正常增加IP", proxyAuth)
        # request.headers["Proxy-Authorization"] = proxyAuth
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
