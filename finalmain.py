import pygame
import random
import math
import sys
from pygame import mixer

#start
pygame.init()
choose_player = "sourcefile/player.png"

#Welcome msg
def welcomemsg():
    loc = "sourcefile/pixelfont.ttf"
    font = pygame.font.Font(loc,30)
    intro = font.render("WELCOME TO SPACE WAR ",True,(100,255,255))
    screen.blit(intro,(140,90))

#Menu tab
def main_menu():
    global choose_player
    click = False
    menurun = True
    backg = pygame.image.load("sourcefile/mainmenu.png")


    while menurun:
        screen.blit(backg,(0,0))

        #Mouse and buttons
        mx,my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(110,500,180,50)
        button_2 = pygame.Rect(510,500,180,50)

        #menu screen options
        loc = "sourcefile/pixelfont.ttf"
        font = pygame.font.Font(loc,20)
        play = font.render("PLAY",True,(100,255,255))
        option = font.render("OPTION",True,(100,255,255))

        if button_1.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_1,border_radius=20)
            play = font.render("PLAY",True,(0,0,0))
            if click:
                default()
                main()

        if button_2.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_2,border_radius=20)
            option = font.render("OPTION",True,(0,0,0))
            if click:
                options_tab()
                main()
        pygame.draw.rect(screen,(255,255,255),button_1,5,20)
        pygame.draw.rect(screen,(255,255,255),button_2,5,20)

        screen.blit(play,(164,514))
        screen.blit(option,(550,514))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menurun = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        welcomemsg()
        pygame.display.update()

#Options tab
def options_tab():
    global choose_player
    click = False
    option_run = True
    back_space = False
    backg = pygame.image.load("sourcefile/final.png")
    while option_run:
        screen.blit(backg,(0,0))

        loc = "sourcefile/pixelfont.ttf"
        font = pygame.font.Font(loc,30)
        intro = font.render("CHOOSE YOUR BATTLE SPACE-SHIP",True,(100,255,255))
        screen.blit(intro,(30,25))

        mx,my = pygame.mouse.get_pos()
        loc = "sourcefile/pixelfont.ttf"
        font = pygame.font.Font(loc,20)
        back_key = font.render("BACK",True,(100,255,255))
        button_1 = pygame.Rect(83,100,100,100)
        button_2 = pygame.Rect(349,100,100,100)
        button_3 = pygame.Rect(615,100,100,100)
        button_4 = pygame.Rect(83,300,100,100)
        button_5 = pygame.Rect(349,300,100,100)
        button_6 = pygame.Rect(615,300,100,100)
        button_7 = pygame.Rect(310,500,180,50)

        #menu screen options
        if button_1.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_1,border_radius=10)
            if click:
                choose_player = "sourcefile/player.png"
                break

        if button_2.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_2,border_radius=10)
            if click:
                choose_player = "sourcefile/spaceship1.png"
                break
        if button_3.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_3,border_radius=10)
            if click:
                choose_player = "sourcefile/spaceship2.png"
                break
        if button_4.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_4,border_radius=10)
            if click:
                choose_player = "sourcefile/spaceship3.png"
                break

        if button_5.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_5,border_radius=10)
            if click:
                choose_player = "sourcefile/spaceship4.png"
                break
        if button_6.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_6,border_radius=10)
            if click:
                choose_player = "sourcefile/spaceship5.png"
                break
        if button_7.collidepoint((mx,my)):
            pygame.draw.rect(screen,(255,255,255),button_7,border_radius=20)
            back_key = font.render("BACK",True,(0,0,0))
            if click:
                main_menu()
        pygame.draw.rect(screen,(255,255,255),button_1,2,10)
        pygame.draw.rect(screen,(255,255,255),button_2,2,10)
        pygame.draw.rect(screen,(255,255,255),button_3,2,10)
        pygame.draw.rect(screen,(255,255,255),button_4,2,10)
        pygame.draw.rect(screen,(255,255,255),button_5,2,10)
        pygame.draw.rect(screen,(255,255,255),button_6,2,10)
        pygame.draw.rect(screen,(255,255,255),button_7,5,20)
        screen.blit(back_key,(364,514))

        choice1 = pygame.image.load("sourcefile/player.png")
        screen.blit(choice1,(100,116))
        choice1 = pygame.image.load("sourcefile/spaceship1.png")
        screen.blit(choice1,(366,116))
        choice1 = pygame.image.load("sourcefile/spaceship2.png")
        screen.blit(choice1,(632,116))
        choice1 = pygame.image.load("sourcefile/spaceship3.png")
        screen.blit(choice1,(100,316))
        choice1 = pygame.image.load("sourcefile/spaceship4.png")
        screen.blit(choice1,(366,316))
        choice1 = pygame.image.load("sourcefile/spaceship5.png")
        screen.blit(choice1,(632,316))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menurun = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_BACKSPACE:
                    back_space = True
                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if back_space:
            break

        pygame.display.update()
    main_menu()





#variables
game_end = False

#Screen
screen = pygame.display.set_mode((800,600))

#Caption
pygame.display.set_caption("Space war")
icon = pygame.image.load("sourcefile/ufo.png")
pygame.display.set_icon(icon)

#Player location
def player(x,y):
    global choose_player
    playerImg = pygame.image.load(choose_player)
    screen.blit(playerImg,(x,y))

#Enemy
def enemy(x,y,i,enemyImg):
    screen.blit(enemyImg[i],(x,y))

#default locations
def default():
    global no_of_enemies, enemyImg,enemy_x,enemy_y,enemyx_change,enemyy_change
    global playerX,playerY,player_change
    playerX = 370
    playerY = 480
    player_change = 0
    no_of_enemies = 6
    enemyImg = []
    enemy_x = []
    enemy_y = []
    enemyx_change = []
    enemyy_change = []
    for i in range(no_of_enemies):
        enemyImg.append(pygame.image.load("sourcefile/alien.png"))
        enemy_x.append(random.randint(0,735))
        enemy_y.append(random.randint(20,100))
        enemyx_change.append(0.4)
        enemyy_change.append(40)


#Scores
score_value = 0
font = pygame.font.Font("freesansbold.ttf",30)
testX = 10
testY = 10

def show_score(x,y):
    score = font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


#Bullet details
bullet_x = 0
bullet_y = 480
bulletx_change = 0
bullety_change = 1.5
bullet_state = "ready"
def fire_bullet(x,y):
    global bullet_state
    bulletImg = pygame.image.load("sourcefile/bullet.png")
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

#Collision condition
def isCollision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x,2)+math.pow(enemy_y-bullet_y,2))
    if distance<27:
        return True
    return False

#Pause control
def gamePause():
    game = True
    largeText = pygame.font.SysFont("comicsansms",115)
    pause_text = largeText.render("Game Paused",True, (255,255,255))
    screen.blit(pause_text,(125,257))
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    main()


        #button("Continue",150,450,100,50,green,bright_green,unpause)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()

#Game over details
def game_over_text():
    click = False
    global testX,testY,game_end,score_value,playerX,playerY
    testX = 1000; testY = 1000
    over_font = pygame.font.Font("freesansbold.ttf",64)
    screen.fill((0,0,0))
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
    show_score(1000, 1000)
    fontscore = pygame.font.Font("freesansbold.ttf",50)
    finalscore = fontscore.render("Your Score: "+str(score_value),True,(255,255,255))
    screen.blit(finalscore,(240,320))

    mx,my = pygame.mouse.get_pos()
    loc = "sourcefile/pixelfont.ttf"
    font = pygame.font.Font(loc,20)
    pg_again = font.render("PLAY AGAIN",True,(100,255,255))
    main_back = font.render("MAIN MENU",True,(100,255,255))
    button_pg = pygame.Rect(100,500,200,50)
    button_mb = pygame.Rect(500,500,200,50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    if button_pg.collidepoint((mx,my)):
        pygame.draw.rect(screen,(255,255,255),button_pg,border_radius=20)
        pg_again = font.render("PLAY AGAIN",True,(0,0,0))
        if click:
            testX = 10
            testY = 10
            game_end = False
            score_value = 0
            playerX = 370
            playerY = 480
            default()
            main()
            return
    if button_mb.collidepoint((mx,my)):
        pygame.draw.rect(screen,(255,255,255),button_mb,border_radius=20)
        main_back = font.render("MAIN MENU",True,(0,0,0))
        if click:
            testX = 10
            testY = 10
            game_end = False
            score_value = 0
            main_menu()
    pygame.draw.rect(screen,(255,255,255),button_pg,5,20)
    screen.blit(pg_again,(116,514))
    pygame.draw.rect(screen,(255,255,255),button_mb,5,20)
    screen.blit(main_back,(529,514))

#Player initial location
playerX = 370
playerY = 480
player_change = 0

#Enemy details
no_of_enemies = 6
enemyImg = []
enemy_x = []
enemy_y = []
enemyx_change = []
enemyy_change = []
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("sourcefile/alien.png"))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(20,100))
    enemyx_change.append(0.4)
    enemyy_change.append(40)

#Main function
def main():
    clock = pygame.time.Clock()
    mixer.music.load("sourcefile/background.wav")
    mixer.music.play(-1)
    global running,bullet_state,bullet_x,bullet_y
    global bulletx_change,bullety_change,score_value,game_end
    global testX,testY
    global playerX,playerY,player_change
    global no_of_enemies, enemyImg,enemy_x,enemy_y,enemyx_change,enemyy_change
    screen.fill((0,0,0))
    backgd = pygame.image.load("sourcefile/final1.png")
    back_space = False

    while True:
        clock.tick(1000)

        screen.blit(backgd,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Keystroke and commands
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_change += -0.6
                if event.key == pygame.K_RIGHT:
                    player_change += 0.6
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("sourcefile/laserfire.wav")
                        bullet_sound.play()
                        bullet_x = playerX
                        fire_bullet(playerX,bullet_y)
                if event.key == pygame.K_BACKSPACE:
                    back_space = True
                    default()
                    break
                if event.key == pygame.K_RSHIFT:
                    gamePause()
            if event.type == pygame.KEYUP:
                player_change = 0
        if back_space:
            break

        #Player movements
        playerX+=player_change
        if playerX<=0:
            playerX = 0
        elif playerX>=736 and playerX<=10000:
            playerX = 736

        #Enemy movements
        for i in range(no_of_enemies):
            #game over
            if abs(enemy_x[i]-playerX)<=27 and enemy_y[i]>=418:
                for j in range(no_of_enemies):
                    enemy_y[j] = 2000
                playerX = 30000
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
                collision_sound = mixer.Sound("sourcefile/blast.wav")
                collision_sound.play()
                bullet_y = 480
                bullet_state = "ready"
                score_value += 1
                enemy_x[i] = random.randint(0,735)
                enemy_y[i] = random.randint(20,100)
                enemyx_change[i]=abs(enemyx_change[i])+0.1
            enemy(enemy_x[i],enemy_y[i],i,enemyImg)


        if game_end:
            game_over_text()

        #Bullet movements
        if bullet_y<=0:
            bullet_state = "ready"
            bullet_y = 480
        if bullet_state == "fire":
            fire_bullet(bullet_x,bullet_y)
            bullet_y -= bullety_change

        player(playerX,playerY)
        show_score(testX,testY)
        pygame.display.update()
    if back_space:
        game_end = False
        score_value = 0
        testX = 10
        testY = 10
        main_menu()
mixer.music.load("sourcefile/background.wav")
mixer.music.play(-1)

#Starting function
main_menu()
