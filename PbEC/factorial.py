number = int(input("enter a number: "))
factorial = 1

if (number == 0):
    print(1)
else:
    for c in range(1, number+1):
        factorial *=c   
    print(factorial)