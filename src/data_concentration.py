import pandas as pd

# Read the data from the CSV file
data = pd.read_csv('./data/water_quality.csv')

# Remove outliers using IQR method
Q1 = data['NO23'].quantile(0.25)
Q3 = data['NO23'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['NO23'] >= lower_bound) & (data['NO23'] <= upper_bound)]

# Calculate the mean nitrogen concentration by year
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
mean_by_year = data.groupby('year')['NO23'].mean()

# Plot the mean nitrogen concentration by year
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(mean_by_year.index, mean_by_year.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Mean Nitrogen Concentration (mg/L)')
plt.title('Mean Nitrogen Concentration by Year')
plt.grid(True)
plt.savefig('./figures/spatial_map.png', dpi=300)
plt.show()