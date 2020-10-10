import numpy as np


class Crossover:

    def __init__(self, population=None, percent_crossover=None):

        if population:
            self.population = population
        else:
            raise TypeError('Population Missing')

        # Note: percent_crossover is the percentage of input population that will produce two children
        if percent_crossover:
            self.percent_crossover = percent_crossover
        else:
            raise TypeError('Percent Crossover Missing')

    @staticmethod
    def ordered_crossover(parent1, parent2):

        """
        An ordered crossover will take a segment of the two parents chromosomes (permutations) and swap them while
        preserving the relative ordering of the parents as much as possible.
        """
        n_obj = len(parent1)
        crossover_index_start = np.random.randint(1, n_obj)

        p1_copy = parent1.copy()
        p2_copy = parent2.copy()

        child1 = []
        child2 = []
        for i in range(n_obj):
            child1.append('None')
            child2.append('None')

        for i in range(crossover_index_start, n_obj):
            child1[i] = parent2[i]
            child2[i] = parent1[i]

        # Remove values from parent (copy) that already exist in children
        for val in child1:
            if val != 'None':
                p1_copy = np.delete(p1_copy, np.where(p1_copy == val))

        for val in child2:
            if val != 'None':
                p2_copy = np.delete(p2_copy, np.where(p2_copy == val))

        j = 0
        k = 0
        for i in range(n_obj):
            if child1[i] == 'None':
                child1[i] = p1_copy[j]
                j = j + 1
            if child2[i] == 'None':
                child2[i] = p2_copy[k]
                k = k + 1

        return child1, child2

    def perform_crossover(self):

        number_of_crossovers = round(self.percent_crossover*len(self.population))
        crossover_offspring = []

        for _ in range(number_of_crossovers):

            # Generate two random parents
            parent1 = self.population[np.random.randint(0, len(self.population))]
            parent2 = self.population[np.random.randint(0, len(self.population))]

            child1, child2 = self.ordered_crossover(parent1=parent1, parent2=parent2)

            crossover_offspring.append(child1)
            crossover_offspring.append(child2)

        return crossover_offspring




