from block_gried import BlockGried

class GameField():

    def __init__(self):
        self.game_field_first_player = []
        self.game_field_second_player = []

        self.busy_blocks = []
        for _ in range(0, 2):
            self.busy_blocks.append([])

        w = 25
        h = 25

        w_size_first_player = int(width/2/w)
        h_size_first_player = int(height/h)
        for y in range(0, h_size_first_player):
            for x in range(0, w_size_first_player):
                self.game_field_first_player.append(BlockGried(w/2+w*x, h/2+y*h, w, h, ''))

        w_size_second_player = int(width/2/w)
        h_size_second_player = int(height/h)
        for y in range(0, h_size_second_player):
            for x in range(0, w_size_second_player):
                self.game_field_second_player.append(BlockGried(width/2+w+w*x, h/2+y*h, w, h, ''))


    def run(self):
        self.show()

    def first_player_touch_to_block_gried(self):
        for block in self.game_field_second_player:
            if (mouseX > block.x - block.w/2 and mouseX < block.x + block.w/2 and
                mouseY > block.y - block.h/2 and mouseY < block.y + block.h/2):
                block.state = 'Empty'
                return True

    def second_player_touch_to_block_gried(self):
        for block in self.game_field_first_player:
            if (mouseX > block.x - block.w/2 and mouseX < block.x + block.w/2 and
                mouseY > block.y - block.h/2 and mouseY < block.y + block.h/2):
                block.state = 'Empty'
                return True

    def show(self):
        for b in self.game_field_first_player:
            b.run()
        for b in self.game_field_second_player:
            b.run()
        for item in self.busy_blocks:
            for block in item:
                block.run()
