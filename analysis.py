# marimo
# email: 23f2004781@ds.study.iitm.ac.in
# This is an interactive Marimo notebook demonstrating variable dependencies

import marimo as mo

# --- Cell 1: Load data ---
# (In real use, you might load a CSV or dataset)
x_values = list(range(1, 101))
y_values = [x**0.5 for x in x_values]  # y depends on x
# Data flow: x_values -> y_values
mo.md("### Data Loaded: x vs sqrt(x)")

# --- Cell 2: Interactive widget ---
# Create a slider to choose how many data points to display
slider = mo.ui.slider(10, 100, step=10, value=50)
slider

# --- Cell 3: Dependent cell ---
# Show the subset of data based on slider value
subset_x = x_values[: slider.value]
subset_y = y_values[: slider.value]

# Documenting data flow:
# slider -> subset_x, subset_y
mo.md(f"### Showing first {slider.value} data points")

# --- Cell 4: Visualization ---
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(subset_x, subset_y, marker="o")
ax.set_title(f"x vs sqrt(x) (first {slider.value} points)")
ax.set_xlabel("x")
ax.set_ylabel("sqrt(x)")
fig
