class maps:

    def __init__(self):
        self.sublist = []
        self.small_map = []
        self.medium_map = []
        self.large_map = []

   
    def show_small_map(self):
        self.sublist.clear()
        for x in range(4):
            self.sublist.append('X')
        for x in range(4):
            self.small_map.append(self.sublist)
        print('size 4x4:' )
        for small in self.small_map:
            print(small)

    def show_medium_map(self):
        self.sublist.clear()
        for x in range(5):
            self.sublist.append('X')
        for x in range(5):
            self.medium_map.append(self.sublist)
        print('size 5x5:')
        for medium in self.medium_map:
            print(medium)
    
    def show_large_map(self):
        self.sublist.clear()
        for x in range(8):
            self.sublist.append('X')
        for x in range(8):
            self.large_map.append(self.sublist)
        print('size 8x8:')
        for large in self.large_map:
            print(large)
