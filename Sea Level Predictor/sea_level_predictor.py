import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read the data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],
               alpha=0.6, label='Observed')

    # Create first line of best fit (all data, extended to 2050)
    all_fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(years_all, all_fit.intercept + all_fit.slope * years_all,
            'r', label='Fit: 1880-present')

    # Create second line of best fit (year 2000 onward, extended to 2050)
    recent = df[df['Year'] >= 2000]
    recent_fit = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, recent_fit.intercept + recent_fit.slope * years_recent,
            'green', label='Fit: 2000-present')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DONOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


if __name__ == '__main__':
    draw_plot()