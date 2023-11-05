from PyQt5.QtWidgets import QApplication


app = QApplication([])
from main_window import *


def switch_box():
    if btn_next.text() == "відповісти":
        RadioGroupBox.hide()
        ...
        btn_next.setText("Наступне питання")

    if btn_next.text() == "Наступне питання":
        RadioGroupBox.show()
        ...
        btn_next.setText("відповісти")

btn_next.clicked.connect(switch_box)


window.show()
app.exec()