from ctypes.wintypes import MAX_PATH


class Weapon:
	def __init__(Weapon, Type, Damage):
		Weapon.Type = Type
		Weapon.Damage = Damage
		
class PC:
	def __init__(pc, Race, Class, Mod, HP, maxHP, mana, maxmana, exp: int, WEAPON, LEVEL: int, NAME, AC):
		pc.Race = Race
		pc.Class = Class
		pc.Mod = Mod
		pc.HP = HP
		pc.maxHP = maxHP
		pc.mana = mana
		pc.maxmana = maxmana
		pc.exp = exp
		pc.weapon = WEAPON
		pc.Level = LEVEL
		pc.Name = NAME
		pc.ac = AC

class weak_enemy:
	options = []
	def __init__(weak_enemy, type, hp, exp, ac, hitmod, weapon, bonus):
		weak_enemy.type = type
		weak_enemy.hp = hp
		weak_enemy.exp = exp
		weak_enemy.ac = ac
		weak_enemy.weapon = weapon
		weak_enemy.bonus = bonus
		weak_enemy.hitmod = hitmod
		__class__.options.append(weak_enemy)

class mid_enemy:
	options = []
	def __init__(mid_enemy, type, hp, exp, ac, hitmod, weapon, bonus):
		mid_enemy.type = type
		mid_enemy.hp = hp
		mid_enemy.exp = exp
		mid_enemy.ac = ac
		mid_enemy.weapon = weapon
		mid_enemy.bonus = bonus
		mid_enemy.hitmod = hitmod
		__class__.options.append(mid_enemy)

class strong_enemy:
	options = []
	def __init__(mid_enemy, type, hp, exp, ac, hitmod, weapon, bonus):
		strong_enemy.type = type
		strong_enemy.hp = hp
		strong_enemy.exp = exp
		strong_enemy.ac = ac
		strong_enemy.weapon = weapon
		strong_enemy.bonus = bonus
		strong_enemy.hitmod = hitmod
		__class__.options.append(strong_enemy)