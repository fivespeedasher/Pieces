import turtle
#if的用法学一下


for again in range(360):
    turtle.forward(1)
    turtle.right(1)

turtle.penup()
turtle.goto(120,120)
turtle.write('circle',font=("times",18,"bold"))
turtle.done()
"""
again = 0
while again < 360:
    turtle.forward(1)
    turtle.right(1)
    again = again + 1

turtle.penup()
turtle.goto(150,150)
turtle.pendown()
turtle.begin_fill()
turtle.color("purple")
turtle.circle(40,steps=10) # Draw a circle
turtle.end_fill() # Fill the shape
turtle.penup()
turtle.goto(-30,-30)
turtle.write('circle')
turtle.hideturtle()
turtle.done()"""