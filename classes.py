import pygame
import numpy as np
import math
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [GREEN, MAGENTA, CYAN]
gravitational_constant = 6.67408E-11
FPS = 30
day=60*60*24
dt=0.1*day/FPS
#dt=1/FPS
k=10**7
class Ball:
    def __init__(self,screen: pygame.Surface, x, y,m,r):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x*k
        self.y = y*k
        self.m = m
        self.r = r
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.color = BLUE
        self.fx = 0
        self.fy = 0
        self.type='ball'
        self.real_r=7*10**6

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
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
            if obj != self and self.type!='sputnic'and obj.type!='sputnic':
                r = ((obj.x - self.x)**2 + (self.y - obj.y)**2)**0.5
                self.fx -= ((gravitational_constant*self.m*obj.m)/(r**2))*((self.x - obj.x)/r)
                self.fy -= ((gravitational_constant*self.m*obj.m)/(r**2)) *((self.y - obj.y)/r)
                print(r)
                if r<100:
                    print(type(self),type(obj))
    def Vander_force(self,planets):
        for obj in planets:
            Vander_constant = (gravitational_constant*self.m*obj.m)*(obj.real_r+self.real_r)**6
            if obj != self and self.type!='sputnic'and obj.type!='sputnic':
                r = ((obj.x - self.x)**2 + (self.y - obj.y)**2)**0.5
                self.fx += ((Vander_constant)/(r**8))*((self.x - obj.x)/r)
                self.fy += ((Vander_constant)/(r**8)) *((self.y - obj.y)/r)
                print(r,self.fx*10**-26)
                if r<100:
                    print(type(self),type(obj))



    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x/k, self.y/k),
            50*self.real_r/k
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        X=((self.x-obj.x)**2+(self.y-obj.y)**2)**0.5<=self.r+obj.r

        if X:
            return True

        else:
            return False
class Sputnic(Ball):
    def __init__(self,screen: pygame.Surface, x, y,m,r,R,vx):
        super().__init__(screen, x, y,m,r)
        self.color=BLACK
        self.fragments=[]
        self.real_r=R
        self.vx=vx
        self.type='sputnic'
        '''
        num=self.real_r /5
        for X in np.arange(-self.real_r,self.real_r+num/2,num):
            for Y in np.arange(-self.real_r, self.real_r+num/2, num):
                if (X**2+Y**2)<=self.real_r**2:
                    fragment=Ball(self.screen,x=(self.x+X)/k,y=(self.y+Y)/k,m=0,r=6)
                    fragment.vx=self.vx
                    self.fragments.append(fragment)
        for i in self.fragments:
            i.m=self.m/(len(self.fragments))
        print(len(self.fragments))
        '''
        n=20
        N=25
        dr=self.real_r/n
        p=self.m/(4/3*math.pi*(self.real_r**3))
        M=0
        for i in range(1,n):
            r=dr*i
            dm=4*math.pi*r*((R**2-r**2)**0.5)*p*dr
            M+=dm
            for j in range(N):
                f=2*math.pi*j/N
                X=r*math.cos(f)
                Y=r*math.sin(f)
                fragment = Ball(self.screen, x=(self.x + X) / k, y=(self.y + Y) / k, m=dm/N, r=3)
                fragment.vx = self.vx
                fragment.real_r = self.real_r / n
                self.fragments.append(fragment)
            fragment = Ball(self.screen, x=(self.x) / k, y=(self.y) / k, m=self.m-M, r=3)
            fragment.vx = self.vx
            fragment.real_r=self.real_r/n
            self.fragments.append(fragment)
        print((self.m-M)/10**18,M/self.m)

    def draw(self):
        for i in self.fragments:
            pygame.draw.circle(
                i.screen,
                i.color,
                (i.x / k, i.y / k),
                10*i.real_r / k
            )


    def move(self):
        for i in self.fragments:
            i.move()

    def gravitation(self, planets):
        for i in self.fragments:
            i.gravitation(planets)










