#Selecting rows

numbers = [[1,2,3], [4,5,6],[7,8,9],[10,11,12]]

print(f"This is a 2D list: {numbers}")
selrow = int(input("Enter a number to select a row: "))

print(f"\nChosen row: {numbers[selrow - 1]}")