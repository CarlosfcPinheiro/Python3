class Circle:
    pi_value = 3.14
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calc_area(self) -> float:
        return Circle.pi_value*(self.radius**2)
    
    def calc_perimet(self) -> float:
        return 2*Circle.pi_value*self.radius

def main():
    circle_radius = int(input("Enter a circle's radius(cm): "))
    circle = Circle(circle_radius)
    print(f"Circle's area: {circle.calc_area():.2f}cm²")
    print(f"Circle's perimeter: {circle.calc_perimet():.2f}cm")

main()