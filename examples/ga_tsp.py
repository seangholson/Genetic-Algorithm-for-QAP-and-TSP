from utilities.objective_functions import TSPObjectiveFunction
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

obj = TSPObjectiveFunction(num_points=20)
solution = obj.min_v
number_of_generations = 50
population_size = 1000
percent_crossover = 0.6
percent_mutation = 0.1

GA = GeneticAlgorithm(objective_function=obj,
                      experiment_type='iter_lim',
                      population_size=population_size,
                      pct_crossover=percent_crossover,
                      pct_mutation=percent_mutation,
                      num_iters=number_of_generations)

GA_response = GA.minimize_objective()

print("")
print("GA answer: {}".format(GA_response[0]))
print("Percent Error: {}".format(GA_response[1]))
print("Timing of code: {}".format(GA_response[2]))
print("Correct answer: {}".format(solution))





