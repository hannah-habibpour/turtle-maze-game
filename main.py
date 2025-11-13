import turtle

# --- Setup window ---
window = turtle.Screen()
window.setup(width=620, height=620)
window.bgcolor("white")
try:
    window.title("Amazing Maze (Turtle Edition)")
except:
    pass
window.tracer(0)

# --- Create the pen for drawing the maze ---
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("blue")
pen.pensize(3)

# --- Player setup ---
player = turtle.Turtle()
player.shape("circle")
player.color("red")
player.penup()
player.speed(0)
player.goto(-245, 270)  # starting position

# --- Maze design (1 = wall, 0 = empty) ---
maze = [
"10111111111111111111",
"10000000010000010001",
"11010111011011010101",
"10010101000010010111",
"11010101011110110101",
"10000101110000000001",
"10110101010010111101",
"10100001011110101001",
"10111100010010101011",
"11101001011010101011",
"10001111001010100001",
"11101000001000111111",
"10000011111010000001",
"11110000010010101101",
"10011111010010101001",
"10111011111011111001",
"10100000010010001101",
"10111011011110100001",
"10000010000000101101",
"10111111111111111111"
]

walls = []

# --- Draw the maze ---
def draw_maze():
    pen.penup()
    start_x = -290
    start_y = 290
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            char = maze[y][x]
            screen_x = start_x + (x * 30)
            screen_y = start_y - (y * 30)
            if char == "1":
                pen.goto(screen_x, screen_y)
                pen.begin_fill()
                for _ in range(4):
                    pen.forward(30)
                    pen.right(90)
                pen.end_fill()
                walls.append((screen_x, screen_y))
    pen.penup()

draw_maze()

# --- Collision detection ---
def touching_wall(x, y):
    for wall_x, wall_y in walls:
        if (wall_x - 15 < x < wall_x + 30) and (wall_y - 30 < y < wall_y + 15):
            return True
    return False

# --- Win condition ---
def check_win():
    if player.ycor() < -280:
        show_win_message()

def show_win_message():
    # Stop player movement and show win text
    window.tracer(1)
    message = turtle.Turtle()
    message.hideturtle()
    message.penup()
    message.goto(0, 0)
    message.color("green")
    message.write("🎉 YOU WON! 🎉", align="center", font=("Arial", 26, "bold"))
    # stop listening so player can’t move anymore
    window.onkey(None, "Left")
    window.onkey(None, "Right")
    window.onkey(None, "Up")
    window.onkey(None, "Down")

# --- Movement functions ---
def move_left():
    x, y = player.position()
    new_x = x - 10
    if not touching_wall(new_x, y):
        player.goto(new_x, y)
    check_win()

def move_right():
    x, y = player.position()
    new_x = x + 10
    if not touching_wall(new_x, y):
        player.goto(new_x, y)
    check_win()

def move_up():
    x, y = player.position()
    new_y = y + 10
    if not touching_wall(x, new_y):
        player.goto(x, new_y)
    check_win()

def move_down():
    x, y = player.position()
    new_y = y - 10
    if not touching_wall(x, new_y):
        player.goto(x, new_y)
    check_win()

# --- Keyboard bindings ---
window.listen()
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")

# --- Game loop ---
while True:
    window.update()
