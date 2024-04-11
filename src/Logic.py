from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QGridLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(400, 300, 500, 700)
        self.setStyleSheet("background-color: black;")

        self.string = ""

        self.lable_list = []

        layout = QGridLayout()

        self.lable = QLabel("")

        self.button_zero = QPushButton()
        self.button_one = QPushButton()
        self.button_two = QPushButton()
        self.button_three = QPushButton()
        self.button_four = QPushButton()
        self.button_five = QPushButton()
        self.button_six = QPushButton()
        self.button_seven = QPushButton()
        self.button_eleven = QPushButton()
        self.button_nine = QPushButton()

        self.button_delete_all = QPushButton()
        self.button_delete = QPushButton()
        self.button_share = QPushButton()
        self.button_multiply = QPushButton()
        self.button_minus = QPushButton()
        self.button_plus = QPushButton()
        self.bitton_equally = QPushButton()

        self.button_zero.setText("0")
        self.button_one.setText("1")
        self.button_two.setText("2")
        self.button_three.setText("3")
        self.button_four.setText("4")
        self.button_five.setText("5")
        self.button_six.setText("6")
        self.button_seven.setText("7")
        self.button_eleven.setText("8")
        self.button_nine.setText("9")

        self.button_delete_all.setText("Delete All")
        self.button_delete.setText("Delete Last")
        self.button_share.setText("Share")
        self.button_multiply.setText("Multiply")
        self.button_minus.setText("Minus")
        self.button_plus.setText("Plus")
        self.bitton_equally.setText("Result")

        self.lable.setFixedSize(100, 65)
        self.lable.setStyleSheet("QLabel { background-color : black; color : white; }")
        self.lable.setFont(QFont("Arial", 13))

        self.button_zero.setFixedSize(65, 65)
        self.button_zero.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_zero.setFont(QFont("Arial", 13))

        self.button_one.setFixedSize(65, 65)
        self.button_one.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_one.setFont(QFont("Arial", 13))

        self.button_two.setFixedSize(65, 65)
        self.button_two.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_two.setFont(QFont("Arial", 13))

        self.button_three.setFixedSize(65, 65)
        self.button_three.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_three.setFont(QFont("Arial", 13))

        self.button_four.setFixedSize(65, 65)
        self.button_four.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_four.setFont(QFont("Arial", 13))

        self.button_five.setFixedSize(65, 65)
        self.button_five.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_five.setFont(QFont("Arial", 13))

        self.button_six.setFixedSize(65, 65)
        self.button_six.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_six.setFont(QFont("Arial", 13))

        self.button_seven.setFixedSize(65, 65)
        self.button_seven.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_seven.setFont(QFont("Arial", 13))

        self.button_eleven.setFixedSize(65, 65)
        self.button_eleven.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_eleven.setFont(QFont("Arial", 13))

        self.button_nine.setFixedSize(65, 65)
        self.button_nine.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_nine.setFont(QFont("Arial", 13))

        self.button_delete.setFixedSize(85, 65)
        self.button_delete.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_delete.setFont(QFont("Arial", 13))

        self.button_delete_all.setFixedSize(78, 65)
        self.button_delete_all.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_delete_all.setFont(QFont("Arial", 13))

        self.button_minus.setFixedSize(65, 65)
        self.button_minus.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_minus.setFont(QFont("Arial", 13))

        self.button_plus.setFixedSize(65, 65)
        self.button_plus.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_plus.setFont(QFont("Arial", 13))

        self.bitton_equally.setFixedSize(65, 65)
        self.bitton_equally.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.bitton_equally.setFont(QFont("Arial", 13))

        self.button_share.setFixedSize(65, 65)
        self.button_share.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_share.setFont(QFont("Arial", 13))

        self.button_multiply.setFixedSize(65, 65)
        self.button_multiply.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.button_multiply.setFont(QFont("Arial", 13))

        self.button_zero.clicked.connect(self.zero)
        self.button_one.clicked.connect(self.one)
        self.button_two.clicked.connect(self.two)
        self.button_three.clicked.connect(self.three)
        self.button_four.clicked.connect(self.four)
        self.button_five.clicked.connect(self.five)
        self.button_six.clicked.connect(self.six)
        self.button_seven.clicked.connect(self.seven)
        self.button_eleven.clicked.connect(self.eleven)
        self.button_nine.clicked.connect(self.nine)

        self.button_delete_all.clicked.connect(self.delete_all)
        self.button_delete.clicked.connect(self.delete)
        self.button_share.clicked.connect(self.share)
        self.button_multiply.clicked.connect(self.multiply)
        self.button_minus.clicked.connect(self.minus)
        self.button_plus.clicked.connect(self.plus)
        self.bitton_equally.clicked.connect(self.equally)

        layout.addWidget(self.button_zero, 4, 1)

        layout.addWidget(self.button_one, 1, 0)
        layout.addWidget(self.button_two, 1, 1)
        layout.addWidget(self.button_three, 1, 2)
        layout.addWidget(self.button_four, 2, 0)
        layout.addWidget(self.button_five, 2, 1)
        layout.addWidget(self.button_six, 2, 2)
        layout.addWidget(self.button_seven, 3, 0)
        layout.addWidget(self.button_eleven, 3, 1)
        layout.addWidget(self.button_nine, 3, 2)
        layout.addWidget(self.button_delete, 4, 0)
        layout.addWidget(self.button_delete_all, 4, 2)
        layout.addWidget(self.bitton_equally, 4, 3)
        layout.addWidget(self.button_share, 5, 0)
        layout.addWidget(self.button_multiply, 5, 1)
        layout.addWidget(self.button_plus, 5, 2)
        layout.addWidget(self.button_minus, 5, 3)

        layout.addWidget(self.lable, 0, 1)

        widget_one = QWidget()
        widget_one.setLayout(layout)
        self.setCentralWidget(widget_one)


    def zero(self):
        self.lable_list.append("0")
        self.lable.setText("0")

    def one(self):
        self.lable_list.append("1")
        self.lable.setText("1")

    def two(self):
        self.lable_list.append("2")
        self.lable.setText("2")

    def three(self):
        self.lable_list.append("3")
        self.lable.setText("3")

    def four(self):
        self.lable_list.append("4")
        self.lable.setText("4")

    def five(self):
        self.lable_list.append("5")
        self.lable.setText("5")

    def six(self):
        self.lable_list.append("6")
        self.lable.setText("6")

    def seven(self):
        self.lable_list.append("7")
        self.lable.setText("7")

    def eleven(self):
        self.lable_list.append("8")
        self.lable.setText("8")

    def nine(self):
        self.lable_list.append("9")
        self.lable.setText("9")

    def delete_all(self):
        self.lable_list.clear()
        self.lable.setText("")

    def delete(self):
        self.lable_list.pop()
        self.logic()
        self.lable.setText(f"{self.string}")

    def share(self):
        self.lable_list.append("/")
        self.lable.setText("/")

    def multiply(self):
        self.lable_list.append("*")
        self.lable.setText("*")

    def minus(self):
        self.lable_list.append("-")
        self.lable.setText("-")

    def plus(self):
        self.lable_list.append("+")
        self.lable.setText("+")

    def equally(self):

        self.logic()
        self.lable.setText(f"{eval(self.string)}")
        self.lable_list.clear()
        self.lable_list.append(self.string)

    def logic(self):
        for el in self.lable_list:
            self.string += el

