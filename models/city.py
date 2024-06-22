import math

class City:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def distance_to(self, other_city):
        return math.sqrt((self.x - other_city.x) ** 2 + (self.y - other_city.y) ** 2)