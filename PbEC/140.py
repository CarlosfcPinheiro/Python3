import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

def display_Data():
    listregister = cursor.execute("""SELECT * FROM  register;""")
    print("")
    for c in listregister:
        print(c)

def add_Register():
    newid = int(input("\nEnter ID: "))
    newfname = str(input("Enter first name: ").strip().title())
    newsurname = str(input("Enter surname: ").strip().title())
    newphone = str(input("Enter phone number: "))

    cursor.execute("""INSERT INTO register(id, FirstName, Surname, PhoneNumber) VALUES(?,?,?,?);""", (newid, newfname, newsurname, newphone))
    db.commit()

def search_Data():
    surname = str(input("\nEnter surname to search: ").strip().title())
    cursor.execute("""SELECT * FROM register WHERE Surname = ?;""", [surname])
    print(f"\n{cursor.fetchall()}")

def delete_Data():
    selectid = int(input("\nEnter an id to delete from the db: "))
    cursor.execute("""DELETE FROM register WHERE id = ?;""", [selectid])
    db.commit()
def main():
    while True:
        option = int(input("""
        [1] View phone book
        [2] Add to phone book
        [3] Search for surname
        [4] Delete person from phone book
        [5] Quit
        
        Select option: """))
        
        match option:
            case 1:
                display_Data()
            case 2:
                add_Register()
            case 3:
                search_Data()
            case 4:
                delete_Data()
            case 5:
                break
            case _:
                print("This option is not avaliable...")
                continue
main()
db.close()