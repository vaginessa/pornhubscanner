# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/egx/git/phs/qt-resources/main.ui'
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
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pageLabel = QtGui.QLabel(self.centralwidget)
        self.pageLabel.setObjectName(_fromUtf8("pageLabel"))
        self.horizontalLayout.addWidget(self.pageLabel)
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
        self.horizontalLayout.addWidget(self.pageBox)
        self.scanButton = QtGui.QPushButton(self.centralwidget)
        self.scanButton.setMinimumSize(QtCore.QSize(0, 30))
        self.scanButton.setAutoDefault(True)
        self.scanButton.setDefault(True)
        self.scanButton.setObjectName(_fromUtf8("scanButton"))
        self.horizontalLayout.addWidget(self.scanButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout_2.addWidget(self.playButton)
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/download.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon1)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout_2.addWidget(self.downloadButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPil = QtGui.QAction(MainWindow)
        self.actionPil.setObjectName(_fromUtf8("actionPil"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.scanButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.videoList.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PornHubScanner", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/logo.png\"/></p></body></html>", None))
        self.pageLabel.setText(_translate("MainWindow", "Page:", None))
        self.scanButton.setText(_translate("MainWindow", "Scan", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.downloadButton.setText(_translate("MainWindow", "Download", None))
        self.actionPil.setText(_translate("MainWindow", "pil", None))

from . import icons_rc
