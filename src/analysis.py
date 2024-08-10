import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_mean_concentration_by_year(data):
    """
    Calculate the mean NO23 concentration per year.

    Parameters:
        data (pandas.DataFrame): Dataframe containing 'date' and 'NO23' columns.

    Returns:
        pandas.Series: Mean NO23 concentration by year.
    """
    try:
        # Check if 'date' column is datetime type, if not, convert it
        if not pd.api.types.is_datetime64_any_dtype(data['date']):
            data['date'] = pd.to_datetime(data['date'])
        data['year'] = data['date'].dt.year
        mean_concentration = data.groupby('year')['NO23'].mean()
        logging.info("Mean concentration calculated by year")
        return mean_concentration
    except KeyError:
        logging.error("Necessary columns are missing from the dataframe")
        raise
    except Exception as e:
        logging.error("Error calculating mean concentration by year: %s", e)
        raise
