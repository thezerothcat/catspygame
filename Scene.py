import pygame

class Scene:
    def __init__(self, screen, number = 0):
        #show the scene
        if number == 0:
            screen.blit(pygame.image.load('images/intro.png').convert_alpha(), (0, 0))
            pygame.display.flip()
            self.wait()

    def wait(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return 0
