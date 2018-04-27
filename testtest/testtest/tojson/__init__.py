# _*_ coding:utf-8 _*_

__author__ = "zhy"
__date__ = "2018/4/12 15:06"

from scrapy.exporters import JsonLinesItemExporter

class chongxie(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super(chongxie, self).__init__(file, ensure_ascii=None)