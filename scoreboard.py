from turtle import Turtle
ALLIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALLIGNMENT, font=FONT)