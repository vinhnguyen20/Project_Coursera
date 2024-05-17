import pandas as pd
from datetime import datetime

file_path = 'stadium_cleaned_2024-05-16_21_07_46.699216.csv'
data = pd.read_csv(file_path)

df = data['location']

df = pd.DataFrame(df, columns=['location'])

tam = []

df['location'] = df['location'].fillna('[nan,nan]')

df['location'].apply(lambda x : tam.append(str(x)))


latitude = []
longtitude = []

for i in range(0,len(tam)):
    if tam[i].find(','):
        longtitude.append(tam[i].split(',')[0].split('[')[1])
        latitude.append(tam[i].split(',')[1].split(']')[0])
# print(latitude)

longtitude_df = pd.DataFrame(longtitude, columns=['longtitude'])
df = pd.concat([df, longtitude_df], axis=1)

latitude_df = pd.DataFrame(latitude, columns=['latitude'])
df = pd.concat([df, latitude_df], axis=1)

data = pd.concat([data, df['longtitude']], axis = 1)

data = pd.concat([data, df['latitude']], axis = 1)

print(df)

# file_name = ('stadium_cleaned_' + str(datetime.now().date()) + "_" + str(datetime.now().time()).replace(":", "_") + '.csv')

# df.to_csv(file_name, index=False)
# print(file_name)