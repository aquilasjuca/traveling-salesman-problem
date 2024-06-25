import random
import math
from models.traveling_salesman import TravelingSalesman

class SimulatedAnnealing:
    def __init__(self, tsp, initial_temp=1000, cooling_rate=0.995, min_temp=1):
        self.tsp = tsp
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.min_temp = min_temp

    def accept_probability(self, old_cost, new_cost, temperature):
        if new_cost < old_cost:
            return 1.0
        return math.exp((old_cost - new_cost) / temperature)

    def two_opt_swap(self, tour, i, j):
        new_tour = tour[:]
        new_tour[i:j+1] = reversed(tour[i:j+1])
        return new_tour

    def optimize(self):
        n = len(self.tsp.cities)
        current_tour = list(range(n))
        random.shuffle(current_tour)
        current_distance = self.tsp.distance(current_tour)
        best_tour = current_tour[:]
        best_distance = current_distance

        temperature = self.initial_temp
        step_count = 0

        while temperature > self.min_temp:
            i, j = sorted(random.sample(range(n), 2))
            new_tour = self.two_opt_swap(current_tour, i, j)
            new_distance = self.tsp.distance(new_tour)

            if self.accept_probability(current_distance, new_distance, temperature) > random.random():
                current_tour = new_tour
                current_distance = new_distance

                if current_distance < best_distance:
                    best_tour = current_tour[:]
                    best_distance = current_distance

            step_count += 1

            temperature *= self.cooling_rate

        self.print_step_count(step_count)
        return best_tour, best_distance

    def print_step_count(self, step_count):
        print(f"Quantidade de passos: {step_count}")
