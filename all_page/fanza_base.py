# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import os
import json
import itertools


#独占】【準新作】ヌードモデルNTR 上司と羞恥に溺れた妻の衝撃的浮気映像 篠田ゆう
#rl = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=jul00959/"

def base():
    url = "https://www.dmm.co.jp/digital/videoa/-/genre/"
    res = requests.get(url) 

    #content_type_encoding = r.encoding if r.encoding != 'ISO-8859-1' else None
    #soup = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)

    soup = BeautifulSoup(res.text, 'html.parser')
    firstpage_url = soup.find('a', class_="ageCheck__link ageCheck__link--r18").get('href')
    res2 = requests.get(firstpage_url)
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    return soup2

soup2 = base()
#print(soup2.find_all('a'))

def sakuhin():
    json_2 = soup2.find("script", {"type": "application/ld+json"})

    data = json_2.text

    json_dict = None
    if "subjectOf" in data and "contentUrl" in data:
        json_dict = json.loads(data)
        #print(json_dict)
        actor_name = json_dict['subjectOf']['actor']['name']
        video_title = json_dict['name']
        description = json_dict['description']
        video_url = (json_dict['subjectOf']['contentUrl']).replace('sm', 'mhb')
        print(actor_name)
        print()
        print(video_title)
        print(description)
        print(video_url)
#sakuhin()


def actress():
    pass

def genru():
    pass

def itiran():
    pass

"""
<div data-v-02cb2b3f="" id="list2" class="seo-genre-box">

"""

print(soup2.title.text)
#print(soup2.find("div",  id="genre_list_box"))
jd = soup2.find("div", id="genre_list_box").find_all("div", class_="seo-genre")

#print(soup2.find_all("div", class_="seo-genre-box"))

#div_tag = jd.find('div', {'data-v-02cb2b3f': True})
print(jd)
