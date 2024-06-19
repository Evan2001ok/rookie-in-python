import turtle
    
class bluemood(turtle.Turtle):# bluemood inherits from Turtle
    def __init__(self): #initial set
        super().__init__()
        self.color("blue")
        self.width(10)