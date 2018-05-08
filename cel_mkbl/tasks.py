# _*_ coding:utf-8 _*_
from __future__ import absolute_import
from celery import Celery
from pyquery import PyQuery as pq


app = Celery("cel_mkbl", broker="redis://127.0.0.1:6379/2", backend="redis://127.0.0.1:6379/5", include=["tasks"])


@app.task
def getUrl():
    urllist = ["http://china.makepolo.com/"]
    return urllist

@app.task
def getOneUrl(html):
    one_list = []
    doc1 = pq(html)
    one_urls = doc1(".sidebar_item h3 a")
    for i in one_urls.items():
        if "http://china.makepolo.com/list/" in i.attr("href"):
            one_url = i.attr("href")
            print one_url
            one_list.append(one_url)
            # one_list = set(one_list)
    return one_list

@app.task
def getTwoUrl(html2):
    two_list = []
    doc2 = pq(html2)
    two_urls = doc2(".category.clearfix .linesbg")
    for ii in two_urls.items():
        two_url = ii.attr("href")
        print two_url
        two_list.append(two_url)
        # two_list = set(two_list)
    return two_list