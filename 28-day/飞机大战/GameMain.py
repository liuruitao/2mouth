import pygame
HERO_FIRE_EVENT = pygame.USEREVENT + 1   #英雄发射子弹事件
from PlanSprite import *
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)	
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		#定时器 毫秒
		#第一个参数是事件的名字
		#第二个参数是多长时间执行一次时间
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		#敌机的精灵组
		self.enemy_group = pygame.sprite.Group()
		#每隔0.5秒发射一次子弹
		pygame.time.set_timer(HERO_FIRE_EVENT,500)
	def __create_sprites(self):
		#英雄组
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
	def start_game(self):
		print("游戏开始...")
		while  True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()	
	#事件监听
	def __event_handler(self):
		#获取用户按键
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 2
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -2
		else:
			self.hero.speed = 0
		
		for event in pygame.event.get():
		# 判断是否退出游戏
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:#定时器事件
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == HERO_FIRE_EVENT:#发射子弹
				self.hero.fire() 
#1、随机x值 一定要有最大值 随机数
#2、初始化速度  随机1-?
#3、初始化y的位置
	def __check_collide(self):
		pass
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)
	
		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)
	@staticmethod		
	def game_over():
		pygame.quit
		exit()
if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()	
