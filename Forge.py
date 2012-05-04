import pygame
import Equipment
import MakeRect


#repair function: not sure if prices are set to reasonable amounts

class Forge:
    def __init__(self):
        self.font = pygame.font.Font(None, 14)     

#        self.choice = 1

        self.itemsrect = pygame.Rect(128, 0, 192, 256)
        self.itemsbox = MakeRect.get(self.itemsrect)

        self.siderect = pygame.Rect(0, 0, 128, 256)
        self.sidebox = MakeRect.get(self.siderect)

        self.bottomrect = pygame.Rect(128, 256, 192, 128)
        self.bottombox = MakeRect.get(self.bottomrect)

        self.extrarect = pygame.Rect(0, 256, 128, 128)
        self.extrabox = MakeRect.get(self.extrarect)

        self.downarrow = pygame.image.load('images/menu/downarrow.png').convert_alpha()
        self.downrect = self.downarrow.get_rect()
        self.downrect.topleft = (self.itemsrect.x + self.itemsrect.width / 2, self.itemsrect.height - 20)

        self.uparrow = pygame.image.load('images/menu/uparrow.png').convert_alpha()
        self.uprect = self.uparrow.get_rect()
        self.uprect.topleft = (self.itemsrect.x + self.itemsrect.width / 2, self.itemsrect.y + 5)

        self.noarrow = pygame.image.load('images/menu/noarrow.png').convert_alpha()

    def drawmain(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(self.itemsbox, self.itemsrect)
        screen.blit(self.sidebox, self.siderect)
        screen.blit(self.bottombox, self.bottomrect)
        screen.blit(self.extrabox, self.extrarect)

    def showmoney(self, player, screen):
        screen.blit(self.extrabox, self.extrarect)
        text = self.font.render('Money:', True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.extrarect.x + 10, self.extrarect.y + 10))
        text = self.font.render('%d' % player.money, True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.extrarect.x + self.extrarect.width - 10 - text.get_clip().width, self.extrarect.y + 10))

    def getcharacter(self, player, screen):        
        msg = 'Select a character:'
        index = 0
        select = 1

        while True:
            done = False
            screen.blit(self.sidebox, self.siderect)

            text = self.font.render(msg, True, (255, 255, 255), (0, 0, 255))
            screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))
    
            for i in range(index, index + len(player.characters)):
                if i < len(player.characters):
                    text = self.font.render(player.characters[i].name, True, (255, 255, 255), (0, 0, 255))
                    screen.blit(text, (self.siderect.x + 10, 15 * i + 25))

            text = self.font.render(player.characters[select + index - 1].name, True, (200, 200, 0), (0, 0, 255))
            screen.blit(text, (self.siderect.x + 10, 15 * select + 10))

            if index + 14 < len(player.characters):
                screen.blit(self.downarrow, self.downrect)
            else:
                screen.blit(self.noarrow, self.downrect)
            if index > 0:
                screen.blit(self.uparrow, self.uprect)
            else:
                screen.blit(self.noarrow, self.uprect)
            pygame.display.flip()

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP]:
                            done = True
                            if select > 1:
                                if select + index - 1 > 0:
                                    text = self.font.render(player.characters[select + index - 1].name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (self.siderect.x + 10, 15 * select + 10))
                                    select -= 1    
                            elif select == 1 and index > 0:
                                    index -= 1                           
                        elif keys[pygame.K_DOWN]:
                            done = True
                            if select < 16:
                                if select + index < len(player.characters):
                                    text = self.font.render(player.characters[select + index - 1].name, True, (255, 255, 255), (0, 0, 255))
                                    screen.blit(text, (self.siderect.x + 10, 15 * select + 10))
                                    select += 1 
                            elif select == 16 and index + 16 < len(player.characters):
                                index += 1                                                       
                        elif keys[pygame.K_RETURN]:
                            return select + index - 1
                        elif keys[pygame.K_ESCAPE]:
                            return None

    def shop(self, player, screen):
        self.drawmain(screen)
        self.showmoney(player, screen)
        got = self.getcharacter(player, screen)
        if got == None:
            return 0
        character = player.characters[got]
        self.drawmain(screen)
        self.showmoney(player, screen)

        forging = True
        while True:
            done = False

            if forging:
                text = self.font.render('Forge (not added)', True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))
                text = self.font.render('Repair', True, (255, 255, 255), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
            else:
                text = self.font.render('Forge (not added)', True, (255, 255, 255), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))
                text = self.font.render('Repair', True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))

            pygame.display.update(self.siderect)

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                            if forging:
                                forging = False
                            else:
                                forging = True
                            done = True
                        elif keys[pygame.K_RETURN]:
                            temp = screen.copy()
                            if forging:
                                self.forge(player, character, screen)
                            else:
                                self.repair(player, character, screen)
                            done = True
                            screen.blit(temp, (0, 0))
                            self.showmoney(player, screen)
                            pygame.display.flip()

                        elif keys[pygame.K_ESCAPE]:
#                            temp = screen.copy()
                            got = self.getcharacter(player, screen)
                            if got == None:
                                return 0
                            character = player.characters[got]
                            self.drawmain(screen)
                            self.showmoney(player, screen)
                            done = True

    def forge(self, player, character, screen):
        self.drawmain(screen)
        self.showmoney(player, screen)
        screen.blit(self.sidebox, self.siderect)
        pygame.display.flip()

        self.drawmain(screen)
        self.showmoney(player, screen)

        forgeweapon = True
        while True:
            done = False

            if forgeweapon:
                text = self.font.render('Weapons', True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))
                text = self.font.render('Armor', True, (255, 255, 255), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
            elif forgeweapon:
                text = self.font.render('Weapons', True, (255, 255, 255), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))
                text = self.font.render('Armor', True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
            pygame.display.update(self.siderect)

            pygame.display.update(self.siderect)

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                            if forgeweapon:
                                forgeweapon = False
                            else:
                                forgeweapon = True
                            done = True
                        elif keys[pygame.K_RETURN]:
                            temp = screen.copy()
                            if forging:
                                self.forge(player, character, screen)
                            else:
                                self.repair(player, character, screen)
                            done = True
                            screen.blit(temp, (0, 0))
                            self.showmoney(player, screen)
                            pygame.display.flip()

                        elif keys[pygame.K_ESCAPE]:
                            return 0



       
    def inventory(self, player, screen, group):
        names = []
        prices = []
        if group == 1:
            names = self.weapons.keys()
            prices = self.weapons.values()
        elif group == 2:
            names = self.armors.keys()
            prices = self.armors.values()
        elif group == 3:
            names = self.items.keys()
            prices = self.items.values()
        
        pricespots = []
        for i in range(0, 16):            
            if i < len(prices):
                price = self.font.render('%d' % prices[i], True, (255, 255, 255), (0, 0, 255))
                pricespots.append(self.itemsrect.x + self.itemsrect.width - price.get_clip().width - 10)

        index = 0
        select = 1

        while True:
            done = False

            self.showmoney(player, screen)
            screen.blit(self.itemsbox, self.itemsrect)

            for i in range(index, index + 16):
                if i < len(names):                
                    text = self.font.render(names[i], True, (255, 255, 255), (0, 0, 255))
                    screen.blit(text, (self.itemsrect.x + 10, 15 * (i - index) + 10))
                    text = self.font.render('%d' % prices[i], True, (255, 255, 255), (0, 0, 255))
                    screen.blit(text, (pricespots[i - index], 15 * (i - index) + 10))

            if len(names) > 0:
                text = self.font.render(names[select + index - 1], True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (self.itemsrect.x + 10, 15 * select - 5))
                text = self.font.render('%d' % prices[select + index - 1], True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (pricespots[select - index - 1], 15 * select - 5))

            if index + 17 < len(names):
                screen.blit(self.downarrow, self.downrect)
            else:
                screen.blit(self.noarrow, self.downrect)
            if index > 0:
                screen.blit(self.uparrow, self.uprect)
            else:
                screen.blit(self.noarrow, self.uprect)
            pygame.display.flip()

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP]:
                            if index > 0 and select == 1:
                                done = True
                                index -= 1                           

                            elif select > 1:
                                done = True
                                if select - 1 > 0: 
                                    select -= 1    

                        elif keys[pygame.K_DOWN]:
                            if index + 17 < len(stuff) and select == 16:
                                done = True
                                index += 1                           
                            elif select < 16:
                                done = True
                                if select + 1 < 17 and select < len(stuff):
                                    select += 1    
                        elif keys[pygame.K_RETURN]:
                            temp = screen.copy()
                            if self.confirm(screen):
                                if not self.dopurchase(player, screen, stuff[select + index - 1].name, prices[select + index - 1]):
                                    self.problem(screen, 'Not enough money!')
                            screen.blit(temp, (0, 0))
                            pygame.display.flip()
                            done = True
                        elif keys[pygame.K_ESCAPE]:
                            return 0

    def repair(self, player, character, screen):
        stuff = character.equipment
        prices = []
        for thing in stuff:
            prices.append(Equipment.prices[thing.name] / 2)

        pricespots = []
        for i in range(0, 16):            
            if i < len(prices):
                price = self.font.render('%d' % prices[i], True, (255, 255, 255), (0, 0, 255))
                pricespots.append(self.itemsrect.x + self.itemsrect.width - price.get_clip().width - 10)

        index = 0
        select = 1

        while True:
            done = False

            self.showmoney(player, screen)
            screen.blit(self.itemsbox, self.itemsrect)

            for i in range(index, index + 16):
                if i < len(stuff):                
                    text = self.font.render(stuff[i].name, True, (255, 255, 255), (0, 0, 255))
                    screen.blit(text, (self.itemsrect.x + 10, 15 * (i - index) + 10))
                    text = self.font.render('%d' % prices[i], True, (255, 255, 255), (0, 0, 255))
                    screen.blit(text, (pricespots[i - index], 15 * (i - index) + 10))

            if len(stuff) > 0:
                text = self.font.render(stuff[select + index - 1].name, True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (self.itemsrect.x + 10, 15 * select - 5))
                text = self.font.render('%d' % prices[select + index - 1], True, (200, 200, 0), (0, 0, 255))
                screen.blit(text, (pricespots[select - index - 1], 15 * select - 5))

            if index + 17 < len(stuff):
                screen.blit(self.downarrow, self.downrect)
            else:
                screen.blit(self.noarrow, self.downrect)
            if index > 0:
                screen.blit(self.uparrow, self.uprect)
            else:
                screen.blit(self.noarrow, self.uprect)
            pygame.display.flip()

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP]:
                            if index > 0 and select == 1:
                                done = True
                                index -= 1                           

                            elif select > 1:
                                done = True
                                if select - 1 > 0: 
                                    select -= 1    

                        elif keys[pygame.K_DOWN]:
                            if index + 17 < len(stuff) and select == 16:
                                done = True
                                index += 1                           
                            elif select < 16:
                                done = True
                                if select + 1 < 17 and select < len(stuff):
                                    select += 1    
                        elif keys[pygame.K_RETURN]:
                            temp = screen.copy()
                            where = select + index - 1
                            if not self.repairitem(player, character, screen, stuff[where], prices[where]):
                                self.problem(screen, 'Not enough money!')
                            screen.blit(temp, (0, 0))
                            pygame.display.flip()
                            done = True
                        elif keys[pygame.K_ESCAPE]:
                            return 0

    def repairitem(self, player, character, screen, item, price):
#        if character.weapon == item:
#                temp = screen.copy()
#            if not self.confirm(screen):
#                self.problem(screen, message = "Can't repair an equipped item!")
#                screen.blit(temp, (0, 0))
#                pygame.display.flip()
#                return False
#            character.unequipweapon()
#        elif character.armor == item:
#                temp = screen.copy()
#            if not self.confirm(screen):
#                self.problem(screen, message = "Can't repair an equipped item!")
#                screen.blit(temp, (0, 0))
#                pygame.display.flip()
#                return False
#            character.unequiparmor()
        if player.money < price:
            return False
        if self.confirm(screen):
            player.money -= price
            item.repair()
            self.showmoney(player, screen)
            return True
        return False

    def dopurchase(self, player, screen, item, price):
        if player.money < price:
            return False
        player.money -= price
        self.showmoney(player, screen)
        if self.choice == 1:
            player.characters[self.getcharacter(player, screen)].equipment.append(Equipment.Weapon(item))
        elif self.choice == 2:
            player.characters[self.getcharacter(player, screen)].equipment.append(Equipment.Armor(item))
        elif self.choice == 3:
            player.characters[self.getcharacter(player, screen)].items.append(item)
        
        return True

    def problem(self, screen, message):
        text = self.font.render(message, True, (255, 255, 255), (0, 0, 255))

        size = text.get_clip()
        screensize = screen.get_clip()
        errorrect = pygame.Rect(((screensize.width - size.width) / 2) - 10, ((screensize.height - size.height) / 2) - 20, size.width + 20, size.height + 40)
        errorbox = MakeRect.get(errorrect)
        screen.blit(errorbox, errorrect)
        screen.blit(text, (errorrect.x + 10, errorrect.y + 10))
        pygame.display.update(errorrect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return 0


    def confirm(self, screen):
        screen.blit(self.sidebox, self.siderect)
        text = self.font.render('Are you sure?', True, (255, 255, 255), (0, 0, 255))
        screen.blit(text, (self.siderect.x + 10, self.siderect.y + 10))

        yes = True
        while True:
            if yes:
                text = self.font.render('Yes', True, (200, 200, 0), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
                text = self.font.render('No', True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 50))
            else:
                text = self.font.render('Yes', True, (255, 255, 255), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 30))
                text = self.font.render('No', True, (200, 200, 0), (0, 0, 255))			
                screen.blit(text, (self.siderect.x + 10, self.siderect.y + 50))
            pygame.display.update(self.siderect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()                    
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                        if yes:
                            yes = False
                        else:
                            yes = True
                    elif keys[pygame.K_RETURN]:
                        return yes
                    elif keys[pygame.K_ESCAPE]:
                        return False

