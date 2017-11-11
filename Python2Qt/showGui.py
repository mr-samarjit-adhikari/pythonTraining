# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created: Tue Nov  7 07:03:45 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(375, 61)
        self.nameEdit = QtGui.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(10, 20, 241, 27))
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.showButton = QtGui.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(270, 20, 91, 27))
        self.showButton.setObjectName("showButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)
        mainDialog.setTabOrder(self.showButton, self.nameEdit)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Main Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.nameEdit.setPlaceholderText(QtGui.QApplication.translate("mainDialog", "what is your name", None, QtGui.QApplication.UnicodeUTF8))
        self.showButton.setText(QtGui.QApplication.translate("mainDialog", "Show!", None, QtGui.QApplication.UnicodeUTF8))

