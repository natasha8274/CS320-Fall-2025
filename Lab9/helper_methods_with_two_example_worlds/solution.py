import random 

def ga_tsp(initial_population, distances, generations):
    
    if initial_population is None or distances is None or generations is None:
        raise ValueError("Invalid argument")
        
    if generations <= 0:
        raise ValueError("Invalid argiment")
    
    population = initial_population
    population_size = len(population)
    
    
