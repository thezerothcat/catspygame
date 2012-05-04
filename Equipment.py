prices = {'Sheet of Paper':10, 'Pokey Stick':10, 'Plastic Knife':10, 'Pointy Stick':10, 'Book on a Stick':10, 'Stretchy String':10, 'Little Toy Bow':10, 'Useful Pebble':10, 'Pokey Stick':10, 'Bibbity Bobbity Boo':10, 'Paper Shield':10, 'Paper Gloves':10, 'Paper Bracelet':10, 'Paper Armor':10, 'Paper Clothes':10, 'Paper Robe':10, 'Paper Helm':10, 'Paper Hat':10, 'Paper Circlet':10, 'Apple':4, 'Miracle':0, 'Sticks & Stones':6}

class EquipmentStat:
    def __init__(self, maxstat): 
        self.max = maxstat
        self.current = maxstat

class WeaponMaker:
    def __init__(self, strength = 1, ranges = [1], maxdur = 20, acc = 85, defense = 0, magicdefense = 0, speed = 0, wtype = 'Sword', crit = 0): #image
        self.attack = strength
        self.critical = crit
        self.accuracy = acc

        self.defense = defense
        self.magicdefense = magicdefense
        self.speed = speed

        self.range = ranges
        self.used = 0
        self.durability = maxdur
        self.broken = False
        self.type = wtype

class ArmorMaker:
    def __init__(self, strength = 0, defense = 1, magicdefense = 1, speed = 0, maxdur = 20, atype = 'Clothes'): #image
        self.attack = strength

        self.defense = defense
        self.magicdefense = magicdefense
        self.speed = speed

        self.used = 0
        self.durability = maxdur
        self.broken = False
        self.type = atype
#        self.


# weapon types = Sword, Spear, Axe; Bow, Throwing; Staff, Wand; Whip, Dagger
# armor types = Shield, Glove, Bracelet, Armor, Clothes, Robe, Helm, Hat, Circlet

weapons = {'None':WeaponMaker(0, [1], 0, wtype = 'None'), 'Sheet of Paper':WeaponMaker(1, [1], wtype = 'Sword'), 'Plastic Knife':WeaponMaker(1, [1], wtype = 'Dagger'), 'Pointy Stick':WeaponMaker(1, [1], wtype = 'Spear'), 'Book on a Stick':WeaponMaker(1, [1], wtype = 'Axe'), 'Stretchy String':WeaponMaker(1, [-1, 1], wtype = 'Whip'), 'Little Toy Bow':WeaponMaker(1, [2], wtype = 'Bow'), 'Useful Pebble':WeaponMaker(1, [1, 2], wtype = 'Throwing'), 'Pokey Stick':WeaponMaker(1, [1], wtype = 'Staff'), 'Bibbity Bobbity Boo':WeaponMaker(1, [1, 2], wtype = 'Spell')}

armors = {'None':ArmorMaker(0, 0, atype = 'None'), 'Paper Shield':ArmorMaker(1, atype = 'Shield'), 'Paper Gloves':ArmorMaker(1, atype = 'Gloves'), 'Paper Bracelet':ArmorMaker(1, atype = 'Bracelet'), 'Paper Armor':ArmorMaker(1, atype = 'Armor'), 'Paper Clothes':ArmorMaker(1, atype = 'Clothes'), 'Paper Robe':ArmorMaker(1, atype = 'Robe'), 'Paper Helm':ArmorMaker(1, atype = 'Helm'), 'Paper Hat':ArmorMaker(1, atype = 'Hat'), 'Paper Circlet':ArmorMaker(1, atype = 'Circlet')}

def equiptype(name):
    if name == 'None':
        return 0
    if name in weapons.keys():
        return 1
    if name in armors.keys():
        return 2
        
    return 3        

class Weapon:
    def __init__(self, weapon):
        self.name = weapon
        self.attack = EquipmentStat(weapons[weapon].attack)
        self.accuracy = EquipmentStat(weapons[weapon].accuracy)
        self.durability = EquipmentStat(weapons[weapon].durability)

        self.defense = EquipmentStat(weapons[weapon].defense)
        self.magicdefense = EquipmentStat(weapons[weapon].magicdefense)
        self.speed = EquipmentStat(weapons[weapon].speed)

        self.range = weapons[weapon].range
        self.type = weapons[weapon].type
        self.critical = weapons[weapon].critical
        self.used = 0
        self.broken = False

#        self.equipped = False

    def use(self):
        if not self.broken:
            self.durability.current -= 1
            if self.durability.current == 0:
                self.broken = True
                self.attack.current /= 2
                self.accuracy.current /= 2

                self.defense.current = 0
                self.magicdefense.current = 0
                self.speed.current = 0
            self.used += 1

    def repair(self):
        self.durability.current = self.durability.max

        if self.broken:
            self.broken = False
            self.attack.current = self.attack.max
            self.accuracy.current = self.accuracy.max

            self.defense.current = self.defense.max
            self.magicdefense.current = self.magicdefense.max
            self.speed.current = self.speed.max

#    def equip(self, character):
#        self.equipped = 
        
class Armor:
    def __init__(self, armor): #image
        self.name = armor
        self.defense = EquipmentStat(armors[armor].defense)
        self.magicdefense = EquipmentStat(armors[armor].magicdefense)

        self.attack = EquipmentStat(armors[armor].attack)
        self.magicattack = EquipmentStat(armors[armor].defense)
        self.speed = EquipmentStat(armors[armor].speed)

        self.used = 0
        self.durability = EquipmentStat(armors[armor].durability)
        self.broken = False
        self.type = armors[armor].type

#        self.equipped = False
#        self.

    def use(self):
        if not self.broken:
            self.durability.current -= 1
            if self.durability == 0:
                self.broken = True
                self.defense.current /= 2
                self.magicdefense.current /= 2

                self.attack.current = 0
                self.magicattack.current = 0
                self.speed.current = 0
            self.used += 1

    def repair(self):
        self.durability.current = self.durability.max

        if self.broken:
            self.broken = False
            self.attack.current = self.attack.max
            self.magicattack.current = self.attack.max

            self.defense.current = self.defense.max
            self.magicdefense.current = self.magicdefense.max
            self.speed.current = self.speed.max

