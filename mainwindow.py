# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        MainWindow.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 10000))
        MainWindow.setStyleSheet(_fromUtf8("* {\n"
"    color: #ffffff;\n"
"    background-color: black;\n"
"}\n"
"\n"
"QLabel {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: #aaaaaa;\n"
"    border-radius: 5px;\n"
"    font: 75px;\n"
"    padding-left: 10px;\n"
"}\n"
""))
        self.horizontalLayout = QtGui.QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.clockLabel = QtGui.QLabel(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clockLabel.sizePolicy().hasHeightForWidth())
        self.clockLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clockLabel.setFont(font)
        self.clockLabel.setStyleSheet(_fromUtf8("font: 100px;\n"
"padding-top: -10px;\n"
"padding-left: 0px;\n"
"background-color: qlineargradient(spread:pad,\n"
"x1:0, y1:0,\n"
"x2:0, y2:1,\n"
"stop:0 rgba(0, 0, 0, 255),\n"
"stop:1 rgba(0, 48, 64, 255)\n"
");\n"
"border-color: rgba(0, 48, 64, 255);\n"
""))
        self.clockLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.clockLabel.setTextFormat(QtCore.Qt.RichText)
        self.clockLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.clockLabel.setIndent(0)
        self.clockLabel.setObjectName(_fromUtf8("clockLabel"))
        self.verticalLayout_2.addWidget(self.clockLabel)
        self.homeLabel = QtGui.QLabel(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeLabel.sizePolicy().hasHeightForWidth())
        self.homeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.homeLabel.setFont(font)
        self.homeLabel.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad,\n"
"x1:0, y1:0,\n"
"x2:0, y2:1,\n"
"stop:0 rgba(0, 0, 0, 255),\n"
"stop:1 rgba(64, 48, 0, 255)\n"
");\n"
""))
        self.homeLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.homeLabel.setTextFormat(QtCore.Qt.RichText)
        self.homeLabel.setIndent(0)
        self.homeLabel.setObjectName(_fromUtf8("homeLabel"))
        self.verticalLayout_2.addWidget(self.homeLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.streetLabel = QtGui.QLabel(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.streetLabel.sizePolicy().hasHeightForWidth())
        self.streetLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.streetLabel.setFont(font)
        self.streetLabel.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad,\n"
"x1:0, y1:0,\n"
"x2:0, y2:1,\n"
"stop:0 rgba(0, 0, 0, 255),\n"
"stop:1 rgba(32, 48, 0, 255)\n"
");\n"
""))
        self.streetLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.streetLabel.setTextFormat(QtCore.Qt.RichText)
        self.streetLabel.setIndent(0)
        self.streetLabel.setObjectName(_fromUtf8("streetLabel"))
        self.verticalLayout.addWidget(self.streetLabel)
        self.balconyLabel = QtGui.QLabel(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.balconyLabel.sizePolicy().hasHeightForWidth())
        self.balconyLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.balconyLabel.setFont(font)
        self.balconyLabel.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad,\n"
"x1:0, y1:0,\n"
"x2:0, y2:1,\n"
"stop:0 rgba(0, 0, 0, 255),\n"
"stop:1 rgba(76, 0, 0, 255)\n"
");\n"
""))
        self.balconyLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.balconyLabel.setTextFormat(QtCore.Qt.RichText)
        self.balconyLabel.setIndent(0)
        self.balconyLabel.setObjectName(_fromUtf8("balconyLabel"))
        self.verticalLayout.addWidget(self.balconyLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Home board", None))
        self.clockLabel.setText(_translate("MainWindow", "18:22", None))
        self.homeLabel.setText(_translate("MainWindow", "<html><head/><body><p>760.0 <span style=\" font-size:50px;\">мм</span><br/>-12.85 <span style=\" font-size:50px;\">°C</span><br/>100.0 <span style=\" font-size:50px;\">%</span></p></body></html>", None))
        self.streetLabel.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.balconyLabel.setText(_translate("MainWindow", "<html><head/><body><p>-12.85 <span style=\" font-size:50px;\">°C</span></p><p>100.0 <span style=\" font-size:50px;\">%</span></p></body></html>", None))

