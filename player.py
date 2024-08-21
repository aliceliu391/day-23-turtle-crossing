from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.reset_position()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def check_completion(self):
        if self.ycor() > 280:
            self.reset_position()
            return True

    def reset_position(self):
        self.goto(STARTING_POSITION)