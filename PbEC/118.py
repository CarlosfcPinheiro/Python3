#Basic Subprogram (function)
def inputNum():
    num = int(input("Enter a num: "))
    return num

def countNum():
    number = inputNum()
    for c in range(0, number):
        c+=1
        print(c)
countNum()