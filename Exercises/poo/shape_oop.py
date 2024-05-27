class Shape:
    def calc_area(self) -> float:
        pass
    def calc_perimeter(self) -> float:
        pass

class Circle(Shape):
    pi_value = 3.14
    def __init__(self, diameter: float) -> None:
        self.diameter = diameter
    
    def calc_area(self):
        return Circle.pi_value * ((self.diameter/2)**2)

    def calc_perimeter(self):
        return 2 * Circle.pi_value * (self.diameter/2)
    
class Rect(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height
    
    def calc_perimeter(self):
        return (self.width*2) + (self.height*2)
    
class Triangle(Shape):
    def __init__(self, height, widht, side1, side2) -> None:
        self.height = height
        self.widht = widht
        self.side1 = side1
        self.side2 = side2

    def calc_area(self) -> float:
        return self.widht * self.height
    
    def calc_perimeter(self) -> float:
        return self.side1 + self.side2 + self.widht

def main():
    option = int(input("""
    [1] Circle
    [2] Rectangle
    [3] Triangle
    Enter an option: """))

    assert option >= 1 and option <= 3, (f"Option {option} is not allowed...")

    match option:
        case 1:
            diameter = float(input("\nEnter a diameter(cm): "))
            circle = Circle(diameter)

            print(f"Area: {circle.calc_area():.2f}")
            print(f"Perimeter: {circle.calc_perimeter():.2f}")
        case 2:
            width = float(input("Enter a width(cm): "))
            height = float(input("Enter a height(cm): "))

            rect = Rect(width, height)
            print(f"Area: {rect.calc_area():.2f}")
            print(f"Perimeter: {rect.calc_perimeter():.2f}")

        case 3:
            width = float(input("\nEnter a width(cm): "))
            height = float(input("Enter a height(cm): "))
            side1 = float(input("Enter a side1(cm): "))
            side2 = float(input("Enter a side2(cm): "))

            triangle = Triangle(height, width, side1, side2)
            print(f"Area: {triangle.calc_area}")
            print(f"Perimeter: {triangle.calc_perimeter}")

        case _:
            print("Nothing.")

main()