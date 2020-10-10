import time
from genetic_algorithm.initialize_population import InitialPopulation
from genetic_algorithm.crossover import Crossover
from genetic_algorithm.mutation import Mutation
from genetic_algorithm.selection import TournamentSelection


class Solver:
    """
    This is the base class for the solver method.
    """
    def __init__(self, objective_function=None):
        if objective_function:
            self.objective_function = objective_function
        else:
            raise AttributeError('Objective function missing.')

    def minimize_objective(self):
        raise NotImplementedError


class GeneticAlgorithm(Solver):
    """
    The Local-QUBO Solver uses a switch/permutation network to encode the QAP permutation
    in a bitstring.
    """
    def __init__(self,
                 objective_function=None,
                 experiment_type=None,
                 population_size=None,
                 pct_crossover=None,
                 pct_mutation=None,
                 num_iters=None):
        super().__init__(objective_function=objective_function)

        if population_size:
            self.population_size = population_size
        else:
            self.population_size = 1000

        if pct_crossover:
            self.pct_crossover = pct_crossover
        else:
            self.pct_crossover = 0.6

        if pct_mutation:
            self.pct_mutation = pct_mutation
        else:
            self.pct_mutation = 0.2

        # The default behavior here is to choose the smaller of either permutation or
        # sorting networks for the given input size.
        self.n_obj = self.objective_function.n
        self.stopwatch = 0

        # Initialize type of experiment
        # When running a timed experiment there is a high number of iterations and a 30 sec wall clock
        # When running a iteration experiment there is a iteration limit of 30 and no wall clock
        if experiment_type == 'time_lim':
            self.n_iters = 1000
            self.time_limit = 30

        if experiment_type == 'iter_lim' and num_iters:
            self.n_iters = num_iters
            self.time_limit = False
        else:
            self.n_iters = 50
            self.time_limit = False

        self.solution = self.objective_function.min_v

    def minimize_objective(self):
        start_code = time.time()

        data_dict = dict()
        data_dict['max_fitness'] = []
        data_dict['max_fitness_chromosome'] = []

        population = InitialPopulation(objective_function=self.objective_function,
                                       population_size=self.population_size).generate_initial_population()

        for iteration in range(self.n_iters):

            # If there is a timing limit and the stopwatch is greater than the timing limit then break
            if self.time_limit and self.time_limit <= self.stopwatch:
                break
            start_iteration = time.time()
            crossover_offspring = Crossover(population=population,
                                            percent_crossover=self.pct_crossover).perform_crossover()
            mutated_offspring = Mutation(population=population, percent_mutate=self.pct_mutation).perform_mutation()

            selection = TournamentSelection(final_population_size=self.population_size,
                                            input_population=population,
                                            mutated_offspring=mutated_offspring,
                                            crossover_offspring=crossover_offspring,
                                            objective_function=self.objective_function)

            population = selection.select_chromosomes()
            fitness = selection.chromosome_fitness(population)
            max_fitness = min(fitness)
            max_fit_chromosome = population[fitness.index(max_fitness)]

            data_dict['max_fitness'].append(max_fitness)
            data_dict['max_fitness_chromosome'].append(max_fit_chromosome)

            print("")
            print("Generation {}".format(iteration + 1))
            print("Max fitness: {}".format(max_fitness))
            print("Max fitness_chromosome: {}".format(max_fit_chromosome))

            end_iteration = time.time()
            self.stopwatch += end_iteration - start_iteration

        end_code = time.time()
        timing_code = end_code - start_code

        ga_ans = min(data_dict['max_fitness'])
        num_iters = len(data_dict['max_fitness'])

        percent_error = abs(self.solution - ga_ans) / self.solution * 100

        return ga_ans, percent_error, timing_code, num_iters, data_dict, data_dict['max_fitness']

