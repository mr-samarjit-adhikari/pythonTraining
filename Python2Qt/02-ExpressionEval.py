import sys

from PySide.QtCore import SIGNAL
from PySide.QtGui import QApplication, QDialog, QTextBrowser, QLineEdit, QVBoxLayout


class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        self.resultList = QTextBrowser()
        self.resultInput = QLineEdit("Enter an expression and press Return key")

        layout = QVBoxLayout()
        layout.addWidget(self.resultList)
        layout.addWidget(self.resultInput)
        self.setLayout(layout)

        self.resultInput.selectAll()
        self.resultInput.setFocus()

        # New way of Connect the signal
        self.resultInput.returnPressed.connect(self.compute)
        # Old Way of connect signal. Does not throw any error
        #self.connect(self.resultInput,SIGNAL("returnPressed()"),self.compute)


    def compute(self):
        try:
            text = self.resultInput.text()
            self.resultList.append("{0} = <b> {1} </b>".format(text,eval(text)))
        except:
            self.resultList.append("<font color=red /><b> Expression invalid </b>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()