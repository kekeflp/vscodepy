# -*- coding:utf-8 -*-
import unittest
from survey import AnonymousSurvey

'''
单元测试的6大要点：
1、引入unittest测试模块，和被测类模块
2、编写测试类（Test+被测类名）的形式，且继承unittest.TestCase
3、内部方法也是以test开头
4、使用断言assertIn()等方法
5、结尾使用unittest.main()进行启用测试类
6、使用def setUp(self) 函数（大小写不能拼错，否则无法识别），
   相对于预置条件的作用。
'''


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        # 首先把多个答案存储到列表
        self.responses = ['English', 'Chineses', 'Spanish']

    # 测试单个答案是否能被正确存储
    def test_store_sigle_responses(self):
        self.my_survey.store_response(self.responses[0])
        # 断言如果English能正确被存储到列表，则通过测试，否则失败。
        self.assertIn(self.responses[0], self.my_survey.responses)

    # 测试多个答案是否能被正确存储
    def test_store_mulit_responses(self):
        for i in self.responses:
            self.my_survey.store_response(i)
        # 断言如果多个答案能正确被存储到列表，则通过测试，否则失败。
        for i in self.responses:
            self.assertIn(i, self.my_survey.responses)


unittest.main()
