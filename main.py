import math
from random import choice
import pygame
from classes import *



WIDTH = 800
HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()

sputnic = Sputnic(screen,R=58*10**6,x=400,y=110,m=2*10**26,r=10,vx=4*10**4)
balls.append(sputnic)
center = Ball(screen,x=400,y=300,m=10**29,r=6)
center.color=YELLOW
balls.append(center)

finished = False

while not finished:
    screen.fill(WHITE)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    for b in balls:
        b.draw()
    pygame.display.update()

    for b in balls:
        b.gravitation(balls)
        b.Vander_force(balls)
    for b in balls:
        b.move()




pygame.quit()