#!/usr/bin/env python
# coding: utf-8

import pickle


with open('./soup2_sa.pickle', 'rb') as f:
    x = pickle.load(f)

print(x.find_all('a'))

