from tkinter import N
import turtle as t
import colorsys
t.width(4)
t.tracer(10)
t.bgcolor('black')
h=0
n=50
for i in range (150):
    c= colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n 
    t.pencolor(c)
    t.circle(i,10)
    t.forward(i)
    t.right(100)
    t.circle(i,200)
    t.forward(i)
    t.right(200)
t.done()