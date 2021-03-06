# -*- coding:utf-8 -*-


class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    # 显示问题
    def show_question(self):
        print(self.question)

    # 存储答案
    def store_response(self, new_response):
        self.responses.append(new_response)

    # 显示答案
    def show_results(self):
        print("Survey results: ")
        for i in self.responses:
            print(" - " + str(i))
