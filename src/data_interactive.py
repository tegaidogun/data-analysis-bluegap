import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

# Read the data from the CSV file
data = pd.read_csv('./data/water_quality.csv')

# Remove outliers using IQR method
Q1 = data['NO23'].quantile(0.25)
Q3 = data['NO23'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
data = data[(data['NO23'] >= lower_bound) & (data['NO23'] <= upper_bound)]

# Perform min-max normalization on 'NO23' column
scaler = MinMaxScaler(feature_range=(0, 1))
data['NO23_normalized'] = scaler.fit_transform(data[['NO23']])

# Create an interactive map with normalized data
fig = px.scatter_mapbox(data, lat='lat', lon='lon', color='NO23_normalized',
                        hover_data=['station', 'date', 'NO23_normalized'],
                        color_continuous_scale='RdBu',
                        range_color=(0, 1),
                        mapbox_style='open-street-map', zoom=10)

fig.update_layout(title='Spatial Distribution of Normalized Nitrogen Concentration',
                  mapbox=dict(center=dict(lat=data['lat'].mean(),
                                          lon=data['lon'].mean())))

fig.show()