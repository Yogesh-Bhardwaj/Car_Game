import random
import os
import pygame
pygame.init()
H=600
W=1300
GameWindow=pygame.display.set_mode((W,H))
pygame.display.set_caption("Cars")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, int(H/10))
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
c=(0,255,0)
d=(0,0,255)
e=(123,3,32)
color=[white,red,black,c,d,e]
bgimg=pygame.image.load("cargame.png").convert_alpha()
bgimg = pygame.transform.scale(bgimg, (W, H)).convert_alpha()
Maincar=pygame.image.load("Maincar.png").convert_alpha()
Maincar=pygame.transform.rotozoom(Maincar,0,0.2).convert_alpha()
pygame.display.set_icon(Maincar)
C1=pygame.transform.rotozoom(pygame.image.load("C1.png"),0,0.2).convert_alpha()
C2=pygame.transform.rotozoom(pygame.image.load("C2.png"),0,0.2).convert_alpha()
C3=pygame.transform.rotozoom(pygame.image.load("C3.png"),0,0.2).convert_alpha()
C=[C1,C2,C3]
h=Maincar.get_height()
w=Maincar.get_width()

pygame.mixer.music.load("Sounds\\Kalimba.mp3")
lose=pygame.mixer.Sound("Sounds\\lose.wav")
win=pygame.mixer.Sound("Sounds\\Win.wav")


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, [x,y])
def welcome():
    gameexit = False
    v=0
    while not gameexit:
        GameWindow.blit(bgimg,(0,v))
        GameWindow.blit(bgimg,(0,v-H))
        text_screen("Welcome to Cars", red, W/3, H/2)
        text_screen("Press Space Bar To Play", red, W/3, H/2 + H/15)
        v=(v+1)%H
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                    # pass
        pygame.display.update()
        clock.tick(60)
def plotopponentcar(x,y,C):
    GameWindow.blit(C,(x,y))

def gameloop():
    pygame.mixer.music.play(-1)
    mcx=int(W/2)
    mcy=H-h
    gameexit=False
    v=0
    ci1=random.randint(0,2)
    ci2=random.randint(0,2)
    cx1=random.randint(int((1.62)*W/10)+int(w/2),int(W/2 -w))
    cx2=random.randint(int(W/2),int(8.4*W/10-w-w/2))
    cy1=-h
    s=8
    cy2=-(1.5)*h
    score=0
    life=1
    t1=1
    t2=1
    while not gameexit:
        cvy1=s+2
        cvy2=s+2

        if(life):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameexit=True
            keys=pygame.key.get_pressed()
            GameWindow.blit(bgimg,(0,v))
            GameWindow.blit(bgimg,(0,v-H))
            GameWindow.blit(Maincar,(mcx,mcy))
            plotopponentcar(cx1,cy1,C[ci1])
            plotopponentcar(cx2,cy2,C[ci2])
            cy1+=cvy1
            cy2+=cvy2
            v=(v+s)%H
            if(keys[pygame.K_RIGHT])and(mcx+w<int(8.4*W/10)):
                mcx+=10
            if(keys[pygame.K_LEFT])and(mcx>int((1.62)*W/10)):
                mcx-=10
            if(keys[pygame.K_UP])and(mcy>0):
                mcy-=10
            if(keys[pygame.K_DOWN])and(mcy+h<H):
                mcy+=10
            t=0
            if(cy1>H):
                ci1=random.randint(0,2)
                # cx1=random.randint(int((1.62)*W/10),int(8.4*W/10)-w)
                cx1=random.randint(int((1.62)*W/10),int(W/2 -w))
                cy1=-h
                t1=1
                score+=10
                pygame.mixer.Sound.play(win)
            if(cy2>H):
                ci2=random.randint(0,2)
                # cx2=random.randint(int((1.62)*W/10),int(8.4*W/10)-w)
                cx2=random.randint(int(W/2),int(8.4*W/10)-w)
                cy2=-(1.5)*h
                t2=1
                score+=10
                pygame.mixer.Sound.play(win)
            if(cy1>(mcy-h))and(cy1<(mcy+h)):
                if(abs(mcx-cx1)<(99)*w/100)and(t1):
                    life-=1
                    t1=0
                    score-=10
                    pygame.mixer.Sound.play(lose)
            if(cy2>(mcy-h))and(cy2<(mcy+h)):
                if(abs(mcx-cx2)<99*w/100)and(t2):
                    life-=1
                    t2=0
                    score-=10
                    pygame.mixer.Sound.play(lose)
            text_screen("Score: " + str(score), red, 5, 5)
            text_screen("Life: " + str(life), red, 300, 5)
            if(score>100):
                s=12
            if(score>200):
                s=16
            if(score>400):
                s=20
        else:
            pygame.mixer.music.stop()
            GameWindow.blit(bgimg,(0,0))
            text_screen(f"SCORE = {int((0.5)*(score+abs(score)))}", red, W/10, H/2)
            text_screen("Game Over! Press Enter To Continue", red, W/40, H/2 + H/15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
welcome()
