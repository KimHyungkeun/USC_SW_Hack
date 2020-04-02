f = open('../폐수위법 처리케이스_2005-2016.csv', 'r')

f.readline()
year_count = [0,0,0,0,0,0,0,0,0,0,0]


while True:
    line = f.readline()

    if line == "" or line == '\0': 
        break 

    date = line.split(',')[2]
    year = date.split('/')[2]

    if '2005' in year :
        year_count[0] += 1
    
    elif '2006' in year :
        year_count[1] += 1 

    elif '2007' in year :
        year_count[2] += 1 

    elif '2008' in year :
        year_count[3] += 1 

    elif '2009' in year :
        year_count[4] += 1 
    
    elif '2010' in year :
        year_count[5] += 1 
    
    elif '2011' in year :
        year_count[6] += 1 
    
    elif '2012' in year :
        year_count[7] += 1 

    elif '2013' in year :
        year_count[8] += 1 

    elif '2014' in year :
        year_count[9] += 1 

    elif '2015' in year :
        year_count[10] += 1 


f.close()

f = open('prisoner_count.csv','w')

column = ['Year','Prisoner_Count']

f.write(column[0] + ',' + column[1] + '\n')

for year in range (2005, 2016) :
    f.write(str(year) + ',' + str(year_count[year-2005]) + '\n')



f.close()