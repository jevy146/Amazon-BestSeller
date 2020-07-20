# -*- coding: utf-8 -*-

# @File    : add_data_to_redis.py
# @Date    : 2019-10-25
# @Author  : ${杨杰伟}


import redis
conn = redis.Redis(host='192.168.31.104', port=6379, )



import pandas as pd

df=pd.read_csv('./goods_link/kinds_links.csv',encoding='utf-8')
print(df.head())

'''传递要爬取的链接'''
for each in (df.link[2000:]): #添加数据
    print(each)
    conn.lpush('BestSeller:start_urls',each)

