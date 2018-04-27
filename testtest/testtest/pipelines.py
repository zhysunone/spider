# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient

class TesttestPipeline(object):
    def process_item(self, item, spider):
        return item


# class Mongopipclass(object):
#     def __init__(self):
#         try:
#             client = MongoClient("192.168.15.34", 27017)
#             db = client.zihuaiyan
#             self.collection = db.huangye88_url
#         except:
#             pass
#
#     def process_item(self, item, spider):
#         try:
#             self.collection.insert({
#                 "_id":item["urls"],
#                 "content":item["content"]
#             })
#         except Exception as e:
#             print e
#         else:
#             print "content insert success...."
#
#         return item




# 存入hbase

import happybase
from happybase_monkey.monkey import monkey_path;monkey_path()

class HBaseClass(object):
    def __init__(self):
        try:
            self.conn = happybase.Connection("", )
            # 测试所用的表
            self.table = self.conn.table("")
        except Exception as e:
            print("make connection error %s" % e)

    def process_item(self, item, spider):
        try:
            self.table.put(item["urls"], {"info:content": item["content"]})
        except Exception as e:
            print("insert error %s"%e)
            print("make a new connection")
            self.conn = happybase.Connection("", )
            self.table = self.conn.table("")
        else:
            print "content insert success!!!"

        return item
