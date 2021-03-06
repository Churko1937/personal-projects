import random, pickle, time
from Classes import *
from os.path import exists



def fight():
	global player_char
	if player_char.Level < 4:
		randIndex = random.randrange(len(weak_enemy.options))
		enemy = weak_enemy.options[randIndex]
	elif player_char.Level < 11 and player_char.Level >= 4:
		randIndex = random.randrange(len(mid_enemy.options))
		enemy = mid_enemy.options[randIndex]
	else:
		randIndex = random.randrange(len(strong_enemy.options))
		enemy = strong_enemy.optins[randIndex]
	print("You've encountered a " + enemy.type + "!\n")
	def Attack(Weapon): 
		nonlocal enemy		
		global player_char
		global WEAPON
		while enemy.hp > 0 and player_char.HP > 0:
			print("What would you like to do?\na: Attack\nb: Run\n")
			attack_choice = input()
			if attack_choice == "a":
				roll20 = random.randint(0, 20)
				enemyroll = random.randint(0, 20)
				print("Attack:" + str(roll20 + player_char.Mod) +"\nEnemy AC: " + str(enemy.ac) + "\n")
				if (roll20 + player_char.Mod) > enemy.ac:
					print("The attack hits!")
					damage = random.randint(0, WEAPON.Damage) + player_char.Mod
					enemy.hp = enemy.hp - damage
					print("Enemy HP: " + str(enemy.hp))
					time.sleep(1)
					if (enemyroll + enemy.hitmod) > player_char.ac:
						print("Your AC: " + str(player_char.ac) + "\n")
						print("The enemy attack hits!")
						enemydamage = random.randint(1, enemy.weapon)
						player_char.HP = player_char.HP - enemydamage                       
					else:
						print("Enemy Attack: " + str(enemyroll + enemy.hitmod))
						print("Your AC: " + str(player_char.ac))
						print("The enemy attack misses!\n")
					attack_choice = None
				else:
					print("The attack misses!\n")
					time.sleep(1)
					if (enemyroll + enemy.hitmod) > player_char.ac:
						print("Enemy Attack: " + str(enemyroll + enemy.hitmod))
						print("Your AC: " + str(player_char.ac))
						print("The enemy attack hits!\n")
						enemydamage = random.randint(1, enemy.weapon)
						player_char.HP = player_char.HP - enemydamage
					else:
						print("Enemy Attack: " + str(enemyroll + enemy.hitmod))
						print("Your AC: " + str(player_char.ac))
						print("The enemy attack misses!\n")
					
			elif attack_choice == "b":
			    choice()
			else:
			    print("Usage: type a or b and press enter\n")
		if enemy.hp <= 0:
			print("EXP gained: " + str(enemy.exp))
			print("Current HP: " + str(player_char.HP))
			return enemy.exp
		else:
			print("You have been slain! Game over man!\n")
			return 0			
	exp = Attack(WEAPON)
	if exp == 0:
		player_char = startup()
		if not player_char:
			pc_race = race_select()
			pc_class = class_select()
			ac = 15
			weapon = weapon_select()
			NAME = input("What be your name brave hero?\n")
			player_char = PC(pc_race, pc_class, newMOD, newHP, newEXP, weapon, newLEVEL, NAME, ac)	
			player_char.Name = NAME
			player_char.Level = newLEVEL
			player_char.Race = pc_race
			player_char.Class = pc_class
			player_char.Mod = newMOD
			player_char.HP = newHP
			player_char.exp = newEXP
			player_char.ac = ac
	player_char.exp = player_char.exp + exp
	global LEVEL
	LEVEL = level()
	print("Current EXP = " + str(player_char.exp))
	
	
def weapon_select():
	weapon = input("Choose your weapon(type --help for options) :\n")
	if weapon == "--help":
		print("Sword\nBow\nGreat Axe\nScimitar\n")
		weapon_select()
	elif weapon == "Sword":
	     weapon = Sword
	     return weapon
	elif weapon == "Bow":
	    weapon = Bow
	    return weapon
	elif weapon == "Great Axe":
	    weapon = Great_Axe
	    return weapon
	elif weapon == "Scimitar":
	    weapon = Scimitar
	    return weapon
	else:
		print("Selection unacceptable, please try again")
		weapon_select()
		
	
def class_select():
	Class = input("Choose your class(type --help for options) :\n")
	if Class == "--help":
		print("Fighter\nPaladin\nWizard\nRanger\n")
		class_select()
	elif Class == "Fighter" or Class == "Paladin" or Class == "Wizard" or Class == "Ranger":
		return Class
	else:
		print("Selection unacceptable please try again\n")
		class_select()
		
def race_select():
	race = input("Choose your race(type --help for options) :\n")
	if race == "--help":
		print("Orc\nHuman\nDwarf\nElf\n")
		race_select()
	elif race == "Orc" or race == "Human" or race == "Dwarf" or race == "Elf":
		return race
	else:
		print("Selection unacceptable please try again\n")
		race_select()
	
	#choose to fight or quit. if quit then save PC class and Weapon class to output files and quits program	
def choice():
	print("What would you like to do?\n")
	print("a: Fight\nb: Quit\nc: items")
	selection = input()
	if selection == "a":
		fight()
		choice()
	elif selection == "b":
		global player_char
		global WEAPON
		with open('dndsave.pkl', 'wb') as output:
			pickle.dump(player_char, output, pickle.HIGHEST_PROTOCOL)
		with open("weaponsave.pkl", "wb") as weapon:
			pickle.dump(WEAPON, weapon, pickle.HIGHEST_PROTOCOL)
		with open("itemsave.pkl", "wb") as item:
			pickle.dump([item_hp, item_mana], item, pickle.HIGHEST_PROTOCOL)
		
		print("Rest and recover hero, for glory still awaits...")
		quit()
	elif selection == "c":
		items()
	else:
		print("Usage: type a or b and hit enter")
		choice()

	choice()

#compares current player exp to threshold and increments level if thresh is reached and sets next level threshold
def level():
	global player_char
	global thresh
	thresh = level_dict[player_char.Level]
	if player_char.exp > thresh:
		player_char.Level = player_char.Level + 1
		print("Level Up! You are now level " + str(player_char.Level) + "!")
		return player_char.Level
	else:
		return player_char.Level

#loads class file from previous saved game or starts a new game. If no saved game exists, start a new game.
def startup():
	try:
		global player_char
		global item_hp
		global item_mana
		print("Welcome Hero! Glory and adventure awaits you!\n")
		game = input("would you like to a) continue  or b) Start new game?\n")
		if game != "a" and game != "b":
			print("Usage: enter a or b")
			startup()
		elif game == "a":
			with open('dndsave.pkl', 'rb') as inp:
				player_char = pickle.load(inp)
			with open('itemsave.pkl', 'rb') as item:
				item_hp, item_mana = pickle.load(item)
				
				return player_char, item_hp, item_mana 
		else:
			return False, 0, 0
	except FileNotFoundError:
		print("No saved game found. Starting new game.")
		return False, 0, 0

#loads weapon class from pervious game, if no game save exists return false
def weaponup():
	try:
		global WEAPON
		with open("weaponsave.pkl", "rb") as inp:
			WEAPON = pickle.load(inp)
			return WEAPON
	except FileNotFoundError:
		return False

def items():		
	def item_choice():
		global newitem_hp
		global newitem_mana
		global item_hp
		global item_mana
		print("You have " + str(item_hp) + " health potion(s)\nYou have " + str(item_mana) + " mana potion(s)")
		print("What would you like to do?\n")
		print("a: consume health potion\n b: consume mana potion\n c: exit\n")
		pick = input()
		if pick == "a":
			global player_char
			if item_hp > 0:
				player_char.HP = player_char.maxHP
				item_hp = item_hp - 1
				print("You feel refreshed!")
				time.sleep(1)
				choice()
			else:
				print("You do not have any health potions to consume.\n")
				choice()
		elif pick == "b":
			if item_mana > 0:
				player_char.mana = player_char.maxmana
				item_mana = item_mana - 1
				print("Your power is retored!")
				time.sleep(1)
				choice()
			else:
				print("You have no mana potions to consume.\n")
				time.sleep(1)
				choice()
		elif pick == "c":
			choice()
		else:
			print("Usage: type a, b or c")
			items()
	if exists("itemsave.pkl"):
		item_choice()
	else:
		global newitem_hp
		global newitem_mana
		global item_hp
		global item_mana
		item_hp = newitem_hp
		item_mana = newitem_mana
		item_choice()
			


	



#type, hp, exp, ac, hitmod, weapon, bonus
Orc = weak_enemy("Orc", 15, 100, 13, 5, 12, 3) 
Crab = weak_enemy("Crab", 2, 10, 11, 0, 1, 1)
Bugbear = weak_enemy("Bugbear", 27, 200, 16, 4, 16, 2)
Faerie = weak_enemy("Faerie", 10, 100, 5, 1, 6, 1)
Giant_bat = weak_enemy("Giant Bat", 22, 50, 13, 4, 6, 2)
Dire_Wolf = weak_enemy("Dire Wolf", 37, 200, 14, 5, 12, 3)

Arch_Mage = mid_enemy("Arch Mage", 99, 8400, 12, 6, 4, 2)
Chimera = mid_enemy("Chimera", 114, 2300, 14, 7, 12, 4)
#Great_Ogre = mid_enemy("Great Ogre", 73, 1100, 8, 5, 2)
Drider = mid_enemy("Drider", 123, 2300, 19, 6, 16, 0)
Frost_Giant= mid_enemy("Frost Giant", 138, 3900, 15, 9, 36, 6)
Hydra = mid_enemy("Hydra", 172, 3900, 15, 8, 10, 5)

Vampire = strong_enemy("Vampire", 144, 10000, 16, 9, 8, 4)
Iron_Golem = strong_enemy("Iron Golem", 210, 15000, 20, 13, 24, 7)
#Dragon = strong_enemy("Dragon", 406, 120000, 17, 16, 3)

Sword = Weapon("Sword", 8)
Bow = Weapon("Bow", 8)
Great_Axe = Weapon("Great Axe", 12)
Scimitar = Weapon("Scimitar", 6)

level_dict = {1:300, 2:900, 3:2700, 4:6500, 5:14000, 6:23000, 7:34000, 8:48000, 9:64000, 10:85000, 11:100000, 12:120000, 13:140000, 14:165000, 15:195000, 16:225000, 17:265000, 18:305000, 19:355000}	
thresh = 0


newitem_hp = 1		
newitem_mana = 1
newLEVEL: int = 1
newMOD = 2
newHP = 25
newHPmax = 25
newmana = 25
newmanamax = 25
newEXP: int = 0
player_char, item_hp, item_mana = startup()
WEAPON = weaponup()



if not player_char:
	pc_race = race_select()
	pc_class = class_select()
	ac = 15
	WEAPON = weapon_select()
	NAME = input("What be your name brave hero?\n")
	player_char = PC(pc_race, pc_class, newMOD, newHP, newHPmax, newmana, newmanamax, newEXP, WEAPON, newLEVEL, NAME, ac)	
	player_char.Name = NAME
	player_char.Level = newLEVEL
	player_char.Race = pc_race
	player_char.Class = pc_class
	player_char.Mod = newMOD
	player_char.HP = newHP
	player_char.maxHP = newHPmax
	player_char.mana = newmana
	player_char.maxmana = newmanamax
	player_char.exp = newEXP
	player_char.ac = ac

if player_char.Level >= 5 and player_char.Level < 9:
	player_char.Mod = 3
elif player_char.Level >= 9 and player_char.Level < 13:
	player_char.Mod = 4
elif player_char.Level >= 13 and player_char.Level < 17:
	player_char.Mod = 5
elif player_char.Level >= 17:
	player_char.Mod = 6
else:
	player_char.Mod = 2	

					
print("Welcome Hero! Glory and adventure awaits you!\n")
print("Congratulations " + player_char.Name + ". You are a(n) " +player_char.Race + " " + player_char.Class + "!\n")
print("You are currently level " + str(player_char.Level) + " EXP: " + str(player_char.exp))
choice()

	
