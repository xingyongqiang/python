#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 解析器
import re

from bs4 import BeautifulSoup


class HtmlPaser(object):
    def _get_new_urls(self, page_url, soup):
        # http://www.xinsu360.cn/wzyx/seozixun/1924.html
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"http://www.yusou8.com/news/show-\d+\.html"))
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        # <h1>新速科技seor小编告诉大家如何做seo-能抛弃你的人，只有你自己</h1>
        res_data = {}
        title_node = soup.find('h1')
        res_data['url'] = page_url
        res_data['title'] = title_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        news_url = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return news_url, new_data
