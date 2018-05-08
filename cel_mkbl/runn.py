# _*_ coding:utf-8 _*_

from tasks import getUrl, getOneUrl, getTwoUrl
import requests
import urllib2

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

header = {
	"Cookie": "_vid=C7E768A4A4F00001A3421A8019701968; __utma=162808035.1190490996.1520650998.1520650998.1520650998.1; __utmz=162808035.1520650998.1.1.utmcsr=china.makepolo.com|utmccn=(referral)|utmcmd=referral|utmcct=/; BDTUJIAID=89ff044e3296a211fec635b631a5b91b; history_view=%7B%220%22%3A100472048312%2C%221%22%3A101035929914%2C%223%22%3A100356747124%2C%224%22%3A101000000011%2C%225%22%3A101000000010%7D; PHPSESSID=235555af6043627f210f9c4b58069764; Hm_lvt_7e7577ecbf4c96abade7fbcaa1d3b519=1522647447,1522720725,1522752328,1522802692; Hm_lpvt_7e7577ecbf4c96abade7fbcaa1d3b519=1522830130",
	"Host": "china.makepolo.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
}
# run 函数
def Run():
    # 得到 一级的url
    urls = getUrl.delay().get()
    print urls
    print type(urls)
    req = urllib2.Request(urls[0], headers=header)
    html = urllib2.urlopen(req, timeout=20).read().decode("utf-8")
    # print html
    one_list = getOneUrl.delay(html).get()
    # print one_list
    for one_url in one_list:
        # print one_url
        req2 = urllib2.Request(one_url, headers=header)
        html2 = urllib2.urlopen(req2, timeout=10).read().decode("utf-8")
        two_list = getTwoUrl.delay(html2).get()
        # print type(two_list)
        for two_url in two_list:
            print two_url


if __name__ == '__main__':
    Run()