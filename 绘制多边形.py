import turtle
def draw(sides,length):
    angle=360/sides
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)
print(draw(5,100))