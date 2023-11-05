from PyQt5.QtWidgets import (QWidget,QHBoxLayout,QVBoxLayout,
                             QLabel, QPushButton, QRadioButton,
                             QGroupBox,QButtonGroup)


window = QWidget()
win_width, wind_height = 700,400
window.resize(win_width,wind_height)
window.setWindowTitle("Memory Card. Автор: Максим")

btn_menu = QPushButton("меню")
btn_next = QPushButton("відповісти")
question = QLabel()

rb_answer_1 = QRadioButton()
rb_answer_2 = QRadioButton()
rb_answer_3 = QRadioButton()
rb_answer_4 = QRadioButton()

RadioGroupBox = QGroupBox("варіанти відповіді")
RadioGroup = QButtonGroup()

RadioGroup.addButton(rb_answer_1)
RadioGroup.addButton(rb_answer_2)
RadioGroup.addButton(rb_answer_3)
RadioGroup.addButton(rb_answer_4)


box_h_line = QHBoxLayout()
box_v_line1 = QVBoxLayout()
box_v_line2 = QVBoxLayout()


box_v_line1.addWidget(rb_answer_1)
box_v_line1.addWidget(rb_answer_2)

box_v_line2.addWidget(rb_answer_3)
box_v_line2.addWidget(rb_answer_4)

box_h_line.addLayout(box_v_line1)
box_h_line.addLayout(box_v_line2)

RadioGroupBox.setLayout(box_h_line)


main_v_line = QVBoxLayout()

main_v_line.addWidget(question)

main_v_line.addWidget(RadioGroupBox)

main_v_line.addWidget(btn_next)

window.setLayout(main_v_line)












