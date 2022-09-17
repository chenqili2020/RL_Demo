import pygame as pg

# Initalize the pygame
pg.init()

# window resolution
window = pg.display.set_mode((900, 550))

# window will close shortly, so we add event, such as quit or movement

running = True

# title and logo
pg.display.set_caption("Dodger")
icon = pg.image.load("bruh.png")
pg.display.set_icon(icon)

# add image, such as player

playerSprite = pg.image.load("nanachi.png")
rect = playerSprite.get_rect()

size = playerSprite.get_size()
print(size)
# rect[0] = rect[0]/4
# rect[1] = rect[1]/4
# change the sprite
# playerSprite = pg.transform.scale(playerSprite, (175, 175))
playerX = 350
playerY = 120


def player(x, y):
    # blit is draw on the window
    window.blit(playerSprite, (x, y))


playerX_Change = 0
playerY_Change = 0

while running:

    # RGB
    window.fill((100, 100, 100))
    for event in pg.event.get():
        # quit the window the pressing "叉"
        if event.type == pg.QUIT:
            running = False

        # check keyboard
        if event.type == pg.KEYDOWN:
            print("-key down-")
            if event.key == pg.K_LEFT:
                print("L down")
                playerX_Change = -0.2
            if event.key == pg.K_RIGHT:
                print("R down")
                playerX_Change = 0.2
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                print("key up")
                playerX_Change = 0.0

    playerX += playerX_Change

    # 会一直出现的东西最好在这

    if playerX <= 0:
        playerX = 0
    if playerX >= 900 - size[0]:
        playerX = 900 - size[0]

    # add player
    player(playerX, playerY)

    # draw box around image
    pg.draw.rect(playerSprite, (255, 255, 255), rect, 1)

    # add to update or not working
    pg.display.update()
