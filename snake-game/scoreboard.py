from turtle import Turtle
FONT = ('Arial', 18, 'bold')
ALIGNMENT = 'center'
COLOR = 'white'
POSITION = (0, 310)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(POSITION)
        self.color(COLOR)
        self.score = 0
        self.higher_score = self.get_higher_score()
        self.update()

    def increase(self):
        self.score += 1
        if self.score > self.higher_score:
            self.higher_score = self.score
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} / Higher score: {self.higher_score}", align=ALIGNMENT, font=FONT)

    def get_higher_score(self):
        value = 0
        with open("higher_score.txt") as hs:
            value = hs.read()
        return int(value)

    def update_higher_score(self):
        with open("higher_score.txt", mode="w") as hs:
            hs.write(str(self.higher_score))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -100)
        self.write(f"Press 'space' key to play again.", align=ALIGNMENT, font=("Arial", 12, "normal"))
        self.update_higher_score()
        