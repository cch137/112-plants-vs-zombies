import pygame
from typing import *
from constants import *
import components.scenes as scenes

main_game = scenes.Scene()

def init():
    from components import Element, load_image, create_textbox, \
        events, Entity, Plant, Zombie, controller
    pass

main_game.init = init