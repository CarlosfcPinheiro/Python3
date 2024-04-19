#Search books by author's place of birth
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT * FROM Authors;""")
list_authors = cursor.fetchall()
for c in list_authors:
    print(c)

placebirth = str(input("Enter a place of birth: ").strip().title())
cursor.execute("""SELECT Name FROM Authors WHERE PlaceofBirth = ?;""", [placebirth])
list_authors = cursor.fetchall() #Authors name storing on the list

print(f"\nThe author's books that the place of birth is {placebirth}: ")
#list authors amount
countauthors = 0
countrow = 1
for i in range(0, len(list_authors)):
    cursor.execute("""SELECT Title, Author, DatePublished FROM Books WHERE Author = ?;""", (list_authors[countauthors]))
    for row in (cursor.fetchall()):
        print(f"[{countrow}] {row}")
        countrow += 1
    countauthors += 1