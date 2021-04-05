import pygame

pygame.init()

window = pygame.display.set_mode((852, 480))

pygame.display.set_caption('The HIVE game')

walkLeft = [pygame.image.load('images\\L1.png'), pygame.image.load('images\\L2.png'), pygame.image.load('images\\L3.png'),
            pygame.image.load('images\\L4.png'), pygame.image.load('images\\L5.png'), pygame.image.load('images\\L6.png'),
            pygame.image.load('images\\L7.png'), pygame.image.load('images\\L8.png'), pygame.image.load('images\\L9.png')]
walkRight = [pygame.image.load('images\\R1.png'), pygame.image.load('images\\R2.png'), pygame.image.load('images\\R3.png'),
            pygame.image.load('images\\R4.png'), pygame.image.load('images\\R5.png'), pygame.image.load('images\\R6.png'),
            pygame.image.load('images\\R7.png'), pygame.image.load('images\\R8.png'), pygame.image.load('images\\R9.png')]
bg = pygame.image.load('images\\bg.jpg')
char = pygame.image.load('images\\standing.png')

clock = pygame.time.Clock()

fireballSound = pygame.mixer.Sound('images\\bullet.mp3')
hitSound = pygame.mixer.Sound('images\\hit.mp3')
bgMusic = pygame.mixer.music.load('images\\music.mp3')

pygame.mixer.music.play(-1)

score = 0


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)  # hitbox rectangle

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        window.blit(text, ((screenWidth / 2) - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class Fireball(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

class Enemy(object):
    walkRight = [pygame.image.load('images\\R1E.png'), pygame.image.load('images\\R2E.png'), pygame.image.load('images\\R3E.png'),
                 pygame.image.load('images\\R4E.png'), pygame.image.load('images\\R5E.png'), pygame.image.load('images\\R6E.png'),
                 pygame.image.load('images\\R7E.png'), pygame.image.load('images\\R8E.png'), pygame.image.load('images\\R9E.png'),
                 pygame.image.load('images\\R10E.png'), pygame.image.load('images\\R11E.png'), ]

    walkLeft = [pygame.image.load('images\\L1E.png'), pygame.image.load('images\\L2E.png'), pygame.image.load('images\\L3E.png'),
                 pygame.image.load('images\\L4E.png'), pygame.image.load('images\\L5E.png'), pygame.image.load('images\\L6E.png'),
                 pygame.image.load('images\\L7E.png'), pygame.image.load('images\\L8E.png'), pygame.image.load('images\\L9E.png'),
                 pygame.image.load('images\\L10E.png'), pygame.image.load('images\\L11E.png'), ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 9
        self.visible = True

    def draw(self, window):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)  # hitbox rectangle

            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (4.75 * (9 - self.health)), 10))

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

screenWidth = 852
screenHeight = 480



def redrawGameWindow():
    # global walkCount
    window.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (255, 0, 0))
    window.blit(text, (390, 10))
    warrior.draw(window)
    goblin.draw(window)
    for fireball in fireballs:
        fireball.draw(window)
    pygame.display.update()

isJump = False
jumpCount = 10

warrior = Player(300, 410, 64, 64)
castLoop = 0
goblin = Enemy(100, 410, 65, 65, 450)
fireballs = []
font = pygame.font.SysFont('comicsans', 30, True, True)


# main window loop
run = True
while run:
    clock.tick(27)
    if goblin.visible == True:
        if warrior.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and warrior.hitbox[1] + warrior.hitbox[3] > goblin.hitbox[1]:
            if warrior.hitbox[0] + warrior.hitbox[2] > goblin.hitbox[0] and warrior.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                warrior.hit()
                score -= 5

    if castLoop > 0:
        castLoop += 1
    if castLoop > 9:
        castLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for fireball in fireballs:
        if goblin.visible == True:
            if fireball.y - fireball.radius < goblin.hitbox[1] + goblin.hitbox[3] and fireball.y + fireball.radius > goblin.hitbox[1]:
                if fireball.x + fireball.radius > goblin.hitbox[0] and fireball.x - fireball.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    hitSound.play()
                    goblin.hit()
                    score += 1
                    fireballs.pop(fireballs.index(fireball))

        if 0 < fireball.x < screenWidth:
            fireball.x += fireball.vel

        else:
            fireballs.pop(fireballs.index(fireball))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and castLoop == 0:
        fireballSound.play()
        if warrior.left:
            facing = -1
        else:
            facing = 1
        if len(fireballs) < 5:
            fireballs.append(Fireball(round(warrior.x + warrior.width // 2), round(warrior.y + warrior.height // 2), 12, (255, 0, 0), facing))
        castLoop = 1
    if keys[pygame.K_LEFT] and warrior.x > warrior.vel:
        warrior.x -= warrior.vel
        warrior.left = True
        warrior.right = False
        warrior.standing = False

    elif keys[pygame.K_RIGHT] and warrior.x < screenWidth - warrior.width - warrior.vel:
        warrior.x += warrior.vel
        warrior.right = True
        warrior.left = False
        warrior.standing = False

    else:
        warrior.standing = True
        warrior.walkCount = 0

    if not warrior.isJump:
        if keys[pygame.K_UP]:
            warrior.isJump = True
            warrior.left = False
            warrior.right = False
            warrior.walkCount = 0
    else:
        if warrior.jumpCount >= -10:
            neg = 1
            if warrior.jumpCount < 0:
                neg = -1
            warrior.y -= (warrior.jumpCount ** 2) * 0.5 * neg

            warrior.jumpCount -= 1
        else:
            warrior.isJump = False
            warrior.jumpCount = 10
    redrawGameWindow()
pygame.quit()