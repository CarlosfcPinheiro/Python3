#Changing values in a column-row

numbers = [[1,2,3], [4,5,6],[7,8,9],[10,11,12]]

row = int(input("Choose a row: ")) - 1
col = int(input("Choose a column: ")) - 1

print(f"\nThe value in this position: {numbers[row][col]}")

choice = str(input("You want to change this value? [Yes=y]/[No=n] ").upper().strip()[0])

if (choice == 'Y'):
    value = int(input("\nEnter a value to substitute: "))
    numbers[row][col] = value

    print(f"The new row: {numbers[row]}")
elif (choice == 'N'):
    print("\nOkay, thank you :)")
else:
    print("\nThis option isn't possible...")