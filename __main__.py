import os
import random

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.stone import Stone
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Green"
WHITE = Color(255, 255, 255)
GREEN = Color(0,255,0)
RED = Color(255,0,0)
GEM_NUMBERS = 35
STONE_NUMBERS = 30


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    score = Actor()
    score.set_text("")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("scores", score)
    
    # create the robot
    x = int(MAX_X / 2)
    y = 585
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    

    # create Gems
    for n in range(GEM_NUMBERS):
        x = random.randint(1,COLS -1)
        y = random.randint(1,ROWS -1)
        position = Point(x,y)
        position = position.scale(CELL_SIZE)
        
        gem = Gem()
        gem.set_text("*")
        gem.set_font_size(FONT_SIZE)
        gem.set_color(GREEN)
        gem.set_position(position)
        cast.add_actor("gems",gem)
    # create Stones
    for n in range(STONE_NUMBERS):
        x = random.randint(1,COLS)
        y = random.randint(1,ROWS)
        position = Point(x,y)
        position = position.scale(CELL_SIZE)
        
        stone = Stone()
        stone.set_text("O")
        stone.set_font_size(FONT_SIZE)
        stone.set_color(RED)
        stone.set_position(position)
        cast.add_actor("stones",stone)   
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()