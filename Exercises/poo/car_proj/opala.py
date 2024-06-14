from car import Car

class Opala(Car): # Creating an derivate/child class that inherit the base class methods
    def __init__(self, name, year, color, price, inst):
        # Car.__init__(self, name, year, color, price, inst) or -->
        super().__init__(
            name, year, color, price, inst
        )

    def commonPhrase(self):
        return "Never leaves you."