from constants import *
import pygame
import random

class Square:
    def __init__(self, col, row):
        self.row = row
        self.col = col
        # if random.randint(0,1) == 0:
        #     self.value = random.randint(1, 9)
        # else:
        #     self.value = ""
        self.value = ""

        self.size = BLOCK_SIZE
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.topleft = col * BLOCK_SIZE, row * BLOCK_SIZE
        self.border_offset = 3
        self.can_edit = False
        self.background_color = WHITE
        self.selected_background_color = (200, 200, 200)
        self.color = WHITE




    def change_number(self, number):
        self.value = number
        self.can_edit = False
        self.color = self.background_color

    def get_value(self):
        return self.value

    def clicked(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.can_edit:
                self.color = self.background_color
                self.can_edit = False
            else:
                self.color = self.selected_background_color
                self.can_edit = True
        else:
            if self.can_edit:
                self.can_edit = False
                self.color = self.background_color


    def update(self):
        if self.can_edit:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                self.change_number(1)
            if keys[pygame.K_2]:
                self.change_number(2)
            if keys[pygame.K_3]:
                self.change_number(3)
            if keys[pygame.K_4]:
                self.change_number(4)
            if keys[pygame.K_5]:
                self.change_number(5)
            if keys[pygame.K_6]:
                self.change_number(6)
            if keys[pygame.K_7]:
                self.change_number(7)
            if keys[pygame.K_8]:
                self.change_number(8)
            if keys[pygame.K_9]:
                self.change_number(9)
            if keys[pygame.K_0]:
                self.change_number("")

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        x = self.rect.left + self.border_offset
        y = self.rect.top + self.border_offset
        w = self.rect.width - self.border_offset
        h = self.rect.height - self.border_offset
        pygame.draw.rect(surface, self.color, (x, y, w, h))
        self.message_display(surface, str(self.value), self.rect.center)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()



    def message_display(self, surface, text, loc):
        largeText = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (loc)
        surface.blit(TextSurf, TextRect)
