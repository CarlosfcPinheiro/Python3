def decorator(func):
    def informations(*args, **kwargs):
        print(f"Function name: {func.__name__} with args {args} and kwargs {kwargs}")

        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")

        return result
    
    return informations
    

@decorator
def multiply(x, y):
    return x * y

result = multiply(5, 6)
print(f"Result: {result}")