#Book's year
import csv

init_num = int(input("Enter a starting year: "))  
end_num = int(input("Enter a ending year: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

c = 0
for row in tmp:
    if (tmp[c][2] >= init_num) and (tmp[c][2] <= end_num):
        print(tmp[c])
        c+=1
    else:
        continue

