from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write_score()

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.update_high_score()
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, ALIGNMENT, FONT)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset_score(self):
        self.score = 0
        self.write_score()

    def update_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.score))
        self.high_score = self.score
