# Flower Species

# Purpose:

By merging the sepal and petal information into a single DataFrame, this project aims to evaluate iris flower data. The application determines statistical summaries (mean, median, and standard deviation) for every species. Based on their physical characteristics, the aim is to identify the iris species that are most and least similar.

# Design & Implementation:

The project uses the pandas library for data handling and analysis.

# Data Processing Steps:

1. Load two CSV files (petal data and sepal data).
2. Merge them using a common 'sample_id'.
3. Clean duplicate species columns after merging.
4. Calculate:

   * Correlations between measurement variables
   * Mean for each variable grouped by species
   * Median for each variable grouped by species
   * Standard deviation for each variable grouped by species

# Columns Used:

* 'sample_id' – Unique identifier for each flower sample
* 'species' – Species name of the iris
* 'petal_length' – Length of the petal
* 'petal_width' – Width of the petal
* 'sepal_length' – Length of the sepal
* 'sepal_width' – Width of the sepal

# Methods Used:

* 'pd.read_csv()' – Load datasets
* 'pd.merge()' – Combine datasets
* '.drop()' – Remove unnecessary columns
* '.rename()' – Rename columns
* '.corr()' – Calculate correlation
* '.groupby()' – Group data by species
* '.mean()' – Calculate average
* '.median()' – Calculate median
* '.std()' – Calculate standard deviation

# Limitations

* Assumes that the 'sample_id' values in the two datasets match.
* Assumes that columns with numbers are formatted correctly.
* Does not deal with faulty or missing data.
