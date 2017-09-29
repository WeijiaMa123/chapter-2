import turtle
wn = turtle.Screen()
frank = turtle.Turtle()
sides=int(input("How much sides"))
for i in range(sides):
    frank.forward(100)
    frank.left(180-((sides-2)*180)/sides)