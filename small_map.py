
class maps:

    def __init__(self):
        self.small_map = [['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x']]
        self.medium_map = [['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']]


    def map_4x4(self):
        print("4x4 size :")
        for small in self.small_map:
            print(small)

    def map_5x5(self):
        print("5x5 size :")
        for medium in self.medium_map:
            print(medium)


x = maps()
x.map_4x4()
x.map_5x5()

