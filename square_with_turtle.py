import turtle

turtle_instance = turtle.Turtle()
drawing_board = turtle.Screen()
drawing_board.bgcolor("Green")

for i in range(4):
    turtle_instance.forward(50)
    turtle_instance.left(90)

turtle.done()
