<!DOCTYPE html>
<html>
<body>

<h1>Visualizing Water Quality Data - BlueGap</h1>

<p>This project focuses on the visualization of water quality data, specifically NO23 levels, using various Python libraries such as pandas, geopandas, and matplotlib. The scripts provided in this project take CSV data and output various visualizations to the figures directory.</p>

<h2>Application & Requirements</h2>

<p>This project requires the following Python libraries:</p>

<ul><li>Pandas</li>
    <li>Geopandas</li>
    <li>Matplotlib</li>
    <li>Numpy</li></ul>

<p>You can install the required libraries using pip:</p>

<pre><code>pip install pandas geopandas matplotlib numpy</code></pre>

<h2>Scripts and their Functions</h2>

<h3>src/data_analysis.py</h3>
<p>This script performs an initial analysis on the water quality data. It calculates basic statistics such as mean, median, and standard deviation for the NO23 levels.</p>

<h3>src/data_interactive.py</h3>
<p>This script creates an interactive plot of the data. The output is a HTML file which displays an interactive map, allowing you to zoom and hover over data points for additional information.</p>

<h3>src/data_visualization.py</h3>
<p>This script creates a static visualization of the data. It generates a scatter plot of the NO23 levels, with color indicating the level of NO23.</p>

<h3>src/data_heatmap.py</h3>
<p>This script creates a heatmap of the NO23 levels. The heatmap provides a geographical visualization of NO23 concentrations, with color indicating the level of NO23. Outliers are handled and logarithmic scaling is applied to better visualize the data spread.</p>

<h2>Output</h2>

<p>All scripts output their respective figures to the <code>figures</code> directory. The figures are saved in PNG format for static visualizations and HTML format for interactive plots.</p>

</body>
</html>
