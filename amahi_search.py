#!/bin/python
import csv

# csv file name
filename = "CSV FLE"

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


    arr = {}
    for row in rows:
     if row[1]:
        #removing all whitespaces and counting the word
        value = row[1].replace(" ", "").lower()
        arr[value] = arr.get(value,0) + 1
        #arr = row.split(',')
arr = {k: v for k, v in sorted(arr.items(), key=lambda item: item[1])}

# printing the field names in order
with open('amahi.txt', 'w') as f:
    for key,value in arr.items():
       print(key,value, file=f)
