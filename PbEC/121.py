#### Manage names ####

def add_Name():
    print(f"\n{names}")
    name = str(input("Enter a name to add to the list: ").title().strip())
    names.append(name)
    return names

def change_Name():
    print(f"\n{names}")
    name_in_list = str(input("Enter the name that you want to change: "))
    new_name = str(input("Enter a new name to substitute: ").title().strip())
    indexname = names.index(name_in_list)
    names[indexname] = new_name
    return names

def delete_Name():
    print(f"\n{names}")
    name_in_list = str(input("Enter a name to delete: ").title().strip())
    indexname = names.index(name_in_list)
    del names[indexname]
    return names

def view_Names():
    count = 0
    print("\nList names: ")
    for x in names:
        print(f"[{count}] = {x}")
        count+=1
    return names

def main():
    while True:
        option = int(input("""\n
    [1] Add a name to the list
    [2] Change a name in the list
    [3] Delete a name from the list
    [4] View the list
    [5] End program
    Enter an option: """))
        match option:
            case 1:
                add_Name()
                continue
            case 2:
                change_Name()
                continue
            case 3:
                delete_Name()
                continue
            case 4:
                view_Names()
                continue
            case 5:
                print("Shutting down the program...")
                break
            case _:
                print("This option does not exist...")
                continue

names = []
main()