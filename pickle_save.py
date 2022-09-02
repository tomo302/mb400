#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import sys
import pickle


url = "https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=sa/"

data = None

sys.setrecursionlimit(20000)

res  = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

res2 = requests.get(soup.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href'])
soup2 = BeautifulSoup(res2.content, 'html.parser')

data = soup2.prettify()

with open("./soup2_sa.pickle", "wb") as f:
    pickle.dump(soup2, f)

print(sys.getrecursionlimit())

