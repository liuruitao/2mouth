import pygame
from GameSprite import *
pygame.init()
#创建窗口
screen = pygame.display.set_mode((480,700))
#创建背景
bg = pygame.image.load('./images/background.png')
screen.blit(bg,(0,0))
#创建飞机
hero = pygame.image.load('./images/hero.gif')
screen.blit(hero,(180,500))
#创建时钟对象
clock = pygame.time.Clock()
#创建飞机的rect
hero_rect = pygame.Rect(180,500,200,200)
#创建精灵组
enemy1 = GameSprite('./images/enemy0.png',3)
enemy2 = GameSprite('./images/enemy1.png',2)
enemy3 = GameSprite('./images/enemy2.png',1)
enemy2.rect.x = 300
enemy3.rect.x = 320
enemy_group = pygame.sprite.Group(enemy1,enemy2,enemy3)

while True:
	clock.tick(60)
	hero_rect.y -= 10
	
	#覆盖背景
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
		#hero_rect.y+hero_rect.height<=0
	if hero_rect.bottom <= 0:  #Y的长度加飞机的长度
		hero_rect.y = 700
	#监听退出
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	enemy_group.update()
	enemy_group.draw(screen)
	pygame.display.update()
pygame.quit()
