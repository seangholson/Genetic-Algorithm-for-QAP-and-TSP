import numpy as np


class TournamentSelection:

    def __init__(self,
                 final_population_size=None,
                 input_population=None,
                 mutated_offspring=None,
                 crossover_offspring=None,
                 objective_function=None):

        if not input_population:
            raise TypeError('Population Missing')

        if not mutated_offspring:
            raise TypeError('Mutated Offspring Missing')

        if not crossover_offspring:
            raise TypeError('Crossover Offspring Missing')

        if objective_function:
            self.objective_function = objective_function
        else:
            raise TypeError('Objective Function Missing')

        self.final_population_size = final_population_size
        self.total_population = input_population + mutated_offspring + crossover_offspring

    # Select 4 random chromosomes and best fit of 4 pass selection
    def tournament_selection(self, population):
        rand_chromosomes = []
        fitness = []
        for _ in range(4):
            chromosome = population[np.random.randint(0, len(population))]
            rand_chromosomes.append(chromosome)
            fitness.append(self.objective_function(chromosome))

        return rand_chromosomes[fitness.index(min(fitness))]

    def select_chromosomes(self):

        selected_chromosomes = []
        for _ in range(self.final_population_size):
            selected_chromosomes.append(self.tournament_selection(population=self.total_population))
        return selected_chromosomes

    def chromosome_fitness(self, selected_chromosomes):
        chromosome_fitness = []
        for chromosome in selected_chromosomes:
            chromosome_fitness.append(self.objective_function(chromosome))

        return chromosome_fitness

