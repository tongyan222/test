import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


s = pd.Series([0.1,0.3,1,2,3],index=['a','b','c','d','e'])
# print(s['b'])



d = pd.DataFrame(data=[['a0',1.255,[0,1,2],{'d0':0}],['a1','返回','c1','d1'],[1,2,3,4]],index=['第一行','第二行','第三行'],columns=['第一列','第二列','第三列','第四列'])
# print(d)
# print(d.iloc[1,1])

# dd = pd.DataFrame(data={'key1':[11,22,33,44],'key3':['vv','ff',45,464]},index=['第一行','第二行','第三行','第四行'])
# # print(dd)
# ddd = pd.DataFrame(data={'key1':pd.Series([0,0,200,3,4],index=['a','b','c','d','e'])
#     ,'key6':pd.Series([0,11,56,31,41],index=['a','b','c','d','e'])
#     ,'key3':pd.Series(data=[5555,6666,12,8888,9999],index=['a','b','c','d','e'])})


help(pd.read_excel)






