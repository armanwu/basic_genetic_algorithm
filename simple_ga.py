from random import randint

#generate individual
def individual(length, min, max):
    return[randint(min, max) for x in range(length)]
#sample: print(individual(10, 0, 10))

#generate population
def population(count, length, min, max):
    return[individual(length, min, max) for x in range(count)]
#sample: print(population(10, 10, 0, 10))

from operator import add
from functools import reduce

#create fitness
def fitness(individual, target):
    sum = reduce(add, individual)
    return abs(target-sum)
"""
sample:
a = individual(10, 0, 10)
print(a)
print(reduce(add, a, 0))
print(fitness(a, 100))
"""

#create grade
def grade(pop, target):
    summed = reduce(add, fitness(x, target) for x in pop)
    return summed/(len(pop)*1.0)


