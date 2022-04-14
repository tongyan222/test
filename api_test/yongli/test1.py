#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest,os
import allure


class TestCase():

    @pytest.fixture(scope='function')
    def login(self,request):
        # print('登录')
        name = request.param
        print(f"前置条件{name}")
        yield
        print("注销")

    name = ['登录账号和密码1','222222']
    ids = [f"登录名:{name}" for name in name]

    @pytest.mark.parametrize( "login",name,ids=ids,indirect=True)
    def test_1(self,login):
        print('测试用例1')

    @pytest.mark.app
    # 标记app
    def test_2(self):
        print('测试用例2',"_"*100)
        dir(str)
        assert 1==1

    @pytest.mark.skip(reason='该用例跳过执行')
    def test_3(self,login):
        print("执行用例2")
        assert 1 == 2



if __name__== "__main__":
    pytest.main(["-vs",'-m','app'])
    # os.system("allure generate ../report/tmp -o ../report/report --clean")





