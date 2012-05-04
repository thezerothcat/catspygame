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

class TextBoxException:
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class TextBox:
    def __init__(self, screen, font_size = 20, characters = 10, restrictions = ''):
        self.allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}|":?><`1234567890-=\][;/.,\''
        self.allowed = filter(lambda letter: letter not in restrictions, self.allowed)
        self.max_characters = characters
        self.font = pygame.font.Font(None, font_size)

        # characters, calc max width
        width = 0
        the_list = self.font.metrics(self.allowed)
        for i in range(0, len(self.allowed)):
            if the_list[i][-1] > width:
                width = the_list[i][-1]
        height = self.font.get_height()

        self.rect = pygame.Rect((screen.get_clip().width - (width * self.max_characters + height * 2)) / 2, (screen.get_clip().height - height) / 2, width * self.max_characters + height * 2, height * 2)
        self.text_rect = pygame.Rect(height / 2, height / 2, width * self.max_characters, height)
        self.cursor_rect = pygame.Rect((self.text_rect.topleft), (width / 2, height))

        self.box = screen.subsurface(self.rect)
        self.rect = self.box.get_clip()
        self.image = get(self.rect)

        self.cursor = pygame.Surface((self.cursor_rect.width, self.cursor_rect.height))
        self.cursor.fill((255, 255, 255))

        self.text = ''
        self.blink_timer = 0

    def update(self, key):
        self.blink_timer = 0
        if len(self.text) < 10:
            self.text += key
        self.draw()

    def draw(self):
        self.box.blit(self.image, self.rect)
        text = self.font.render(self.text, True, (255, 255, 255), (0, 0, 255))
        t_part = text.get_clip()
        if self.text != '':
            if len(self.text) <= 10:
                self.cursor_rect.x = t_part.width + self.text_rect.x
        else:
            self.cursor_rect.x = self.text_rect.x
        self.box.blit(text, self.text_rect)

    def backspace(self):
        self.blink_timer = 0
        self.text = self.text[0:-1]
        self.draw()

    def run(self):
        self.draw()
        while True:
            self.blink()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return self.text
                    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        self.backspace()
                    elif event.key == pygame.K_ESCAPE:
                        raise TextBoxException("Quit the textbox without selecting text")
                    else:
                        try:
                            letter = event.unicode.encode('ascii')
                        except UnicodeEncodeError:
                            pass
                        else:
                            if letter in self.allowed:
                                self.update(letter)
            pygame.display.flip()

    def blink(self):
        self.blink_timer += 1
        if self.blink_timer >= 1000:
            self.blink_timer -= 1000

        if self.blink_timer <= 500:
            self.cursor.set_alpha(255 * self.blink_timer / 500)
        elif self.blink_timer > 500:
            self.cursor.set_alpha(255 - (255 * (self.blink_timer - 500) / 500))
            
        self.draw()
        self.box.blit(self.cursor, self.cursor_rect)

