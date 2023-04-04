#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import json

def make_pageNationUrlList(max_page, page_kind):
    print("受取ったページの種類は、" + page_kind + "です。最大ページは：" + str(max_page) + "です")

def soup2(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    res2 = requests.get(soup.find('a', class_ = "ageCheck__link ageCheck__link--r18")['href'])
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    
    return soup2

#５０音ページ、ジャンルページ、出演作品一覧ページを判定する関数。
def page_kind(soup2):

    pk = str(soup2.find_all('li', class_ = 'terminal')[1]).split('/')[6]

    if pk == "article=actress":
        print("出演作品一覧ページです")
        pk = "sakuhin"
    elif pk == "article=keyword":
        print("ジャンルページです")
        pk = "genru"
    elif pk == "actress":
        print("５０音ページです")
        pk = "50on"
    return pk

#この最大ページ数取得はページによっては使えない！！
def get_maxPage(soup2):
    max_page = soup2.find_all('li', class_ = 'terminal')
    max_page = int(str(max_page[1]).split('/')[-4].split('=')[1])
    return max_page