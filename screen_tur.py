import turtle

wn = turtle.Screen()
ahmed = turtle.Turtle()
ahmed.color("blue")
ahmed.shape("turtle")
ahmed.penup()
for i in range(50):
    ahmed.forward(50)
    ahmed.stamp()
    ahmed.right(-50)
    ahmed.right(36)


wn.exitonclick()
