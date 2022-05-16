import pandas as pd
import numpy as np
# from matplotlib import pyplot as plt


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



def dev(ff):    #这个函数专门用来存放装饰器所需的参数，若装饰器不需要参数，则可不要此层
    def func1(func): #将被装饰的函数当作变量传入，固定写法
        #想要保留原函数的文档和函数名属性，需要修正装饰器
        # @wraps(func) #functools模块下提供一个装饰器wraps
        def sdsa(*args, **kwargs):#用来存放被装饰函数的变量，固定写法
            print('函数执行*****')
            res= func(*args, **kwargs)**ff
            return res
        return sdsa
    return func1

@dev(ff=3)
def yhan(a,b):
    c=a+b
    return c

# jj=yhan(3,5)
# print(jj)

#可变参数
def dun(*args,**kwargs):
    print(args)
    print(kwargs)

id=(1,2,3,4)
cd={"kl":"2","hgjh":"5","gu":"6"}
# dun(*id)
# dun(*id,**cd)

#迭代器
list1=[i for i in range(5)]

def han(i):

    while True:
        i += 1
        yield i
        return i

g=(i for i in list1)
print(next(g))
