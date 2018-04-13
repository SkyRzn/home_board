# -*- coding: utf-8 -*-

from PyQt4.QtGui import QColor


BG = '#000000'

GRADIENT_PATTERN = """qlineargradient(spread:pad,
x1:0, y1:0,
x2:0, y2:1,
stop:0 %s,
stop:1 %s
);"""



def color(h, s, v):
	c = QColor()
	c.setHsv(h, s, v)
	return c.name()

def gradient(c1, c2):
	return GRADIENT_PATTERN % (c1, c2)

def mainSS(col, bgcol, font, pleft = 10, ptop = 0, border_width = 1, border_radius = 10):
	res = '* {\n'
	res += '  color: %s;\n' % col
	res += '  background-color: %s;\n' % bgcol
	res += '}\n'

	res += 'QLabel {\n'
	res += '  border-width: %dpx;\n' % border_width
	res += '  border-radius: %dpx;\n' % border_radius
	res += '  font: %dpx;\n' % font
	res += '  padding-left: %dpx;\n' % pleft
	res += '  padding-right: -10px;\n'
	res += '  padding-top: %dpx;\n' % ptop
	res += '  border-style: solid;\n'
	res += '}\n'

	return res

def boxSS(col, ptop = None, pleft = None, font = None):
	res = 'background-color: %s;\n' % gradient(BG, col)
	res += 'border-color: %s;\n' % col
	if font != None:
		res += 'font: %dpx;\n' % font
	if ptop != None:
		res += 'padding-top: %dpx;\n' % ptop
	if pleft != None:
		res += 'padding-left: %dpx;\n' % pleft
	return res
