import pandas as pd

# Set display options
pd.set_option('display.max_colwidth', 100)

# Read the data from the CSV file
data = pd.read_csv('./data/water_quality.csv')

# Display the first few rows of the data
# display(data.head())

# Check the data types and summary statistics
data.info()
data.describe()