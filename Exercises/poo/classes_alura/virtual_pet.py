class VirtualPet:
    def __init__(self, name: str, hungry=100, health=100, age=0):
        self.name = name
        self.hungry = hungry
        self.health = health
        self.age = age

    def feed(self):
        def checkHealth():
            if self.health <= 97:
                self.health += 3
            else:
                self.heatl += 100 - self.health

        if (self.hungry < 95):
            self.hungry += 5
            checkHealth()
        else:
            self.hungry += 100 - self.hungry
            checkHealth()

    def showStatus(self):
        print(f"\n{self.name}'s Status:")
        print(f" -> Health: {self.health}")
        print(f" -> Hungry: {self.hungry}")
        print(f" -> Age: {self.age}")
        print(f" -> Hapiness: {self.hungry + self.health}")

    def showHapiness(self):
        hapiness = self.hungry + self.health 
        if (hapiness < 100):
            print(f"Your level of hapiness is {hapiness}.")
            print(f"Make it more happy!")
        elif (hapiness < 20):
            print(f"Your hapiness level is {hapiness}.")
            print(f"It is very sad :(")
        elif (hapiness >= 100):
            print(f"Your hapiness level is {hapiness}.")
            print(f"It is really happy :)")
        

pet = VirtualPet("Coisa", 80, 50, 2)
pet.showStatus()
pet.showHapiness()
pet.feed()
pet.showStatus()