import csv

file = (csv.reader(open("Books.csv", "r")))

i = 1
for row in file:
    print(f"{row} = {i}")
    i+=1
