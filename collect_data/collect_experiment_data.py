from experiment_code.experiment_class import GAExperiment
from experiment_code.statistics_class import ExperimentStatistics
from utilities.objective_functions import QAPObjectiveFunction, TSPObjectiveFunction
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--sge_task_id",
                    type=int,
                    default=1)
args = parser.parse_args()
sge_task_id = args.sge_task_id


num_trials = 2
num_iters = 10
pct_crossover = 0.55
pct_mutation = 0.15
population_size = 10000


QAP_array = [
    'had4',
    'had6',
    'had8',
    'had10',
    'had12',
    'had14',
    'had16',
    'had18',
    'had20',
    'nug12',
    'nug14',
    'nug15',
    'nug16a',
    'nug16b',
    'nug17',
    'nug18',
    'nug20',
]

TSP_array = list(range(4, 21))

#  Decode the sge_task_id into index for solver and obj fcn array
if sge_task_id < 18:
    obj_fcn = QAPObjectiveFunction(dat_file=QAP_array[sge_task_id - 1] + '.dat',
                                   sln_file=QAP_array[sge_task_id - 1] + '.sln')
    if 'nug' in QAP_array[sge_task_id - 1]:
        instance = 'nug'
        size = QAP_array[sge_task_id - 1].replace(instance, '')
    else:
        instance = 'had'
        size = QAP_array[sge_task_id - 1].replace(instance, '')
else:
    obj_fcn = TSPObjectiveFunction(num_points=TSP_array[sge_task_id - 18])
    instance = 'tsp'
    size = str(TSP_array[sge_task_id - 18])


experiment = GAExperiment(
    save_csv=True,
    objective_function=obj_fcn,
    experiment_type='iter_lim',
    num_trials=num_trials,
    size=size,
    instance=instance,
    problem_type=instance,
    num_iters=num_iters,
    population_size=population_size,
    pct_crossover=pct_crossover,
    pct_mutation=pct_mutation,
)
run_experiment = experiment.run_experiment()
stats = ExperimentStatistics(results_dict=run_experiment).run_stats()



