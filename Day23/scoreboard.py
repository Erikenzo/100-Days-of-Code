from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def display_score(self):
        self.goto(-290,270)
        self.write("Level 1", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.goto(-290, 270)
        self.increasing_level()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increasing_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 50, "normal"))