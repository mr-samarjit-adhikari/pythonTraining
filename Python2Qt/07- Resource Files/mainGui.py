# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Nov  8 06:02:24 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(189, 177)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(mainDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.archButton = QtGui.QPushButton(mainDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/arch-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archButton.setIcon(icon1)
        self.archButton.setIconSize(QtCore.QSize(32, 32))
        self.archButton.setObjectName("archButton")
        self.gridLayout.addWidget(self.archButton, 0, 0, 1, 1)
        self.fedoraButton = QtGui.QPushButton(mainDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/fedora-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fedoraButton.setIcon(icon2)
        self.fedoraButton.setIconSize(QtCore.QSize(32, 32))
        self.fedoraButton.setObjectName("fedoraButton")
        self.gridLayout.addWidget(self.fedoraButton, 1, 0, 1, 1)
        self.windowsButton = QtGui.QPushButton(mainDialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/windows-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.windowsButton.setIcon(icon3)
        self.windowsButton.setIconSize(QtCore.QSize(32, 32))
        self.windowsButton.setFlat(False)
        self.windowsButton.setObjectName("windowsButton")
        self.gridLayout.addWidget(self.windowsButton, 2, 0, 1, 1)

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Pick an OS", None, QtGui.QApplication.UnicodeUTF8))
        self.archButton.setText(QtGui.QApplication.translate("mainDialog", "Load Arch", None, QtGui.QApplication.UnicodeUTF8))
        self.fedoraButton.setText(QtGui.QApplication.translate("mainDialog", "Load Fedora", None, QtGui.QApplication.UnicodeUTF8))
        self.windowsButton.setText(QtGui.QApplication.translate("mainDialog", "Load Windows", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
