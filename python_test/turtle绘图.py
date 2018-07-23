import turtle
import time
#绘制太阳花
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
#red为笔的颜色，yellow为填充的颜色
turtle.color("red", "yellow")
#准备开始填充图形
turtle.begin_fill()
for _ in range(20):
    turtle.forward(200)
    turtle.left(170)
#填充完成
turtle.end_fill()

#绘制五角星
turtle.penup()
turtle.goto(100,100) 
turtle.pendown()
turtle.color("red", "yellow") 
turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.left(144)
#填充完成
turtle.end_fill()

#隐藏箭头
turtle.hideturtle()
#必须是乌龟图形程序中的最后一个语句   
turtle.done()