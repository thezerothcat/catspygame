import pygame
import random
import Finder
import Cell
import Map
import Stats
import Paths
import Menu
import Items
import Classes
#import Attacks
from Equipment import Weapon
from Equipment import Armor
from Equipment import equiptype
from Paths import *

#state 0 = none, 1 = moving, 2 = acting, 3 = moved, 4 = acted, 5 = moved + acting, 6 = acted + moving, 7 = done


########################################################
#		   Living CellObject		       #
########################################################

class Actor:
    def __init__(self, name, image, pos, stats, items = [], eqp = [], wpn = 'None', armr = 'None', deathexp = 10, cls = 'Knight'):
        self.name = name
        self.exp = 0
        self.deathexp = deathexp
        self.type = 'actor'
        self.imagename = 'images/actors/'+image
        self.image = pygame.image.load(self.imagename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.speed = 4
        self.stats = stats
        self.friends = 1
        self.validpaths = PathSet(Path(Point(self.rect.x, self.rect.y)))
        self.validtargets = []
        self.effects = []
        self.alive = True
        self.hadturn = False
        self.state = 1
        self.moving = False
        self.acted = False
        self.attacking = False
        self.weapon = Weapon('None')
        self.armor = Armor('None')
        self.critical = Classes.classcrits[cls]

        self.equipment = []
        for thing in eqp:
            if equiptype(thing) == 1:
                self.equipment.append(Weapon(thing))
            elif equiptype(thing) == 2:
                self.equipment.append(Armor(thing))

        self.items = []
        for thing in items:
            self.items.append(thing)

        self.classname = cls
        self.equippable = []

        for thing in Classes.classequips[cls]:
            self.equippable.append(thing)

        if wpn != 'None':           
            inst = Weapon(wpn)
            self.equipment.append(inst)
            if inst.type in self.equippable:
            # equip the weapon
                self.weapon = inst

        if armr != 'None':           
            inst2 = Armor(armr)
            self.equipment.append(inst2)
            if inst2.type in self.equippable:
            # equip the weapon
                self.armor = inst2



########################################################
#		             Enemy CellObject		           #
########################################################

class Enemy:
    def __init__(self, name, image, pos, stats, friends, items = [], eqp = [], wpn = 'None', armr = 'None', deathexp = 20, cls = 'Knight'):
        self.name = name
        self.exp = 0
        self.deathexp = deathexp
        self.type = 'actor'
        self.imagename =  'images/actors/'+image
        self.image = pygame.image.load(self.imagename).convert_alpha()
        self.alive = True
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.speed = 2
        self.stats = stats
        self.friends = friends
        self.validpaths = PathSet(Path(Point(self.rect.x, self.rect.y)))
        self.validtargets = {}
        self.items = items
        self.equipment = eqp
        self.effects = []
        self.weapon = Weapon('None')
        self.armor = Armor('None')
        self.critical = Classes.classcrits[cls]

        self.classname = cls
        self.equippable = []
        for thing in Classes.classequips[cls]:
            self.equippable.append(thing)

        if wpn != 'None':           
            inst = Weapon(wpn)
            self.equipment.append(inst)
            if inst.type in self.equippable:
            # equip the weapon
                self.weapon = inst

        if armr != 'None':           
            inst2 = Armor(armr)
            self.equipment.append(inst2)
            if inst2.type in self.equippable:
            # equip the weapon
                self.armor = inst2

    def equipweapon(self, wpn):
        if wpn.type in self.equippable:
            self.weapon = wpn
            return True
        return False

    def unequipweapon(self):
        self.weapon = Weapon('None')

    def equiparmor(self, armr):
        if armr.type in self.equippable:
            self.armor = armr
            return True
        return False

    def unequiparmor(self):
        self.armor = Armor('None')

    def picklefix(self):
        self.image = None
#        if self.weapon != None:
#            self.weapon.image = None
#        if self.armor != None:
#            self.armor.image = None
        # for equipment in equipments:
            # equipment.image = None

    def unpicklefix(self):
        self.image = pygame.image.load(self.imagename).convert_alpha()
#        if self.weapon != None:
#            self.weapon.image = pygame.image.load(self.weapon.imagename).convert_alpha()
#        if self.armor != None:
#            self.armor.image = pygame.image.load(self.armor.imagename).convert_alpha()
        # for equipment in equipments:
            # equipment.image = pygame.image.load(equipment.imagename).convert_alpha()

    def prepare(self, screen, cmap):
        self.validpaths = PathSet(Path(Point(self.rect.x, self.rect.y)))
        self.validtargets = {}
        for effect in self.effects:
            effect.turn(screen, cmap)

    def drawTravel(self, screen, cmap, thispath):
        cmap.cells[(self.rect.x, self.rect.y)].removeobject()
        index = 1
        while (self.rect.x, self.rect.y) != (thispath[-1].x, thispath[-1].y):
            pos = Point(self.rect.x, self.rect.y)
            while (self.rect.x, self.rect.y) != (thispath[index].x, thispath[index].y):
                if self.rect.x != thispath[index].x:
                     if self.rect.x < thispath[index].x:
                        self.rect.x += self.speed
                     elif self.rect.x > thispath[index].x:
                        self.rect.x -= self.speed
                elif self.rect.y != thispath[index].y:
                    if self.rect.y < thispath[index].y:
                        self.rect.y += self.speed
                    elif self.rect.y > thispath[index].y:
                        self.rect.y -= self.speed
                cmap.cells[(pos.x, pos.y)].draw(screen)
                cmap.cells[(thispath[index].x, thispath[index].y)].draw(screen)
                screen.blit(self.image, self.rect)
                pygame.display.flip()	
            index += 1
        cmap.cells[(self.rect.x, self.rect.y)].addobject(self)
        return True

    def die(self, screen, cmap):
        spot = cmap.cells[(self.rect.topleft)]
        spot.removeobject()
        spot.draw(screen)
        self.alive = False
        cmap.enemies.remove(self)
        pygame.display.flip()
        del self

#    def drawattack(self, screen, attack):
#        spotrect = pygame.Rect(64, 64, 64, 64)
#        spot = screen.subsurface(spotrect)
#        images = 
#        for image in Attacks.images[attack]:
#            screen.blit(imagerect, image

    def attack(self, target, screen, cmap):
        if self.targetok(target, cmap) and target.alive:
            accuracy = self.weapon.accuracy.current  + self.stats.skill.current * 3 - target.stats.speed.current * 2 - target.weapon.speed.current * 2 - target.armor.speed.current * 2
            i = random.randrange(0, 100)
            if i < accuracy:
                return target.takedamage(screen, cmap, enemy = self)
            else:
                return 1
        return 0


    def battle(self, target, screen, cmap):
        speeddiff = (self.stats.speed.current + self.weapon.speed.current + self.armor.speed.current) - (target.stats.speed.current + target.weapon.speed.current + target.armor.speed.current)

        bonus = self.attack(target, screen, cmap)
        while speeddiff > 3:
            b2 = self.attack(target, screen, cmap)
            if bonus < b2:
                bonus = b2
            speeddiff -= 4
        self.grow(bonus)

        if target.alive:
            speeddiff = -1 * ((self.stats.speed.current + self.weapon.speed.current + self.armor.speed.current) - (target.stats.speed.current + target.weapon.speed.current + target.armor.speed.current))
    
            target.attack(self, screen, cmap)
            while speeddiff > 3:
                target.attack(self, screen, cmap)
                speeddiff -= 4

    def targetok(self, target, cmap):
        x = abs((target.rect.x - self.rect.x) / cmap.cellsize)
        y = abs((target.rect.y - self.rect.y) / cmap.cellsize)

        if x in self.weapon.range and y == 0:
            return True
        elif y in self.weapon.range and x == 0:
            return True
        elif x == y and -x in self.weapon.range:
            return True
        return False


    def grow(self, exp):
        levelup = 0
        while exp > 0:
            self.exp += 1
            if self.exp == 100:
                levelup += 1
                self.exp = 0
            # draw exp increase
            exp -= 1
        while levelup > 0:
            self.level()
            levelup -= 1

    def level(self):
        if self.stats.level < 20:
            self.stats.level += 1
            if self.stats.hp.max  < self.stats.hp.cap:
                if random.randrange(0, 100) < self.stats.hp.growth:
                    self.stats.hp.max += 1
                    self.stats.hp.current += 1
            if self.stats.attack.max  < self.stats.attack.cap:
                if random.randrange(0, 100) < self.stats.attack.growth:
                    self.stats.attack.max += 1
                    self.stats.attack.current += 1
            if self.stats.magicattack.max  < self.stats.magicattack.cap:
                if random.randrange(0, 100) < self.stats.magicattack.growth:
                    self.stats.magicattack.max += 1
                    self.stats.magicattack.current += 1
            if self.stats.defense.max  < self.stats.defense.cap:
                if random.randrange(0, 100) < self.stats.defense.growth:
                    self.stats.defense.max += 1
                    self.stats.defense.current += 1
            if self.stats.magicdefense.max  < self.stats.magicdefense.cap:
                if random.randrange(0, 100) < self.stats.magicdefense.growth:
                    self.stats.magicdefense.max += 1
                    self.stats.magicdefense.current += 1
            if self.stats.skill.max  < self.stats.skill.cap:
                if random.randrange(0, 100) < self.stats.skill.growth:
                    self.stats.skill.max += 1
                    self.stats.skill.current += 1
            if self.stats.speed.max  < self.stats.speed.cap:
                if random.randrange(0, 100) < self.stats.speed.growth:
                    self.stats.speed.max += 1
                    self.stats.speed.current += 1

    def takedamage(self, screen, cmap, enemy = None, damage = None):
        if enemy != None:
            if enemy.weapon.type == 'Staff':
                atk = (enemy.stats.attack.current + enemy.stats.magicattack.current + enemy.armor.attack.current + enemy.armor.magicattack.current) / 2 + enemy.weapon.attack.current
                defense = (self.stats.defense.current + self.stats.magicdefense.current + self.armor.defense.current + self.armor.magicdefense.current +  self.weapon.defense.current + self.weapon.magicdefense.current) / 2
            elif enemy.weapon.type == 'Spell':
                atk = enemy.stats.magicattack.current + enemy.weapon.attack.current + enemy.armor.magicattack.current
                defense = self.stats.magicdefense.current + self.armor.magicdefense.current
            else:
                atk = enemy.stats.attack.current + enemy.weapon.attack.current
                defense = self.stats.defense.current + self.armor.defense.current
            enemy.weapon.use()
            self.armor.use()

            # enemy.critical is class bonus
            critical = enemy.stats.skill.current / 2 + enemy.weapon.critical + enemy.critical
            if random.randrange(0, 100) < critical:
                atkpower = atk * 2
            else:
                atkpower = atk - defense

            if atkpower < 0:
                atkpower = 0
            self.stats.hp.current -= atkpower
            if self.stats.hp.current <= 0:
                self.stats.hp.current = 0
                self.die(screen, cmap)
                return self.experience(enemy) + self.deathexp
            return self.experience(enemy)
        elif damage != None:
            self.stats.hp.current -= damage
            if self.stats.hp.current <= 0:
                self.stats.hp.current = 0
                self.die(screen, cmap)
                return 20
            return 10

    def experience(self, attacker): # screen is for later
        exp = 2 * (self.stats.level - attacker.stats.level) + 10
        if exp < 1:
            exp = 1
        return exp

    def heal(self, power, screen):  # screen is for future graphics improvement
        self.stats.hp.current += power
        if self.stats.hp.current > self.stats.hp.max:
            self.stats.hp.current = self.stats.hp.max

    def turn(self, screen, cmap):
        self.validpaths = PathSet(Path(Point(self.rect.x, self.rect.y)))
        self.validtargets = {}
        self.validpaths.addpoints(self.stats.moverange, cmap)

        self.validtargets = Finder.attacks(self, cmap, Point(self.rect.x, self.rect.y))
        goodtargets = self.validtargets.keys()
        if len(goodtargets) < 1:
# for now, if the comp can't attack anyone it will stay put
#			Paths2 = PathSet(Path(Point(self.rect.x,
#			for apath in self.validpaths:
#				paths2 = 
            screen.blit(cmap.cells[(self.rect.x, self.rect.y)].image, self.rect)
            screen.blit(self.image, self.rect)
            pygame.display.update(self.rect)
            return 0
        besttarget = goodtargets[0]
        strength = self.stats.attack.current
        if self.weapon != None:
            strength += self.weapon.attack.current
        for target in goodtargets:
# not putting the friend check here means that human players are not allowed to attack friends
                damage = strength - target.stats.defense.current
                if target.stats.hp.current - damage <= 0:
                    if besttarget.stats.hp.current - damage <= 0:
                        if besttarget.stats.hp.current > target.stats.hp.current:                    
                            besttarget = target
                    else:
                        besttarget = target
                elif (strength - besttarget.stats.defense.current) < damage:
                    besttarget = target
                        
        goodpath = Path(Point(0,0))
        goodpath.poplast()
        apath = self.validtargets[besttarget]
        for apoint in apath:
            goodpath.add(Point(apoint.x, apoint.y))
        #used to be an if statement
        self.drawTravel(screen, cmap, goodpath)
        self.battle(besttarget, screen, cmap)
        return 0

########################################################
#		           Obstacle CellObjects		           #
########################################################

class Mountain:
    def __init__(self, pos):
        self.type = 'object'
        self.image = pygame.image.load('images/objects/mountain.png').convert_alpha()
        self.alive = False
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class Rock:
    def __init__(self, pos):
        self.type = 'object'
        self.image = pygame.image.load('images/objects/rock.png').convert_alpha()
        self.alive = False
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class PineTree:
    def __init__(self, pos):
        self.type = 'object'
        self.image = pygame.image.load('images/objects/pinetree.png').convert_alpha()
        self.alive = False
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

########################################################
#	       Non-Obstacle CellObjects (Contents2)        #
########################################################

class AppleTree:
    def __init__(self, pos):
        self.image = pygame.image.load("images/objects/appletree.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.alive = False
        self.harvested = False
        self.type = 'plant'
        self.food = 'Apple'

    def harvest(self, harvester, screen, cmap):
        if not self.harvested:
            self.harvested = True
            self.image = pygame.image.load("images/objects/tree.png").convert_alpha()
            cmap.cells[self.rect.topleft].draw(screen)
            pygame.display.update(self.rect)
            harvester.items.append(self.food)
            #give person fruit

class TreasureChest:
    def __init__(self, pos, item = 'Apple'):
        self.image = pygame.image.load('images/objects/chest.png').convert_alpha()
        self.alive = False
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.type = 'treasure'
        self.item = item

    def open(self, opener, screen, cmap):
        opener.items.append(self.item)
        chestcell = cmap.cells[self.rect.topleft]
        chestcell.contents2 = None
        chestcell.draw(screen)
        pygame.display.update(self.rect)

class House:
    def __init__(self, pos, event = None):
        self.image = pygame.image.load('images/objects/house.png').convert_alpha()
        self.alive = False
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.type = 'house'
        self.visited = False
        self.event = event
#       self.event = None

    def visit(self, visitor, screen, cmap):
        if self.event == None:
            return False
        else:
            self.event.happen(visitor, screen, cmap)
      
class VBridge:
    def __init__(self, pos):
        self.type = 'bridge'
        self.image = pygame.image.load('images/objects/vbridge.png').convert_alpha()
        self.alive = False
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
                
class HBridge:
    def __init__(self, pos):
        self.type = 'bridge'
        self.image = pygame.image.load('images/objects/hbridge.png').convert_alpha()
        self.alive = False
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


