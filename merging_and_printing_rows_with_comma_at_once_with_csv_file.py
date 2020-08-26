import csv

# KEYWORD file name
filename = "casualshirt_keyword.csv"

# initializing the titles and rows list
fields = []
rows = []
same = {}
terms = ""
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)


    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    
    #printing keyowords one by one with comma at end
    for row in rows:
     #character limit of 200, +1 for end comma
     if (len(terms) + len(row[0])) > 201:
         break
     if same.get(row[0]) == 1 or row[0]=="" or row[0]==" ":
         continue
     
     #checking for numbers and characters
     terms=terms[:]+ row[0]
     same[row[0]] = 1
     print(row[0],end = ', ')