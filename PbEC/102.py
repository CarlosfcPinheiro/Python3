#Shoes size

names_ss = {}
for c in range(0, 4):
    name = str(input("\nEnter a name: ").capitalize().strip())
    size = float(input("Enter a shoe size: "))
    age = int(input("Enter an age: "))

    names_ss[name] = {"Size": size, "Age": age}

choice = str(input("\nEnter a name to view the shoe size: ").capitalize().strip())

if (choice in names_ss):
    print(f"The shoe size is: {names_ss[choice]}")
else:
    print("\nThis name does not exist in the dictionary...")