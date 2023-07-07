import turtle


def draw_maze_box(width: int = 400, height: int = 400, wall_width: int = 4, drawing_speed: int = 0) -> None:
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
draw_maze_box(400, 400)
