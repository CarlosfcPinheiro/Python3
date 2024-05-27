class Calculator:
    def __init__(self, number1=0, number2=0) -> None:
        self.number1 = number1
        self.number2 = number2

    def sum(self) -> float:
        return self.number1 + self.number2
    
    def sub(self) -> float:
        return self.number1 - self.number2
    
    def div(self) -> float:
        return self.number1 / self.number2
    
    def mult(self) -> float:
        return self.number1 * self.number2
    

def main():
    while True:
        option = int(input("""
        [1] Sum
        [2] Subtract
        [3] Multiply
        [4] Divide
        [5] Quit
        Enter an option: """))
        assert option >= 1 and option <= 5, (f"Option {option} is not allowed...")

        if (option == 5):
            print("\nShutting down...")
            break

        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        
        calculator = Calculator(num1, num2)
        match option:
            case 1:
                print(f"Result: {calculator.sum():.2f}")
                continue
            case 2:
                print(f"Result: {calculator.sub():.2f}")
                continue
            case 3:
                print(f"Result: {calculator.mult():.2f}")
                continue
            case 4:
                print(f"Result: {calculator.div():.2f}")
                continue
            case _:
                print("How did you get here?")
                break

main()