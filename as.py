from queue import PriorityQueue as PQ

import turtle
import time
import sys
from collections import deque

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A BFS Maze Solving Program")
wn.setup(1300,700)


# this is the class for the Maze
timeSpeed=0
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(timeSpeed)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(timeSpeed)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(timeSpeed)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(timeSpeed)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(timeSpeed)


# grid = [
# "+++++++++++++++",
# "+s+       + +e+",
# "+ +++++ +++ + +",
# "+ + +       + +",
# "+ +   +++ + + +",
# "+ + + +   + + +",
# "+   + +   + + +",
# "+++++ +   + + +",
# "+     +   +   +",
# "+++++++++++++++",
# ]

# grid = [
# "+++++++++",
# "+ ++s++++",
# "+ ++ ++++",
# "+ ++ ++++",
# "+    ++++",
# "++++ ++++",
# "++++ ++++",
# "+      e+",
# "+++++++++",
# ]

grid = [
"+++++++++++++++",
"+             +",
"+             +",
"+             +",
"+     e       +",
"+             +",
"+             +",
"+             +",
"+ s           +",
"+++++++++++++++",
]
# grid = [
# "+++++++++++++++++++++++++++++++++++++++++++++++++++",
# "+               +                                 +",
# "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
# "+s          +                 +               ++  +",
# "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
# "+  +     +  +           +  +                 +++  +",
# "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
# "+  +  +  +  +  +  +        +  +  +        +       +",
# "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
# "+  +     +  +          +   +           +  +  ++  ++",
# "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
# "+     +  +     +              +              ++   +",
# "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
# "+  +  +                    +     +     +  +  +++  +",
# "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
# "+  +  +     +     +     +  +  +     +     +  ++  ++",
# "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
# "+                       +  +  +              ++  ++",
# "+ ++++++             +  +  +  +  +++        +++  ++",
# "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
# "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
# "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
# "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
# "+      ++ +++++++e+++     ++          ++    +++++++",
# "+++++++++++++++++++++++++++++++++++++++++++++++++++",
#  ]


def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x,screen_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)

def endProgram():
    wn.exitonclick()
    sys.exit()

def search(x,y):
    distance1=((abs(end_x-start_x))**2+(abs(end_y-start_y))**2)**0.5

    frontier.put((distance1,[x,y]))
    solution[x,y] = x,y

    while not frontier.empty():
        time.sleep(0)
        node =frontier.get()
        templist = node[1]
        x,y=templist
        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = [x, y + 24]
            solution[cell[0],cell[1]] = x, y
            tempDist1=((abs(end_x-x))**2+(abs(end_y-(y+24)))**2)**0.5
            tempDist2=((abs(start_x-x))**2+(abs(start_y-(y+24)))**2)**0.5
            frontier.put((tempDist1+tempDist2,cell))
            visited.add((x, y + 24))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = [x, y - 24]
            solution[cell[0],cell[1]] = x, y
            tempDist1=((abs(end_x-x))**2+(abs(end_y-(y-24)))**2)**0.5
            tempDist2=((abs(start_x-x))**2+(abs(start_y-(y-24)))**2)**0.5
            frontier.put((tempDist1+tempDist2,cell))
            visited.add((x, y - 24))

        if(x - 24, y) in path and (x - 24, y) not in visited:
            cell = [x - 24, y]
            solution[cell[0],cell[1]] = x, y
            tempDist1=((abs(end_x-(x-24)))**2+(abs(end_y-y))**2)**0.5
            tempDist2=((abs(start_x-(x-24)))**2+(abs(start_y-y))**2)**0.5
            frontier.put((tempDist1+tempDist2,cell))
            visited.add((x-24, y))

        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = [x + 24, y]
            solution[cell[0],cell[1]] = x, y
            tempDist1=((abs(end_x-(x+24)))**2+(abs(end_y-y))**2)**0.5
            tempDist2=((abs(start_x-(x+24)))**2+(abs(start_y-y))**2)**0.5
            frontier.put((tempDist1+tempDist2,cell))
            visited.add((x +24, y))

        green.goto(x,y)
        green.stamp()
        if grid[int((288-y)/(24))][int((588+x)/24)] == "e":
            break

maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

walls = []
path = []
visited = set()
frontier = PQ()
solution = {}

setup_maze(grid)
print(end_x)
search(start_x,start_y)
wn.exitonclick()

