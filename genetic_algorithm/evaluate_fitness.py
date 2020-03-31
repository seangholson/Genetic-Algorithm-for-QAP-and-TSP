
class EvaluateFitness:

    def __init__(self,
                 input_population=None,
                 mutated_offspring=None,
                 crossover_offspring=None,
                 objective_function=None,
                 network=None):

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

        if network:
            self.network = network
        else:
            raise TypeError('Network Missing')

        self.total_population = input_population + mutated_offspring + crossover_offspring

    @staticmethod
    def sort_first(val):
        return val[0]

    def evaluate_population_fitness(self):
        population_fitness = []
        for chromosome in self.total_population:
            permutation = self.network.permute(chromosome)
            fitness = self.objective_function(permutation)
            # Fill population_fitness array with fitness value and corresponding chromosome
            population_fitness.append([fitness, chromosome])

        # Sort population by descending fitness score
        population_fitness.sort(key=self.sort_first)

        return population_fitness

