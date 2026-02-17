# Import necessary libraries for data manipulation and file operations
import pandas as pd
import os

# Get the directory of the current script (not currently used)
os.path.join(os.path.dirname(__file__))

# Alternative: change working directory to the Python folder (currently disabled)
os.chdir('/Users/vaishnav/Library/Mobile Documents/com~apple~CloudDocs/Python/')

# Load petal and sepal measurement datasets from CSV files
petal_data = pd.read_csv('Petal_Data.csv')
sepal_data = pd.read_csv('Sepal_Data.csv')

# Merge the two datasets on the 'sample_id' column to combine petal and sepal measurements
final_data = pd.merge(petal_data, sepal_data, on = 'sample_id')

# Extract individual measurement columns from the merged dataset for correlation analysis
petal_length = final_data['petal_length']
petal_width = final_data['petal_width']
sepal_length = final_data['sepal_length']
sepal_width = final_data['sepal_width']

# Calculate and print pairwise correlations between all flower measurements
# Correlation values range from -1 to 1, showing the strength of linear relationships
print(petal_length.corr(petal_width))
print(petal_length.corr(sepal_length))
print(petal_length.corr(sepal_width))
print(petal_width.corr(sepal_length))
print(petal_width.corr(sepal_width))
print(sepal_length.corr(sepal_width))

# Handle duplicate 'species' column from the merge
# Pandas appended '_x' and '_y' suffixes to distinguish the duplicate columns
# Remove the duplicate and rename for clarity
final_data = final_data.drop(columns = ['species_y'])
final_data = final_data.rename(columns = {'species_x': 'species'})

# Calculate mean values for each flower measurement grouped by species
mean_values = final_data.groupby('species')[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].mean()
print(mean_values)

# Calculate median values for each flower measurement grouped by species
mediam_values = final_data.groupby('species')[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].median()
print(mediam_values)

# Calculate standard deviation for each flower measurement grouped by species
std_values = final_data.groupby('species')[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].std()
print(std_values)

# Analysis Summary:
# - Versicolor and Virginica are most similar (similar mean petal lengths/widths)
# - Large overlap in standard deviations between Versicolor and Virginica
# - Setosa is least similar to the other two species (significantly lower petal measurements)
