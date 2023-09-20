
import colorgram
import turtle
from turtle import Turtle, Screen
import random
franklin = Turtle()
turtle.colormode(255)
color_list = [(202, 164, 110), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208),
              (168, 99, 102),  (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

franklin.penup()
franklin.setheading(225)
franklin.forward(300)
franklin.setheading(0)
number_of_dots = 100

for _ in range(1, number_of_dots+1):
    franklin.dot(20, random.choice(color_list) )
    franklin.forward(50)
    if _ % 10 == 0:
        franklin.left(90)
        franklin.forward(50)
        franklin.left(90)
        franklin.forward(500)
        franklin.setheading(0)


screen = Screen()
screen.exitonclick()