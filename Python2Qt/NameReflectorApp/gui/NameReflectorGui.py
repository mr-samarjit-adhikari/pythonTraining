# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reflector.ui'
#
# Created: Wed Nov  8 16:26:48 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_nameReflectorDialog(object):
    def setupUi(self, nameReflectorDialog):
        nameReflectorDialog.setObjectName("nameReflectorDialog")
        nameReflectorDialog.resize(272, 162)
        self.gridLayout = QtGui.QGridLayout(nameReflectorDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.nameLineEdit = QtGui.QLineEdit(nameReflectorDialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 0, 0, 1, 1)
        self.clickMePB = QtGui.QPushButton(nameReflectorDialog)
        self.clickMePB.setObjectName("clickMePB")
        self.gridLayout.addWidget(self.clickMePB, 0, 1, 1, 1)
        self.displayTextBrowser = QtGui.QTextBrowser(nameReflectorDialog)
        self.displayTextBrowser.setObjectName("displayTextBrowser")
        self.gridLayout.addWidget(self.displayTextBrowser, 1, 0, 1, 2)

        self.retranslateUi(nameReflectorDialog)
        QtCore.QMetaObject.connectSlotsByName(nameReflectorDialog)

    def retranslateUi(self, nameReflectorDialog):
        nameReflectorDialog.setWindowTitle(QtGui.QApplication.translate("nameReflectorDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLineEdit.setPlaceholderText(QtGui.QApplication.translate("nameReflectorDialog", "Write your name", None, QtGui.QApplication.UnicodeUTF8))
        self.clickMePB.setText(QtGui.QApplication.translate("nameReflectorDialog", "Click ME!", None, QtGui.QApplication.UnicodeUTF8))

