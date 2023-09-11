from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from ui_calculator import Ui_Calculator

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.setWindowTitle('Calculator')

        self.ui.button_1.clicked.connect(self.method_1)
        self.ui.button_2.clicked.connect(self.method_2)
        self.ui.button_3.clicked.connect(self.method_3)
        self.ui.button_4.clicked.connect(self.method_4)
        self.ui.button_5.clicked.connect(self.method_5)
        self.ui.button_6.clicked.connect(self.method_6)
        self.ui.button_7.clicked.connect(self.method_7)
        self.ui.button_8.clicked.connect(self.method_8)
        self.ui.button_9.clicked.connect(self.method_9)
        self.ui.button_0.clicked.connect(self.method_zero)
        self.ui.point.clicked.connect(self.method_point)
        self.ui.sum.clicked.connect(self.method_plus)
        self.ui.sub.clicked.connect(self.method_min)
        self.ui.multiple.clicked.connect(self.method_mult)
        self.ui.division.clicked.connect(self.method_div)
        self.ui.equal.clicked.connect(self.method_equal)
        self.ui.clear.clicked.connect(self.method_clear)
        self.ui.delete_2.clicked.connect(self.method_del)


    def omit_decimal(self, value : int | float) -> int | float:
        if int(value) == value:
            return int(value)
        return value

    def method_1(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"1")

    def method_2(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"2")

    def method_3(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"3")

    def method_4(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"4")

    def method_5(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"5")

    def method_6(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"6")

    def method_7(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"7")

    def method_8(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"8")

    def method_9(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"9")
        
    def method_zero(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"0")

    def method_point(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+".")

    def method_plus(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"+")

    def method_min(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"-")

    def method_mult(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"*")

    def method_div(self):
        text=self.ui.label.text()
        self.ui.label.setText(text+"/")

    def method_clear(self):
        self.ui.label.setText("")

    def method_del(self):
        text=self.ui.label.text()
        self.ui.label.setText(text[:len(text)-1])

    def method_equal(self):
        text=self.ui.label.text()

        try:
            ans = eval(text)
            ans = self.omit_decimal(ans)
            self.ui.label.setText(str(ans))
        except:
            self.ui.label.setText("Wrong Input")
    
