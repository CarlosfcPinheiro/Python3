import sqlite3

with sqlite3.connect("Bookinfo.db") as db:
    cursor = db.cursor()

year = int(input("Enter year: "))
cursor.execute("""SELECT Title, Author, DatePublished FROM Books WHERE DatePublished >= ? ORDER BY DatePublished ASC;""", [year])
listdata = cursor.fetchall()

print(f"\nBooks where the date published is upper than {year}: ")
count = 1
for c in listdata:
    print(f"[{count}] {c}")
    count += 1