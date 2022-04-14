# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import configparser

import requests,json,time,os
from db_fixture.func import fun
from configparser import ConfigParser

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "env.ini")  # 读取到本机的配置文件

conf = ConfigParser()
cf = conf.read(cfgpath, encoding='utf-8')

class comm():

    def __init__(self, env):

        en = env
        self.url = conf.get(en, 'IP')
        self .api_url = conf.get(en, 'api_url')
        self.AK = conf.get(en, 'AK')
        self.secret = conf.get(en, 'secret')
        self.tel = conf.get(en, 'tel')
        self.password = conf.get(en, 'password')

    def get_bady(self):
        """
        根据env3.ini的配置文件，获取登录的请求参数
        :return:登录的请求参数
        """
        password_sec = fun.SHA256(self.password)
        password_secaa = fun.md5(self.password)
        print(password_secaa)
        # 密码加密
        if env == "oss_test":
            data = {
                "applicationId": '201935',
                "password":password_sec,#password_sec,
                "tel": self.tel
            }
            return data

        elif env == 'app_And_test':
            data ={
                "applicationId": '201933',
                "password": '6f8d13d52296bfa2e44ad142bf78d11d5d131008b439a48cfd88ef0e1c6c43a4',
                "tel": self.tel,
                "loginType": 5
                # "invitationUserId": ""
            }
            return data
        else:
            print('环境有误')


    def get_header(self,data):
        """
        构造登录请求接口的header参数
        :return: header
        """
        # 时间戳，到毫秒
        t = time.time()
        TS = str(round(t * 1000))

        # ContentMD5的加密   bady的字符串长度，+ ';'+时间戳
        ContentMD5 = str(len(str(data))) + ';' + TS  # ContentMD5的加密方式
        # print(ContentMD5)
        # 加密
        Content_MD5 = fun.md5(ContentMD5)

        # sign加密    # 加密方式= '路径'+';'+'时间戳'+';'+"请求方法"+';'+'rs'+';'+'Content_MD5'+';'+'token'+';'+secret
        method = 'POST'
        rs = 'o4U80DyzNRanneWPqH7mXeGGCyktHJKk'  # 32位随机字符串

        ws = self.api_url + ';' + TS + ';' + method + ';' + rs + ';' + Content_MD5 + ';'
        signstring = ws + ';' + self.secret  # 加密前的sign
        # 加密，按sign-Type传的方式。md5和sha256
        sign = fun.SHA256(signstring)

        # 构造请求header
        header = {
            'ak': self.AK,  # 固定值
            "Content-MD5": Content_MD5,
            # "Content-Type":"application/json;charset=UTF-8",
            "rs": rs,  # 随机字符串
            "sign": sign,
            "TS": TS,
            'sign-Type': 'SHA-256',#加密方式
            'Authorization': '',
            'version': '1.0.0'

        }
        return header


    def login_request(self):
        """
        请求登录接口
        :return: 接口返回参数
        """
        url = self.url+self.api_url
        data = self.get_bady()
        header = self.get_header(data)
        print('请求地址',url)
        print('请求参数', data)
        print('请求header', header)
        # 请求接口
        result = requests.post(url,json=data,headers=header)
        print('返回参数',result.json())
        return result.json()



if __name__ == "__main__":
    env = 'app_And_test'
    a=comm(env)
    b=a.login_request()

