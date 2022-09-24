#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import sys
import pickle


<<<<<<< HEAD
url = "https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=ki/"
=======
url = "https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=sa/"
url1 = "https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=sa/"
>>>>>>> 095c58079e6498b8621db53d8b9794d0470e4ba1

data = None

sys.setrecursionlimit(20000)

res  = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

res2 = requests.get(soup.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href'])
soup2 = BeautifulSoup(res2.content, 'html.parser')

replace_word = " - エロ動画・アダルトビデオ - FANZA動画"


#data = soup2.prettify()



#print(data)
page_title = soup2.title.text.replace(replace_word, '')
print(page_title)

with open("./" + page_title + ".pickle", "wb") as f:
    pickle.dump(soup2, f)

print(sys.getrecursionlimit())

