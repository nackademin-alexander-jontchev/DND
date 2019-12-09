class maps:

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