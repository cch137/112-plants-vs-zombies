import pygame
from typing import *
from utils.constants import *
import components.scenes as scenes

the_end = scenes.Scene()

def init():
    from components import Element, TextBox, media, \
        events, Entity, plants, zombies, controller, levels
    
    if controller.victory:
        bg = Element(media.load_image('scenes/victory.png', (WINDOW_WIDTH, WINDOW_HEIGHT)))
        the_end.add_element(bg)
    else:
        bg = Element(media.load_image('scenes/game_over.png', (WINDOW_WIDTH, WINDOW_HEIGHT)))
        the_end.add_element(bg)


    ele = Element((315, 65))
    ele.background_color = (0,0,0,0)
    ele.cursor = 'hand'
    ele.rect.center = (528, 490)
    the_end.add_element(ele)
    ele.add_event_listener(events.CLICK, lambda: controller.goto_scene(controller.scenes.testing1))
the_end.init = init


 