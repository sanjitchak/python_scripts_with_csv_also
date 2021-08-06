  
import csv
import os
# csv file name
filename = "trial.csv"

# initializing the titles and rows list
fields = []
rows = []
 

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    

    # extracting field names through first row


    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    dr = 0
    cr = 0

    i = -1
    Dict = {}
    for row in rows:
     i += 1
     
     Dict[i] = row[2].strip()
    filename = "new.csv"

    Dict2 = {}
    i =-1
# writing to csv file 
    with open(filename, 'w' , newline='', encoding='utf-8') as csvfile:
     
     csvwriter = csv.writer(csvfile) 
     for row in rows:
        i+=1  
     
        if row[1].strip() and (row[1] in Dict.values() or row[1].strip() in Dict2.values()):
           # print(row)
            continue
        Dict2[i] = row[1].strip()
        csvwriter.writerow(row)
        #print(row[0], row[1])
        #print(row)
    # name of csv file 
    
    # creating a csv writer object 
    
        
    # writing the fields 
     
        
  
        #arr = row.split(',')
# printing the field names
