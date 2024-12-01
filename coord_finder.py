import turtle
from turtle import Screen
import pandas as pd
screen=Screen()
screen.setup(850,850)
screen.bgpic("new_erangel.gif")

def mouse(x,y):
            print(x,y)

screen.onscreenclick(mouse)

turtle.mainloop()