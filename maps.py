class maps:

    def __init__(self):
        self.active_map = ''
        self.small_map = []
        self.medium_map = []
        self.large_map = []

    def create_small_map(self):
        self.small_map = [['X'] * 4 for i in range(4)]
        

    def create_medium_map(self):
        self.medium_map = [['X'] * 5 for i in range(5)]


    def create_large_map(self):
        self.large_map = [['X'] * 8 for i in range(8)]
    
    def show_small_map(self):
        print('size 4x4:' )
        for small in self.small_map:
            print(small)
    

    def show_medium_map(self):        
        print('size 5x5:')
        for medium in self.medium_map:
            print(medium)
        
    
    def show_large_map(self):
        print('size 8x8:')
        for large in self.large_map:
            print(large)

    def move_upwards(self):
       pass
    
    def place_player(self, mapsize, corner):
        #use 's','m','l' to ensure the correct map is updated
        #ul = upper left
        if mapsize == 's':
            mapsize = self.small_map
        if mapsize == 'm':
            mapsize = self.medium_map
        if mapsize == 'l':
            mapsize = self.large_map

        if corner == 'ul':
            mapsize[0][0] = '@'
        if corner == 'ur':
            mapsize[0][len(mapsize)-1] = '@'
        if corner == 'lr':
            mapsize[len(mapsize)-1][len(mapsize)-1] = '@'
        if corner == 'll':
            mapsize[len(mapsize)-1][0] = '@'





