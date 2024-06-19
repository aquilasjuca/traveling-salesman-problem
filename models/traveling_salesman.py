import random

class TravelingSalesman:
    def __init__(self, cities):
        self.cities = cities

    def distance(self, tour):
        return sum(self.cities[tour[i]][tour[i+1]] for i in range(len(tour) - 1)) + self.cities[tour[-1]][tour[0]]

