import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Felix', 'Ruth'],
    'Age': [25, 30, 35, 25, 16, 40],
    'Salary': [70000, 80000, 120000, 80000, 30000, np.nan]  # Include a NaN value for demonstration
}
df = pd.DataFrame(data)

# 1. head(n), tail(n): first/last n rows
# head() shows the first n rows (default is 5)
print("First 2 rows:\n", df.head(2), "\n")
# tail() shows the last n rows (default is 5)
print("Last 2 rows:\n", df.tail(2), "\n")
#
# # 2. describe(): generate descriptive statistics (for numeric columns only)
# # describe() provides summary statistics for numerical columns
# print("Descriptive Statistics:\n", df.describe(), "\n")
#
# 3. max(), min(): return max/min values for all numeric columns
# max() returns the maximum value for each numeric column
# print("Max values:\n", df.max(numeric_only=True), "\n")
# # min() returns the minimum value for each numeric column
# print("Min values:\n", df.min(numeric_only=True), "\n")

# 4. mean(), median(): return mean/median values for all numeric columns
# mean() calculates the mean for each numeric column
# print("Mean values:\n", df.mean(numeric_only=True), "\n")
# # median() calculates the median for each numeric column
# print("Median values:\n", df.median(numeric_only=True), "\n")
#
# # 5. std(): standard deviation
# # std() calculates the standard deviation for each numeric column
# print("Standard Deviation:\n", df.std(numeric_only=True), "\n")
#
# # 6. var(): variance
# # var() calculates the variance for each numeric column
# print("Variance:\n", df.var(numeric_only=True), "\n")
#
# # 7. mode(): mode
# # mode() calculates the mode for each numeric column
# print("Mode values:\n", df.mode(numeric_only=True), "\n")
#
# # 8. sem(): standard error of mean
# # sem() calculates the standard error of the mean for each numeric column
# print("Standard Error of Mean:\n", df.sem(numeric_only=True), "\n")
#
# # 9. skew(): skewness
# # skew() calculates the skewness for each numeric column
# print("Skewness:\n", df.skew(numeric_only=True), "\n")
#
# # 10. kurt(): kurtosis
# # kurt() calculates the kurtosis for each numeric column
# print("Kurtosis:\n", df.kurt(numeric_only=True), "\n")
#
# # 11. sample(n): returns a random sample of the DataFrame
# # sample() returns a random sample of n rows
# print("Random Sample of 2 rows:\n", df.sample(2), "\n")
#
# 12. dropna(): drop all records with missing values
# dropna() removes rows with any NaN values
print("DataFrame with NaNs dropped:\n", df.dropna(), "\n")
#
# # Slicing: Select specific rows and columns
# print("Slicing: First 3 rows, 'Name' and 'Salary' columns:\n", df.loc[:2, ['Name', 'Salary']], "\n")
#
# Groupby: Group by 'Age' and calculate the mean salary
grouped_by_age = df.groupby('Age')['Salary'].mean()
print("Grouped by Age (Mean Salary):\n", grouped_by_age, "\n")
#
# # Filter: Select rows where 'Salary' is greater than 75000
# filtered_df = df[df['Salary'] > 75000]
# print("Filtered DataFrame (Salary > 75000):\n", filtered_df, "\n")
