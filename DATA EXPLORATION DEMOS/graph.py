import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [70000, 80000, 120000, np.nan]  # Include a NaN value for demonstration
}
df = pd.DataFrame(data)

# Plotting the histogram for Age
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=5, edgecolor='black', alpha=0.7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plotting the histogram for Salary
plt.figure(figsize=(8, 5))
plt.hist(df['Salary'].dropna(), bins=5, edgecolor='black', alpha=0.7)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
