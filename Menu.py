import pygame
import Stats
import Equipment
import CellObject

###how to make init fail if items per column is off?)###
class Menu:
    def __init__(self):
        self.textbox = pygame.image.load('images/menu/textview.png').convert_alpha()	
        self.textrect = self.textbox.get_rect()
        self.textrect.topleft = (0, 320)
        self.charbase = pygame.image.load('images/menu/charview.png').convert_alpha()
        self.charrect = self.charbase.get_rect()
        self.charrect.topleft = (256, 320)
        self.wholerect = pygame.Rect(0, 320, 320, 64)
        self.downarrow = pygame.image.load('images/menu/downarrow.png').convert_alpha()
        self.downrect = self.downarrow.get_rect()
        self.downrect.topleft = (126, 375)
        self.uparrow = pygame.image.load('images/menu/uparrow.png').convert_alpha()
        self.uprect = self.uparrow.get_rect()
        self.uprect.topleft = (126, 32)
        self.noarrow = pygame.image.load('images/menu/noarrow.png').convert_alpha()
        self.font = pygame.font.Font(None, 14)
        self.highlight = pygame.image.load('images/menu/highlight.png').convert_alpha()
        self.unhighlight = pygame.image.load('images/menu/unhighlight.png').convert_alpha()
        self.active = False
        self.message = None

										
    def drawchoice(self, screen):
        if self.item == 1:
            screen.blit(self.highlight, (25, 330))
        elif self.item == 2:
            screen.blit(self.highlight, (133, 330))
        elif self.item == 3:
            screen.blit(self.highlight, (25, 350))
        elif self.item == 4:
            screen.blit(self.highlight, (133, 350))
        pygame.display.update(self.textrect)

    def undraw(self, screen):
        if self.item == 1:
            screen.blit(self.unhighlight, (25, 330))
        elif self.item == 2:
            screen.blit(self.unhighlight, (133, 330))
        elif self.item == 3:
            screen.blit(self.unhighlight, (25, 350))
        elif self.item == 4:
            screen.blit(self.unhighlight, (133, 350))
        pygame.display.update()


        self.textbox = pygame.image.load('images/menu/textview.png').convert_alpha()	
        self.textrect = self.textbox.get_rect()
        self.textrect.topleft = (0, 320)
        self.charbase = pygame.image.load('images/menu/charview.png').convert_alpha()
        self.charrect = self.charbase.get_rect()
        self.charrect.topleft = (256, 320)
        self.wholerect = pygame.Rect(0, 320, 320, 64)
        self.downarrow = pygame.image.load('images/menu/downarrow.png').convert_alpha()
        self.downrect = self.downarrow.get_rect()
        self.downrect.topleft = (126, 375)
        self.uparrow = pygame.image.load('images/menu/uparrow.png').convert_alpha()
        self.uprect = self.uparrow.get_rect()
        self.uprect.topleft = (126, 32)
        self.noarrow = pygame.image.load('images/menu/noarrow.png').convert_alpha()
        self.font = pygame.font.Font(None, 14)
        self.highlight = pygame.image.load('images/menu/highlight.png').convert_alpha()
        self.unhighlight = pygame.image.load('images/menu/unhighlight.png').convert_alpha()
        self.active = False
        self.message = None
#		self.text 

    def display(self, screen):		
        screen.blit(self.textbox, self.textrect)
        screen.blit(self.charbase, self.charrect)
        if self.message != None:
            text = self.font.render(self.message, True, (255, 255, 255), (0, 0, 255))			
            screen.blit(text, (self.textrect.x + 15, self.textrect.y + 15))
        pygame.display.update(self.wholerect)

    def treasure(self, screen):
        self.message = 'Press [SPACEBAR] to open the treasure chest'
        screen.blit(self.textbox, self.textrect)
        text = self.font.render(self.message, True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 15, self.textrect.y + 15))
        pygame.display.update(self.textrect)
        
    def plant(self, screen):
        self.message = 'Press [SPACEBAR] to harvest the plant'
        screen.blit(self.textbox, self.textrect)
        text = self.font.render(self.message, True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 15, self.textrect.y + 15))
        pygame.display.update(self.textrect)

    def location(self, screen):
        self.message = 'Press [SPACEBAR] to visit the location'
        screen.blit(self.textbox, self.textrect)
        text = self.font.render(self.message, True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 15, self.textrect.y + 15))
        pygame.display.update(self.textrect)

    def showmenu(self, screen, character):
        self.item = 1
        screen.blit(self.textbox, self.textrect)
        screen.blit(self.charbase, self.charrect)
		
        if character.moved:
            text = self.font.render('Move', True, (150, 150, 150), (0, 0, 255))
        else: # if not character.moved
            text = self.font.render('Move', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 30, self.textrect.y + 15))
		
        if character.acted:
            text = self.font.render('Attack', True, (150, 150, 150), (0, 0, 255))
        else: # if not character.acted
            text = self.font.render('Attack', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 138, self.textrect.y + 15))

        if character.acted:
            text = self.font.render('Inventory', True, (150, 150, 150), (0, 0, 255))
        else: # if not character.acted
            text = self.font.render('Inventory', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 30, self.textrect.y + 35))
	
        text = self.font.render('Wait', True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 138, self.textrect.y + 35))

        pygame.display.update(self.wholerect)



        while True:
            self.drawchoice(screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        self.undraw(screen)
                        if self.item == 1:
                            self.item = 2
                        elif self.item == 2:
                            self.item = 1
                        elif self.item == 3:
                            self.item = 4
                        elif self.item == 4:
                            self.item = 3
                    elif keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        self.undraw(screen)
                        if self.item == 1:
                            self.item = 3
                        elif self.item == 2:
                            self.item = 4
                        elif self.item == 3:
                            self.item = 1
                        elif self.item == 4:
                            self.item = 2
                    elif keys[pygame.K_RETURN]:
#                        self.active = False
                        if self.item == 1:
                            if not character.moved:
                                screen.blit(self.textbox, self.textrect)
                                pygame.display.update(self.textrect)
                                return 1
                        elif self.item == 2:
                            if not character.acted:
                                screen.blit(self.textbox, self.textrect)
                                pygame.display.update(self.textrect)
                                return 2
                        elif self.item == 3:
                            if not character.acted:
                                screen.blit(self.textbox, self.textrect)
                                pygame.display.update(self.textrect)
                                return 3
                        elif self.item == 4:
                            return 4
                    elif keys[pygame.K_ESCAPE]:
                        self.info(screen, character)
                        return 0
										
    def drawchoice(self, screen):
        if self.item == 1:
            screen.blit(self.highlight, (25, 330))
        elif self.item == 2:
            screen.blit(self.highlight, (133, 330))
        elif self.item == 3:
            screen.blit(self.highlight, (25, 350))
        elif self.item == 4:
            screen.blit(self.highlight, (133, 350))
        pygame.display.update(self.textrect)

    def undraw(self, screen):
        if self.item == 1:
            screen.blit(self.unhighlight, (25, 330))
        elif self.item == 2:
            screen.blit(self.unhighlight, (133, 330))
        elif self.item == 3:
            screen.blit(self.unhighlight, (25, 350))
        elif self.item == 4:
            screen.blit(self.unhighlight, (133, 350))
        pygame.display.update()
						
	
    def info(self, screen, character):
        screen.blit(self.textbox, self.textrect)
        screen.blit(self.charbase, self.charrect)
        cimg = character.image.get_rect()
        #this positioning may change later
        cimg.topleft = (self.charrect.x + 16, self.charrect.y + 16)
        screen.blit(character.image, cimg)

        #now to add text for character info
        text = self.font.render(character.name + ' (Lv%d %s)' % (character.stats.level, character.classname), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 10, self.textrect.y + 10))

        text = self.font.render('Experience: %d' % character.exp, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 10, self.textrect.y + 20))

        text = self.font.render('Moves: %d' % character.stats.moverange, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 10, self.textrect.y + 30))

        ranges = ''
        for arange in character.weapon.range:  #for arange in character.weapon.attackrange:
            if arange != character.weapon.range[0]: #if arange != character.weapon.attackrange:
                ranges += ', '
            if arange == -1:
                ranges += 'D'
            else:
                ranges += '%d' % arange
        text = self.font.render('Range: ' + ranges , True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 10, self.textrect.y + 40))

        text = self.font.render('HP: %d/%d' % (character.stats.hp.current, character.stats.hp.max), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 114, self.textrect.y + 10))

        if character.weapon.type == 'Spell':
            text = self.font.render('Attack: %d' % (character.stats.magicattack.current + character.weapon.attack.current + character.armor.magicattack.current), True, (255, 255, 255), (0, 0,255))
        elif character.weapon.type == 'Staff':       
            text = self.font.render('Attack: %d + %d' % (character.stats.attack.current / 2 + character.stats.magicattack.current / 2 + character.weapon.attack.current + character.armor.attack.current / 2 + character.armor.magicattack.current / 2), True, (255, 255, 255), (0, 0,255))
        else:
            text = self.font.render('Attack: %d' % (character.stats.attack.current + character.weapon.attack.current + character.armor.attack.current), True, (255, 255, 255), (0, 0,255))
        screen.blit(text, (self.textrect.x + 114, self.textrect.y + 20))

        text = self.font.render('Defense: %d + %d' % (character.stats.defense.current, character.armor.defense.current + character.weapon.defense.current), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 114, self.textrect.y + 30))

        text = self.font.render('M Def: %d + %d' % (character.stats.defense.current, character.armor.defense.current + character.weapon.defense.current), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 114, self.textrect.y + 40))


        text = self.font.render('Speed: %d + %d' % (character.stats.speed.current, character.armor.speed.current + character.weapon.speed.current), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 188, self.textrect.y + 10))

        text = self.font.render('Hit: %d' % (character.stats.skill.current * 3 + character.weapon.accuracy.current), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 188, self.textrect.y + 20))

        text = self.font.render('Dodge: %d' % (character.stats.speed.current * 2 - character.weapon.speed.current * 2 - character.armor.speed.current * 2), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 188, self.textrect.y + 30))

        text = self.font.render('Critical: %d' % (character.stats.skill.current / 2 + character.weapon.critical + character.critical), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.textrect.x + 188, self.textrect.y + 40))


        pygame.display.update(self.wholerect)

    def inventory(self, screen, character):
        items = True
        while True:
            done = False

            screen.blit(self.textbox, self.textrect)

            text = self.font.render('Items', True, (255, 255, 255), (0, 0, 255))			
            screen.blit(text, (self.textrect.x + 30, self.textrect.y + 15))

            text = self.font.render('Equipment', True, (255, 255, 255), (0, 0, 255))			
            screen.blit(text, (self.textrect.x + 138, self.textrect.y + 15))

            if items:
                screen.blit(self.highlight, (25, 330))
            else: #if equipment
                screen.blit(self.highlight, (133, 330))

            pygame.display.update(self.textrect)

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                            done = True
                            if items:                
                                screen.blit(self.unhighlight, (133, 330))
                                items = False
                            else:
                                screen.blit(self.unhighlight, (25, 330))
                                items = True
                        elif keys[pygame.K_RETURN]:
#                        self.active = False
                            if items:
                                screen.blit(self.textbox, self.textrect)
                                pygame.display.update(self.textrect)
                                thing = self.items(screen, character)
                                if thing != -1:
                                    return thing
                                done = True
                            else: #if equipment:
                                screen.blit(self.textbox, self.textrect)
                                pygame.display.update(self.textrect)
                                self.getequipment(screen, character)
                                done = True
                        elif keys[pygame.K_ESCAPE]:
                            screen.blit(self.textbox, self.textrect)
                            pygame.display.update(self.textrect)
                            return -1


    def items(self, screen, character):
        self.item = 1
        index = 0
        while True:
            done = False

            screen.blit(self.textbox, self.textrect)
            if index < len(character.items):
                slot1 = character.items[index]
#                text = self.font.render(slot1.name + '\t' + slot1.quantity, True, (255, 255, 255), (0, 0, 255))			
                text = self.font.render(slot1, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 30, self.textrect.y + 15))
            if index + 1 < len(character.items):
                slot2 = character.items[index + 1]
#                text = self.font.render(slot2.name + '\t' + slot2.quantity, True, (255, 255, 255), (0, 0, 255))			
                text = self.font.render(slot2, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 138, self.textrect.y + 15))
            if index + 2 < len(character.items):
                slot3 = character.items[index + 2]
#                text = self.font.render(slot3.name + '\t' + slot3.quantity, True, (255, 255, 255), (0, 0, 255))			
                text = self.font.render(slot3, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 30, self.textrect.y + 35))
            if index + 3 < len(character.items):
                slot4 = character.items[index + 3]
#                text = self.font.render(slot4.name + '\t' + slot3.quantity, True, (255, 255, 255), (0, 0, 255))			
                text = self.font.render(slot4, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 138, self.textrect.y + 35))

            if index + 4 < len(character.items):
                screen.blit(self.downarrow, self.downrect)
            else:
                screen.blit(self.noarrow, self.downrect)

            if index > 0:
                screen.blit(self.uparrow, self.uprect)
            else:
                screen.blit(self.noarrow, self.uprect)

            self.drawchoice(screen)
#            pygame.display.update(self.textrect)

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                            self.undraw(screen)
                            done = True
                            if self.item == 1:
                                self.item = 2
                            elif self.item == 2:
                                self.item = 1
                            elif self.item == 3:
                                self.item = 4
                            elif self.item == 4:
                                self.item = 3
                        elif keys[pygame.K_UP]:
                            done = True
                            if self.item == 1 or self.item == 2:
                                if index > 0:
                                    index -= 2
                            else:
                                self.undraw(screen)
                                if self.item == 3:
                                    self.item = 1
                                elif self.item == 4:
                                    self.item = 2
                        elif keys[pygame.K_DOWN]:
                            done = True
                            if self.item == 3 or self.item == 4:
                                if index + 4 < len(character.items):
                                    index += 2
                            else:
                                self.undraw(screen)
                                if self.item == 1:
                                    self.item = 3
                                elif self.item == 2:
                                    self.item = 4
                        elif keys[pygame.K_RETURN]:
#                        self.active = False
                            if (self.item + index - 1) < len(character.items):
                                screen.blit(self.textbox, self.textrect)
                                pygame.display.update(self.textrect)
                                return self.item + index - 1
                        elif keys[pygame.K_ESCAPE]:
                            screen.blit(self.textbox, self.textrect)
                            pygame.display.update(self.textrect)
                            return -1

    def getequipment(self, screen, character):
        self.item = 1
        index = 0
        while True:
            done = False

            screen.blit(self.textbox, self.textrect)
            if index < len(character.equipment):
                slot1 = character.equipment[index]
                text = self.font.render(slot1.name, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 30, self.textrect.y + 15))
            if index + 1 < len(character.equipment):
                slot2 = character.equipment[index + 1]
                text = self.font.render(slot2.name, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 138, self.textrect.y + 15))
            if index + 2 < len(character.equipment):
                slot3 = character.equipment[index + 2]
                text = self.font.render(slot3.name, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 30, self.textrect.y + 35))
            if index + 3 < len(character.equipment):
                slot4 = character.equipment[index + 3]
                text = self.font.render(slot4.name, True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.textrect.x + 138, self.textrect.y + 35))

            if index + 4 < len(character.equipment):
                screen.blit(self.downarrow, self.downrect)
            else:
                screen.blit(self.noarrow, self.downrect)

            if index > 0:
                screen.blit(self.uparrow, self.uprect)
            else:
                screen.blit(self.noarrow, self.uprect)

            self.drawchoice(screen)
#            pygame.display.update(self.textrect)

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                            self.undraw(screen)
                            done = True
                            if self.item == 1:
                                self.item = 2
                            elif self.item == 2:
                                self.item = 1
                            elif self.item == 3:
                                self.item = 4
                            elif self.item == 4:
                                self.item = 3
                        elif keys[pygame.K_UP]:
                            done = True
                            if self.item == 1 or self.item == 2:
                                if index > 0:
                                    index -= 2
                            else:
                                self.undraw(screen)
                                if self.item == 3:
                                    self.item = 1
                                elif self.item == 4:
                                    self.item = 2
                        elif keys[pygame.K_DOWN]:
                            done = True
                            if self.item == 3 or self.item == 4:
                                if index + 4 < len(character.equipment):
                                    index += 2
                            else:
                                self.undraw(screen)
                                if self.item == 1:
                                    self.item = 3
                                elif self.item == 2:
                                    self.item = 4
                        elif keys[pygame.K_RETURN]:
                            thisitem = (self.item + index - 1)
                            if thisitem < len(character.equipment):
                                screen.blit(self.textbox, self.textrect)
                                pygame.display.update(self.textrect)
                                eq = character.equipment[thisitem]
                                if eq.name in Equipment.weapons.keys():
                                    if character.weapon == eq:
                                        if self.ask(screen):
                                            character.unequipweapon()
                                    elif self.showitem(screen, character, eq):
                                        if not character.equipweapon(eq):
                                            temp = screen.copy()
                                            screen.blit(self.textbox, self.textrect)
                                            text = self.font.render(character.name + " can't equip this item!", True, (255, 255, 255), (0, 0, 255))
                                            screen.blit(text, (self.textrect.x + self.textrect.width/2 - text.get_clip().width/2, self.textrect.y + 10))
                                            pygame.display.update(self.textrect)
                                            wait = True
                                            while wait:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.KEYDOWN:
                                                        wait = False
                                            screen.blit(temp, (0, 0))
                                            pygame.display.update()
                                elif eq.name in Equipment.armors.keys():
                                    if character.armor == eq:
                                        if self.ask(screen):
                                            character.unequiparmor()
                                    elif self.showitem(screen, character, eq):
                                        if not character.equiparmor(eq):
                                            temp = screen.copy()
                                            screen.blit(self.textbox, self.textrect)
                                            text = self.font.render(character.name + " can't equip this item!", True, (255, 255, 255), (0, 0, 255))
                                            screen.blit(text, (self.textrect.x + self.textrect.width/2 - text.get_clip().width/2, self.textrect.y + 10))
                                            pygame.display.update(self.textrect)
                                            wait = True
                                            while wait:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.KEYDOWN:
                                                        wait = False
                                            screen.blit(temp, (0, 0))
                                            pygame.display.update()
                                            
                            done = True
                        elif keys[pygame.K_ESCAPE]:
                            screen.blit(self.textbox, self.textrect)
                            pygame.display.update(self.textrect)
                            return -1

    def ask(self, screen, message = 'Do you want to unequip this item?'):
        highlight = pygame.image.load('images/menu/highlight2.png').convert_alpha()
        unhighlight = pygame.image.load('images/menu/unhighlight2.png').convert_alpha()

        text = self.font.render(message, True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 15, self.textrect.y + 15))
        text = self.font.render('Yes', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 95, self.textrect.y + 40))
        text = self.font.render('No', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.textrect.x + 175, self.textrect.y + 40))

        yes = True

        while True:
            if yes:
                screen.blit(unhighlight, (self.textrect.x + 170, self.textrect.y + 35))
                screen.blit(highlight, (self.textrect.x + 90, self.textrect.y + 35))
            else:
                screen.blit(unhighlight, (self.textrect.x + 90, self.textrect.y + 35))
                screen.blit(highlight, (self.textrect.x + 170, self.textrect.y + 35))
            pygame.display.update(self.textrect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()                    
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        if yes:
                            yes = False
                        else:
                            yes = True
                    elif keys[pygame.K_RETURN]:
                        return yes
                    elif keys[pygame.K_ESCAPE]:
                        return False
        
    def showitem(self, screen, character, item):
        highlight = pygame.image.load('images/menu/highlight2.png').convert_alpha()
        unhighlight = pygame.image.load('images/menu/unhighlight2.png').convert_alpha()
        yes = True

        change = '0'
        if Equipment.equiptype(item.name) == 1:
            diff = item.attack.current - character.weapon.attack.current
            if diff < 0:
                change = '%d' % diff
            else: #if diff >= 0:
                change = '+%d' % diff            
            eqtxt = self.font.render('Weapon: Attack ' + change, True, (255, 255, 255), (0, 0, 255))			
        else: #if Equipment.equiptype(item) == 2:
            diff = item.defense.current - character.armor.defense.current
            if diff < 0:
                change = '%d' % diff
            else: #if diff >= 0:
                change = '+%d' % diff            
            eqtxt = self.font.render('Armor: Defense ' + change, True, (255, 255, 255), (0, 0, 255))	
        message = self.font.render('Equip %s?' % item.name, True, (255, 255, 255), (0, 0, 255))
        eqwhere = (self.textrect.x + message.get_clip().width + 30, self.textrect.y + 15)

        while True:
            screen.blit(self.textbox, self.textrect)
            screen.blit(eqtxt, eqwhere)
            screen.blit(message, (self.textrect.x + 15, self.textrect.y + 15))
            text = self.font.render('Yes', True, (255, 255, 255), (0, 0, 255))			
            screen.blit(text, (self.textrect.x + 95, self.textrect.y + 40))
            text = self.font.render('No', True, (255, 255, 255), (0, 0, 255))			
            screen.blit(text, (self.textrect.x + 175, self.textrect.y + 40))

            if yes:
                screen.blit(unhighlight, (self.textrect.x + 170, self.textrect.y + 35))
                screen.blit(highlight, (self.textrect.x + 90, self.textrect.y + 35))
            else:
                screen.blit(unhighlight, (self.textrect.x + 90, self.textrect.y + 35))
                screen.blit(highlight, (self.textrect.x + 170, self.textrect.y + 35))
            pygame.display.update(self.textrect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()                    
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        if yes:
                            yes = False
                        else:
                            yes = True
                    elif keys[pygame.K_RETURN]:
                        return yes
                    elif keys[pygame.K_ESCAPE]:
                        return False


