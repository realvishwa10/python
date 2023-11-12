from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = file.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        with open("data.txt") as file:
            self.highscore = file.read()
        if self.score > int(self.highscore):
            highscore = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{highscore}")
        self.score = 0

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
