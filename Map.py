import Cell
import CellObject
from Characters import Character
import Stats
import pygame
import os
import sys
import Menu
import Items
import Player
import Paths
import Events
from Paths import *

class Map:
    def __init__(self, player):
        self.player1 = player

        if self.player1.progress == 0:
#            villainstats = Stats.Stats(22, 8, 5, 3)
#            villain = CellObject.Enemy('Boss', 'evil.png', (288, 0), villainstats, 2)

            villainstats2 = Stats.Stats(15, 5, 3, 2, 2, 2, 2, 5)
            villain2 = CellObject.Enemy('Angry', 'angry.png', (64, 128), villainstats2, 2)
				
#            self.enemies = [villain, villain2]
            self.enemies = [villain2]

            chest1 = CellObject.TreasureChest((32, 32), 'Miracle')

            event1 = Events.Event(1)
            house1 = CellObject.House((32, 224), event1)

            plant1 = CellObject.AppleTree((64, 64))

            obj1 = CellObject.Mountain((96, 0))
            obj2 = CellObject.Rock((96, 96))
            obj3 = CellObject.PineTree((0, 0))

            self.cells = {}
            self.cellsize = 32
            self.turns = 0
            self.menu = Menu.Menu()

            #column one
            self.cells[(0,0)] = Cell.GrassCell((0,0), obj3)
            self.cells[(0,32)] = Cell.GrassCell((0,32))
            self.cells[(0,64)] = Cell.GrassCell((0,64))
            self.cells[(0,96)] = Cell.GrassCell((0,96))
            self.cells[(0,128)] = Cell.GrassCell((0,128))
            self.cells[(0,160)] = Cell.GrassCell((0,160))
            self.cells[(0,192)] = Cell.GrassCell((0,192))
            self.cells[(0,224)] = Cell.GrassCell((0,224))
            self.cells[(0,256)] = Cell.GrassCell((0,256))
            self.cells[(0,288)] = Cell.GrassCell((0,288))

            #column two
            self.cells[(32,0)] = Cell.GrassCell((32,0))
            self.cells[(32,32)] = Cell.GrassCell((32,32), contents2 = chest1)
            self.cells[(32,64)] = Cell.GrassCell((32,64))
            self.cells[(32,96)] = Cell.GrassCell((32,96))
            self.cells[(32,128)] = Cell.GrassCell((32,128))
            self.cells[(32,160)] = Cell.GrassCell((32,160))
            self.cells[(32,192)] = Cell.GrassCell((32,192))
            self.cells[(32,224)] = Cell.GrassCell((32,224), contents2 = house1)
            self.cells[(32,256)] = Cell.GrassCell((32,256))
            self.cells[(32,288)] = Cell.GrassCell((32,288))

            #column three
            self.cells[(64,0)] = Cell.GrassCell((64,0))
            self.cells[(64,32)] = Cell.GrassCell((64,32))
            self.cells[(64,64)] = Cell.GrassCell((64,64), contents2 = plant1)
            self.cells[(64,96)] = Cell.GrassCell((64,96))
            self.cells[(64,128)] = Cell.GrassCell((64,128), villain2)
            self.cells[(64,160)] = Cell.GrassCell((64,160))
            self.cells[(64,192)] = Cell.GrassCell((64,192))
            self.cells[(64,224)] = Cell.GrassCell((64,224))
            self.cells[(64,256)] = Cell.GrassCell((64,256))
            self.cells[(64,288)] = Cell.GrassCell((64,288))

            #column four
            self.cells[(96,0)] = Cell.GrassCell((96,0), obj1)
            self.cells[(96,32)] = Cell.GrassCell((96,32))
            self.cells[(96,64)] = Cell.GrassCell((96,64))
            self.cells[(96,96)] = Cell.GrassCell((96,96), obj2)
            self.cells[(96,128)] = Cell.GrassCell((96,128))
            self.cells[(96,160)] = Cell.GrassCell((96,160))
            self.cells[(96,192)] = Cell.GrassCell((96,192))
            self.cells[(96,224)] = Cell.GrassCell((96,224))
            self.cells[(96,256)] = Cell.GrassCell((96,256))
            self.cells[(96,288)] = Cell.GrassCell((96,288))

            self.cells[(128,0)] = Cell.GrassCell((128,0))
            self.cells[(128,32)] = Cell.GrassCell((128,32))
            self.cells[(128,64)] = Cell.GrassCell((128,64))
            self.cells[(128,96)] = Cell.GrassCell((128,96))
            self.cells[(128,128)] = Cell.WaterCell((128,128))
            self.cells[(128,160)] = Cell.WaterCell((128,160))
            self.cells[(128,192)] = Cell.GrassCell((128,192))
            self.cells[(128,224)] = Cell.GrassCell((128,224))
            self.cells[(128,256)] = Cell.GrassCell((128,256))
            self.cells[(128,288)] = Cell.GrassCell((128,288))

            self.cells[(160,0)] = Cell.GrassCell((160,0))
            self.cells[(160,32)] = Cell.GrassCell((160,32))
            self.cells[(160,64)] = Cell.GrassCell((160,64))
            self.cells[(160,96)] = Cell.GrassCell((160,96))
            self.cells[(160,128)] = Cell.WaterCell((160,128))
            self.cells[(160,160)] = Cell.WaterCell((160,160))
            self.cells[(160,192)] = Cell.GrassCell((160,192))
            self.cells[(160,224)] = Cell.GrassCell((160,224))
            self.cells[(160,256)] = Cell.GrassCell((160,256))
            self.cells[(160,288)] = Cell.GrassCell((160,288))
		
            self.cells[(192,0)] = Cell.GrassCell((192,0))
            self.cells[(192,32)] = Cell.GrassCell((192,32))
            self.cells[(192,64)] = Cell.GrassCell((192,64))
            self.cells[(192,96)] = Cell.GrassCell((192,96))
            self.cells[(192,128)] = Cell.GrassCell((192,128))
            self.cells[(192,160)] = Cell.GrassCell((192,160))
            self.cells[(192,192)] = Cell.GrassCell((192,192))
            self.cells[(192,224)] = Cell.GrassCell((192,224))
            self.cells[(192,256)] = Cell.GrassCell((192,256))
            self.cells[(192,288)] = Cell.GrassCell((192,288))

            self.cells[(224,0)] = Cell.GrassCell((224,0))
            self.cells[(224,32)] = Cell.GrassCell((224,32))
            self.cells[(224,64)] = Cell.GrassCell((224,64))
            self.cells[(224,96)] = Cell.GrassCell((224,96))
            self.cells[(224,128)] = Cell.GrassCell((224,128))
            self.cells[(224,160)] = Cell.GrassCell((224,160))
            self.cells[(224,192)] = Cell.GrassCell((224,192))
            self.cells[(224,224)] = Cell.GrassCell((224,224))
            self.cells[(224,256)] = Cell.GrassCell((224,256))
            self.cells[(224,288)] = Cell.GrassCell((224,288))
		
            self.cells[(256,0)] = Cell.GrassCell((256,0))
            self.cells[(256,32)] = Cell.GrassCell((256,32))
            self.cells[(256,64)] = Cell.GrassCell((256,64))
            self.cells[(256,96)] = Cell.GrassCell((256,96))
            self.cells[(256,128)] = Cell.GrassCell((256,128))
            self.cells[(256,160)] = Cell.GrassCell((256,160))
            self.cells[(256,192)] = Cell.GrassCell((256,192))
            self.cells[(256,224)] = Cell.GrassCell((256,224))
            self.cells[(256,256)] = Cell.GrassCell((256,256))
            self.cells[(256,288)] = Cell.GrassCell((256,288))

            self.cells[(288,0)] = Cell.GrassCell((288,0))#, villain)
            self.cells[(288,32)] = Cell.GrassCell((288,32))
            self.cells[(288,64)] = Cell.GrassCell((288,64))
            self.cells[(288,96)] = Cell.GrassCell((288,96))
            self.cells[(288,128)] = Cell.GrassCell((288,128))
            self.cells[(288,160)] = Cell.GrassCell((288,160))
            self.cells[(288,192)] = Cell.GrassCell((288,192))
            self.cells[(288,224)] = Cell.GrassCell((288,224))
            self.cells[(288,256)] = Cell.GrassCell((288,256))
            self.cells[(288,288)] = Cell.GrassCell((288,288))

            ##################################################
            #     Player Character Positioning Goes Here     #
            ##################################################

#            for character in self.player1.characters:
#                if character.name == 'Hero':
            self.cells[(32, 96)].contents = self.player1.characters[0]
            self.player1.characters[0].rect.topleft = (32, 96)

        elif self.player1.progress % 2 == 1:
            villainstats = Stats.Stats(22, 8, 5, 5, 5, 4, 4, 3)
            villain = CellObject.Enemy('Boss', 'evil.png', (288, 0), villainstats, 2, deathexp = 57)

            villainstats2 = Stats.Stats(15, 5, 3, 2, 2, 2, 2, 5)
            villain2 = CellObject.Enemy('Angry', 'angry.png', (64, 128), villainstats2, 2)
				
            self.enemies = [villain, villain2]

            self.cells = {}
            self.cellsize = 32
            self.turns = 0
            self.menu = Menu.Menu()

            #column one
            self.cells[(0,0)] = Cell.GrassCell((0,0), )
            self.cells[(0,32)] = Cell.GrassCell((0,32))
            self.cells[(0,64)] = Cell.GrassCell((0,64))
            self.cells[(0,96)] = Cell.GrassCell((0,96))
            self.cells[(0,128)] = Cell.GrassCell((0,128))
            self.cells[(0,160)] = Cell.GrassCell((0,160))
            self.cells[(0,192)] = Cell.GrassCell((0,192))
            self.cells[(0,224)] = Cell.GrassCell((0,224))
            self.cells[(0,256)] = Cell.GrassCell((0,256))
            self.cells[(0,288)] = Cell.GrassCell((0,288))

            #column two
            self.cells[(32,0)] = Cell.GrassCell((32,0))
            self.cells[(32,32)] = Cell.GrassCell((32,32), contents2 = CellObject.TreasureChest((32, 32), 'Apple'))
            self.cells[(32,64)] = Cell.GrassCell((32,64))
            self.cells[(32,96)] = Cell.GrassCell((32,96))
            self.cells[(32,128)] = Cell.GrassCell((32,128))
            self.cells[(32,160)] = Cell.GrassCell((32,160))
            self.cells[(32,192)] = Cell.GrassCell((32,192), CellObject.Rock((32, 192)))
            self.cells[(32,224)] = Cell.GrassCell((32,224))
            self.cells[(32,256)] = Cell.GrassCell((32,256))
            self.cells[(32,288)] = Cell.GrassCell((32,288))

            #column three
            self.cells[(64,0)] = Cell.GrassCell((64,0))
            self.cells[(64,32)] = Cell.GrassCell((64,32))
            self.cells[(64,64)] = Cell.GrassCell((64,64))
            self.cells[(64,96)] = Cell.GrassCell((64,96))
            self.cells[(64,128)] = Cell.GrassCell((64,128), villain2)
            self.cells[(64,160)] = Cell.GrassCell((64,160))
            self.cells[(64,192)] = Cell.GrassCell((64,192))
            self.cells[(64,224)] = Cell.GrassCell((64,224))
            self.cells[(64,256)] = Cell.GrassCell((64,256))
            self.cells[(64,288)] = Cell.GrassCell((64,288))

            #column four
            self.cells[(96,0)] = Cell.GrassCell((96,0), CellObject.Mountain((96, 0)))
            self.cells[(96,32)] = Cell.GrassCell((96,32), CellObject.Mountain((96, 32)))
            self.cells[(96,64)] = Cell.GrassCell((96,64))
            self.cells[(96,96)] = Cell.GrassCell((96,96))
            self.cells[(96,128)] = Cell.GrassCell((96,128))
            self.cells[(96,160)] = Cell.GrassCell((96,160))
            self.cells[(96,192)] = Cell.GrassCell((96,192))
            self.cells[(96,224)] = Cell.GrassCell((96,224))
            self.cells[(96,256)] = Cell.GrassCell((96,256))
            self.cells[(96,288)] = Cell.GrassCell((96,288))

            self.cells[(128,0)] = Cell.GrassCell((128,0))
            self.cells[(128,32)] = Cell.GrassCell((128,32))
            self.cells[(128,64)] = Cell.GrassCell((128,64), CellObject.Mountain((128, 64)))
            self.cells[(128,96)] = Cell.GrassCell((128,96))
            self.cells[(128,128)] = Cell.WaterCell((128,128))
            self.cells[(128,160)] = Cell.WaterCell((128,160), contents2 = CellObject.HBridge((128, 160)))
            self.cells[(128,192)] = Cell.WaterCell((128,192))
            self.cells[(128,224)] = Cell.GrassCell((128,224))
            self.cells[(128,256)] = Cell.GrassCell((128,256))
            self.cells[(128,288)] = Cell.GrassCell((128,288))

            self.cells[(160,0)] = Cell.GrassCell((160,0))
            self.cells[(160,32)] = Cell.GrassCell((160,32))
            self.cells[(160,64)] = Cell.GrassCell((160,64))
            self.cells[(160,96)] = Cell.GrassCell((160,96), contents2 = CellObject.AppleTree((160, 96)))
            self.cells[(160,128)] = Cell.WaterCell((160,128))
            self.cells[(160,160)] = Cell.WaterCell((160,160), contents2 = CellObject.HBridge((160, 160)))
            self.cells[(160,192)] = Cell.WaterCell((160,192))
            self.cells[(160,224)] = Cell.GrassCell((160,224))
            self.cells[(160,256)] = Cell.GrassCell((160,256), CellObject.PineTree((160, 256)))
            self.cells[(160,288)] = Cell.GrassCell((160,288))
		
            self.cells[(192,0)] = Cell.GrassCell((192,0))
            self.cells[(192,32)] = Cell.GrassCell((192,32))
            self.cells[(192,64)] = Cell.GrassCell((192,64))
            self.cells[(192,96)] = Cell.GrassCell((192,96))
            self.cells[(192,128)] = Cell.GrassCell((192,128), CellObject.Rock((192, 128)))
            self.cells[(192,160)] = Cell.GrassCell((192,160))
            self.cells[(192,192)] = Cell.GrassCell((192,192))
            self.cells[(192,224)] = Cell.GrassCell((192,224))
            self.cells[(192,256)] = Cell.GrassCell((192,256))
            self.cells[(192,288)] = Cell.GrassCell((192,288))

            self.cells[(224,0)] = Cell.GrassCell((224,0))
            self.cells[(224,32)] = Cell.GrassCell((224,32))
            self.cells[(224,64)] = Cell.GrassCell((224,64), contents2 = CellObject.House((224, 64), Events.Event(2)))
            self.cells[(224,96)] = Cell.GrassCell((224,96))
            self.cells[(224,128)] = Cell.GrassCell((224,128))
            self.cells[(224,160)] = Cell.GrassCell((224,160))
            self.cells[(224,192)] = Cell.GrassCell((224,192))
            self.cells[(224,224)] = Cell.GrassCell((224,224))
            self.cells[(224,256)] = Cell.GrassCell((224,256))
            self.cells[(224,288)] = Cell.GrassCell((224,288))
		
            self.cells[(256,0)] = Cell.GrassCell((256,0))
            self.cells[(256,32)] = Cell.GrassCell((256,32))
            self.cells[(256,64)] = Cell.GrassCell((256,64))
            self.cells[(256,96)] = Cell.GrassCell((256,96))
            self.cells[(256,128)] = Cell.GrassCell((256,128))
            self.cells[(256,160)] = Cell.GrassCell((256,160))
            self.cells[(256,192)] = Cell.GrassCell((256,192))
            self.cells[(256,224)] = Cell.GrassCell((256,224))
            self.cells[(256,256)] = Cell.GrassCell((256,256))
            self.cells[(256,288)] = Cell.GrassCell((256,288))

            self.cells[(288,0)] = Cell.GrassCell((288,0), villain)
            self.cells[(288,32)] = Cell.GrassCell((288,32))
            self.cells[(288,64)] = Cell.GrassCell((288,64))
            self.cells[(288,96)] = Cell.GrassCell((288,96))
            self.cells[(288,128)] = Cell.GrassCell((288,128), CellObject.PineTree((288, 128)))
            self.cells[(288,160)] = Cell.GrassCell((288,160))
            self.cells[(288,192)] = Cell.GrassCell((288,192))
            self.cells[(288,224)] = Cell.GrassCell((288,224))
            self.cells[(288,256)] = Cell.GrassCell((288,256))
            self.cells[(288,288)] = Cell.GrassCell((288,288))

            ##################################################
            #     Player Character Positioning Goes Here     #
            ##################################################

            self.cells[(32, 96)].contents = self.player1.characters[0]
            self.player1.characters[0].rect.topleft = (32, 96)

            for character in self.player1.characters:
#                if character.name == 'Hero':
#                    self.cells[(32, 96)].contents = character
#                    character.rect.topleft = (32, 96)
                if character.name == 'Kamikaze':
                    self.cells[(160, 288)].contents = character
                    character.rect.topleft = (160, 288)
        elif self.player1.progress % 2 == 0:
            villainstats = Stats.Stats(22, 8, 5, 5, 5, 4, 4, 3)
            villain = CellObject.Enemy('Boss', 'evil.png', (288, 0), villainstats, 2, deathexp = 57)

            villainstats2 = Stats.Stats(15, 5, 3, 2, 2, 2, 2, 5)
            villain2 = CellObject.Enemy('Angry', 'angry.png', (64, 128), villainstats2, 2)
				
            self.enemies = [villain, villain2]

            self.cells = {}
            self.cellsize = 32
            self.turns = 0
            self.menu = Menu.Menu()

            #column one
            self.cells[(0,0)] = Cell.GrassCell((0,0), CellObject.PineTree((0, 0)))
            self.cells[(0,32)] = Cell.GrassCell((0,32))
            self.cells[(0,64)] = Cell.GrassCell((0,64))
            self.cells[(0,96)] = Cell.GrassCell((0,96), CellObject.PineTree((0, 96)))
            self.cells[(0,128)] = Cell.GrassCell((0,128))
            self.cells[(0,160)] = Cell.GrassCell((0,160))
            self.cells[(0,192)] = Cell.GrassCell((0,192))
            self.cells[(0,224)] = Cell.GrassCell((0,224))
            self.cells[(0,256)] = Cell.GrassCell((0,256))
            self.cells[(0,288)] = Cell.GrassCell((0,288), contents2 = CellObject.House((0, 288), Events.Event(2)))

            #column two
            self.cells[(32,0)] = Cell.GrassCell((32,0))
            self.cells[(32,32)] = Cell.GrassCell((32,32), CellObject.PineTree((32, 32)))
            self.cells[(32,64)] = Cell.GrassCell((32,64))
            self.cells[(32,96)] = Cell.GrassCell((32,96))
            self.cells[(32,128)] = Cell.GrassCell((32,128))
            self.cells[(32,160)] = Cell.GrassCell((32,160))
            self.cells[(32,192)] = Cell.GrassCell((32,192))
            self.cells[(32,224)] = Cell.GrassCell((32,224))
            self.cells[(32,256)] = Cell.GrassCell((32,256))
            self.cells[(32,288)] = Cell.GrassCell((32,288))

            #column three
            self.cells[(64,0)] = Cell.GrassCell((64,0))
            self.cells[(64,32)] = Cell.GrassCell((64,32), CellObject.PineTree((64, 32)))
            self.cells[(64,64)] = Cell.GrassCell((64,64), contents2 = CellObject.AppleTree((64, 64)))
            self.cells[(64,96)] = Cell.GrassCell((64,96))
            self.cells[(64,128)] = Cell.GrassCell((64,128), villain2)
            self.cells[(64,160)] = Cell.GrassCell((64,160))
            self.cells[(64,192)] = Cell.GrassCell((64,192), CellObject.Mountain((64, 192)))
            self.cells[(64,224)] = Cell.WaterCell((64,224))
            self.cells[(64,256)] = Cell.WaterCell((64,256))
            self.cells[(64,288)] = Cell.WaterCell((64,288))

            #column four
            self.cells[(96,0)] = Cell.GrassCell((96,0))
            self.cells[(96,32)] = Cell.GrassCell((96,32))
            self.cells[(96,64)] = Cell.GrassCell((96,64))
            self.cells[(96,96)] = Cell.GrassCell((96,96), CellObject.Rock((96, 96)))
            self.cells[(96,128)] = Cell.GrassCell((96,128))
            self.cells[(96,160)] = Cell.GrassCell((96,160))
            self.cells[(96,192)] = Cell.GrassCell((96,192))
            self.cells[(96,224)] = Cell.WaterCell((96,224), contents2 = CellObject.VBridge((96, 224)))
            self.cells[(96,256)] = Cell.GrassCell((96,256))
            self.cells[(96,288)] = Cell.GrassCell((96,288))

            self.cells[(128,0)] = Cell.GrassCell((128,0))
            self.cells[(128,32)] = Cell.GrassCell((128,32))
            self.cells[(128,64)] = Cell.GrassCell((128,64))
            self.cells[(128,96)] = Cell.GrassCell((128,96))
            self.cells[(128,128)] = Cell.GrassCell((128,128))
            self.cells[(128,160)] = Cell.GrassCell((128,160), contents2 = CellObject.AppleTree((128, 160)))
            self.cells[(128,192)] = Cell.GrassCell((128,192))
            self.cells[(128,224)] = Cell.WaterCell((128,224))
            self.cells[(128,256)] = Cell.GrassCell((128,256))
            self.cells[(128,288)] = Cell.GrassCell((128,288))

            self.cells[(160,0)] = Cell.GrassCell((160,0))
            self.cells[(160,32)] = Cell.GrassCell((160,32))
            self.cells[(160,64)] = Cell.GrassCell((160,64))
            self.cells[(160,96)] = Cell.GrassCell((160,96))
            self.cells[(160,128)] = Cell.GrassCell((160,128))
            self.cells[(160,160)] = Cell.GrassCell((160,160))
            self.cells[(160,192)] = Cell.GrassCell((160,192))
            self.cells[(160,224)] = Cell.WaterCell((160,224), CellObject.Rock((160, 224)))
            self.cells[(160,256)] = Cell.GrassCell((160,256))
            self.cells[(160,288)] = Cell.GrassCell((160,288))
		
            self.cells[(192,0)] = Cell.GrassCell((192,0))
            self.cells[(192,32)] = Cell.GrassCell((192,32))
            self.cells[(192,64)] = Cell.GrassCell((192,64), contents2 = CellObject.AppleTree((192, 64)))
            self.cells[(192,96)] = Cell.GrassCell((192,96))
            self.cells[(192,128)] = Cell.GrassCell((192,128))
            self.cells[(192,160)] = Cell.GrassCell((192,160))
            self.cells[(192,192)] = Cell.GrassCell((192,192))
            self.cells[(192,224)] = Cell.WaterCell((192,224), contents2 = CellObject.VBridge((192, 224)))
            self.cells[(192,256)] = Cell.GrassCell((192,256))
            self.cells[(192,288)] = Cell.GrassCell((192,288))

            self.cells[(224,0)] = Cell.GrassCell((224,0))
            self.cells[(224,32)] = Cell.GrassCell((224,32))
            self.cells[(224,64)] = Cell.GrassCell((224,64))
            self.cells[(224,96)] = Cell.GrassCell((224,96))
            self.cells[(224,128)] = Cell.GrassCell((224,128))
            self.cells[(224,160)] = Cell.GrassCell((224,160))
            self.cells[(224,192)] = Cell.GrassCell((224,192), CellObject.Mountain((224, 192)))
            self.cells[(224,224)] = Cell.WaterCell((224,224))
            self.cells[(224,256)] = Cell.WaterCell((224,256))
            self.cells[(224,288)] = Cell.WaterCell((224,288))
		
            self.cells[(256,0)] = Cell.GrassCell((256,0))
            self.cells[(256,32)] = Cell.GrassCell((256,32))
            self.cells[(256,64)] = Cell.GrassCell((256,64))
            self.cells[(256,96)] = Cell.GrassCell((256,96))
            self.cells[(256,128)] = Cell.GrassCell((256,128))
            self.cells[(256,160)] = Cell.GrassCell((256,160))
            self.cells[(256,192)] = Cell.GrassCell((256,192))
            self.cells[(256,224)] = Cell.GrassCell((256,224))
            self.cells[(256,256)] = Cell.GrassCell((256,256))
            self.cells[(256,288)] = Cell.GrassCell((256,288))

            self.cells[(288,0)] = Cell.GrassCell((288,0), villain)
            self.cells[(288,32)] = Cell.GrassCell((288,32))
            self.cells[(288,64)] = Cell.GrassCell((288,64))
            self.cells[(288,96)] = Cell.GrassCell((288,96))
            self.cells[(288,128)] = Cell.GrassCell((288,128))
            self.cells[(288,160)] = Cell.GrassCell((288,160))
            self.cells[(288,192)] = Cell.GrassCell((288,192))
            self.cells[(288,224)] = Cell.GrassCell((288,224))
            self.cells[(288,256)] = Cell.GrassCell((288,256), contents2 = CellObject.TreasureChest((288, 256), 'Sticks & Stones'))
            self.cells[(288,288)] = Cell.GrassCell((288,288))

            ##################################################
            #     Player Character Positioning Goes Here     #
            ##################################################

            self.cells[(128, 288)].contents = self.player1.characters[0]
            self.player1.characters[0].rect.topleft = (128, 288)

            for character in self.player1.characters:
#                if character.name == 'Hero':
#                    self.cells[(128, 288)].contents = character
#                    character.rect.topleft = (128, 288)
                if character.name == 'Kamikaze':
                    self.cells[(160, 288)].contents = character
                    character.rect.topleft = (160, 288)
                    self.enemies = [villain, villain2]

        for i in range(0, self.player1.progress / 2):
            for enemy in self.enemies:
                enemy.level()            


    def draw(self, screen):
#    		pygame.mixer.music.load("songs/songHome.mp3")
#   		pygame.mixer.music.play()
		
        for cell in self.cells.values():
            cell.draw(screen)

        self.menu.display(screen)

    def play(self, screen):
        self.draw(screen)
        pygame.display.flip()

        for character in self.player1.characters:
            character.prepare(screen, self)

        for enemy in self.enemies:
            enemy.prepare(screen, self)

        while True:
            victory = self.turn(screen)

            if victory != 0:
#                for character in self.player1.characters:
#                    character.restore()
                font = pygame.font.Font(None, 60, bold = True)
                if victory == 1:
                    t = font.render('You win!', False, (255, 20, 0))
                elif victory == 2:
                    t = font.render('You lose...', False, (255, 20, 0))
                screen.blit(t, (80, 160))
                pygame.display.flip()
                pygame.time.wait(3000)
                return victory

            for character in self.player1.characters:
                if character.alive:
                    character.prepare(screen, self)
            for enemy in self.enemies:
                if enemy.alive:
                    enemy.prepare(screen, self)


    def turn(self, screen):
        done = False
        while not done:
            done = True
            for character in self.player1.characters:
                if character.alive and not character.hadturn:
                    done = False
            for character in self.player1.characters:
                if character.alive and not character.hadturn:
                    z = character.turn(screen, self)
                    if z != 0:
                        return z
                    win = self.victorycheck()
                    if win != 0:
                        return win

        for enemy in self.enemies:
            if enemy.alive:
                enemy.turn(screen, self)
                win = self.victorycheck()
                if win != 0:
                    return win

#        for neutral in self.neutral:
#            neutral.turn(screen, self)

        return self.victorycheck()
        self.turns += 1

    def victorycheck(self):
        enemyvictory = True
        for character in self.player1.characters:
            if character.alive:
                enemyvictory = False
        if enemyvictory:
            return 2

        playervictory = True
        for enemy in self.enemies:
            if enemy.alive:
                playervictory = False
        if playervictory:
            return 1
        return 0

    def send(self):
        enemies = []
        for enemy in self.enemies:
            enemies.append(enemy.send())
        cells = []
        for cell in self.cells:
            cells.append(cell.send())

        data = {'player':self.player1.send(), 'other':{'turns':self.turns, 'enemies':enemies, 'cells':cells}}

        return data

    def receive(self, data):
        self.player1.receive(data['player'])
        self.turns = data['other']['turns']
        enemies = []
        for enemy_data in data['other']['enemies']:
            dummy = CellObject.Enemy('Angry', 'angry.png', (64, 128), Stats.Stats(15, 5, 3, 2, 2, 2, 2, 5), 2)
            enemies.append(dummy.receive(enemy_data))
        self.enemies = enemies

        cells = []
        for cell_data in data['other']['cells']:
            dummy = CellObject.Enemy('Angry', 'angry.png', (64, 128), Stats.Stats(15, 5, 3, 2, 2, 2, 2, 5), 2)
            cells.append(dummy.receive(enemy_data))
        self.cells = cells

        
        


