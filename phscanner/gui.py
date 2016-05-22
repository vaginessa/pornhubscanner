# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt-resources/phs.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(786, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 30))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.actionBox = QtGui.QComboBox(self.centralwidget)
        self.actionBox.setMinimumSize(QtCore.QSize(170, 30))
        self.actionBox.setObjectName(_fromUtf8("actionBox"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBox.addItem(icon, _fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/download.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBox.addItem(icon1, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.actionBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.videoList = QtGui.QListWidget(self.centralwidget)
        self.videoList.setMinimumSize(QtCore.QSize(256, 0))
        self.videoList.setStyleSheet(_fromUtf8("QListView {\n"
"        show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item {\n"
"    padding: 5px;\n"
"}"))
        self.videoList.setAlternatingRowColors(True)
        self.videoList.setObjectName(_fromUtf8("videoList"))
        self.gridLayout.addWidget(self.videoList, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pageBox = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageBox.sizePolicy().hasHeightForWidth())
        self.pageBox.setSizePolicy(sizePolicy)
        self.pageBox.setMinimumSize(QtCore.QSize(115, 30))
        self.pageBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pageBox.setFont(font)
        self.pageBox.setMinimum(1)
        self.pageBox.setMaximum(1000)
        self.pageBox.setObjectName(_fromUtf8("pageBox"))
        self.horizontalLayout_3.addWidget(self.pageBox)
        self.scanButton = QtGui.QPushButton(self.centralwidget)
        self.scanButton.setMinimumSize(QtCore.QSize(0, 30))
        self.scanButton.setAutoDefault(True)
        self.scanButton.setDefault(True)
        self.scanButton.setObjectName(_fromUtf8("scanButton"))
        self.horizontalLayout_3.addWidget(self.scanButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.abortButton = QtGui.QPushButton(self.centralwidget)
        self.abortButton.setEnabled(True)
        self.abortButton.setMinimumSize(QtCore.QSize(35, 27))
        self.abortButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.abortButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/abort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abortButton.setIcon(icon2)
        self.abortButton.setFlat(True)
        self.abortButton.setObjectName(_fromUtf8("abortButton"))
        self.horizontalLayout_2.addWidget(self.abortButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPil = QtGui.QAction(MainWindow)
        self.actionPil.setObjectName(_fromUtf8("actionPil"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.videoList, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.videoList, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QListWidgetItem*)")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pageBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lineEdit.clear)
        QtCore.QObject.connect(self.scanButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.videoList.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PornHubScanner", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/logo.png\"/></p></body></html>", None))
        self.actionBox.setItemText(0, _translate("MainWindow", "Play mode", None))
        self.actionBox.setItemText(1, _translate("MainWindow", "Download mode", None))
        self.scanButton.setText(_translate("MainWindow", "Scan", None))
        self.actionPil.setText(_translate("MainWindow", "pil", None))

from . import icons_rc
