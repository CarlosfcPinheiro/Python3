#Manage a book's data
type(1)
import csv
#Function to show data
def showData(data):
    i = 0
    for row in data:
        print(f"[{i}] = {row}")
        i+=1

file = list(csv.reader(open("Books.csv")))
book_list = []
for row in file:
    book_list.append(row)
print(f"{showData(book_list)}\n")

############## Row delete section ################
row_del = int(input("Select a row to delete: "))
del book_list[row_del]
print(f"{showData(book_list)}\n")

############## Data in row edit section ############
row_alter = int(input("Enter a row that you want to change: "))
i = 0
for row in book_list[row_alter]:
    print(f"[{i}] = {book_list[row_alter][i]}")
    i+=1

datasel_index = int(input("Which data that you want to change: "))
newdata = str(input("Enter a new data to substitute: ").title().strip())
book_list[row_alter][datasel_index] = newdata
print(book_list[row_alter])

############## Row edit section ################
file = open("Books.csv", "w")
i = 0
for row in book_list:
    newrecord = (f"{book_list[i][0]}, {book_list[i][1]}, {book_list[i][2]}\n")
    file.write(newrecord)
    i+=1
file.close()