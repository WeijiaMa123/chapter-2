import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
clock = turtle.Turtle()
clock.shape("turtle")
clock.color("blue")
for i in range(12):
    clock.penup()
    clock.forward(100)
    clock.stamp()
    clock.backward(100)
    clock.left(30)

 
 