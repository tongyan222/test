#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

import pytest,os
import allure
import requests


class TestCase01():
    ip = 'http://192.168.0.254:15010'
    data = {
        'userId': 101618,
        'paperId': 440,
        'examId': 611,
        'jiaojuan': '',
        'pcLoginCheck': 'ec55f7c26643427c89cce00c6f15fe5d',
        'answerPaperCard': [{'key':'01'}],
        'answerTopicCard': [{'key':'01'}],
        'answerQuestionCard': [{'key':'01'}],
        'answerTopicTemp': [[{'key':'01'}]]
    }

    # @pytest.fixture(scope='function')
    def login(self,data):
        print('用例开始')
        url = self.ip +'/answers2/modifyAnswerByUserId.do'

        re=requests.post(url,data)
        print('用例地址：',url)
        print('用例请求参数',data)
        print('用例返回参数',re.text)
        return re



    def test_1(self):
        # self.data['pcLoginCheck']= 'ghhhhhhhhhhhhhmmjmjj'
        # self.login(self.data)

        for i in self.data.keys():
            self.data[i] =''
            self.data['pcLoginCheck'] = 'ec55f7c26643427c89cce00c6f15fe5d'
            time.sleep(2)
            self.login(self.data)






    def test_2(self):
        self.data['pcLoginCheck']= 'ghhhhhhhhhhhhhmmjmjj'
        self.login(self.data)



    def test_3(self):
        print("执行用例2")
        assert 1 == 2



if __name__== "__main__":
    result_dir = 'report/test_report.html'
    pytest.main(["-vs",'--html=%s'%result_dir,'--capture=sys'])
    # os.system("allure generate ../report/tmp -o ../report/report --clean")





