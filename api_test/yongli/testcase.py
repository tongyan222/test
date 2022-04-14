# -*- coding:utf-8 -*-
import pytest

from db_fixture.excel import db
from db_fixture.func import fun

DB = db()


@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")

    request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
    print('setup_function called.')


@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")

    request.addfinalizer(teardown_module)
    print('setup_module called.')


# @pytest.mark.select
class TestClass():

    def setup_method(self):
        print("用例开始")
        file_path = r'F:/快快/版本管理/快快2.5.0/快快V2.5.0接口测试用例.xlsx'
        i = 3
        con = DB.readExcel(file_path, i)
        self.method = con[0]
        self.url = con[1]
        self.data = con[2]
        self.header = con[3]

    def teardown_method(self):
        print("用例结束")

    def test_1(self):
        print('Test_1 called.')
        res = fun.run_method(self.method, self.url, self.data, self.header)
        assert res['code'] == 0

        print(res)

    def test_2(setup_module):
        print('Test_2 called.')

    def test_3(setup_module):
        print('Test_3 called.')
        assert 2 == 1 + 1  # 通过assert断言确认测试结果是否符合预期


if __name__ == '__main__':
    pytest.main(['-s', 'yongli.py::TestClass::test_1'])  # 调用pytest的main函数执行测试
