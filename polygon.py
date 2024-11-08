import turtle
turtle.Screen().bgcolor("darkblue")
turtle.Screen().setup(300,300)
polygon=turtle.Turtle()
num_sides=6
angle=360/num_sides
side_length=70
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()