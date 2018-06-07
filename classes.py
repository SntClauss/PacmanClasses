from enum import Enum

class GhostColor(Enum):
    pink = 0
    blue = 1
    orange = 2 
    red = 3
class Direction(Enum):
    top = 0
    bottom = 1
    left = 2 
    right = 3
class Status(Enum):
    alive = 0
    dead = 1
    frightened = 2 
    powered = 3
class Character:
    direction = Direction.top
    speed = 0
    status = Status.alive
    x = 0
    y = 0
    def die():
        return
    def spawn(x,y):
        return
    def move(direction):
        return
    def teleport(x,y):
        return
class Ghost(Character):
    color = GhostColor.red
    status = Status.alive
    scatterTimer = 0
    frightenedTimer = 0
    def updateScore():
        return
    def leaveCage():
        return
    def getBackToCage():
        return
    def setFrightened(seconds):
        return
    def scatter(seconds):
        return
    def decideDirection(pacX,pacY):
        return
class Pacman(Character):
    killStreak = 0
    lastControl = Direction.top
    def control(direction):
        return
    def collide():
        return
class Maze():
    score = 0
    lives = 3
    tiles = None
    def pillsLeft():
        return
    def addToScore():
        return
    def killGhost():
        return
    def reset():
        return
    def win():
        return
    
class Collectable():
  score = 0
  displayScore = False
  x = 0
  y = 0
  def consume():
        return
  def sideEffect():
        return
  def displayScore():
        return
    
class Fruit(Collectable):
    def __init__(self, Collectable):
        self = Collectable

class Pill(Collectable):
    def __init__(self, Collectable):
        self = Collectable
    
class PowerPill(Pill):
    def __init__(self, Pill):
        self = Pill
        
    def activateSideEffect():
        return
class Tile(Character, Collectable):
    type = enum
    x = 0
    y = 0
    char = Character
    item = Collectable
    
    def getAllTileDirection():
        return
    def getFromPosition(x,y):
        return
