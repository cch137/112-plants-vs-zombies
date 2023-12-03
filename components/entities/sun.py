from components.media import media
from components.entities import Entity
from random import randint
from typing import Tuple, Any

class Sun(Entity):
    def __init__(self, x_range: Tuple[int, int], y_range: Tuple[int, int], move_limit: int | None = None, value=25):
        self.value = value
        Entity.__init__(self, media.load_image('entities/sun.png', 75))
        self.rect.center = (randint(*x_range), -self.rect.height / 2)
        if move_limit is None:
            self.move_limit = int(self.rect.height / 2 + randint(*y_range))
        else:
            self.move_limit = move_limit
        self.velocity_y = 3
        self.velocity_a = 1 * (1 if randint(0, 1) else -1)
        self.z_index = 999
        self.radius_scale = 0.6
        self.cursor_r = 'hand'
    
    def update(self):
        if self.move_limit <= 0:
            self.velocity_a = 0
    
    def kill(self, *args: Any, **kwargs: Any):
        '''Returns sun value.'''
        Entity.kill(self, *args, **kwargs)
        return self.value
