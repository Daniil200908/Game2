from pygame import * #подключаю бибилотеку pygame




class GameSprite(sprite.Sprite): #
   def __init__(self, image_sprite, img_x, img_y, speed):
       super().__init__()
       self.image = transform.scale(image.load(image_sprite),(65,65))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = img_x
       self.rect.y = img_y
  
   def show_s(self):
       window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_d] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_hight - 80:
           self.rect.y += self.speed

class Enemy(GameSprite):
    naprav ='Left'
    def update(self):
        if self.rect.x <= 470:
            self.naprav = 'right'        
        if self.rect.x >= win_width - 85:
            self.naprav = 'Left' 

        if self.naprav == 'Left':
            self.rect.x -= self.speed
        else: 
            self.rect.x += self.speed
 
class wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_wight): 
        super().__init__()
        self.color1 = color1 
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_wight = wall_wight
         
        self.image = Surface ((self.wall_width, self.wall_wight)) 
        self.image.fill((self.color1, self.color2, self.color3)) 

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y  

    def show_w(self): 
        window.blit(self.image,(self.rect.x, self.rect.y))

win_width = 700
win_hight = 500


window = display.set_mode((win_width,win_hight))
display.set_caption("Лабиринт")
#ошибка   
backgraund = transform.scale(image.load("background.jpg"),(win_width,win_hight))


player = Player("hero.png",5, win_hight-70, 4)
#ошибка название картинки


mostr = Enemy("cyborg.png", win_width - 80, 280, 2)
finish_s = GameSprite("treasure.png", win_width - 120, win_hight - 80, 0)
#ошибка название картинки

w1 = wall(123,0,34,   200,150,   200, 10)
w2 = wall(123,0,34,  100,100,   10, 200)

game = True
finish = False


clock = time.Clock()




mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()
font = font.Font(None, 70) 
win = font.render('YOU WIN!', True,(255, 215,0)) 
lose = font.render('YOU LOSE!', True,(180, 0, 0)) 
 
while game:
   for i in event.get():
       if i.type == QUIT:
           game = False
  
   if finish != True:
       window.blit(backgraund,(0,0))
       player.show_s()
       mostr.show_s()
       finish_s.show_s()
       w1.show_w()
       w2.show_w()
       player.update()
       mostr.update()

       if sprite.collide_rect(player, mostr) or sprite.collide_rect(player, w1) or sprite.collide_rect(player,w2): 
          finish = True 
          window.blit(lose,(200, 200))
   display.update() 
   clock.tick(60)

  

  
   

          
          




