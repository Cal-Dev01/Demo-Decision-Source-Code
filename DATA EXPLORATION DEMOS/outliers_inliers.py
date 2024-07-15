import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate synthetic data
np.random.seed(42)
uk_births = np.random.normal(loc=1000, scale=200, size=50)  # 50 data points representing births in the UK
non_uk_births = np.random.normal(loc=100, scale=50, size=10)  # 10 data points representing births outside the UK

# Combine into a single dataset
data_uk = pd.DataFrame({'Location': ['UK']*50, 'Births': uk_births})
data_non_uk = pd.DataFrame({'Location': ['Non-UK']*10, 'Births': non_uk_births})
df = pd.concat([data_uk, data_non_uk], ignore_index=True)

# Plotting
plt.figure(figsize=(10, 6))

# Identify inliers (UK births) and outliers (Non-UK births) for plotting
plt.scatter(data_uk.index, data_uk['Births'], color='blue', label='UK Births', marker='x')
plt.scatter(data_non_uk.index + 50, data_non_uk['Births'], color='red', label='Non-UK Births', marker='o')

# Adding labels and legend
plt.xlabel('Index')
plt.ylabel('Number of Births')
plt.title('Scatter Plot of UK and Non-UK Births by British Parents')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
