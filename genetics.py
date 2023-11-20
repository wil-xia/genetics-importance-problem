# William Xia
# 10/29/23
# Assignment 3: Genetic Algorithms

# This program searches for the best configuration of weighted boxes in a 
# backpack of limited size. Each box has a unique weight value and importance
# value, the backpack can hold up to 250 pounds (weight value). The algorithm
# will find the most optimal configuration for the max importance value using a
# Genetic Algorithm

import random

# Set of all boxes and their respective importance values
# (Weight, Importance)
boxes = [
    (20, 6),
    (30, 5),
    (60, 8),
    (90, 7),
    (50, 6),
    (70, 9),
    (30, 4),
    (30, 5),
    (70, 4),
    (20, 9),
    (20, 2),
    (60, 1)
]

# Get Genetic algorithm constants from User
while True:
    try:
        population_size = int(input("Enter the population size for the Genetic Algorithm: "))
        if(population_size<1):
            print("Invalid size, please enter an integer greater than 0")
            print("")
        break
    except ValueError:
        print("Invalid input. Please enter an integer")
        print("")

while True:
    try:
        num_generations = int(input("Enter the number of generations for the Genetic Algorithm (Culling/mutation cycles): "))
        if(num_generations<1):
            print("Invalid number, please enter an integer greater than 0")
            print("")
        break
    except ValueError:
        print("Invalid input. Please enter an integer")
        print("")    

while True:
    try:
        mutation_rate = int(input("Enter the % Mutation Chance for each individual each cycle (Integer 0-50): "))
        if(mutation_rate<0):
            print("Invalid number, please enter a postive integer")
            print("")
        if(mutation_rate>50):
            print("Invalid number, please enter a percent value 50 or less")
            print("")
        break
    except ValueError:
        print("Invalid input. Please enter an integer")
        print("")    

mutation_rate = mutation_rate/100


# population_size = 100
# num_generations = 100
# mutation_rate = 0.1

# Initialize the population with random indivduals
# For each box, each indivdual generated will have a random chance to include (1)
# or exclude (0) that box. We don't account for the maximum weight here, since
# we can declare boxes overweight boxes unfit during the culling/mutation
population = [random.choices([0, 1], k=len(boxes)) for _ in range(population_size)]

# Return the fitness of a given individual
def fitness(individual):
    # calculate and check if overweight, return 0 (unfit) if so
    total_weight = sum(boxes[i][0] for i in range(len(individual)) if individual[i] == 1)
    if total_weight > 250:
        return 0 

    total_importance = sum(boxes[i][1] for i in range(len(individual)) if individual[i] == 1)
    return total_importance

# x=0
# for i in population:
#     print(i)
#     x=x+1
#     print(x)

# print(population[0])

# Main loop for genetic algorithm
print("Running Algorithm....")
for generation in range(num_generations):
    # Evaluate the fitness of each genome
    fitness_scores = [fitness(individual) for individual in population]

    # Selection: Choose parents based on fitness
    # Each parent is selected randomly, with favor based on those with higher fitness scores, 
    # The same individual can be selected multiple times as a parent, and it's possible that not 
    # all individuals in the population will be selected as parents.
    selected_parents = random.choices(population, weights=fitness_scores, k=population_size)

    # Crossover: Create new genomes by combining parents
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = random.sample(selected_parents, 2)
        crossover_point = random.randint(1, len(boxes) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        new_population.extend([child1, child2])
    
    # Culling: Keep the top 50% of genomes
    # Create new dual list with fitness scores, sort, then delete half
    population_with_fitness = list(zip(population, fitness_scores))
    population_with_fitness.sort(key=lambda x: x[1], reverse=True)
    population = [individual for individual, _ in population_with_fitness[:population_size // 2]]

    # After culling, append new children to original population array
    population.extend(new_population)

    # Mutation: Introduce random changes to genomes
    for i in population:
        #randomly check if mutation occurs
        if random.random() < mutation_rate:
            #randomly decide the location of the mutation
            mutation_point = random.randint(0, len(boxes) - 1)
            #swap the value at the mutation location
            i[mutation_point] = 1 - i[mutation_point]

    
# Get the best solution after all generations
best_solution, best_fitness = max(zip(population, fitness_scores), key=lambda x: x[1])

#print results
print("")
print("Best Solution Found!")
print("Bag Configuration: ", best_solution)
temp = 0
total_weight = 0
for i in best_solution:
    if(i == 1):
        total_weight = total_weight + boxes[temp][0]
    temp = temp + 1
print("Total Weight:", total_weight)
print("Total Importance Value:", best_fitness)
