#!/bin/python
import csv

# csv file name
filename = "CSV FILE"

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
    i = -1
    for row in rows:
     i += 1
     if row[1]:
        #removing all whitespaces and counting the word
        value = row[1].replace(" ", "")
        arr[value] = arr.get(value,0) + 1
        #arr = row.split(',')
arr_value = []
for value in arr.values():
    arr_value.append(value)
arr_value.sort(reverse=True)

def get_key(val):
    for key, value in arr.items():
         if val == value:
             return key

# printing the field names in desc order
with open('amahi.txt', 'w') as f:
    for value in arr_value:
       print(get_key(value),value, file=f)
