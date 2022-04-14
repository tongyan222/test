import requests


class Oss_Api():
    url="http://192.192.192.53:9001/" #后台IP
    url = url + "/v240/oilFume/list"  # 接口地址
    print(url)
    def oilFume(self):
        """
        POST
        分页获取油烟管控查询记录
        return:data
        """
        data={
            "pageNum":1,
            "pageSize":20,
            "tel":"",#手机号码
            "address":'',#查询地址
            "result":"", #NOT_CONTROLLED，UNCERTAIN
            "visited":False

        }
        print(type(data))
        return data

    def methon(self,data):
        result = requests.post(self.url,json=data)
        print(result.text)
        return result

    def case1(self):
        #未回访的查询
        data=self.oilFume()
        data['visited'] =True
        print(data)
        return data


if __name__ == "__main__":
    a=Oss_Api()
    data=a.case1()
    c=a.methon(data)