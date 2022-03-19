import random
import turtle
import sys
turtle.screensize(500,500)
turtle.setpos(-315,250)
turtle.ht()
turtle.penup()
turtle.right(90)
turtle.color("white")
turtle.bgcolor("black")
turtle.write('Discord singleplayer. By Minty')
turtle.forward(15)
URNE = turtle.textinput("Discord", "Username here")
FLNE = (URNE + '#' + str(random.randint(0,100)))
while True:
    Message = turtle.textinput("Discord", "Write what you want to say down here")
    turtle.write(FLNE + ' : ' + Message)
    if Message == ("exit"):
        sys.exit()
    turtle.forward(15)
    
     
