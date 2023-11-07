from typing import *
from typing import Any
from constants import *
from components.entities import Entity, Element

class Level(Element):
    ticks: int

class Spawner():
    def __init__(self, schedule_tick: int, *entities: Entity):
        self.schedule = schedule_tick
        self.entities = entities
    
    def spawnable(self, ticks: int):
        return not self.spawned and self.schedule <= ticks

class BoundSpawner():
    def __init__(self, level: Level, spawner: Spawner):
        '''Please use `Spawner`, DO NOT use this class directly.'''
        self.level = level
        self.spawner = spawner
        self.__used = False
    
    @property
    def is_spawnable(self):
        return not self.__used and self.spawner.schedule <= self.level.ticks
    
    @property
    def used(self):
        return self.__used
    
    def spawn(self):
        if self.__used:
            raise 'Spawner has been used'
        self.level.scene.add_element(*self.spawner.entities)
        self.__used = True

class Level(Element):
    def __init__(self, spawners: Iterable[Spawner]):
        Element.__init__(self, (0, 0))
        self.__spawners = set(BoundSpawner(self, s) for s in spawners)
        self.ticks = 0
    
    def add_spawner(self, spawner: Spawner):
        self.remove_spawner(spawner)
        self.__spawners.add(BoundSpawner(self, spawner))
    
    def remove_spawner(self, spawner: Spawner):
        for bound in tuple(self.__spawners):
            if bound.spawner is spawner:
                self.__spawners.remove(bound)
    
    def update(self, *args: Any, **kwargs: Any) -> None:
        Element.update(self, *args, **kwargs)
        for spawner in self.__spawners:
            if spawner.is_spawnable:
                spawner.spawn()
        self.ticks += 1