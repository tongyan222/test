import hashlib
import json

import requests


class fun():

    def send_reqquest(self,method,url,json=None,headers=None,data=None,files=None,params=None,cookies=None,auth=None,timeout=None,proxies=None,verify=None,cert=None):
        """
        封装调用方法
        :param data:
        :param params:
        :param headers:
        :param cookies:
        :param json:
        :param file:
        :param auth:
        :param timeout:
        :param proxies:
        :param verify:
        :param cert:
        :return:
        """
        r = requests.request(method,url,data=data,params=params,headers=headers,cookies=cookies,json=json,files=files,auth=auth,timeout=timeout,proxies=proxies,verify=verify,cert=cert)
        self.actual_result = r.json()   #json.loads(r.text)
        self.actual_code = self.actual_result['code']# 获取实际结果的code
        return self.actual_result

    @staticmethod
    # 封装post请求方法，传入需要的参数url和data
    def post_method(url,data=None,header=None):
        global res
        if header is not None:
            res = requests.post(url,json=data,headers=header)
        else:
            res = requests.post(url,json=data)

        if  str(res) == "<Response [200]>":
            return res.json()
        else:
            return res.text


    # 封装get请求方法，传入需要的参数url和data
    @staticmethod
    def get_method(url, data=None, header=None):

        if header is not None:
            res = requests.get(url, params=data, headers=header)
        else:
            res = requests.get(url, params=data)
        return res.json()

    # 请求方法put
    @staticmethod
    def put_method(url, data=None, header=None):
        if header is not None:
            res = requests.put(url, json=data, headers=header)
        else:
            res = requests.delete(url, json=data)
        return res.json()

    # 请求方法delete
    @staticmethod
    def delete_method(url, data=None, header=None):
        if header is not None:
            res = requests.delete(url, json=data, headers=header)
        else:
            res = requests.delete(url, json=data)
        return res.json()

    @classmethod
    # 主方法
    def run_method(cls,method,url,data=None,header=None):
        if method == 'get' or method == 'GET':
            res = cls.get_method(url,data,header)
        elif method == 'post' or method =='POST':
            res = cls.post_method(url,data,header)
        elif method == 'put' or method == 'PUT':
            res = cls.put_method(url,data,header)
        elif method == 'delete' or method == 'DELETE':
            res = cls.post_method(url,data,header)
        else:
            res = "你的请求方式不正确！"
        # return res
        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True,separators=(',', ':')) #转换为字符串

    @staticmethod
    def md5(astr):
        """
        :param str: 需要加密的字符串
        :return: 加密后的字符串
        """
        data_sha = hashlib.md5(astr.encode('utf-8')).hexdigest()
        return data_sha

    @staticmethod
    def SHA256(str):
        """
        :param str: 需要加密的字符串
        :return: 加密后的字符串
        """
        data_sha = hashlib.sha256(str.encode('utf-8')).hexdigest()
        return data_sha
