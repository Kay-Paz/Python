import turtle
tina = turtle.Turtle()
tina.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for each_color in colors:
    angle = 360 / len(colors)
    # tina.fillcolor(each_color)
    # tina.begin_fill()
    tina.color(each_color)
    # tina.end_fill()
    tina.begin_fill()
    tina.circle(60)
    tina.end_fill()
    # tina.circle(40)
    # tina.circle(20)
    tina.right(angle)
    tina.forward(30)