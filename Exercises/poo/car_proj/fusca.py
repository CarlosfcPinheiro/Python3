from car import Car

class Fusca(Car):
    def __init__(self, name, year, color, price, inst):
        super().__init__(
            name, year, color, price, inst
        )

    def commonPhrase(self):
        return "Fits everyone."