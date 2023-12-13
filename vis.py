import pygame

points = []
class Button:
    def __init__(self,screen: pygame.Surface, x, y,h,w,name,color):
        self.screen = screen
        self.x = x
        self.y = y
        self.h = h
        self.w = w 
        self.color=color
        self.name = name

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x - self.h, self.y - self.w, self.h * 2, self.w * 2))
        f = pygame.font.SysFont('monospace', 30)
        text = f.render(self.name, True, (20, 10, 10),self.color)
        self.screen.blit(text, (self.x - 0.9*self.h, self.y - 0.5*self.w))
    def click(self,event):
        if abs(event.pos[0]-self.x)<=self.h and abs(event.pos[1]-self.y)<=self.w:
            return 1
        else:
            return 0
    def event(self):
        ''
            
class Button_ON(Button):
    def __init__(self, screen: pygame.Surface, x, y, h, w,name,color):
        super().__init__(screen, x, y,h,w,name,color)
    def event(self,state):
        super().event()
        if state == 1:
            return True
        else:
            return False
        
class Button_Point(Button):
    def __init__(self, screen: pygame.Surface, x, y, h, w,name,color):
        super().__init__(screen, x, y,h,w,name,color)
    def event(self,state,time):
        super().event()
        global points
        if state == 1:
            points.append(time)
            
            
        