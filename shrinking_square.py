import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Shrinking Squares")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")


def shrinkingsquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5


shrinkingsquare(150)
shrinkingsquare(130)
shrinkingsquare(110)
shrinkingsquare(90)


turtle.done()
