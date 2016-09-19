#coding=utf-8
import tornado.web, time, json,  hashlib
from controller.base import BaseHandler
from util.function import not_need_login, hash
from tornado import gen
from tornado.escape import url_escape, utf8
from model.user import UserModel
#from util.captcha import Captcha
from util.sendemail import Sendemail
try:
	from cStringIO import StringIO
except:
	from StringIO import StringIO




class LoginHandler(BaseHandler):
	def initialize(self):
		BaseHandler.initialize(self)
		

	@not_need_login
	def prepare(self):
		BaseHandler.prepare(self)

	def get(self):
		self.render("login.html")

	@tornado.web.asynchronous
	@gen.coroutine
	def post(self):
		try:
			username = self.get_body_argument('username', default="")
			password = self.get_body_argument('password', default="")
			remember='off'

			# check captcha
			#captcha = self.get_body_argument("captcha", default="")
			#if self.settings["captcha"]["login"] and not Captcha.check(captcha, self):
				#self.custom_error("验证码错误")

			user = yield self.db.member.find_one({"username": username})
			check = yield self.backend.submit(hash.verify, password, user.get("password"))
			if check and user["power"] >= 0:
				session = self.set_session(user)
				if remember == "on":
					cookie_json = json.dumps(session)
					self.set_secure_cookie("user_info", cookie_json, expires_days = 30, httponly = True)
				yield self.db.member.find_and_modify({"username": username},{
				        "$set": {
				                "logintime": time.time(),
				                "loginip": self.get_ipaddress()
				        }
				})
				self.redirect("/index")
			else:
				assert False
		except tornado.web.Finish:
			pass
		except:
			import traceback
			print traceback.print_exc()
			self.custom_error("用户名或密码错误或账号被禁用", jump = "/login")
