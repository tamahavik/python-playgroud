from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.speed("fastest")
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score : {self.score} High score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.show()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show()

    def save_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
