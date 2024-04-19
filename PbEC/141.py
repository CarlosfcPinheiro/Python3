import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    Name text NOT NULL,
    PlaceofBirth text NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
    ID integer NOT NULL,
    Title text NOT NULL,
    Author text NOT NULL,
    DatePublished integer NOT NULL);""")

for c in range(0, 4):
    name = str(input("Name: ").strip().title())
    placeofbirth = str(input("Place of Birth: ").strip().title())
    cursor.execute("""INSERT INTO Authors(Name, PlaceofBirth) VALUES(?,?);""", (name, placeofbirth))
    db.commit()

print("")
for i in range(0, 12):
    enterid = int(input("ID: "))
    title = str(input("Title: ").strip().title())
    author = str(input("Author: ").strip().title())
    date = int(input("Date published: "))

    cursor.execute("""INSERT INTO Books(ID, Title, Author, DatePublished) VALUES(?,?,?,?);""", (enterid, title, author, date))
    db.commit()

db.close()