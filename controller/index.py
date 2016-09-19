#coding=utf-8
__author__ = 'i3esn0w'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import pymongo
from bson.objectid import ObjectId
from util.function import time_span, intval
import motor
class IndexHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    
    def get(self, *args, **kwargs):
        user=self.get_current_user()
        self.render("index.html",user=user['username'])
        
    @gen.coroutine
    def get_sort(self):
        sorts = []
        cursor = self.db.sort.find({
            "show": True
        })
        while (yield cursor.fetch_next):
            sorts.append(cursor.next_object())
        raise gen.Return(sorts)
    
class MainHandler(BaseHandler):

    #@gen.coroutine
    def get_content_num(self):
        #client = motor.MotorClient("mongodb://192.243.116.148:27017/")
        conn = pymongo.Connection("192.243.116.148",27017)
        weibo_db = conn["Sina"]
        return  weibo_db['Tweets'].find().count()
    def get_user_count(self):
        conn = pymongo.Connection("192.243.116.148",27017)
        weibo_db = conn["Sina"]        
        return weibo_db['Information'].find().count()
    def get_system_user(self):
        conn = pymongo.Connection("192.243.116.148",27017)
        weibo_db = conn["minblog"]        
        return weibo_db['member'].find().count()        
        
        
    @tornado.web.asynchronous
    @gen.coroutine    
    def get(self):
        count_num=self.get_content_num()
        user_count=self.get_user_count()
        system_user=self.get_system_user()
        self.render("index_v148b2.html",count_num=count_num,user_count=user_count,system_user=system_user)
    