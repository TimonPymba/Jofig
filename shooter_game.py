#Создай собственный Шутер!

from pygame import *
from random import randint

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Шутер")
back = transform.scale(image.load("galaxy.jpg"), (700,500))
game = True
nadpis = 0
font.init()
font = font.SysFont("Arial",40)
propush = 0

#Классы
class GameSprite(sprite.Sprite):
    def __init__(self,image1,speed,x,y,size1,size2):
        super().__init__()
        self.image = transform.scale(image.load(image1), (size1,size2))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 595:
           self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",9,self.rect.centerx,self.rect.top,8,33)
        bullets.add(bullet)

class Ufo(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            global propush
            propush +=1
            self.rect.y = -50
            self.rect.x = randint(0,595)
            self.speed = randint(2,4)

class Drug(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            global nadpis
            nadpis += 1
            self.rect.y = -50
            self.rect.x = randint(0,595)
            self.speed = randint(2,4)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y<0:
            self.kill()

igrok = Player("rocket.png",10,150,400,120,200)
bullets = sprite.Group()
vrag1 = sprite.Group()

for i in range(5):
    vrag = Ufo("ufo.png",randint(5,6),randint(0,595),0,113,80)
    vrag1.add(vrag)

clock = time.Clock()
FPS = 27
finish = False
#обработай событие «клик по кнопке "Закрыть окно"»
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                igrok.fire()

    if not finish:
        propusk = font.render("Пропущено:"+str(propush),True,(245, 245, 245))
        schet = font.render("Счёт:"+ str(nadpis),True,(245,245,245))
        window.blit(back,(0,0))
        window.blit(schet,(0,0))
        window.blit(propusk,(0,30))
        igrok.reset()
        igrok.update()
        bullets.update()
        bullets.draw(window)
        vrag1.update()
        vrag1.draw(window)
        v = sprite.groupcollide(bullets,vrag1, True,True)
        for i in v:
            nadpis += 1
            vrag = Ufo("ufo.png",randint(5,6),randint(0,595),0,113,80)
            vrag1.add(vrag)
        if propush > 10:
            finish = True
            proigris = font.render("Вы проиграли!", True, (255, 0, 0))
            window.blit(proigris,(225,250))

    clock.tick(FPS)
    display.update()