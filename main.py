import json
from src.stat_engine import StatEngine
from src.monte_carlo import MonteCarloSim

# --- PART 1: Salary Analysis & Projections ---
sim = MonteCarloSim(base_salary=50000)
projected_salaries = sim.run_salary_sim() # This creates the list

analyzer = StatEngine(projected_salaries)
print("--- 5-YEAR SALARY PROJECTION RESULTS ---")
print(f"Average Final Salary: ${analyzer.get_mean():,.2f}")
print(f"Median Final Salary: ${analyzer.get_median():,.2f}")

# --- PART 2: Outliers (From your existing data) ---
with open("data/sample_salaries.json", "r") as f:
    mock_data = json.load(f)
mock_analyzer = StatEngine(mock_data)
outliers = mock_analyzer.get_outliers()
print(f"Outliers found in mock data: {outliers}")

# --- PART 3: Server Reliability Simulation ---
print("\n--- SERVER RELIABILITY SIMULATION (4.5% Crash Prob) ---")

sim_30 = MonteCarloSim(probability=0.045, trials=30)
print(f"30-Day Trial Crash Rate: {sim_30.run_simulation():.2%}")

sim_10000 = MonteCarloSim(probability=0.045, trials=10000)
print(f"10,000-Day Trial Crash Rate: {sim_10000.run_simulation():.2%}")
