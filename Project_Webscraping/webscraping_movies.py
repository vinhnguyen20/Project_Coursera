import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from datetime import datetime
import json

NO_IMAGE = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/No-image-available.png/480px-No-image-available.png'


url = 'https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'D:/myProject/Data Engineer/Coursera/New folder/project/Project_Webscraping/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

def clean_text(text):
    text = str(text).strip()
    text = text.replace('&nbsp', '')
    if text.find(' ♦'):
        text = text.split(' ♦')[0]
    if text.find('[') != -1:
        text = text.split('[')[0]
    if text.find(' (formerly)') != -1:
        text = text.split(' (formerly)')[0]

    return text.replace('\n', '')

html_page = requests.get(url).text
soup = BeautifulSoup(html_page, 'html.parser')

table = soup.find_all("table", {"class": "wikitable sortable sticky-header"})[0]
rows = table.find_all('tr')

def get_lat_long(country, city):
    geolocator = Nominatim(user_agent='VinhLam20app', timeout=10)
    location = geolocator.geocode(f'{city}, {country}')

    if location:
        return location.latitude, location.longitude
    else:
        return 0, 0

    # return None


data = []
for i in range(1, 60):
    tds = rows[i].find_all('td')
    values = {
        'rank': i,
        'stadium': clean_text(tds[0].text),
        'capacity': clean_text(tds[1].text).replace(',', '').replace('.', ''),
        'region': clean_text(tds[2].text),
        'country': clean_text(tds[3].text),
        'city': clean_text(tds[4].text),
        'images': 'https://' + tds[5].find('img').get('src').split("//")[1] if tds[5].find('img') else "NO_IMAGE",
        'home_team': clean_text(tds[6].text),
    }
    data.append(values)



stadiums_df = pd.DataFrame(data)
stadiums_df['latitude'] = stadiums_df.apply(lambda x: get_lat_long(x['country'], x['stadium'])[0], axis=1)
stadiums_df['longtitude'] = stadiums_df.apply(lambda x: get_lat_long(x['country'], x['stadium'])[1], axis=1)
stadiums_df['images'] = stadiums_df['images'].apply(lambda x: x if x not in ['NO_IMAGE', '', None] else NO_IMAGE)
stadiums_df['capacity'] = stadiums_df['capacity'].astype(int)

# # handle the duplicates
# duplicates_lat = stadiums_df[stadiums_df.duplicated(['latitude'])]
# duplicates_long = stadiums_df[stadiums_df.duplicated(['longtitude'])]
# duplicates_lat['latitude'] = duplicates_lat.apply(lambda x: get_lat_long(x['country'], x['city']), axis=1)
# duplicates_long['longtitude'] = duplicates_long.apply(lambda x: get_lat_long(x['country'], x['city']), axis=1)[1]

# stadiums_df.update(duplicates_lat)
# stadiums_df.update(duplicates_long)

print(stadiums_df)

# sta_df= stadiums_df['location']

# sta_df = pd.DataFrame(sta_df, columns=['location'])

# tam = []

# sta_df['location'] = sta_df['location'].fillna('[nan,nan]')

# sta_df['location'].apply(lambda x : tam.append(str(x)))


# latitude = []
# longtitude = []

# for i in range(0,len(tam)):
#     if tam[i].find(','):
#         longtitude.append(tam[i].split(',')[0].split('(')[1])
#         latitude.append(tam[i].split(',')[1].split(')')[0])

# longtitude_df = pd.DataFrame(longtitude, columns=['longtitude'])
# sta_df = pd.concat([sta_df, longtitude_df], axis=1)

# latitude_df = pd.DataFrame(latitude, columns=['latitude'])
# sta_df = pd.concat([sta_df, latitude_df], axis=1)

# stadiums_df = pd.concat([stadiums_df, sta_df['longtitude']], axis=1)

# stadiums_df = pd.concat([stadiums_df, sta_df['latitude']], axis=1)

# print(stadiums_df)