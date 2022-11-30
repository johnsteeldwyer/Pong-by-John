from turtle import Turtle


class Score(Turtle):
    def __init__(self, side):
        super().__init__()
        self.points = 0
        self.create_scoreboard(side)

    def create_scoreboard(self, side):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(215)
        if side == "l":
            self.setx(-100)
        elif side == "r":
            self.setx(100)
        self.update()

    def score(self):
        self.points += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.points}", False, "center", ("Courier", 60, "bold"))
