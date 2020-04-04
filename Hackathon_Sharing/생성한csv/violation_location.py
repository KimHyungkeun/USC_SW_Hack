import pandas as pd 
import math

f = open('violation_location.csv','w')

df = pd.read_csv('../폐수 위법사항_2001-2016_0.csv', sep=',') 
column_df = df['Location 1'] 
index = 0
limit = len(column_df)
column = ['Latitude', 'Longitude']


f.write(column[0] + ',' +column[1] + '\n')

while True:

    if index == limit : 
        break 

    if column_df[index] != column_df[index] :
        index += 1
        continue

    val = column_df[index]
    line = str(val)

    latitude = line.split(',')[0]
    longitude = line.split(',')[1]

    latitude = latitude.lstrip('(') 
    longitude = longitude.rstrip(')')

    f.write(str(latitude) + ',' + str(longitude) + '\n')
    
    index += 1
    


f.close()