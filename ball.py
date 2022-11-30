import turtle
import random as r

BASE_SPEED = 4


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(.7, .7, 0)
        self.setheading(25)
        self.adjusted_speed = BASE_SPEED

    def move(self):
        # Change tiltangle so ball doesnt rotate
        self.tiltangle(self.heading() * -1)
        self.forward(self.adjusted_speed)

    def bounce(self):
        heading = self.heading()
        self.setheading((heading - 360) * -1)
        self.adjusted_speed -= 0.2
        self.move()

    def volley(self):
        # Pick a random destination angle
        y_destination = r.randint(-700, 700)
        # Right paddle hit
        if self.xcor() > 0:
            self.setheading(self.towards(-400, y_destination))
        # Left paddle hit
        else:
            self.setheading(self.towards(400, y_destination))
        # Add speed when ball is hit
        self.adjusted_speed += 0.5
        self.move()

    def reset(self):
        self.adjusted_speed = BASE_SPEED
        self.setpos(0, 0)
