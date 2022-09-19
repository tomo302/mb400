#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import json

'''
URLサンプル
５０音「さ」のURL　　　：：https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=sa/
ジャンル「温泉」のURL　：：https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=4140/
女優の出演作品一覧URL）：：https://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=1008785/sort=ranking/　（篠田ゆう）
作品URL　　　　　　　　：：https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=cead00336/?dmmref=actress_1008785&i3_ref=list&i3_ord=49

'''

#url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=1019/"

def soup2(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    res2 = requests.get(soup.find('a', class_ = "ageCheck__link ageCheck__link--r18")['href'])
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    
    return soup2
    

def actors50(soup2):
	pass

def genru(soup2):
	pass

def get_maxPage(soup2):

    #max_page = soup2.find_all('li', class_ = 'terminal')
    #max_page = int(str(max_page[1]).split('/')[9].split('=')[1])

    #print(max_page)

    #movie_nmber 取得値はstr型になる。9,368: ４桁だと「、」が入っていて
    #int型に変換するのに削除する必要あり
    movie_number = soup2.find('div', class_='list-boxcaptside')#動画の本数を取得第一段階
    #動画本数の取得地が、３桁の時はint型で４桁のときstr型になるのを、str型で統一する。
    move = str(movie_number.find('p').string)#動画の本数取得第二段階
    #動画の本数取得ここまで。
    #mcs = []#分割文字列はリストタイプなので空のリスト変数を作成
    #pタグの取得地「9,368タイトル」を「タ」で分割して数値部分のみを抽出。
    ######################################################################
    #女優一覧ページの場合はsplit('人')
    mcs = move.split('人')#分割実行
    #ジャンルページの場合split('タ')
    #mcs = move.split('タ')#分割実行
    ########################################################################
    mc = mcs[0]
    print(mc)
    #動画の本数が４桁以上だった場合「、」が含まれているので削除。
    if len(mc) > 4:
        mc = mc.replace(',', '')

    print(mc)
    print(type(mc))
    mc = int(mc)#動画の本数部分だけをstr型からint型に変換しつつ取得する。
    #mc=9368 int型
    #動画の本数取得はここまでーーーーー
    #動画本数を利用してページ数を取得。１２０は1ページの表示数。
    NumberOfPage = -(-mc//120)#切り上げ計算。ページ数なので3.7ではダメ！！4がほし
    
    print(NumberOfPage)


def page_kind(soup2):
    page_kind = str(soup2.find_all('li', class_ = 'terminal')[1]).split('/')[6]

    if page_kind == "article=actress":
        print("出演作品一覧ページです")

