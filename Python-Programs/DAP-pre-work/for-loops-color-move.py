import turtle
tina = turtle.Turtle()
tina.shape('turtle')

color_list = ["violet", "blue", "purple", "green", "pink", "cyan", "teal", "crimson"]

tina.left(90)

for color in color_list:
    tina.left(5)
    tina.forward(20)
    tina.color(color)
    tina.write("What color am I now?")