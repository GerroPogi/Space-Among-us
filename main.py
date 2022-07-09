import pygame as py
import random as r
import math as m
from pygame import mixer

# initialize every module
py.init()
mainmenu = True
playgame = False
logoy = -300
logoanimation = True
# the window
width = 800
height = 600
window = py.display.set_mode((width, height))
Mabook = py.sysfont.SysFont("Mabook.tff", 32)

# player
playerImg = py.image.load("player.png")
playerX = width * 0.43
playerY = height * 0.7
Yspeed = 0
Xspeed = 0

# Score
score = 0
sfont = py.font.Font("mabook.ttf", 32)
fontX = 10
fontY = 10

# game over

gfont = py.font.Font("mabook.ttf", 70)
gameover = False
clicked = False


def over():
    global clicked
    gameover = True
    if gameover:
        # Game over
        py.draw.rect(window, (0, 0, 0), py.Rect(190, 190, 350, 70))
        gover = gfont.render("Game Over :(", True, (255, 255, 255))
        window.blit(gover, (200, 200))
        # Retry
        replaybtn = py.draw.rect(window, (0, 0, 0), py.Rect(90, 290, 135, 39))
        playagain = sfont.render("Play Again?", True, (255, 255, 255))
        window.blit(playagain, (100, 300))
        if py.Rect.collidepoint(replaybtn, float(posX), float(posY)):
            if py.mouse.get_pressed()[0] == 1 and clicked == False:
                eposition()
                clicked = True
            if py.mouse.get_pressed()[0] == 0:
                clicked = False


def sscore(x, y):
    stext = sfont.render(f"Score: {str(score)}", True, (255, 255, 255))
    window.blit(stext, (x, y))


def player(x, y):
    window.blit(py.transform.scale(playerImg, (100, 100)), (x, y))


# enemy
Xespeed = []
enemyImg = []
enemyX = []
enemyY = []
enemies = 12
for i in range(enemies):
    enemyImg.append(py.image.load("amongus.png"))
    enemyX.append(r.randrange(20, 680, 50))
    enemyY.append(r.randrange(20, 300, 50))
    Xespeed.append(0.6)


def enemy(x, y, i):
    window.blit(py.transform.scale(enemyImg[i], (70, 70)), (x, y))


def eposition():
    global playerX, playerY, enemyX, enemyY
    enemyX = []
    enemyY = []
    for i in range(enemies):
        enemyX.append(r.randrange(20, 680, 50))
        enemyY.append(r.randrange(20, 300, 50))
    playerX = width * 0.43
    playerY = height * 0.7


# Bullet
Ybspeed = 3
bullet = py.image.load("bulleto.png")
bulletY = playerY
bulletX = playerX
bulletstate = True


def fire(x, y):
    global bulletstate
    bulletstate = False
    window.blit(py.transform.scale(bullet, (40, 40)), (x + 16, y + 10))


# background
bg = py.image.load("guarara.png")
mixer.music.load("bg.mp3")
mixer.music.play(-1)

# title and icon
py.display.set_caption("Space AMONGUS")
icon = py.image.load("flushed.png")
py.display.set_icon(icon)

# Collision
def collision(ex, ey, bx, by):
    distance = m.sqrt((m.pow(ex - bx, 2)) + (m.pow(ey - by, 2)))
    if distance < 50:
        return True
    else:
        return False


# Main Menu
logo = py.image.load("logo.png")
gamefont = py.font.Font("mabook.ttf", 70)
clock = py.time.Clock()
# game loop
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if not gameover:
                if event.key == py.K_w:
                    Yspeed -= 2
                if event.key == py.K_s:
                    Yspeed += 2
                if event.key == py.K_a:
                    Xspeed -= 2
                if event.key == py.K_d:
                    Xspeed += 2
                if event.key == py.K_w and event.key == py.K_a:
                    Xspeed -= 1
                    Yspeed -= 1
                if event.key == py.K_w and event.key == py.K_d:
                    Xspeed += 1
                    Yspeed -= 1
                if event.key == py.K_s and event.key == py.K_a:
                    Xspeed -= 1
                    Yspeed += 1
                if event.key == py.K_s and event.key == py.K_d:
                    Xspeed += 1
                    Yspeed += 1
                if event.key == py.K_ESCAPE:
                    for j in range(enemies):
                        enemyY[j] = 2000
                    over()
                    break
                if event.key == py.K_SPACE:
                    if bulletstate:
                        bulletsound = mixer.Sound("bullet.mp3")
                        bulletsound.play()
                        bulletX = playerX
                        fire(bulletX, bulletY)
        elif event.type == py.KEYUP:
            if not gameover:
                Yspeed = 0
                Xspeed = 0

    posX, posY = py.mouse.get_pos()

    if mainmenu:
        window.fill((10, 20, 40))
        playtext = gamefont.render("Play", True, (255, 255, 255))
        playbtn = py.Rect(100, 400, 150, 70)
        if py.Rect.collidepoint(playbtn, posX, posY):
            if py.mouse.get_pressed()[0] == 1 and clicked:
                playgame = True
                mainmenu = False
                clicked = False
            if py.mouse.get_pressed()[0] == 0:
                clicked = True
        window.blit(playtext, (100, 400))
        # Logo animation
        while logoanimation:
            window.fill((10, 20, 40))
            logoy += 1
            window.blit(py.transform.scale(logo, (1280 * 0.5, 720 * 0.5)), (100, logoy))
            if logoy >= 50:
                logoy = 50
                logoanimation = False
            playtext = gamefont.render("Play", True, (255, 255, 255))
            window.blit(playtext, (100, 400))
            playbtn = py.Rect(100, 400, 150, 70)
            window.blit(playtext, (100, 400))
            py.display.update()
        if not logoanimation:
            window.blit(py.transform.scale(logo, (1280 * 0.5, 720 * 0.5)), (100, logoy))

    elif playgame:
        # BG
        window.fill((10, 50, 205))
        window.blit(py.transform.scale(bg, (800, 600)), (0, 0))

        # player movement

        playerY += Yspeed
        playerX += Xspeed

        # Stopping at boarder
        # Player
        if playerX < 0:
            playerX = 0
        elif playerX > 700:
            playerX = 700
        elif playerY < 0:
            playerY = 0
        elif playerY > 500:
            playerY = 500

        # Enemy
        for i in range(enemies):
            # game over
            if enemyY[i] > 400:
                for j in range(enemies):
                    enemyY[j] = 2000
                over()
                break

            if enemyX[i] < 0:
                Xespeed[i] = 0.6
                enemyY[i] += 50
            elif enemyX[i] > 750:
                Xespeed[i] = -0.6
                enemyY[i] += 50
            enemyX[i] += Xespeed[i]
            if collision(enemyX[i], enemyY[i], bulletX, bulletY):
                bodysound = mixer.Sound("bodyhit.mp3")
                bodysound.play()
                bulletY = 480
                bulletstate = True
                enemyX[i] = r.randrange(20, 680, 50)
                enemyY[i] = r.randrange(20, 300, 50)
                score += 1
            enemy(enemyX[i], enemyY[i], i)
        # bullet movement
        if bulletY < 0:
            bulletstate = True
            bulletY = playerY
        if not bulletstate:
            fire(bulletX, bulletY)
            bulletY -= Ybspeed

        # line
        py.draw.rect(window, (255, 0, 0), py.Rect(0, 440, 800, 20))

        # if gameover:

        sscore(fontX, fontY)
        player(
            playerX,
            playerY,
        )
    else:
        running = False

    py.display.update()
    clock.tick(100)
