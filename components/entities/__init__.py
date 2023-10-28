from typing import *
import pygame
import utils.process as process
from components import Element

class Entity: pass

class Ability():
    def __init__(
            self,
            entities: Entity,
            name: str = '_',
            attack: int = 0,
            colddown: int = 60,
        ):
        self.entities = entities
        self.name = name
        self.attack = attack
        self.colddown = colddown
        '''unit: second'''
        self.last_used_at: float = 0.0

    @property
    def is_cooling_down(self):
        return self.last_used_at + self.colddown > process.timestamp
    
    def use(self):
        if self.is_cooling_down: # 技能正在冷卻中，無法使用
            return
        if self.effect():
            self.last_used_at = process.timestamp

    def effect(self) -> bool:
        '''重寫此函式以賦予 Ability 效果。
        注意：此函式須返回一個布林值！布林值表示為此能力是否使用成功。'''
        return True

class Entity(Element):
    health: int = 100
    defense: int = 0
    '''number between 0 and 100'''
    vision_range: int = 3
    '''視野。單位：格(地圖 tile)'''
    velocity_x: int = 0
    velocity_y: int = 0
    acceleration_x: int = 0
    acceleration_y: int = 0

    def __init__(self, image: pygame.Surface):
        Element.__init__(self, image)
        self.abilities: set[Ability] = set()
    
    def damage(self, value: int):
        self.health -= value * (100 - self.defense)
    
    def auto_update(self, *args: Any, **kargs: Any):
        Element.update(self, *args, **kargs)
        for ability in self.abilities:
            ability.use()
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        self.x += self.velocity_x
        self.y += self.velocity_y

import components.entities.plants as plants
import components.entities.zombies as zombies
