import numpy as np


class Mutation:

    def __init__(self, population=None, percent_mutate=None):

        if population:
            self.population = population
        else:
            raise TypeError('Population Missing')

        # Note: percent_mutate is the percentage of input population that will undergo a mutation
        if percent_mutate:
            self.percent_mutate = percent_mutate
        else:
            raise TypeError('Percent Crossover Missing')

    @staticmethod
    def point_mutation(parent):

        # Pick a random gene to mutate
        random_gene = np.random.randint(0, len(parent))

        if parent[random_gene] == 0:
            parent[random_gene] = 1
        else:
            parent[random_gene] = 0

        return parent

    def perform_mutation(self):

        number_of_mutations = round(self.percent_mutate*len(self.population))
        mutation_offspring = []

        for _ in range(number_of_mutations):

            # Generate a random parent
            rand_parent = self.population[np.random.randint(0, len(self.population))]

            mutated_child = self.point_mutation(rand_parent)
            mutation_offspring.append(mutated_child)

        return mutation_offspring







