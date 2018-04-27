# _*_ coding:utf-8 _*_

__author__ = "zhy"
__date__ = "2018/4/12 14:25"

import scrapy
# from pymongo import MongoClient
import redis
from testtest.items import TesttestItem

class TestSpider(scrapy.Spider):
    name = "test"

    cookie = {
         "_ga": "GA1.2.1629770587.1520296856",
         "PHPSESSID": "qgv643cj6joaedt618iaujicpp",
         "_gid": "GA1.2.1867243428.1523766336",
         "Hm_lvt_c8184fd80a083199b0e82cc431ab6740": "1523766337",
         "hy88showeditems": "a%3A1%3A%7Bi%3A171583034%3Ba%3A2%3A%7Bs%3A7%3A%22subject%22%3Bs%3A84%3A%22%E5%A4%A9%E6%B4%A5%E5%8D%97%E5%BC%80%E5%8C%BA%E5%AE%89%E8%A3%85%E9%92%A2%E5%88%B6%E7%94%B2%E7%BA%A7%E9%98%B2%E7%81%AB%E9%97%A8%EF%BC%8C%E5%8E%82%E5%AE%B6%E5%AE%9A%E5%88%B6%E5%AD%90%E6%AF%8D%E9%98%B2%E7%81%AB%E9%97%A8%E7%9B%B4%E9%94%80%E7%94%B5%E8%AF%9D%22%3Bs%3A3%3A%22url%22%3Bs%3A54%3A%22http%3A%2F%2Ftianjin.huangye88.com%2Fxinxi%2F7616_171583034.html%22%3B%7D%7D",
         "gr_user_id": "23a5dff8-2976-4688-849d-0a91b2dbef04",
         "gr_session_id_aa3229224cce7805": "dab590b2-84a0-4b9a-87fc-6912f02080d9",
         "Hm_lpvt_c8184fd80a083199b0e82cc431ab6740":"1523766426",
         "_gat": "1"
    }

    def start_requests(self):
        r = redis.Redis(host="", port="", db=0, decode_responses=True)
        while True:
            new_url = r.rpop("url")
            if new_url:
                yield scrapy.Request(url=new_url, cookies=self.cookie, meta={"url": new_url},
                                     callback=self.parse_result)
            else:
                break

    def parse_result(self, response):
        # 得到url
        url = response.meta["url"]
        content = response.text

        Item = TesttestItem()
        Item["urls"] = url
        Item["content"] = content

        yield Item
