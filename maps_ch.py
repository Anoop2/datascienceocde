# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:43:01 2018

@author: Anoop
"""

import time
import requests, json 
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


key = 'AIzaSyD58GJSHakEbJtJnCDGqrkHD_V69iMTvcs'
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

query = input('Enter place: ') 
r = requests.get(url + 'query=' + query + '&key=' + key) 
x = r.json() 
y=x['results']
while not y:
    query = input('Enter valid place: ')
    r = requests.get(url + 'query=' + query + '&key=' + key) 
    x = r.json() 
    y=x['results']
 
lat=y[0]['geometry']['location']['lat']
lon=y[0]['geometry']['location']['lng']

query2='banks in ' + query

r = requests.get(url + 'query=' + query2 + '&key=' + key) 
x = r.json() 
y=x['results']
bank=len(y)
for i in range(0,2):
    try:
        x['next_page_token']
        z=x['next_page_token']
        time.sleep(3)
        r = requests.get(url + '&key=' + key + '&pagetoken=' + z )
        x = r.json() 
        y=x['results']
        bank=bank+len(y)
    except KeyError:
        break
print('bank : ',bank)


query3='Insurance companies in ' + query
r = requests.get(url + 'query=' + query3 + '&key=' + key) 
x = r.json() 
y=x['results']
ins=len(y)

for i in range(0,2):
    try:
        x['next_page_token']
        z=x['next_page_token']
        time.sleep(3)
        r = requests.get(url + '&key=' + key + '&pagetoken=' + z )
        x = r.json() 
        y=x['results']
        ins=ins+len(y)
    except KeyError:
        break
print('insurance : ',ins)





map = Basemap(projection='merc', lat_0 = 53.1424, lon_0 = -7.6921,
    resolution = 'i', area_thresh = 0.1,
    llcrnrlon=-11.01, llcrnrlat=51.42,
    urcrnrlon=-5.77, urcrnrlat=55.35)
 
map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='#ffffff', linewidth=.0)
map.drawmapboundary(fill_color='#46bcec')
map.fillcontinents(color = '#f2f2f2',lake_color='#46bcec')
#map.drawmapboundary()
map.readshapefile('gadm36_IRL_1', 'areas')

x,y = map(lon, lat)
bank_detail='no of banks: ' + str(bank)
ins_detail='no of insurance companies: ' + str(ins)
plt.text(x, y+5000, query,weight='bold')
plt.text(x, y-35000, bank_detail,weight='bold')
plt.text(x, y-65000, ins_detail,weight='bold')
plt.show()

