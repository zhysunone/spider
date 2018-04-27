# _*_ coding:utf-8 _*_

__author__ = "zhy"
__date__ = "2018/4/26 17:58"

from scrapy_redis.spiders import RedisCrawlSpider
from redis_step.items import RedisStepItem

class MoviespiderSpider(RedisCrawlSpider):
    name = 'ff'
    redis_key = 'fenbuSpider:start_urls'

    def parse(self , response):
        content = response.text

        item = RedisStepItem()
        item["content"] = content

        yield item