import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS register(
    id integer PRIMARY KEY,
    FirstName text NOT NULL,
    Surname text NOT NULL,
    PhoneNumber text NOT NULL);""")

cursor.execute("""INSERT INTO register(id, FirstName, Surname, PhoneNumber) VALUES("1", "Simon", "Howels", "01223 349752");""")
db.commit()

cursor.execute("""INSERT INTO register(id, FirstName, Surname, PhoneNumber) VALUES("2", "Karen", "Phillips", "1954 295773");""")
db.commit()

cursor.execute("""INSERT INTO register(id, FirstName, Surname, PhoneNumber) VALUES("3", "Darren", "Smith", "01584 749012");""")
db.commit()

cursor.execute("""INSERT INTO register(id, FirstName, Surname, PhoneNumber) VALUES("4", "Anne", "Jones", "01323 567322");""")
db.commit()

cursor.execute("""INSERT INTO register(id, FirstName, Surname, PhoneNumber) VALUES("5", "Mark", "Smith", "01223 855534");""")
db.commit()

db.close()