#### Managing Salaries, but delete it ####
import csv

def addToFile():
    file = open("Salaries.csv", "a")
    name = str(input("\nEnter a name: ").title().strip())
    salary = float(input("Enter the salary: "))
    new_record = (f"{name}, {salary}\n")
    file.write(new_record)
    file.close()
    return file

def viewRecords():
    file = list(csv.reader(open("Salaries.csv")))
    count = 0
    print("")
    for row in file:
        print(f"[{count}] = {row}")
        count+=1
    return file

def deleteRecord():
    file = open("Salaries.csv", "r")
    tmp_lsit = []
    row_number = int(input("Enter a row number to delete: "))
    for row in file:
        tmp_lsit.append(row)
    file.close()
    del tmp_lsit[row_number]
    file = open("Salaries.csv", "w")
    for row in tmp_lsit:
        file.write(row)
    file.close()
    return file

def main():
    while True:
        option = int(input(""" 
    [1] Add to file
    [2] View all records
    [3] Delete a record (check the index before)
    [4] Quit program
    Select an option: """))
        match option:
            case 1:
                addToFile()
                continue
            case 2:
                viewRecords()
                continue
            case 3:
                deleteRecord()
                continue
            case 4:
                print("\nShutting down the program...")
                break
            case _:
                print("\nThis option does not exist...")
                continue

file = open("Salaries.csv", "a")
file.close()
main()