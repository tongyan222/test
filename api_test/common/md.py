# coding:utf-8


import os
from configparser import ConfigParser
# 用os模块来读取


curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "env.ini")  # 读取到本机的配置文件
print(cfgpath)

# 调用读取配置模块中的类
conf = ConfigParser()
cf=conf.read(cfgpath,encoding='utf-8')
conf.sections()#获取文件中所有的section
host = conf.get('oss_test','IP')
print(host)




