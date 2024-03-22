#Controling files

import time

while True:
    print("""
    1) Create a new file
    2) Display the file
    3) Add a new item to the file
    4) Exit the program""")
    sel = int(input("Make a selection 1, 2, 3 or 4: "))

    match sel:
        case 1:
            subject = str(input("\nEnter a subject: ").capitalize().strip())
            file = open("Subject.txt", "w")
            file.write(f"{subject}\n")
            file.close()
        case 2:
            file = open("Subject.txt", "r")
            print(f"\n{file.read()}")
            time.sleep(2)
            file.close()
        case 3:
            subjetc = str(input("\nEnter a new subjetc: ").capitalize().strip())
            file = open("Subject.txt", "a")
            file.write(f"{subjetc}\n")
            file.close()
            file = open("Subject.txt", "r")
            print(f"\n{file.read()}")
            file.close()
            time.sleep(2)
        case 4:
            print("\nShutting down the program...")
            time.sleep(1)
            break
        case _:
            print("\nThis is not an option")
