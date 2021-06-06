import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

File = open('myHome.csv','w',encoding='utf-8_sig', newline='\n')
Writer = csv.writer(File)
Writer.writerow(['title','address','price'])
page = 1
while page<7:
    url = f'https://www.myhome.ge/ka/s/iyideba-bina-Tbilisi?Keyword=%E1%83%97%E1%83%91%E1%83%98%E1%83%9A%E1%83%98%E1%83%A1%E1%83%98&AdTypeID=1&PrTypeID=1&Page={page}&mapC=41.73188365%2C44.8368762993663&regions=687578743&fullregions=687578743&districts=62176122.319380261.58416723.2953929439.58420997.152297954.61645269.6273968347.58416582.58416672.58377946&cities=1996871&GID=1996871'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    main_div = soup.find('div', class_='statement-row-search list haslist')
    homes = main_div.find_all('div', class_='wrapper full-width')
    for each in homes:
        title = each.h5.text
        address = each.find('div', class_='address').text
        price = each.find('b', class_='item-price-gel').text
        Writer.writerow([title, address, price + 'GEL'])
    page+=1
    sleep(15)
    print(r.url)
File.close()
