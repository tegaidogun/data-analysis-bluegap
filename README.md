# Data Analysis - BlueGAP

Welcome to the Data Analysis - BlueGAP project! This repository contains an in-depth analysis of water quality data, focusing on nitrogen concentration across various monitoring stations. The project involves data cleaning, analysis, visualization, and interactive exploration.

## Project Overview

The goal of this project is to analyze water quality data to understand trends and patterns in nitrogen concentrations. This analysis supports environmental assessments and regulatory compliance efforts by identifying trends, geographical patterns, and potential outliers in the data.

## Project Structure

- **data/**: Contains the raw and cleaned water quality data files.
  - `cleaned_water_quality.csv`: Cleaned data ready for analysis.
  - `original_water_quality.csv`: The dataset before any cleaning.
  - `water_quality.csv`: The raw original dataset.

- **notebooks/**: Jupyter notebooks with various analyses and visualizations.
  - 01_Data_Analysis.ipynb: Notebook analyzing the cleaned water quality data.
  - 02_Visualization.ipynb: Notebook creating static visualizations of the data.
  - 03_Interactive_Visualizations.ipynb: Notebook with interactive visualizations for dynamic data exploration.

- **reports/**: Contains the generated analysis report and figures.
  - analysis_report.md: Markdown version of the analysis report.
  - analysis_report.html: HTML version of the analysis report.
  - figures/: Directory with figures and interactive maps.
    - mean_nitrogen_by_year.png: Visualization of mean nitrogen concentration by year.
    - spatial_distribution_nitrogen.png: Spatial distribution of nitrogen concentration.
    - cleaned_data_map.html: Interactive map of cleaned data.
    - original_data_map.html: Interactive map of original data.

- **src/**: Source code for data processing and analysis.
  - analysis.py: Functions for calculating mean nitrogen concentrations and other metrics.
  - data_loader.py: Functions for loading and preprocessing data.
  - prepare_data.py: Functions for preparing and cleaning data.
  - visualization.py: Functions for generating visualizations.

- **main.py**: Entry point for running the main script.

## Analysis Report

For a detailed analysis of the data, please refer to the [Markdown version of the analysis report](reports/analysis_report.md) hosted in the `reports` directory. The report includes an overview of data cleaning, preprocessing, and insights gained from the analysis.

## Interactive Visualizations

Interactive visualizations are available through the [interactive visualizations notebook](https://mybinder.org/v2/gh/tegaidogun/data-analysis-bluegap/HEAD?labpath=notebooks). This notebook provides dynamic exploration tools to better understand the data distributions and patterns.

## Conclusion

The analysis highlighted significant variations in nitrogen concentration across different years and locations. Understanding these variations is crucial for targeted environmental protection and remediation efforts.

## Recommendations

- Continued monitoring and more focused studies on identified hotspots are recommended to assess the sources and impacts of nitrogen concentrations.
- Implementing advanced analytical techniques like time series forecasting could provide further insights into future trends.

### Note

To view the Jupyter notebooks locally, ensure you have [Jupyter Notebook](https://jupyter.org/install) installed on your system.

## License

This project is licensed under the GNU GPL v3 License. See the `LICENSE` file for details.