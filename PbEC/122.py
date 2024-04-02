#### Managing Salaries ####
import csv

def add_ToFile():
    file = open("Salaries.csv", "a")
    name = str(input("\nEnter a name: ").title().strip())
    salary = float(input("Enter the salary: "))
    new_record = (f"{name}, {salary}\n")
    file.write(new_record)
    file.close()
    return file

def view_Records():
    file = list(csv.reader(open("Salaries.csv")))
    count = 0
    print("")
    for row in file:
        print(f"[{count}] = {row}")
        count +=1
    return file

def main():
    while True:
        option = int(input("""\n
    1) Add to file
    2) View all recors
    3) Quit program
    Select an option: """))
        match option:
            case 1:
                add_ToFile()
                continue
            case 2:
                view_Records()
                continue
            case 3:
                print("Shutting down the program...")
                break
            case _:
                print("\nThis option does not exist...")
                continue

file = open("Salaries.csv", "a")
file.close()
main()
    