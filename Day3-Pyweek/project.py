#Hands on python
#Numpy and pandas
#csv file
import numpy as np

# 1. Creating basic arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([[10, 20, 30],
              [40, 50, 60]])

# 2. Checking shapes and sizes
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)

# 3. Basic indexing and slicing
print("First element of a:", a[0])
print("First row of b:", b[0])
print("Slice of a (1:4):", a[1:4])

# 4. Creating special arrays
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
rand = np.random.random((2, 2))

# 5. Mathematical operations
print("a + 5:", a + 5)
print("a * 2:", a * 2)
print("Element-wise addition:", a[:3] + np.array([10, 20, 30]))

# 6. Matrix operations
mat1 = np.array([[1, 2],
                 [3, 4]])
mat2 = np.array([[5, 6],
                 [7, 8]])

print("Matrix multiplication:")
print(mat1.dot(mat2))

# 7. Useful statistics
print("Mean of a:", np.mean(a))
print("Sum of b:", np.sum(b))
print("Max of b:", np.max(b))
print("Standard deviation of a:", np.std(a))


import pandas as pd

# 1. Creating a Series
s = pd.Series([10, 20, 30, 40], name="Scores")
print("Series:")
print(s)

# 2. Creating a DataFrame
data = {
    "Name": ["Ali", "Sara", "John", "Riya", "Rohan"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [88, 92, 75, 95, 85],
    "City": ["Hyd", "Delhi", "Hyd", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# 3. Basic info
print("\nHead:")
print(df.head())

print("\nDescribe:")
print(df.describe())

# 4. Selecting columns
print("\nNames column:")
print(df["Name"])

# 5. Filtering rows
print("\nStudents with marks > 85:")
print(df[df["Marks"] > 85])

# 6. Adding a new column
df["Pass"] = df["Marks"] > 80

# 7. Sorting values
df_sorted = df.sort_values(by="Marks", ascending=False)

print("\nSorted by marks:")
print(df_sorted)

# 8. Group by City
city_group = df.groupby("City")["Marks"].mean()

print("\nAverage marks by city:")
print(city_group)

# 9. Saving to CSV (optional)
df.to_csv("students.csv", index=False)
