#coding=utf-8
__author__ = 'i3esn0w'
import tornado.web
from controller.base import BaseHandler
from tornado import gen
import pymongo
from bson.objectid import ObjectId
from util.function import time_span, intval
import motor

class TableHandler(BaseHandler):
    def get(self):
        pass