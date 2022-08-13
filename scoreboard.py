from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Gill Sans', 25, "bold"))

