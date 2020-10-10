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
    def swap_mutation(parent):

        # Pick 2 random points to swap
        random_gene_loc1 = np.random.randint(0, len(parent))
        random_gene_loc2 = np.random.randint(0, len(parent))

        parent[random_gene_loc1], parent[random_gene_loc2] = parent[random_gene_loc2], parent[random_gene_loc1]

        return parent

    def perform_mutation(self):

        number_of_mutations = round(self.percent_mutate*len(self.population))
        mutation_offspring = []

        for _ in range(number_of_mutations):

            # Generate a random parent
            rand_parent = self.population[np.random.randint(0, len(self.population))]

            mutated_child = self.swap_mutation(rand_parent)
            mutation_offspring.append(mutated_child)

        return mutation_offspring







