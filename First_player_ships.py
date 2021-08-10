from block import Block
from score import Score

class FirstPlayer():

    def __init__(self, game_field):

        self.game_field = game_field

        self.score = Score(width/2-250, height/2-300, 'Survived ships', 0)

        self.ships_second_player = []

        start_for_del_new_busy_blocks = 0

        self.ships = []
        for _ in range(0, 3):
            self.ships.append([]) # elem 0 - small ships, elem 1 - meduim ships, elem 2 - big ships

        for i in range(0, len(self.ships)):
            for j in range(0, 6-i):
                rand_block = int(random(0, len(self.game_field.game_field_first_player)))
                for k in range(0, 1*(i+1)):
                    x = self.game_field.game_field_first_player[rand_block+k].x
                    y = self.game_field.game_field_first_player[rand_block].y
                    self.game_field.busy_blocks[0].append(self.game_field.game_field_first_player[rand_block+k])
                    self.ships[i].append(Block(x, y, self.game_field.game_field_first_player[0].w, self.game_field.game_field_first_player[0].h))

            for j in range(start_for_del_new_busy_blocks, len(self.game_field.busy_blocks[0])):
                self.game_field.game_field_first_player.remove(self.game_field.busy_blocks[0][j])
            start_for_del_new_busy_blocks = len(self.game_field.busy_blocks[0])

        self.score.load_player(self)

    def run(self):
        self.show()
        self.score.run()

    def load_ships_second_player(self, item):
        self.ships_second_player = item

    def show(self):
        for s in self.ships:
            for ship in s:
                ship.run()

    def touch_to_ships(self):
        for block in self.game_field.busy_blocks[1]:
            if (mouseX > block.x - block.w/2 and mouseX < block.x + block.w/2 and
                mouseY > block.y - block.h/2 and mouseY < block.y + block.h/2):
                block.state = 'Kill'

        for ships in self.ships_second_player:
            for block in ships[:]:
                if (mouseX > block.x - block.w/2 and mouseX < block.x + block.w/2 and
                    mouseY > block.y - block.h/2 and mouseY < block.y + block.h/2):
                    ships.remove(block)
                    return True
                
