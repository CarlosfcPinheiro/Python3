#Adding books
import csv

bookname = str(input("Enter a book name: ").title().strip())
author = str(input("Enter the author's name: ").title().strip())
year = int(input("Enter the book's year: "))

file = open("Books.csv", "a")
newrecord = (f"{bookname}, {author}, {year}\n")
file.write(newrecord)

file.close()
file = open("Books.csv", "r")

for row in file:
    print(row)

file.close()