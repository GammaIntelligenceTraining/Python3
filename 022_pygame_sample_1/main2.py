# pip install pygame
# https://www.pygame.org/docs/

import pygame

# Creating a window
WIDTH, HEIGHT = 900, 500
# Width and height are given as a Tuple
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting program title
pygame.display.set_caption("Let's learn Pygame")


# Window border (x, y, width, height)
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
# Variable to set FPS
FPS = 60
# Velocity
VEL = 5
BULLET_VEL = 7

# Adding an image to pygame
CAT_IMAGE = pygame.image.load('cat.png')
# Image resizing
CAT_IMAGE_WIDTH = 128
CAT_IMAGE_HEIGHT = 128
CAT = pygame.transform.scale(CAT_IMAGE, (CAT_IMAGE_WIDTH, CAT_IMAGE_HEIGHT))
# Image rotating
CAT = pygame.transform.rotate(CAT, 90)


def cat_square_movement(keys_pressed, cat_square):
    # If statement to give action for pressed key
    if keys_pressed[pygame.K_LEFT] and cat_square.x - VEL > 0:
        cat_square.x -= VEL

    if keys_pressed[pygame.K_RIGHT] and cat_square.x + VEL < WIDTH - CAT_IMAGE_WIDTH:
        cat_square.x += VEL

    if keys_pressed[pygame.K_UP] and cat_square.y - VEL > 0:
        cat_square.y -= VEL

    if keys_pressed[pygame.K_DOWN] and cat_square.y + VEL < HEIGHT - CAT_IMAGE_HEIGHT:
        cat_square.y += VEL


# Function to redraw window
def draw_window(CAT_SQUARE):
    # fill screen with one color passed as an RGB Tuple (255, 255, 255)
    # if fill will be applied after image, image will disappear
    WIN.fill((125, 125, 125))

    # Draw a rectangle(window, color(R,G,B),
    # pygame.draw.rect(WIN, (0, 0, 0), BORDER)

    # in order to load an image it needs to be drawn (x, y)
    # WIN.blit(CAT_IMAGE, (0, 0))
    WIN.blit(CAT, (CAT_SQUARE.x, CAT_SQUARE.y))
    # display must be update every while cycle
    pygame.display.update()


# Main function that is looped
def main():
    # Create an invisible square for a CAT_IMAGE
    CAT_SQUARE = pygame.Rect(0, 0, CAT_IMAGE_WIDTH, CAT_IMAGE_HEIGHT)
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

        # Pressed keys used to press multiple keys
        keys_pressed = pygame.key.get_pressed()
        cat_square_movement(keys_pressed, CAT_SQUARE)

        # CAT_SQUARE.x += 1
        draw_window(CAT_SQUARE)

    pygame.quit()


# Makes sure that program can only run when opened file, not imported
if __name__ == "__main__":
    main()