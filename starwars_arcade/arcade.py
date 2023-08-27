import pygame as pg
import random as rand
pg.init()

# make screen
screen = pg.display.set_mode((1920,1080))
clock = pg.time.Clock()

#make background

background = pg.image.load(r"C:\Users\zhang\Downloads\space.jpg")
# neko = pg.image.load(r"C:\Users\zhang\Downloads\Neko Para Vol. 4 Neko to Patissier no Noel\308_neko4_an26i.webp")
# scaled_background = pg.transform.scale(neko, (1920,1080))

#change title and icon
pg.display.set_caption("space invader")
icon = pg.image.load(r"C:\Users\zhang\Downloads\starwars.png")
pg.display.set_icon(icon)

#player
player_img = pg.image.load(r"C:\Users\zhang\Downloads\space-ship.png")
player_x = 960
player_y = 880
player_x_change = 0
player_y_change = 0
player_rect = pg.Rect(player_x,player_y,32,32)

#enemy
enemy_img = pg.image.load(r"C:\Users\zhang\Downloads\tie-fighter.png")
enemy_x = rand.randint(0,1855)
enemy_y = rand.randint(0,400)
enemy_x_change = rand.randint(1,2)
enemy_y_change = rand.randint(1,2)
enemy_rect = pg.Rect(enemy_x,enemy_y,32,32)

#laser
laser_img = pg.image.load(r"C:\Users\zhang\Downloads\laser.png")
laser_x = 0
laser_y = player_y +10 # fire from nose 
laser_x_change = 0
laser_y_change = 40
laser_rect = pg.Rect(laser_x,laser_y,32,32)
laser_ready = True

#score
score = 0
fontt = pg.font.Font('freesansbold.ttf',32)

#game_over_text
game_over_font = pg.font.Font('freesansbold.ttf',64)

def show_score():
    score_display = fontt.render("Score :" + str(score),True,(255,255,255))
    screen.blit(score_display, (10,10))


def player(player_x,player_y):
    screen.blit(player_img, (player_x,player_y))
    
def enemy(enemy_x,enemy_y):
    screen.blit(enemy_img, (enemy_x,enemy_y))

def fire_laser(laser_x,laser_y):
    global laser_ready
    laser_ready = False
    screen.blit(laser_img,(laser_x+16,laser_y+10))

def hit(rect1,rect2):
    return pg.Rect.colliderect(rect1,rect2)
    
def game_over_text():
    game_over = game_over_font.render("Game Over",True,(255,255,255))
    screen.blit(game_over, (960,540))
    


running = True
while running:
    #do something
        # fill the screen with a color to wipe away anything from last frame
    screen.fill("pink")
    screen.blit(background,(0,0))

    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        

        #if a key is pressed DOWN, check what it is
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_x_change = -10
            if event.key == pg.K_RIGHT:
                player_x_change = 10
            if event.key == pg.K_UP:
                player_y_change = -10
            if event.key == pg.K_DOWN:
                player_y_change = 10

            #fire
            if event.key == pg.K_SPACE:
                #only fire another if current leave screen
                if laser_ready:
                    laser_x = player_x
                    fire_laser(laser_x,laser_y)
            
        #if a key is pressed up, check what it is and stop movement
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player_x_change = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                player_y_change = 0

        
            
    

    # update where player is 
    player_x += player_x_change
    player_y += player_y_change
    # the space ship is 64x64 start from 0 left to right top to bottom, subtract by this number to keep ship in frame
    if player_x <= 0:
        player_x = 0
    elif player_x >=1856:
        player_x = 1856
    if player_y <= 0:
        player_y = 0
    elif player_y >=1016:
        player_y = 1016
    
    enemy_x += enemy_x_change
    enemy_y += enemy_y_change
    if enemy_x <= 0 or enemy_x >=1856:
        enemy_x_change = -enemy_x_change
    if enemy_y <= 0 or enemy_y >=1016:
        enemy_y_change = -enemy_y_change
    
    if laser_y <= 0 :
        laser_y = player_y +10
        laser_ready = True

    #keep laser on screen
    if not laser_ready:
        fire_laser(laser_x,laser_y)
        laser_y -= laser_y_change

    #determin collision
    laser_collision = hit(laser_rect,enemy_rect)
    player_collision = hit(player_rect,enemy_rect)
    #redetermine where the rect is
    player_rect = pg.Rect(player_x,player_y,32,32)
    enemy_rect = pg.Rect(enemy_x,enemy_y,32,32)
    laser_rect = pg.Rect(laser_x,laser_y,32,32)

    #when it is a hit, reset laser, reset laser_ready to true, relocate enemy
    if laser_collision:
        laser_y = player_y +10
        laser_ready = True
        score += 1
        #reset enemy when hit
        enemy_x = rand.randint(0,1855)
        enemy_y = rand.randint(0,400)
    # when enemy hit player, end game
    if player_collision:
        game_over_text()
        running = False




    #show the player on screen, must be after the screen, because screen is draw first
    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    show_score()

    

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.time.delay(1000)
pg.quit()