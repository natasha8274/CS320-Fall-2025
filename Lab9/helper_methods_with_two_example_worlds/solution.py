import random
from functools import partial
from util import cost, best_path


def optimize_path_crossover(parent1, parent2):
    child = [None]
    return tuple(child)
def ga_tsp(initial_population, distances, generations):
    
    if initial_population is None or distances is None or generations is None:
        raise ValueError("Invalid argument")
        
    if generations <= 0:
        raise ValueError("Invalid argiment")
    
    population = initial_population
    population_size = len(population)
    
    for _ in range(generations):
        sorted_pop = sorted(population, key=partial(cost, distances=distances))
        
        parents = sorted_pop[:population_size // 2]
        
        children = []
        while len(children) < population_size:
            #  choose two parents randomly from the elite pool
            p1 = random.choice(parents)
            p2 = random.choice(parents)
            
            child = optimize_path_crossover(p1, p2)
            
        
    
