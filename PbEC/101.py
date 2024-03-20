#Viewing and changing datas

sales = {'John':{'N':3056, 'S':8463, 'E':8441, 'W':2694}, 'Tom':{'N':4832, 'S':6786, 'E':4737, 'W':3612}, 'Anne':{'N':5239, 'S':4802, 'E':5820, 'W':1859}, 'Fiona':{'N':3904, 'S':3645, 'E':8821, 'W':2451}}

print(f'This is a sales table: ')
print(f"John: {sales['John']}")
print(f"Tom: {sales['Tom']}")
print(f"Anne: {sales['Anne']}")
print(f"Fiona: {sales['Fiona']}")

name = str(input("\nChoose a name: ").capitalize().strip())
if (name in sales):
    region = str(input("Enter a region [N, E, S, W]: ").upper().strip()[0])
    if (region in sales[name]):
        print(f"\nThis is the data: {sales[name][region]}")
        option = str(input("You want to change this value? [Y=yes]/[N=no]: ").upper().strip()[0])
        if (option == 'Y'):
            sales[name][region] = int(input("\nEnter a new value: "))
            print(f"This is your new row: {sales[name]}")
        elif (option == 'N'):
            print("\nShutting down the program...")
        else:
            print("\nThis option does not exist...")
    else:
        print("\nThis region does not exist...")
else:
    print("\nThis name isn't present in the dictionary...")

