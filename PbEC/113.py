#Manage book's data
import csv

times = int(input("Enter how many books do you want to add: "))

file = open("Books.csv", "a")
for n in range(0, times):
    name = str(input("\nBook's name: ").title().strip())
    author = str(input("Author's name: ").title().strip())
    year = int(input("Enter the book's year: "))

    newrecord = (f"{name}, {author}, {year}\n")
    file.write(newrecord)

    n += 1
file.close()

file = open("Books.csv", "r")
search = str(input("\nEnter author's name: ").title().strip())

count = 0
for row in file:
    if search in str(row):
        print(row)
        count += 1

if (count == 0):
    print("There are no books with this author's name in the book's data...")