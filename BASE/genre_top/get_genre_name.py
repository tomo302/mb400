#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup
import os
import json
import itertools
import csv
import regex
import re

def genre_name_list():
    url = "https://www.dmm.co.jp/digital/videoc/-/genre/"
    genre_base_url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id="
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    firstpage_url = soup.find('a', class_="ageCheck__link ageCheck__link--r18").get('href')
    res2 = requests.get(firstpage_url)
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    # ENDここまで全ページ共通コード
    
    #ここからgenre top page固有のコード
    data = soup2.find("div", id="genre_list_box").encode().decode('unicode-escape')
    #正規表現で{}囲まれている部分を抽出。リストで取得される。インデックスは１まで
    dic = re.findall(r'\{.*\}', data) 
    # END ここまでで取得期待している値が入っている部分を取得済み
    
    
    dic1 = dic[1] #ここが取得したい部分でstrなので、まだ値をキーを使用して取り出せない
    
    dic_01 = eval(dic[1])
    
    dd = dic_01[0]['genres']
    
    genre_name = []
    for _ in dd:
        #print(_['genre_id'] + _['genre'])
        genre_name.append(list(_.values()))
        #result = list(my_list[0].items())
        print(tuple(_.values()))
    #作成した配列を使用してCSVファイルに保存
    with open('genre_シチュエーション.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(genre_name)
    #各ジャンルのURLを作成
    genre_url = []
    for _ in genre_name:
        genre_url.append(genre_base_url + _[0] + "/")
    
    return genre_url


gu = genre_name_list()

