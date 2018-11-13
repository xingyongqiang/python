#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# url管理器

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 单个网址
    def add_new_url(self, root_url):
        if root_url is None:
            return
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    # 多网址
    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    # 是否存在url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个新的URl
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
