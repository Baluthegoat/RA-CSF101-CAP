import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Start Button
start_button = turtle.Turtle()
start_button.speed(0)
start_button.color("white")
start_button.penup()
start_button.goto(0, 0)
start_button.write("Press 'Enter' to Start", align="center", font=("Courier", 24, "normal"))
start_button.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(2)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# function to detect collision 
def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 20:
        return True
    else:
        return False

# function to change the color of the food    
def change_food_color():
    colors = ["red", "blue", "yellow", "black", "white", "pink"]
    new_color = random.choice(colors)
    food.color(new_color)

# function to change the color of the snake head 
def change_head_color():
    colors = ["red", "blue", "yellow", "black", "white", "pink"]
    new_color = random.choice(colors)
    head.color(new_color)

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Start Game Function
def start_game():
    start_button.clear()
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(wn.bye, "Escape")
    game_loop()

# Main game loop
def game_loop():
    global score, high_score, delay

    while True:
        wn.update()

        # checking for collision with food
        if is_collision(head, food):
            change_food_color()
            change_head_color()

        # Check for a collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # change the color of the food
            change_food_color()

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1

                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

                time.sleep(delay)

        # Delay to control the speed of the snake
        time.sleep(delay)

# Listen for 'Enter' key press to start the game
wn.listen()
wn.onkeypress(start_game, "Return")
wn.listen()
wn.onkeypress(wn.bye, "Escape")

# Keep the window open
wn.mainloop()