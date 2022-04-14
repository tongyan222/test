import json

import pytest
import requests
# from db_fixture.excel import db
from db_fixture.func import fun

# db=db()
@pytest.fixture()
def login(method,url,data):
    """
    验证码登录----（流程：先发送验证码，再登录，测试验证码固定666666）
    :param request:phoneNum
    :return:phoneLoginCheck
    """

    # data = request.param
    print(f"== 账号是：{data} ==")
    # res = fun.run_method(method,url,data)
    #获取返回的token
    # phoneLoginCheck = json.loads(res)['']
    # return phoneLoginCheck


file_path = ''
# url=db.readExcel(file_path)
data = [
    {'phoneNum':'183202010263','loginRoleType':'10'},
    {'phoneNum':'182044444444','loginRoleType':'10'}
]
ids = [f"login_test_name is:{name}" for name in data]

"""
（1）添加  indirect=True  参数是为了把 login 当成一个函数去执行，而不是一个参数，并且将data当做参数传入函数
（2）def test_name(login) ，这里的login是获取fixture返回的值
"""


@pytest.mark.parametrize("login", data, ids=ids, indirect=True)
def test_name(login):
    print(f" 测试用例的登录账号是：{login} ")


if __name__=="__main__":
    pytest.main['test_name','-v']
