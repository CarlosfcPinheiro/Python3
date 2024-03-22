#Adding a new name

file = open("Names.txt", "r")
print("This is a name list: ")
print(file.read())

name = str(input("\nEnter a new name: ").capitalize().strip())
file = open("Names.txt", "a")
file.write(f"\n{name}")

file = open("Names.txt", "r")
print(f"""This is your new name list:
{file.read()}""")
