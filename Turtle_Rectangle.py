import turtle

t = turtle.Turtle()

length = 200   
breadth = 100  

for i in range(2):
    t.forward(length)
    t.left(90)
    t.forward(breadth)
    t.left(90)

turtle.done()
