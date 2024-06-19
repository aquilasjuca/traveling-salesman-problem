from models.traveling_salesman import TravelingSalesman
from algorithms.hill_climbing import HillClimbing
from file_management.TSPFileReader import *
# from algorithms.genetic_algorithm import GeneticAlgorithm
# from algorithms.simulated_annealing import SimulatedAnnealing

class TSPSolver:
    def __init__(self, cities):
        self.tsp = TravelingSalesman(cities)

    def solve_with_hill_climbing(self):
        hill_climbing = HillClimbing(self.tsp)
        return hill_climbing.optimize()

    # def solve_with_genetic_algorithm(self):
    #     genetic_algorithm = GeneticAlgorithm(self.tsp)
    #     return genetic_algorithm.optimize()

    # def solve_with_simulated_annealing(self):
    #     simulated_annealing = SimulatedAnnealing(self.tsp)
    #     return simulated_annealing.optimize()

def main():
    cities = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    archive_name = 'distance.txt'
    dist_reader = TSPFileReader(archive_name)
    dist_reader.read_file()

    for line in dist_reader.get_dist_mat():
        print(line)
        
    solver = TSPSolver(cities)

    print("Hill Climbing:")
    tour, dist = solver.solve_with_hill_climbing()
    print("Melhor rota:", tour)
    print("Distância:", dist)

    # print("\nAlgoritmo Genético:")
    # tour, dist = solver.solve_with_genetic_algorithm()
    # print("Melhor rota:", tour)
    # print("Distância:", dist)

    # print("\nTêmpera Simulada:")
    # tour, dist = solver.solve_with_simulated_annealing()
    # print("Melhor rota:", tour)
    # print("Distância:", dist)

if __name__ == "__main__":
    main()

