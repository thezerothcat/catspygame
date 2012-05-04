#import CellObject
#import Stats

class SideEffect:
    def __init__(self, itype, power, ranges = [], stat = 1, duration = 0, delay = 0, percent = False, multi = False):
        # item type for use method
        self.type = itype
        self.stat = stat
        # power, either fixed or as percent of a stat
        self.power = power
        # boolean: power as percent or fixed value
        self.percent = percent
        # 0 = self, 1 = range 1, 2 = range 2, ..., 50 = range any
        self.ranges = ranges
        # multi allows for multiple targets; as many as are within range for now
        self.multi = multi

        # 1 = hp, 2 = attack, 3 = defense
        self.stat = stat
        # 0 = immediately ends
        self.duration = duration
        # default items will take effect instantly
        self.delay = delay
        self.durationtimer = 0
        self.delaytimer = 0
        self.attached = None

    def start(self, character, screen, mapcells):
        print 'sideEffect.start'
        validtargets = []
        for r in self.ranges:
            if r == 50:
                for cell in mapcells.cells.values():
                    if cell.contents != None and cell.contents.alive == True:
                        validtargets.append(cell)
            elif r == 0:
                validtargets.append(mapcells.cells[(character.rect.topleft)])
            else:
                thisrange = r * mapcells.cellsize
                if (character.rect.x - thisrange >= 0):
                    t = mapcells.cells[(character.rect.x - thisrange, character.rect.y)]
                    if t.contents != None and t.contents.alive == True:
                        validtargets.append(t) 
                if (character.rect.y - thisrange >= 0):
                    t = mapcells.cells[(character.rect.x, character.rect.y - thisrange)]
                    if t.contents != None and t.contents.alive == True:
                        validtargets.append(t) 
                if(character.rect.x + thisrange <= 288):
                    t = mapcells.cells[(character.rect.x + thisrange, character.rect.y)]
                    if t.contents != None and t.contents.alive == True:
                        validtargets.append(t) 
                if (character.rect.y + thisrange <= 288):
                    t = mapcells.cells[(character.rect.x, character.rect.y + thisrange)]
                    if t.contents != None and t.contents.alive == True:
                        validtargets.append(t)
        if len(validtargets) > 0:
            if self.multi:
                for target in validtargets:
                    change = SideEffect(self.type, self.power, self.ranges, self.stat, self.duration, self.delay, self.percent, self.multi)
                    change.attach(target.contents, screen, mapcells)
    
    def attach(self, character, screen, mapcells):
        self.attached = character
        self.attached.effects.append(self)
        if self.delay == 0:
            self.durationtimer = self.duration
            self.turn(screen, mapcells)
        else:
            self.delaytimer = self.delay - 1

    def turn(self, screen, mapcells):
        print 'taking itemturn: %d' % self.durationtimer
        if self.delaytimer == 0:
            self.durationtimer = self.duration
            if self.type == 'heal':
                if self.stat == 1:
                    if self.percent:
                        self.attached.heal(self.power  * self.attached.stats.hp.max / 100, screen)
                    else:
                        self.attached.heal(self.power, screen)
            elif self.type == 'damage':
                if self.stat == 1:
                    if self.percent:
                        self.attached.takedamage(screen, mapcells, damage = (self.power * self.attached.stats.hp.max / 100) )
                    else:
                        self.attached.takedamage(screen, mapcells, damage = self.power)
            self.durationtimer -= 1
            if self.durationtimer <= 0:
                print 'removing self'
                self.attached.effects.remove(self)
                del self
        else:
            self.delaytimer -= 1



class Effect:
    def __init__(self, itype, power, ranges = [], stat = 1, duration = 0, delay = 0, percent = False, multi = False, secondary = []):
        # item type for use method
        self.type = itype
        self.stat = stat
        # power, either fixed or as percent of a stat
        self.power = power
        # boolean: power as percent or fixed value
        self.percent = percent
        # 0 = self, 1 = range 1, 2 = range 2, ..., 50 = range any
        self.ranges = ranges
        # multi allows for multiple targets; as many as are within range for now
        self.multi = multi

        # 1 = hp, 2 = attack, 3 = defense
        self.stat = stat
        # 0 = immediately ends
        self.duration = duration
        # default items will take effect instantly
        self.delay = delay
        self.durationtimer = 0
        self.delaytimer = 0
        self.attached = None
        self.secondary = secondary

    def start(self, character, screen, mapcells):
        self.attach(character, screen, mapcells)
        for effect in self.secondary:
            effect.start(character, screen, mapcells)

    def attach(self, character, screen, mapcells):
        self.attached = character
        self.attached.effects.append(self)
        if self.delay == 0:
            self.durationtimer = self.duration
            self.turn(screen, mapcells)
        else:
            self.delaytimer = self.delay

    def turn(self, screen, mapcells):
        if self.delaytimer == 0:
            if self.type == 'heal':
                if self.stat == 1:
                    if self.percent:
                        self.attached.heal(self.power  * self.attached.stats.hp.max / 100, screen)
                    else:
                        self.attached.heal(self.power, screen)
            elif self.type == 'damage':
                if self.stat == 1:
                    if self.percent:
                        self.attached.takedamage(screen, mapcells, damage = (self.power * self.attached.stats.hp.max / 100) )
                    else:
                        self.attached.takedamage(screen, mapcells, damage = self.power)
        else:
            self.delaytimer -= 1

        self.durationtimer -= 1
        if self.durationtimer <= 0:
            self.attached.effects.remove(self)
#            self.attached = None
            del self






class Item:
    def __init__(self, name, effect):
        # item name for menu display
        self.name = name
        # primary effect of item
        self.effect = effect
        # most items will have 1 use, but some may have multiple
#        self.uses = uses
        self.targets = []
    
    def use(self, cells, screen, mapcells):########################
        for target in cells:
            if target.contents != None:
                thiseffect = Effect(self.effect.type, self.effect.power, self.effect.ranges, self.effect.stat, self.effect.duration, self.effect.delay, self.effect.percent, self.effect.multi, self.effect.secondary)
                thiseffect.start(target.contents, screen, mapcells)
        for cell in cells:
            cell.active = False
            cell.draw(screen)
#        self.uses -= 1
#        if self.uses < 1:
#            user.inventory

    
    def gettargets(self, user, screen, mapcells):
        mfriends = 1
        if len(self.targets) > 0:
            mfriends = self.targets[0].contents.friends + 1
        self.targets = []
        for r in self.effect.ranges:
            if r == 50:
                for cell in mapcells.cells.values():
                    if cell.contents != None and cell.contents.alive and (cell.contents.friends == mfriends):
                        self.targets.append(cell)
            else:
                thisrange = r * mapcells.cellsize
                if (user.rect.x - thisrange >= 0):
                    t = mapcells.cells[(user.rect.x - thisrange, user.rect.y)]
                    if t.contents != None and t.contents.alive == True:
                        self.targets.append(t) 
                if (user.rect.y - thisrange >= 0):
                    t = mapcells.cells[(user.rect.x, user.rect.y - thisrange)]
                    if t.contents != None and t.contents.alive == True:
                        self.targets.append(t) 
                if(user.rect.x + thisrange <= 288):
                    t = mapcells.cells[(user.rect.x + thisrange, user.rect.y)]
                    if t.contents != None and t.contents.alive == True:
                        self.targets.append(t) 
                if (user.rect.y + thisrange <= 288):
                    t = mapcells.cells[(user.rect.x, user.rect.y + thisrange)]
                    if t.contents != None and t.contents.alive == True:
                        self.targets.append(t)

        for t in self.targets:
            t.red = True
            if self.effect.multi:
                t.active = True
            t.draw(screen)


# Effect: type, power, ranges, stat, duration, delay, percent, multi
items = {'Apple':Item('Apple', Effect('heal', 10, ranges = [0], stat = 1, duration = 0, delay = 0)), 'Miracle':Item('Miracle', Effect('heal', 100, [50], percent = True, multi = True)), 'Sticks & Stones':Item('Sticks & Stones', Effect('damage', 10, [1, 2])), 'Bomb':Item('Bomb', Effect('damage', 50, ranges = [1, 2, 3, 4], percent = True, secondary = [SideEffect('damage', 10, ranges = [1], percent = True, multi = True)])), 'Poison Gas':Item('Poison Gas', Effect('damage', 80, ranges = [1, 3, 5], duration = 0, percent = False, secondary = [SideEffect('damage', 5, ranges = [0, 1], duration = 5, delay = 1, percent = True, multi = True)]))}
