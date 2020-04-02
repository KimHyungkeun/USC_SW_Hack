import pandas as pd 

df = pd.read_csv('../폐수 위법사항_2001-2016_0.csv',sep=',') 

column_df = df['OCCURRED ON'] 
index = 0

year_count = [0,0,0,0,0,0,0,0,0,0,0] # 2005 ~ 2015


while True:

    if index == len(column_df): 
        break 

    line = column_df[index]

    if '2005' in line :
        year_count[0] += 1
    
    elif '2006' in line :
        year_count[1] += 1 

    elif '2007' in line :
        year_count[2] += 1 

    elif '2008' in line :
        year_count[3] += 1 

    elif '2009' in line :
        year_count[4] += 1 
    
    elif '2010' in line :
        year_count[5] += 1 
    
    elif '2011' in line :
        year_count[6] += 1 
    
    elif '2012' in line :
        year_count[7] += 1 

    elif '2013' in line :
        year_count[8] += 1 

    elif '2014' in line :
        year_count[9] += 1 

    elif '2015' in line :
        year_count[10] += 1 

    index += 1
    


f = open('violation_case_count.csv','w')

column = ['Year','Viotation_Case_Count']

f.write(column[0] + ',' + column[1] + '\n')

for year in range (2005, 2016) :
    f.write(str(year) + ',' + str(year_count[year-2005]) + '\n')



f.close()