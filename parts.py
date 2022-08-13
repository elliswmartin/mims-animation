import turtle
import time
from turtle import pensize,goto,forward,backward,penup,pendown,left,right,begin_fill,end_fill,hideturtle,circle,color,setheading,clear
from helpers import setup

def draw_c1(x1, y1, size1):
    #draws circle 1 of cloud
    color("light cyan")
    setup(x1, y1)
    begin_fill()
    circle(size1)
    end_fill()
    hideturtle()

def draw_c2(x2, y2, size2):
    # draws circle 2 of cloud
    color("light cyan")
    goto(x2, y2)
    begin_fill()
    circle(size2)
    end_fill()
    hideturtle()

def draw_c3(x3, y3, size3):
    # draws circle 3 of cloud
    color("light cyan")
    goto(x3, y3)
    begin_fill()
    circle(size3)
    end_fill()
    hideturtle()

def draw_c4(x4, y4, size4):
    # draws circle 4 of cloud
    color("light cyan")
    goto(x4, y4)
    begin_fill()
    circle(size4)
    end_fill()
    hideturtle()

def draw_base(x1, y1, x4, y4, height):
    # draws base of the cloud
    goto(x1, y1)
    color("light cyan")
    begin_fill()
    left(90)
    forward(height)
    right(90)
    goto(x4, y4 + height)
    right(90)
    forward(height)
    end_fill()
    hideturtle()

def draw_cloud(x1,y1,size1,x2,y2,size2,x3,y3,size3,x4,y4,size4,height):
    color("light cyan")
    draw_c1(x1, y1, size1)
    draw_c2(x2, y2, size2)
    draw_c3(x3, y3, size3)
    draw_c4(x4, y4, size4)
    draw_base(x1, y1, x4, y4, height)
    hideturtle()

def drawRays(length, radius):
    # rays for the sun
    color("gold")
    pensize(2)
    for i in range(8):
        penup()
        goto(200,200)
        forward(radius)
        pendown()
        forward(length)
        penup()
        backward(length + radius)
        left(45)

def draw_circle(radius):
    # circle for the sun
    setup((200+radius), 200)
    color("gold")
    begin_fill()
    circle(radius)
    end_fill()
    hideturtle()

def draw_rainbow(start_x, start_y):
    # draws a single 7 color rainbow
    size = 300
    for i in range(7):
        if i % 7 == 0:
            color("red")
        elif i % 7 == 1:
            color("orange")
        elif i % 7 == 2:
            color("yellow")
        elif i % 7 == 3:
            color("green")
        elif i % 7 == 4:
            color("blue")
        elif i % 7 == 5:
            color("purple")
        else:
            color("violet")
        start_x = start_x + 30
        size = size - 30
        penup()
        setheading(0)
        goto(start_x, start_y)
        pendown()
        begin_fill()
        right(90)
        circle(size, -180)
        end_fill()

def move_rainbow(start_x, start_y, num_frames, screen, sleeptime):
    # animates the rainbow
    for j in range(num_frames):
        if j < num_frames // 2:
            start_x = start_x + 20
            # x + number -- decrease number to make smoother
        if j > num_frames // 2:
            start_x = start_x - 20
        draw_rainbow(start_x, start_y)
        screen.update()
        time.sleep(sleeptime)
        clear()