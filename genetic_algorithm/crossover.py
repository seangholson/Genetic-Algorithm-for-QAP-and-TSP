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
    def single_point_crossover(parent1, parent2):

        """
        A single point crossover will pick a random point in in the chromosomes of the two parents and split each
        chromosome into two parts.  Then the children's chromosomes are made by combining the parts of the two parents
        chromosomes.
        """

        crossover_index = np.random.randint(0, len(parent1))

        parent1_gene_a = parent1[crossover_index:]
        parent2_gene_a = parent2[crossover_index:]

        parent1_gene_b = parent1[:crossover_index]
        parent2_gene_b = parent2[:crossover_index]

        child1 = [*parent1_gene_a, *parent2_gene_b]
        child2 = [*parent2_gene_a, *parent1_gene_b]

        return child1, child2

    def perform_crossover(self):

        number_of_crossovers = round(self.percent_crossover*len(self.population))
        crossover_offspring = []

        for _ in range(number_of_crossovers):

            # Generate two random parents
            parent1 = self.population[np.random.randint(0, len(self.population))]
            parent2 = self.population[np.random.randint(0, len(self.population))]

            child1, child2 = self.single_point_crossover(parent1=parent1, parent2=parent2)

            crossover_offspring.append(child1)
            crossover_offspring.append(child2)

        return crossover_offspring




