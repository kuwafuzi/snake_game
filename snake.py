from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_snakes.append(new_segment)

    def reset(self):
        for seg in self.all_snakes:
            seg.goto(1000, 1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]

    def extend(self):
        self.add_segment(self.all_snakes[-1].position())

    def move(self):
        for seg_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[seg_num - 1].xcor()
            new_y = self.all_snakes[seg_num - 1].ycor()
            self.all_snakes[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
