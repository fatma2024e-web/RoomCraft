# config.py  -- shared constants (change only after telling the team leader)
SCREEN_W, SCREEN_H = 1000, 650
FPS = 60

SIDEBAR_W = 200          # left panel: furniture menu
TOOLBAR_H = 60           # top panel: Move / Rotate / Delete / Color

# Room (fixed size, drawn in the main area)
ROOM_X, ROOM_Y = SIDEBAR_W + 50, TOOLBAR_H + 40
ROOM_W, ROOM_H = 600, 450
GRID_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BG = (240, 240, 240)
FLOOR_COLORS = [(222, 184, 135), (176, 196, 222), (144, 238, 144)]  # 3 preset floors
