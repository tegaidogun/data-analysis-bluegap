import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Ensure src can be imported

from data_loader import load_data, preprocess_data
from utilities import remove_outliers
import pandas as pd

def prepare_data():
    """
    Prepares the water quality data by loading, preprocessing, and removing outliers.
    The function saves both the original and cleaned datasets for further analysis.

    Outputs:
    - 'original_water_quality.csv' containing the original data.
    - 'cleaned_water_quality.csv' containing the processed data.
    """
    # Define the path to the data
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'water_quality.csv')
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

    # Load data
    data = load_data(data_path)

    # Save a copy of the original uncleaned data for analysis
    data.to_csv(os.path.join(output_path, 'original_water_quality.csv'), index=False)

    # Process data
    data_processed = preprocess_data(data)
    data_processed = remove_outliers(data_processed, 'NO23')

    # Save the cleaned data
    data_processed.to_csv(os.path.join(output_path, 'cleaned_water_quality.csv'), index=False)

if __name__ == '__main__':
    prepare_data()
