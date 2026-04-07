import json
from src.stat_engine import StatEngine
from src.monte_carlo import MonteCarloSim

# 1. Run the Simulation
sim = MonteCarloSim(base_salary=50000)
projected_salaries = sim.run_simulation()

# 2. Analyze the results
analyzer = StatEngine(projected_salaries)

# 3. Create a dictionary of the final report
report_data = {
    "average_final_salary": round(analyzer.get_mean(), 2),
    "median_final_salary": round(analyzer.get_median(), 2),
    "mode": analyzer.get_mode(),
    "starting_salary": 50000
}

# 4. Save to a file named 'simulation_results.json'
with open("simulation_results.json", "w") as f:
    json.dump(report_data, f, indent=4)

print("--- 5-YEAR SALARY PROJECTION RESULTS ---")
print(f"Average Final Salary: ${report_data['average_final_salary']}")
print(f"Median Final Salary:  ${report_data['median_final_salary']}")
print(f"Results saved to 'simulation_results.json'!")
# Create the 'data' folder and 'sample_salaries.json' if you haven't yet
# Then add this logic to main.py:
with open("data/sample_salaries.json", "r") as f:
    mock_data = json.load(f)

mock_analyzer = StatEngine(mock_data)
outliers = mock_analyzer.get_outliers(threshold=2)

print(f"Outliers found in mock data: {outliers}")