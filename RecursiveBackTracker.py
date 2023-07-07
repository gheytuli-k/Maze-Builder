import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the size of the maze cells
cell_size = 20

def draw_maze():
    # Define the maze structure
    maze = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    
    # Draw the maze
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, WHITE, (j * cell_size, i * cell_size, cell_size, cell_size))
    
    # Update the display
    pygame.display.update()

# Call the draw_maze function
draw_maze()

# Keep the window open until it's closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
