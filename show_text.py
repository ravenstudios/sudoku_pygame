
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()



def message_display(surface, text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)
