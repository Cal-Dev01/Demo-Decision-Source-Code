import pandas as pd

# Create a sample dictionary with data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Felix'],
    'Age': [25, 30, 35, 50],
    'Salary': [70000, 80000, 120000, 56000],
}

# Create a DataFrame from the dictionary
# This DataFrame contains columns 'Name', 'Age', and 'Salary' with 3 rows of data
df = pd.DataFrame(data)

# # 1. dtypes: list the types of the columns
# # This attribute provides the data types of each column in the DataFrame.
# print("Data Types:\n", df.dtypes, "\n")

# # 2. columns: list the column names
# # This attribute lists the column names of the DataFrame.
# print("Column Names:\n", df.columns, "\n")

# # 3. axes: list the row labels and column names
# # This attribute returns a list of the row labels and column names.
# print("Axes:\n", df.axes, "\n")
#
# # 4. ndim: number of dimensions
# # This attribute returns the number of dimensions of the DataFrame.
# print("Number of Dimensions:\n", df.ndim, "\n")
#
# # 5. size: number of elements
# # This attribute returns the number of elements in the DataFrame.
# print("Size (Number of Elements):\n", df.size, "\n")
#
# # 6. shape: return a tuple representing the dimensionality
# # This attribute returns a tuple representing the dimensionality of the DataFrame (rows, columns).
# print("Shape (Dimensions):\n", df.shape, "\n")
#
# 7. values: numpy representation of the data
# This attribute returns the underlying numpy representation of the data.
print("Numpy Representation of Data:\n", df.values, "\n")
