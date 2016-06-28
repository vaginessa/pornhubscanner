# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/egx/git/phs/qt-resources/error.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(300, 120)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stopLabel = QtGui.QLabel(Dialog)
        self.stopLabel.setText(_fromUtf8(""))
        self.stopLabel.setTextFormat(QtCore.Qt.RichText)
        self.stopLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/action-unavailable-symbolic.symbolic.png")))
        self.stopLabel.setScaledContents(False)
        self.stopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stopLabel.setObjectName(_fromUtf8("stopLabel"))
        self.gridLayout.addWidget(self.stopLabel, 0, 0, 1, 1)
        self.errorLabel = QtGui.QLabel(Dialog)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.gridLayout.addWidget(self.errorLabel, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 30))
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.buttonBox.setStyleSheet(_fromUtf8("QDialogButtonBox {\n"
"dialogbuttonbox-buttons-have-icons: 0;\n"
"}"))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PornHubScanner - Error!", None))
        self.errorLabel.setText(_translate("Dialog", "TextLabel", None))

from . import icons_rc
