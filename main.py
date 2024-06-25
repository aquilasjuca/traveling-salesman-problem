import time

from algorithms.hill_climbing import HillClimbing
from algorithms.simulated_annealing import SimulatedAnnealing
from file_management.TSPFileReader import TSPFileReader
from file_management.BestSolutionReader import BestSolutionReader
from models.traveling_salesman import TravelingSalesman

# from algorithms.genetic_algorithm import GeneticAlgorithm


class TSPSolver:
    def __init__(self, cities):
        self.tsp = TravelingSalesman(cities)

    def solve_with_hill_climbing(self):
        hill_climbing = HillClimbing(self.tsp)
        return hill_climbing.optimize()

# def solve_with_genetic_algorithm(self):
    #     genetic_algorithm = GeneticAlgorithm(self.tsp)
    #     return genetic_algorithm.optimize()

    def solve_with_simulated_annealing(self):
        simulated_annealing = SimulatedAnnealing(self.tsp)
        return simulated_annealing.optimize()


def print_menu():
    print("Escolha o algoritmo para resolver o problema do Caixeiro Viajante:")
    print("0 - Sair")
    print("1 - Hill Climbing")
    print("2 - Algoritmo Genético")
    print("3 - Têmpera Simulada")


def main():
    archive_name = "distance.txt"
    another_archive_name = "path.txt"
    dist_reader = TSPFileReader(archive_name)
    dist_reader.read_file()
    sol = BestSolutionReader(another_archive_name)
    solucao_otima = sol.read_file()
    solver = TSPSolver(dist_reader.get_dist_mat())

    while True:
        print_menu()
        choice = input("Digite a sua escolha: ")

        if choice == "1":
            print("Hill Climbing:")
            start_time = time.time()
            tour, dist = solver.solve_with_hill_climbing()
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Melhor rota:", tour)
            print("Distância:", dist)
            print(f"Tempo gasto: {elapsed_time:.2f} segundos")
            print("Solução Ótima:", solucao_otima)
            
        elif choice == "2":
            # print("Algoritmo Genético:")
            # start_time = time.time()
            # tour, dist = solver.solve_with_genetic_algorithm()
            # end_time = time.time()
            # elapsed_time = end_time - start_time
            # print("Melhor rota:", tour)
            # print("Distância:", dist)
            # print(f"Tempo gasto: {elapsed_time:.2f} segundos")
            print("Algoritmo Genético ainda não implementado.")

        elif choice == "3":
            print("Têmpera Simulada:")
            start_time = time.time()
            tour, dist = solver.solve_with_simulated_annealing()
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Melhor rota:", tour)
            print("Distância:", dist)
            print(f"Tempo gasto: {elapsed_time:.2f} segundos")
            print("Solução Ótima:", solucao_otima)

        elif choice == "0":
            break

        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()
