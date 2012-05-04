import pygame
import pickle
import Characters
import Player
from TextBox import *
import MakeRect

def main_screen(screen):
    player = Player.Player()

    #highlight = pygame.image.load('images/menu/mainhighlight.png').convert_alpha()
    #unhighlight = pygame.image.load('images/menu/mainunhighlight.png').convert_alpha()
    pawprint = pygame.image.load('images/menu/pawprint.png').convert_alpha()
    unprint = pygame.image.load('images/menu/blackbox.png').convert_alpha()

    item = 1
    index = 0
    ok = False
    while not ok:
        screen.fill((0, 0, 0))
        message = pygame.font.Font(None, 50)
        text = message.render("Cat's Game", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (57, 88))
        message = pygame.font.Font(None, 20)
        text = message.render("New Game", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (102, 218))
        text = message.render("Load Game", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (102, 248))
        text = message.render("Help (Not added)", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (102, 278))
        text = message.render("Exit", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (102, 308))
        screen.blit(pawprint, (83, 218 + 30 * (item - 1)) )
        pygame.display.update()
        done = False
     
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        screen.blit(unprint, (83, 218 + 30 * (item - 1)) )
    #                    screen.blit(unhighlight, (97, 233 + item * (height + 10)) )
                        done = True
                        item -= 1
                        if item < 1:
                            item = 4
                    elif keys[pygame.K_DOWN]:
                        screen.blit(unprint, (83, 218 + 30 * (item - 1)) )
    #                            screen.blit(unhighlight, (97, 233 + item * (height + 10)) )
                        done = True
                        item += 1
                        if item > 4:
                            item = 1
                    elif keys[pygame.K_RETURN]:
                        if item == 1:
                            try:
                                name = text_screen(screen)
                            except TextBoxException:
                                ok = False
                            else:
                                player = Player.Player(name)
                                ok = True
                            finally:
                                done = True
                        elif item == 2:
                            try:
                                save_name = text_screen(screen, description = 'Name of saved game:')
                            except TextBoxException:
                                ok = False
                            else:
                                ok = True

                                try:
                                    loadfile = open('saves/player/' + save_name + '.pkl', 'rb')
                                    player = pickle.load(loadfile)
                                    for character in player.characters:
                                        character.unpicklefix()
                                    loadfile.close()
                                except IOError:
                                    ok = False
                                finally:
                                    done = True
                        else: # if item == 4: (once help is added)
                            pygame.quit()
    return player

def text_screen(screen, description = 'Name your character:'):
    screen.fill((0, 0, 0))
    message = pygame.font.Font(None, 50)
    box = TextBox(screen, font_size = 24)

    highlight = pygame.image.load('images/menu/highlight2.png').convert_alpha()
    unhighlight = pygame.image.load('images/menu/unhighlight2.png').convert_alpha()
    text_rect = pygame.Rect(180, 150, 100, 75)
    confirm_font = pygame.font.Font(None, 14)
    confirm_box = MakeRect.get(text_rect)


    while True:
#        text = message.render("Name your", True, (255, 255, 255), (0, 0, 0))
#        screen.blit(text, (90, 50))
#        text = message.render("character:", True, (255, 255, 255), (0, 0, 0))
#        screen.blit(text, (80, 100))
        text = message.render(description, True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (10, 10))

        try:
            name = box.run()
        except TextBoxException:
            raise

        temp = screen.copy()
        screen.blit(confirm_box, text_rect)

        text = confirm_font.render("Are you sure?", True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (text_rect.x + 10, text_rect.y + 10))
        text = confirm_font.render('Yes', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (text_rect.x + 20, text_rect.y + 30))
        text = confirm_font.render('No', True, (255, 255, 255), (0, 0, 255))			
        screen.blit(text, (text_rect.x + 20, text_rect.y + 50))

        yes = True
        done = False

        while not done:
            if yes:
                screen.blit(highlight, (text_rect.x + 15, text_rect.y + 27))
                screen.blit(unhighlight, (text_rect.x + 15, text_rect.y + 47))
            else:
                screen.blit(unhighlight, (text_rect.x + 15, text_rect.y + 27))
                screen.blit(highlight, (text_rect.x + 15, text_rect.y + 47))
            pygame.display.update(text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()                    
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN] or keys[pygame.K_UP]:
                        if yes:
                            yes = False
                        else:
                            yes = True
                    elif keys[pygame.K_RETURN]:
                        if yes:
                            return name
                        else:
                            screen.blit(temp, (0, 0))
                            done = True
                            break

