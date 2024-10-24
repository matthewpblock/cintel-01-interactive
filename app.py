import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
from palmerpenguins import load_penguins

# Page title
ui.page_opts(title="Matt's PyShiny App with Plot", fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    # Add a slider that specifies the number of bins in the histogram
    # ui.input_slider function is called with 5 arguments:
    # 1. a string id ("selected_number_of_bins") uniquely identifying the input
    # 2. a string label ("Number of Bins") displayed along the slider
    # 3. minimum number of bins
    # 4. maximum number of bins
    # 5. initial preset value of slider  
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(808)
    random_array = 100 + 15 * np.random.randn(437)
    # Create a histogram of the random data. Arguments:
    # 1. the data array
    # 2. number of bins dynamically set by the slider input
    # 3. density parameter: True=percentages, False=raw numbers
    plt.hist(random_array, input.selected_number_of_bins(), density=True)

# I tried to create a second histogram using data from the palmerpenguins data but couldn't quite figuring it out, showing me I don't quite understand what's going on in the histogram creation exercise yet
# @render.plot(alt="A histogram")
# def histogram():
#    penguins = load_penguins()
#    penguins = penguins[penguins["species"] == input.species()]
    # Create a histogram of the random data. Arguments:
    # 1. the data array
    # 2. number of bins dynamically set by the slider input
    # 3. density parameter: True=percentages, False=raw numbers
#    plt.hist(penguins, input.species(), density=False)
# End of experimental code
    
# I really like labeling the arguments so that it's easy to tell what each one is later!
