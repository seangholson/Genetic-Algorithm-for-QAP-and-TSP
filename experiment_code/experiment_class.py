# Built-ins:
from datetime import datetime


# Installed packages:

# Project locals:
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

# These are the valid experiment types:
experiment_types = [
    'time_lim',
    'iter_lim',
]


class GAExperiment:
    """
    This class is designed to run multiple trials of a solver for a
    specified QAP/ TSP and collect data.
    """
    def __init__(self,
                 save_csv=None,
                 instance=None,
                 size=None,
                 population_size=None,
                 pct_crossover=None,
                 pct_mutation=None,
                 problem_type=None,
                 objective_function=None,
                 num_trials=None,
                 num_iters=None,
                 experiment_type=None):

        # Initialize objective function
        if objective_function:
            self.objective_function = objective_function
            self.answer = objective_function.min_v
        else:
            raise AttributeError('Objective function missing.')

        # Initialize number of trials in experiment
        if num_trials:
            self.num_trials = num_trials
        else:
            self.num_trials = 10

        if num_iters:
            self.num_iters = num_iters
        else:
            self.num_iters = 10

        self.instance = instance
        self.problem_type = problem_type
        self.size = size
        self.save_csv = save_csv
        self.solver_str = 'Genetic Algorithm'

        if experiment_type in experiment_types:
            self.experiment_str = experiment_type
        else:
            raise AttributeError('Invalid experiment type')

        self.solver = GeneticAlgorithm(objective_function=self.objective_function,
                                       experiment_type=self.experiment_str,
                                       population_size=population_size,
                                       pct_mutation=pct_mutation,
                                       pct_crossover=pct_crossover,
                                       num_iters=self.num_iters)

    def run_experiment(self):
        results = dict()
        main_key = 'solver, size, experiment type, problem type, instance, save_csv bool, answer'
        results[main_key] = [self.solver_str,
                             self.size,
                             self.experiment_str,
                             self.problem_type,
                             self.instance,
                             self.save_csv,
                             self.answer]
        results['approx_ans'] = []
        results['percent_error'] = []
        results['obtain_optimal'] = []
        results['timing_code'] = []
        results['number_of_iterations'] = []
        results['max_fitness_array'] = []

        for trial in range(self.num_trials):
            t = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            f = self.objective_function.dat_file
            s = self.solver_str
            e = self.experiment_str
            print(f'{t} {f} {s} {e} trial {trial+1} starting trial')

            solver = self.solver
            solver_ans = solver.minimize_objective()

            results['approx_ans'].append(solver_ans[0])
            results['percent_error'].append(solver_ans[1])
            results['obtain_optimal'].append(solver_ans[2])
            results['timing_code'].append(solver_ans[3])
            results['number_of_iterations'].append(solver_ans[4])
            results['trial_{}_data_dict'.format(trial + 1)] = solver_ans[5]
            results['max_fitness_array'].append(solver_ans[6])

        t = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f = self.objective_function.dat_file
        s = self.solver_str
        print(f'{t} {f} {s} experiment finished')

        return results


