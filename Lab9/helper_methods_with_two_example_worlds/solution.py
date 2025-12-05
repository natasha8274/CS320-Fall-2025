import random
from functools import partial
from util import cost, best_path


def optimize_path_crossover(parent1, parent2):
    size = len(parent1)

    #  Getting a random slice from parent1
    start = random.randint(0, size - 1)
    end = random.randint(0, size - 1)

    if start > end:
        start, end = end, start

    #  Initialize the child with None to track the empty spots
    child = [None] * size

    #  copy the slice from parent1 to the child
    for i in range(start, end + 1):
        child[i]  = parent1[i]

    curr_position = (end + 1) % size
    p2_position = (end + 1) % size

    #  fill the remaing positions using cities from parent2
    while None in child:
        city = parent2[p2_position]
        #  can only add the city if it isnt in the child
        if city not in child:
            child[curr_position] = city
            curr_position = (curr_position + 1) % size
        p2_position = (p2_position + 1) % size

    return tuple(child)


def mutate_path(path):
    path_list = list(path)

    index1, index2 = random.sample(range(len(path)), 2)

    path_list[index1], path_list[index2] = path_list[index2], path_list[index1]

    return tuple(path_list)


def ga_tsp(initial_population, distances, generations):

    if initial_population is None or distances is None or generations is None:
        raise ValueError("Invalid argument")

    if generations <= 0:
        raise ValueError("Invalid argiment")

    population = initial_population
    population_size = len(population)

    for _ in range(generations):
        #  sort the population by cost
        sorted_pop = sorted(population, key=partial(cost, distances=distances))

        #  keeping the top 50% as the elite group
        parents = sorted_pop[:population_size // 2]

        children = []

        #  keep generating children until it matches original size
        while len(children) < population_size:
            #  choose two parents randomly from the elite pool
            p1 = random.choice(parents)
            p2 = random.choice(parents)

            #  Uses helper method for crossover
            child = optimize_path_crossover(p1, p2)

            if random.random() < 0.1:
                child = mutate_path(child)

            children.append(child)

        #  Comvine the elite group with the new children
        combined_population = parents + children

        #  Sort them to keep only the top for the next generation 
        sorted_combined = sorted(combined_population, key=partial(cost, distances=distances))
        population = sorted_combined[:population_size]

    #  finally return the best path found in the final generation
    return best_path(population, distances)
