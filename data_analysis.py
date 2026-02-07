import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np  



df = pd.read_csv('data.csv')

print("First 5 rows of the dataset:")
print(df.head())


print("\nSummary statistics of the dataset:")
print(df.describe())

selected_column = 'sepal_length'
average_value = df[selected_column].mean()
print(f"\nAverage of '{selected_column}': {average_value:.2f}")

grouped_means = df.groupby('species').mean()
print("\nAverage values per species:")
print(grouped_means)


plt.figure(figsize=(12, 8))


plt.subplot(2, 2, 1)  
species_counts = df['species'].value_counts()
species_counts.plot(kind='bar', color='skyblue')
plt.title('Bar Chart: Count of Each Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)  
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for species, color in colors.items():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['petal_length'], color=color, label=species, alpha=0.7)
plt.title('Scatter Plot: Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend()


plt.subplot(2, 2, 3) 

numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar() 
plt.title('Heatmap: Correlation Matrix')

plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)


plt.tight_layout()
plt.show()