#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 14:08
# @Author  : 结尾！！！
# @File    : 查缺补漏.py


import pandas as pd
df1=pd.read_excel(r'E:\pyhton代码\美国产品-新方法挖掘\包晗的分类树\home-improvement.xlsx',
                  sheet_name="Sheet1",)
df2=pd.read_excel(r'E:\pyhton代码\美国产品-新方法挖掘\包晗的分类树\industrial_browse.xlsx',
                  sheet_name="Sheet1",)
print(df1.head())
Node=df1['Node ID'][1:].tolist()+df2['Node ID'][1:].tolist()
Node_ID=set(Node)
print(len(Node_ID))
#
# import pymongo
# # 创建MongoDB数据库连接
# mongoClient = pymongo.MongoClient(host = "192.168.0.151", port = 27017)
# # 创建mongodb数据库名称
# dbname = mongoClient["US_AMZ"]
# # 创建mongodb数据库的表名称
# table = dbname["Tools"] #类目
#
# # res = table.find_one({'URL': 'https://www.amazon.com/gp/bestsellers/zgbs/700744011/?&pg=2'})
# # print(res)
#
#
# import redis
# conn=redis.Redis(host='192.168.0.128',port=6379)
#
# for each in Node_ID:
#     pg_1=f'https://www.amazon.com/gp/bestsellers/zgbs/{each}'
#     res = table.find_one({'URL': pg_1})
#     if not res :
#         conn.lpush('BestSeller:start_urls', pg_1)
#         print(pg_1)
#
#     pg_2=pg_1+'/?&pg=2'
#     res = table.find_one({'URL': pg_2})
#     if not res:
#         conn.lpush('BestSeller:start_urls',pg_2)
#         print(pg_2)






