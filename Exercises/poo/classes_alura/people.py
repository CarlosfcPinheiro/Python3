class People:
    def __init__(self, name, age:int, weight:float, height:float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def Growing(self, years):
        self.age += years
        if (self.age < 21):
            self.height += 0.5
    
    def fatten(self, weight):
        self.fatten += weight

    def grow(self, height):
        self.height += height
