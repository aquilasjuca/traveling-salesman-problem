import random
from models.traveling_salesman import TravelingSalesman

class HillClimbing:
    def __init__(self, tsp):
        self.tsp = tsp

    def optimize(self):
        n = len(self.tsp.cities)
        current_tour = list(range(n))
        random.shuffle(current_tour)
        current_distance = self.tsp.distance(current_tour)

        while True:
            neighbors = []
            for i in range(n):
                for j in range(i + 1, n):
                    neighbor = current_tour[:]
                    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                    neighbors.append(neighbor)

            best_neighbor = min(neighbors, key=lambda tour: self.tsp.distance(tour))
            best_neighbor_distance = self.tsp.distance(best_neighbor)

            if best_neighbor_distance < current_distance:
                current_tour, current_distance = best_neighbor, best_neighbor_distance
            else:
                break

        return current_tour, current_distance

