# -*- coding: utf-8 -*-
####### FIXME remove


from PyQt4.QtCore import QString


smallFont = 50
lineHeight = 50

def setOptions(font, height):
	global smallFont, lineHeight
	smallFont = font
	lineHeight = height

def PTH(p = None, t = None, h = None):
	global smallFont, lineHeight

	res = '<html><head/><body>\n'

	if p != None:
		res += '<p style="line-height:%d">%.1f<span style=" font-size:%dpx;"> мм</span></p>\n' % (lineHeight, p, smallFont)
	if t != None:
		res += '<p style="line-height:%d">%.2f<span style=" font-size:%dpx;"> °C</span></p>\n' % (lineHeight, t, smallFont)
	if h != None:
		res += '<p style="line-height:%d">%.2f<span style=" font-size:%dpx;"> %%</span></p>\n' % (lineHeight, h, smallFont)
	res += '</body></html>\n'

	return QString.fromUtf8(res)

