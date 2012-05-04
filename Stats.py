class Stat:
    def __init__(self, maxstat, growth = 50, cap = 30):
        self.max = maxstat
        self.current = maxstat
        self.growth = growth
        self.cap = cap

class Stats:
    def __init__(self, hp, attack, magic, defense, magicdefense, skill, speed, moverange, hpgrowth = 90, hpcap = 50, atkgrowth = 50, atkcap = 30, magatkgrowth = 50, magatkcap = 30, defgrowth = 50, defcap = 30, magdefgrowth = 50, magdefcap = 30, skillgrowth = 50, skillcap = 30, speedgrowth = 50, speedcap = 30, level = 1):
        self.level = level
        self.hp = Stat(hp, growth = hpgrowth, cap = hpcap)
        self.attack = Stat(attack, growth = atkgrowth, cap = atkcap)
        self.magicattack = Stat(magic, growth = magatkgrowth, cap = magatkcap)
        self.defense = Stat(defense, growth = defgrowth, cap = defcap)
        self.magicdefense = Stat(magicdefense, growth = magdefgrowth, cap = magdefcap)
        self.skill = Stat(skill, growth = skillgrowth, cap = skillcap)
        self.speed = Stat(speed, growth = speedgrowth, cap = speedcap)
        self.moverange = moverange
#        self.attackrange = 1

	#def __init__(self):
	#	self.hp = 10
	#	self.attack = 1
	#	self.defense = 1
	#	self.moverange = 5
	#	self.attackrange = 1
