#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import os
import json
import itertools


# In[3]:


url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=jul00959/"


# In[4]:


res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
firstpage_url = soup.find('a', class_="ageCheck__link ageCheck__link--r18").get('href')
res2 = requests.get(firstpage_url)
soup2 = BeautifulSoup(res2.text, 'html.parser')


# In[5]:


json_2 = soup2.find("script", {"type": "application/ld+json"})


# In[6]:


print(type(json_2))


# In[7]:


data = json_2.text


# In[8]:


data


# In[9]:


print(type(data))


# In[10]:


json_dict = None
if "subjectOf" in data and "contentUrl" in data:
    json_dict = json.loads(data)
    #print(json_dict)
    actor_name = json_dict['subjectOf']['actor']['name']
    video_title = json_dict['name']
    description = json_dict['description']
    video_url = (json_dict['subjectOf']['contentUrl']).replace('sm', 'mhb')
    print(actor_name)
    print(video_title)
    print()
    print(description)
    print()
    print(video_url)


# In[18]:


(json_dict['subjectOf']['contentUrl']).replace('sm', 'mhb')


# In[24]:


json_dict['description']


# In[21]:


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
            with open('/home/fed36-mb400/ビデオ/Fanza/熟女ページ１/' + move_title + '.mp4', 'wb') as saveFile:
                saveFile.write(response.content)


# In[1]:


soup2


# In[ ]:




