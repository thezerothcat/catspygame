import CellObject
import Map
import pygame
#from CellObject import *

class WaterCell:
    def __init__(self, pos, contents = None, contents2 = None):
        self.type = 'water'
        self.image = pygame.image.load('images/cells/water.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.contents = contents
        self.contents2 = contents2
        self.contents = contents
        self.contents2 = contents2
        if contents2 == None:
            self.walkable = False
        elif contents2.type == 'bridge':
            self.walkable = True
        else:
            self.walkable = False
        self.pathimage = pygame.image.load('images/cells/path.png').convert_alpha()
        self.targetimage = pygame.image.load('images/cells/target.png').convert_alpha()
        self.activeimage = pygame.image.load('images/cells/active.png').convert_alpha()
        self.red = False
        self.blue = False
        self.active = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.contents2 != None:
            screen.blit(self.contents2.image, self.rect)
        if self.contents != None:
            screen.blit(self.contents.image, self.rect)
        if self.blue:
            screen.blit(self.pathimage, self.rect)
        if self.red:
            screen.blit(self.targetimage, self.rect)
        if self.active:
            screen.blit(self.activeimage, self.rect)

    def addobject(self, contents):
        self.contents = contents
        self.walkable = False

    def removeobject(self):
        self.contents = None
        self.walkable = True


########################################################
#      		       Lava Cell 		       #
########################################################

class LavaCell:
    def __init__(self, pos, contents = None, contents2 = None):
        self.type = 'lava'
        self.image = pygame.image.load('images/cells/lava.png').convert_alpha()	
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.contents = contents
        self.contents2 = contents2
        if contents2 == None:
            self.walkable = False
        elif contents2.type == 'bridge':
            self.walkable = True
        else:
            self.walkable = False
        self.pathimage = pygame.image.load('images/cells/path.png').convert_alpha()
        self.targetimage = pygame.image.load('images/cells/target.png').convert_alpha()
        self.activeimage = pygame.image.load('images/cells/active.png').convert_alpha()
#        self.contents2 = contents2	
#        if contents == None:
#            self.contents = None
        self.red = False
        self.blue = False
        self.active = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.contents2 != None:
            screen.blit(self.contents2.image, self.rect)
        if self.contents != None:
            screen.blit(self.contents.image, self.rect)
        if self.blue:
            screen.blit(self.pathimage, self.rect)
        if self.red:
            screen.blit(self.targetimage, self.rect)
        if self.active:
            screen.blit(self.activeimage, self.rect)

    def addobject(self, contents):
        self.contents = contents
        self.walkable = False

    def removeobject(self):
        self.contents = None
        self.walkable = True

########################################################
#      		      Grass Cell 		       #
########################################################

class GrassCell:
    def __init__(self, pos, contents = None, contents2 = None):
        self.type = 'grass'
        self.image = pygame.image.load('images/cells/grass.png').convert_alpha()
        self.pathimage = pygame.image.load('images/cells/path.png').convert_alpha()
        self.targetimage = pygame.image.load('images/cells/target.png').convert_alpha()
        self.activeimage = pygame.image.load('images/cells/active.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.red = False
        self.blue = False
        self.active = False
        self.contents2 = contents2	
        if contents == None:
            self.contents = None
            self.walkable = True
        else:
            self.contents = contents
            self.walkable = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.contents2 != None:
            screen.blit(self.contents2.image, self.rect)
        if self.contents != None:
            screen.blit(self.contents.image, self.rect)
        if self.blue:
            screen.blit(self.pathimage, self.rect)
        if self.red:
            screen.blit(self.targetimage, self.rect)
        if self.active:
            screen.blit(self.activeimage, self.rect)
#		pygame.display.update(self.rect)			

    def addobject(self, contents):
        self.contents = contents
        self.walkable = False

    def removeobject(self):
        self.contents = None
        self.walkable = True


