# Task 1: Load & Explore Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (replace 'iris.csv' with your file)
df = pd.read_csv("iris.csv")

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Check structure
print("\nDataset Info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# Clean data (drop missing values for simplicity)
df = df.dropna()

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Example grouping: average petal length by species
grouped = df.groupby("species")["petal_length"].mean()
print("\nAverage petal length per species:")
print(grouped)

# Task 3: Data Visualization

# 1. Line chart (not time-series in iris, so we'll use index vs sepal length as a simple trend)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.title("Line Chart - Sepal Length over Index")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6,4))
grouped.plot(kind="bar", color="skyblue")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.title("Bar Chart - Avg Petal Length per Species")
plt.show()

# 3. Histogram (distribution of sepal length)
plt.figure(figsize=(6,4))
plt.hist(df["sepal_length"], bins=15, color="orange", edgecolor="black")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram - Sepal Length Distribution")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")
plt.title("Scatter Plot - Sepal vs Petal Length")
plt.show()
