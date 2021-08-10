class BlockGried():

    def __init__(self, x, y, w, h, state):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.state = state

    def run(self):
        self.show()

    def show(self):
        if self.state == 'Kill':
            fill(0,255,0)
        elif self.state == 'Empty':
            fill(255,0,0)
        else:
            noFill()

        rect(self.x, self.y, self.w, self.h)
