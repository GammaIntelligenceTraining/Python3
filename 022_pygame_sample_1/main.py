# pip install pygame
# https://www.pygame.org/docs/

import pygame

# Creating a window
WIDTH, HEIGHT = 900, 500
# Width and height are given as a Tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting program title
pygame.display.set_caption("Let's learn Pygame")

# Variable to set FPS
FPS = 60

# Adding an image to pygame
CAT_IMAGE = pygame.image.load('cat.png')
# Image resizing
CAT = pygame.transform.scale(CAT_IMAGE, (128, 128))
# Image rotating
CAT = pygame.transform.rotate(CAT, 90)


# Function to redraw window
def draw_window():
    # fill screen with one color passed as an RGB Tuple (255, 255, 255)
    # if fill will be applied after image, image will disappear
    WIN.fill((125, 125, 125))
    # in order to load an image it needs to be drawn (x, y)
    # WIN.blit(CAT_IMAGE, (0, 0))
    WIN.blit(CAT, (0, 0))
    # Draw a rectangle
    pygame.draw.rect(WIN, (0, 100, 0), (700, 300, 128, 128))
    # display must be update every while cycle
    pygame.display.update()


# Main function that is looped
def main():
    # Creates a Clock() object to control FPS
    clock = pygame.time.Clock()
    # In order to redraw main window a while loop is used
    condition = True
    while condition:
        # run Clock()
        clock.tick(FPS)
        # for loop for pygame events is used to check if event occurred
        for event in pygame.event.get():
            # Check if user quit the window
            if event.type == pygame.QUIT:
                condition = False
        draw_window()

    pygame.quit()


# Makes sure that program can only run when opened file, not imported
if __name__ == "__main__":
    main()