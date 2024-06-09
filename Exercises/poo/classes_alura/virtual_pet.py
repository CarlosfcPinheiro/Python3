class VirtualPet():
    def __init__(self, name, hungry=20, health=50, age=0):
        self.name = name
        self.hungry = hungry
        self.health = health
        self.age = age

    def calcHumor(self):
        humor = self.hungry + self.health
        return humor

    def feed(self):
        def checkHealthtoAdd(): # function to check health and then add it
            if (self.health < 95):
                self.health += 3
            elif (self.heath+3 > 100):
                self.heath += 100 - self.health

        if (self.hungry <= 95):
            self.hungry += 5
            self.health += 3
            if self.hungry == 100:
                print(f"You feed your pet :D")
                print(f"Your actual hungry is 100!")
            else:
                print(f"You feed your pet :D")
                print(f"Actual hungry: {self.hungry}")
        
        elif (self.hungry+5 > 100):
            self.hungry += 100 - self.hungry
            checkHealthtoAdd()  
            print("You feed your pet :D")
            print(f"You actual hungry is 100!")

    def showStatus(self):
        print(f"""{self.name}'s Satus:
            Hungry: {self.hungry}
            Health: {self.health}
            Hapiness: {}""")