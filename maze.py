from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
back = transform.scale(image.load("background.jpg"), (700,500))
game = True



font.init()
font = font.Font(None,70)
win = font.render("YOU WIN!!!", True, (34, 255, 3))
los = font.render("YOU LOSE!!!", True,(254, 2, 2))

class GameSprite():
    def __init__(self,image1,speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 700:
           self.rect.x += self.speed

class Enemy(GameSprite):
    discraption = "left"
    def update(self):
        if self.rect.x < 0:
            self.discraption = "right"
        if self.rect.x > 330:
            self.discraption = "left"
        if self.discraption == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall():
    def __init__(self, width,height,color_1,color_2,color_3,x,y):
            self.width = width
            self.height = height
            self.color_1 = color_1
            self.color_2 = color_2
            self.color_3 = color_3
            self.image = Surface((self.width,self.height))
            self.image.fill((self.color_1,self.color_2,self.color_3))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

sssr = Player("hero.png",2,0,100)
sssr2 = Enemy("cyborg.png",1,100,400)
sssr3= GameSprite("treasure.png",0,600,400)
wall = Wall(15, 290, 0,0,0,90,90)
wall1 = Wall(15, 390, 0,0,0,200,0)
wall2 = Wall(15, 300, 0,0,0,300,0)
wall3 = Wall(15, 390, 0,0,0,400,120)
wall4 = Wall(15, 300, 0,0,0,500,0)
wall5 = Wall(15, 400, 0,0,0,585,100)
wall6 = Wall(106,15,0,0,0,0,380)
wall7 = Wall(215,15,0,0,0,300,380)
clock = time.Clock()
FPS = 200
finish = False
#обработай событие «клик по кнопке "Закрыть окно"»
while game:
    

    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(back,(0,0))
        sssr.reset()
        sssr.update()
        sssr2.reset()
        sssr2.update()
        sssr3.reset()
        wall.reset()
        wall1.reset()
        wall2.reset()
        wall3.reset()
        wall4.reset()
        wall5.reset()
        wall6.reset()
        wall7.reset()
        if sprite.collide_rect(sssr, sssr3):
            window.blit(win,(200,200))
            finish = True
        if sprite.collide_rect(sssr,sssr2) or sprite.collide_rect(sssr,wall) or sprite.collide_rect(sssr,wall1) or sprite.collide_rect(sssr,wall2) or sprite.collide_rect(sssr,wall3) or sprite.collide_rect(sssr,wall4) or sprite.collide_rect(sssr,wall5) or sprite.collide_rect(sssr,wall6) or sprite.collide_rect(sssr,wall7):
            window.blit(los,(200,200))
            finish = True
    clock.tick(FPS)
    display.update()