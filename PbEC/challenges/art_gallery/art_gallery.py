import tkinter
import sqlite3

def create_db():
    with sqlite3.connect("arts.db") as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS artists(
        ArtistID integer PRIMARY KEY,
        Name text NOT NULL,
        Address text NOT NULL,
        Town text,
        Country text NOT NULL,
        PostCode text NOT NULL);""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS pieces(
        PieceID integer PRIMARY KEY,
        ArtistID integer NOT NULL,
        Title text NOT NULL,
        Medium text NOT NULL,
        Price integer NOT NULL);""")

def record_Artist(cursor, db):
    for c in range(0, 5):
        numid = int(input("\nEnter id: "))
        name = str(input("Enter name: ").title().strip())
        address = str(input("Enter address: ").title().strip())
        town = str(input("Enter town: ").title().strip())
        country = str(input("Enter country: ").title().strip())
        postcode = str(input("Enter postcode: ").upper().strip())

        cursor.execute("""INSERT INTO artists(ArtistID, Name, Address, Town, Country, PostCode) VALUES(?, ?, ?, ?, ?, ?);""", (numid, name, address, town, country, postcode))
        
        db.commit()

def record_Piece(cursor, db):
    for c in range(0, 17):
        pieceID = int(input("\nEnter pieceid: "))
        artistID = int(input("Enter artistid: "))
        title = str(input("Enter title: ").capitalize().strip())
        medium = str(input("Enter medium: ").capitalize().strip())
        price = int(input("Enter price: "))

        cursor.execute("""INSERT INTO pieces(PieceID, ArtistID, Title, Medium, Price) VALUES(?, ?, ?, ?, ?);""", (pieceID, artistID, title, medium, price))
        db.commit()

def clear(entry):
    entry.delete(0, tkinter.END)

def artist_Window():

    def clear_all_Entry():
        clear(id_entry)
        clear(name_entry)
        clear(address_entry)
        clear(town_entry)
        clear(country_entry)
        clear(postcode_entry)

    def add_Datas_artists():
        idartist = id_entry.get()
        nameartist = name_entry.get().capitalize()
        address = address_entry.get().capitalize()
        town = town_entry.get().capitalize()
        country = country_entry.get().capitalize()
        postcode = postcode_entry.get().upper()

        cursor.execute("""INSERT INTO artists(ArtistID, Name, Address, Town, Country, PostCode) VALUES(?, ?, ?, ?, ?, ?);""", [idartist, nameartist, address, town, country, postcode])
        db.commit()


    window_artist = tkinter.Toplevel(window)
    window_artist.geometry("300x200")
    window_artist.title("Add Artist")
    window_artist.resizable(False, False)

    # Label insert datas 
    entermsglbl = tkinter.Label(window_artist, text="Insert the respective datas", font=("Courier", 10))
    entermsglbl.place(x=150, y=10, anchor="center")

    # ID
    idlbl = tkinter.Label(window_artist, text="ID: ")
    idlbl.place(x=10, y=30)
    id_entry = tkinter.Entry(window_artist)
    id_entry.place(x=30, y=30, width=20)

    # Name 
    namelbl = tkinter.Label(window_artist, text="Name: ")
    namelbl.place(x=75, y=30)
    name_entry = tkinter.Entry(window_artist)
    name_entry.place(x=115, y=30, width=120)
    
    # Address
    addresslbl = tkinter.Label(window_artist, text="Address: ")
    addresslbl.place(x=10, y=60)
    address_entry = tkinter.Entry(window_artist)
    address_entry.place(x=60, y=60, width=100)

    # Town
    townlbl = tkinter.Label(window_artist, text="Town: ")
    townlbl.place(x=170, y=60)
    town_entry = tkinter.Entry(window_artist)
    town_entry.place(x=210, y=60, width=70)

    # Country
    countrylbl = tkinter.Label(window_artist, text="Country: ")
    countrylbl.place(x=10, y=90)
    country_entry = tkinter.Entry(window_artist)
    country_entry.place(x=60, y=90, width=80)

    # Postcode
    postcodelbl = tkinter.Label(window_artist, text="PostCode: ")
    postcodelbl.place(x=150, y=90)
    postcode_entry = tkinter.Entry(window_artist)
    postcode_entry.place(x=210, y=90, width=70)

    # Button add data
    addbtn = tkinter.Button(window_artist, text="Add Data", command=add_Datas_artists)
    addbtn.place(x=120, y=150, anchor="center")

    #Button clear entry
    clearbtn = tkinter.Button(window_artist, text="Clear", command=clear_all_Entry)
    clearbtn.place(x=180, y=150, anchor="center")

def piece_Window():

    def clear_all_Entry():
        clear(piece_entry)
        clear(artistid_entry)
        clear(title_entry)
        clear(medium_entry)
        clear(price_entry)

    def add_Datas_Pieces():
        pieceid = piece_entry.get()
        artistid = artistid_entry.get()
        title = title_entry.get().capitalize()
        medium = medium_entry.get().title()
        price = price_entry.get()

        cursor.execute("""INSERT INTO pieces(PieceID, ArtistID, Title, Medium, Price) VALUES(?, ?, ?, ?, ?)""", [pieceid, artistid, title, medium, price])
        db.commit()

    window_piece = tkinter.Tk()
    window_piece.geometry("300x200")
    window_piece.title("Add Piece")
    window_piece.resizable(False, False)

    # Label insert datas 
    entermsglbl = tkinter.Label(window_piece, text="Insert the respective datas", font=("Courier", 10))
    entermsglbl.place(x=150, y=10, anchor="center")

    # Piece ID
    piecelbl = tkinter.Label(window_piece, text="piece ID: ")
    piecelbl.place(x=10, y=30)
    piece_entry = tkinter.Entry(window_piece)
    piece_entry.place(x=60, y=30, width=20)

    # Artist ID
    artistidlbl = tkinter.Label(window_piece, text="Artist ID: ")
    artistidlbl.place(x=95, y=30)
    artistid_entry = tkinter.Entry(window_piece)
    artistid_entry.place(x=150, y=30, width=120)
    
    # Title
    titlelbl = tkinter.Label(window_piece, text="Title: ")
    titlelbl.place(x=10, y=60)
    title_entry = tkinter.Entry(window_piece)
    title_entry.place(x=40, y=60, width=100)

    # Medium
    mediumlbl = tkinter.Label(window_piece, text="Medium: ")
    mediumlbl.place(x=145, y=60)
    medium_entry = tkinter.Entry(window_piece)
    medium_entry.place(x=200, y=60, width=70)

    # Price
    pricelbl = tkinter.Label(window_piece, text="Price: ")
    pricelbl.place(x=10, y=90)
    price_entry = tkinter.Entry(window_piece)
    price_entry.place(x=45, y=90, width=80)

    # Button add data
    addbtn = tkinter.Button(window_piece, text="Add Data", command=add_Datas_Pieces)
    addbtn.place(x=120, y=150, anchor="center")

    #Button clear entry 
    clearbtn = tkinter.Button(window_piece, text="Clear", command=clear_all_Entry)
    clearbtn.place(x=180, y=150, anchor="center")

def check_ButtonNext():
    optionselection = option.get()
    if (optionselection == "Artist"):
        artist_Window()
    elif (optionselection == "Piece"):
        piece_Window()
    else:
        print("nothing...")

def check_Search():
    search_listbox.delete(0, tkinter.END)

    inputvalue = search_entry.get()
    searched_option_value = search_option.get()

    match searched_option_value:
        case "Artist":
            cursor.execute("""SELECT ArtistID FROM artists WHERE Name = ?""", [inputvalue])
            artistid = cursor.fetchall()[0][0]

            cursor.execute("""SELECT Title, Medium, Price FROM pieces WHERE ArtistID = ?;""", [artistid])
        case "Medium":
            cursor.execute("""SELECT Title, Medium, Price FROM pieces WHERE Medium = ?;""", [inputvalue])
        case "Price":
            cursor.execute("""SELECT Title, Medium, Price FROM pieces WHERE Price = ?;""", [inputvalue])
        case _:
            print("Insert a value to search...")

    item_list = ""
    for c in cursor.fetchall():
        item_list = ""
        for i in c:
            item_list += (f" {i} |")
        search_listbox.insert(tkinter.END, item_list)

    search_entry.delete(0, tkinter.END)
    
with sqlite3.connect("arts.db") as db:
    cursor = db.cursor()

# ------ GUI ------
window = tkinter.Tk()
window.geometry("400x400")
window.title("Arts Database")
window.resizable(False, False)

# Labeltext
text_enter = tkinter.Label(text="Welcome to arts Database!", borderwidth=1, relief="solid", pady=5, padx=5)
text_enter.config(font=("Courier", 10))
text_enter.place(x=200,y=20, anchor="center")

# label to add artist or piece
optionlbl = tkinter.Label(text="Select to add a piece or an artist to the DB:")
optionlbl.config(font=("Arial", 9))
optionlbl.place(x=15, y=60)

# Select Artist or Piece to add
option = tkinter.StringVar(window)
option.set("Select")
option_menu = tkinter.OptionMenu(window, option, "Artist", "Piece")
option_menu.place(x=15,y=80)
    
# Button next
next_btn = tkinter.Button(text="Next", command=check_ButtonNext)
next_btn.place(x=100, y=82)

# Search Label
searchlbl = tkinter.Label(text="Select to search by name artist, medium, or price: ", font=("Arial", 9))
searchlbl.place(x=15, y=160)

# Search option select
search_option = tkinter.StringVar(window)
search_option.set("Select")
search_option_menu = tkinter.OptionMenu(window, search_option, "Artist", "Medium", "Price")
search_option_menu.place(x=15, y=180)

# Search entry
search_entry = tkinter.Entry()
search_entry.place(x=110, y=182, height=30)

# Search listbox output
search_listbox = tkinter.Listbox()
search_listbox.place(x=15, y=220, width=365)

# Search button
search_button = tkinter.Button(text="Search", command=check_Search)
search_button.place(x=245, y=182)
    
window.mainloop()
db.close()