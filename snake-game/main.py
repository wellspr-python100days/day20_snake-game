from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from decoration import Decoration

import time

s = Screen()
s.listen()
s.setup(width=700, height=700, startx=0, starty=0)
s.title('Python Snake Game')
s.screensize(canvheight = 600, canvwidth = 600)
s.bgcolor('black')

t = Turtle(visible=False)
t.color('white')
t.penup()
t.write(f"Press 'space' key to start game.", align='center', font=('Arial', 12, 'normal') )

def snake_game(s):
    s.tracer(0)

    snake = Snake(screen=s)

    s.onkey(snake.up, 'Up')
    s.onkey(snake.down, 'Down')
    s.onkey(snake.left, 'Left')
    s.onkey(snake.right, 'Right')

    decoration = Decoration(screen=s)
    decoration.borders()

    score = ScoreBoard()
    food = Food()

    game_over = False

    while not game_over:
        s.update()
        time.sleep(.1) #SPEED

        snake.move()

        if snake.head.distance(food) < 20:
            snake.increase()
            food.refresh()
            score.increase()

        elif snake.hit_walls():
            game_over = True
            score.game_over()
        
        for segment in snake.segments[2:]:
            if snake.head.distance(segment) < 10:
                game_over = True
                score.game_over()


def play():
    s.resetscreen()
    snake_game(s)

s.onkey(play, 'space')

s.mainloop()