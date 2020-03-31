import numpy as np


class InitialPopulation:

    def __init__(self, objective_function=None, network=None, population_size=None):

        if objective_function:
            self.objective_function = objective_function
        else:
            raise TypeError('Objective Function Missing')

        if network:
            self.network = network
        else:
            raise TypeError('Network Missing')

        self.population_size = population_size

    def generate_initial_population(self):

        population = []
        for _ in range(self.population_size):
            rand_chromosome = np.random.randint(0, 2, size=self.network.depth)
            population.append(rand_chromosome)

        return population
