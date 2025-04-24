import turtle
import time
level = 1
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
screen2 = turtle.Screen()
def triangle(signal1, signal2, signal3):
    screen2.tracer(0) 
    color = 1
    turtle.forward(10 + level)
    turtle.left(80)
    for i in range(3):
        if color == 1:
            turtle.pencolor("blue")
        elif color == 2:
            turtle.pencolor("green")
        elif color == 3:
            turtle.pencolor("red")
        if signal1 == True and color == 1:
            turtle.pendown()
        if signal2 == True and color == 2:
            turtle.pendown()
        if signal3 == True and color == 3:
            turtle.pendown()
        turtle.forward(120-(10 + level))
        turtle.left(120)
        turtle.penup()
        if color == 3:
            color = 0
        color +=1
    turtle.penup()
    screen2.update()
for i in range(300):
    level += 1
    triangle(True, True, True)
screen2.mainloop() 