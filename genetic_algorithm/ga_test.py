from utilities.objective_functions import QAPObjectiveFunction, TSPObjectiveFunction
from switch_networks.switch_networks import PermutationNetwork, SortingNetwork
from genetic_algorithm.initialize_population import InitialPopulation
from genetic_algorithm.crossover import Crossover
from genetic_algorithm.mutation import Mutation
from genetic_algorithm.evaluate_fitness import EvaluateFitness
from genetic_algorithm.selection import Selection

obj = QAPObjectiveFunction(dat_file='had20.dat', sln_file='had20.sln')
solution = obj.min_v
number_of_generations = 30
population_size = 1000
percent_crossover = 0.6
percent_mutation = 0.1

s = SortingNetwork(obj.n)
p = PermutationNetwork(obj.n)
if s.depth <= p.depth:
    network = s
else:
    network = p

population = InitialPopulation(objective_function=obj,
                               network=network,
                               population_size=population_size).generate_initial_population()
max_fitness = []

for _ in range(number_of_generations):

    crossover_offspring = Crossover(population=population, percent_crossover=percent_crossover).perform_crossover()
    mutated_offspring = Mutation(population=population, percent_mutate=percent_mutation).perform_mutation()

    evaluation = EvaluateFitness(input_population=population,
                                 mutated_offspring=mutated_offspring,
                                 crossover_offspring=crossover_offspring,
                                 objective_function=obj,
                                 network=network).evaluate_population_fitness()

    max_fitness.append(evaluation[0][0])
    population = Selection(population_size=population_size, population_fitness=evaluation).select_chromosomes()

    print('Max Fitness: {}'.format(evaluation[0][0]))

ga_answer = min(max_fitness)
percent_error = (abs(ga_answer - solution)/solution)*100
print('Final Answer: {}'.format(ga_answer))
print('Percent Error: {}'.format(percent_error))





