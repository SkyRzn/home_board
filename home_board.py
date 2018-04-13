#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mainwindow, css, label
from auth import API_KEY, LOGIN, PASSWORD
from narodmon import Narodmon
from box import Box

CLOCK_FONT = 110
MAIN_FONT = 77

BOX_VAL = 100
CLOCK_COLOR = css.color(200, 255, BOX_VAL)
HOME_COLOR = css.color(50, 255, BOX_VAL)
STREET_COLOR = css.color(75, 255, BOX_VAL)
BALCONY_COLOR = css.color(0, 255, BOX_VAL)


class MainWindow(QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		#self.ui = mainwindow.Ui_MainWindow()
		#self.ui.setupUi(self)

		self.setStyleSheet(css.mainSS('white', 'black', MAIN_FONT, pleft = 5, ptop = 0, border_width = 2))

		self.clockLabel = Box(css.boxSS(CLOCK_COLOR, -10, 0, CLOCK_FONT), 40, 80)
		self.homeLabel = Box(css.boxSS(HOME_COLOR))
		self.streetLabel = Box(css.boxSS(STREET_COLOR))
		self.balconyLabel = Box(css.boxSS(BALCONY_COLOR))

		self.l1 = QVBoxLayout()
		self.l1.addWidget(self.clockLabel)
		self.l1.addWidget(self.homeLabel)

		self.l2 = QVBoxLayout()
		self.l2.addWidget(self.streetLabel)
		self.l2.addWidget(self.balconyLabel)

		self.l = QHBoxLayout()
		self.l.addLayout(self.l1)
		self.l.addLayout(self.l2)

		self.setLayout(self.l)

		#self.ui.clockLabel.setStyleSheet(css.boxSS(CLOCK_COLOR, -10, 0, CLOCK_FONT))
		#self.ui.homeLabel.setStyleSheet(css.boxSS(HOME_COLOR))
		#self.ui.streetLabel.setStyleSheet(css.boxSS(STREET_COLOR))
		#self.ui.balconyLabel.setStyleSheet(css.boxSS(BALCONY_COLOR))

		#self.showFullScreen()

		#label.setOptions(40, 80)

		self.nm = Narodmon(API_KEY, LOGIN, PASSWORD)
		if not self.nm.auth():
			self.nm = None
			print 'Narodmon failed'

		self.timer = QTimer(self)
		self.timer.timeout.connect(self.setValues)
		self.timer.start(60*1000)
		self.setValues()

	def setValues(self):
		if not self.nm:
			return
		data = self.nm.dev_sensors(450)
		bt = 0
		bh = 0

		sensors = data['sensors']
		for sensor in sensors:
			if sensor['id'] == 6374:
				bt = sensor['value']
			elif sensor['id'] == 16626:
				bh = sensor['value']

		self.clockLabel.setText(time.strftime('%H:%M'))
		self.homeLabel.setText(label.PTH(p = 000.0, t = -00.00, h = 000.0))
		self.streetLabel.setText(label.PTH(t = 00.00, h = 000.0))
		self.balconyLabel.setText(label.PTH(t = bt, h = bh))


app = QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
