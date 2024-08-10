# Imports for external use
from .data_loader import load_data, preprocess_data
from .utilities import remove_outliers
from .analysis import calculate_mean_concentration_by_year
from .visualization import plot_mean_concentration_by_year, plot_spatial_distribution

# Configuration settings (if any)
import logging

# Setup basic configuration for logging across the entire package
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Possible package-wide configurations or constants
DATA_PATH = './data/water_quality.csv'
OUTPUT_PATH = './figures'

# Init function to initialize any necessary settings or parameters
def init_package():
    """
    Initialize the package configuration and logging settings.
    This can include setting up logging levels, logging formats,
    or any other package-wide settings.
    """
    logging.info("Package src initialized, ready for data processing.")

# Optionally, execute some package-wide initialization upon import
init_package()
