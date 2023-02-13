import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TARGET_STRING = ''.join(random.choices(['0','1','2','3','4','5','6','7','8','9'], k=30))

POPULATION_SIZE = 50
TOURNAMENT_SIZE = 5
CONVERGENCE_THRESHOLD = 5
MUTATION_RATE = 0.03

#initial population
population = [''.join(random.choices(['0','1','2','3','4','5','6','7','8','9'], k=30)) for _ in range(POPULATION_SIZE)]
print(population)
average_fitness = []
generation = 0

def tournament_selection(population, fitness):
    tournament_participants = random.sample(population, TOURNAMENT_SIZE)
    tournament_fitness = [fitness[population.index(pos)] for pos in tournament_participants]
    # Select the best individual from the tournament
    return tournament_participants[tournament_fitness.index(min(tournament_fitness))]

def calc_fitness(individual):
    score = 0
    for i in range(len(individual)):
       score += abs(int(TARGET_STRING[i]) - int(individual[i]))
    # score = sum(a == b for a, b in zip(individual, TARGET_STRING))
    return score

while True:
    fitness = []
    for individual in population:
        score = calc_fitness(individual)
        #Store the fitness
        fitness.append(score)
    #Calculate average fitness
    avg_fitness = sum(fitness) / len(fitness)
    average_fitness.append(avg_fitness)
    best_fitness = min(fitness)
    worst_fitness = max(fitness)
    print("worst: ",worst_fitness, "Best: ", best_fitness)

    #Check for convergence
    if population.count(TARGET_STRING)>0:
        print("found")
        break

    # #Check for convergence
    # if best_fitness - worst_fitness <= CONVERGENCE_THRESHOLD or population.count(TARGET_STRING)>0:
    #     print("converged")
    #     break

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
        for j in range(len(child)):
            if random.random() < MUTATION_RATE:
                    child = child[:j] + ''.join(random.choices(['0','1','2','3','4','5','6','7','8','9'])) + child[j+1:]
                    
        new_population.append(child)
    #Replace old population with new
    population = new_population
    generation += 1
print(population)
print(TARGET_STRING)

#Average fitness against num of generations
plt.plot(range(0,generation+1), average_fitness)
plt.xlabel("Generations")
plt.ylabel("Average Fitness")
plt.show()
