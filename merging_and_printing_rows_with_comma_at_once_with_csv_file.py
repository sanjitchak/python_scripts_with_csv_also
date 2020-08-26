import csv

# KEYWORD file name
filename = "casualshirt_keyword.csv"

# initializing the titles and rows list
fields = []
rows = []
same = {}

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)


    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    
    #printing keyowords one by one with comma at end
    for row in rows:
     if same.get(row[0]) == 1 or row[0]=="" or row[0]==" ":
         continue
     
     #checking for special characters
     row[0] = ''.join(i for i in row[0] if not i == "-")
     
     same[row[0]] = 1
     print(row[0],end = ', ')