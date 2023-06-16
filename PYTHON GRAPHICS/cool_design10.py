import turtle 
import colorsys
turtle.bgcolor('black')
s=turtle.Turtle()
s.speed(20)
s.pencolor('red')
for i in range(200):
    s.forward(i)
    c = colorsys.hsv_to_rgb(i,1,0.9)
    s.left(90)
    s.right(10)
turtle.done()