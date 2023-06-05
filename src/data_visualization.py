import pandas as pd
import matplotlib.pyplot as plt

# Enable antialiasing
plt.rcParams['lines.antialiased'] = True

# Read the data from the CSV file
data = pd.read_csv('./data/water_quality.csv')

# Convert the 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Remove outliers using IQR method
Q1 = data['NO23'].quantile(0.25)
Q3 = data['NO23'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['NO23'] >= lower_bound) & (data['NO23'] <= upper_bound)]

# Spatial Map (using latitude and longitude)
plt.figure(figsize=(10, 8))
plt.scatter(data['lon'], data['lat'], c=data['NO23'], cmap='viridis', alpha=0.7, s=50)
plt.colorbar(label='Nitrogen Concentration (mg/L)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Spatial Distribution of Nitrogen Concentration')
plt.savefig('./figures/spatial_map.png', dpi=300)
plt.show()