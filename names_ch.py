# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 04:44:56 2018

@author: Anoop
"""

import requests
from bs4 import BeautifulSoup
ir_url = ['http://www.babynamewizard.com/name-list/irish-boys-names-most-popular-names-for-boys-in-the-republic-of-ireland',
          'http://www.babynamewizard.com/name-list/irish-girls-names-most-popular-names-for-girls-in-the-republic-of-ireland-2014']

print('Irish Names:')
call_val=['m','f']
for i in range(0,2):
    r = requests.get(ir_url[i]).content
    news_soup = BeautifulSoup(r, "html.parser")
    name_list = news_soup.findAll(class_="sex-"+call_val[i])
    for name in name_list:
        name=name.contents[0]
        print(name)

ir_url = ['http://www.babynamewizard.com/name-list/english-boys-names-most-popular-names-for-boys-in-england',
          'http://www.babynamewizard.com/name-list/english-girls-names-most-popular-names-for-girls-in-england-2015']

print('English Names:')
call_val=['m','f']
for i in range(0,2):
    r = requests.get(ir_url[i]).content
    news_soup = BeautifulSoup(r, "html.parser")
    name_list = news_soup.findAll(class_="sex-"+call_val[i])
    for name in name_list:
        name=name.contents[0]
        print(name)
        
        


