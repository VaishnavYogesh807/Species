import pandas as pd

petal_data = pd.read_csv('/Users/vaishnav/Library/Mobile Documents/com~apple~CloudDocs/Python/Petal_Data.csv')
sepal_data = pd.read_csv('/Users/vaishnav/Library/Mobile Documents/com~apple~CloudDocs/Python/Sepal_Data.csv')

final_data = pd.merge(petal_data, sepal_data, on = 'sample_id')

petal_length = final_data['petal_length']
petal_width = final_data['petal_width']
sepal_length = final_data['sepal_length']
sepal_width = final_data['sepal_width']

print(petal_length.corr(petal_width))
print(petal_length.corr(sepal_length))
print(petal_length.corr(sepal_width))
print(petal_width.corr(sepal_length))
print(petal_width.corr(sepal_width))
print(sepal_length.corr(sepal_width))

# When merging the two datasets, we have two columns with the same name 'species'. 
# To avoid confusion, pandas automatically adds suffixes to the column names. 
# In this case, it added '_x' to the 'species' column from the petal_data and '_y' to the 'species' column from the sepal_data. 
# Since both columns contain the same information, we can drop one of them and rename the other for clarity.
final_data = final_data.drop(columns = ['species_y'])
final_data = final_data.rename(columns = {'species_x': 'species'})

mean_values = final_data.groupby('species')[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].mean()
print(mean_values)

mediam_values = final_data.groupby('species')[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].median()
print(mediam_values)

std_values = final_data.groupby('species')[['petal_length', 'petal_width', 'sepal_length', 'sepal_width']].std()
print(std_values)

#Versicolor and Virginica are most similar because they have similar mean petal lengths and widths. 
# They also have a large overlap in standard deviations. 
# The mean and correlation statistics indicate that Setosa is least similar to the other two species due to its significantly lower petal measures.