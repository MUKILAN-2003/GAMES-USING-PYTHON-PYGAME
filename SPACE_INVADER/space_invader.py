############################# DEVELOPED BY: S.MUKILAN ##########################

import pygame as pg
import random
import time
import os
import class_space_invader as invade
import pickle
pg.init()

screen_width = 550
screen_height = 450
win = pg.display.set_mode((screen_width,screen_height),pg.HWSURFACE | pg.DOUBLEBUF)
pg.display.set_caption("SPACE_INVADER")
bg = pg.image.load('images/bg_space.jpg')
bg_intro = pg.image.load('images/main_pg.jpg')
alien1 = pg.image.load("images/alien1.png")
alien2 = pg.image.load("images/alien2.png")
ast1 = pg.image.load("images/asteriod.png")
ast2 = pg.image.load("images/asteriod1.png")
battle_enem = pg.image.load("images/enem_ship.png")
gunfire = pg.mixer.Sound("sounds/gun fire.wav")
boom = pg.mixer.Sound("sounds/boom.wav")
bg_m = pg.mixer.music.load("sounds/space_bg.wav")
clock = pg.time.Clock()
font = pg.font.SysFont('comicsan',16)
scr_font = pg.font.SysFont('comicsan',25)
main_fnt = pg.font.SysFont('comicsan',35)
pg.mixer.music.play(-1)

game = False
intro = True
restart = False
shipx = 265
shipy = 370
score = 0
bullets = []
ship_xmove = 0
enemy1 = invade.Enemyship(alien1)
enemy2 = invade.Enemyship(alien2)
enemy3 = invade.Enemyship(alien1)
enemy4 = invade.Enemyship(alien2)
enemy5 = invade.Enemyship(alien2)
enemy6 = invade.Enemyship(battle_enem)
asteriod1 = invade.Enemyship(ast1)
asteriod2 = invade.Enemyship(ast2)
enemy_num = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,asteriod1,asteriod2]

def scr_and_earth():
    global score
    score = score -(enemy1.scr + enemy2.scr+enemy3.scr+enemy4.scr+enemy5.scr)
    for i in enemy_num:
        i.scr = 0
    ear_life = font.render(("EARTH LIFE"),5,(0,255,0))
    scr = scr_font.render(("SCORE: " + str(score)),5,(255,0,0))
    win.blit(scr,(10,15))
    win.blit(ear_life,(410,10))
    
def scr_enemy_check_diff():
    enemy1.draw(win)
    if score > 20:
        enemy2.draw(win)
    if score > 60:    
        enemy3.draw(win)
        asteriod1.draw(win)
        asteriod1.enemyship_vel = 1
    if score > 120:    
        enemy4.draw(win)
        asteriod2.draw(win)
        asteriod2.enemyship_vel = 1
    if score > 280:    
        enemy5.draw(win)
    if score > 380:
        enemy6.draw(win)
    if score > 750:
        enemy1.enemyship_vel = 3
        enemy4.enemyship_vel = 3
    if score > 1200:
        enemy2.enemyship_vel = 4
        enemy6.enemyship_vel = 5
        asteriod2.enemyship_vel = 2
    
def draw_game_window():
    global game,enemy_num,restart,score
    earth_live = (enemy1.earth_life + enemy2.earth_life + enemy3.earth_life + enemy4.earth_life + enemy5.earth_life + asteriod1.earth_life + asteriod2.earth_life)/7
    pg.draw.rect(win,(255,0,0),(410,20,100,5))
    pg.draw.rect(win,(0,255,0),(410,20,(earth_live),5))
    battleship = invade.Battleship(shipx,shipy)
    battleship.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    if earth_live <= 0:
        defect = main_fnt.render(("EARTH DESTROYED YOU LOSS"),5,(255,0,0))
        win.blit(defect,(95,225))
        boom.play()
        restart = True
        
    if score >= 3000:    
        won = main_fnt.render(("EARTH PROTECTED YOU WON"),5,(0,255,0))
        win.blit(won,(95,225))
        boom.play()
        restart = True    
    bullet_check()    
    scr_enemy_check_diff()    
    scr_and_earth()
    pg.display.update()

def bullet_check():
    global score
    for bullet in bullets:
        for i in enemy_num:
            if (bullet.bulletx > i.enemyship_x) and (bullet.bulletx < i.enemyship_x+50):
                if(bullet.bullety < i.enemyship_y + 40):
                    i.enemyship_x = random.randint(0,480)
                    i.enemyship_y = -50
                    bullets.pop(bullets.index(bullet))
                    score += 10
                    break
                
while intro:
    win.blit(bg_intro,(0,0))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game = True
                intro = False

    while game:
        clock.tick(30)
        win.blit(bg,(0,0))
        pg.display.update()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            ship_xmove = -10
        elif keys[pg.K_RIGHT]:
            ship_xmove = 10
            
        for event in pg.event.get():            
            if event.type == pg.QUIT:
                game = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    gunfire.play()
                    bullets.append(invade.Shipfire(shipx+25,bullets))
                        
        shipx += ship_xmove
        ship_xmove = 0
        if shipx < -2:
            shipx = 0
        if shipx > 500:
            shipx = 498
        draw_game_window()

        while restart: 
            reset = scr_font.render(("HIT SPACE TO RESET"),5,(255,242,0))
            win.blit(reset,(185,300))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    restart = False
                    game = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        for i in enemy_num:
                            i.earth_life = 100
                            i.enemyship_vel = 2
                        enemy1.enemyship_y = -50    
                        score = 0    
                        restart = False

pg.quit()
############################# SPACE INVADER ##########################
