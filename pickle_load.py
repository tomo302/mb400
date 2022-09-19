#!/usr/bin/env python
# coding: utf-8
import os
import glob
import pickle
import sys
#from pickle_save import soup2
sys.setrecursionlimit(20000)
dir_path = "C:/Users/i3-12100/git/mb400/*pickle" ##ワイルドカードを設定「*txt」
txt_files = glob.glob(dir_path)
txt_files = txt_files[0]

print(txt_files)
full_size = 0

with open('./actor_ta.pickle','rb') as f:
	

	x = pickle.load(f)
	print(x)
	print(x.find_all('a'))
print("aaaaaa")