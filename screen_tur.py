import turtle

wn = turtle.Screen()

ahmed = turtle.Turtle()
wn.bgcolor("black")
# Make the width thicker so that the line will be easier to see
ahmed.width(5)
# Move back without drawing anything
ahmed.penup()
ahmed.back(140)
ahmed.pendown()

# Draw three red lines, with space in between
ahmed.color("red")
for colors in ["red", "orange", "yellow"]:
    ahmed.color(colors)
    ahmed.forward(50)
    ahmed.penup()
    ahmed.forward(50)
    ahmed.pendown()



wn.exitonclick()
