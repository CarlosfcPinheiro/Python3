#This program will measure the time spent by a recursive function and a for loop function that calculates a factorial
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        exe_time = end_time - start_time
        print(f"The function {func.__name__} tooks {exe_time:.6f} seconds to execute")
        
        return result
    return wrapper

@time_decorator
def recursive_fac(num) -> int:
    if num == 1:
        return 1
    else:
        return num * recursive_fac(num-1)

@time_decorator
def for_fac(num) -> int:
    result = 1
    for c in range(1, num+1):
        result *= c
    return result

number = int(input("Enter a number: "))
print(f"Result: {recursive_fac(number)}\n")
print(f"Result: {for_fac(number)}")