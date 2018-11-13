#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# urllib2模块直接导入就可以用，在python3中urllib2被改为urllib.request
import urllib.request


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        response = urllib.request.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read()
