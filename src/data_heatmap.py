import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Read data
df = pd.read_csv('./data/water_quality.csv')

# Clip outliers for NO23 values
upper_bound = df['NO23'].quantile(0.95)
lower_bound = df['NO23'].quantile(0.05)
df['NO23_clipped'] = np.clip(df['NO23'], lower_bound, upper_bound)

# Apply logarithmic scale
df['NO23_log'] = np.log(df['NO23_clipped'] + 1e-9)  # adding small constant to avoid log(0)

# Convert DataFrame to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, 1)

# Create divider for the main axis position
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

# Plot the heatmap
gdf.plot(column='NO23_log', ax=ax, legend=True, cax=cax, cmap='coolwarm')

# Set the plot title
ax.set_title("NO23 Heatmap (Log Scale)", fontsize=20)

# Save the plot
plt.savefig('./figures/heatmap.png')

# Show the plot
plt.show()
