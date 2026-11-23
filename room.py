# room.py  -- Person 1
# Draws the room walls + grid using the DDA/Bresenham from algorithms/line.py
import config

class Room:
    def __init__(self):
        self.x, self.y = config.ROOM_X, config.ROOM_Y
        self.w, self.h = config.ROOM_W, config.ROOM_H
        self.floor_color = config.FLOOR_COLORS[0]

    def draw(self, screen):
        """Draw floor, walls, and grid."""
        pass

    def contains(self, rect):
        """Return True if a pygame.Rect is fully inside the room."""
        pass
