class Ball:
    def __init__(self, color, circuference, material):
        self.color = color
        self.cirecuference = circuference
        self.material = material
    
    def changeColor(self, newcolor):
        self.color = newcolor

    def showColor(self):
        return self.color
    
ball = Ball("red", 6, "rubber")
print(ball.showColor())