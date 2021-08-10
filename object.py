class Object():

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def show(self):
        if key == 'c':
            fill(0,0,0)
        else:
            noFill()

        rect(self.x, self.y, self.w, self.h)
