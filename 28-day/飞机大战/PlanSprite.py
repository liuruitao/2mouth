import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#敌机事件的常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.rect.y += self.speed	
class Background(GameSprite):
	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Enemy(GameSprite):
	def __init__(self):
		image_name = "./images/enemy-1.gif"
		super().__init__(image_name)
		self.speed = random.randint(1,4)
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)  #随机位置
		self.rect.bottom = 0
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
	def __del__(self):
		print('消除敌机')
#英雄精灵
class Hero(GameSprite):
	def __init__(self):
		#设置初始位置
		super().__init__('./images/hero1.png',0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullets = pygame.sprite.Group()
	def update(self):
		#飞机水平移动
		self.rect.x += self.speed
		#判断屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
	def fire(self):
		print('biubiubiubiu')
		for i in (1,2,3):
			#创建子弹精灵
			bullet = Bullet()
			#设置精灵位置
			bullet.rect.bottom = self.rect.y - i * 20
			bullet.rect.centerx = self.rect.centerx
			#将精灵添加到精灵组
			self.bullets.add(bullet)
#子弹精灵
class Bullet(GameSprite):
	def __init__(self):
		super().__init__('./images/bullet1.png',-2)
	def update(self):
		super().update()
		#判断是否超出屏幕，如果是，从精灵组删除
		if self.rect.bottom < 0:
			self.kill()
	def __del__(self):
		print('消除子弹')
