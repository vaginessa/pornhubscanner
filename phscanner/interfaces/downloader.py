# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt-resources/downloader.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Download(object):
    def setupUi(self, Download):
        Download.setObjectName(_fromUtf8("Download"))
        Download.resize(480, 70)
        self.gridLayout = QtGui.QGridLayout(Download)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.progressBar = QtGui.QProgressBar(Download)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.abortButton = QtGui.QPushButton(Download)
        self.abortButton.setEnabled(True)
        self.abortButton.setMinimumSize(QtCore.QSize(35, 27))
        self.abortButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.abortButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/abort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abortButton.setIcon(icon)
        self.abortButton.setFlat(True)
        self.abortButton.setObjectName(_fromUtf8("abortButton"))
        self.gridLayout.addWidget(self.abortButton, 0, 1, 1, 1)

        self.retranslateUi(Download)
        QtCore.QMetaObject.connectSlotsByName(Download)

    def retranslateUi(self, Download):
        Download.setWindowTitle(_translate("Download", "PornHubScanner - Downloader", None))

from . import icons_rc
