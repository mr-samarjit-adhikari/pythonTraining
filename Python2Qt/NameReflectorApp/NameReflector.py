#/usr/bin/python

import sys
from PySide.QtGui import QApplication, QDialog

from gui.NameReflectorGui import Ui_nameReflectorDialog


class NameReflectorForm(QDialog,Ui_nameReflectorDialog):
    def __init__(self,parent=None):
        super(NameReflectorForm, self).__init__(parent)
        self.setupUi(self)

        self.clickMePB.clicked.connect(self.setTBMessage)

    def setTBMessage(self):
        text = self.nameLineEdit.text()
        self.displayTextBrowser.append("Hello "+text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = NameReflectorForm()
    form.show()
    app.exec_()