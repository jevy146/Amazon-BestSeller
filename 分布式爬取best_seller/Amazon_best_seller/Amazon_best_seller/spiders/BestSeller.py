# -*- coding: utf-8 -*-
import random
import time

import redis
import scrapy

from Amazon_best_seller.items import AmazonBestSellerItem

#使用scrapy_redis
from scrapy_redis.spiders import RedisSpider
class BestsellerSpider(RedisSpider):
    name = 'BestSeller'
    allowed_domains = ['www.amazon.co.uk/gp/bestsellers/']
    # start_urls = ['http://www.amazon.ca/gp/bestsellers//']
    redis_key = 'BestSeller:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(BestsellerSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)

        if 'Robot Check' in response.text:

            '''将数据保存到redis重新爬取'''
            print('有验证码。。。',response.url)
            URL=response.url
            conn = redis.Redis(host='192.168.0.128', port=6379, )
            conn.lpush('BestSeller:start_urls', URL)
            print('将链接重新加入到redis数据库中', URL)
            # time.sleep(random.randint(2,5))
            import win32api,win32con
            win32api.MessageBox(0, "帅哥 有验证码 爬虫需要关闭", "提醒",win32con.MB_OK)
            self.crawler.engine.close_spider(self, '有验证码，主动关闭爬虫')
            return


        commodity_info = AmazonBestSellerItem()
        #9爬虫的链接
        commodity_info['URL'] = response.url
        # 8.商品种类
        kinds_of_commodity = response.xpath('//*[@id="zg-right-col"]/h1/span/text()').extract()
        commodity_info['kinds_of_commodity'] = kinds_of_commodity

        list_lis = response.xpath('//*[@id="zg-ordered-list"]//li')
        if  len(list_lis):
            print('list_lis 长度', len(list_lis))
            for each_li in list_lis:
                # 1.详情页链接
                commodity_info['link_normal'] = each_li.xpath(
                    './span/div/span/a[@class="a-link-normal"]/@href').extract()
                # 2.产品名称
                commodity_info['title'] = each_li.xpath('./span/div/span/a/span/div/img/@alt').extract()
                # 7.图片
                commodity_info['img'] = each_li.xpath('./span/div/span/a/span/div/img/@src').extract()
                # 3.评分
                try:
                    commodity_info['score'] = each_li.xpath(
                        './span/div/span/div[1]/a[1]/@title').extract()  # ['4,6 von 5 Sternen']
                except:
                    commodity_info['score'] = ['null']
                # 4.评论数
                try:
                    commodity_info['reviews'] = each_li.xpath('./span/div/span/div[1]/a[2]/text()').extract()
                except:
                    commodity_info['reviews'] = ['null']
                # 5.价格区间
                try:
                    commodity_info['price_Interval'] = each_li.xpath(
                        './span/div/span/div/a/span/span/text()').extract()  # 没有星级的价格
                except:
                    commodity_info['price_Interval'] = each_li.xpath(
                        './span/div/span/div[2]/a/span/span/text()').extract()  # 有星级的价格

                # 6.排名
                commodity_info['Ranking'] = each_li.xpath('./span/div/div/span[1]/span/text()').extract()

                yield commodity_info
        else:
            print("没有数据，程序结束")
            return
