"""
File: circle.py
Draws a circle.

1. The inputs are the coourdinates of the center point and the radius.

"""

import math
from turtle import Turtle, TK

def drawCircle(t: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a circle with the given center point and radius."""
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)
    

def main() -> None:
    """Allows the user to enter the center point and the radius."""
    t = Turtle()
    while True:
        x = t.screen.numinput("Input", "Enter the x coordinate of the center or cancel to quit: ")
        if x is None:
            break
        y = t.screen.numinput("Input", "Enter the y coordinate of the center: ")
        radius = t.screen.numinput("Input", "Enter the radius: ")
        if(x is not None and y is not None and radius is not None and radius > 0):
            drawCircle(t, x, y, radius)
            break
        else:
            TK.messagebox.showerror("Error", "Please enter valid coordinates and a positive radius.")

if __name__ == "__main__":
   main()