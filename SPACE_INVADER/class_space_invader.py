import pygame as pg
import random
pg.init()
boom = pg.mixer.Sound("sounds/boom.wav")

class Battleship(object):
    ship = pg.image.load('images/battleship.png')
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,win):
        win.blit(self.ship,(self.x, self.y))
        pg.display.update()
    
class Shipfire(object):
    bullet_img = pg.image.load("images/bullet.png")
    def __init__(self,x,bullets):
        self.bulletx = x
        self.bullety = 380
        self.bullets = bullets
        self.bullet_vel = -3
    def draw(self,win):
        win.blit(self.bullet_img,(self.bulletx,self.bullety))
        pg.display.update()
    
        for bullet in self.bullets:
            if len(self.bullets) >= 6:
                self.bullets.pop(self.bullets.index(bullet))
            if self.bullety > -20:
                self.bullety += self.bullet_vel
                
class Enemyship(object):
    def __init__(self,img):
        self.enemyship_x = random.randint(0,480)
        self.enemyship_y = -50
        self.enemyship_vel = 2
        self.earth_life = 100
        self.scr = 0
        self.img = img
    def draw(self,win):
        win.blit(self.img,(self.enemyship_x,self.enemyship_y))
        self.enemyship_y += self.enemyship_vel
        pg.display.update()

        if self.enemyship_y > 450:
            boom.play()
            self.enemyship_x = random.randint(0,480)
            self.enemyship_y = -50
            self.earth_life -= 50
            self.scr = 10

  
