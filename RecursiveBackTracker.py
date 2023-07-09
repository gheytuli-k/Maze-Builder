import turtle
import numpy as np
import random
from typing import Tuple

def draw_maze_box(width: int = 400, height: int = 400, wall_width: int = 4, drawing_speed: int = 2) -> None:
    """
    :param width: The width of the maze
    :type width: int
    :param height: The height of the maze
    :type width: int
    :param wall_width: The thickness of the walls
    :type wall_width: int
    :param drawing_speed: The speed that the maze will be draw with
    :type drawing_speed: int
    :return: None
    """
    maze_object = turtle.Turtle()  # Making a turtle object
    maze_object.hideturtle()  # hiding the cursor

    maze_object.speed(drawing_speed)  # Setting the drawing speed
    maze_object.width(wall_width)

    maze_object.penup()
    maze_object.goto(-width/2, -height/2) # Setting the bottom right corner of the maze
    maze_object.pendown()

    maze_object.forward(width)  # Drawing the bottom wall
    maze_object.left(90)  # Rotating 90 degrees

    maze_object.forward(height)  # Drawing the right wall
    maze_object.left(90)  # Rotating 90 degrees

    maze_object.forward(width)  # Drawing the upper wall
    maze_object.left(90)  # Rotating 90 degrees

    maze_object.forward(height)  # Drawing the left wall

    turtle.Screen().exitonclick()  # Close the window by clicking on the screen


# Call the draw_maze_box function
#draw_maze_box(400, 400)

def index_mapper(point: Tuple) -> int:
    """"
    :param point: The point that we want to map it to an index
    :type point: Tuple
    :return: Index of the mapped point
    :rtype: int
    """
    
    x, y = point
    return x * 30 + y

def maze_maker(nr_rows: int, nr_cols: int) -> np.array:
    maze = np.array((nr_rows**2, nr_cols**2)) # Create the maze
    starting_vertex = (0, 0) # The position that the maze would start
    stack = [] # Defining a stack to store vertecies in it
    explored_vertices = set() # A set to make sure not to explore a vertex more than once
    
    current_vertex = starting_vertex
    explored_vertices.add(current_vertex)
    while True:
        stack.append(current_vertex)

        curr_x, curr_y = current_vertex
        # Storing all the possible neighbors of the current vertex
        neighbors = [(curr_x, curr_y+1), (curr_x, curr_y-1), (curr_x+1, curr_y), (curr_x-1, curr_y)]

        # Removing all the neighbors outside the maze
        neighbors = [(x, y) for (x, y) in neighbors if (0 <= x <= nr_cols) and (0 <= y <= nr_rows) and
                      ((x, y) not in explored_vertices)]
        
        next_vertex = random.choice(neighbors)        

maze_maker(30, 30)