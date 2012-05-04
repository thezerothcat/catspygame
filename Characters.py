import pygame
import CellObject
import random
import Finder
import Cell
import Map
import Stats
import Paths
import Menu
import Items
import PlayerScreen
import Classes
import Stats
from Equipment import Weapon
from Equipment import Armor
from Paths import *

#name is currently not changeable; this is a problem
#game save message is cut off
#repair function? how does that work?

chargen = {'Hero':CellObject.Actor('Hero', 'smiley.png', (-100, -100), Stats.Stats(15, 6, 0, 4, 3, 3, 3, 5), items = ['Apple'], wpn = 'Stretchy String', armr = 'Paper Hat'), 'Kamikaze':CellObject.Actor('Kamikaze', 'tophatsmiley.png', (-20, -20), Stats.Stats(10, 3, 14, 0, 0, 6, 2, 5), wpn = 'Bibbity Bobbity Boo', cls = 'Magician')}

chargen = {'Hero':CellObject.Actor('Hero', 'smiley.png', (-100, -100), Stats.Stats(15, 6, 0, 4, 3, 3, 3, 5), items = ['Apple'], wpn = 'Stretchy String', armr = 'Paper Hat'), 'Kamikaze':CellObject.Actor('Kamikaze', 'tophatsmiley.png', (-20, -20), Stats.Stats(10, 3, 14, 0, 0, 6, 2, 5), wpn = 'Bibbity Bobbity Boo', cls = 'Magician')}

class Character:
    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.deathexp = chargen[name].deathexp
        self.type = 'actor'
        self.imagename = chargen[name].imagename
        self.image = chargen[name].image
        self.rect = chargen[name].rect
        self.speed = 4
        self.stats = Stats.Stats(chargen[name].stats.hp.max, chargen[name].stats.attack.max,  chargen[name].stats.magicattack.max, chargen[name].stats.defense.max, chargen[name].stats.magicdefense.max, chargen[name].stats.skill.max, chargen[name].stats.speed.max, chargen[name].stats.moverange)
        self.friends = 1
        self.validpaths = chargen[name].validpaths
        self.validtargets = chargen[name].validtargets
        self.items = chargen[name].items
        self.equipment = chargen[name].equipment
        self.effects = []
        self.alive = True
        self.hadturn = False
        self.moved = False
        self.moving = False
        self.acted = False
        self.attacking = False
        self.classname = chargen[name].classname
        self.equippable = []
        self.critical = chargen[name].critical

        for thing in Classes.classequips[self.classname]:
            self.equippable.append(thing)

        self.weapon = chargen[name].weapon
        self.armor = chargen[name].armor

        self.equippable = chargen[name].equippable

        self.equipment = chargen[name].equipment
    

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

    def removeequipment(self, thing):
        if thing == self.weapon:
            self.weapon = Weapon('None')
        if thing == self.armor:
            self.armor = Armor('None')
        self.equipment.remove(thing)

    def turn(self, screen, cmap):
        # set up active cell 
        cell = cmap.cells[(self.rect.x, self.rect.y)]
        cell.active = True
        cell.draw(screen)
        cmap.menu.info(screen, cell.contents)
        pygame.display.update(cell.rect)

        # for undo option
        startcell = cmap.cells[self.rect.topleft]

        # begin character turn loop
        item = None
        #until I find a better way to prevent the 'get-item-and-go-back' abuse potential
        spacebarred = False

        while True:
            z = cmap.victorycheck()
            if z != 0:
                return z
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_BACKSPACE]:
                        cell.active = False
                        cell.draw(screen)
    
                        if self.moving:
                            for path in self.validpaths:
                                last = cmap.cells[(path[-1].x, path[-1].y)]
                                last.blue = False
                                last.draw(screen)
                            self.moving = False
                            cell = cmap.cells[self.rect.topleft]
                            cell.active = True
                            cell.draw(screen)
                            pygame.display.update()
                            cmap.menu.info(screen, self)
                        elif self.attacking:
                            for target in self.validtargets:
                                square = cmap.cells[target.rect.topleft]
                                square.red = False
                                square.draw(screen)
                            self.attacking = False
                            self.validtargets = []
                            cell = cmap.cells[self.rect.topleft]
                            cell.active = True        
                            cell.draw(screen)
                            pygame.display.update()
                            cmap.menu.info(screen, self)
                        elif item != None:
                            for target in item.targets:
                                target.active = False
                                target.red = False
                                target.draw(screen)
                            item = None
                            cell = cmap.cells[self.rect.topleft]
                            cell.active = True
                            cell.draw(screen)
                            pygame.display.update()
                            # ???
                            cmap.menu.inventory(screen, self)
                        elif self.moved and not spacebarred and not self.acted:# and not self.skipped:
                            cmap.menu.message = None
                            last = cmap.cells[self.rect.topleft]
                            last.removeobject()
                            last.draw(screen)
                            self.rect.topleft = startcell.rect.topleft
                            self.moved = False
                            startcell.addobject(self)
                            startcell.draw(screen)
                            cell = startcell
                            cell.active = True
                            cell.draw(screen)
                            cmap.menu.info(screen, self)
                            pygame.display.update()
                        else: # if not self.moved and not self.acted:
#                            self.skipped = True
                            cmap.menu.message = None
                            pygame.display.update(cell.rect)
                            return 0
                    elif keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        if keys[pygame.K_LEFT]:
                            if item == None or (item != None and not item.effect.multi):
                                if cell.rect.x - cmap.cellsize >= 0:
                                    cell.active = False
                                    cell.draw(screen)
                                    cell = cmap.cells[(cell.rect.x - cmap.cellsize, cell.rect.y)]
                                    cell.active = True
                                    cell.draw(screen)
                                    pygame.display.update(pygame.Rect(cell.rect.topleft, (cmap.cellsize * 2, cmap.cellsize)))			
                            elif item.effect.multi:
                                for target in item.targets:
                                    target.red = False
                                    target.active = False
                                    target.draw(screen)
                                    item.gettargets(self, screen, cmap)
                                    if len(item.targets) < 1:
                                        item.gettargets(self, screen, cmap)
                                pygame.display.update()
                        elif keys[pygame.K_RIGHT]:
                            if item == None or (item != None and not item.effect.multi):
                                if cell.rect.x + cmap.cellsize <= 288:
                                    cell.active = False
                                    cell.draw(screen)
                                    cell = cmap.cells[(cell.rect.x + cmap.cellsize, cell.rect.y)]
                                    cell.active = True
                                    cell.draw(screen)
                                    pygame.display.update(pygame.Rect(cell.rect.x - cmap.cellsize, cell.rect.y, cmap.cellsize * 2, cmap.cellsize))
                            elif item.effect.multi:
                                for target in item.targets:
                                    target.red = False
                                    target.active = False
                                    target.draw(screen)
                                    item.gettargets(self, screen, cmap)
                                    if len(item.targets) < 1:
                                        item.gettargets(self, screen, cmap)
                                pygame.display.update()
                        elif keys[pygame.K_UP]:
                            if item == None or (item != None and not item.effect.multi):
                                if cell.rect.y - cmap.cellsize >= 0:
                                    cell.active = False
                                    cell.draw(screen)
                                    cell = cmap.cells[(cell.rect.x, cell.rect.y - cmap.cellsize)]
                                    cell.active = True
                                    cell.draw(screen)
                                    pygame.display.update(pygame.Rect(cell.rect.topleft, (cmap.cellsize, cmap.cellsize * 2)))			
                            elif item.effect.multi:
                                for target in item.targets:
                                    target.red = False
                                    target.active = False
                                    target.draw(screen)
                                    item.gettargets(self, screen, cmap)
                                    if len(item.targets) < 1:
                                        item.gettargets(self, screen, cmap)
                                pygame.display.update()
                        elif keys[pygame.K_DOWN]:
                            if item == None or (item != None and not item.effect.multi):
                                if cell.rect.y + cmap.cellsize <= 288:
                                    cell.active = False
                                    cell.draw(screen)
                                    cell = cmap.cells[(cell.rect.x, cell.rect.y + cmap.cellsize)]
                                    cell.active = True
                                    cell.draw(screen)
                                    pygame.display.update(pygame.Rect(cell.rect.x, cell.rect.y - cmap.cellsize, cmap.cellsize, cmap.cellsize * 2))
                            elif item.effect.multi:
                                for target in item.targets:
                                    target.red = False
                                    target.active = False
                                    target.draw(screen)
                                    item.gettargets(self, screen, cmap)
                                    if len(item.targets) < 1:
                                        item.gettargets(self, screen, cmap)
                                pygame.display.update()

                        thing = cell.contents
                        if thing == None:
                            cmap.menu.display(screen)
                        elif thing.alive:
                            if thing == self and cmap.menu.message != None:
                                cmap.menu.display(screen)
                            else:
                                cmap.menu.info(screen, thing)
                        else:
                            cmap.menu.display(screen)
                        pygame.display.update(pygame.Rect(0, 320, 320, 64))
                    elif keys[pygame.K_SPACE]:
                        c = cmap.cells[self.rect.topleft].contents2 
                        if c != None:
                            if c.type == 'treasure':
                                c.open(self, screen, cmap)
                                spacebarred = True
                                cmap.menu.message = False
                                cmap.menu.display(screen)
                            if c.type == 'house':
                                c.visit(self, screen, cmap)
                                spacebarred = True
                                cmap.menu.message = False
                                cmap.menu.display(screen)                                    
                            if c.type == 'plant':
                                c.harvest(self, screen, cmap)
                                spacebarred = True
                                cmap.menu.message = False
                                cmap.menu.display(screen)
                            cmap.menu.message = None
                    elif keys[pygame.K_RETURN]:
                        if not self.moving and not self.attacking and item == None:
                            cell.active = False
                            cell.draw(screen)
                            cell = cmap.cells[self.rect.topleft]
                            cell.active = True
                            cell.draw(screen)
                            pygame.display.update()
							
                            choice = cmap.menu.showmenu(screen, self)

                            if choice == 1: # move
                                self.validpaths.addpoints(self.stats.moverange, cmap)
                                for path in self.validpaths:
                                    last = cmap.cells[(path[-1].x, path[-1].y)]
                                    last.blue = True
                                    last.draw(screen)
                                pygame.display.flip()
                                self.moving = True
                            elif choice == 2:  # attack
                                self.findTargets(cmap)

                                if len(self.validtargets) >= 1:
                                    self.attacking = True

                                    for target in self.validtargets:
                                        last = cmap.cells[(target.rect.topleft)]
                                        last.red = True
                                        last.draw(screen)
                                    if len(self.validtargets) == 1:
                                        cell.active = False
                                        cell.draw(screen)
                                        cell = cmap.cells[(self.validtargets[0].rect.topleft)]
                                        cell.active = True
                                        cell.draw(screen)
                                    pygame.display.flip()
                            elif choice == 3: # items
                                select = cmap.menu.inventory(screen, self)
                                if select != -1:
                                    item = Items.items[self.items[select]]
                                    item.gettargets(self, screen, cmap)
                                    pygame.display.update()
                                else:
                                    cmap.menu.info(screen, self)
                            elif choice == 4: # wait
                                self.moved = True
                                self.acted = True
                                cmap.menu.display(screen)
                                cmap.menu.message = None
                        elif self.moving:
                            where = Point(cell.rect.x, cell.rect.y)
                            if self.move(screen, cmap, where, False):
                                for path in self.validpaths:
                                    last = cmap.cells[(path[-1].x, path[-1].y)]
                                    last.blue = False
                                    last.draw(screen)
                                if self.move(screen, cmap, where, True):
                                    cell.active = False
                                    cell.draw(screen)
                                    pygame.display.update()
                                    self.moving = False
                                    self.moved = True

                                    c = cmap.cells[self.rect.topleft].contents2 
                                    if c != None:
                                        if c.type == 'treasure':
                                            cmap.menu.treasure(screen)
                                        elif c.type == 'house':
                                            cmap.menu.location(screen)
                                        elif c.type == 'plant':
                                             cmap.menu.plant(screen)
                                    else:
                                        cmap.menu.info(screen, self)
                                    if self.acted:
                                        self.hadturn = True
                                        cell.active = False
                                        cell.draw(screen)
                                        pygame.display.update(cell.rect)
                                        cmap.menu.message = None
                                        return 0
                                    cell = cmap.cells[self.rect.topleft]
                                    cell.active = True
                                    cell.draw(screen)
                                    pygame.display.update(cell.rect)                                    
                        elif self.attacking:
                            if self.targetok(cell.contents, cmap):
                                cell.active = False
                                cell.draw(screen)

                                for target in self.validtargets:
                                    square = cmap.cells[target.rect.topleft]
                                    square.red = False
                                    square.draw(screen)
                                targetcell = cell
                                # eventually attack will catch the update
                                pygame.display.update()                                    

                                self.battle(targetcell.contents, screen, cmap)
                                self.attacking = False
                                self.acted = True
                                self.validtargets = []
                                if self.moved:
                                    self.hadturn = True
                                    cell.active = False
                                    cell.draw(screen)
                                    pygame.display.update(cell.rect)
                                    cmap.menu.message = None
                                    return 0
                                cell = cmap.cells[self.rect.topleft]
                                cell.active = True
                                cell.draw(screen)
                                cmap.menu.info(screen, self)
                                pygame.display.update(cell.rect)                                    
                        elif item != None:
                            targets = []
                            if item.effect.multi:
                                for place in item.targets:
                                    if place.active:
                                        targets.append(place)
                            else:
                                if cell in item.targets:
                                    targets.append(cell)
                            if len(targets) > 0:
                                cell.active = False
                                cell.draw(screen)

                                for square in item.targets:
#                                        square = cmap.cells[target.rect.topleft]
                                    square.red = False
                                    square.active = False
                                    square.draw(screen)
                                item.use(targets, screen, cmap)
                                self.items.remove(item.name)
                                item = None
                                self.acted = True
                                if self.moved:
                                    self.hadturn = True
                                    cell.active = False
                                    cell.draw(screen)
                                    pygame.display.update(cell.rect)
                                    cmap.menu.message = None
                                    return 0
                                cell = cmap.cells[self.rect.topleft]
                                cell.active = True
                                cell.draw(screen)
                                cmap.menu.info(screen, self)
                                pygame.display.update()
                                                                                        
                        if self.moved and self.acted:
                            self.hadturn = True
                            cell.active = False
                            cell.draw(screen)
                            pygame.display.update(cell.rect)
                            return 0
                    elif keys[pygame.K_ESCAPE]:
                        temp = screen.copy()
                        view = PlayerScreen.PlayerScreen(1)
#                        view.disabled.append(0)
#                        view.disabled.append(3)
#                        view.disabled.append(4)
#                        view.disabled.append(5)
                        if view.mainscreen(cmap.player1, screen) == -1:
                            return -1
                        screen.blit(temp, (0, 0))
                        pygame.display.flip()

    def prepare(self, screen, cmap):
        self.hadturn = False
        self.moved = False
        self.moving = False
        self.acted = False
        self.attacking = False
        self.validpaths = PathSet(Path(Point(self.rect.x, self.rect.y)))
        self.validtargets = []
        for effect in self.effects:
            effect.turn(screen, cmap)

    def die(self, screen, cmap):
        self.alive = False
        self.hadturn = True
        cmap.player1.characters.remove(self)
        spot = cmap.cells[(self.rect.topleft)]
        spot.contents = None
        spot.walkable = True
        spot.draw(screen)
        pygame.display.flip()
        del self
	
    def findTargets(self, cmap):
        for arange in self.weapon.range:
            if arange > 0:
                thisrange = arange * cmap.cellsize
                if (self.rect.x - thisrange >= 0):
                    t = cmap.cells[(self.rect.x - thisrange, self.rect.y)].contents
                    if t != None and t.alive == True and t.friends != self.friends:
                        self.validtargets.append(t) 
                if (self.rect.y - thisrange >= 0):
                    t = cmap.cells[(self.rect.x, self.rect.y - thisrange)].contents
                    if t != None and t.alive == True and t.friends != self.friends:
                        self.validtargets.append(t) 
                if(self.rect.x + thisrange <= 288):
                    t = cmap.cells[(self.rect.x + thisrange, self.rect.y)].contents
                    if t != None and t.alive == True and t.friends != self.friends:
                        self.validtargets.append(t) 
                if (self.rect.y + thisrange <= 288):
                    t = cmap.cells[(self.rect.x, self.rect.y + thisrange)].contents
                    if t != None and t.alive == True and t.friends != self.friends:
                        self.validtargets.append(t) 
            else:
                if arange == -1:
                    thisrange = cmap.cellsize
                    if (self.rect.x - thisrange >= 0) and (self.rect.y - thisrange >= 0): # top left
                        t = cmap.cells[(self.rect.x - thisrange, self.rect.y - thisrange)].contents
                        if t != None and t.alive == True and t.friends != self.friends:
                            self.validtargets.append(t) 
                    if (self.rect.x + thisrange <= 288) and (self.rect.y - thisrange >= 0): # top right
                        t = cmap.cells[(self.rect.x + thisrange, self.rect.y - thisrange)].contents
                        if t != None and t.alive == True and t.friends != self.friends:
                            self.validtargets.append(t) 
                    if(self.rect.x + thisrange <= 288) and (self.rect.y + thisrange <= 288): # bottom right
                        t = cmap.cells[(self.rect.x + thisrange, self.rect.y + thisrange)].contents
                        if t != None and t.alive == True and t.friends != self.friends:
                            self.validtargets.append(t) 
                    if (self.rect.x - thisrange >= 0) and (self.rect.y + thisrange <= 288): # bottom left
                        t = cmap.cells[(self.rect.x - thisrange, self.rect.y + thisrange)].contents
                        if t != None and t.alive == True and t.friends != self.friends:
                            self.validtargets.append(t) 

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




    def battle(self, target, screen, cmap):
        speeddiff = (self.stats.speed.current + self.weapon.speed.current + self.armor.speed.current) - (target.stats.speed.current + target.weapon.speed.current + target.armor.speed.current)

        bonus = self.attack(target, screen, cmap)
        while speeddiff > 3:
            b2 = self.attack(target, screen, cmap)
            if bonus < b2:
                bonus = b2
            speeddiff -= 4
        print '%d + %d' % (self.exp, bonus)
        self.grow(bonus)
        print self.exp

        if target.alive:
            speeddiff = -1 * ((self.stats.speed.current + self.weapon.speed.current + self.armor.speed.current) - (target.stats.speed.current + target.weapon.speed.current + target.armor.speed.current))
    
            target.attack(self, screen, cmap)
            while speeddiff > 3:
                target.attack(self, screen, cmap)
                speeddiff -= 4
        return True
	
    def attack(self, target, screen, cmap):
        if self.targetok(target, cmap) and target.alive:
            accuracy = self.weapon.accuracy.current + self.stats.skill.current * 3 - target.stats.speed.current * 2- target.weapon.speed.current * 2 - target.armor.speed.current * 2
            if random.randrange(0, 100) < accuracy:
                return target.takedamage(screen, cmap, enemy = self)
            else:
                return 1
        return 0

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
            # will later adjust these to have multi stats and only give back the right ones
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
#        print random.randrange(0, 100)
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

    def heal(self, power, screen): # screen is for future graphics improvement
        self.stats.hp.current += power
        if self.stats.hp.current > self.stats.hp.max:
            self.stats.hp.current = self.stats.hp.max

    def move(self, screen, cmap, dest, go):
        if dest.x < 0:
            return False
        if dest.y < 0:
            return False
		
        valid = False
        thispath = None
        for apath in self.validpaths:
            if (apath[-1].x, apath[-1].y) == (dest.x, dest.y):
                valid = True
                if thispath == None:				
                     thispath = apath
                elif len(thispath.points) > len(apath.points):
                     thispath = apath
        if valid == False:
            return False
        if go == False:
            return True
        if self.drawTravel(screen, cmap, dest, thispath):
            return True
        return False

    def drawTravel(self, screen, cmap, dest, thispath):
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

    def restore(self):
        self.stats.hp.current = self.stats.hp.max
        self.stats.attack.current = self.stats.attack.max
        self.stats.defense.current = self.stats.defense.max
        self.effects = []
        self.validtargets = []
        self.validpaths = []

    def picklefix(self):
        self.image = None

    def unpicklefix(self):
        self.image = pygame.image.load(self.imagename).convert_alpha()

#class Knight(Character):
#    def __init__(self, name):
#        super(name)

#class Magician(Character):
#    def __init__(self, name):
#        super(name)
#        self.spell = None

#Classes.classcrits[cls]
#    for thing in Classes.classequips[cls]:

    def send(self):
        data = {'name':self.name, 'exp':self.exp, 'deathexp':self.deathexp, 'type':self.type, 'imagename':self.imagename, 'rect':self.rect, 'stats':self.stats.send(), 'items':items, 'effects':effects, 'alive':self.alive, 'hadturn':self.hadturn, 'moved':self.moved, 'moving':self.moving, 'acted':self.acted, 'attacking':self.attacking, 'classname':self.classname, 'equippable':self.equippable, 'weapon':self.weapon.send(), 'armor':self.armor.send()}

        data['equipment'] = equipment



    def receive(self, data):
        self.speed = 4
        self.friends = 1

        self.name = data['name']
        

        self.weapon = chargen[name].weapon
        self.armor = chargen[name].armor

        self.equippable = chargen[name].equippable

        self.equipment = chargen[name].equipment


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
