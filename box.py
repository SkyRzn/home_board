# -*- coding: utf-8 -*-


from PyQt4.QtGui import *
from PyQt4.QtCore import *
import css


class Box(QLabel):
	def __init__(self, style, smallFont=50, interval=50):
		super(Box, self).__init__()

		self.smallFont = smallFont
		self.interval = interval

		self.setStyleSheet(style)

	def setValues(self, p = None, t = None, h = None):
		text = '<html><head/><body>\n'

		line = '<p style="line-height:%d">%%s<span style=" font-size:%dpx;"> мм</span></p>\n' % (self.interval, self.smallFont)

		if p != None:
			text += line % ('%.1f' % p)
		if t != None:
			text += line % ('%.2f' % t)
		if h != None:
			text += line % ('%.2f' % h)
		text += '</body></html>\n'

		self.setText(QString.fromUtf8(text))

