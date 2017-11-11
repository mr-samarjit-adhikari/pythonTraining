from PySide.QtCore import Signal
from PySide.QtGui import *
import sys


class ZeroSpinBox(QSpinBox):

    zeros = 0 #Class variable
    atZero = Signal(int)

    def __init__(self,parent=None):
        super(ZeroSpinBox,self).__init__(parent)

        self.valueChanged.connect(self.check_zero)

    def check_zero(self,value):
        if value==0:
            self.zeros += 1;
            self.atZero.emit(self.zeros)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)
        self.spinbox.atZero.connect(self.printValue)


    def printValue(self, zeros):
        print ("The SpinBox has been at zero {0} times".format(zeros))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()