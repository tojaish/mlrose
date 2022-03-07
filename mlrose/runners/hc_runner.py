import mlrose
from mlrose.decorators import short_name

from mlrose.runners._runner_base import _RunnerBase

"""
Example usage:

    experiment_name = 'example_experiment'
    problem = TSPGenerator.generate(seed=SEED, number_of_cities=22)

    hc = HCRunner(problem=problem,
                    experiment_name=experiment_name,
                    output_directory=OUTPUT_DIRECTORY,
                    seed=SEED,
                    iteration_list=2 ** np.arange(10),
                    max_attempts=5000,
                    restart_list=[25, 75, 100])   

    # the two data frames will contain the results
    df_run_stats, df_run_curves = hc.run()               
"""


@short_name('hc')
class HCRunner(_RunnerBase):

    def __init__(self, problem, experiment_name, seed, iteration_list, restart_list,
                 max_attempts=500, generate_curves=True, **kwargs):
        super().__init__(problem=problem, experiment_name=experiment_name, seed=seed, iteration_list=iteration_list,
                         max_attempts=max_attempts, generate_curves=generate_curves,
                         **kwargs)
        self.restart_list = restart_list

    def run(self):
        return super().run_experiment_(algorithm=mlrose.hill_climb,
                                       restarts=('Restarts', self.restart_list))
