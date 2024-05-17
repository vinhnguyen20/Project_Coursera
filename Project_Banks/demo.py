from bs4 import BeautifulStoneSoup
import numpy as np
import pandas as pd
import requests
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup

#----------------------------------------------- Demo phuong an
# format_time = "%Y-%h-%d-%H:%M:%S"
# now = datetime.now()
# time_stamp = now.strftime(format_time)

# with open('./demo.txt','a') as f:
#     f.write(time_stamp + ':' + 'Vinh Lam')


#----------------------------------------------- Parse
url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribus = ['Name', 'MC_USD_Billion']

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')
table_data = data.find_all('tbody')
rows = table_data[0].find_all('tr')

for row in rows:
    col = row.find_all('td')
    if len(col) != 0:
        col_name = col[1].find_all('a')[1]['title']
        col_price = col[2].contents[0]
        print(col_name)
# print(rows)

# print(time_stamp)