# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonBestSellerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Ranking = scrapy.Field()  # 小排名
    URL = scrapy.Field()  # 网页
    link_normal = scrapy.Field()  # 详情页链接
    title = scrapy.Field()  # 标题
    img = scrapy.Field()  # 图片
    price_Interval = scrapy.Field()  # 价格区间
    reviews = scrapy.Field()  # 评论数
    score = scrapy.Field()  # 得分
    kinds_of_commodity = scrapy.Field()  # 商品种类
