# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load the dataset
file_path = '../Movies.csv'
df = pd.read_csv(file_path)

# Set display options to ensure all columns are visible
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 25)
pd.set_option('display.max_columns', None)

# Way 1: Fill missing values with 'missing' using assign
df = df.assign(**{'Lead Studio': df['Lead Studio'].fillna('missing')})
print("\nData after filling missing values with 'missing':")
print(df.tail())

# Reload the dataset for Way 2 demonstration
df = pd.read_csv(file_path)

# Way 2: Manually update the missing value
df.at[75, 'Lead Studio'] = 'Disney'
print("\nData after manually updating the missing value:")
print(df.loc[75])

# Step 3: Display the first few rows of the dataframe
pd.set_option('display.max_columns', None)  # Ensure all columns are displayed
print("Original Data:")
print(df.head(75))

# Step 4: Identify missing values
print("\nMissing values before handling:")
print(df.isnull().sum())

# Step 5: Handling missing numeric values using average
# Assuming 'Audience score %' is the column with missing numeric values
average_score = df['Audience score %'].mean()
df['Audience score %'] = df['Audience score %'].fillna(average_score)

print("\nData after replacing missing numeric values with average:")
print(df.head(75))

# Step 6: Interpolation for missing numeric values
df['Audience score %'] = df['Audience score %'].interpolate()

print("\nData after interpolation:")
print(df.head())

# Examples of forward fill and backward fill
df_ffill = df.copy()
df_bfill = df.copy()

# Forward fill example
df_ffill['Audience score %'] = df_ffill['Audience score %'].ffill()
print("\nData after forward fill:")
print(df_ffill.head(75))

# Backward fill example
df_bfill['Audience score %'] = df_bfill['Audience score %'].bfill()
print("\nData after backward fill:")
print(df_bfill.head(75))

# Step 7: Save the cleaned dataframe to a new CSV file
output_path = '../Cleaned_Movies.csv'
df.to_csv(output_path, index=False)

# Step 8: Display the final state of the dataframe
print("\nFinal Data:")
print(df.head())

print("\nMissing values after handling:")
print(df.isnull().sum())
