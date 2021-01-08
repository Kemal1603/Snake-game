import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.move_distance = 5

    def create_snake(self):
        for points in STARTING_POSITION:
            snake_parts = turtle.Turtle('square')
            snake_parts.shapesize(0.1, 0.1, 7)
            snake_parts.color('white')
            snake_parts.penup()
            snake_parts.goto(points)
            self.segments.append(snake_parts)

    def add_part(self):
        snake_parts = turtle.Turtle('square')
        snake_parts.shapesize(0.1, 0.1, 7)
        snake_parts.penup()
        snake_parts.color('white')
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        snake_parts.goto(x, y)
        self.segments.append(snake_parts)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].speed('slow')
        self.segments[0].forward(self.move_distance)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)

    def speed_up(self):
        if self.move_distance < 8:
            self.move_distance += 1


