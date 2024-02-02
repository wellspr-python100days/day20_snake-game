from turtle import Turtle

COLOR = 'green'
HEAD_INITIAL_POS = {'x': -10, 'y': 10}

class Snake:

    def __init__(self, screen) -> None:
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]
        self.screen = screen
        

    def generate_segment(self):
        t = Turtle(shape='square', visible=False)
        t.color(COLOR)
        t.penup()
        return t


    def initialize_snake(self):
        for i in range(3):
            t = self.generate_segment()
            t.showturtle()
            t.goto(HEAD_INITIAL_POS['x'] - i * 20, HEAD_INITIAL_POS['y'])
            self.segments.append(t)
    

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].showturtle()
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        self.head.forward(20)
        #self.connect_walls()

    
    def increase(self):
        new_segment = self.generate_segment()
        self.segments.append(new_segment)


    def connect_walls(self):
        height = int(self.screen.canvheight/2)
        width = int(self.screen.canvwidth/2)

        if self.head.xcor() > width or self.head.xcor() < -width:
            x = -width+10 if self.head.xcor()>0 else width-10
            y = self.head.ycor()
            self.head.goto(x, y)
        elif self.head.ycor() > height or self.head.ycor() < -height:
            x = self.head.xcor()
            y = -height+10 if self.head.ycor()>0 else height-10
            self.head.goto(x, y)


    def hit_walls(self):
        height = int(self.screen.canvheight/2)
        width = int(self.screen.canvwidth/2)

        hit_right_wall = self.head.xcor() > width
        hit_left_wall = self.head.xcor() < -width
        hit_top_wall = self.head.ycor() > height
        hit_bottom_wall = self.head.ycor() < -height

        return hit_left_wall or hit_right_wall or hit_top_wall or hit_bottom_wall


    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)


    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)


    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)


    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)
