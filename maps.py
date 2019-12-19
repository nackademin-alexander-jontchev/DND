from random import randint
from copy import deepcopy


class Maps:

    def __init__(self):
        self.small_map = []
        self.medium_map = []
        self.large_map = []
        self.current_map = []
        self.current_position = ()
        self.monster_map = []
        self.treasure_map = []
        self.previous_position = []

    def create_small_map(self):
        self.small_map = [['X'] * 4 for i in range(4)]
        self.current_map = self.small_map

    def create_medium_map(self):
        self.medium_map = [['X'] * 5 for i in range(5)]
        self.current_map = self.medium_map

    def create_large_map(self):
        self.large_map = [['X'] * 8 for i in range(8)]
        self.current_map = self.large_map

    def show_small_map(self):
        print('size 4x4:')
        for small in self.small_map:
            print(small)

    def show_medium_map(self):
        print('size 5x5:')
        for medium in self.medium_map:
            print(medium)

    def randomize_monster(self):
        # makes a copy of the map with monsters in it
        monster_board = deepcopy(self.current_map.copy())

        for row in monster_board:
            for room in row:
                monster_list = []
                rnd1 = randint(1, 100) / 100
                if rnd1 <= 0.2:
                    monster_list.append('Big spider')
                rnd2 = randint(1, 100) / 100
                if rnd2 <= 0.15:
                    monster_list.append('Skeleton')
                rnd3 = randint(1, 100) / 100
                if rnd3 <= 0.1:
                    monster_list.append('Orc')
                rnd4 = randint(1, 100) / 100
                if rnd4 <= 0.05:
                    monster_list.append('Troll')

                row[row.index(room)] = monster_list

        self.monster_map = deepcopy(monster_board)

    def randomize_treasure(self):
        # makes a copy if the map woth treasures
        treasure_board = deepcopy(self.current_map.copy())

        for row in treasure_board:
            for room in row:
                treassure_list = []

                rnd1 = randint(1, 100) / 100
                if rnd1 <= 0.40:
                    treassure_list.append('Loose coins')
                rnd2 = randint(1, 100) / 100
                if rnd2 <= 0.20:
                    treassure_list.append('Money pouch')
                rnd3 = randint(1, 100) / 100
                if rnd3 <= 0.15:
                    treassure_list.append('Gold jewelry')
                rnd4 = randint(1, 100) / 100
                if rnd4 <= 0.10:
                    treassure_list.append('Gemstone')
                rnd5 = randint(1, 100) / 100
                if rnd5 <= 0.05:
                    treassure_list.append('Small chest')

                row[row.index(room)] = treassure_list
        self.treasure_map = deepcopy(treasure_board.copy())

    def show_map(self):
        if len(self.current_map) == 8:
            print('size 8x8:')
        elif len(self.current_map) == 5:
            print('size 5x5:')
        elif len(self.current_map) == 4:
            print('size 4x4:')
        for grid in self.current_map:
            print(grid)

    def place_player(self, corner):
        if corner == 'ul':
            self.current_map[0][0] = '@'
            self.current_position = (0, 0)
        if corner == 'ur':
            self.current_map[0][len(self.current_map) - 1] = '@'
            self.current_position = (0, len(self.current_map) - 1)
        if corner == 'lr':
            self.current_map[len(self.current_map) - 1][len(self.current_map) - 1] = '@'
            self.current_position = (len(self.current_map) - 1, len(self.current_map) - 1)
        if corner == 'll':
            self.current_map[len(self.current_map) - 1][0] = '@'
            self.current_position = (len(self.current_map) - 1, 0)

    def move_up(self):
        if self.current_position[0] - 1 < 0:
            print("Cant go that way")
            return self.current_position

        else:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0] - 1][self.current_position[1]] = '@'
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
            return self.current_position

    def move_down(self):
        try:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0] + 1][self.current_position[1]] = '@'
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
            return self.current_position
        except:
            print('Cant go that way')
            self.current_map[self.current_position[0]][self.current_position[1]] = '@'
            return self.current_position

    def move_left(self):
        if self.current_position[1] - 1 < 0:
            print("Cant go that way")
            return self.current_position

        else:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0]][self.current_position[1] - 1] = '@'
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
            return self.current_position

    def move_right(self):

        try:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0]][self.current_position[1] + 1] = '@'
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
            return self.current_position
        except:
            print('Cant go that way')
            self.current_map[self.current_position[0]][self.current_position[1]] = '@'
            return self.current_position

    def escape_room(self, previous_pos):
        self.current_map[self.current_position[0]][self.current_position[1]] = 'X'
        self.current_position = previous_pos
        self.current_map[self.current_position[0]][self.current_position[1]] = '@'
        return self.current_position
