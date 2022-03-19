import turtle
turtle.color('red')
turtle.bgcolor("black")
turtle.penup()
turtle.speed(0)
turtle.title('Walking game')

def Up():
    turtle.forward(10)
def Down():
    turtle.back(10)
def Left():
    turtle.left(90)
def Right():
    turtle.right(90)

turtle.onkey(Up, "w")
turtle.listen()
turtle.onkey(Left, "a")
turtle.listen()
turtle.onkey(Down, "s")
turtle.listen()
turtle.onkey(Right, "d")
turtle.listen()
