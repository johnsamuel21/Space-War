import pygame
import random
import math

#Start
pygame.init()
clock = pygame.time.Clock()


#variables
game_end = False
running = True

#Screen
screen = pygame.display.set_mode((800,600))
backgd = pygame.image.load("final1.png")


#Caption and icon
pygame.display.set_caption("Space war")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerx = 370
playery = 480
player_change = 0
def player(x,y):
    screen.blit(playerImg,(x,y))

#Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",30)
testX = 10
testY = 10


def show_score(x,y):
    score = font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    global backgd,testX,testY
    testX = 1000; testY = 1000
    over_font = pygame.font.Font("freesansbold.ttf",64)
    backgd = pygame.image.load("blackbg.png")
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
    show_score(testX, testY)
    fontscore = pygame.font.Font("freesansbold.ttf",50)
    finalscore = fontscore.render("Your Score: "+str(score_value),True,(255,255,255))
    screen.blit(finalscore,(240,320))
#Enemy
no_of_enemies = 6
enemyImg = []
enemy_x = []
enemy_y = []
enemyx_change = []
enemyy_change = []
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(20,100))
    enemyx_change.append(0.4)
    enemyy_change.append(40)
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

# Bullets
bulletImg = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bulletx_change = 0
bullety_change = 1.5
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))


# Collision check
def isCollision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x,2)+math.pow(enemy_y-bullet_y,2))
    if distance<27:
        return True
    return False


while running:

    #Screen color (RGB)
    #screen.fill((0,0,0))
    screen.blit(backgd,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Keystroke and commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change += -0.6
            if event.key == pygame.K_RIGHT:
                player_change += 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    fire_bullet(playerx,bullet_y)
                    bullet_x  = playerx
        if event.type == pygame.KEYUP:
            player_change = 0

    playerx+=player_change

    #Player boundary
    if playerx<=0:
        playerx = 0
    elif playerx>=736 and playerx<=10000:
        playerx = 736

    #Enemy movements
    for i in range(no_of_enemies):

        #game over
        if abs(enemy_x[i]-playerx)<=27 and enemy_y[i]>=417:
            for j in range(no_of_enemies):
                enemy_y[j] = 2000
            playerx = 30000
            game_end = True
            break
        enemy_x[i] += enemyx_change[i]
        if enemy_x[i] <= 0:
            enemyx_change[i] = -(enemyx_change[i])
            enemy_y[i] += enemyy_change[i]
        elif enemy_x[i] >=736:
            enemyx_change[i] = -(enemyx_change[i])
            enemy_y[i] += enemyy_change[i]
        #collision
        collision = isCollision(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0,735)
            enemy_y[i] = random.randint(20,100)
            enemyx_change[i]=abs(enemyx_change[i])+0.1
        enemy(enemy_x[i],enemy_y[i],i)

    if game_end:
        game_over_text()
    # Bullet movement
    if bullet_y<=0:
        bullet_state = "ready"
        bullet_y = 480

    if bullet_state == "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullety_change



    player(playerx,playery)
    show_score(testX,testY)
    pygame.display.update()
