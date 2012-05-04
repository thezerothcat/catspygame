import pygame

def get(drawrect):
    bg = pygame.Surface((drawrect.width, drawrect.height))
    pygame.draw.line(bg, (255, 255, 255), (1, 0), (drawrect.width - 2, 0) )
    pygame.draw.line(bg, (255, 255, 255), (1, drawrect.height - 1), (drawrect.width - 2, drawrect.height - 1) )
    pygame.draw.line(bg, (255, 255, 255), (0, 1), (0, drawrect.height - 2) )
    pygame.draw.line(bg, (255, 255, 255), (drawrect.width - 1, 1), (drawrect.width - 1, drawrect.height - 2) )
    for y in range(1, drawrect.height - 1):
        pygame.draw.line(bg, (0, 0, 255), (1, y), (drawrect.width - 2, y) )

    return bg

