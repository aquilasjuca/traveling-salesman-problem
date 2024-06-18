from algorithms.hill_climbing import hill_climbing
#from algorithms.genetic_algorithm import genetic_algorithm
#from algorithms.simulated_annealing import simulated_annealing

# Defina suas cidades aqui (matriz de distâncias)
cities = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def main():
    print("Hill Climbing:")
    tour, dist = hill_climbing(cities)
    print("Melhor rota:", tour)
    print("Distância:", dist)
    
    #print("\nAlgoritmo Genético:")
    #tour, dist = genetic_algorithm(cities)
    #print("Melhor rota:", tour)
    #print("Distância:", dist)
    
    #print("\nTêmpera Simulada:")
    #tour, dist = simulated_annealing(cities)
    #print("Melhor rota:", tour)
    #print("Distância:", dist)

if __name__ == "__main__":
    main()

