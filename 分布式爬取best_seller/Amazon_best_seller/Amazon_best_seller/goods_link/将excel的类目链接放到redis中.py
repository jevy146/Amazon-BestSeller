# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 15:11
# @Author  : 结尾！！
# @FileName: 将excel的类目链接放到redis中.py
# @Software: PyCharm


import pandas as pd

df1=pd.read_excel(r'E:\pyhton代码\2020选品分析-爱奇儿\美日德英四国户外\美\sporting-goods_browse_tree_guide._TTH_.xls',
                   )

print(df1.head())
Node=df1['Node ID'][1:].tolist()
Node_ID=set(Node)
print(len(Node_ID))
import redis
conn=redis.Redis(host='192.168.0.128',port=6379)
for each in Node_ID:
    pg_1=f'https://www.amazon.com/gp/bestsellers/zgbs/{each}'
    print(pg_1)
    conn.lpush('BestSeller:start_urls', pg_1)


    # pg_2=pg_1+'/?&pg=2'
    # print(pg_2)
    # conn.lpush('BestSeller:start_urls',pg_2)


#保存列表为csv
# lk=pd.DataFrame(columns=['link'],data=pg)
# lk.to_csv('./日本户外链接.csv')


