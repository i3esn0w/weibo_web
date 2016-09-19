#coding=utf-8
__author__ = 'i3esn0w'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import pymongo
from bson.objectid import ObjectId
from util.function import time_span, intval

class IndexHandler(BaseHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render("index.html")
        
    @gen.coroutine
    def get_sort(self):
        sorts = []
        cursor = self.db.sort.find({
            "show": True
        })
        while (yield cursor.fetch_next):
            sorts.append(cursor.next_object())
        raise gen.Return(sorts)