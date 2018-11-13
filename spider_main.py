#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 爬虫总调
from xinsu_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlPaser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  # 如果存在新的url
            try:
                new_url = self.urls.get_new_url()  # 取出一个新的url
                print("craw %d : %s" % (count, new_url))  # 打印
                html_cont = self.downloader.download(new_url)  # 下载页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析页面
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 5:
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.out_put_html()

if __name__ == "__main__":
    root_url = "http://www.yusou8.com/news/show-12316.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
