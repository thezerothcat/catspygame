import pygame
import pickle
import Equipment
import Shop
import Forge
from TitleScreen import text_screen
#import Player
#from CellObject import Actor

class PlayerScreen:
    def __init__(self, state):
#        self.textbase = pygame.image.load('images/menu/textview.png').convert_alpha()	
#        self.textrect = self.textbase.get_rect()
#        self.textrect.topleft = (0, 320)
#        self.charbase = pygame.image.load('images/menu/charview.png').convert_alpha()
#        self.charrect = self.charbase.get_rect()
#        self.charrect.topleft = (256, 320)
        self.font = pygame.font.Font(None, 14)
        self.smallfont = pygame.font.Font(None, 12)        
        self.highlightc = pygame.image.load('images/menu/highlightc.png').convert_alpha()
        self.unhighlightc = pygame.image.load('images/menu/unhighlightc.png').convert_alpha()
        self.downarrow = pygame.image.load('images/menu/downarrow.png').convert_alpha()
        self.downrect = self.downarrow.get_rect()
        self.downrect.topleft = (126, 375)
        self.uparrow = pygame.image.load('images/menu/uparrow.png').convert_alpha()
        self.uprect = self.uparrow.get_rect()
        self.uprect.topleft = (126, 5)
        self.noarrow = pygame.image.load('images/menu/noarrow.png').convert_alpha()
        self.main = pygame.image.load('images/menu/vmenu2.png').convert_alpha()
        self.mainrect = self.main.get_rect()
        self.mainrect.topleft = (96, 64)
        self.highlight = pygame.image.load('images/menu/highlight.png').convert_alpha()
        self.unhighlight = pygame.image.load('images/menu/unhighlight.png').convert_alpha()
        self.sidebox = pygame.image.load('images/menu/sidebar.png').convert_alpha()
        self.siderect = self.sidebox.get_rect()
        self.siderect.topleft = (230, 0)
        self.state = state

    def mainscreen(self, player, screen):
        item = 1
        index = 0

        screen.fill((0, 0, 0))        

        screen.blit(self.main, self.mainrect)

        text = self.font.render('Info', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.mainrect.x + 30, self.mainrect.y + 15))

        text = self.font.render('Characters', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (self.mainrect.x + 30, self.mainrect.y + 35))

        if self.state == 0:
            text = self.font.render('Shop', True, (255, 255, 255), (0, 0, 255))			
        else: #if state == 1:
            text = self.font.render('Shop', True, (100, 100, 100), (0, 0, 255))			
        screen.blit(text, (self.mainrect.x + 30, self.mainrect.y + 55))
    
        if self.state == 0:
            text = self.font.render('Forge', True, (255, 255, 255), (0, 0, 255))			
        else: #if state == 1:
            text = self.font.render('Forge', True, (100, 100, 100), (0, 0, 255))			
        screen.blit(text, (self.mainrect.x + 30, self.mainrect.y + 75))

        if self.state == 0:
            text = self.font.render('Save', True, (255, 255, 255), (0, 0, 255))			
        else: #if state == 1:
            text = self.font.render('Save', True, (100, 100, 100), (0, 0, 255))			
        screen.blit(text, (self.mainrect.x + 30, self.mainrect.y + 95))

        text = self.font.render('Continue', True, (255, 255, 255), (0, 0, 255))                                	
        screen.blit(text, (self.mainrect.x + 30, self.mainrect.y + 115))

        text = self.font.render('Quit to Title', True, (255, 255, 255), (0, 0, 255))                                	
        screen.blit(text, (self.mainrect.x + 30, self.mainrect.y + 135))

        while True:
            screen.blit(self.highlight, (self.mainrect.x + 20, self.mainrect.y + 20 * item - 10))
        
            pygame.display.update()

            done = False

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP]:
                            screen.blit(self.unhighlight, (self.mainrect.x + 20, self.mainrect.y + 20 * item - 10))
                            done = True
                            item -= 1
                            if item < 1:
                                item = 7
                        elif keys[pygame.K_DOWN]:
                            screen.blit(self.unhighlight, (self.mainrect.x + 20, self.mainrect.y + 20 * item - 10))
                            done = True
                            item += 1
                            if item > 7:
                                item = 1
                        elif keys[pygame.K_RETURN]:
                            if item == 1: # info
                                temp = screen.copy()
                                self.info(player, screen)
                                screen.blit(temp, (0, 0))
                                pygame.display.update()
                            elif item == 2: # characters
                                temp = screen.copy()
                                self.characterselect(player, screen)
                                screen.blit(temp, (0, 0))
                                pygame.display.update()
                            elif item == 3 and self.state == 0:
                                temp = screen.copy()
                                place = Shop.Store(1)
                                place.shop(player, screen)
                                screen.blit(temp, (0, 0))
                                pygame.display.update()
                            elif item == 4 and self.state == 0:
                                temp = screen.copy()
                                place = Forge.Forge()
                                place.shop(player, screen)
                                screen.blit(temp, (0, 0))
                                pygame.display.update()
                            elif item == 5 and self.state == 0: # save
                                temp = screen.copy()
                                self.savescreen(player, screen)
                                screen.blit(temp, (0, 0))
                                pygame.display.update()
                            elif item == 6:
                                return 0
                            elif item == 7:
                                return -1
#                        elif keys[pygame.K_ESCAPE]:
#                            return 0

    def info(self, player, screen):
        screen.fill((0, 0, 255))
        text = self.smallfont.render('[ESC] to go back', True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (0, 0))
        text = self.font.render('You have %d money.' % player.money, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (90, 185))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        return 0


    def savescreen(self, player, screen):
        try:
            name = text_screen(screen, description = 'Enter a save name:')
            savefile = open('saves/player/' + name + '.pkl', 'wb')

            for character in player.characters:
                character.picklefix()
            pickle.dump(player, savefile)
        except:
            text = self.font.render('Game save failed.', True, (255, 255, 255), (0, 0, 255))
        else:
            text = self.font.render('Game saved.', True, (255, 255, 255), (0, 0, 255))
        finally:
            savefile.close()
            for character in player.characters:
                character.unpicklefix()

            screen.fill((0, 0, 255))
            screen.blit(text, (90, 185))
            text = self.smallfont.render('[ESC] to go back', True, (255, 255, 255), (0, 0, 255))
            screen.blit(text, (0, 0))

            pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        return 0
        #info - money, progress, etc?
        #characters
        #save
        #exit

    def characterscreen(self, player, character, screen):
        screen.fill((0, 0, 255))
        text = self.smallfont.render('[ESC] to go back', True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (0, 0))

        cimg = character.image.get_rect()
        #this positioning may change later
        cimg.topleft = (272, 26)
        screen.blit(character.image, cimg)

        #now to add text for character info
        text = self.font.render('Name: ' + character.name, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (10, 20))
        text = self.font.render('HP: %d/%d' % (character.stats.hp.current, character.stats.hp.max), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (10, 30))
        text = self.font.render('Attack: %d + %d' % (character.stats.attack.current, character.weapon.attack.current), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (10, 40))
        text = self.font.render('Defense: %d + %d' % (character.stats.defense.current, character.armor.defense.current), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (10, 50))
        text = self.font.render('Level %d %s' % (character.stats.level, character.classname), True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (128, 20))
        text = self.font.render('Experience: %d' % character.exp, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (128, 30))
        text = self.font.render('Moves: %d' % character.stats.moverange, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (128, 40))
        ranges = ''
        for arange in character.weapon.range:
            if arange != character.weapon.range[0]:
                ranges += ', '
            ranges += '%d' % arange
        text = self.font.render('Range: ' + ranges , True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (128, 50))

#        text = self.font.render('Items:', True, (200, 200, 0), (0, 0, 255))
#        screen.blit(text, (10, 100))
 
#        text = self.font.render('Equipment:', True, (255, 255, 255), (0, 0, 255))
#        screen.blit(text, (10, 200))

        places = []
        for y in range(0, 3):
            for x in range(0, 4):
                places.append((75 * x + 10, y * 20 + 120))
        places.pop(11)
        places.pop(10)
        for y in range(0, 3):
            for x in range(0, 4):
                places.append((75 * x + 10, y * 20 + 220))           
        places[20] = (10, 100)
        places[21] = (10, 200)

        i = 0
        for thing in character.items:
            text = self.font.render(thing, True, (255, 255, 255), (0, 0, 255))
            screen.blit(text, places[i])
            i += 1
        i = 10
        for thing in character.equipment:
            text = self.font.render(thing.name, True, (255, 255, 255), (0, 0, 255))
            screen.blit(text, places[i])
            i += 1
        select = 21

        while True:
            done = False

            if select == 21:
                text = self.font.render('Equipment:', True, (255, 255, 255), (0, 0, 255))
                screen.blit(text, places[21])
                text = self.font.render('Items:', True, (200, 200, 0), (0, 0, 255))
            elif select == 22:
                text = self.font.render('Items:', True, (255, 255, 255), (0, 0, 255))
                screen.blit(text, places[20])
                text = self.font.render('Equipment:', True, (200, 200, 0), (0, 0, 255))
            elif select < 11:
                text = self.font.render(character.items[select - 1], True, (200, 200, 0), (0, 0, 255))
            else: # if select > 10:
                text = self.font.render(character.equipment[select - 11].name, True, (200, 200, 0), (0, 0, 255))

            screen.blit(text, places[select - 1])

            pygame.display.update()

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()

                        if keys[pygame.K_ESCAPE]:
                            if select > 20:
                                return 0
                            elif select > 10:
                                text = self.font.render(character.equipment[select - 11].name, True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, places[select - 1])
                                select = 22
                            else:
                                text = self.font.render(character.items[select - 1], True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, places[select - 1])
                                select = 21
                            done = True
                        elif keys[pygame.K_RIGHT]:
                            if select < 11:
                                if select + 1 <= len(character.items):
                                    text = self.font.render(character.items[select - 1], True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select += 1
                                    done = True
                            elif select < 21:
                                if select - 9 <= len(character.equipment): # select - 10 + 
                                    text = self.font.render(character.equipment[select - 11].name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select += 1
                                    done = True
                        elif keys[pygame.K_LEFT]:
                            if select < 11:
                                if select - 1 > 0: 
                                    text = self.font.render(character.items[select - 1], True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select -= 1                        
                                    done = True
                            elif select < 21:
                                if select - 11 > 0: # select - 10 + 
                                    text = self.font.render(character.equipment[select - 11].name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select -= 1
                                    done = True
                        elif keys[pygame.K_DOWN]:
                            if select < 11:
                                if select + 4 <= len(character.items):
                                    text = self.font.render(character.items[select - 1], True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select += 4                        
                                    done = True
                            elif select < 21:
                                if select - 6 <= len(character.equipment): # select - 10 + 4
                                    text = self.font.render(character.equipment[select - 11].name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select += 4                        
                                    done = True
                            elif select == 21:
                                text = self.font.render('Items:', True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, places[select - 1])
                                select = 22
                                done = True
                            elif select == 22:
                                text = self.font.render('Equipment:', True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, places[select - 1])
                                select = 21
                                done = True
                        elif keys[pygame.K_UP]:
                            if select < 11:
                                if select - 4 > 0:
                                    text = self.font.render(character.items[select - 1], True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select -= 4                        
                                    done = True
                            elif select < 21:
                                if select - 14 > 0: # select - 10 + 4
                                    text = self.font.render(character.equipment[select - 11].name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, places[select - 1])
                                    select -= 4                        
                                    done = True
                            elif select == 21:
                                text = self.font.render('Items:', True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, places[select - 1])
                                select = 22
                                done = True
                            elif select == 22:
                                text = self.font.render('Equipment:', True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, places[select - 1])
                                select = 21
                                done = True
                        elif keys[pygame.K_RETURN]:
                            if self.state == 0:
                                if select < 21:
                                    if select < 11:
                                        self.giveitem(character.items[select - 1], character, player, screen)
                                        select = 21
    
                                        screen.fill((0, 0, 255))
                                        text = self.smallfont.render('[ESC] to go back', True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, (0, 0))
    
                                        text = self.font.render('Equipment:', True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, places[21])
                                        text = self.font.render('Items:', True, (200, 200, 0), (0, 0, 255))
                                        screen.blit(text, places[20])
                                    else:
                                        self.getequipment(character.equipment[select - 11], character, player, screen)
                                        select = 22
    
                                        screen.fill((0, 0, 255))
                                        text = self.smallfont.render('[ESC] to go back', True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, (0, 0))
    
                                        text = self.font.render('Items:', True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, places[20])
                                        text = self.font.render('Equipment:', True, (200, 200, 0), (0, 0, 255))
                                        screen.blit(text, places[21])
    
                                    cimg = character.image.get_rect()
                                    #this positioning may change later
                                    cimg.topleft = (272, 26)
                                    screen.blit(character.image, cimg)
        
                                    #now to add text for character info
                                    text = self.font.render('Name: ' + character.name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (10, 20))
                                    text = self.font.render('HP: %d/%d' % (character.stats.hp.current, character.stats.hp.max), True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (10, 30))
                                    text = self.font.render('Attack: %d + %d' % (character.stats.attack.current, character.weapon.attack.current), True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (10, 40))
                                    text = self.font.render('Defense: %d + %d' % (character.stats.defense.current, character.armor.defense.current), True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (10, 50))
                                    text = self.font.render('Level %d %s' % (character.stats.level, character.classname), True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (128, 20))
                                    text = self.font.render('Experience: %d' % character.exp, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (128, 30))
                                    text = self.font.render('Moves: %d' % character.stats.moverange, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (128, 40))
                                    ranges = ''
                                    for arange in character.weapon.range:
                                        if arange != character.weapon.range[0]:
                                            ranges += ', '
                                        ranges += '%d' % arange
                                    text = self.font.render('Range: ' + ranges , True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (128, 50))
    
                                    text = self.font.render('Items:', True, (200, 200, 0), (0, 0, 255))
                                    screen.blit(text, (10, 100))
    
                                    text = self.font.render('Equipment:', True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (10, 200))
        
                                    i = 0
                                    for thing in character.items:
                                        text = self.font.render(thing, True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, places[i])
                                        i += 1
                                    i = 10
                                    for thing in character.equipment:
                                        text = self.font.render(thing.name, True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, places[i])
                                        i += 1
                                    done = True
    
                                elif select == 21:
                                    if len(character.items) > 0:
                                        text = self.font.render('Items:', True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, places[20])
                                        select = 1
                                        done = True
                                elif select == 22:
                                    if len(character.equipment) > 0:
                                        text = self.font.render('Equipment:', True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, places[21])
                                        select = 11
                                        done = True
    
    def getequipment(self, thing, character, player, screen):
        screen.blit(self.sidebox, self.siderect.topleft)
        eq = True

        while True:
            text = self.font.render('Do what?', True, (255, 255, 255), (0, 0, 255))
            screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))
    
            if eq:
                text = self.font.render('Equip', True, (200, 200, 0), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
                text = self.font.render('Give', True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 45))
            else:
                text = self.font.render('Equip', True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
                text = self.font.render('Give', True, (200, 200, 0), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 45))
            pygame.display.update(self.siderect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()                    
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        if eq:
                            eq = False
                        else:
                            eq = True
                    elif keys[pygame.K_RETURN]:
                        if eq:
                            if thing == character.weapon:                                                       
                                if self.ask(screen, question = 'Unequip?'):
                                    character.unequipweapon()
                            elif thing == character.armor:
                                if self.ask(screen, question = 'Unequip?'):
                                    character.unequiparmor()
                            elif self.ask(screen, question = 'Equip?'):
                                if thing.name in Equipment.weapons.keys():
                                    if not character.equipweapon(thing):
                                        temp = screen.copy()
                                        screen.blit(self.sidebox, self.siderect)
                                        text = self.font.render(character.name + " can't equip this item!", True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, (self.siderect.x + self.siderect.width/2 - text.get_clip().width/2, self.siderect.y + 10))
                                        pygame.display.update(self.siderect)
                                        wait = True
                                        while wait:
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    wait = False
                                        screen.blit(temp, (0, 0))
                                        pygame.display.update()
                                elif thing.name in Equipment.armors.keys():
                                    if not character.equiparmor(thing):
                                        temp = screen.copy()
                                        screen.blit(self.sidebox, self.siderect)
                                        text = self.font.render(character.name + " can't equip this item!", True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, (self.siderect.x + self.siderect.width/2 - text.get_clip().width/2, self.siderect.y + 10))
                                        pygame.display.update(self.siderect)
                                        wait = True
                                        while wait:
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    wait = False
                                        screen.blit(temp, (0, 0))
                                        pygame.display.update()

                        else:
                            self.giveitem(thing, character, player, screen, justitem = False)
                        return 0
                    elif keys[pygame.K_ESCAPE]:
                        return 0


        

    def ask(self, screen, question = 'Equip?'):
        screen.blit(self.sidebox, self.siderect.topleft)
        text = self.font.render(question, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))

        yes = True

        while True:
            if yes:
                text = self.font.render('Yes', True, (200, 200, 0), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
                text = self.font.render('No', True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 45))
            else:
                text = self.font.render('Yes', True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
                text = self.font.render('No', True, (200, 200, 0), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 45))
            pygame.display.update(self.siderect)

            done = False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()                    
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                            done = True
                            if yes:
                                yes = False
                            else:
                                yes = True
                        elif keys[pygame.K_RETURN]:
                            return yes
                        elif keys[pygame.K_RETURN]:
                            return False        

    def giveitem(self, item, character, player, screen, justitem = True):
        screen.blit(self.sidebox, self.siderect)
        text = self.font.render('Give to whom?', True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (240, 10))

        i = 0

        for i in range(0, 18):
            if i < len(player.characters):
                text = self.font.render(player.characters[i].name, True, (255, 255, 255), (0, 0, 255))
                screen.blit(text, (240, 20 * i + 24))
        if len(player.characters) > 17:
            screen.blit(self.downarrow, (273, 375))

        select = 1
        index = 0
        # may change if size changes
        last = 18
        while True:
            text = self.font.render(player.characters[select - 1].name, True, (200, 200, 0), (0, 0, 255))
            screen.blit(text, (240, 20 * (select - 1) + 24))

            pygame.display.update()
            done = False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()

                        if keys[pygame.K_ESCAPE]:
                            return 0
                        elif keys[pygame.K_DOWN]:
                            if select + index + 1 <= len(player.characters):
                                if select < last:
                                    text = self.font.render(player.characters[select + index - 1].name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (240, 20 * (select - 1) + 24))
                                    select += 1
                                    done = True
                                else:                                    
                                    for i in range(0, 18):
                                        if i < len(player.characters):
                                            text = self.font.render(player.characters[i + index - 1].name, True, (255, 255, 255), (0, 0, 255))
                                            screen.blit(text, (240, 20 * i + 24))
                                    screen.blit(self.uparrow, (273, 20))
                                    if len(player.characters) > 17:
                                        screen.blit(self.downarrow, (273, 375))
                                    else:
                                        screen.blit(self.noarrow, (273, 375))
                                    done = True

                        elif keys[pygame.K_UP]:
                            if select > 1:
                                text = self.font.render(player.characters[select + index - 1].name, True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, (240, 20 * (select - 1) + 24))
                                select -= 1
                                done = True
                            elif index > 0:
                                index -= 1                                    
                                for i in range(0, 18):
                                    if i < len(player.characters):
                                        text = self.font.render(player.characters[i + index - 1].name, True, (255, 255, 255), (0, 0, 255))
                                        screen.blit(text, (240, 20 * i + 24))
#position of up arrow????
                                if index > 0:
                                    screen.blit(self.uparrow, (273, 20))
                                else:
                                    screen.blit(self.noarrow, (273, 20))
                                screen.blit(self.downarrow, (273, 375))                                       
                                done = True

                        elif keys[pygame.K_RETURN]:
                            if justitem == True:
                                player.characters[select + index - 1].items.append(item)
                                character.items.remove(item)
                            else:
                                guy = player.characters[select + index - 1]
                                if guy.weapon == item:
                                    guy.unequipweapon()
                                if guy.armor == item:
                                    guy.unequiparmor()

                                player.characters[select + index - 1].equipment.append(item)
                                character.removeequipment(item)
                            return 0                
                        elif keys[pygame.K_ESCAPE]:
                            return 0

    def characterselect(self, player, screen):
        screen.fill((0, 0, 255))

        text = self.smallfont.render('[ESC] to go back', True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (0, 0))

        places = [pygame.Rect(10, 10, 150, 50), pygame.Rect(160, 10, 150, 50), pygame.Rect(10, 60, 150, 50), pygame.Rect(160, 60, 150, 50), pygame.Rect(10, 110, 150, 50), pygame.Rect(160, 110, 150, 50), pygame.Rect(10, 160, 150, 50), pygame.Rect(160, 160, 150, 50), pygame.Rect(10, 210, 150, 50), pygame.Rect(160, 210, 150, 50), pygame.Rect(10, 260, 150, 50), pygame.Rect(160, 260, 150, 50)]

        # can show 12 characters

        self.item = 1
        index = 0

        while True:
            done = False

            self.drawscreen(index, places, player, screen)
            pygame.display.update()

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                            done = True
                            screen.blit(self.unhighlightc, places[self.item + index- 1])
                            if self.item % 2 == 1:
                                self.item += 1
                            else: #if self.item % 2 == 0:
                                self.item -= 1
                        elif keys[pygame.K_UP]:
                            done = True
                            if self.item == 1 or self.item == 2:
                                if index > 0:
                                    index -= 2
                            else:
                                screen.blit(self.unhighlightc, places[self.item + index- 1])
                                self.item -= 2
                        elif keys[pygame.K_DOWN]:
                            done = True
                            if self.item == 11 or self.item == 12:
                                if index + 4 < len(player.characters):
                                    index += 2
                            else:
                                screen.blit(self.unhighlightc, places[self.item + index- 1])
                                self.item += 2
                        elif keys[pygame.K_RETURN]:
                            if (self.item + index - 1) < len(player.characters):
                                # go to character menu
                                self.characterscreen(player, player.characters[self.item + index - 1], screen)

                                screen.fill((0, 0, 255))
                                text = self.smallfont.render('[ESC] to go back', True, (255, 255, 255), (0, 0, 255))
                                screen.blit(text, (0, 0))
                                places = [pygame.Rect(10, 10, 150, 50), pygame.Rect(160, 10, 150, 50), pygame.Rect(10, 60, 150, 50), pygame.Rect(160, 60, 150, 50), pygame.Rect(10, 110, 150, 50), pygame.Rect(160, 110, 150, 50), pygame.Rect(10, 160, 150, 50), pygame.Rect(160, 160, 150, 50), pygame.Rect(10, 210, 150, 50), pygame.Rect(160, 210, 150, 50), pygame.Rect(10, 260, 150, 50), pygame.Rect(160, 260, 150, 50)]
                                self.item = 1
                                index = 0
                                self.drawscreen(index, places, player, screen)
                                pygame.display.update()
                        elif keys[pygame.K_ESCAPE]:
                            return 0

    def drawscreen(self, index, places, player, screen):
        if index < len(player.characters):
            slot1 = player.characters[index]
            text = self.font.render(slot1.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index].x + 9, places[index].y + 9))		
            screen.blit(slot1.image, (places[index].x + 89, places[index].y + 9))
        if index + 1 < len(player.characters):
            slot2 = player.characters[index + 1]
            text = self.font.render(slot2.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 1].x + 9, places[index + 1].y + 9))		
            screen.blit(slot2.image, (places[index + 1].x + 89, places[index + 1].y + 9))
        if index + 2 < len(player.characters):
            slot3 = player.characters[index + 2]
            text = self.font.render(slot2.name, True, (255, 255, 255), (0, 0, 255))              
            screen.blit(text, (places[index + 2].x + 9, places[index + 2].y + 9))		
            screen.blit(slot3.image, (places[index + 2].x + 89, places[index + 2].y + 9))
        if index + 3 < len(player.characters):
            slot4 = player.characters[index + 3]
            text = self.font.render(slot4.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 3].x + 9, places[index + 3].y + 9))		
            screen.blit(slot4.image, (places[index + 3].x + 89, places[index + 3].y + 9))
        if index + 4 < len(player.characters):
            slot5 = player.characters[index + 4]
            text = self.font.render(slot5.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 4].x + 9, places[index + 4].y + 9))		
            screen.blit(slot5.image, (places[index + 4].x + 89, places[index + 4].y + 9))
        if index + 5 < len(player.characters):
            slot6 = player.characters[index + 5]
            text = self.font.render(slot6.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 5].x + 9, places[index + 5].y + 9))		
            screen.blit(slot6.image, (places[index + 5].x + 89, places[index + 5].y + 9))
        if index + 6 < len(player.characters):
            slot7 = player.characters[index + 6]
            text = self.font.render(slot7.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 6].x + 9, places[index + 6].y + 9))		
            screen.blit(slot7.image, (places[index + 6].x + 89, places[index + 6].y + 9))
        if index + 7 < len(player.characters):
            slot8 = player.characters[index + 7]
            text = self.font.render(slot8.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 7].x + 9, places[index + 7].y + 9))		
            screen.blit(slot8.image, (places[index + 7].x + 89, places[index + 7].y + 9))
        if index + 8 < len(player.characters):
            slot9 = player.characters[index + 8]
            text = self.font.render(slot9.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 8].x + 9, places[index + 8].y + 9))		
            screen.blit(slot9.image, (places[index + 8].x + 89, places[index + 8].y + 9))
        if index + 9 < len(player.characters):
            slot10 = player.characters[index + 9]
            text = self.font.render(slot10.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 9].x + 9, places[index + 9].y + 9))		
            screen.blit(slot10.image, (places[index + 9].x + 89, places[index + 9].y + 9))
        if index + 10 < len(player.characters):
            slot11 = player.characters[index + 10]
            text = self.font.render(slot11.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 10].x + 9, places[index + 10].y + 9))		
            screen.blit(slo1t1.image, (places[index + 10].x + 89, places[index + 10].y + 9))
        if index + 11 < len(player.characters):
            slot12 = player.characters[index + 11]
            text = self.font.render(slot12.name, True, (255, 255, 255), (0, 0, 255))                
            screen.blit(text, (places[index + 11].x + 9, places[index + 11].y + 9))		
            screen.blit(slot12.image, (places[index + 11].x + 89, places[index + 11].y + 9))
        if index + 12 < len(player.characters):
            screen.blit(self.downarrow, self.downrect)
        else:
            screen.blit(self.noarrow, self.downrect)

        if index > 0:
            screen.blit(self.uparrow, self.uprect)
        else:
            screen.blit(self.noarrow, self.uprect)

        screen.blit(self.highlightc, places[self.item + index- 1])

#    def menu0start(self, screen):
