import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(filepath):
    """
    Load data from a CSV file and parse the 'date' column as datetime.

    Parameters:
        filepath (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: Dataframe containing the loaded data.
    """
    try:
        data = pd.read_csv(filepath, parse_dates=['date'])
        logging.info("Data loaded successfully from %s", filepath)
        return data
    except Exception as e:
        logging.error("Failed to load data from %s: %s", filepath, e)
        raise

def preprocess_data(data):
    """
    Perform initial preprocessing of the data, such as removing unnecessary columns.

    Parameters:
        data (pandas.DataFrame): The raw data.

    Returns:
        pandas.DataFrame: Dataframe with unnecessary columns removed.
    """
    try:
        if 'uni' in data.columns:
            data.drop('uni', axis=1, inplace=True)
            logging.info("Column 'uni' removed from data")
        return data
    except Exception as e:
        logging.error("Failed to preprocess data: %s", e)
        raise
