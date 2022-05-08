from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,spr_image,spr_height,spr_weight,spr_x,spr_y,spr_speed):
        super().__init__()
        self.image = transform.scale(image.load(spr_image), (spr_height,spr_weight))
        self.speed = spr_speed

        self.rect = self.image.get_rect()
        self.rect.x = spr_x
        self.rect.y = spr_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < w_win - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < h_win - 80:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_y, wall_x, wall_widht, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.widht = wall_widht
        self.height = wall_height
        self.image = Surface((self.widht, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def paint(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Enemy(GameSprite):
    direction = "left" #направление 
    def update(self): # Функция перемещения 
        if self.rect.x <= 470: #граница
            self.direction = "right"
        if self.rect.x >= w_win - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed








h_win = 500
w_win = 700
window = display.set_mode((w_win,h_win))
display.set_caption("Догонялки")
b_im = image.load("background.jpg")#загрузка картинки
bgrd = transform.scale(b_im,(w_win,h_win))#изменяем размер до окна;;;;;

player = Player('hero.png', 100, 100 ,250, 300, 5)
gold = GameSprite('treasure.png', 100, 100 ,600, 400, 5)
enemy = Enemy('cyborg.png', 100, 100 ,w_win - 80, 180, 2)

w1 = Wall(100,236,121,100,50,50,250)
w2 = Wall(100,50,121,100,150,250,50)
#музика

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()



clock = time.Clock()

FPS  = 60

mixer.init()
win_sound = mixer.Sound("money.ogg")


font.init()
font = font.SysFont('Arial', 70)
win_text = font.render("POBEDA", True, (0,255,0))
win_text2 = font.render("lox", True, (255,0,0))
# игровой цикл
game = True
finish = False
while game:



    if finish != True:
       window.blit(b_im,(0,0))
       enemy.update()
       player.update()
       player.reset()
       enemy.reset()
       w1.paint()
       w2.paint()
       gold.reset()


       if sprite.collide_rect(player, gold):#проверка столкновения
           finish = True#остановка игри
           window.blit(win_text, ((200, 200)))
           win_sound.play()

       if sprite.collide_rect(player, enemy):#проверка столкновения
           finish = True#остановка игри
           window.blit(win_text2, ((200, 200)))
           win_sound.play()



    for e in event.get():
        if e.type == QUIT:
            game = False





    display.update()
    clock.tick(FPS)