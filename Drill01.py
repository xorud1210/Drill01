import turtle

def move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

turtle.shape('turtle')

turtle.onkey(move_up,'w')
turtle.listen()
             
