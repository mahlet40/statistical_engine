import random

class MonteCarloSim:
    def __init__(self, base_salary, iterations=1000):
        # This MUST be indented once (1 Tab)
        self.base_salary = base_salary
        self.iterations = iterations

    def run_simulation(self):
        # This MUST be indented once (1 Tab)
        results = []
        for _ in range(self.iterations):
            current_salary = self.base_salary
            for year in range(5):
                raise_percent = random.uniform(0.02, 0.10)
                current_salary *= (1 + raise_percent)
            results.append(current_salary)
        return results