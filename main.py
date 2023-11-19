from PyQt5.QtWidgets import QApplication
from random import choice, shuffle


app = QApplication([])
from main_window import *

class Question:
    def __init__(self,question_text, ans, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.answer = ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    ...

q1 = Question("Дім","house","hose","horse","mouse")
q2 = Question("Текст","text","trs","trans","train")
q3 = Question("Ялина","tree","trom","transgender","turkie")
q4 = Question("Літак","plane","plone","plus","perpen")
q5 = Question("Трикутник","triangle","tros","trom","truck")
q6 = Question("Рятівник","savior","sals","self","sqwer")

radio_list = [rb_answer_1,rb_answer_2,rb_answer_3,rb_answer_4]
question_list = [q1,q2,q3,q4,q5,q6]


def next_question():
    current_qustion = choice(question_list)
    question.setText(current_qustion.question_text)
    shuffle(radio_list)
    radio_list[0].setText(current_qustion.answer)
    radio_list[1].setText(current_qustion.wrong1)
    radio_list[2].setText(current_qustion.wrong2)
    radio_list[3].setText(current_qustion.wrong3)

    correct_answer.setText(current_qustion.answer)

next_question()

def check_result():
    RadioGroup.setExclusive(False)
    for b in radio_list:
        if b.isChecked():
            if b.text() == correct_answer.text():
                result_text.setText("Правильно,excelent")
            else:
                result_text.setText("неправильно гавно")
            b.setChecked(False)

    RadioGroup.setExclusive(True)


def switch_box():
    if btn_next.text() == "відповісти":
        check_result()
        RadioGroupBox.hide()
        AnswerGroupBox.show()
        btn_next.setText("Наступне питання")

    elif btn_next.text() == "Наступне питання":
        RadioGroupBox.show()
        AnswerGroupBox.hide()
        btn_next.setText("відповісти")
        next_question()

btn_next.clicked.connect(switch_box)


window.show()
app.exec()