# Module pygame_tool

import pygame


class button:
    def __init__(self, x, y, width, height, screen_Id):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen_Id

    def Clicked(self, position):
        if self.x < position[0] < self.x + self.width:
            if self.y < position[1] < self.y + self.height:
                if self.screen == screen_id:
                    return True


def default_setting():
    global done
    global clock
    done = False
    clock = pygame.time.Clock()
    return done, clock


def color():
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    cyan = (0, 255, 255)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)
    return black, white, blue, green, red, cyan, yellow, magenta


def screen_setting(size_x, size_y, caption):
    global screen
    global screen_id
    screen_id = 0
    size = [size_x, size_y]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    return screen, screen_id


def button_add(pos_x, pos_y, width, height, buttonid, screen_Id):
    globals()[f'button_{buttonid}'] = button(pos_x, pos_y, width, height, screen_Id)
    return globals()[f'button_{buttonid}']


def keyboard(key):
    buttons = [pygame.key.name(k) for k, v in enumerate(pygame.key.get_pressed()) if v]
    if key in buttons:
        globals()[f'{key}_pressed'] = True
    else:
        globals()[f'{key}_pressed'] = False
    return globals()[f'{key}_pressed']


def text(msg, colour='BLACK', position=(50, 50), text_font="Calibri", text_size=50, screen_Id=0):
    font = pygame.font.SysFont(text_font, text_size)
    textSurface = font.render(msg, True, pygame.Color(colour), None)
    textRect = textSurface.get_rect()
    textRect.topleft = position

    blit(textSurface, textRect, screen_Id)


def blit(texture, pos, screen_Id):

    if type(screen_Id) == list:
        if screen_id in screen_Id:
            screen.blit(texture, pos)
    else:
        if screen_Id == screen_id:
            screen.blit(texture, pos)
