import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Insert a slider
with ui.sidebar():
    ui.input_slider("n", "Number of columns", 1, 100, 20)
    # 1. output definition
    # 2. Slider title
    # 3. minimum
    # 4. maximum
    # 5. preset

# Insert a histogram
@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(10000)
    plt.hist(x, input.n(), density=True)
    #

# Insert a secondhistogram
@render.plot(alt="A histogram")
def another_histogram():
    np.random.seed(15245)
    x = 100 + np.random.randn(50000)
    plt.hist(x, input.n(), density=False)
