import turtle

def drawing():
    window = turtle.Screen()
    window.bgcolor("red")


    point = turtle.Turtle()
    point.shape("turtle")
    point.color("yellow")
    point.speed(3)


    point.forward(100)
    point.right(90)
    point.forward(100)
    point.right(90)
    point.forward(100)
    point.right(90)
    point.forward(100)
    point.right(90)

    pen = turtle.Turtle("turtle")
    pen.color("blue")
    pen.speed(5)
    pen.circle(100)

    window.exitonclick()

drawing()