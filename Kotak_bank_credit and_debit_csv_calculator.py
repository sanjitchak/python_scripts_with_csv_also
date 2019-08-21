import csv

# csv file name
filename = "Report-20190822010552.csv"

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
    for row in rows:
     i += 1
     if len(row) < 5:
         print(i,row)
     if len(row) > 5:
        if row[5] == 'CR' and "UPI" not in row[2]:
         cr += float(row[4].replace(",",""))
        if row[5] == 'DR' and "UPI" not in row[2]:
          dr += float(row[4].replace(",",""))
        #arr = row.split(',')
# printing the field names
print("CR",cr,"DR",dr)

