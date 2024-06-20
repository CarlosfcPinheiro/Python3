from math import pow
class Square:
    def __init__(self, sidelen:float):
        self.sidelen = sidelen

    def changeSidelen(self, new_sidelen):
        self.sidelen = new_sidelen

    def showSidelen(self) -> float:
        return self.sidelen
    
    def calcArea(self) -> float:
        area = float(pow(self.sidelen, 2))
        return area

square = Square(4)
print(square.calcArea())
print(square.changeSidelen(6))
print(square.showSidelen())
