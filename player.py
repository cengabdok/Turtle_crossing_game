from turtle import Turtle
import time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)      

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def restart(self):
        self.go_to_start()
    
