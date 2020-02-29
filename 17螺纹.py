
"""""
import turtle
length=int(input('请输入边长'))
angle=int(input('请输入角度'))
again=1
while again<length:
    turtle.forward(again)
    turtle.right(angle)
    again = again + 1
turtle.hideturtle()
turtle.done()
"""""
import turtle
length=int(input('请输入边长'))
angle=int(input('请输入角度'))
while length < 100:
    turtle.forward(length)
    turtle.right(angle)
    length = length + 1

