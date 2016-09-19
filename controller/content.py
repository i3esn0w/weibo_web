#coding=utf-8
__author__ = 'i3esn0w'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import pymongo
from bson.objectid import ObjectId
from util.function import time_span, intval
import motor


class ContentHandler(BaseHandler):
    def get_weibo_content(self):
        conn = pymongo.Connection("192.243.116.148",27017)
        weibo_db = conn["Sina"]
        text=weibo_db.Tweets.find()
        return text
    def get(self):
        text=self.get_weibo_content()
        count = text.count()
        limit = 20
        page = self.get_argument('page')
        page=intval(page)
        if not page or page <= 0 : page = 1
        text.sort([('Pubtime', pymongo.DESCENDING)]).limit(limit).skip((page - 1) * limit)
        self.render('content.html',text=text,page = page,count = count, each = limit)

class WbUserHandler(BaseHandler):
    def get_weibo_user(self):
        conn = pymongo.Connection("192.243.116.148",27017)
        weibo_db = conn["Sina"]
        text=weibo_db.Information.find()
        return text
    def get(self):
        text=self.get_weibo_user()
        count = text.count()
        limit = 20
        page = self.get_argument('page')
        page=intval(page)
        if not page or page <= 0 : page = 1
        text.sort([("NickName", pymongo.DESCENDING)]).limit(limit).skip((page - 1) * limit)
        self.render('user.html',text=text,page = page,count = count, each = limit)
    
    