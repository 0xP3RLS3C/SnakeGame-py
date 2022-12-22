from turtle import Turtle
ALLIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALLIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align=ALLIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align=ALLIGNMENT, font=FONT)