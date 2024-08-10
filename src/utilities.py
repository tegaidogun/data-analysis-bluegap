import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove_outliers(data, column):
    """
    Remove outliers based on the IQR method for a specific column.

    Parameters:
        data (pandas.DataFrame): The dataframe from which to remove outliers.
        column (str): The column name for which outliers need to be removed.

    Returns:
        pandas.DataFrame: Dataframe with outliers removed.
    """
    try:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        filtered_data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
        logging.info("Outliers removed from column '%s'", column)
        return filtered_data
    except KeyError:
        logging.error("Column %s not found in dataframe", column)
        raise
    except Exception as e:
        logging.error("Error removing outliers from column %s: %s", column, e)
        raise
