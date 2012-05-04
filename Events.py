import pygame
import Map
import CellObject
#import Player
import Stats
from Characters import Character

class Event:
    def __init__(self, number):
        self.number = number
        self.font = pygame.font.Font(None, 14)
        self.highlight = pygame.image.load('images/menu/highlight2.png').convert_alpha()
        self.unhighlight = pygame.image.load('images/menu/unhighlight2.png').convert_alpha()
        self.done = False
        if self.number == 1:
            self.character = Character('Kamikaze')
            self.message = 'A new character wants to join! Is this ok?'
        elif self.number == 2:
            self.message = "There's a wallet lying on the ground. Pick it up?"

    def choice(self, screen, menu):
        menu.display(screen)
        textrect = menu.textrect
        text = self.font.render(self.message, True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (textrect.x + 15, textrect.y + 15))
        text = self.font.render('Yes', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (textrect.x + 95, textrect.y + 40))
        text = self.font.render('No', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (textrect.x + 175, textrect.y + 40))

        yes = True

        while True:
            if yes:
                screen.blit(self.unhighlight, (textrect.x + 170, textrect.y + 35))
                screen.blit(self.highlight, (textrect.x + 90, textrect.y + 35))
            else:
                screen.blit(self.unhighlight, (textrect.x + 90, textrect.y + 35))
                screen.blit(self.highlight, (textrect.x + 170, textrect.y + 35))
            pygame.display.update(textrect)

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

    def happen(self, visitor, screen, cmap):
        if not self.done:
            if self.number == 1:
                yes = self.choice(screen, cmap.menu)
                if yes:
                    cell = None
                    if (visitor.rect.x - cmap.cellsize) >= 0:
                        cell = cmap.cells[(visitor.rect.x - cmap.cellsize, visitor.rect.y)]
                        if cell.walkable:
                            self.visited = True
                            self.character.rect.topleft = cell.rect.topleft
                            cell.addobject(self.character)
                            cmap.player1.characters.append(self.character)
                            cell.draw(screen)
                            pygame.display.update(cell.rect)
                            self.character.prepare(screen, cmap)
                        else:
                            cell = None
                    if cell == None:
                        if (visitor.rect.y - cmap.cellsize) >= 0:
                            cell = cmap.cells[(visitor.rect.x, visitor.rect.y - cmap.cellsize)]
                            if cell.walkable:
                                self.visited = True
                                self.character.rect.topleft = cell.rect.topleft
                                cell.addobject(self.character)
                                cmap.player1.characters.append(self.character)
                                cell.draw(screen)
                                pygame.display.update(cell.rect)
                                self.character.prepare(screen, cmap)
                            else:
                                cell = None
                        if cell == None:
                            if (visitor.rect.x + cmap.cellsize) <= 288:
                                cell = cmap.cells[(visitor.rect.x + cmap.cellsize, visitor.rect.y)]
                                if cell.walkable:
                                    self.visited = True
                                    self.character.rect.topleft = cell.rect.topleft
                                    cmap.player1.characters.append(self.character)
                                    cell.addobject(self.character)
                                    cell.draw(screen)
                                    pygame.display.update(cell.rect)
                                    self.character.prepare(screen, cmap)
                                else:
                                    cell = None
                            if cell == None:
                                if (visitor.rect.y + cmap.cellsize) <= 288:
                                    cell = cmap.cells[(visitor.rect.x, visitor.rect.y + cmap.cellsize)]
                                    if cell.walkable:
                                        self.visited = True
                                        cmap.player1.characters.append(self.character)
                                        cell.addobject(self.character)
                                        cell.draw(screen)
                                        pygame.display.update(cell.rect)
                                        self.character.prepare(screen, cmap)
                                    else:
                                        cell = None
                                if cell == None:
                                    cmap.menu.display(screen)
                                    text = self.font.render('The character has nowhere to go!', True, (255, 255, 255), (0, 0, 255))			
                                    screen.blit(text, (cmap.menu.textrect.x + 15, cmap.menu.textrect.y + 15))
                                    pygame.display.update(cmap.menu.textrect)   
                    self.done = True
            elif self.number == 2:
                yes = self.choice(screen, cmap.menu)
                if yes:
                    cmap.player1.money += 15
                    text = self.font.render('You gained $50!', True, (255, 255, 255), (0, 0, 255))			
                    screen.blit(text, (cmap.menu.textrect.x + 15, cmap.menu.textrect.y + 15))
                    pygame.display.update(cmap.menu.textrect)   
                    self.done = True
                                    
