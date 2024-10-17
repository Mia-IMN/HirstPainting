import colorgram
import turtle
import random

num_of_colors = 30
colors = colorgram.extract('img.jpg', num_of_colors)

# my_colors = [(None, None, None)] * num_of_colors
#
# for _ in range(0, num_of_colors):
#     extracted_color = colors[_].rgb
#     Red = extracted_color[0]
#     Green = extracted_color[1]
#     Blue = extracted_color[2]
#     my_colors[_] = (Red, Green, Blue)

my_colors = []

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    my_colors.append((red, green, blue))

tony = turtle.Turtle()
tony.shape("circle")
tony.speed("fastest")
screen = turtle.Screen()

screen.colormode(255)

tony.hideturtle()
tony.penup()
tony.setheading(225)
tony.forward(300)
tony.setheading(0)

i = 0
ycor = -212.13
while i < 10:
    for _ in range(10):
        random_color = random.choice(my_colors)
        tony.color(random_color)
        tony.dot(20, random_color)
        tony.forward(50)

    ycor += 50
    tony.goto(-212.13, ycor)
    i += 1

screen.exitonclick()
