import os
import webbrowser
from src.data_loader import load_data, preprocess_data
from src.utilities import remove_outliers
from src.analysis import calculate_mean_concentration_by_year
from src.visualization import plot_mean_concentration_by_year, plot_spatial_distribution
import pandas as pd

def main():
    # Define file paths
    data_path = './data/water_quality.csv'
    output_path = './reports/figures'
    
    # Load and preprocess data
    print("Loading and preprocessing data...")
    data = load_data(data_path)
    data = preprocess_data(data)
    data = remove_outliers(data, 'NO23')
    
    # Perform analysis
    print("Analyzing data...")
    mean_concentration = calculate_mean_concentration_by_year(data)
    
    # Generate visualizations
    print("Generating visualizations...")
    plot_mean_concentration_by_year(mean_concentration, output_path)
    plot_spatial_distribution(data, output_path)
    
    print("All processes completed successfully!")

    # Open the HTML report in the default web browser
    webbrowser.open('file://' + os.path.realpath('./reports/analysis_report.html'))

if __name__ == '__main__':
    main()
