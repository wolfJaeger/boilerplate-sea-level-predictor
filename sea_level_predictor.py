import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sealevel_df = pd.read_csv('./epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(16, 10))
    axes.scatter(x=sealevel_df['Year'], y=sealevel_df['CSIRO Adjusted Sea Level'])
   
    # Create first line of best fit
    res = linregress(x=sealevel_df['Year'], y=sealevel_df['CSIRO Adjusted Sea Level'])
    sealevel_year_up_to_2050 = np.arange(1880, 2051)
    axes.plot(sealevel_year_up_to_2050, \
              res.intercept + res.slope*sealevel_year_up_to_2050,\
              color='y')
   
    # Create second line of best fit
    sealevel_starting_2000 = sealevel_df[(sealevel_df['Year'] >= 2000)]
    sealevel_starting_2000.head()

    regression_starting_year_2k = linregress(x=sealevel_starting_2000['Year'],\
                                             y=sealevel_starting_2000['CSIRO Adjusted Sea Level'])

    sealevel_year_from_2000_to_2050 = np.arange(2000, 2051)
    axes.plot(sealevel_year_from_2000_to_2050, \
              regression_starting_year_2k.intercept + regression_starting_year_2k.slope*sealevel_year_from_2000_to_2050,\
              color='r')
    # Add labels and title
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    axes.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
