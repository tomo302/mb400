# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:59:50 2022

@author: i3-12100
"""


from bs4 import BeautifulSoup
import itertools
import requests
import re
import json
import time

url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=cjod00364/?dmmref=videoa_top_pickup_pc&i3_ref=recommend&i3_ord=6"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

age_check_url = soup.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']

res2 = requests.get(age_check_url)

soup2 = BeautifulSoup(res2.text, 'html.parser')

json_2 = soup2.find("script", {"type": "application/ld+json"})

data = json_2.text
#print(data)

jd = json.loads(data)

#print(jd['name'])
print(jd)

