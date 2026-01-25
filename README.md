# Experiment Tracker Lite

A lightweight Python library for tracking machine learning experiments with automatic logging, comparison, and visualization capabilities.

## Features

- **Automatic Experiment Tracking**: Each run creates timestamped directories with organized subdirectories for plots and checkpoints
- **Metric Logging**: Log and save training metrics (loss, accuracy, etc.) as JSON files
- **Experiment Comparison**: Compare multiple runs and identify best-performing experiments
- **Visualization**: Generate and save matplotlib plots for experiment analysis

## Project Structure

```
experiment-tracker-lite/
├── src/
│   ├── experiment.py    # Core Experiment class for tracking runs
│   ├── comparison.py    # Tools to compare and find best experiments
│   └── visualize.py     # Visualization utilities
├── experiments/         # Auto-generated experiment runs with metrics
└── main.py             # Entry point
```

## Usage

```python
from src.experiment import Experiment

# Initialize experiment
exp = Experiment(config={"lr": 0.01}, tags=["test"])

# Log metrics
exp.log_metric("loss", 0.5)
exp.log_metric("accuracy", 0.8)
exp.save_metrics()
```
