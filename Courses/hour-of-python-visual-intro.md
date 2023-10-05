# Hour of Python:

## A Visual Introduction

> A visual introduction to code using the Python programming language and Turtles.

###### *Taken as part of the pre-work for SAVVY Coders' Data Analytics & Python program.*

### [Index](https://hourofpython.com/a-visual-introduction-to-python/index.html)

### Welcome!

We begin by importing our `turtle` module to follow along with the exercises.

```python
import turtle
tina = turtle.Turtle()
tina.shape('turtle')
```

### Turtles!

- Learned how to make Tina draw `pendown()` or lift her pen so she doesn't draw `penup()`
- Learned how to make Tina move (i.e `tina.left(50)`)
- Learned about Tina's grid and how to make her move to specific points (i.e. `tina.goto(200,200)`)
- Learned how to make Tina draw a circle (i.e. `tina.circle(130)`)
- Learned how to make Tina draw a circle with a color
```python
tina.penup()
tina.begin_fill()
tina.color('green')
tina.goto(30,-150)
tina.pendown()
tina.circle(130)
```
- ^ that draws an empty circle with a green outline. to fill that circle in with green, you add:
```python
tina.penup()
tina.end_fill()
```
- Altogether, Tina now makes a filled-in white circle over her green circle
```python
tina.color('white')
tina.goto(0,0)
tina.begin_fill()
tina.pendown()
tina.circle(20)
tina.penup()
tina.end_fill()
```

### Repeating with Loops and Lists

- Using a `for loop` to have Tina move through specific points from a list of numbers

```python
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

number_list = [1,2,3,4,5,6,7,8,9,10] 

tina.color("green") 
for number in number_list: 
    tina.forward(number*10) 
    tina.left(60)
```
![image](https://github.com/Kay-Paz/Python/assets/91631432/24022b95-26c6-4c3a-b49b-bc96f927830e)

- Another example of using a `for loop` to write more efficient code:

```python
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.left(90)
tina.forward(20)
tina.write("What color am I now?")

tina.forward(20)
tina.color("blue")
tina.write("What color am I now?")

tina.forward(20)
tina.color("purple")
tina.write("What color am I now?")

tina.forward(20)
tina.color("green")
tina.write("What color am I now?")
```

^ *does the exact same thing as this:*

```python
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

color_list = ["black", "blue", "purple", "green"]

tina.left(90)

for color in color_list:
    tina.forward(20)
    tina.color(color)
    tina.write("What color am I now?")
```
![image](https://github.com/Kay-Paz/Python/assets/91631432/62e8fd6e-c313-4886-8ee9-531e06f0f3bd)

- `for loop` to draw and fill multiple circles of varying colors:
```python
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for each_color in colors:
    angle = 360 / len(colors)
    tina.color(each_color)
    tina.begin_fill()
    tina.circle(60)
    tina.end_fill()
    tina.right(angle)
    tina.forward(30)
```
![image](https://github.com/Kay-Paz/Python/assets/91631432/ee5267c1-ace0-4f8c-a033-db12f3dd3701)

### Multiple Turtles

- Our turtle does NOT have to be named `tina`. We can give it whatever name we wish, so long as we stay consistent with the name. For example:

```python
import turtle

bob = turtle.Turtle()
bob.shape('turtle')

bob.forward(100)
```

> Tina is a turtle. But what's a turtle? It's what's called an **object**. This means that a programmer has written some code that we can use to do cool things.
> In Tina's case, she knows how to go *forward, backward, left, and right* because the people who wrote the turtle object thought those would be neat things for turtles to do.
> At the beginning of all of our examples, we **import turtle**. This lets us use code that's already been written and gives Tina and any other turtles we make their abilities.
> You can give Tina a different name, and that newly named turtle will know how to do everything Tina does.

- Two turtles in one program:

```python
import turtle

tina = turtle.Turtle()
tina.shape('turtle')
tina.color('violet')

tina.left(90)
tina.forward(100)
tina.write("I'm Tina!")
tina.forward(20)
tina.right(90)

tommy = turtle.Turtle()
tommy.shape('turtle')
tommy.color('teal')

tommy.right(90)
tommy.forward(100)
tommy.write("I'm Tommy!")
tommy.forward(20)
tommy.left(90)
```
![image](https://github.com/Kay-Paz/Python/assets/91631432/279c5d33-95af-4a91-b898-910ace5e9db3)

### If-Else Statements

- `if-else` statement with `try-except`

> In the example below you'll see there are `try:` and `except:`. These lines try to run code that comes after `try:`, and if any errors happen, do what's in the `except:` section.
> This is how Tina knows whether you put in a real number like `15`. This is how real programmers change the behavior of programs based on any errors that might come up.

```python
import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

try:
    age = int(input("How old are you? (Use numbers)"))
    if age >= 10 and age <= 15:
        tina.write("You're between 10 and 15 years old")
        tina.backward(20)
    elif age < 10:
        tina.write("You're less than 10 years old")
        tina.backward(20)
    elif age > 15:
        tina.write("You're over 15 years old")
        tina.backward(20)
except:
    tina.backward(100)
    tina.write("I don't think I understand that age.  Are you using numbers?")
    tina.backward(20)
```
`try:`

![image](https://github.com/Kay-Paz/Python/assets/91631432/132ae67b-d241-493a-a81c-5e8fe3177582)

`except:`

![image](https://github.com/Kay-Paz/Python/assets/91631432/8ded299c-aa51-4aab-8662-da73619a06e1)

###### How High Up is Tina?

![image](https://github.com/Kay-Paz/Python/assets/91631432/121f8a06-c3ea-4ffe-9386-041a25681533)


> Line 9, **tina.pos()[1]** asks tina how far up or down the grid she is. `elif` is short for "else if".
> Each of the tests of height is tried in order until one is true. If none of the tests are true, the program moves on to the lines indented below `else`.
> In Python, `else` means, "if all else fails, do this". The `raise` inside the `else` block raises an error, which means switch to the `except` block.
> That's how the program can respond differently if you enter anything except a number in between `200` and `-200`.  

### Functions

> Earlier we talked about how **functions** are like recipes. In this exercise, we've already taught Tina the recipe for making a picture of a cake and she's made three.

```python
import turtle
tina=turtle.Turtle()
tina.shape('turtle')

def make_cake(x=0, y=0):
    tina.penup()
    tina.color('pink')
    tina.goto(x, y)
    tina.pendown()
    tina.begin_fill()
    tina.goto(x + 20, y)
    tina.goto(x + 20, y + 20)
    tina.goto(x - 20, y + 20)
    tina.goto(x - 20, y)
    tina.goto(x, y)  
    tina.end_fill()
    tina.goto(x, y + 20)
    tina.color('yellow')
    tina.goto(x, y + 35)
    tina.goto(x, y + 30)
    tina.color('black')
    tina.goto(x, y + 20)
    tina.penup()
    tina.goto(x, y + 10)

make_cake(0,0)
make_cake(-100,0)
make_cake(100,0)
```

![image](https://github.com/Kay-Paz/Python/assets/91631432/7e470195-2eb0-4678-8241-bdb7ff02604b)



### You Did It!

![image](https://github.com/Kay-Paz/Python/assets/91631432/2d02d12e-0add-466d-90ee-3837407f9fd3)

```python
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.end_fill()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(10)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("I completed an Hour of Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)
tommy.write("Try it out at HourofPython.com", align="center", font=(None, 16, "bold"))
tommy.goto(0,-110)
```

![image](https://github.com/Kay-Paz/Python/assets/91631432/5e638ad0-697c-4ff2-ada5-ef5b928fe241)

