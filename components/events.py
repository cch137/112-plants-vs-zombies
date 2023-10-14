import pygame

CLICK = 'click'
HOVER = 'hover'
MOUSEENTER = 'mouseenter'
MOUSELEAVE = 'mouseleave'

class UserEvent():
    def __init__(self, name: str):
        self.name = name

class MouseEvent(UserEvent):
    def __init__(self, name: str, pos: tuple[int, int]):
        UserEvent.__init__(self, name)
        self.pos = pos

class HoverEvent(MouseEvent):
    def __init__(self, pos: tuple[int, int]):
        MouseEvent.__init__(self, HOVER, pos)

class MouseEnterEvent(MouseEvent):
    def __init__(self, pos: tuple[int, int]):
        MouseEvent.__init__(self, MOUSEENTER, pos)

class MouseLeaveEvent(MouseEvent):
    def __init__(self, pos: tuple[int, int]):
        MouseEvent.__init__(self, MOUSELEAVE, pos)

class ClickEvent(UserEvent):
    def __init__(self, pos: tuple[int, int]):
        MouseEvent.__init__(self, CLICK, pos)
