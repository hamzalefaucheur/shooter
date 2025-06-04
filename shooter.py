
from pygame import *

class Enemy :
    
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        self.player_image=player_image
        self.player_x=player_x
        self.player_y=player_y
        self.size_x=size_x
        self.size_y=size_y
        self.player_speed=player_speed

    def draw(self):
      ufo = transform.scale(image.load(self.player_image), (self.size_x,self.size_y))  
      window.blit(ufo,(self.player_x,self.player_y))

    def updateposition(self):
        self.player_y=self.player_y+self.player_speed
        if self.player_y==600:
            self.player_y=50


enemy=Enemy("ufo.png",350,50,90,50,10)

window = display.set_mode((700, 500))

display.set_caption("prn")

background = transform.scale(image.load("galaxy.jpg"), (700, 500))
rocket = transform.scale(image.load("rocket.png"), (150,150))
x1=300
y1=300


game=True
while game:
    window.blit(background,(0, 0))
    window.blit(rocket,(x1, y1))

    enemy.draw()
    for e in event.get():
        if e .type == QUIT:
                game = False
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT]:
        x1=x1-10

    if keys_pressed[K_RIGHT]:
        x1=x1+10
    enemy.updateposition()



    display.update()



