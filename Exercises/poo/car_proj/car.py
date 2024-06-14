class Car: # Creating base class named "car"
    all = []
    def __init__(self, name:str, year:int, color:str, price:float, inst:int): # Setting the attributes to the class
        self.name = name
        self.year = year
        self.color = color
        self.price = price
        self.inst = inst

        Car.all.append(self)

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name}, year={self.year}, color={self.color}, price={self.price}, inst={self.inst})")

    # Creating methods to the base class
    def calcInst(self) -> float:
        return (f"{float(self.price / self.inst):.2f} per month.")
    
    def message(self):
        return "Cars are very usefull!"