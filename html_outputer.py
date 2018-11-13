#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输出器

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def out_put_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<ul>")
        for data in self.datas:
            fout.write("<li>")
            fout.write("<span>%s</span>&nbsp;&nbsp;<span>%s</span>" % (data['url'],data['title']))
            fout.write("</li>")
        fout.write("</ul>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
