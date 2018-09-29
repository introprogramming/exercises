from example.ct_pygame import *

##
## Global variables
##

TILES = None
TILE_MAP = None
OFF = 100
GAP = 0
WID = 20
HEI = 14
SIZE = 32
TIME = None
HORIZONTAL = 0
VERTICAL = 1
ORIENTATION = HORIZONTAL
SMALL_BOAT = 0
LARGE_BOAT = 1
SELECTED_BOAT_TYPE = 0
PLACED_BOATS = None
ID_GENERATOR = 0
SELECTED_TILES = None
GAME_MODE_PLACE_PLAYER_0 = 0
GAME_MODE_PLACE_PLAYER_1 = 1
GAME_MODE_PLAY_PLAYER_0 = 2
GAME_MODE_PLAY_PLAYER_1 = 3
GAME_MODE = GAME_MODE_PLACE_PLAYER_0

PLAYER_BOATS = [LARGE_BOAT, LARGE_BOAT, SMALL_BOAT, SMALL_BOAT, SMALL_BOAT]
BOATS_TO_PLACE = []
CROSSES_PLACED = []
PLAYER_0_HITS = 0
PLAYER_1_HITS = 0
PLAYER_HITS_NEEDED_TO_WIN = 1 * 3 + 3 * 2


##
## Classes
##

class Cross:
    def __init__(self, position, side, did_hit):
        global ID_GENERATOR
        self.position = position
        self.side = side
        self.tag = "marker_" + str(ID_GENERATOR)
        if did_hit:
            self.image = "x.png"
        else:
            self.image = "miss.png"
        self.did_hit = did_hit
        ID_GENERATOR += 1


class Boat:
    def __init__(self, x, y, w, h, side):
        global ID_GENERATOR
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.side = side
        self.tag = "boat_" + str(ID_GENERATOR)
        ID_GENERATOR += 1


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tag = "tile(" + str(x) + "," + str(y) + ")"
        self.occupant = None


##
##
##

def coordToPosition(x, y):
    global OFF
    global GAP
    global SIZE
    return (OFF + x * (SIZE + GAP), OFF + y * (SIZE + GAP))


def positionToCoord(x, y):
    global WID
    global HEI
    global OFF
    global GAP
    global SIZE
    return (int(round((x - OFF) / (SIZE + GAP))),
            int(round((y - OFF) / (SIZE + GAP))))


def getBoatImage(boat_type):
    global ORIENTATION
    global HORIZONTAL
    global VERTICAL
    global SELECTED_BOAT_TYPE
    global SMALL_BOAT
    global LARGE_BOAT
    if SELECTED_BOAT_TYPE == SMALL_BOAT:
        return "small_boat.png"
    else:
        if ORIENTATION == HORIZONTAL:
            return "large_boat_horizontal.png"
        else:
            return "large_boat_vertical.png"


def getBoatTileBounds(boat_type):
    # Return format ( dx, dy, w, h )
    global ORIENTATION
    global HORIZONTAL
    global VERTICAL
    global SELECTED_BOAT_TYPE
    global SMALL_BOAT
    global LARGE_BOAT
    if SELECTED_BOAT_TYPE == SMALL_BOAT:
        return (0, 0, 1, 1)
    else:
        if ORIENTATION == HORIZONTAL:
            return (-1, 0, 3, 1)
        else:
            return (0, -1, 1, 3)


def updateCursor():
    global GAME_MODE
    global GAME_MODE_PLAY_PLAYER_0
    global BOATS_TO_PLACE
    global SELECTED_BOAT_TYPE
    if ctHasObject("cursor"):
        ctDestroyObject("cursor")
    if GAME_MODE < GAME_MODE_PLAY_PLAYER_0:
        bounds = getBoatTileBounds(SELECTED_BOAT_TYPE)
        mp = ctGetMousePosition()
        sz = (SIZE * bounds[2], SIZE * bounds[3])
        pos = (mp[0] - sz[0] / 2.0, mp[1] - sz[1] / 2.0)
        ctCreateObject("cursor", getBoatImage(SELECTED_BOAT_TYPE),
                       position=pos, size=sz)
        updateHeldBoat()


def displayCurrentEnemies():
    global GAME_MODE
    global PLACED_BOATS
    global CROSSES_PLACED
    side = GAME_MODE % 2
    game_over = isGameOver()
    for boat in PLACED_BOATS:
        ctSetObjectVisible(boat.tag, boat.side == side or game_over)
    for cross in CROSSES_PLACED:
        ctSetObjectVisible(cross.tag, cross.side == side or cross.did_hit or game_over)


def getEnemyXLimits():
    global WID
    other_side = (GAME_MODE + 1) % 2
    half = WID / 2
    min_x = other_side * half
    max_x = min_x + half
    return (min_x, max_x)


def crossFreeTile(x, y):
    global CROSSES_PLACED
    p = (x, y)
    for cross in CROSSES_PLACED:
        if cross.position == p:
            return False
    return True


def loadField():
    # Start a new game.
    global TIME
    global PLACED_BOATS
    global SELECTED_TILES
    global BOATS_TO_PLACE
    global PLAYER_BOATS
    global GAME_MODE
    global GAME_MODE_PLACE_PLAYER_0
    global SELECTED_BOAT_TYPE
    global PLAYER_0_HITS
    global PLAYER_1_HITS
    TIME = 0.0
    if PLACED_BOATS:
        for boat in PLACED_BOATS:
            ctDestroyObject(boat.tag)
    PLACED_BOATS = []
    SELECTED_TILES = []
    BOATS_TO_PLACE = PLAYER_BOATS[::]
    SELECTED_BOAT_TYPE = BOATS_TO_PLACE.pop()
    GAME_MODE = GAME_MODE_PLACE_PLAYER_0
    PLAYER_0_HITS = 0
    PLAYER_1_HITS = 0


def selectTile(x, y):
    global TILES
    global SIZE
    global SELECTED_TILES
    tile = TILES[y][x]
    SELECTED_TILES.append(tile)
    ctSetObjectImage(tile.tag, "water_selected.png", size=(SIZE, SIZE))


def deselectTile(x, y):
    global TILES
    global SIZE
    global SELECTED_TILES
    tile = TILES[y][x]
    if tile in SELECTED_TILES:
        SELECTED_TILES.remove(tile)
        ctSetObjectImage(tile.tag, "water.png", size=(SIZE, SIZE))


def deselectTiles():
    global SELECTED_TILES
    if SELECTED_TILES:
        for tile in SELECTED_TILES:
            if ctHasObject(tile.tag) and not ctGetObjectHovered(tile.tag):
                deselectTile(tile.x, tile.y)


def boatFits(x, y, w=1, h=1, side=0):
    # Test if the boat fits at the selected tile.
    global PLACED_BOATS
    global WID
    global HEI
    min_x = (WID / 2) * side
    max_x = min_x + WID / 2
    if x < min_x or x + w > max_x or y < 0 or y + h > HEI:
        return False
    else:
        for boat in PLACED_BOATS:
            if (x + w - 1 >= boat.x and x <= boat.x + boat.w - 1
                    and y + h - 1 >= boat.y and y <= boat.y + boat.h - 1):
                return False
        return True


def updateHeldBoat():
    global SELECTED_BOAT_TYPE
    global TILES
    global GAME_MODE
    mouse_position = ctGetMousePosition()
    if ctHasObject("cursor"):
        ctPlaceCenterObject("cursor", mouse_position);
        bounds = getBoatTileBounds(SELECTED_BOAT_TYPE)
        mouse_tile = positionToCoord(mouse_position[0], mouse_position[1])
        x = mouse_tile[0] + bounds[0]
        y = mouse_tile[1] + bounds[1]
        w = bounds[2]
        h = bounds[3]
        deselectTiles()
        if boatFits(x, y, w, h, side=(GAME_MODE % 2)):
            for ty in xrange(y, y + h):
                for tx in xrange(x, x + w):
                    selectTile(tx, ty)


def isGameOver():
    global PLAYER_0_HITS
    global PLAYER_1_HITS
    global PLAYER_HITS_NEEDED_TO_WIN
    return (PLAYER_0_HITS >= PLAYER_HITS_NEEDED_TO_WIN
            or PLAYER_1_HITS >= PLAYER_HITS_NEEDED_TO_WIN)


##
## Implementation of the "mall.py" template file.
##

def start():
    global TILES
    global TILE_MAP
    global WID
    global HEI
    global SIZE
    TILES = []
    TILE_MAP = {}
    for y in xrange(0, HEI):
        xs = []
        TILES.append(xs)
        for x in xrange(0, WID):
            tile = Tile(x, y)
            xs.append(tile)
            TILE_MAP[tile.tag] = tile
            ctCreateObject(tile.tag, "water.png", position=coordToPosition(x, y), size=(SIZE, SIZE))
    ctCreateObject("line", "line.png", position=coordToPosition(WID / 2.0 - 0.05, 0), size=(4, SIZE * (HEI + GAP)))
    updateCursor()
    updateInstructions()
    # Start a new game.
    loadField()


def update():
    global TILES
    global TIME
    global PLACED_BOATS
    r = (math.cos(TIME) * (180.0 / math.pi)) * 0.1
    TIME += 0.05
    for xs in TILES:
        for tile in xs:
            ctAngleObject(tile.tag, r)
    for boat in PLACED_BOATS:
        if ctHasObject(boat.tag):
            ctAngleObject(boat.tag, r)
    pass


def keyPressed(key):
    global ORIENTATION
    global HORIZONTAL
    global VERTICAL
    if key == pygame.K_SPACE:
        if ORIENTATION == HORIZONTAL:
            ORIENTATION = VERTICAL
        else:
            ORIENTATION = HORIZONTAL
        updateCursor()


def mouseMoved(buttons):
    updateHeldBoat()
    pass


def updateInstructions():
    global GAME_MODE
    global GAME_MODE
    global PLACED_BOATS
    global CROSSES_PLACED
    if PLACED_BOATS:
        for boat in PLACED_BOATS:
            ctSetObjectVisible(boat.tag, False)
    if CROSSES_PLACED:
        for cross in CROSSES_PLACED:
            ctSetObjectVisible(cross.tag, False)
    if GAME_MODE == 0:
        ctCreateText("player_text", "PLAYER 1 PLACE YOUR BOATS TO THE LEFT SIDE (Space to turn)")
    elif GAME_MODE == 1:
        ctSetObjectText("player_text", "PLAYER 2 PLACE YOUR BOATS TO THE RIGHT SIDE (Space to turn)")
    elif (GAME_MODE % 2) == 0:
        ctSetObjectText("player_text", "PLAYER 1 ATTACK ON THE RIGHT SIDE")
    elif (GAME_MODE % 2) == 1:
        ctSetObjectText("player_text", "PLAYER 2 ATTACK ON THE LEFT SIDE")


def raycast(name, tag, abs_pos, rel_pos):
    global TILE_MAP
    global SIZE
    global PLACED_BOATS
    global ORIENTATION
    global HORIZONTAL
    global VERTICAL
    global SELECTED_BOAT_TYPE
    global BOATS_TO_PLACE
    global PLAYER_BOATS
    global GAME_MODE
    global GAME_MODE_PLAY_PLAYER_0
    global SELECTED_BOAT_TYPE
    global CROSSES_PLACED
    global PLAYER_0_HITS
    global PLAYER_1_HITS
    global PLAYER_HITS_NEEDED_TO_WIN
    if GAME_MODE < GAME_MODE_PLAY_PLAYER_0:
        if "tile" in tag:
            tile = TILE_MAP[tag]
            bounds = getBoatTileBounds(SELECTED_BOAT_TYPE)
            x = tile.x + bounds[0]
            y = tile.y + bounds[1]
            w = + bounds[2]
            h = + bounds[3]
            img = getBoatImage(SELECTED_BOAT_TYPE)
            if boatFits(x, y, w, h, side=(GAME_MODE % 2)):
                boat = Boat(x, y, w, h, GAME_MODE)
                PLACED_BOATS.append(boat)
                # Create a new ship at mouse position.
                ctCreateObject(boat.tag, img, position=coordToPosition(x, y), size=(SIZE * w, SIZE * h))
                if (len(BOATS_TO_PLACE) == 0):
                    # When the current player has placed all of his/her boats
                    # we move on to the next player.
                    GAME_MODE += 1
                    if GAME_MODE < GAME_MODE_PLAY_PLAYER_0:
                        # The second player gets to place their boats.
                        BOATS_TO_PLACE = PLAYER_BOATS[::]
                        SELECTED_BOAT_TYPE = BOATS_TO_PLACE.pop()
                        updateInstructions()
                    else:
                        # All players have placed their boats,
                        # move on to the battle stage.
                        updateInstructions()
                        displayCurrentEnemies()
                    deselectTiles()
                else:
                    SELECTED_BOAT_TYPE = BOATS_TO_PLACE.pop()
                updateCursor()
    elif not isGameOver():
        if "tile" in tag:
            side = GAME_MODE % 2
            other_side = (GAME_MODE + 1) % 2
            enemy_limits = getEnemyXLimits()
            tile_coords = positionToCoord(abs_pos[0], abs_pos[1])
            # Make sure the player aims on the enemy side.
            if tile_coords[0] >= enemy_limits[0] and tile_coords[0] < enemy_limits[1]:
                # Makde sure the player has not shoot on that spot before.
                if crossFreeTile(tile_coords[0], tile_coords[1]):
                    did_hit = not boatFits(tile_coords[0], tile_coords[1], 1, 1, side=other_side)
                    # Put a marker on the shot tile.
                    cross = Cross(tile_coords, side, did_hit)
                    ctCreateObject(cross.tag, cross.image,
                                   position=coordToPosition(cross.position[0], cross.position[1]), size=(SIZE, SIZE))
                    CROSSES_PLACED.append(cross)
                    if cross.did_hit:
                        # Give a point to the current player.
                        if side == 0:
                            PLAYER_0_HITS += 1
                            if PLAYER_0_HITS >= PLAYER_HITS_NEEDED_TO_WIN:
                                # Player 0 must have hit all enemy ships, he/she wins.
                                ctCreateText("winner_text", "PLAYER 1 WON!", position=(320, 320));
                                ctDestroyObject("player_text");
                        else:
                            PLAYER_1_HITS += 1
                            if PLAYER_1_HITS >= PLAYER_HITS_NEEDED_TO_WIN:
                                # Player 1 must have hit all enemy ships, he/she wins.
                                ctCreateText("winner_text", "PLAYER 2 WON!", position=(320, 320));
                                ctDestroyObject("player_text");
                    GAME_MODE += 1
                    # Move on to the other player's turn.
                    updateInstructions()
                    displayCurrentEnemies()


def raycastEntered(name, tag, abs_pos, rel_pos):
    global TILE_MAP
    global GAME_MODE
    global GAME_MODE_PLAY_PLAYER_0
    enemy_limits = getEnemyXLimits()
    if GAME_MODE >= GAME_MODE_PLAY_PLAYER_0 and not isGameOver():
        # Allow for highlighting a enemy tile when in battle mode.
        if "tile" in tag:
            tile = TILE_MAP[tag]
            if (GAME_MODE < GAME_MODE_PLAY_PLAYER_0
                    or tile.x >= enemy_limits[0] and tile.x < enemy_limits[1]):
                selectTile(tile.x, tile.y)
            else:
                deselectTile(tile.x, tile.y)


def raycastExited(name, tag, abs_pos, rel_pos):
    global TILE_MAP
    global GAME_MODE
    global GAME_MODE_PLAY_PLAYER_0
    if GAME_MODE >= GAME_MODE_PLAY_PLAYER_0:
        if "tile" in tag:
            tile = TILE_MAP[tag]
            deselectTile(tile.x, tile.y)


# Setup program and start.
ctSetup(2 * OFF + WID * (SIZE + GAP), 2 * OFF + HEI * (SIZE + GAP), "Battleship", background=(49, 54, 152, 255), fps=30)
ctBindFunctions(start, update, key_pressed=keyPressed, mouse_moved=mouseMoved, ray_cast=raycast,
                ray_cast_entered=raycastEntered, ray_cast_exited=raycastExited)
ctBegin()
