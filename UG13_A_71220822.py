import turtle
window = turtle.Screen()
a = turtle.Turtle()
def angka2(ulang):
    for i in range(ulang):
        a.pendown()
        a.color('blue')
        a.forward(50)
        a.back(50)
        a.left(90)
        a.forward(43.5)
        a.right(90)
        a.forward(50)
        a.left(90)
        a.forward(43.5)
        a.left(90)
        a.forward(50)
        a.left(90)
        a.forward(5)
        a.penup()
        a.sety(0)
        a.setheading(0)
        a.forward(80)
a.pensize(3)
a.penup()
a.setx(-200)
#buat huruf A
a.pendown()
a.color('black')
a.left(60)
a.forward(100)
a.right(120)
a.forward(100)
a.back(35)
a.setheading(0)
for i in range(2):
    a.left(180)
    a.forward(67)
a.setheading(300)
a.forward(35)
a.setheading(0)
a.penup()
a.forward(30)
#buat angaka 8
a.pendown()
a.color('Green')
for i in range(2):
    a.forward(50)
    a.left(90)
    a.forward(87)
    a.left(90)
a.setheading(90)
a.forward(43.5)
a.right(90)
a.forward(50)
a.sety(0)
a.penup()
a.forward(30)
#buat angka 2
angka2(2)
#buat huruf P
a.left(90)
a.pendown()
a.color('brown')
a.forward(87)
for i in range(3):
    a.right(90)
    a.forward(40)
a.sety(0)
a.setheading(0)
a.penup()
a.forward(80)
#amogus
a.pendown()
a.color('red')
a.fillcolor('red')
a.begin_fill()
a.forward(50)
a.left(90)
a.forward(50)
a.circle(25, 180)
a.forward(50)
#kaki
a.forward(40)
a.setheading(180)
a.circle(10,180)
a.forward(20)
a.left(90)
a.forward(60)
a.setheading(0)
a.forward(10)
a.setheading(270)
a.forward(40)
a.setheading(180)
a.circle(10,180)
a.forward(20)
a.left(90)
a.forward(60)
a.setheading(0)
a.forward(20)
a.left(90)
a.forward(30)
a.circle(20,90)
a.end_fill()
a.color("black")
a.setheading(270)
a.forward(50)
a.back(50)
a.setheading(180)
a.penup()
a.forward(5)
a.pendown()
a.fillcolor('gray')
a.begin_fill()
a.forward(40)
a.back(40)
a.setheading(90)
a.circle(20,180)
a.end_fill()
window.bgpic("nahidasus.png")
window.exitonclick()