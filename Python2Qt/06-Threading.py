from PySide.QtCore import *
from PySide.QtGui import *
import sys,time

import showGui

class MainDialog(QDialog,showGui.Ui_mainDialog):

    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self)

        self.connect(self.showButton, SIGNAL("clicked()"), self.processData)
        self.workerThread = WorkerThread()
        self.connect(self.workerThread,SIGNAL("threadDone(QString)"),self.threadDone)

    def processData(self):
        self.workerThread.start()
        QMessageBox.information(self,"Hello!","Hello "+self.nameEdit.text())

    def threadDone(self,param):
        QMessageBox.warning(self,"Warning!","Thread Execution Completed")
        print ("param passed as "+param)


class WorkerThread(QThread):

    def __init__(self,parent=None):
        super(WorkerThread,self).__init__(parent)

    def run(self):
        time.sleep(5)
        self.emit(SIGNAL("threadDone(QString)"),"This is QString param")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()