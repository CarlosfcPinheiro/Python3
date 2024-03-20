#Changing the value in a row

numbers = [[1,2,3], [4,5,6],[7,8,9],[10,11,12]]

print(f"2D list: {numbers}")
row = int(input("Choose a row: "))
print(f"\nChosen row: {numbers[row - 1]}")

num = int(input("Enter a value to add at this row: "))
numbers[row - 1].append(num)

print(f"\nThis is the new row: {numbers[row - 1]}")