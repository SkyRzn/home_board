#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui
import mainwindow, css, label

CLOCK_FONT = 110
MAIN_FONT = 77

CLOCK_COLOR = css.color(200, 255, 48)
HOME_COLOR = css.color(50, 255, 48)
STREET_COLOR = css.color(75, 255, 48)
BALCONY_COLOR = css.color(0, 255, 48)


class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = mainwindow.Ui_MainWindow()
		self.ui.setupUi(self)

		self.setStyleSheet(css.mainSS('white', 'black', MAIN_FONT, ptop = 0))

		self.ui.clockLabel.setStyleSheet(css.boxSS(CLOCK_COLOR, -10, 0, CLOCK_FONT))
		self.ui.homeLabel.setStyleSheet(css.boxSS(HOME_COLOR))
		self.ui.streetLabel.setStyleSheet(css.boxSS(STREET_COLOR))
		self.ui.balconyLabel.setStyleSheet(css.boxSS(BALCONY_COLOR))

		label.setOptions(40, 80)

		self.setValues()

	def setValues(self):
		self.ui.clockLabel.setText('22:11')
		self.ui.homeLabel.setText(label.PTH(p = 777.7, t = -66.66, h = 100.0))
		self.ui.streetLabel.setText(label.PTH(t = 88.88, h = 100.0))
		self.ui.balconyLabel.setText(label.PTH(t = 6.78, h = 10.0))

		print self.geometry()

	#def advanceSlider(self):
		#self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)


app = QtGui.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
