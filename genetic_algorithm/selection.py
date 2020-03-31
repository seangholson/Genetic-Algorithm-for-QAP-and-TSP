
class Selection:

    def __init__(self, population_fitness=None, population_size=None):

        if population_fitness:
            self.population_fitness = population_fitness
        else:
            raise TypeError('Population Fitness Missing')

        if population_size:
            self.population_size = population_size
        else:
            raise TypeError('Selection Probability Missing')

    def select_chromosomes(self):

        selected_chromosomes = []
        for chromosome in range(self.population_size):

            selected_chromosome = self.population_fitness[chromosome][1]

            selected_chromosomes.append(selected_chromosome)

        return selected_chromosomes



