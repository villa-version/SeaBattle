from game_field import GameField
from First_player_ships import FirstPlayer
from Second_player_ships import SecondPlayer

class Main():

    def __init__(self):
        self.game_field = GameField()
        self.first_player = FirstPlayer(self.game_field)
        self.second_player = SecondPlayer(self.game_field)
        self.first_player.load_ships_second_player(self.second_player.ships)
        self.second_player.load_ships_first_player(self.first_player.ships)

        self.progress = 'FirstPLayer'

    def run(self):
        self.game_field.run()
        self.first_player.run()
        self.second_player.run()

    def touch_to(self):
        if self.progress == 'FirstPLayer':
            if self.game_field.first_player_touch_to_block_gried() or self.first_player.touch_to_ships():
                self.progress = 'SecondPLayer'
            
        if self.progress == 'SecondPLayer':
            if self.second_player.touch_to_ships() or self.game_field.second_player_touch_to_block_gried():
                self.progress = 'FirstPLayer'
