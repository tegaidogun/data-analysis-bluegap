import matplotlib.pyplot as plt
import logging

# Ensure the logger is configured to handle messages appropriately
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_mean_concentration_by_year(mean_concentration, output_path=None):
    """
    Plot and optionally save the mean NO23 concentration by year.
    
    Parameters:
        mean_concentration (pandas.Series): Series containing the mean NO23 concentration by year.
        output_path (str, optional): Path to save the plot. If None, the plot will be displayed.
    """
    try:
        plt.figure(figsize=(10, 6))
        mean_concentration.plot(kind='bar', color='skyblue')
        plt.xlabel('Year')
        plt.ylabel('Mean NO23 Concentration (mg/L)')
        plt.title('Mean Nitrogen Concentration by Year')
        plt.grid(True)
        if output_path:  # Correctly check for None here
            plt.savefig(f'{output_path}/mean_nitrogen_by_year.png', dpi=300)
            plt.close()
            logging.info("Plot saved to %s/mean_nitrogen_by_year.png", output_path)
        else:
            plt.show()
    except Exception as e:
        logging.error("Failed to plot mean concentration by year: %s", e)
        raise

def plot_spatial_distribution(data, output_path=None):
    """
    Plot and optionally save the spatial distribution of nitrogen concentration.

    Parameters:
        data (pandas.DataFrame): Dataframe containing 'lon', 'lat', and 'NO23' columns.
        output_path (str, optional): Path to save the plot. If None, the plot will be displayed.
    """
    try:
        plt.figure(figsize=(10, 8))
        scatter = plt.scatter(data['lon'], data['lat'], c=data['NO23'], cmap='viridis', alpha=0.7, s=50)
        plt.colorbar(scatter, label='Nitrogen Concentration (mg/L)')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Spatial Distribution of Nitrogen Concentration')
        if output_path:
            plt.savefig(f'{output_path}/spatial_distribution_nitrogen.png', dpi=300)
            plt.close()
            logging.info("Spatial distribution plot saved to %s/spatial_distribution_nitrogen.png", output_path)
        else:
            plt.show()
    except Exception as e:
        logging.error("Failed to plot spatial distribution: %s", e)
        raise
