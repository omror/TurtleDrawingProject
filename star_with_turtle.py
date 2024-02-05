import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("Green")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()

for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(100)
turtle.done()
