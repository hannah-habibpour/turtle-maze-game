#4. Drawing the maze

import turtle

pen = turtle.Turtle()
pen.speed(0)

maze = [
    "11111",
    "10001",
    "10101",
    "10001",
    "11111"
]

start_x, start_y = -100, 100

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == "1":
            pen.penup()
            pen.goto(start_x + x * 20, start_y - y * 20)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(20)
                pen.right(90)
            pen.end_fill()

turtle.done()