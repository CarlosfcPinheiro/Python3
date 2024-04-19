#Saving search datas on a text file
import sqlite3

file = open("morebooks.txt", "w")
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

author = str(input("Enter an author name: ").strip().title())
cursor.execute("""SELECT * FROM Books WHERE Author = ?;""", [author])
listselect = cursor.fetchall()

for row in range(0, len(listselect)):
    newrecord = (f"{listselect[row][0]} - {listselect[row][1]} - {listselect[row][2]} - {listselect[row][3]}\n")
    file.write(newrecord)

file.close()
db.close()