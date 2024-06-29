class Rect:
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def changeSides(self, new_sideA, new_sideB):
        self.sideA = new_sideA
        self.sideB = new_sideB

    def showSides(self) -> tuple:
        sides = (self.sideA, self.sideB)
        return sides
    
    def calcArea(self) -> float:
        return self.sideA * self.sideB
    
    def calcPerimeter(self) -> float:
        return self.sideA + self.sideB
    
def main() -> None:
    side_a = float(input("Enter width: "))
    side_b = float(input("Enter height: "))
    rect = Rect(side_a, side_b)

    pisos_t = float(input("\nEnter floor's size: "))
    pisos_t_area = pow(pisos_t, 2)
    quantity = rect.calcArea() / pisos_t_area

    print(f"With a ground meassuring {rect.calcArea()}m² you will need {quantity} floors for this.")

main()
