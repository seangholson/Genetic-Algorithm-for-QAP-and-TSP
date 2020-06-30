from experiment_code.experiment_class import GAExperiment
from experiment_code.statistics_class import ExperimentStatistics
from utilities.objective_functions import QAPObjectiveFunction, TSPObjectiveFunction

obj = TSPObjectiveFunction(num_points=20)

GA = GAExperiment(save_csv=True,
                  instance='tsp',
                  size='20',
                  population_size=1000,
                  pct_crossover=0.6,
                  pct_mutation=0.1,
                  problem_type='tsp',
                  objective_function=obj,
                  num_trials=10,
                  num_iters=30,
                  experiment_type='iter_lim')
GA_stats = ExperimentStatistics(results_dict=GA.run_experiment())
GA_stats_results = GA_stats.run_stats()

print("Percent Error: {}".format(GA_stats_results['percent_error']))
print("Timing of Code: {}".format(GA_stats_results['timing_code']))
print("Number of iterations: {}".format(GA_stats_results['number_of_iterations']))

