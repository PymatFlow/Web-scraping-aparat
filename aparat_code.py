# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:15:35 2019

@author: Kazem
"""

import bs4
import requests
import pandas

addres = 'https://www.aparat.com/eeiranmatlab/videos'
page = requests.get(addres)

cc = page.content

cc1 = page.text

soup = bs4.BeautifulSoup(cc1,'html.parser')

tag1 = soup.find_all("div",{"class":"grid-thumbnail"})

tag2 = tag1[0].find_all("div",{"class":"item grid-item"})
tag3 = tag1[0].find_all("div",{"class":"thumb-view-date"})
l =[]
for item2,item3 in zip(tag2,tag3):
    dic ={}
    dic["title"] = item2.find("a",{"class":"title"}).find("span").text
    dic["num_view"] = item3.text.split("\n")[1].replace("  بازدید","")
    l.append(dic)

df = pandas.DataFrame(l)

