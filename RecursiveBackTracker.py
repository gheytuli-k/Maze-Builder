import turtle
import numpy as np
import random
from typing import Tuple


def draw_maze_box(nr_rows: int, width: int = 400, height: int = 400, wall_width: int = 4, drawing_speed: int = 0) -> None:
    """
    :param nr_rows: Number of rows and column inside the maze
    :type nr_rows: int
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
    # Setting the bottom right corner of the maze
    maze_object.goto(-width/2, -height/2)
    maze_object.pendown()

    maze_object.forward(width)  # Drawing the bottom wall
    maze_object.left(90)  # Rotating 90 degrees

    maze_object.forward(height)  # Drawing the right wall
    maze_object.left(90)  # Rotating 90 degrees

    maze_object.forward(width)  # Drawing the upper wall
    maze_object.left(90)  # Rotating 90 degrees

    maze_object.forward(height)  # Drawing the left wall

    # Drawing all the walls for cells in the maze

    # Drawing the horizantile lines
    maze_object.left(90)  # Rotating 90 degrees
    for row in range(1, nr_rows):
        maze_object.penup()
        maze_object.goto(-width/2, -height/2 + row*height/nr_rows)
        maze_object.pendown()
        maze_object.forward(width)

    # Drawing the vertical lines
    maze_object.left(90)  # Rotating 90 degrees
    for column in range(1, nr_rows):
        maze_object.penup()
        maze_object.goto(-width/2 + column*width/nr_rows, -height/2)
        maze_object.pendown()
        maze_object.forward(height)

    turtle.Screen().exitonclick()  # Close the window by clicking on the screen


# Call the draw_maze_box function
draw_maze_box(30, 600, 600)


def index_mapper(point: Tuple, col_size: int) -> int:
    """"
    :param point: The point that we want to map it to an index
    :type point: Tuple
    :param col_size: The dimentions of the maze
    :type col_size: int
    :return: Index of the mapped point
    :rtype: int
    """

    x, y = point
    return x * col_size + y


def maze_maker(nr_cols_rows: int, starting_vertex: Tuple = (0, 0)) -> np.array:
    """
    :param nr_cols_rows: The dimentions of the maze
    :type: int
    :param starting_vertex: The position to start the maze from
    :type starting_vertex: Tuple
    :return: The random generated maze
    :rtype: Numpy.Array
    """

    maze = np.zeros((nr_cols_rows**2, nr_cols_rows**2),
                    dtype=np.int_)  # Create the maze
    starting_vertex = (0, 0)  # The position that the maze would start
    stack = []  # Defining a stack to store vertecies in it
    explored_vertices = set()  # A set to make sure not to explore a vertex more than once

    current_vertex = starting_vertex
    stack.append(current_vertex)
    while True:
        explored_vertices.add(current_vertex)

        curr_x, curr_y = current_vertex
        # Storing all the possible neighbors of the current vertex
        neighbors = [(curr_x, curr_y+1), (curr_x, curr_y-1),
                     (curr_x+1, curr_y), (curr_x-1, curr_y)]

        # Removing all the neighbors outside the maze
        neighbors = [(x, y) for (x, y) in neighbors if (0 <= x < nr_cols_rows) and (0 <= y < nr_cols_rows) and
                     ((x, y) not in explored_vertices)]
        if len(neighbors) != 0:
            # Choosing a random neighbor
            next_vertex = random.choice(neighbors)

            # Finding the index of the current and the next point
            curr_index, next_index = index_mapper(
                current_vertex, nr_cols_rows), index_mapper(next_vertex, nr_cols_rows)

            # Storing the path into the adjacency matrix
            maze[curr_index][next_index], maze[next_index][curr_index] = 1, 1

            # Preparing for the next iteration
            current_vertex = next_vertex
            # Storing the vertex into the stack to retrieve it later if needed
            stack.append(current_vertex)

        else:
            if len(stack) != 0:
                # Check for the last useable vertex to return to in the stack
                current_vertex = stack.pop()
            else:
                # The algorithm has finished and checked all the vertices
                break

    return maze

#maze_maker(300, 300)
