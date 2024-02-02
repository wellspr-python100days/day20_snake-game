from turtle import Turtle

BORDER_COLOR = 'gray'
BORDER_WIDTH = 2

class Decoration(Turtle):
    
    def __init__(self, screen):
        super().__init__(visible=False)
        self.screen = screen
        self.max_x = screen.canvwidth/2
        self.min_x = -screen.canvwidth/2    
        self.max_y = screen.canvheight/2
        self.min_y = -screen.canvheight/2

    def borders(self):
        self.speed('fastest')
        self.color('gray')
        self.pensize(2)
        self.penup()
        # DRAW A SQUARE BORDER
        self.goto(self.min_x, self.max_y) #top left
        self.pendown()
        self.goto(self.max_x, self.max_y) #top right
        self.goto(self.max_x, self.min_y) #bottom right
        self.goto(self.min_x, self.min_y) #bottom left
        self.goto(self.min_x, self.max_y) #top left
