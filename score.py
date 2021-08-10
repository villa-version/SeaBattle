class Score():

    def __init__(self, x, y, txt, count):
        self.x = x
        self.y = y
        self.txt = txt
        self.count = count
        self.player = None

    def run(self):
        self.count_ships()
        self.show()

    def count_ships(self):
        self.count = len(self.player.ships[0]) + len(self.player.ships[1]) + len(self.player.ships[2])

    def show(self):
        fill(0,0,0)
        text(self.txt + ': ' + str(self.count), self.x, self.y)

    def load_player(self, item):
        self.player = item
