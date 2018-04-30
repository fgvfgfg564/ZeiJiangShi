class MouseClickItem:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class MouseMove:
    def __init__(self, x, y):
        self.pos = (x, y)


class KeyDown:
    def __init__(self, key):
        self.key = key