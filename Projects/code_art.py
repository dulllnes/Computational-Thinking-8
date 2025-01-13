import turtle
t = turtle.Turtle()



#Eyes
t.penup()
t.goto(-155, 0)
t.color("black")
t.pendown()

t.left(60)
t.forward(28)
t.right(60)
t.forward(50)
t.right(60)
t.forward(26)

t.penup()
t.goto(-148, 7)
t.pendown()

t.forward(18)
t.left(60)
t.forward(48)
t.left(60)
t.forward(20)

t.penup()
t.goto(-130, 24)
t.pendown()

t.right(150)
t.begin_fill()
for i in range (2):
    t.forward(34)
    t.left(90)
    t.forward(28)
    t.left(90)
t.end_fill()

t.penup()
t.goto(130, 0)
t.color("black")
t.pendown()

t.left(90)
t.left(60)
t.forward(28)
t.right(60)
t.forward(50)
t.right(60)
t.forward(26)

t.penup()
t.goto(135, 7)
t.pendown()

t.forward(18)
t.left(60)
t.forward(48)
t.left(60)
t.forward(20)

t.penup()
t.goto(155, 24)
t.pendown()

t.right(150)
t.begin_fill()
for i in range (2):
    t.forward(34)
    t.left(90)
    t.forward(28)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-140,30)
t.pendown()

t.right(270)
t.forward(53)

t.penup()
t.goto(140,30)
t.pendown()

t.forward(53)

t.penup()
t.goto(-70,20)
t.pendown()

t.right(60)
t.forward(20)
t.right(70)
t.forward(20)

t.penup()
t.goto(120,20)
t.pendown()

t.left(130)
t.left(240)
t.forward(20)
t.left(70)
t.forward(20)

#mouth
t.penup()
t.goto(-100,-150)
t.pendown()

t.right(310)
t.forward(150)


#Square
t.penup()
t.goto(-250,-200)
t.pendown()

for i in range(4):
    t.forward(420)
    t.left(90)

#Spiral
t.penup()
t.goto(0,0)
t.pendown()

colors = ["pink","cyan","yellow"]
for i in range(200):
    t.color(colors[i % 3])
    t.forward(3 + i)
    t.left(15)



turtle.exitonclick()