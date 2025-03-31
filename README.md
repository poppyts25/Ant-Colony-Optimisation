# Ant-Colony-Optimisation
Implementation of the Ant Colony Optimisation (ACO) algorithm to solve the Bin Packing Problem (BPP).

The goal is to distribute a set of items into a fixed number of bins, aiming to minimize the difference between the heaviest and lightest bins (optimize fitness). The project performs multiple trials with varying parameters, visualizes the results using matplotlib, and saves the fitness data in tables and plots.

## **Features**
- **Ant Colony Optimization:**
    - Random pheromone initialization.
    - Ant path construction influenced by pheromone levels.
    - Pheromone update and evaporation processes.
- **Bin Packing Problem (BPP):**
    - **BPP1:** Uses linear weights (1 to N).
    - **BPP2:** Uses quadratic weights.
- **Visualization:**
    - Plots fitness results from multiple trials.
    - Saves fitness tables as images.
- **Multiple Trials Execution:**
    - Runs trials with different values for:
        - `p`: Number of paths.
        - `e`: Evaporation rate.
    - Displays the best fitness result for each trial.

## **Technologies Used**
- **Language:** Python 3.10.11
- **Libraries:**
    - `random` → For random pheromone initialization and path selection.
    - `matplotlib` → For visualizing fitness results and creating tables.

