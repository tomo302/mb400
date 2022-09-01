#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 23:11:04 2022

@author: fed36-mb400
"""

#!/usr/bin/env python
# coding: utf-8
#このコードは、女優別出演作品のURLを抽出するコード。urlには女優の出演作品一覧ページのurlをセットすると、出演作品の個別ページのURLを取得して動画をダウンロードするコードです。
from bs4 import BeautifulSoup
import itertools
import requests
import re
import json
import time
#url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=1053615/sort=date/?dmmref=arm00929&i3_ref=detail&i3_ord=1&i3_pst=info_actress"
#ジャンルのURL
url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=4124/"
#上記のurlを詠み込む。
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

#resには年齢確認ページにリダイレクトされたページの内容が入っている
#リダイレクトされたページから、年齢確認をクリアして目的のurlを取得するためタグをfindして、再びrequeststする。
url2 = soup.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']
res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.text, 'html.parser')

#上記で、目的の女優の出演作品一覧ページを取得に成功！！。作品別urlを抽出する。
#動画のURLを取得するための配列
videos_url  = []
soup2.find_all('p', class_ = 'tmb')
#for p in soup2.find_all('p', class_ = 'tmb', limit=2):#何本の作品を取得するかは、ここのlimit引数で決まる。参考までに。出演数が多い女優にどうぞ。
for p in soup2.find_all('p', class_ = 'tmb'):#すべて取得。通常
    #print(p)
    for row in p.find_all('a'):#class:tmbのpタグの中にはaタグは一つしかないので、単純にaタグ指定のみで期待されるurlを取得できたいる。
        print(row['href'])
        videos_url.append(row['href'])
#ここから作品ページURL取得開始

url_list = [
"https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=1dldss00066/",
"https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=1stars00523/"
]

def get_move(url):
    json_dict = None
    res3 = requests.get(url)
    soup3 = BeautifulSoup(res3.text, 'html.parser')
    url3 = soup3.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']
    res4 = requests.get(url3)
    soup4 = BeautifulSoup(res4.text, 'html.parser')
    json_2= soup4.find("script", {"type": "application/ld+json"})
    data = json_2.text
    #サンプル動画が存在しないと['subjectOf']キーが無いってエラーが出るのでサンプル動画があったら処理をする。
    if "subjectOf" in data and "contentUrl" in data:
        json_dict = json.loads(data)
        print(json_dict)
        move_url = (json_dict['subjectOf']['contentUrl']).replace('sm', 'mhb')
        move_title = (json_dict['name'])
        #動画タイトル名をファイル名に使用するので長すぎるとエラーになるので５０文字以上なら短く加工する処理
        if len(move_title) > 50:
            #タイトルの先頭から３５文字に＊＊＊＊をつなげてタイトル末尾１５文字を連結してファイル名を作成。
            move_title = move_title[:35] + '＊＊＊＊' + move_title[-15:]
        #動画タイトルの中に「/」スラッシュが入っていると、動画保存するパスが変わってしまうので置換処理。
        move_title = move_title.replace('/', '_')
        response = requests.get(move_url)
        if response.status_code == 200:
            start_time = time.process_time()
            with open('/home/fed36-mb400/git/mb400/video/' + move_title + '.mp4', 'wb') as saveFile:
                saveFile.write(response.content)
 
def start_down(videos_url):
    # 開始 sleep時間をカウントしない処理時間
    start_time = time.process_time()
    i = 0
    for url in videos_url:
        i = i+1
        print(str(i) + "本目をダウンロード中")
        get_move(url)

    # ダミー処理
    time.sleep(1)
 
    # 修了
    end_time = time.process_time()
 
    # 経過時間を出力(秒)
    elapsed_time = end_time - start_time
    print(elapsed_time)
    print("終了しました")

start_down(videos_url)
