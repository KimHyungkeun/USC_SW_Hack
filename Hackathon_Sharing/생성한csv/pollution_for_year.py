import pandas as pd 

toxicsum = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # 2008 ~ 2015
year_per_num = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # 2008 ~ 2015
year = 0


f = open('../오염수치조사표(피레스톨로이드).csv', 'r') 

f.readline() 

while True :
    
    line = f.readline()

    if line == "" or  line == '\0' :
        break

    if line.split(',')[1] == "Agriculture"  or line.split(',')[2] == "#N/A" :
        #print('Point')
        #print(line)
        continue

    #print(line)
    percentage = line.split(',')[2]
    year = line.split(',')[3]
    toxic_units = line.split(',')[5]
    
    #print(toxic_units)

    
    if float(toxic_units) == 0 :
        #print('Zero')
        continue

    if '2008' in year :
        if float(percentage) < 7 :
            toxicsum[0][0] += float(toxic_units)
            year_per_num[0][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[0][1] += float(toxic_units)
            year_per_num[0][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[0][2] += float(toxic_units)
            year_per_num[0][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[0][3] += float(toxic_units)
            year_per_num[0][3] += 1 

    elif '2009' in year :
        if float(percentage) < 7 :
            toxicsum[1][0] += float(toxic_units)
            year_per_num[1][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[1][1] += float(toxic_units)
            year_per_num[1][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[1][2] += float(toxic_units)
            year_per_num[1][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[1][3] += float(toxic_units)
            year_per_num[1][3] += 1 
    
    elif '2010' in year :
        if float(percentage) < 7 :
            toxicsum[2][0] += float(toxic_units)
            year_per_num[2][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[2][1] += float(toxic_units)
            year_per_num[2][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[2][2] += float(toxic_units)
            year_per_num[2][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[2][3] += float(toxic_units)
            year_per_num[2][3] += 1 
    
    elif '2011' in year :
        if float(percentage) < 7 :
            toxicsum[3][0] += float(toxic_units)
            year_per_num[3][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[3][1] += float(toxic_units)
            year_per_num[3][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[3][2] += float(toxic_units)
            year_per_num[3][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[3][3] += float(toxic_units)
            year_per_num[3][3] += 1 
    
    elif '2012' in year :
        if float(percentage) < 7 :
            toxicsum[4][0] += float(toxic_units)
            year_per_num[4][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[4][1] += float(toxic_units)
            year_per_num[4][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[4][2] += float(toxic_units)
            year_per_num[4][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[4][3] += float(toxic_units)
            year_per_num[4][3] += 1  

    elif '2013' in year :
        if float(percentage) < 7 :
            toxicsum[5][0] += float(toxic_units)
            year_per_num[5][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[5][1] += float(toxic_units)
            year_per_num[5][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[5][2] += float(toxic_units)
            year_per_num[5][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[5][3] += float(toxic_units)
            year_per_num[5][3] += 1 

    elif '2014' in year :
        if float(percentage) < 7 :
            toxicsum[6][0] += float(toxic_units)
            year_per_num[6][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[6][1] += float(toxic_units)
            year_per_num[6][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[6][2] += float(toxic_units)
            year_per_num[6][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[6][3] += float(toxic_units)
            year_per_num[6][3] += 1  

    elif '2015' in year :
        if float(percentage) < 7 :
            toxicsum[7][0] += float(toxic_units)
            year_per_num[7][0] += 1 
        
        elif float(percentage) < 30 :
            toxicsum[7][1] += float(toxic_units)
            year_per_num[7][1] += 1 
        
        elif float(percentage) < 60 :
            toxicsum[7][2] += float(toxic_units)
            year_per_num[7][2] += 1 
        
        elif float(percentage) <= 100 :
            toxicsum[7][3] += float(toxic_units)
            year_per_num[7][3] += 1 
 
#for year in range (0,8) :
#    for i in range (0,4) :
#        print(toxicsum[year][i])

f.close()

f = open('pollution_for_year.csv', 'w')

column = ['Year', 'Urban', 'Pollution']

f.write(column[0] + ',' + column[1] + ',' + column[2] + '\n')

for year in range (2008, 2016) :
    for index in range (0,4) :
    
        if year_per_num[year-2008][index] == 0 :
            avg = 0

        else :
            avg = toxicsum[year-2008][index] / year_per_num[year-2008][index]

        f.write(str(year) + ',' + 'Index'+'['+ str(index) + ']' + ',' + str(avg) + '\n')

f.close()