import pygame

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's learn Python")

BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)

FPS = 60
VEL = 5
CHANGE = True
CHANGE2 = True


CAT_IMAGE_WIDTH = 128
CAT_IMAGE_HEIGHT = 128

CAT_IMAGE = pygame.image.load('cat.png')
CAT = pygame.transform.scale(CAT_IMAGE, (CAT_IMAGE_HEIGHT, CAT_IMAGE_HEIGHT))
# CAT = pygame.transform.rotate(CAT, -90)
CAT.set_alpha(15)


def cat_movement(cat_square):
    global CHANGE
    global CHANGE2
    if cat_square.x >= 0 and cat_square.x + VEL < WIDTH - CAT_IMAGE_WIDTH and CHANGE == True:
        cat_square.x += VEL
    else:
        CHANGE = False
    if cat_square.x - VEL > 0 and CHANGE == False:
        cat_square.x -= VEL
    else:
        CHANGE = True
    if cat_square.y >= 0 and cat_square.y + VEL < HEIGHT - CAT_IMAGE_HEIGHT and CHANGE2 == True:
        cat_square.y += VEL
    else:
        CHANGE2 = False
    if cat_square.y - VEL > 0 and CHANGE2 == False:
        cat_square.y -= VEL
    else:
        CHANGE2 = True


def draw_window(cat_square):
    WIN.fill((125, 125, 125))
    WIN.blit(CAT, (cat_square.x, cat_square.y))
    # pygame.draw.rect(WIN, (125, 0, 0), (0, 0, 100, 100))
    # pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    pygame.display.update()


def main():
    cat_square = pygame.Rect(0, 0, CAT_IMAGE_WIDTH, CAT_IMAGE_HEIGHT)
    clock = pygame.time.Clock()
    condition = True
    while condition:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                condition = False
        # keys_pressed = pygame.key.get_pressed()
        cat_movement(cat_square)
        change = True
        draw_window(cat_square)
    pygame.quit()


if __name__ == "__main__":
    main()