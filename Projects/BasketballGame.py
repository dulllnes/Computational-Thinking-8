# ###############################################
# ### SETUP ###
import turtle
# ###############################################

# Create turtle object
t = turtle.Turtle()
t.speed(3)
t.penup()

# Draw the head
t.goto(0, 0)
t.pendown()
t.color("brown")
t.begin_fill()
t.circle(30)  # Head
t.end_fill()

# Draw the eyes
t.penup()
t.goto(-10, 10)  # Left eye position
t.pendown()
t.color("white")
t.begin_fill()
t.circle(5)  # Left eye
t.end_fill()

t.penup()
t.goto(10, 10)  # Right eye position
t.pendown()
t.begin_fill()
t.circle(5)  # Right eye
t.end_fill()

t.penup()
t.goto(-10, 10)  # Left pupil position
t.pendown()
t.color("black")
t.begin_fill()
t.circle(2)  # Left pupil
t.end_fill()

t.penup()
t.goto(10, 10)  # Right pupil position
t.pendown()
t.begin_fill()
t.circle(2)  # Right pupil
t.end_fill()

# Draw the body
t.penup()
t.goto(0, -30)
t.pendown()
t.color("blue")
t.begin_fill()
t.goto(0, -30)
t.goto(40, -100)  # Right arm
t.goto(20, -100)  # Right leg
t.goto(20, -30)   # Back to body
t.goto(0, -30)    # Back to the center
t.goto(-40, -100) # Left arm
t.goto(-20, -100) # Left leg
t.goto(-20, -30)  # Back to body
t.end_fill()

# Draw the basketball
t.penup()
t.goto(50, -80)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(20)  # Basketball
t.end_fill()

# Draw the basketball lines
t.color("black")
t.penup()
t.goto(50, -80)
t.pendown()
t.setheading(30)
t.circle(20, 60)  # Top line
t.penup()
t.goto(50, -80)
t.pendown()
t.setheading(-30)
t.circle(20, -60)  # Bottom line
t.penup()
t.goto(50, -80)
t.setheading(0)
t.pendown()
t.forward(20)  # Horizontal line

# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
