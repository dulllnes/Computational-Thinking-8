
import turtle
import time
import random

rotation_speed = 0.5
spawn_interval = 0.05
ball_speed = 2

#Set up window
window = turtle.Screen()
window.tracer(0)

spinner = turtle.Turtle()

#Spawn new balls
colour = random.random(), random.random(), random.random()

balls = []

def spawn_ball(reference):
    balls.append(turtle.Turtle())
    balls[-1].shape("circle")
    balls[-1].color(colour)
    balls[-1].turtlesize(0.5)
    balls[-1].penup()
    balls[-1].setposition(reference.position())
    balls[-1].setheading(reference.heading())

#Main animation loop
spawn_timer = time.time()
while True:
    spinner.left(rotation_speed)

    #Spawn new ball
    if time.time() - spawn_timer > spawn_interval:
        spawn_ball(spinner)
        spawn_timer = time.time()
    
    #Move all balls and clear balls that leave the screen
    for ball in balls:
        ball.forward(ball_speed)
        #check if ball has left the screen
        if (
            abs(ball.xcor()) > window.window_width() / 2
            or abs (ball.ycor()) > window.window_height() / 2
        ):
            ball.hideturtle()
            balls.remove(ball)

        

    window.update()

turtle.done()