.
# Statistical Engineering & Simulation Engine
## 📌 Project Overview
This project is a Python-based statistical engine designed to perform data analysis and Monte Carlo simulations. It demonstrates core mathematical principles like Bessel's Correction and the Law of Large Numbers (LLN) using startup server failure data and employee salary sets.
## 📂 Engineering Standards
Following professional software development practices, the project is organized into a modular directory structure:
 * src/: Contains core logic (stat_engine.py) and the simulation model (monte_carlo.py).
 * tests/: Contains test_stat_engine.py, a comprehensive unit testing suite.
 * data/: Stores the sample_salaries.json dataset used for analysis.
## 🧮 Mathematical Implementation
### 1. Central Tendency & Median Logic
The engine calculates Mean, Mode, and Median from scratch. The get_median() function specifically handles the Even/Odd Constraint:
 * For odd-sized sets, it returns the middle value.
 * For even-sized sets (like the 50-item salary list), it calculates the average of the two central values.
### 2. Dispersion & Bessel’s Correction
To ensure an unbiased estimate of variance when working with a sample of data, the engine applies Bessel's Correction (n-1). This adjustment is critical for accurate standard deviation mapping.
### 3. Outlier Detection
The engine identifies "extreme" values using a threshold of 2 standard deviations from the mean.
 * Business Insight: In the salary dataset, this identifies high-earning executives. This proves why the "Mean" can be a misleading metric for a startup budget, as outliers skew the average higher than what a typical employee earns.
## 🎲 Monte Carlo Simulation
The simulation models a server with a 4.5% daily crash probability.
 * 30-Day Trial: Demonstrates high volatility where "luck" can skew perceived reliability.
 * 10,000-Day Trial: Demonstrates the Law of Large Numbers. As the number of trials increases, the simulated frequency converges toward the theoretical 4.5% probability.
## 🚦 Testing & Validation
The project includes 5 automated unit tests to verify:
 1. Median (Odd) calculation.
 2. Median (Even) calculation.
 3. Graceful Failure: Correctly raising a ValueError for empty datasets.
 4. Standard Deviation Mapping: Verifying math against known outcomes.
 5. Outlier Detection: Confirming the engine flags extreme values.
To run tests:
python -m unittest discover -s tests