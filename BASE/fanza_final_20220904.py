#!/usr/bin/env python
# coding: utf-8

# In[106]:


import requests
from bs4 import BeautifulSoup
import os
import json
import itertools
import csv


# In[9]:


url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=1075/"


# In[10]:


base_url = ""


# In[102]:


def genru(url):
    base_url = url + "page="

    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    firstpage_url = soup.find('a', class_="ageCheck__link ageCheck__link--r18").get('href')
    res2 = requests.get(firstpage_url)
    g_soup = BeautifulSoup(res2.text, 'html.parser')
    #最大ページ数
    max_page = int(g_soup.find('div', class_ = "list-boxcaptside list-boxpagenation").p.text.split('タ')[0].replace(',', '')) // 120 + 2
    #ジャンル名
    genru_name = (g_soup.title.text.split('- エ')[0])
    #print(max_page)
    genru_lists = []
    actor_lists = []
    for num in range(1, max_page):
        print(num)
        url = base_url + str(num) + "/"
        print(url)
        res3 = requests.get(url)
        #print(res3.status_code)
        soup3 = BeautifulSoup(res3.text, 'html.parser')
        res4 = requests.get(soup3.find('a', class_="ageCheck__link ageCheck__link--r18").get('href'))
        soup4 = BeautifulSoup(res4.text, 'html.parser')
        #print(soup4.title)
        #出演者名取得　例外処理必要
        for _ in soup4.find_all('p', class_ = 'sublink'):
            try:
                print(_.a.text)
                actor_name = _.a.text
                actor_lists.append(actor_name)
            except AttributeError:
                print("出演者：複数")
                actor_name = "出演者：複数"
                actor_lists.append(actor_name)
        #作品タイトル、　作品ページURL、　DVDジャケット表画像URL
        for row in soup4.find_all('p', class_ = 'tmb'):
            print(row.img['alt'])
            sakuhin_title = row.img['alt']
            sakuhin_url = row.a['href']
            dvd_jaketo_omote = row.img['src']
        
            genru_lists.append([sakuhin_title, sakuhin_url, dvd_jaketo_omote])
    return genru_lists, actor_lists, genru_name


# In[103]:


g_lists, act_list, genru_name = genru(url)


# In[104]:


#act_listは1カラムのリストでg_listsは3カラムの2次元配列で、3カラムの先頭にacr_listを追加して4カラムの2次元配列を作成するコード
#list構造でカラム追記はinsertを使用するらしい
i = 0
for _ in act_list:
    g_lists[i].insert(0, _)  
    i += 1
print(g_lists)


# In[108]:


#labels = ['出演者名', '作品タイトル', '作品ページURL', 'DVDジャケット画像']
with open(genru_name + '.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(g_lists)


# In[ ]:


max_page = int(g_soup.find('div', class_ = "list-boxcaptside list-boxpagenation").p.text.split('タ')[0].replace(',', '')) // 120


# In[ ]:


actor_name = g_soup.find('p', class_ = 'sublink').a.text


# In[ ]:


sakuhin_title = g_soup.find_all('p', class_ = 'tmb')[0].img['alt']


# In[ ]:


sakuhin_url = g_soup.find_all('p', class_ = 'tmb')[0].a['href']


# In[ ]:


dvd_jaketo_omote = g_soup.find_all('p', class_ = 'tmb')[0].img['src']


# In[ ]:


genru_list = []


# In[109]:


os.getcwd()


# In[ ]:


#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=hhf00007/?dmmref=81b5e821-9a8f4f0a4d9f58928c89ef3b0f00aaa0&i3_ref=recommend&i3_ord=13"
url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=venx00159/?dmmref=recommend1_detail&i3_ref=recommend&i3_ord=3"
#出演者単独
#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=venx00116/?dmmref=81b5e821-9a8f4f0a4d9f58928c89ef3b0f00aaa0&i3_ref=recommend&i3_ord=9"
#サンプル動画がない作品
#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=78godr00937/?dmmref=keyword_6960&i3_ref=list&i3_ord=19"
#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=jufe00419/?dmmref=videoa_top_pickup_pc&i3_ref=recommend&i3_ord=6"
#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=lulu00152/?dmmref=keyword_1018&i3_ref=list&i3_ord=96"
#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=umso00459/?dmmref=actress_1069702&i3_ref=list&i3_ord=67"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
firstpage_url = soup.find('a', class_="ageCheck__link ageCheck__link--r18").get('href')
res2 = requests.get(firstpage_url)
soup2 = BeautifulSoup(res2.text, 'html.parser')


# In[ ]:


#soup2.title.text.split("-")[0]


# In[ ]:


dvd_jacket_url = soup2.find("div", class_ = "tx10 pd-3").a['href']


# In[ ]:


video_title = soup2.find("img", class_ ="tdmm")['alt']


# In[ ]:


#出演者複数作品の出演者１０名まで取得可能・・取得値は参考までで使用していない。
actors = ""
for a in soup2.find('span', id = 'performer').find_all('a'):
    b = a.text.replace('▼すべて表示する', '') + ','
    actors = actors + b
actors = actors.replace(',,', '')
print(actors)


# In[ ]:


json_2 = soup2.find("script", {"type": "application/ld+json"})


# In[ ]:


data = json_2.text


# In[ ]:


json_dict = None


# In[ ]:


def get_sakuhin_data():
    #サンプル画像URL取得
    sample_gazou = []
    for _ in soup2.find_all("img", class_ ="mg-b6"):
        sample_gazou.append(_['src'])
    #ENDーサンプル画像
    
    #作品データ詳細取得：作品タイトル、作品内容詳細、作品内画像URL、DVDジャケット見開き画像URL、サンプル動画URL、出演者名
    json_2 = soup2.find("script", {"type": "application/ld+json"})
    data = json_2.text
    json_dict = None
    #サンプル動画の有無を確認
    if "subjectOf" in data and "contentUrl" in data:
        json_dict = json.loads(data)
        
        sakuhin_name = json_dict['name']
        sakuhin_description = json_dict['description']
        sakuhin_image = json_dict['image']
        dvd_jacket_url = soup2.find("div", class_ = "tx10 pd-3").a['href']
        sample_video_url = json_dict['subjectOf']['contentUrl']#デフォルットだと小さい画像なので
        try:
            actor_name = json_dict['subjectOf']['actor']['name']
        except KeyError:
            actor_name = "出演者複数"
            print(actor_name)
            
        #サンプル画像URLを取得してリストで保存    
        sample_gazou = []
        for _ in soup2.find_all("img", class_ ="mg-b6"):
            sample_gazou.append(_['src'])
        
    #取得してリターンする値：：作品タイトル、作品内容詳細、作品内画像URL、DVDジャケット見開き画像URL、サンプル動画URL、出演者名、作品サンプル画像
    sakuhin_list = []
    sakuhin_list = [json_dict['name'], json_dict['description'], json_dict['image'], dvd_jacket_url, json_dict['subjectOf']['contentUrl'].replace('sm', 'mhb'), actor_name, sample_gazou] 
    
    #return sakuhin_name, sakuhin_description, sakuhin_image, sample_video_url
    return sakuhin_list


# In[ ]:


def sakuhin_down(sakuhin_list):
    BASE_PATH = "/home/fed36-mb400/git/mb400/FANZA/"
    os.chdir(BASE_PATH)
    print(BASE_PATH)
    actor_name = sakuhin_list[5]
    if actor_name not in os.listdir():
        #女優名フォルダが存在しなかったら、女優名でフォルダ作成
        os.makedirs(actor_name)
        #作成したフォルダにCD
        os.chdir(actor_name)
    else:
        #既存の女優名のフォルダにCD
        os.chdir(actor_name)
       
    sakuhin_title = sakuhin_list[0]
    #現在女優のフォルダ内・・作品名のフォルダが存在しなかったら作品名でフォルダ作成 
    if sakuhin_title not in os.listdir():
        #作品名でフォルダ作成
        os.makedirs(sakuhin_title)
        #作成したフォルダにCD
        os.chdir(sakuhin_title)
    else:
        os.chdir(sakuhin_title)
    #これ以降作品名のフォルダ内にサンプル画像、DVDジャケット画像、サンプル動画をダウンロードする
    response = requests.get(sakuhin_list[4])
    if response.status_code == 200:
        with open(os.getcwd() + '/' + sakuhin_title + '.mp4', 'wb') as saveFile:
            saveFile.write(response.content)
            print("ダウンロードしました")
    else:
        #大きい解像度の動画が存在しない場合は、URLを変更して小さい映像の動画をダウンロードする。
        sakuhin_title = sakuhin_title.replace('mhb', 'sm')
        with open(os.getcwd() + sakuhin_title + '.mp4', 'wb') as saveFile:
            saveFile.write(response.content)
            print("解像度の低い動画をダウンロードしました")
    
    return sakuhin_title


# In[ ]:


sakuhin_list = get_sakuhin_data()


# In[ ]:


#カレント内のファイル名＆ディレクトリ名取得
os.listdir()


# In[ ]:


#os.chdir(sakuhin_list[5])


# In[ ]:


os.getcwd()


# In[ ]:


os.chdir("/home/fed36-mb400/git/mb400")


# In[ ]:


print(sakuhin_down(sakuhin_list))


# In[ ]:




