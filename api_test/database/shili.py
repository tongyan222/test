import os
import random
from configparser import ConfigParser

import pymysql
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['Simhei']
class comm():
    def read_excel(self):
        """
        读取数据
        :return:
        """
        file_path = r'C:/Users/DELL/Desktop/朝代表.xlsx'# Excel文件路径

        df = pd.read_excel(file_path,sheet_name='Sheet2',skiprows=[1],nrows=40,usecols=[0,3])
        # print(df)

        df1=df.dropna(axis=0,subset=['朝代']) ##删除缺失值
        hang = len(df1) #获取行数
        # print(df1)


        # print(random.sample(range(1,100),hang))
        series = pd.Series(random.sample(range(1,100),hang))
        series.index = df1.loc[:,'时间']

        series.plot(kind="barh", stacked=True)
        # plt.show()
        # help(series.plot)

    def read_sql(self):
        """
        # 读取数据库不同业务类型已完成订单的数量
        :return:
        """

        # 连接数据库
        con = pymysql.connect(host='192.192.192.137',user='root',password='KKniubi@666',db='tckk20_order_test',charset='utf8')

        sql='select order_type,count(*) as 已付款 from dftc_order_community where status=3 GROUP BY order_type'
        # 读取需要的数据
        df = pd.read_sql_query(sql, con,index_col='order_type')
        # print(df)

        sql1 = 'select order_type,count(*) as 已退款 from dftc_order_community where status=22 GROUP BY order_type'
        df1=pd.read_sql_query(sql1, con,index_col='order_type')
        # print(df1)

        sql1 = 'select order_type,count(*) as 已取消 from dftc_order_community where status=41 GROUP BY order_type'
        df2=pd.read_sql_query(sql1, con,index_col='order_type')
        # 两个df链接合并
        aaaa = pd.merge(df,df1,on='order_type',how="outer")
        # print(aaaa)
        aaaa = pd.merge(aaaa, df2, on='order_type', how="outer")
        # 用 0 填充 NaN
        aaaa = aaaa.fillna(0)
        print(aaaa)
        # print(aaaa.loc[6])
        # print(aaaa.index)

        # 变更索引名称
        # aaaa.index=[]
        ff =aaaa.rename(index ={6:'办证',9:'税务代办',10:'装修拼团',11:'透明厨房类型',13:'服务订单'})
        print(ff)
        ff.plot(kind="bar", stacked=True)
        plt.show()




if __name__ == "__main__":
    a=comm()
    a.read_sql()