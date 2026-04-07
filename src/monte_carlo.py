import random

class MonteCarloSim:
    def __init__(self, **kwargs):
        # This fixes the 'unexpected keyword argument' errors
        self.probability = kwargs.get('probability', 0.045)
        self.trials = kwargs.get('trials', 10000)
        self.base_salary = kwargs.get('base_salary', 50000)

    def run_simulation(self):
        # Server crash simulation
        crashes = 0
        for _ in range(self.trials):
            if random.random() < self.probability:
                crashes += 1
        return crashes / self.trials

    def run_salary_sim(self):
        # Returns a LIST of 50 salaries so StatEngine doesn't error
        projected = []
        for _ in range(50):
            growth = self.base_salary * (1 + random.uniform(0.02, 0.05))
            projected.append(growth)
        return projected
