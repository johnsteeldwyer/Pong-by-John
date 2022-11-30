from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(4, .8, 0)
        self.goto(position)

    def up(self):
        if self.ycor() < 258:
            self.sety(self.ycor() + 25)

    def down(self):
        if self.ycor() > -258:
            self.sety(self.ycor() - 25)
