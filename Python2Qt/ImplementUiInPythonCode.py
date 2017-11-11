from PySide.QtCore import *
from PySide.QtGui import *
import sys

import showGui

class MainDialog(QDialog,showGui.Ui_mainDialog):

    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)

        self.connect(self.showButton,SIGNAL("clicked()"),self.showMsgDlg)

    def showMsgDlg(self):
        QMessageBox.information(self,"Hello!","Hello "+self.nameEdit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()