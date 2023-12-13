import pygame
import numpy as np
import math
RED = 0xFF0000
BLUE = 0x0050FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
gravitational_constant = 6.67408E-11
FPS = 30
day=60*60*24
#dt=0.01*day/FPS
dt=75/FPS
k=10**7
class Ball:
    def __init__(self,screen: pygame.Surface, x, y,m,R):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x*k
        self.y = y*k
        self.m = m
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.color = BLUE
        self.fx = 0
        self.fy = 0
        self.type='ball'
        self.real_r=R
        self.center=0
        self.ox = []
        self.oy = []

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        self.ax = self.fx / self.m
        self.ay = self.fy / self.m
        self.vx += self.ax*dt
        self.vy += self.ay*dt
        self.x += self.vx*dt
        self.y += self.vy*dt
    def gravitation(self,planets):
        self.fx=0
        self.fy=0
        for obj in planets:
            if obj != self:
                if obj.type=='sputnic':
                    Fx=self.fx 
                    Fy=self.fy 
                    self.gravitation(obj.fragments)
                    self.fx +=Fx
                    self.fy +=Fy
                else:
                    r = ((obj.x - self.x)**2 + (self.y - obj.y)**2)**0.5
                    if r==0:
                        print(self,obj)
                    self.fx -= ((gravitational_constant*self.m*obj.m)/(r**2))*((self.x - obj.x)/r)
                    self.fy -= ((gravitational_constant*self.m*obj.m)/(r**2)) *((self.y - obj.y)/r)


    def Vander_force(self,planets):
        for obj in planets:
            if obj != self:
                if obj.type=='sputnic':
                    self.Vander_force(obj.fragments)
                else:
                    Vander_constant = (gravitational_constant * self.m * obj.m) * (obj.real_r + self.real_r) ** 6
                    r = ((obj.x - self.x)**2 + (self.y - obj.y)**2)**0.5
                    if r==0:
                        print(self,obj)
                    self.fx += ((Vander_constant)/(r**8))*((self.x - obj.x)/r)
                    self.fy += ((Vander_constant)/(r**8)) *((self.y - obj.y)/r)



    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x/k, self.y/k),
            7*self.real_r/k
        )
    def info(self,time,objs):
        for obj in objs:
            if self.type == 'sputnic':
                self = self.main
            if self.center!=1 and obj.center==1:
                r = ((obj.x - self.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
                self.ox.append(time)
                self.oy.append(r)
            


class Sputnic(Ball):
    def __init__(self,screen: pygame.Surface, x, y,m,R,vx):
        super().__init__(screen, x, y,m,R)
        self.color=BLACK
        self.fragments=[]
        self.vx=vx
        self.type='sputnic'
 
        n=6
        dr=self.real_r/n
        p=self.m/(4/3*math.pi*(self.real_r**3))
        M=0
        for i in range(1,n):
            r=dr*i
            dm=4*math.pi*r*((R**2-r**2)**0.5)*p*dr
            M+=dm
            N=int(math.pi*r/dr)
            for j in range(N):
                f=2*math.pi*j/N
                X=r*math.cos(f)
                Y=r*math.sin(f)
                fragment = Ball(self.screen, x=(self.x + X) / k, y=(self.y + Y) / k, m=dm/N,R=dr*((n+1)/(2*n)))
                fragment.vx = self.vx
                self.fragments.append(fragment)
        fragment = Ball(self.screen, x=(self.x) / k, y=(self.y) / k, m=self.m-M,R=dr*((n+1)/(2*n)))
        fragment.vx = self.vx
        self.fragments.append(fragment)
        self.main=fragment
        print(len(self.fragments))


    def draw(self):
        for i in self.fragments:
            pygame.draw.circle(
                i.screen,
                i.color,
                (i.x / k, i.y / k),
                4.5*i.real_r / k
            )


    def move(self):
        for i in self.fragments:
            i.move()

    def gravitation(self, planets):
        for i in self.fragments:
            i.gravitation(planets)

    def Vander_force(self, planets):
        for i in self.fragments:
            i.Vander_force(planets)










