# main.py  -- Person 4 (integration)
import pygame
import config
from room import Room
from furniture import Sidebar
from ui import Toolbar

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_W, config.SCREEN_H))
    pygame.display.set_caption("RoomCraft - Simple Room Designer")
    clock = pygame.time.Clock()

    room = Room()
    sidebar = Sidebar()
    toolbar = Toolbar()
    furniture_list = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # TODO: handle mouse events (select / drag / click buttons)

        screen.fill(config.BG)
        room.draw(screen)
        sidebar.draw(screen)
        toolbar.draw(screen)
        for f in furniture_list:
            f.draw(screen)

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
