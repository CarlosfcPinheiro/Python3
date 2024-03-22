#Excluding rows

file = open("Names.txt", "r")
print(f"""Names list: 
{file.read()}""")
file.close()

file = open("Names.txt", "r")
nameoption = str(input("Enter a name of the list: ").capitalize().strip())
nameoption += "\n"

for row in file:
    if (row != nameoption):
        file = open("Names2.txt", "a")
        file.write(row)
        file.close()
file.close()

