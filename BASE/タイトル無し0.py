# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 19:28:33 2022

@author: i3-12100
"""
import os
import requests
from bs4 import BeautifulSoup

url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=cead00336/?dmmref=actress_1008785&i3_ref=list&i3_ord=31"

def soup2(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    age_check_url = soup.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']
    
    res2 = requests.get(age_check_url)
    
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    
    return soup2

def actress(url):
    pass

def genru(url):
    pass

def sakuhin_list(url):
    pass

def video_page(url):
    print("ビデオです")
    soup2 = soup2(url)
    
    # 作品名取得
    print(soup2(url).find('h1',  class_ = "item fn").text)
    
    video_title = (soup2(url).find('h1',  class_ = "item fn").text)
    
    if not os.path.exists(video_title):
        os.mkdir(video_title)
    
    soup2.find('div', class_ = "list-boxcaptside list-boxpagenation")
        
    
    #os.mkdir(video_title)
    print(os.path.exists(video_title))
    
    # カレントディレクトリ取得（参考コードで通常はos.getcwd()を使用する
    print(os.path.abspath(os.curdir))
    
    # カレントディレクトリ取得（本命）
    print(os.getcwd())
    os.chdir(video_title)
    
    print(os.getcwd())
    
    
    
    
    



#重要・URLを判定してページに合った関数を実行させる役割のurl_check(url)関数。
def url_check(url):
    if "d/i" in url:
        print("ジャンルページです")
        #ジャンルページ用の関数を実行
    elif "a/-/a" in url:
        print("５０音ページです")
        #５０音ページ用の関数を実行
    elif "t&" in url:
        print("ビデオページです")
<<<<<<< HEAD
        #ビデオページ用の関数を実行
        video_page(url)
        
    elif "s/i" in url:
        print("出演一覧ページ")
        #出演一覧ページ用の関数を実行
=======
	    #ビデオページ用の関数を実行

        video_page(url)
        
    elif "s/i" in url:
	    print("出演一覧ページ")
	    #出演一覧ページ用の関数を実行



>>>>>>> f112d7e4cf491859cd2d23d99587453ad3da4fd2
url_check(url)






    