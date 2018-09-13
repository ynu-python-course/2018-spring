#import
import pygame, sys, random
from pygame.locals import *

#init
pygame.init()

#界面
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('跳伞游戏')
#load image
background = pygame.image.load('resources/image/background.jpg').convert()
background0 = pygame.image.load('resources/image/background0.png')
game_over = pygame.image.load('resources/image/gameover.png')
#游戏音乐
collision_sound = pygame.mixer.Sound('resources/sound/collision.wav')
collision_sound.set_volume(0.3)
bottom_sound = pygame.mixer.Sound('resources/sound/bottom.wav')
bottom_sound.set_volume(0.3)
game_over_sound = pygame.mixer.Sound('resources/sound/game_over.wav')
game_over_sound.set_volume(0.3)
pygame.mixer.music.load('resources/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


class Player(pygame.sprite.Sprite):
    def __init__(self,player_image,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
    #玩家移动      
    def moveup(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else :
            self.rect.top -= self.speed
            
    def movedown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else :
            self.rect.top += self.speed
            
    def moveleft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
            
    def moveright(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

class P2(pygame.sprite.Sprite):
    def __init__(self,p2_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.speedy = 5
        self.speedx = 2
        self.image = p2_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        
    def moveright(self):
        self.rect.left = self.rect.left + self.speedx

    def moveup(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else :
            self.rect.top -= self.speedy
            
    def movedown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else :
            self.rect.top += self.speedy

class Bird(pygame.sprite.Sprite):
    def __init__(self,bird_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 2
        self.speedy = 1
        self.image = bird_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos

    def moveup(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else :
            self.rect.top -= self.speedy
            
    def movedown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else :
            self.rect.top += self.speedy

    def move(self):
        self.rect.left = self.rect.left + self.speedx

class Island(pygame.sprite.Sprite):
    def __init__(self,island_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 2
        self.image = island_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        
    def move(self):
        self.rect.left = self.rect.left + self.speed

#bird初始化
bird_image1 = pygame.image.load('resources/image/bird1.png')
bird_image2 = pygame.image.load('resources/image/bird2.png')
bird_image3 = pygame.image.load('resources/image/bird3.png')
bird_images = [bird_image1,bird_image2,bird_image3]

bird_number = 0
birds = pygame.sprite.Group()
bird_rect = pygame.Rect(0, 0, 40, 20)

#island初始化
island_image = pygame.image.load('resources/image/island.png')
island_number = 0
island_rect = pygame.Rect(0,0,40,40)  
islands = pygame.sprite.Group()

#p2初始化
p2_image = pygame.image.load('resources/image/p2.png')
p2_number = 0
p2_rect = pygame.Rect(0,0,40,25)  
p2s = pygame.sprite.Group()
#player初始化       
player_image = pygame.image.load('resources/image/player.png')
player_rect = pygame.Rect(0,0,40,25)        
player_pos = [600-player_rect.width, SCREEN_HEIGHT/2]
player = Player(player_image,player_pos)
ph = 100
#帧数       
clock = pygame.time.Clock()
#游戏开始界面
screen.blit(background0,(0,0))
pygame.display.flip()
#选择单人或双人游戏
start = True
while start:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and 75<=event.pos[0]<=236 and 300<=event.pos[1]<=340:
            bottom_sound.play()
            time0 = pygame.time.get_ticks()
            chiose = 1
            start = False
        if event.type==pygame.MOUSEBUTTONDOWN and 368<=event.pos[0]<= 535 and 300<=event.pos[1]<=340:
            bottom_sound.play()
            time0 = pygame.time.get_ticks()
            chiose = 2
            start =False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
running = True 
while chiose == 1 and running :
    #60帧
    clock.tick(60)

    #背景图
    screen.blit(background,(0,0))

    #生成鸟
    if bird_number % 50 ==0:   
        bird_pos = (-bird_rect.width,random.randint(0,SCREEN_HEIGHT-bird_rect.height))
        bird_img = bird_images[random.randint(0,2)]
        bird = Bird(bird_img,bird_pos)
        birds.add(bird)
    bird_number += 1
    if bird_number >= 100:  
        bird_number = 0
    for bird in birds:
        screen.blit(bird_images[random.randint(0,2)], bird.rect)
        bird.move()
        if bird.rect.left + bird_rect.width <= player.rect.left:
            if bird.rect.top > player.rect.top :
                bird.moveup()
            if bird.rect.top < player.rect.top :
                bird.movedown()
        
        if bird.rect.left >=  SCREEN_WIDTH:
            birds.remove(bird)
    
        if pygame.sprite.collide_circle(bird,player):
            collision_sound.play()
            ph -= 10
            birds.remove(bird)

    #生成island
    if len(islands) == 0 and int(pygame.time.get_ticks()/1000) % 15 == 0 :
        island_pos = (0-island_rect.width, random.randint(0,SCREEN_HEIGHT-island_rect.height))
        island = Island(island_image , island_pos) 
        islands.add(island) 
    for island in islands:
        screen.blit (island_image , island.rect)
        island.move()
        #islands移除island
        if island.rect.left > 600:
            islands.remove(island)
        #判断island和player是否碰撞
        if pygame.sprite.collide_circle(island,player):
            collision_sound.play()
            ph += 20
            islands.remove(island)

    # 绘制玩家
    if ph >= 100:
        ph = 100
    if ph > 0:
        screen.blit(player_image, player.rect)
    else:
        game_over_sound.play()
        running = False
    #血条显示
    pygame.draw.rect(screen, (255,0,0), Rect(250,450,ph,18))
    pygame.draw.rect(screen, (100,200,100,180), Rect(250,450,100,20), 2)
    #记时
    time_font = pygame.font.Font(None, 36)
    time_text = time_font.render(str(int((pygame.time.get_ticks()-time0)/1000)), True, (128, 128, 128))
    text_rect = time_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(time_text, text_rect)

    # 更新屏幕
    pygame.display.update()
    
    # 处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()
    # 处理键盘事件（移动p1的位置）
    if  key_pressed[K_UP]:
        player.moveup()
    if  key_pressed[K_DOWN]:
        player.movedown()
    if  key_pressed[K_LEFT]:
        player.moveleft()
    if  key_pressed[K_RIGHT]:
        player.moveright()



running2 = True
while chiose == 2 and running2 :
    #60帧
    clock.tick(60)
    #背景图
    screen.fill(0)
    screen.blit(background,(0,0))

    #生成鸟
    if bird_number % 50 ==0:   
        bird_pos = (-bird_rect.width,random.randint(0,SCREEN_HEIGHT-bird_rect.height))
        bird_img = bird_images[random.randint(0,2)]
        bird = Bird(bird_img,bird_pos)
        birds.add(bird)
    bird_number += 1
    if bird_number >= 100:  
        bird_number = 0
    for bird in birds:
        screen.blit(bird_images[random.randint(0,2)], bird.rect)
        bird.move()
        
        #bird出屏幕后就移除出birds
        if bird.rect.left >= SCREEN_WIDTH:
            birds.remove(bird)
        #判断bird和player是否碰撞
        if pygame.sprite.collide_circle(bird,player):
            collision_sound.play()
            ph -=20
            birds.remove(bird)

        #生成island
    if len(islands) == 0 and int(pygame.time.get_ticks()/1000) % 15 == 0  :
        island_pos = (0-island_rect.width, random.randint(0,SCREEN_HEIGHT-island_rect.height))
        island = Island(island_image , island_pos) 
        islands.add(island) 
    for island in islands:
        screen.blit (island_image , island.rect)
        island.move()
        #islands移除island
        if island.rect.left > 600:
            islands.remove(island)
        #判断island和player是否碰撞
        if pygame.sprite.collide_circle(island,player):
            collision_sound.play()
            ph += 20
            islands.remove(island)


    #生成p2
    if len(p2s) == 0 :
        p2_pos = (0,SCREEN_HEIGHT/2)
        p2 = P2(p2_image , p2_pos) 
        p2s.add(p2) 
    for p2 in p2s:
        screen.blit (p2_image , p2.rect)
        p2.moveright()
        #p2s移除p2
        if p2.rect.left > 600:
            p2s.remove(p2)
        #判断p2和player是否碰撞
        if pygame.sprite.collide_circle(p2,player):
            collision_sound.play()
            ph -= 20
            p2s.remove(p2)


    # 绘制玩家
    if ph >= 100:
        ph = 100
    if ph > 0:
        screen.blit(player_image, player.rect)
    else:
        game_over_sound.play()
        running2 = False
    
    #血条显示
    pygame.draw.rect(screen, (255,0,0), Rect(250,450,ph,18))
    pygame.draw.rect(screen, (100,200,100,180), Rect(250,450,100,20), 2)
    #记时
    time_font = pygame.font.Font(None, 36)
    time_text = time_font.render(str(int((pygame.time.get_ticks()-time0)/1000)), True, (128, 128, 128))
    text_rect = time_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(time_text, text_rect)


    # 更新屏幕
    pygame.display.update()
    
    # 处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # 获取键盘事件（上下左右按键）
    key_pressed = pygame.key.get_pressed()
    # 处理键盘事件（移动player的位置）
    if  key_pressed[K_UP]:
        player.moveup()
    if  key_pressed[K_DOWN]:
        player.movedown()
    if  key_pressed[K_LEFT]:
        player.moveleft()
    if  key_pressed[K_RIGHT]:
        player.moveright()
    #移动p2
    if  key_pressed[K_w]:
        p2.moveup()
    if  key_pressed[K_s]:
        p2.movedown()

screen.blit(game_over, (0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
