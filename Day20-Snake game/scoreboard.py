from turtle import Turtle
ALIGnMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.clear()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-50,0)
        self.write(f"GAME OVER. Final Score: {self.score}")