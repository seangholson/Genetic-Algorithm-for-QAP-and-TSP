import time
from switch_networks.switch_networks import PermutationNetwork, SortingNetwork
from genetic_algorithm.initialize_population import InitialPopulation
from genetic_algorithm.crossover import Crossover
from genetic_algorithm.mutation import Mutation
from genetic_algorithm.evaluate_fitness import EvaluateFitness
from genetic_algorithm.selection import Selection


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
                 num_iters=None,
                 network_type='minimum'):
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

        # Initialize switch network:
        # The default behavior here is to choose the smaller of either permutation or
        # sorting networks for the given input size.
        self.n_obj = self.objective_function.n
        if network_type == 'sorting':
            self.network = SortingNetwork(self.n_obj)
        elif network_type == 'permutation':
            self.network = PermutationNetwork(self.n_obj)
        elif network_type == 'minimum':
            s = SortingNetwork(self.n_obj)
            p = PermutationNetwork(self.n_obj)
            if s.depth <= p.depth:
                self.network = s
            else:
                self.network = p
        else:
            raise TypeError('Network type {} not recognized'.format(str(network_type)))

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

        population = InitialPopulation(objective_function=self.objective_function,
                                       network=self.network,
                                       population_size=self.population_size).generate_initial_population()

        for iteration in range(self.n_iters):

            # If there is a timing limit and the stopwatch is greater than the timing limit then break
            if self.time_limit and self.time_limit <= self.stopwatch:
                break
            start_iteration = time.time()
            crossover_offspring = Crossover(population=population,
                                            percent_crossover=self.pct_crossover).perform_crossover()
            mutated_offspring = Mutation(population=population, percent_mutate=self.pct_mutation).perform_mutation()

            evaluation = EvaluateFitness(input_population=population,
                                         mutated_offspring=mutated_offspring,
                                         crossover_offspring=crossover_offspring,
                                         objective_function=self.objective_function,
                                         network=self.network).evaluate_population_fitness()

            data_dict['max_fitness'].append(evaluation[0][0])

            population = Selection(population_size=self.population_size,
                                   population_fitness=evaluation).select_chromosomes()

            end_iteration = time.time()
            self.stopwatch += end_iteration - start_iteration

        end_code = time.time()
        timing_code = end_code - start_code

        ga_ans = min(data_dict['max_fitness'])
        num_iters = len(data_dict['max_fitness'])

        if ga_ans == self.solution:
            obtain_optimal = 1
            percent_error = 0
        else:
            percent_error = abs(self.solution - ga_ans) / self.solution * 100
            obtain_optimal = 0

        return ga_ans, percent_error, obtain_optimal, timing_code, num_iters, data_dict, data_dict['max_fitness']

