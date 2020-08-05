 #####################!! PROGRAMMER : S.MUKILAN !!############################

#--------------------------------  FLAPPY BIRD --------------------------------#

import pygame       #IMPORT PYGAME
import random
import time

pygame.init()           #INTILIZING PYGAME

wn = pygame.display.set_mode((630,450))         #SETTING SCREEN SIZE
pygame.display.set_caption("FLAPPY BIRD")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('bg.jpg')            #LOADING IMAGES
bg1 = pygame.image.load('intro.jpg')
wing = pygame.mixer.Sound('wing.wav')       #LOAING SOUNDS
point = pygame.mixer.Sound('point.wav')
hit = pygame.mixer.Sound('hit.wav')
bg_mus = pygame.mixer.music.load('happy.wav')
scr = 0

bird_fly = ['bird_d.png','bird_m.png','bird_u.png']
bird = pygame.image.load(random.choice(bird_fly))
pygame.mixer.music.play(0)          #TO PLAY MUSICS CONTINOUSLY

d_pipe = pygame.image.load('b_p.png')       #DOWN PIPE
u_pipe = pygame.image.load('t_p.png')       #UP PIPE

font = pygame.font.SysFont('comicsan',70)           #FONTS TO WRITE ON SCREEN
font_p = pygame.font.SysFont('comicsan',30)

hit_p = font.render(("YOU HIT ON PIPE"),5,(255,0,0))

clock = pygame.time.Clock()     #FPS

class screen(object):               #CLASS
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.main()

    def main(self):
        game = False
        intro = True
        while intro:
            wn.blit(bg1,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        intro = False
                        game = True
        self.birdx = 35
        self.birdy = 225
        bird_xmove = 0
        bird_ymove = 0
        pipe_space = 200
        pipe_spd = 1
        #####   PIPE X  Y   CORDINATES   #####
        space = 100
        p1_x = 100
        p1_y = 270

        p2_x = p1_x + pipe_space
        p2_y = 200

        p3_x = p2_x + pipe_space
        p3_y = 300

        p4_x = p3_x + pipe_space
        p4_y = 230
        #####   PIPE X  Y   CORDINATES   #####
        
        pipe1 = Pipes(p1_x, p1_y, space, pipe_spd)
        pipe2 = Pipes(p2_x, p2_y, space, pipe_spd)
        pipe3 = Pipes(p3_x, p3_y, space, pipe_spd)
        pipe4 = Pipes(p4_x, p4_y, space, pipe_spd)

        #IT SHOWS SCORE ON SCREEN
        def score(scr):
                point = font_p.render(("SCORE: "+str(scr)),5,(255,0,0))
                wn.blit(point,(500,20))
                
        scr = 0
        #MAIN LOOP
        while game:
            clock.tick(60)          #FPS IS 60
            pygame.display.update()             #UPDATE THE PYGAME SCREEN
            wn.blit(bg,(0,0))   #SHOW THE BACKGROUND

                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()           #IF QUIT BUTTON CLICKED SCREEN QUITS

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        wing.play()                 #IF UP KEY PRESS BIRD FLY
                        bird_ymove = -3

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        wing.play()
                        bird_ymove = 1          ##CONTINOUSLY BIRD MOVES DOWN
         
            self.birdx += bird_xmove
            self.birdy += bird_ymove
            bird = FlappyBird(self.birdx, self.birdy)
            bird.draw()         #DRAW BIRD

            pipe1.draw_pipes()
            pipe2.draw_pipes()              #DRAW PIPES
            pipe3.draw_pipes()          
            pipe4.draw_pipes()
        
            pipe1.check_if()
            pipe2.check_if()            #CHECK THE PIPE X CORDINATES
            pipe3.check_if()
            pipe4.check_if()

            p1_newx = pipe1.pipe_move()         #MOVE PIPE
            p2_newx = pipe2.pipe_move()
            p3_newx = pipe3.pipe_move()
            p4_newx = pipe4.pipe_move()


            #######    PIPE COLLISION    #########
            if (self.birdy <= p1_y - 90) and (self.birdy <= p1_y) and (self.birdx >= p1_newx-25) and (self.birdx <= (p1_newx + 55)) or (self.birdy >= (p1_y)) and (self.birdy >= p1_y-50) and (self.birdx >= p1_newx-25) and (self.birdx <= (p1_newx + 55)) :
                hit.play()
                wn.blit(hit_p,(110,200))
                wn.blit(scr_s,(110,280))
                pygame.display.update()
                time.sleep(3)
                game = False

            if (self.birdy <= (p2_y -90)) and (self.birdy <= p2_y) and (self.birdx >= p2_newx-25) and (self.birdx <= (p2_newx + 55)) or (self.birdy >= (p2_y)) and (self.birdy >= p2_y-50) and (self.birdx >= p2_newx-25) and (self.birdx <= (p2_newx + 55)): 
                hit.play()
                wn.blit(hit_p,(110,200))
                wn.blit(scr_s,(110,280))
                pygame.display.update()
                time.sleep(3)
                game = False

            if (self.birdy <= (p3_y -90)) and (self.birdy <= p3_y) and (self.birdx >= p3_newx-25) and (self.birdx <= (p3_newx + 55)) or (self.birdy >= (p3_y)) and (self.birdy >= p3_y-50) and (self.birdx >= p3_newx-25) and (self.birdx <= (p3_newx + 55)):
                hit.play()
                wn.blit(hit_p,(110,200))
                wn.blit(scr_s,(110,280))
                pygame.display.update()
                time.sleep(3)
                game = False
    
            if (self.birdy <= (p4_y -90)) and (self.birdy <= p4_y) and (self.birdx >= p4_newx-25) and (self.birdx <= (p4_newx + 55)) or (self.birdy >= (p4_y)) and (self.birdy >= p4_y-50) and (self.birdx >= p4_newx-25) and (self.birdx <= (p4_newx + 55)):
                hit.play()
                wn.blit(hit_p,(110,200))
                wn.blit(scr_s,(110,280))
                pygame.display.update()
                time.sleep(3)
                game = False
            #######    PIPE COLLISION    #########    


            #INCREASE 1 SCORE IF CROSS ONE PIPE
            if self.birdx == p1_newx+20 or self.birdx == p2_newx+20 or self.birdx == p3_newx+20 or self.birdx == p4_newx+20: 
                 scr = scr + 1
                 point.play()
            score(scr)
            scr_s = font.render(("YOUR SCORE : "+str(scr)),5,(255,0,0))
                
        pygame.quit()                
            
class FlappyBird(object):       #TO DRAW BIRD
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        bird = pygame.image.load(random.choice(bird_fly))
        wn.blit(bird,(self.x, self.y))

class Pipes(object):            #TO DRAW PIPE
    def __init__(self, x, y, space, speed):
        self.x = x
        self.y = y
        self.space = space
        self.speed = speed

    def draw_pipes(self):
        wn.blit(d_pipe,(self.x, self.y + 20))
        wn.blit(u_pipe,(self.x, self.y - 330))


    def pipe_move(self):        #MOVE PIPE
        self.x -= self.speed
        return self.x

    def check_if(self):
        if self.x < -60:
            self.x = 750

            
screen(630,450)             #MAIN CLASS


#------------------------------- GAME COMPLECTED -----------------------------#
#####################!! PROGRAMMER : S.MUKILAN !!############################
