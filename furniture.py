# furniture.py  -- Person 2
# Furniture pieces (Bed, Desk, Chair, Sofa, Wardrobe) + the sidebar menu.
import config

FURNITURE_TYPES = ["Bed", "Desk", "Chair", "Sofa", "Wardrobe"]

class Furniture:
    def __init__(self, kind, x, y, w, h):
        self.kind = kind
        self.x, self.y = x, y        # top-left position
        self.w, self.h = w, h
        self.angle = 0               # 0 or 90 (changed by transforms.py)

    def draw(self, screen):
        """Draw this piece (top view)."""
        pass

    def get_rect(self):
        """Return pygame.Rect (swap w/h when angle is 90)."""
        pass

class Sidebar:
    def draw(self, screen):
        """Draw the list of furniture types."""
        pass

    def get_clicked_type(self, mouse_pos):
        """Return the furniture kind clicked, or None."""
        pass
