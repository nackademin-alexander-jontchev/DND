from treasure import Treasure
from monsters import Monsters
from random import randint


class Maps:

    def __init__(self):
        self.small_map = []
        self.medium_map = []
        self.large_map = []
        self.current_map = []
        self.current_position = ()

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
        monster_board = self.current_map.copy()

        big_spider = Monsters(7, 1, 2, 3, 0.2)
        skeleton = Monsters(4, 2, 3, 3, 0.15)
        orc = Monsters(6, 3, 4, 4, 0.1)
        troll = Monsters(2, 4, 7, 2, 0.05)

        for row in monster_board:
            for room in row:
                monster_list = []
                rnd1 = randint(1, 100) / 100
                if rnd1 <= 0.2:
                    monster_list.append(big_spider)
                rnd2 = randint(1, 100) / 100
                if rnd2 <= 0.15:
                    monster_list.append(skeleton)
                rnd3 = randint(1, 100) / 100
                if rnd3 <= 0.1:
                    monster_list.append(orc)
                rnd4 = randint(1, 100) / 100
                if rnd4 <= 0.05:
                    monster_list.append(troll)

                row[row.index(room)] = monster_list

        return monster_board

    def randomize_treasure(self):
        # makes a copy if the map woth treassures
        treasure_board = self.current_map.copy()

        loosecoins = Treasure('loose coins', 2, 0.4)
        moneypouch = Treasure('money pouch', 6, 0.2)
        goldjewelry = Treasure('golden jewelry', 10, 0.15)
        gemstone = Treasure('gemstone', 14, 0.1)
        smallchest = Treasure('small chest', 20, 0.05)
        for row in treasure_board:
            for room in row:
                treassure_list = []
                rnd1 = randint(1, 100) / 100
                if rnd1 <= 0.40:
                    treassure_list.append(loosecoins)
                rnd2 = randint(1, 100) / 100
                if rnd2 <= 0.20:
                    treassure_list.append(moneypouch)
                rnd3 = randint(1, 100) / 100
                if rnd3 <= 0.15:
                    treassure_list.append(goldjewelry)
                rnd4 = randint(1, 100) / 100
                if rnd4 <= 0.10:
                    treassure_list.append(gemstone)
                rnd5 = randint(1, 100) / 100
                if rnd5 <= 0.05:
                    treassure_list.append(smallchest)

                row[row.index(room)] = treassure_list
        return treasure_board

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
        try:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0] - 1][self.current_position[1]] = '@'
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
        except:
            print('Out of bounds')

    def move_down(self):
        try:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0] + 1][self.current_position[1]] = '@'
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        except:
            print('Out of bounds')

    def move_left(self):
        try:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0]][self.current_position[1] - 1] = '@'
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
        except:
            print('Out of bounds')

    def move_right(self):
        try:
            self.current_map[self.current_position[0]][self.current_position[1]] = 'O'
            self.current_map[self.current_position[0]][self.current_position[1] + 1] = '@'
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
        except:
            print('Out of bounds')
