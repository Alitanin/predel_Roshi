import math
from random import choice
import pygame
from grafs import *


WIDTH = 800
HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()

sputnic = Sputnic(screen,R=58*10**6,x=400,y=150,m=2*10**26,vx=5.6*10**4)
balls.append(sputnic)

center = Ball(screen,x=400,y=300,m=10**29,R=7*10**6)
center.color=YELLOW
center.center=1
balls.append(center)

finished = False
time = 0
while not finished:

    screen.fill(WHITE)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    for i in range(10 ** 3):
        time += dt
        screen.fill(WHITE)
        for b in balls:
            b.draw()
        pygame.display.update()

        for b in balls:
            b.gravitation(balls)
            b.Vander_force(balls)
        for b in balls:
            b.move()
            b.info(time,balls)



pygame.quit()
for b in balls:
    draw_graf(b)