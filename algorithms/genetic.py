import random

class Genetic:
    def __init__(self, tsp, population_size=50, mutation_rate=0.01):
        self.tsp = tsp
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.steps = 0  
        self.max_iterations = 1000  
        self.iterations_without_improvement = 0

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            tour = list(range(len(self.tsp.cities)))
            random.shuffle(tour)
            population.append(tour)
        return population

    def crossover(self, parent1, parent2):
        n = len(parent1)
        start, end = sorted(random.sample(range(n), 2))
        offspring = [-1] * n
        for i in range(start, end + 1):
            offspring[i] = parent1[i]

        remaining = [item for item in parent2 if item not in offspring]
        j = 0
        for i in range(n):
            if offspring[i] == -1:
                offspring[i] = remaining[j]
                j += 1
        return offspring

    def mutate(self, tour):
        if random.random() < self.mutation_rate:
            n = len(tour)
            i, j = random.sample(range(n), 2)
            tour[i], tour[j] = tour[j], tour[i]
        return tour

    def evolve_population(self, population):
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = random.sample(population, 2)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            new_population.append(child)
        return new_population

    def optimize(self):
        population = self.initialize_population()
        best_tour = min(population, key=lambda tour: self.tsp.distance(tour))
        best_distance = self.tsp.distance(best_tour)

        while self.iterations_without_improvement < self.max_iterations:
            new_population = self.evolve_population(population)
            new_best_tour = min(new_population, key=lambda tour: self.tsp.distance(tour))
            new_best_distance = self.tsp.distance(new_best_tour)

            if new_best_distance < best_distance:
                best_tour, best_distance = new_best_tour, new_best_distance
                self.iterations_without_improvement = 0
            else:
                self.iterations_without_improvement += 1

            self.steps += 1

        print("Número de passos (generations):", self.steps)

        return best_tour, best_distance
