from turtle import Turtle
import random

SHAPE = 'circle'
COLOR = 'red'

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__(shape=SHAPE)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color(COLOR)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)