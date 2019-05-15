# -*- coding:utf-8 -*-
from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    respons = input("language: ")
    if respons == 'q':
        break
    my_survey.store_response(respons)

my_survey.show_results()
