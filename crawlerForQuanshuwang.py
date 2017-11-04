# -*- coding: utf-8 -*-

import urllib, urllib2
import re


def getNovelListUrl():
    html = urllib.urlopen('http://www.quanshuwang.com/list/1_1.html').read().decode('gbk').encode('utf-8')
    reg = r'<a target="_blank" title=".*?" href="(.*?)" class="clearfix stitle">(.*?)</a>作者：<a href=".*?">(.*?)</a>'
    # 正则表达以获取/略过信息
    urlList = re.findall(reg, html)
    return urlList

def getNovelInfo(url):
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<a href="(.*?)"  class="l mr11">'
    infoUrl = re.findall(reg, html)
    return infoUrl

def getChapterUrl(url):
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<li><a href="(.*?)" title="(.*?)">.*?</a></li>'
    chapterList = re.findall(reg, html)
    return chapterList

def getContents(url):
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    # 因为括号()是正则表达式的一部分如果源文件中有(), 则需要转译
    reg = re.compile(reg, re.S)
    # 多行抓取需要compile正则表达
    contents = re.findall(reg, html)
    return contents

novelUrl = getNovelListUrl()
for urls in novelUrl:
    information = getNovelInfo(urls[0])
    chapters = getChapterUrl(information[0])
    for chapter in chapters:
        print chapter[1].decode('utf-8')
        print
        novel = getContents(information[0] + '/' + chapter[0])
        novel = novel[0].replace('&nbsp;', '')
        novel = novel.replace('<br />', '')
        print novel.decode('utf-8')
        print
        print
        print
    break
