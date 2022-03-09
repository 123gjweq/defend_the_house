import pyglet
from pyglet.media import StaticSource, load, Player
from math import sin, pi

#icon
icon = pyglet.resource.image("bgorHUD/icon.png")

#main menu and stuff
play = pyglet.image.load("bgorHUD/play.png")
play_highlight = pyglet.image.load("bgorHUD/play_highlight.png")
background = pyglet.image.load("bgorHUD/background.png")
loser_img = pyglet.image.load("bgorHUD/loser.png")
win_img = pyglet.image.load("bgorHUD/win.png")
enemy_img = pyglet.image.load("animation/sprite2.png")

#animations
sprite2 = pyglet.image.load("animation/sprite2.png")
sprite3 = pyglet.image.load("animation/sprite3.png")
sprite4 = pyglet.image.load("animation/sprite4.png")
sprite5 = pyglet.image.load("animation/sprite5.png")
sprite6 = pyglet.image.load("animation/sprite6.png")
sprite7 = pyglet.image.load("animation/sprite7.png")
sprite8 = pyglet.image.load("animation/sprite8.png")
sprite9 = pyglet.image.load("animation/sprite9.png")
list_of_walking_animations = (sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8, sprite9)
path_to_walk1 = [int(20 * sin(4 * i *  pi/180)) for i in range(1000)]
path_to_walk2 = [int(10 * sin(3 * i *  pi/180)) for i in range(1000)]
path_to_walk3 = [int(5 * sin(10 * i *  pi/180)) for i in range(1000)]

attack1 = pyglet.image.load("animation/spriteattack1.png")
attack2 = pyglet.image.load("animation/spriteattack2.png")
attack3 = pyglet.image.load("animation/spriteattack3.png")
bullet = pyglet.image.load("animation/bullet.png")
rocket_attack = pyglet.image.load("animation/spriteattackrocket.png")
list_of_attacking_animations = (attack1, attack2, attack3, attack3, attack3, attack3, attack2, attack1)
bullet_moves = [i for i in range(750) if i % 10 == 0]

#hud
hud = pyglet.image.load("bgorHUD/hud.png")
wall_font = pyglet.font.add_file("animation/freesansbold.ttf")

#sounds
player = Player()
bullet_sound = StaticSource(load("sounds/gun.wav"))
gunman_sound = StaticSource(load("sounds/sniper_shot.wav"))
reload_sound = StaticSource(load("sounds/reload.wav"))
select_sound = StaticSource(load("sounds/click.wav"))

#shot animation
blood1 = pyglet.image.load("animation/blood1.png")
blood2 = pyglet.image.load("animation/blood2.png")
blood3 = pyglet.image.load("animation/blood3.png")
blood4 = pyglet.image.load("animation/blood4.png")
blood5 = pyglet.image.load("animation/blood5.png")
blood6 = pyglet.image.load("animation/blood6.png")
blood7 = pyglet.image.load("animation/blood7.png")
blood8 = pyglet.image.load("animation/blood8.png")
blood9 = pyglet.image.load("animation/blood9.png")
blood10 = pyglet.image.load("animation/blood10.png")
list_of_bloods_temp = [blood1, blood2, blood3, blood4, blood5, blood6, blood7, blood8, blood9, blood10]
list_of_bloods = []
for x in range(10):
	for y in range(3):
		list_of_bloods.append(list_of_bloods_temp[x])

#explosion animation
crater1 = pyglet.image.load("animation/crater1.png")
crater2 = pyglet.image.load("animation/crater2.png")
crater3 = pyglet.image.load("animation/crater3.png")
crater4 = pyglet.image.load("animation/crater4.png")
crater5 = pyglet.image.load("animation/crater5.png")
crater6 = pyglet.image.load("animation/crater6.png")
crater7 = pyglet.image.load("animation/crater7.png")
list_of_craters_temp = [crater1, crater2, crater3, crater4, crater5, crater6, crater7, crater1]
list_of_craters = []
for x in range(8):
	for y in range(2):
		list_of_craters.append(list_of_craters_temp[x])

#sniper-shot
sniper_bullet = pyglet.image.load("animation/sniper_shot.png")

#dict of levels
dict_of_levels = {
	0: (150, 50, 100000), #enemy spawn rate, time duration, rocket spawn rate
	1: (100, 5, 100000),
	2: (90, 5, 100000),
	3: (80, 6, 100000),
	4: (70, 7, 100000),
	5: (60, 8, 100000),
	6: (50, 10, 100000),
	7: (40, 20, 100000),
	8: (38, 30, 100000),
	9: (36, 25, 100000),
	10: (35, 25, 100000),
	11: (33, 20, 100000),
	12: (30, 25, 100000),
	13: (28, 25, 100000),
	14: (16, 45, 100000),
	15: (22, 40, 150),
	16: (18, 40, 100),
	17: (16, 40, 60),
	18: (15, 40, 42),
	19: (14, 40, 30),
	20: (12, 30, 26),
	21: (13, 30, 40),
	22: (11, 40, 30),
	23: (10, 50, 20),
	24: (25, 70, 150),
	}

#shop
shop_background = pyglet.image.load("shop/shop.png")
shop_start = pyglet.image.load("shop/nextround.png")
shop_start_highlight = pyglet.image.load("shop/nextround_highlight.png")
bullet_pic = pyglet.image.load("shop/bullet.png")
bullet_pic_highlight = pyglet.image.load("shop/bullet_select.png")
hammer_pic = pyglet.image.load("shop/hammer.png")
hammer_pic_highlight = pyglet.image.load("shop/hammer_highlight.png")
repair_pic = pyglet.image.load("shop/repair.png")
repair_pic_highlight = pyglet.image.load("shop/repair_highlight.png")
sniper = pyglet.image.load("shop/sniper.png")
sniper_highlight = pyglet.image.load("shop/sniper_highlight.png")
fortify = pyglet.image.load("shop/fortify.png")
fortify_highlight = pyglet.image.load("shop/fortify_highlight.png")
sniper_man = pyglet.image.load("shop/sniper_man.png")
sniper_man_highlight = pyglet.image.load("shop/sniper_man_highlight.png")
repair_man = pyglet.image.load("shop/repair_man.png")
repair_man_highlight = pyglet.image.load("shop/repair_man_highlight.png")