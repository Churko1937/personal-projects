import random

class Weapon:
	def __init__(Weapon, Type, Damage):
		Weapon.Type = Type
		Weapon.Damage = Damage
		
class PC:
	def __init__(pc, Race, Class, Mod, HP, exp):
		pc.Race = Race
		pc.Class = Class
		pc.Mod = Mod
		pc.HP = HP
		pc.exp = exp
		
class enemy:
	options = []
	def __init__(enemy, type, hp, exp, ac, weapon, bonus):
		enemy.type = type
		enemy.hp = hp
		enemy.exp = exp
		enemy.ac = ac
		enemy.weapon = weapon
		enemy.bonus = bonus
		__class__.options.append(enemy)
		
Orc = enemy("Orc", 10, 50, 8, 10, 1)
Arch_Mage = enemy("Arch Mage", 99, 8400, 9 , 15, 3)
Bugbear = enemy("Bugbear", 38, 450, 13, 10, 2)
Chimera = enemy("Chimera", 104, 1800, 14, 15, 3)
Crab = enemy("Crab", 32, 200, 7, 9, 0)
Dragon = enemy("Dragon", 406, 120000, 17, 16, 3)
Dire_Wolf = enemy("Dire Wolf", 150, 2900, 10, 10, 2)
Drider = enemy("Drider", 123, 2300, 10, 9, 1)
Faerie = enemy("Faerie", 10, 100, 5, 8, 1)
Frost_Giant = enemy("Frost Giant", 138, 3900, 15, 13, 3)
Great_Ogre = enemy("Great Ogre", 73, 1100, 8, 5, 2)
Hydra = enemy("Hydra", 104, 1800, 14, 10, 4)


Sword = Weapon("Sword", 8)
Bow = Weapon("Bow", 8)
Great_Axe = Weapon("Great Axe", 12)
Scimitar = Weapon("Scimitar", 6)

LEVEL = 1
MOD = 2
HP = 25
EXP = 0
	
def fight():
	randIndex = random.randrange(len(enemy.options))
	rand_enemy = enemy.options[randIndex]
	print("You've encountered a " + rand_enemy.type + "!\n")
	def Attack(Weapon):
		nonlocal rand_enemy
		global player_char
		while rand_enemy.hp > 0:
			print("What would you like to do?\na: Attack\nb: Run\n")
			attack_choice = input()
			if attack_choice == "a":
				roll20 = random.randint(0, 20)
				print("Attack:" + str(roll20) +"\nEnemy AC: " + str(rand_enemy.ac) + "\n")
				if (roll20 + player_char.MOD) > rand_enemy.ac:
					print("The attack hits!")
					damage = random.randint(0, WEAPON.Damage) + player_char.MOD
					rand_enemy.hp = rand_enemy.hp - damage
					print(rand_enemy.hp)
					attack_choice = None
				else:
					print("The attack misses!")
			elif attack_choice == "b":
			    return 0
			else:
			    print("Usage: type a or b and press enter\n")
		print("EXP gained: " + str(rand_enemy.exp))
		return rand_enemy.exp
	global EXP
	exp = Attack(WEAPON)
	EXP = EXP + exp
	print("Current EXP = " + str(EXP))
	
	
def weapon_select():
	weapon = input("Choose your weapon(type --help for options) :")
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
	Class = input("Choose your class(type --help for options) :")
	if Class == "--help":
		print("Fighter\nPaladin\nWizard\nRanger\n")
		class_select()
	elif Class == "Fighter" or Class == "Paladin" or Class == "Wizard" or Class == "Ranger":
		return Class
	else:
		print("Selection unacceptable please try again\n")
		class_select()
		
def race_select():
	race = input("Choose your race(type --help for options) :")
	if race == "--help":
		print("Orc\nHuman\nDwarf\nElf\n")
		race_select()
	elif race == "Orc" or race == "Human" or race == "Dwarf" or race == "Elf":
		return race
	else:
		print("Selection unacceptable please try again\n")
		race_select()
	
		
def choice():
	print("What would you like to do?\n")
	print("a: Fight\nb: Quit\n")
	selection = input()
	if selection == "a":
		fight()
		choice()
	elif selection == "b":
		print("Rest and recover hero, for glory still awaits...")
		quit()
	else:
		print("Usage: type a or b and hit enter")
		choice()

	choice()
	
	
pc_race = race_select()
pc_class = class_select()
				
print("Welcome Hero! Glory and adventure awaits you!\n")
pc_name = input("What be your name brave hero?\n")
print("Congratulations " + pc_name + ". You are a(n) " +pc_race + " " + pc_class + "!\n")
player_char = PC(pc_race, pc_class, MOD, HP, EXP)
player_char.Race = pc_race
player_char.Class = pc_class
player_char.MOD = MOD
player_char.HP = HP
player_char.EXP = EXP

print(player_char.Race)
WEAPON = weapon_select()
choice()
	
	