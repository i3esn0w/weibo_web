#encoding:utf8

import tornado.web, time, re, pymongo
from controller.base import BaseHandler
from tornado import gen
from bson.objectid import ObjectId
#from util.captcha import Captcha
from util.function import intval, not_need_login, time_span




class LoginHandler(BaseHandler):
	@not_need_login
	def prepare(self):
		BaseHandler.prepare(self)

    	def get(self):
        	self.render('login.html')
        def post(self):
        	username=self.get_argument('username')
        	password=self.get_argument('password')
        	if username==password:
        		self.write("log in ")
