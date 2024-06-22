import random
import math
from file_mangement.sp_file_reader import TSPFileReader

class GeneticAlgorithm:
    def __init__(self, tsp_reader, population_size=50, crossover_rate=0.8, mutation_rate=0.02, generations=1000):
        self.tsp_reader = tsp_reader
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.dimension = tsp_reader.get_dimension()
        self.edge_weights = tsp_reader.get_edge_weights()
        self.best_solution = None
        self.best_fitness = float('inf')

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = list(range(1, self.dimension + 1))
            random.shuffle(individual)
            population.append(individual)
        return population

    def evaluate_fitness(self, individual):
        total_distance = 0
        for i in range(self.dimension - 1):
            start = individual[i] - 1
            end = individual[i + 1] - 1
            total_distance += self.edge_weights[start][end]
        # Add distance from last city back to the first city
        start = individual[-1] - 1
        end = individual[0] - 1
        total_distance += self.edge_weights[start][end]
        return total_distance

    def select_parents(self, population):
        # Tournament selection
        tournament_size = 3
        selected_parents = []
        for _ in range(2):
            tournament = random.sample(population, tournament_size)
            tournament.sort(key=lambda x: self.evaluate_fitness(x))
            selected_parents.append(tournament[0])
        return selected_parents

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            # Order crossover (OX1)
            start_idx = random.randint(0, self.dimension - 1)
            end_idx = random.randint(start_idx + 1, self.dimension)
            child = [-1] * self.dimension
            for i in range(start_idx, end_idx):
                child[i] = parent1[i]
            remaining_elements = [item for item in parent2 if item not in child]
            insert_idx = 0
            for i in range(self.dimension):
                if child[i] == -1:
                    child[i] = remaining_elements[insert_idx]
                    insert_idx += 1
            return child
        else:
            return parent1

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            # Swap mutation
            idx1, idx2 = random.sample(range(self.dimension), 2)
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

    def run_genetic_algorithm(self):
        population = self.initialize_population()

        for generation in range(1, self.generations + 1):
            new_population = []

            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents(population)
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                self.mutate(child1)
                self.mutate(child2)
                new_population.extend([child1, child2])

            population = new_population

            # Find the best individual in the current population
            best_individual = min(population, key=self.evaluate_fitness)
            best_fitness = self.evaluate_fitness(best_individual)

            # Update the best solution found so far
            if best_fitness < self.best_fitness:
                self.best_solution = best_individual
                self.best_fitness = best_fitness

            # Print progress every 100 generations
            if generation % 100 == 0:
                print(f"Generation {generation}: Best Fitness = {self.best_fitness}")

        print("\nGenetic Algorithm completed.")
        print(f"Best Solution: {self.best_solution}")
        print(f"Best Fitness: {self.best_fitness}")