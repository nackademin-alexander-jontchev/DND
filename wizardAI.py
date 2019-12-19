from monsters import Monsters
from random import choice

big_spider = Monsters(' Big spider', 7, 1, 2, 3, 0.2)
orc = Monsters('Orc', 6, 3, 4, 4, 0.1)
troll = Monsters('Troll', 2, 4, 7, 2, 0.05)
skeleton = Monsters('Skeleton', 4, 2, 3, 3, 0.15)


class WixardAI:

    def __init__(self):
        self.corner = '4'
        self.movement = 'w'
        self.mapsz = ''
        self.current_pos = ()
        self.lst = ['w','d','s','a']
        self.rooms_been_in = []
        self.defeated_monsters = 0

    def change_direction(self, current_pos):
        x = current_pos[1]
        y = current_pos[0]

        self.rooms_been_in.append(current_pos)

        if current_pos in self.rooms_been_in:
            self.movement = choice(self.lst)

        if self.movement == 'w' and y == 0:
            self.movement = choice(self.lst)
        if self.movement == 'a' and x == 0:
            self.movement = choice(self.lst)
        if self.movement == 's' and y == self.mapsz-1:
            self.movement = choice(self.lst)
        if self.movement == 'd' and x == self.mapsz-1:
            self.movement = choice(self.lst)

    
    def fighting(self, monsters):

        return '1'