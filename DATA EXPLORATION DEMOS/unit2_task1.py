import pandas as pd

# Load the dataset
df = pd.read_csv('../salaries.csv')  # Make sure to replace 'path_to_your_Salaries.csv' with the actual path to your CSV file

# Display the first few rows of the dataframe
print("Headers:\n", df.head())

# Display the data types of each column
print("\nData Types:\n", df.dtypes)

# Group by a relevant column (e.g., 'rank') and calculate the mean salary
group_by_rank = df.groupby('rank')['salary'].mean()
print("\nMean Salary by Rank:\n", group_by_rank)

# Apply a filter (e.g., salaries greater than 100000)
high_salaries = df[df['salary'] > 100000]
print("\nSalaries Greater Than 100000:\n", high_salaries)

# Slice the dataframe to get the first 10 rows and specific columns
sliced_data = df.loc[:9, ['rank', 'discipline', 'salary']]
print("\nSliced Data (First 10 Rows of 'rank', 'discipline', 'salary'):\n", sliced_data)

# Check for variations in salary
salary_variations = df['salary'].describe()
print("\nSalary Variations:\n", salary_variations)

# Check for variations in salary by rank
salary_variation_by_rank = df.groupby('rank')['salary'].describe()
print("\nSalary Variations by Rank:\n", salary_variation_by_rank)
