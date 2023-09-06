#Importy
import pygame
import random
import os

pygame.init()

#Proměnné
sirka_okno = 2400
vyska_okno = 1025

sirka = 1000
vyska = sirka

left_x = 730
right_x = sirka_okno - 730

velikost_x = 80
velikost_y = 80
velikost_ast = sirka / 10 - 10
velikost_star = velikost_ast // 2

rychlost = sirka / 40
rychlost_ast = sirka / 30
rychlost_buff = rychlost / 3
rychlost_stars_front = 3 * rychlost // 4
rychlost_stars_middle = rychlost_stars_front // 1.5
rychlost_stars_bottom = rychlost_stars_front // 3

velikost_button = 160

fps = 30

cerna = (0, 0, 0)
bila = (255, 255, 255)
seda = (50, 50, 50)
modra = (0, 160, 255)
tmava_modra = (0, 30, 60)
zelena = (0, 255, 40)

sance = 80

#okno
okno = pygame.display.set_mode((sirka_okno, vyska_okno))
pygame.display.set_caption("Roket")

ship1_raw = pygame.image.load(os.path.join("ship1.png"))
ship1 = pygame.transform.scale(ship1_raw, (velikost_x, velikost_y)).convert_alpha()

ship2_raw = pygame.image.load(os.path.join("ship2.png"))
ship2 = pygame.transform.scale(ship2_raw, (velikost_x, velikost_y)).convert_alpha()

ship3_raw = pygame.image.load(os.path.join("ship3.png"))
ship3 = pygame.transform.scale(ship3_raw, (velikost_x, velikost_y)).convert_alpha()

asteroid1_raw = pygame.image.load(os.path.join("asteroid1.png"))
asteroid1_proc = pygame.transform.scale(asteroid1_raw, (round(velikost_ast), 2 * round(velikost_ast))).convert_alpha()

asteroid2_raw = pygame.image.load(os.path.join("asteroid2.png"))
asteroid2_proc = pygame.transform.scale(asteroid2_raw, (round(velikost_ast), 2 * round(velikost_ast))).convert_alpha()

shield_raw = pygame.image.load(os.path.join("inv_buff.png"))
shield = pygame.transform.scale(shield_raw, (round(velikost_ast), round(velikost_ast))).convert_alpha()

inv_bubble_raw = pygame.image.load(os.path.join("inv_bubble.png"))
inv_bubble = pygame.transform.scale(inv_bubble_raw, (200, 200)).convert_alpha()

laser_raw = pygame.image.load(os.path.join("laser_buff.png"))
laser = pygame.transform.scale(laser_raw, (round(velikost_ast), round(velikost_ast))).convert_alpha()

laser_proj_raw = pygame.image.load(os.path.join("laser.png"))
laser_proj = pygame.transform.scale(laser_proj_raw, (round(velikost_ast), round(velikost_ast // 4))).convert_alpha()

laser_proj_start_raw = pygame.image.load(os.path.join("laser_start.png"))
laser_proj_start = pygame.transform.scale(laser_proj_start_raw, (round(velikost_ast), round(velikost_ast // 4))).convert_alpha()

star1_raw = pygame.image.load(os.path.join("star1.png"))
star1 = pygame.transform.scale(star1_raw, (round(velikost_star), round(velikost_star))).convert_alpha()

star3_raw = pygame.image.load(os.path.join("star3.png"))
star3 = pygame.transform.scale(star3_raw, (round(velikost_star), round(velikost_star))).convert_alpha()

life_raw = pygame.image.load(os.path.join("lajf.png"))
life = pygame.transform.scale(life_raw, (round(velikost_ast), round(velikost_ast))).convert_alpha()

life_empty_raw = pygame.image.load(os.path.join("lajf_empty.png"))
life_empty = pygame.transform.scale(life_empty_raw, (round(velikost_ast), round(velikost_ast))).convert_alpha()

life_buff_raw = pygame.image.load(os.path.join("lajf_buff.png"))
life_buff_img = pygame.transform.scale(life_buff_raw, (round(velikost_ast), round(velikost_ast))).convert_alpha()

arrow_button_raw = pygame.image.load(os.path.join("arrow_button.png"))
arrow_button = pygame.transform.scale(arrow_button_raw, (velikost_button, velikost_button)).convert_alpha()

arrow_button_right = pygame.transform.rotate(arrow_button, -90).convert_alpha()
arrow_button_down = pygame.transform.rotate(arrow_button, 180).convert_alpha()
arrow_button_left = pygame.transform.rotate(arrow_button, 90).convert_alpha()

arrow_button_diagonal_raw = pygame.image.load(os.path.join("arrow_button_diagonal.png"))
arrow_button_diagonal = pygame.transform.scale(arrow_button_diagonal_raw, (velikost_button, velikost_button)).convert_alpha()

arrow_button_diagonal_right = pygame.transform.rotate(arrow_button_diagonal, -90).convert_alpha()
arrow_button_diagonal_down = pygame.transform.rotate(arrow_button_diagonal, 180).convert_alpha()
arrow_button_diagonal_left = pygame.transform.rotate(arrow_button_diagonal, 90).convert_alpha()

laser_button_raw = pygame.image.load(os.path.join("laser_button.png"))
laser_button = pygame.transform.scale(laser_button_raw, (velikost_button, velikost_button)).convert_alpha()

pause_button_raw = pygame.image.load(os.path.join("pause_button.png"))
pause_button = pygame.transform.scale(pause_button_raw, (velikost_button, velikost_button)).convert_alpha()

laser_sca_pos = (right_x - 90 - round(velikost_star), vyska_okno - 50 - velikost_star // 2)
star_sca_tuple = (round(velikost_star // 1.5), round(velikost_star // 1.5))
star3_sca_tuple = (round(velikost_star // 3), round(velikost_star // 3))
half_sirka = sirka_okno // 2
half_vyska = vyska_okno // 2
quart_vyska = vyska_okno // 4
fifth_vyska = vyska_okno // 5
third_sirka = sirka // 3
half_vel_x = velikost_x // 2
half_vel_y = velikost_y // 2
vel_star_tuple = (round(velikost_star), round(velikost_star))
vel_ast_sirka = left_x + sirka - velikost_ast
third_star = velikost_star // 3
sirka_sto = sirka_okno // 100
vyska_dva = vyska_okno + 200
left_x_ten = left_x + 10
rychlost_pol = rychlost // 2

font = pygame.font.Font("MinecraftRegular-Bmg3.otf", 40)
font_small = pygame.font.Font("MinecraftRegular-Bmg3.otf", 20)
font_large = pygame.font.Font("MinecraftRegular-Bmg3.otf", 80)

text_roket = font_large.render(f"ROKET", True, bila)
text_rect_roket = text_roket.get_rect()
text_rect_roket.center = (sirka_okno // 2, vyska_okno // 4)

text_mobile = font.render(f"mobile", True, bila)
text_rect_mobile = text_mobile.get_rect()
text_rect_mobile.center = (sirka_okno // 2, text_rect_roket.y + 120)

text_pause = font_small.render(f"Stiskni > pro start / pauzu", True, bila, cerna)
text_rect_pause = text_pause.get_rect()
text_rect_pause.center = (half_sirka, 4 * fifth_vyska)

# vykreslení
def render(raketa, asteroids, skore, hiskore, last, diff, diff_tick, invincible_time, invincible, buffs, pause, lasers, laser_las, las_used, las_invent, ship, asteroid, stars_front, stars_bottom, lifes, life_buff, clock, tup, tright, tdown, tleft, tupdi, trightdi, tdowndi, tleftdi, tpause, tlaser):
	
	okno.fill(cerna)
	
	# vykreslení hvězd
	for stars in stars_front:
		okno.blit(star1, stars)
		
	for stars in stars_bottom:
		star_sca = pygame.transform.scale(star3, star3_sca_tuple)
		okno.blit(star_sca, stars)
	
	# vykreslení textů	
	text_skore = font.render(f"SC: {skore}", True, seda, cerna)
	text_rect_skore = text_skore.get_rect()
	text_rect_skore.center = (half_sirka, half_vyska)
	
	text_last = font.render(f"LT: {last}", True, seda, cerna)
	text_rect_last = text_last.get_rect()
	text_rect_last.center = (half_sirka, half_vyska + 45)
	
	text_hiskore = font.render(f"HI: {hiskore}", True, seda, cerna)
	text_rect_hiskore = text_hiskore.get_rect()
	text_rect_hiskore.center = (half_sirka, half_vyska + 90)
	
	text_invincible = font.render(f"{invincible_time}", True, bila)
	text_rect_invincible = text_invincible.get_rect()
	text_rect_invincible.center = (raketa.x + half_vel_x, raketa.y + 1.3 * velikost_y)
	
	text_laser = font.render(f"{las_invent}", True, bila)
	text_rect_laser = text_laser.get_rect()
	text_rect_laser.center = (right_x - 50, vyska_okno - 50)
	
	text_fps = font.render(f"{round(clock.get_fps())}", True, seda)
	text_rect_fps = text_fps.get_rect()
	text_rect_fps.center = (left_x + 100, 100)
	
	okno.blit(text_skore, text_rect_skore)
	okno.blit(text_last, text_rect_last)
	okno.blit(text_hiskore, text_rect_hiskore)
	
	# vykreslení ochranného štítu
	if invincible:
		okno.blit(inv_bubble, (raketa.x - 60, raketa.y - 60))
		okno.blit(text_invincible, text_rect_invincible)
		
	# vykreslení počtu laserů
	okno.blit(text_laser, text_rect_laser)
	laser_sca = pygame.transform.scale(laser, vel_star_tuple)
	okno.blit(laser_sca, laser_sca_pos)
	
	# vykreslení rakety
	okno.blit(ship, raketa)
	
	# vykreslení asteroidů
	for asts in asteroids:
		okno.blit(asteroid, asts)
	
	# vykreslení buffů
	for buff in buffs:
		okno.blit(shield, buff)
	
	for laser_buff in lasers:
		okno.blit(laser, laser_buff)
		
	for lif in life_buff:
		okno.blit(life_buff_img, lif)
		
	# vykreslení laseru
	if las_used:
		laser_proj = pygame.transform.scale(laser_proj_raw, (50, raketa.y))
		laser_proj_start = pygame.transform.scale(laser_proj_start_raw, (50, 50))
		okno.blit(laser_proj, laser_las)
		okno.blit(laser_proj_start, (raketa.x + half_vel_x - 25, raketa.y - half_vel_y - 1))
		
	# vykreslení životů
	if lifes > 0:
		okno.blit(life, (left_x_ten, vyska - 100))
		okno.blit(life_empty, (left_x_ten + velikost_ast, vyska - 100))
		okno.blit(life_empty, (left_x_ten + 2 * velikost_ast, vyska - 100))
	if lifes > 1:
		okno.blit(life, (left_x_ten + velikost_ast, vyska - 100))
		okno.blit(life_empty, (left_x_ten + 2 * velikost_ast, vyska - 100))
	if lifes > 2:
		okno.blit(life, (left_x_ten + 2 * velikost_ast, vyska - 100))
	
	# vykreslení tlačítek ovládání
	okno.blit(arrow_button, tup)
	okno.blit(arrow_button_right, tright)
	okno.blit(arrow_button_down, tdown)
	okno.blit(arrow_button_left, tleft)
	
	okno.blit(arrow_button_diagonal, tupdi)
	okno.blit(arrow_button_diagonal_right, trightdi)
	okno.blit(arrow_button_diagonal_down, tdowndi)
	okno.blit(arrow_button_diagonal_left, tleftdi)
	
	okno.blit(laser_button, tlaser)
	#pause je v pause ;)
		
	# vykreslení pause
	if pause:
		okno.blit(text_pause, text_rect_pause)
		okno.blit(text_roket, text_rect_roket)
		okno.blit(text_mobile, text_rect_mobile)
		okno.blit(arrow_button_right, tpause)
	else:
		okno.blit(pause_button, tpause)
		
	# vykreslení fps
	okno.blit(text_fps, text_rect_fps)
	
	# update
	pygame.display.flip()
	
# pohyb rakety
def roket_pohyb(vstup, raketa, pause, tupd, trightd, tdownd, tleftd, tupdd, trightdd, tdowndd, tleftdd):
	
	if tupd and not pause and raketa.y > 0:
		raketa.y -= rychlost
	elif tdownd and not pause and raketa.y + velikost_y < vyska:
		raketa.y += rychlost
	elif tleftd and not pause and raketa.x > left_x:
		raketa.x -= rychlost
	elif trightd and not pause and raketa.x + velikost_x < right_x:
		raketa.x += rychlost
		
	elif tupdd and not pause and raketa.y > 0 and raketa.x > left_x:
		raketa.y -= rychlost_pol
		raketa.x -= rychlost_pol
	elif tleftdd and not pause and raketa.y + velikost_y < vyska and raketa.x > left_x:
		raketa.y += rychlost_pol
		raketa.x -= rychlost_pol
	elif tdowndd and not pause and raketa.y + velikost_y < vyska and raketa.x + velikost_x < right_x:
		raketa.y += rychlost_pol
		raketa.x += rychlost_pol
	elif trightdd and not pause and raketa.y > 0 and raketa.x + velikost_x < right_x:
		raketa.y -= rychlost_pol
		raketa.x += rychlost_pol
		
# vytvoření asteroidů
def ast_spawn(asteroids, raketa, skore, hiskore, diff, pause):
	
	diff_sance = round(sance / (diff / 2))
	
	if random.randint(0, diff_sance) == 0 and not pause:
		ast1 = pygame.Rect(random.randint(left_x, left_x + third_sirka - velikost_ast), -100, velikost_ast, velikost_ast)
		asteroids.append(ast1)
			
	if random.randint(0, diff_sance) == 0 and not pause:
		ast2 = pygame.Rect(random.randint(left_x + third_sirka, left_x + 2 * third_sirka - velikost_ast), -100, velikost_ast, velikost_ast)
		asteroids.append(ast2)
	
	if random.randint(0, diff_sance) == 0 and not pause:
		ast3 = pygame.Rect(random.randint(left_x + 2 * third_sirka, left_x + 3 * third_sirka - velikost_ast), -100, velikost_ast, velikost_ast)
		asteroids.append(ast3)

# vytvoření buffů
def buff_spawn(buffs, pause):
	
	if random.randint(0, sance * 6) == 0 and not pause:
		buff_inv = pygame.Rect(random.randint(left_x, vel_ast_sirka), - 100, velikost_ast, velikost_ast)
		buffs.append(buff_inv)

# vytvoření laserů
def laser_spawn(lasers, pause):
	
	if random.randint(0, sance * 5) == 0 and not pause:
		buff_las = pygame.Rect(random.randint(left_x, vel_ast_sirka), - 100, velikost_ast, velikost_ast)
		lasers.append(buff_las)
		
# vytvoření životů
def life_spawn(life_buff, pause):
	
	if random.randint(0, sance * 10) == 0 and not pause:
		buff_lif = pygame.Rect(random.randint(left_x, vel_ast_sirka), - 100, velikost_ast, velikost_ast)
		life_buff.append(buff_lif)
	
# vytvoření hvězd v pozadí
def stars_spawn_front(stars_front, pause):
	
	if random.randint(0, 100) == 0 and not pause:
		star_front = pygame.Rect(random.randint(left_x, left_x + sirka - velikost_star), - 100, velikost_star, velikost_star)
		stars_front.append(star_front)
		
def stars_spawn_bottom(stars_bottom, pause):
	
	if random.randint(0, 20) == 0 and not pause:
		star_bottom = pygame.Rect(random.randint(left_x, left_x + sirka - velikost_star), - 100, third_star, third_star)
		stars_bottom.append(star_bottom)

# Program

def main():
	
	spusteno = True
	clock = pygame.time.Clock()
	
	# pause
	pause = True
	pause_sleep = 5
	
	# cheat
	cheat_sleep = 0
	
	# raketa
	raketa = pygame.Rect(half_sirka - half_vel_x, (quart_vyska) * 3, velikost_x, velikost_y)
	
	# tlačítka ovládání
	tup = pygame.Rect(2 * (velikost_button + 10), vyska_okno - 3 * (velikost_button + 10), velikost_button, velikost_button)
	tright = pygame.Rect(3 * (velikost_button + 10), vyska_okno - 2 * (velikost_button + 10), velikost_button, velikost_button)
	tdown = pygame.Rect(2 * (velikost_button + 10), vyska_okno - (velikost_button + 10), velikost_button, velikost_button)
	tleft = pygame.Rect((velikost_button + 10), vyska_okno - 2 * (velikost_button + 10), velikost_button, velikost_button)
	
	tupdi = pygame.Rect((velikost_button + 10), vyska_okno - 3 * (velikost_button + 10), velikost_button, velikost_button)
	trightdi = pygame.Rect(3 * (velikost_button + 10), vyska_okno - 3 * (velikost_button + 10), velikost_button, velikost_button)
	tdowndi = pygame.Rect(3 * (velikost_button + 10), vyska_okno - (velikost_button + 10), velikost_button, velikost_button)
	tleftdi = pygame.Rect((velikost_button + 10), vyska_okno - (velikost_button + 10), velikost_button, velikost_button)
	
	tlaser = pygame.Rect(sirka_okno - 2 * (velikost_button + 10), vyska_okno - 2 * (velikost_button + 10), velikost_button, velikost_button)
	tpause = pygame.Rect(sirka_okno - 2 * (velikost_button + 10), (velikost_button + 10), velikost_button, velikost_button)
	
	# laser
	laser_las = pygame.Rect(raketa.x + half_vel_x - 5, 0, 50, vyska - raketa.y)
	
	# asteroidy
	asteroids = []
	
	# hvězdy
	stars_front = []
	stars_bottom = []
	
	# body dotyku
	touchpoints = {}
	
	tupd = False
	trightd= False
	tdownd = False
	tleftd = False
	
	tupdd = False
	trightdd = False
	tdowndd = False
	tleftdd = False
	
	# buffy
	buffs = []
	lasers = []
	life_buff = []
	
	# animace lodi
	anim_frame = 1
	anim_tick = 0
	ship = ship1
	
	# animace asteroidů
	animast_frame = 1
	animast_tick = 0
	asteroid = asteroid1_proc
	
	# sleep_tick
	sleep_tick = 0
	
	# sk´ore
	skore = 0
	skore_tick = 0
	
	hiskore = 0
	last = 0
	
	# obtížnost
	diff = 1
	diff_tick = 0
	
	# životy
	lifes = 3000
	lifes_sleep = 0
	
	# nesmrtelnost
	inv_pick = False
	invincible = False
	invincible_tick = 0
	invincible_time = 0
	
	# laser buffy
	las_pick = False
	las_invent = 0
	las_used = False
	las_time = 0
	
	# life buffy
	lif_pick = False
	
	while spusteno:
		
		clock.tick(fps)
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				spusteno = False
				
			if event.type == pygame.FINGERDOWN:
				fing_x = event.x * sirka_okno
				fing_y = event.y * vyska_okno
				touchpoints[event.finger_id] = fing_x, fing_y
			
			if event.type == pygame.FINGERUP:
				touchpoints.pop(event.finger_id, None)
				
			# reset pohybu
			tupd = False
			trightd= False
			tdownd = False
			tleftd = False	
			
			tupdd = False
			trightdd = False
			tdowndd = False
			tleftdd = False
			
			tlaserd = False
			tpaused = False
				
			for finger, pos in touchpoints.items():
				if tup.collidepoint(pos):
					tupd = True
					
				if tright.collidepoint(pos):
					trightd = True
					
				if tdown.collidepoint(pos):
					tdownd = True
					
				if tleft.collidepoint(pos):
					tleftd = True
					
					
				if tupdi.collidepoint(pos):
					tupdd = True
					
				if trightdi.collidepoint(pos):
					trightdd = True
					
				if tdowndi.collidepoint(pos):
					tdowndd = True
					
				if tleftdi.collidepoint(pos):
					tleftdd = True
					
				if tlaser.collidepoint(pos):
					tlaserd = True
					
				if tpause.collidepoint(pos):
					tpaused = True
		
		# reset sleep_tick
		if sleep_tick >= 2:
			sleep_tick = 0
		
		# přičtění sleep_tick
		sleep_tick += 1
		
		# vytvoření asteroidů						
		ast_spawn(asteroids, raketa, skore, hiskore, diff, pause)
		
		# vytvoření hvězd
		stars_spawn_front(stars_front, pause)
		stars_spawn_bottom(stars_bottom, pause)
		
		# vytvoření buffů
		buff_spawn(buffs, pause)
		laser_spawn(lasers, pause)
		life_spawn(life_buff, pause)
		
		# přičítání pause_sleep
		pause_sleep += 1
		
		# přičítání lifes_sleep
		lifes_sleep += 1
		
		# přičítání anim_frame
		anim_tick += 1
		
		# přičítání sk´ore
		if not pause: # tady začíná pause - - - - - - - - - - - - - - -
			skore_tick += 1
			if skore_tick == 30:
				skore += 1
				skore_tick = 0
		
		# zvýšení obtížnosti
			diff_tick += 1
			if diff_tick > 300:
				diff += 1
				diff_tick = 0
		
		# přičítání animace lodi
			anim_tick += 1
			if anim_tick >= 15:
				anim_frame += 1
				anim_tick = 0
				
			if anim_frame >= 4:
				anim_frame = 1
		
		# přičítání animace astroidů
			animast_tick += 1
			if animast_tick >= 15:
				animast_frame += 1
				animast_tick = 0
			
			if animast_frame == 3:
				animast_frame = 1
		
		# přičítání cheat_sleep
			cheat_sleep += 1
																		
		# zjištění vstupů		
		vstup = pygame.key.get_pressed()
		if pause and tpaused and pause_sleep > 10:
			pause = False
			pause_sleep = 0
		elif not pause and tpaused and pause_sleep > 10:
			pause = True
			pause_sleep = 0
		
		roket_pohyb(vstup, raketa, pause, tupd, trightd, tdownd, tleftd, tupdd, trightdd, tdowndd, tleftdd)
		
		# sebrání nesmrtelnosti
		if not pause:
		
		# odečítání z času nesmrtelnosti
			if inv_pick:
				invincible = True
				invincible_time = 5
				invincible_tick =0
				inv_pick = False
		
			if invincible:
				invincible_tick += 1
				
				if invincible_tick == 30:
					invincible_time -= 1
					invincible_tick = 0
				
				if invincible_time == 0:
					invincible = False
			
		# odečítání z času laseru
			if tlaserd and not las_used and las_invent > 0:
				las_used = True
				las_invent -= 1
				print(las_invent)
				
			if las_pick:
				las_invent += 1
				las_pick = False
			
			if las_used:
				las_time += 1
				laser_las.update(raketa.x + half_vel_x - 25, 0, 50, raketa.y)
			
			if las_time == 40:
				las_used = False
				las_time = 0
		
		# přičtění životů z buffu
			if lif_pick and lifes < 3:
				lifes += 1
				lif_pick = False
		
		# pohyb asteroidů
		if not pause:
			for asts in asteroids:
				asts.y += rychlost_ast
		
				if raketa.colliderect(asts) and not invincible and lifes_sleep > 10:
	
					lifes -= 1
					lifes_sleep = 0
					
					asteroids.remove(asts)
				
				if raketa.colliderect(asts) and invincible:
					asteroids.remove(asts)
				
				if asts.y > vyska_dva:
					asteroids.remove(asts)
					
				try:
					if laser_las.colliderect(asts) and len(asteroids) > 0:
						asteroids.remove(asts)
				except:
					print()
					
		# reset
			if lifes == 0:
				
				asteroids.clear()
				buffs.clear()
				lasers.clear()
				life_buff.clear()
				
				last = skore
									
				if skore > hiskore:
					hiskore = skore
				skore = 0
				skore_tick = 0
				
				diff = 1
				diff_tick = 0
				
				raketa.x = half_sirka - half_vel_x
				raketa.y = (quart_vyska) * 3
				
				las_used = False
				las_invent = 0
				las_time = 0
				
				lifes = 3
				
				pause = True					
		
		# pohyb buffů
			for buff in buffs:
				buff.y += rychlost_buff
				
				if raketa.colliderect(buff):
					buffs.remove(buff)
					inv_pick = True
					
				if buff.y > vyska_dva:
					buffs.remove(buff)
			
		# pohyb laser buffů
			for laser_buff in lasers:
				laser_buff.y += rychlost_buff
				
				if raketa.colliderect(laser_buff):
					lasers.remove(laser_buff)
					las_pick = True
				
				if laser_buff.y > vyska_dva:
					lasers.remove(laser_buff)
		
		# pohyb life buffů
			for life_buffs in life_buff:
				life_buffs.y += rychlost_buff
				
				if raketa.colliderect(life_buffs) and lifes < 3:
					life_buff.remove(life_buffs)
					lif_pick = True
				
				if life_buffs.y > vyska_dva:
					life_buff.remove(life_buffs)
			
		# pohyb hvězd
		if not pause: # and sleep_tick == 1:
			for stars in stars_front:
				stars.y += rychlost_stars_front
				
				if stars.y > vyska_dva:
					stars_front.remove(stars)
				
			for stars in stars_bottom:
				stars.y += rychlost_stars_bottom
				
				if stars.y > vyska_dva:
					stars_bottom.remove(stars)
		
		# změna animace lodi
		if not pause:
			if anim_frame == 1:
				ship = ship1
			elif anim_frame == 2:
				ship = ship2
			elif anim_frame == 3:
				ship = ship3
			else:
				ship = ship3
				
		# změna animace asteroidů
		if not pause:
			if animast_frame == 1:
				asteroid = asteroid1_proc
			elif animast_frame == 2:
				asteroid = asteroid2_proc
			else:
				asteroid = asteroid1_proc
						
		render(raketa, asteroids, skore, hiskore, last, diff, diff_tick, invincible_time, invincible, buffs, pause, lasers, laser_las, las_used, las_invent, ship, asteroid, stars_front, stars_bottom, lifes, life_buff, clock, tup, tright, tdown, tleft, tupdi, trightdi, tdowndi, tleftdi, tpause, tlaser)
		
	pygame.quit()
	
if __name__ == "__main__":
	main()