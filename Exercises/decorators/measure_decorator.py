#Program to test the usability of decorators
import time

def functime(func):
    def calctime(*args, **kwargs): #function that executes something before the decorated function
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time_spent = end_time - start_time

        print(f"The func {func.__name__} spent {time_spent:.6f}s to execute.")
    
    return calctime

@functime
def multbymult(a, b):
    result = a * b

@functime
def multbysum(a, b):
    result = 0
    for c in range(b):
        result += a

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

print(f"Result 1: {multbymult(number1, number2)}")
print(f"Result 2: {multbysum(number1, number2)}")