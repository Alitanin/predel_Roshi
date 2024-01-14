import math
from random import choice
import pygame
from grafs import *
from vis import *

WIDTH = 800
HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
finished = False
but_start = Button_ON(screen, 400, 500, 50, 30, 'start', CYAN)
while not finished:
    screen.fill(BLACK)
    clock.tick(FPS)
    but_start.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            finished = but_start.event(but_start.click(event))
pygame.quit()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
button_point = Button_Point(screen, 100, 600, 90, 24, 'make mark', CYAN)
clock = pygame.time.Clock()

sputnic = Sputnic(screen, R=1.7*10**6, x=400, y=204, m=7.4*10**22, vx=6.46*10**3)
balls.append(sputnic)

center = Ball(screen, x=400, y=300, m=6*10**24, R=6.4*10**6)
center.color = GREEN
center.center = 1
balls.append(center)
finished = False
time = 0
while not finished:

    screen.fill(BLACK)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_point.event(button_point.click(event), time)
    screen.fill(BLACK)
    for b in balls:
        b.draw()
    button_point.draw()
    pygame.display.update()
    for i in range(7*10 ** 2):
        time += dt
        for b in balls:
            b.gravitation(balls)
            b.Vander_force(balls)
        for b in balls:
            b.move()
            b.info(time, balls)
pygame.quit()
for b in balls:
    draw_graf(b, points)
