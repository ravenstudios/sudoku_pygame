from constants import *
import pygame
import board_manager

board_manager = board_manager.Board_manager()



clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  #Better to seperate to a new if statement aswell, since there's more buttons that can be clicked and makes for cleaner code.
                if event.button == 1:
                    board_manager.clicked()
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    board_manager.draw(surface)
    pygame.draw.line(surface, RED, (0, 3 * BLOCK_SIZE), (GAME_WIDTH, 3 * BLOCK_SIZE), width=3)
    pygame.draw.line(surface, RED, (0, 6 * BLOCK_SIZE), (GAME_WIDTH, 6 * BLOCK_SIZE), width=3)
    pygame.draw.line(surface, RED, (3 * BLOCK_SIZE, 0), (3 * BLOCK_SIZE, GAME_HEIGHT), width=3)
    pygame.draw.line(surface, RED, (6 * BLOCK_SIZE, 0), (6 * BLOCK_SIZE, GAME_HEIGHT), width=3)

    pygame.display.flip()



def update():
    board_manager.update()



if __name__ == "__main__":
    main()
