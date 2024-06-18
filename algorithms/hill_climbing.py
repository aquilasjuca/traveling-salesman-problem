import random

def distance(cities, tour):
    return sum(cities[tour[i]][tour[i+1]] for i in range(len(tour) - 1)) + cities[tour[-1]][tour[0]]

def hill_climbing(cities):
    n = len(cities)
    current_tour = list(range(n))
    random.shuffle(current_tour)
    current_distance = distance(cities, current_tour)
    
    while True:
        neighbors = []
        for i in range(n):
            for j in range(i + 1, n):
                neighbor = current_tour[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        
        best_neighbor = min(neighbors, key=lambda tour: distance(cities, tour))
        best_neighbor_distance = distance(cities, best_neighbor)
        
        if best_neighbor_distance < current_distance:
            current_tour, current_distance = best_neighbor, best_neighbor_distance
        else:
            break
    
    return current_tour, current_distance

