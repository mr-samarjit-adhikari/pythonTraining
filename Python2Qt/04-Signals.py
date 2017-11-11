from PySide.QtGui import *
import sys

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QDial()
        self.dial.setMaximum(150)
        self.dial.setNotchesVisible(True)

        self.spinbox = QSpinBox()
        self.spinbox.setMaximum(150)
        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()