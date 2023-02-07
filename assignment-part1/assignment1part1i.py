import random
import numpy as np
import matplotlib.pyplot as plt

TARGET_STRING = "1" * 30
POPULATION_SIZE = 100
TOURNAMENT_SIZE = 5
CONVERGENCE_THRESHOLD = 2
MUTATION_RATE = 0.01

#initial population
population = [''.join(random.choices(['0', '1'], k=30)) for i in range(POPULATION_SIZE)]
average_fitness = []
generation = 0

def tournament_selection(population, fitness):
    tournament_participants = random.sample(population, TOURNAMENT_SIZE)
    tournament_fitness = [fitness[population.index(pos)] for pos in tournament_participants]
    # Select the best individual from the tournament
    return tournament_participants[tournament_fitness.index(max(tournament_fitness))]

while True:
    fitness = []
    for individual in population:
        #Count the number of 1s
        score = individual.count("1")
        #Store the fitness
        fitness.append(score)
    #Calculate average fitness
    avg_fitness = sum(fitness) / len(fitness)
    average_fitness.append(avg_fitness)
    best_fitness = max(fitness)
    worst_fitness = min(fitness)

    #Check for convergence
    if population.count(TARGET_STRING) > 0:
        break

    #Create a new population
    new_population = []
    for i in range(POPULATION_SIZE):
        #Select two individuals
        parent1 = tournament_selection(population, fitness)
        parent2 = tournament_selection(population, fitness)
        #Perform one-point crossover
        crossover_point = random.randint(1, 29)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        #Perform mutation
        for i in range(len(child)):
            if random.random() < MUTATION_RATE:
                if child[i] == "0":
                    child = child[:i] + "1" + child[i+1:]
                else:
                    child = child[:i] + "0" + child[i+1:]
                    
        new_population.append(child)
    #Replace old population with new
    population = new_population
    generation += 1

#Average fitness against num of generations
print(new_population)
plt.plot(range(0,generation+1), average_fitness)
plt.xlabel("Generations")
plt.ylabel("Average Fitness")
plt.show()
