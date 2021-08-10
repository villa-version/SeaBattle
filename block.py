from object import Object

class Block(Object):

    def __init__(self, x, y, w, h):
        Object.__init__(self, x, y, w, h)

    def run(self):
        Object.show(self)
