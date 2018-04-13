#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib2
import json
import hashlib
import uuid


class Narodmon:
	def __init__(self, api_key, login, password, lang = 'ru'):
		self.login = login
		self.api_key = api_key
		self.app_id = str(uuid.getnode())
		self.uuid = hashlib.md5(self.app_id).hexdigest()
		self.md5_pass = hashlib.md5(password).hexdigest()
		self.md5_auth = hashlib.md5(self.uuid + self.md5_pass).hexdigest()
		self.lang = lang
		self.uid = None

	def auth(self):
		res = self.cmd('userLogon', {'login': self.login, 'hash': self.md5_auth})

		if not res or not res.get('uid'):
			return False
		self.uid = res['uid']
		return True

	def dev_sensors(self, dev_id):
		return self.cmd('sensorsOnDevice', {'id': dev_id})

	def cmd(self, cmd, data = None):
		if data == None:
			data = {}
		data['cmd'] = cmd
		data['uuid'] = self.uuid
		data['api_key'] = self.api_key
		data['lang'] = self.lang

		try:
			req = urllib2.Request('http://narodmon.ru/api', json.dumps(data))
			resp = urllib2.urlopen(req)
			return json.loads(resp.read())
		except urllib2.URLError, e:
			print 'HTTP error:', e

		except (ValueError, TypeError), e:
			print 'JSON error:', e

		return None

