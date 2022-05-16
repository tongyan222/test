#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pytest


if __name__ == "__main__":
    result_dir  = 'report/test_report.html'
    pytest.main(['-s','-v','--html=%s'%result_dir,'--capture=sys','yongli/lianxi.py::TestCase01::test_1'])
    # ret = os.system('allure generate --clean %s -o %s'%(result_dir,report))
    # os.system("allure generate ../report/tmp -o ../report/report --clean")
    #
    # # if ret:
    # #     print('生成测试报告成功')
    # # else:
    # #     print('生成报告失败')


