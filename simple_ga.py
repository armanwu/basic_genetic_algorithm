from random import randint

#generate individual
def individual(length, min, max):
    return[randint(min, max) for x in range(length)]

#generate population
def population(count, length, min, max):
    return[individual(length, min, max) for x in range(count)]

from operator import add
from functools import reduce

#create fitness
def fitness(individual, target):
    sum = reduce(add, individual)
    return abs(target - sum)

#create grade
def grade(pop, target):
    summed = reduce(add, (fitness(x, target) for x in pop))
    return summed / (len(pop) * 1.0)

from random import random

generation=population(5, 10, 0, 10)

#create mutation
def mutation(generation):
    prob_mutate = 0.5
    print(f'The population: {generation}\n')
    n = 0
    for i in generation:
        r = random()
        generation[n] = i
        print(f'This is individual number {n+1}')
        print(i)
        print(f'Random number for individual number {n+1} is', "{:.2f}".format(r))
        if prob_mutate > r:
            print('0.5 is bigger than', "{:.2f}".format(r))
            modify = randint(0, len(i)-1)
            mod = modify + 1
            print(f'So this individual will mutate on number {mod}')
            print(i[modify])
            i[modify] = randint(min(i), max(i))
        generation[n] = i
        n = n + 1
        print(i, "\n")
    return generation

mutation(generation)