import pygame, sys,os
from pygame.locals import * 

WIDTH = 320
HEIGHT = 384

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat's Game") 
screen = pygame.display.get_surface() 

import Map
import Player
import PlayerScreen
import TitleScreen
import Scene

#player1 = TitleScreen.show(player, screen)
#premenu = PlayerScreen.PlayerScreen()

#player1.number = 2
#quit = 1

premenu = PlayerScreen.PlayerScreen(0)

while True:
    player1 = TitleScreen.main_screen(screen)
#    print player1.characters[0].stats.hp.current
##########show error message

    while True:
        if player1.progress > 0:
            if premenu.mainscreen(player1, screen) < 0:
                break

        Scene.Scene(screen, player1.progress)
        level = Map.Map(player1)
        victory = level.play(screen)

        if victory == 2:
            screen.fill((0, 0, 0))
            message = pygame.font.Font(None, 32)
            text = message.render('You lose!', True, (255, 255, 255), (0, 0, 0))
            screen.blit(text, (102, 178))
            pygame.display.update()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        waiting = False
            del player1
            break
        elif victory < 0:
            break

        player1.progress += 1
#        if player1.progress > 2:
#            player1.progress = 1
        for character in player1.characters:
            character.restore()

#    if not shown:
#        Scenes.Scene(number)

