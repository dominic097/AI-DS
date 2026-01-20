Unit I

1.  \(i\) Discuss how lists differ from other data structures like
    tuples and sets. Given a list- numbers = \[2, 4, 6, 8, 10\]. How to
    create a list and access its elements. How to modify, add, and
    remove elements from a list with examples, and sort the list in
    descending order. (10M)

### Answer (i)

**Differences between Lists, Tuples, and Sets:**

1. **Lists**: Mutable, ordered, allow duplicates, indexed by position
2. **Tuples**: Immutable, ordered, allow duplicates, indexed by position
3. **Sets**: Mutable, unordered, no duplicates, not indexed

```python
# Creating and working with the given list
numbers = [2, 4, 6, 8, 10]  # Creating a list with square brackets

# Accessing elements by index (0-based indexing)
print(f"First element: {numbers[0]}")      # Access first element (index 0)
print(f"Last element: {numbers[-1]}")      # Access last element using negative indexing
print(f"Second to fourth: {numbers[1:4]}") # Slice from index 1 to 3 (4 is exclusive)

# Modifying elements
numbers[0] = 1          # Change first element from 2 to 1
print(f"Modified list: {numbers}")  # Print the modified list

# Adding elements
numbers.append(12)      # Add element at the end of the list
numbers.insert(2, 5)    # Insert element 5 at index 2
print(f"After adding: {numbers}")   # Display list after additions

# Removing elements
numbers.remove(5)       # Remove first occurrence of value 5
popped = numbers.pop()  # Remove and return last element
del numbers[1]          # Delete element at index 1
print(f"After removal: {numbers}")  # Display list after removals

# Sorting in descending order
numbers.sort(reverse=True)  # Sort the list in descending order in-place
print(f"Sorted descending: {numbers}")  # Display sorted list

# Alternative sorting method (creates new list)
original = [2, 4, 6, 8, 10]  # Reset to original
sorted_desc = sorted(original, reverse=True)  # Create new sorted list
print(f"Original unchanged: {original}")      # Original list remains unchanged
print(f"New sorted list: {sorted_desc}")      # New sorted list

# Comparison with other data structures
# Tuple example (immutable)
tuple_example = (2, 4, 6, 8, 10)  # Create tuple with parentheses
print(f"Tuple: {tuple_example}")
# tuple_example[0] = 1  # This would cause an error - tuples are immutable

# Set example (no duplicates, unordered)
set_example = {2, 4, 6, 8, 10, 2}  # Create set with curly braces
print(f"Set (duplicates removed): {set_example}")  # Duplicate 2 is automatically removed
# print(set_example[0])  # This would cause an error - sets are not indexed
```

> \(ii\) Explain the concept of a NumPy Array and its applications in
> data analysis. Include the following in your answer: (10M)
>
> a\. What is a NumPy Series? How is it different from a Python list?
>
> b\. How do you create a NumPy Series? Provide an example with code.
>
> c\. Explain how mathematical operations can be performed on a NumPy
> Series.
>
> d\. Discuss the advantages of using NumPy Series for handling large
> datasets.

### Answer (ii)


## NumPy Array and Its Applications in Data Analysis

A **NumPy array** is the core data structure of the NumPy library. It is a fast, memory-efficient, multi-dimensional container for numerical data. Unlike Python lists, NumPy arrays:  
- Store data in a **homogeneous and contiguous memory block**, making access faster.  
- Support **vectorized operations**, so mathematical functions can be applied to entire arrays at once without explicit loops.  
- Can represent **1-D (vectors), 2-D (matrices), and higher-dimensional tensors**.  

---

### Applications in Data Analysis
1. **Efficient storage of large datasets** – Handles millions of elements compactly.  
2. **Mathematical & Statistical analysis** – Provides built-in functions like `mean`, `std`, `corrcoef`, etc.  
3. **Data cleaning and filtering** – Easy to replace missing values, slice, and filter subsets of data.  
4. **Matrix and linear algebra operations** – Supports multiplication, eigenvalues, and decomposition.  
5. **Foundation for other libraries** – Base for Pandas, Scikit-learn, TensorFlow, and PyTorch.  

---

**Summary:**  
A NumPy array is a high-performance, multi-dimensional structure for numerical data. Its ability to handle large datasets, perform fast vectorized operations, and support advanced computations makes it indispensable in data analysis.



**NumPy Arrays and Data Analysis Applications:**

```python
import numpy as np  # Import NumPy library for numerical operations
import pandas as pd  # Import Pandas for data manipulation

# a. NumPy Series (Note: NumPy has arrays, Pandas has Series)
# Creating a Pandas Series for comparison
series_example = pd.Series([1, 2, 3, 4, 5])  # Create a Pandas Series
list_example = [1, 2, 3, 4, 5]               # Create a Python list
numpy_array = np.array([1, 2, 3, 4, 5])      # Create a NumPy array

print("Pandas Series:")
print(series_example)      # Series has index labels and data type info
print("\nPython List:")
print(list_example)        # Simple list without additional information
print("\nNumPy Array:")
print(numpy_array)         # Array with data type information

# Key differences:
# 1. Series has labeled index, lists use positional indexing
# 2. Series has homogeneous data types, lists can have mixed types
# 3. Series supports vectorized operations, lists require loops

# b. Creating NumPy Arrays (and Pandas Series)
# Different ways to create NumPy arrays
array1 = np.array([1, 2, 3, 4, 5])           # From list
array2 = np.arange(1, 6)                     # Using arange function
array3 = np.linspace(1, 5, 5)                # Using linspace (5 points from 1 to 5)
array4 = np.zeros(5)                         # Array of zeros
array5 = np.ones(5)                          # Array of ones
array6 = np.random.random(5)                 # Random values between 0 and 1

print(f"From list: {array1}")
print(f"Using arange: {array2}")
print(f"Using linspace: {array3}")
print(f"Zeros array: {array4}")
print(f"Ones array: {array5}")
print(f"Random array: {array6}")

# Creating Pandas Series
series1 = pd.Series([10, 20, 30, 40, 50])                    # Simple series
series2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])     # With custom index
series3 = pd.Series({'A': 100, 'B': 200, 'C': 300})         # From dictionary

print(f"\nSimple series:\n{series1}")
print(f"\nCustom index series:\n{series2}")
print(f"\nFrom dictionary:\n{series3}")

# c. Mathematical operations on NumPy arrays and Pandas Series
# NumPy array operations
arr = np.array([1, 2, 3, 4, 5])

# Element-wise operations (vectorized)
print(f"Original array: {arr}")
print(f"Add 10: {arr + 10}")              # Add 10 to each element
print(f"Multiply by 2: {arr * 2}")        # Multiply each element by 2
print(f"Square: {arr ** 2}")              # Square each element
print(f"Square root: {np.sqrt(arr)}")     # Square root of each element

# Statistical operations
print(f"Sum: {np.sum(arr)}")              # Sum of all elements
print(f"Mean: {np.mean(arr)}")            # Average of elements
print(f"Standard deviation: {np.std(arr)}") # Standard deviation
print(f"Maximum: {np.max(arr)}")          # Maximum value
print(f"Minimum: {np.min(arr)}")          # Minimum value

# Operations between arrays
arr2 = np.array([2, 4, 6, 8, 10])
print(f"Array addition: {arr + arr2}")    # Element-wise addition
print(f"Array multiplication: {arr * arr2}") # Element-wise multiplication
print(f"Dot product: {np.dot(arr, arr2)}") # Dot product

# Pandas Series operations
series = pd.Series([1, 2, 3, 4, 5])
print(f"\nSeries operations:")
print(f"Series + 10:\n{series + 10}")     # Add 10 to each element
print(f"Series mean: {series.mean()}")    # Calculate mean
print(f"Series sum: {series.sum()}")      # Calculate sum

# d. Advantages for large datasets
# Demonstrating performance and memory efficiency
large_list = list(range(1000000))         # Create large Python list
large_array = np.array(range(1000000))    # Create large NumPy array

print(f"\nMemory usage comparison:")
print(f"List size: {large_list.__sizeof__()} bytes")      # Memory used by list
print(f"Array size: {large_array.nbytes} bytes")          # Memory used by array

# Time comparison example (conceptual)
import time

# List operation (requires explicit loop)
start_time = time.time()
list_result = [x * 2 for x in large_list[:10000]]  # List comprehension
list_time = time.time() - start_time

# Array operation (vectorized)
start_time = time.time()
array_result = large_array[:10000] * 2              # Vectorized operation
array_time = time.time() - start_time

print(f"List operation time: {list_time:.6f} seconds")
print(f"Array operation time: {array_time:.6f} seconds")
print(f"Speed improvement: {list_time/array_time:.2f}x faster")

# Additional advantages demonstration
# 1. Broadcasting - operations with different sized arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
arr_1d = np.array([10, 20, 30])            # 1D array
broadcasted = arr_2d + arr_1d               # Automatically broadcasts
print(f"\n2D array:\n{arr_2d}")
print(f"1D array: {arr_1d}")
print(f"Broadcasted addition:\n{broadcasted}")

# 2. Boolean indexing
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = arr > 5                              # Create boolean mask
filtered = arr[mask]                        # Filter using mask
print(f"Original array: {arr}")
print(f"Boolean mask: {mask}")
print(f"Filtered array (>5): {filtered}")
```

2.  Provide two practical examples of tasks where NumPy Series would be
    beneficial in data processing and analysis. **Write a Python program
    to perform the following tasks using Pandas:**

### Answer

**Two Practical Examples of NumPy/Pandas Series Benefits:**

1. **Financial Time Series Analysis**: Stock price calculations, moving averages, and percentage changes

### Answer

```python
import pandas as pd
import numpy as np

# 1. Financial Time Series Analysis
dates = pd.date_range(start='2020-01-01', periods=100)
prices = np.random.normal(loc=100, scale=10, size=len(dates))
stock_data = pd.Series(data=prices, index=dates)

# Calculate moving average
moving_avg = stock_data.rolling(window=5).mean()

# Calculate daily returns
daily_returns = stock_data.pct_change()

print("Financial Time Series Analysis:")
print(f"Stock Prices:\n{stock_data.head()}")
print(f"Moving Average:\n{moving_avg.head()}")
print(f"Daily Returns:\n{daily_returns.head()}")

```

with numpy arrays 

```python
import numpy as np 
# Creating a NumPy array for financial data
price = np.random.normal(loc=100, scale=10, size=100)
print(price)

rolling_mvg = np.convolve(price, np.ones(5)/5, mode='valid')
print(rolling_mvg)

print(np.mean(rolling_mvg))
```

2. **Sensor Data Processing**: Temperature readings, statistical analysis, and anomaly detection

```python
import pandas as pd
import numpy as np

# Simulate temperature data
dates = pd.date_range(start='2023-01-01', periods=100)
temperature = np.random.normal(loc=20, scale=5, size=len(dates))
sensor_data = pd.Series(data=temperature, index=dates)

# Calculate basic statistics
mean_temp = sensor_data.mean()
std_temp = sensor_data.std()

# Detect anomalies (e.g., values outside 3 standard deviations)
anomalies = sensor_data[np.abs(sensor_data - mean_temp) > 3 * std_temp]

print("Sensor Data Processing:")
print(f"Temperature Data:\n{sensor_data.head()}")
print(f"Mean Temperature: {mean_temp:.2f}")
print(f"Standard Deviation: {std_temp:.2f}")
print(f"Anomalies Detected:\n{anomalies}")
```


```python
import pandas as pd          # Import Pandas for data manipulation
import numpy as np           # Import NumPy for numerical operations
from datetime import datetime, timedelta  # Import for date operations
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# First, let's create sample data since we don't have the actual Excel file
print("Creating sample employee data...")

# Create sample employee data
np.random.seed(42)  # Set seed for reproducible random numbers
sample_data = {
    'EmployeeID': list(range(1, 51)) + [1, 2],  # 50 unique + 2 duplicates
    'Name': [f'Employee_{i}' for i in range(1, 51)] + ['Employee_1', 'Employee_2'],
    'Department': np.random.choice(['HR', 'IT', 'Finance', 'Marketing'], 52),
    'Salary': np.random.normal(60000, 20000, 52),  # Normal distribution around 60k
    'JoinDate': [datetime.now() - timedelta(days=np.random.randint(365, 3650)) 
                 for _ in range(52)],
    'Experience': np.random.randint(0, 15, 52)
}

# Introduce some missing values for demonstration
sample_data['Salary'][5] = np.nan      # Missing salary value
sample_data['Salary'][15] = np.nan     # Another missing salary
sample_data['Experience'][10] = np.nan # Missing experience value
sample_data['Experience'][20] = np.nan # Another missing experience

# Create DataFrame from sample data
df = pd.DataFrame(sample_data)

# Convert JoinDate to string first (simulating Excel import)
df['JoinDate'] = df['JoinDate'].dt.strftime('%Y-%m-%d')

# Save sample data to Excel file (simulating the original file)
df.to_excel('employee_data.xlsx', index=False)
print("Sample data created and saved to employee_data.xlsx")

# Now let's perform the requested tasks:

# a) Load Excel file into Pandas DataFrame
print("\na) Loading Excel file into DataFrame...")
try:
    df = pd.read_excel('employee_data.xlsx')  # Read Excel file into DataFrame
    print(f"Successfully loaded DataFrame with shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")    # Display column names
except FileNotFoundError:
    print("Error: employee_data.xlsx file not found!")
    exit()

# Display basic information about the DataFrame
print("\nDataFrame info:")
print(df.info())  # Show data types, non-null counts, and memory usage

# b) Display the last 10 rows of the DataFrame
print("\nb) Last 10 rows of the DataFrame:")
print(df.tail(10))  # Show last 10 rows using tail() method

# Alternative way to show last 10 rows
print("\nAlternative method using iloc:")
print(df.iloc[-10:])  # Use iloc with negative indexing for last 10 rows

# c) Identify and handle missing values
print("\nc) Handling missing values...")

# Check for missing values in all columns
print("Missing values before handling:")
print(df.isnull().sum())  # Count missing values in each column

# Handle missing values in Salary column
if df['Salary'].isnull().any():  # Check if there are any missing salary values
    salary_median = df['Salary'].median()  # Calculate median of non-null salary values
    print(f"Salary median: {salary_median:.2f}")
    df['Salary'].fillna(salary_median, inplace=True)  # Fill missing values with median
    print("Missing salary values filled with median")

# Handle missing values in Experience column
if df['Experience'].isnull().any():  # Check if there are any missing experience values
    df['Experience'].fillna(0, inplace=True)  # Fill missing values with 0
    print("Missing experience values filled with 0")

# Verify missing values are handled
print("\nMissing values after handling:")
print(df.isnull().sum())  # Verify no missing values remain

# d) Remove duplicate rows based on EmployeeID column
print("\nd) Removing duplicate rows...")
print(f"DataFrame shape before removing duplicates: {df.shape}")

# Check for duplicates based on EmployeeID
duplicates = df.duplicated(subset=['EmployeeID'], keep='first')  # Mark duplicates
print(f"Number of duplicate EmployeeIDs found: {duplicates.sum()}")

if duplicates.any():
    print("Duplicate rows found:")
    print(df[duplicates])  # Show duplicate rows
    
    # Remove duplicates, keeping first occurrence
    df = df.drop_duplicates(subset=['EmployeeID'], keep='first')
    print(f"DataFrame shape after removing duplicates: {df.shape}")

# e) Convert JoinDate column to datetime format
print("\ne) Converting JoinDate to datetime format...")
print(f"JoinDate data type before conversion: {df['JoinDate'].dtype}")

# Convert string dates to datetime objects
df['JoinDate'] = pd.to_datetime(df['JoinDate'])  # Convert to datetime
print(f"JoinDate data type after conversion: {df['JoinDate'].dtype}")

# Display sample of converted dates
print("Sample of converted JoinDate values:")
print(df[['Name', 'JoinDate']].head())

# f) Filter DataFrame for HR and IT departments with salary > 50,000
print("\nf) Filtering DataFrame...")
print(f"Original DataFrame shape: {df.shape}")

# Create boolean conditions for filtering
dept_condition = df['Department'].isin(['HR', 'IT'])  # Check if department is HR or IT
salary_condition = df['Salary'] > 50000               # Check if salary > 50,000
combined_condition = dept_condition & salary_condition # Combine conditions with AND

# Apply the filter
filtered_df = df[combined_condition].copy()  # Create filtered copy
print(f"Filtered DataFrame shape: {filtered_df.shape}")

# Display department and salary distribution in filtered data
print("\nDepartment distribution in filtered data:")
print(filtered_df['Department'].value_counts())

print(f"\nSalary statistics for filtered data:")
print(filtered_df['Salary'].describe())  # Show statistical summary

# Display sample of filtered data
print("\nSample of filtered data:")
print(filtered_df[['EmployeeID', 'Name', 'Department', 'Salary']].head(10))

# g) Save cleaned and filtered DataFrame to new Excel file
print("\ng) Saving filtered DataFrame to Excel...")
try:
    # Save to new Excel file
    filtered_df.to_excel('filtered_employee_data.xlsx', index=False)
    print("Successfully saved filtered data to 'filtered_employee_data.xlsx'")
    
    # Display final summary
    print(f"\nFinal summary:")
    print(f"- Original records: {len(df)}")
    print(f"- Filtered records: {len(filtered_df)}")
    print(f"- Records removed: {len(df) - len(filtered_df)}")
    print(f"- Columns in final dataset: {list(filtered_df.columns)}")
    
except Exception as e:
    print(f"Error saving file: {e}")

# Additional analysis for better understanding
print("\nAdditional Data Analysis:")

# Show data types of all columns
print("\nData types of all columns:")
print(filtered_df.dtypes)

# Show basic statistics for numerical columns
print("\nStatistical summary of numerical columns:")
print(filtered_df.describe())

# Show unique values in categorical columns
print(f"\nUnique departments: {filtered_df['Department'].unique()}")
print(f"Department counts:\n{filtered_df['Department'].value_counts()}")

# Example of practical NumPy Series usage
print("\nPractical NumPy Series Examples:")

# Example 1: Financial calculations
stock_prices = pd.Series([100, 102, 98, 105, 108, 103, 110])
print("Stock Price Analysis:")
print(f"Stock prices: {stock_prices.values}")
print(f"Daily returns: {stock_prices.pct_change().values}")  # Percentage change
print(f"Moving average (3-day): {stock_prices.rolling(3).mean().values}")

# Example 2: Sensor data processing
temperature_readings = pd.Series([22.5, 23.1, 24.8, 22.9, 25.2, 21.8, 23.7])
print("\nTemperature Sensor Analysis:")
print(f"Temperatures: {temperature_readings.values}")
print(f"Above average count: {(temperature_readings > temperature_readings.mean()).sum()}")
print(f"Temperature range: {temperature_readings.max() - temperature_readings.min():.1f}°C")
```

Unit 2

1.  i\) Load a dataset into a Pandas DataFrame and clean the data
    (handle missing values, drop unnecessary columns) and Perform group
    by operations and calculate summary Statistics, display the first 10
    rows, and perform basic data manipulation (sorting, filtering).
    (10M)

+----------------+--------------+--------------+---------+-------------+
| > Date         | > Store      | > Product    | > Sales | > Quantity  |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-01   | > Store A    | > Widget A   | > 200   | > 10        |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-02   | > Store A    | > Widget B   | > 150   | > 5         |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-03   | > Store B    | > Widget A   | > 300   | > 15        |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-04   | > Store B    | > Widget C   |         | > 8         |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-05   | > Store A    |              | > 250   | > 20        |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-06   | > Store C    | > Widget A   | > 400   | > 20        |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-07   | > Store C    | > Widget B   | > 100   | > 2         |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-08   | > Store A    | > Widget C   | > 150   | > 6         |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-09   | > Store B    | > Widget B   |         | > 5         |
+----------------+--------------+--------------+---------+-------------+
| > 2023-01-10   | > Store C    | > Widget C   | > 350   | > 10        |
+----------------+--------------+--------------+---------+-------------+

### Answer (i)

**Data Loading, Cleaning, and Analysis**

```python
import pandas as pd         # Import Pandas for data manipulation
import numpy as np          # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import seaborn as sns       # Import Seaborn for enhanced visualization

# Create the dataset from the given table
print("Creating dataset from the given table...")
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
             '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'],
    'Store': ['Store A', 'Store A', 'Store B', 'Store B', 'Store A',
              'Store C', 'Store C', 'Store A', 'Store B', 'Store C'],
    'Product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', np.nan,
                'Widget A', 'Widget B', 'Widget C', 'Widget B', 'Widget C'],
    'Sales': [200, 150, 300, np.nan, 250, 400, 100, 150, np.nan, 350],
    'Quantity': [10, 5, 15, 8, 20, 20, 2, 6, 5, 10]
}

# Load data into Pandas DataFrame
df = pd.DataFrame(data)  # Create DataFrame from dictionary
print("Dataset loaded successfully!")
print(f"DataFrame shape: {df.shape}")  # Display dimensions (rows, columns)

# Display basic information about the dataset
print("\nDataset Information:")
print(df.info())  # Show data types, non-null counts, memory usage

print("\nFirst 10 rows of the dataset:")
print(df.head(10))  # Display first 10 rows (or all if less than 10)

# Data Cleaning Process
print("\n" + "="*50)
print("DATA CLEANING PROCESS")
print("="*50)

# Step 1: Check for missing values
print("\n1. Checking for missing values:")
missing_values = df.isnull().sum()  # Count missing values per column
print(missing_values)

# Identify columns with missing values
columns_with_missing = missing_values[missing_values > 0]  # Filter columns with missing data
if len(columns_with_missing) > 0:
    print(f"\nColumns with missing values: {list(columns_with_missing.index)}")
else:
    print("No missing values found!")

# Step 2: Handle missing values
print("\n2. Handling missing values:")

# Fill missing Sales values with median
if df['Sales'].isnull().any():
    sales_median = df['Sales'].median()  # Calculate median of non-null values
    print(f"Filling missing Sales values with median: {sales_median}")
    df['Sales'].fillna(sales_median, inplace=True)  # Fill missing values in-place

# Fill missing Product values with 'Unknown'
if df['Product'].isnull().any():
    print("Filling missing Product values with 'Unknown'")
    df['Product'].fillna('Unknown', inplace=True)  # Fill missing product names

# Verify missing values are handled
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 3: Convert Date column to datetime
print("\n3. Converting Date column to datetime format:")
df['Date'] = pd.to_datetime(df['Date'])  # Convert string dates to datetime objects
print(f"Date column data type: {df['Date'].dtype}")

# Step 4: Add calculated columns for analysis
print("\n4. Adding calculated columns:")
df['Revenue_Per_Unit'] = df['Sales'] / df['Quantity']  # Calculate revenue per unit
print("Added 'Revenue_Per_Unit' column")

# Display cleaned dataset
print("\nCleaned dataset (first 10 rows):")
print(df.head(10))

# Data Manipulation Operations
print("\n" + "="*50)
print("DATA MANIPULATION OPERATIONS")
print("="*50)

# Sorting operations
print("\n1. Sorting Operations:")

# Sort by Sales in descending order
df_sorted_sales = df.sort_values('Sales', ascending=False)  # Sort by sales descending
print("Dataset sorted by Sales (descending):")
print(df_sorted_sales[['Store', 'Product', 'Sales']].head())

# Sort by multiple columns
df_sorted_multi = df.sort_values(['Store', 'Sales'], ascending=[True, False])  # Sort by store ascending, then sales descending
print("\nDataset sorted by Store (asc) then Sales (desc):")
print(df_sorted_multi[['Store', 'Product', 'Sales']].head())

# Filtering operations
print("\n2. Filtering Operations:")

# Filter high sales records (>200)
high_sales = df[df['Sales'] > 200]  # Boolean filtering for sales > 200
print(f"Records with Sales > 200 ({len(high_sales)} records):")
print(high_sales[['Store', 'Product', 'Sales']])

# Filter specific stores
store_filter = df[df['Store'].isin(['Store A', 'Store B'])]  # Filter for specific stores
print(f"\nRecords from Store A and Store B ({len(store_filter)} records):")
print(store_filter[['Store', 'Product', 'Sales']].head())

# Complex filtering
complex_filter = df[(df['Sales'] >= 150) & (df['Quantity'] >= 10)]  # Multiple conditions
print(f"\nRecords with Sales>=150 AND Quantity>=10 ({len(complex_filter)} records):")
print(complex_filter[['Store', 'Product', 'Sales', 'Quantity']])

# Group By Operations and Summary Statistics
print("\n" + "="*50)
print("GROUP BY OPERATIONS & SUMMARY STATISTICS")
print("="*50)

# Group by Store
print("\n1. Analysis by Store:")
store_stats = df.groupby('Store').agg({  # Group by store and calculate multiple statistics
    'Sales': ['sum', 'mean', 'count'],      # Sum, mean, count of sales
    'Quantity': ['sum', 'mean'],            # Sum and mean of quantity
    'Revenue_Per_Unit': 'mean'              # Mean revenue per unit
}).round(2)  # Round to 2 decimal places

print("Statistics by Store:")
print(store_stats)

# Group by Product
print("\n2. Analysis by Product:")
product_stats = df.groupby('Product').agg({  # Group by product
    'Sales': ['sum', 'mean', 'max', 'min'],     # Various sales statistics
    'Quantity': 'sum'                           # Total quantity sold
}).round(2)

print("Statistics by Product:")
print(product_stats)

# Group by Store and Product
print("\n3. Analysis by Store and Product:")
store_product_stats = df.groupby(['Store', 'Product'])['Sales'].sum()  # Group by multiple columns
print("Total Sales by Store and Product:")
print(store_product_stats)

# Overall Summary Statistics
print("\n4. Overall Summary Statistics:")
numerical_summary = df.describe()  # Statistical summary of numerical columns
print("Numerical columns summary:")
print(numerical_summary)

# Custom aggregations
print("\n5. Custom Aggregations:")
custom_agg = df.groupby('Store').agg({  # Custom aggregation functions
    'Sales': lambda x: x.max() - x.min(),     # Sales range (max - min)
    'Quantity': lambda x: x.std(),            # Standard deviation of quantity
    'Date': lambda x: x.max() - x.min()       # Date range
})
custom_agg.columns = ['Sales_Range', 'Quantity_StdDev', 'Date_Range']  # Rename columns
print("Custom aggregations by Store:")
print(custom_agg)

# Additional Analysis
print("\n" + "="*50)
print("ADDITIONAL ANALYSIS")
print("="*50)

# Top performing records
print("\n1. Top 5 records by Sales:")
top_sales = df.nlargest(5, 'Sales')  # Get top 5 records by sales
print(top_sales[['Store', 'Product', 'Sales', 'Quantity']])

# Store performance ranking
print("\n2. Store Performance Ranking:")
store_ranking = df.groupby('Store')['Sales'].sum().sort_values(ascending=False)  # Rank stores by total sales
print("Stores ranked by total sales:")
for i, (store, sales) in enumerate(store_ranking.items(), 1):
    print(f"{i}. {store}: ${sales:,.2f}")

# Product popularity
print("\n3. Product Popularity (by quantity sold):")
product_popularity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)  # Rank products by quantity
print("Products ranked by total quantity sold:")
for i, (product, quantity) in enumerate(product_popularity.items(), 1):
    print(f"{i}. {product}: {quantity} units")

# Daily sales trend
print("\n4. Daily Sales Trend:")
daily_sales = df.groupby('Date')['Sales'].sum().sort_values(ascending=False)  # Sales by date
print("Daily sales (sorted by amount):")
print(daily_sales)

# Final cleaned dataset
print("\n" + "="*50)
print("FINAL CLEANED DATASET")
print("="*50)
print(f"Final dataset shape: {df.shape}")
print("\nFinal dataset preview:")
print(df)
```

ii\) Demonstrate how to create different types of plots (line plot, bar
plot, scatter plot) using Matplotlib. Provide code examples. Explain how
to add titles, labels (x and y axis), and customize colors in these
plots. Include examples of customization in your code. (10M)

### Answer (ii)

**Matplotlib Plotting and Customization**

```python
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import numpy as np               # Import NumPy for numerical operations
import pandas as pd              # Import Pandas for data handling
import seaborn as sns            # Import Seaborn for enhanced styling

# Set up the plotting style
plt.style.use('seaborn-v0_8')   # Use seaborn style for better appearance
plt.rcParams['figure.figsize'] = (12, 8)  # Set default figure size

# Sample data for demonstrations
print("Creating sample data for plotting demonstrations...")

# Data for line plot - Stock prices over time
dates = pd.date_range('2023-01-01', periods=30, freq='D')  # Create 30 consecutive dates
stock_prices = 100 + np.cumsum(np.random.randn(30) * 2)   # Simulate stock price movement
volume = np.random.randint(1000, 5000, 30)                # Random trading volume

# Data for bar plot - Sales by product category
categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']  # Product categories
sales_data = [25000, 18000, 12000, 15000, 20000]                     # Sales figures
colors_bar = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'] # Custom colors

# Data for scatter plot - Height vs Weight correlation
np.random.seed(42)  # Set seed for reproducible results
height = np.random.normal(170, 10, 50)      # Height in cm (normal distribution)
weight = 0.8 * height + np.random.normal(0, 8, 50) - 50  # Correlated weight with noise

print("Data created successfully! Creating plots...")

# 1. LINE PLOT DEMONSTRATION
print("\n1. Creating Line Plot...")
plt.figure(figsize=(14, 10))  # Create figure with specific size

# Subplot 1: Basic Line Plot
plt.subplot(2, 2, 1)  # Create subplot: 2 rows, 2 columns, position 1
plt.plot(dates, stock_prices)  # Create basic line plot
plt.title('Basic Line Plot - Stock Price Over Time')  # Add title
plt.xlabel('Date')           # Add x-axis label
plt.ylabel('Stock Price ($)') # Add y-axis label
plt.xticks(rotation=45)      # Rotate x-axis labels for better readability
plt.grid(True, alpha=0.3)    # Add grid with transparency

# Subplot 2: Customized Line Plot
plt.subplot(2, 2, 2)  # Position 2
plt.plot(dates, stock_prices, 
         color='#e74c3c',      # Custom red color
         linewidth=2.5,        # Thicker line
         linestyle='-',        # Solid line style
         marker='o',           # Circle markers at data points
         markersize=4,         # Marker size
         markerfacecolor='white',  # White marker fill
         markeredgecolor='#e74c3c',  # Red marker edge
         alpha=0.8)            # Line transparency
plt.title('Customized Line Plot', fontsize=14, fontweight='bold')  # Styled title
plt.xlabel('Date', fontsize=12, fontweight='bold')    # Styled x-label
plt.ylabel('Stock Price ($)', fontsize=12, fontweight='bold')  # Styled y-label
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, linestyle='--')  # Dashed grid lines

# Subplot 3: Multiple Lines
plt.subplot(2, 2, 3)  # Position 3
# Create multiple datasets
line1 = stock_prices
line2 = stock_prices * 0.8 + 10  # Second line with different values
line3 = stock_prices * 1.2 - 20  # Third line

plt.plot(dates, line1, label='Stock A', color='#3498db', linewidth=2)  # Blue line
plt.plot(dates, line2, label='Stock B', color='#e74c3c', linewidth=2)  # Red line  
plt.plot(dates, line3, label='Stock C', color='#2ecc71', linewidth=2)  # Green line
plt.title('Multiple Line Plot with Legend')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend(loc='upper left')  # Add legend in upper left corner
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Subplot 4: Styled Line Plot with Fill
plt.subplot(2, 2, 4)  # Position 4
plt.plot(dates, stock_prices, color='#9b59b6', linewidth=3)  # Purple line
plt.fill_between(dates, stock_prices, alpha=0.3, color='#9b59b6')  # Fill area under curve
plt.title('Line Plot with Fill Area')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()  # Automatically adjust spacing between subplots
plt.show()          # Display the plots

# 2. BAR PLOT DEMONSTRATION
print("\n2. Creating Bar Plots...")
plt.figure(figsize=(14, 10))  # Create new figure

# Subplot 1: Basic Vertical Bar Plot
plt.subplot(2, 2, 1)  # Position 1
bars = plt.bar(categories, sales_data)  # Create basic bar plot
plt.title('Basic Vertical Bar Plot - Sales by Category')
plt.xlabel('Product Category')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)  # Rotate category names

# Add value labels on top of bars
for bar, value in zip(bars, sales_data):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f'${value:,}',     # Format with comma separator
             ha='center',       # Horizontal alignment: center
             va='bottom')       # Vertical alignment: bottom

# Subplot 2: Customized Vertical Bar Plot
plt.subplot(2, 2, 2)  # Position 2
bars = plt.bar(categories, sales_data,
               color=colors_bar,      # Use custom colors for each bar
               edgecolor='black',     # Black border around bars
               linewidth=1.5,         # Border thickness
               alpha=0.8)             # Bar transparency
plt.title('Customized Bar Plot with Colors', fontsize=14, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.xticks(rotation=45)

# Add gradient-like effect by varying alpha
for i, bar in enumerate(bars):
    bar.set_alpha(0.6 + i * 0.1)  # Increasing transparency

# Add value labels
for bar, value in zip(bars, sales_data):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f'${value:,}', ha='center', va='bottom', fontweight='bold')

# Subplot 3: Horizontal Bar Plot
plt.subplot(2, 2, 3)  # Position 3
bars = plt.barh(categories, sales_data, color='#34495e')  # Horizontal bars
plt.title('Horizontal Bar Plot')
plt.xlabel('Sales ($)')
plt.ylabel('Product Category')

# Add value labels to the right of bars
for i, (bar, value) in enumerate(zip(bars, sales_data)):
    plt.text(bar.get_width() + 500, bar.get_y() + bar.get_height()/2,
             f'${value:,}', ha='left', va='center')

# Subplot 4: Grouped Bar Plot
plt.subplot(2, 2, 4)  # Position 4
# Create data for grouped bars
quarters = ['Q1', 'Q2', 'Q3', 'Q4']  # Time periods
product_a = [20000, 25000, 30000, 28000]  # Product A sales
product_b = [15000, 22000, 28000, 32000]  # Product B sales

x = np.arange(len(quarters))  # Positions for bars
width = 0.35  # Width of bars

# Create grouped bars
bars1 = plt.bar(x - width/2, product_a, width, label='Product A', color='#3498db')
bars2 = plt.bar(x + width/2, product_b, width, label='Product B', color='#e74c3c')

plt.title('Grouped Bar Plot - Quarterly Sales Comparison')
plt.xlabel('Quarter')
plt.ylabel('Sales ($)')
plt.xticks(x, quarters)  # Set x-axis labels
plt.legend()  # Add legend

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 500,
                f'${height:,.0f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

# 3. SCATTER PLOT DEMONSTRATION
print("\n3. Creating Scatter Plots...")
plt.figure(figsize=(14, 10))

# Subplot 1: Basic Scatter Plot
plt.subplot(2, 2, 1)  # Position 1
plt.scatter(height, weight)  # Basic scatter plot
plt.title('Basic Scatter Plot - Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True, alpha=0.3)

# Subplot 2: Customized Scatter Plot
plt.subplot(2, 2, 2)  # Position 2
plt.scatter(height, weight,
            c='#e74c3c',       # Red color
            s=60,              # Size of points
            alpha=0.6,         # Transparency
            edgecolors='black', # Black edge around points
            linewidths=1)      # Edge thickness
plt.title('Customized Scatter Plot', fontsize=14, fontweight='bold')
plt.xlabel('Height (cm)', fontsize=12)
plt.ylabel('Weight (kg)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')

# Add trend line
z = np.polyfit(height, weight, 1)  # Calculate linear regression
p = np.poly1d(z)                   # Create polynomial function
plt.plot(height, p(height), "r--", alpha=0.8, linewidth=2)  # Add trend line

# Subplot 3: Color-coded Scatter Plot
plt.subplot(2, 2, 3)  # Position 3
# Create categories based on BMI
bmi = weight / ((height/100) ** 2)  # Calculate BMI
colors = ['green' if b < 18.5 else 'blue' if b < 25 else 'orange' if b < 30 else 'red' 
          for b in bmi]  # Color-code based on BMI categories

plt.scatter(height, weight, c=colors, s=80, alpha=0.7, edgecolors='black')
plt.title('Color-coded Scatter Plot (BMI Categories)')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True, alpha=0.3)

# Add legend for colors
from matplotlib.patches import Patch  # Import for custom legend
legend_elements = [Patch(facecolor='green', label='Underweight (<18.5)'),
                  Patch(facecolor='blue', label='Normal (18.5-25)'),
                  Patch(facecolor='orange', label='Overweight (25-30)'),
                  Patch(facecolor='red', label='Obese (>30)')]
plt.legend(handles=legend_elements, loc='upper left')

# Subplot 4: Size and Color Varying Scatter Plot
plt.subplot(2, 2, 4)  # Position 4
# Create additional data for size variation
income = np.random.normal(50000, 15000, 50)  # Random income data
age = np.random.randint(20, 60, 50)          # Random age data

# Create scatter plot with varying size and color
scatter = plt.scatter(height, weight,
                     c=age,           # Color based on age
                     s=income/500,    # Size based on income
                     alpha=0.6,
                     cmap='viridis',  # Color map
                     edgecolors='black')

plt.title('Multi-dimensional Scatter Plot')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True, alpha=0.3)

# Add color bar for age
cbar = plt.colorbar(scatter)
cbar.set_label('Age (years)', rotation=270, labelpad=20)

# Add text annotation for size meaning
plt.text(0.02, 0.98, 'Bubble size = Income', transform=plt.gca().transAxes,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# 4. ADVANCED CUSTOMIZATION EXAMPLES
print("\n4. Advanced Customization Examples...")
plt.figure(figsize=(15, 5))

# Advanced Line Plot with Multiple Customizations
plt.subplot(1, 3, 1)
x = np.linspace(0, 10, 100)  # Create x values
y1 = np.sin(x)               # Sine wave
y2 = np.cos(x)               # Cosine wave

plt.plot(x, y1, color='#e74c3c', linewidth=3, linestyle='-', 
         marker='o', markersize=3, markevery=10, label='sin(x)')
plt.plot(x, y2, color='#3498db', linewidth=3, linestyle='--', 
         marker='s', markersize=3, markevery=10, label='cos(x)')

plt.title('Advanced Line Plot Customization', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('X Values', fontsize=14, fontweight='bold')
plt.ylabel('Y Values', fontsize=14, fontweight='bold')
plt.legend(fontsize=12, frameon=True, shadow=True)
plt.grid(True, alpha=0.3, linestyle=':', linewidth=1)
plt.axhline(y=0, color='black', linewidth=0.5)  # Add horizontal line at y=0
plt.axvline(x=0, color='black', linewidth=0.5)  # Add vertical line at x=0

# Advanced Bar Plot with Gradient Effect
plt.subplot(1, 3, 2)
data = [10, 25, 30, 45, 20]
labels = ['A', 'B', 'C', 'D', 'E']
colors_gradient = plt.cm.plasma(np.linspace(0, 1, len(data)))  # Gradient colors

bars = plt.bar(labels, data, color=colors_gradient, 
               edgecolor='white', linewidth=2)

# Add patterns to bars
patterns = ['///', '...', '+++', 'xxx', '|||']
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

plt.title('Advanced Bar Plot with Patterns', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Categories', fontsize=14, fontweight='bold')
plt.ylabel('Values', fontsize=14, fontweight='bold')

# Add value labels with custom styling
for bar, value in zip(bars, data):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f'{value}', ha='center', va='bottom', 
             fontsize=12, fontweight='bold', 
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# Advanced Scatter Plot with Annotations
plt.subplot(1, 3, 3)
x = np.random.randn(20)
y = np.random.randn(20)
colors = np.random.rand(20)
sizes = 1000 * np.random.rand(20)

scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, 
                     cmap='tab10', edgecolors='black', linewidth=1)

plt.title('Advanced Scatter Plot', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('X Coordinate', fontsize=14, fontweight='bold')
plt.ylabel('Y Coordinate', fontsize=14, fontweight='bold')

# Add annotations for specific points
for i in range(0, 20, 5):  # Annotate every 5th point
    plt.annotate(f'Point {i}', (x[i], y[i]), 
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.grid(True, alpha=0.3)
plt.colorbar(scatter, label='Color Scale')

plt.tight_layout()
plt.show()

print("\nPlotting demonstrations completed!")
print("Key customization features demonstrated:")
print("- Titles, labels, and text formatting")
print("- Colors, transparency, and gradients") 
print("- Line styles, markers, and patterns")
print("- Legends, colorbars, and annotations")
print("- Grid styling and axis customization")
print("- Multiple subplots and layouts")
```

[Lab questions]{.underline}

1.  You are given a dataset called \"student_scores.csv\" that contains
    the following columns:

  ----------------- ----------------- ----------------- -----------------
  Name              Math_Score        Science_Score     English_Score

  Alice             78                85                92

  Bob               85                82                88

  Charlie           92                91                85

  David             88                79                78

  Eva               79                95                91

  Frank             76                84                77
  ----------------- ----------------- ----------------- -----------------

> a\. Create a NumPy array using the above data for the first 5
> students\' Math scores.
>
> b\. Perform the following operations on the NumPy array:
>
> i\) Find the mean of the Math scores.
>
> ii\) Find the maximum and minimum Math scores.

### Answer

**Student Scores Analysis using NumPy**

```python
import numpy as np      # Import NumPy for numerical operations
import pandas as pd     # Import Pandas for data manipulation

# Create the student dataset as given in the problem
print("Creating student scores dataset...")

# Define the data as provided in the table
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Math_Score': [78, 85, 92, 88, 79, 76],
    'Science_Score': [85, 82, 91, 79, 95, 84],
    'English_Score': [92, 88, 85, 78, 91, 77]
}

# Create DataFrame for better data visualization
df = pd.DataFrame(student_data)  # Convert dictionary to DataFrame
print("Complete Student Dataset:")
print(df)  # Display the complete dataset

print("\n" + "="*50)
print("PART A: Creating NumPy Array")
print("="*50)

# a. Create a NumPy array using the first 5 students' Math scores
first_5_math_scores = np.array(student_data['Math_Score'][:5])  # Extract first 5 math scores
print(f"First 5 students' names: {student_data['Name'][:5]}")   # Show corresponding names
print(f"First 5 Math scores as list: {student_data['Math_Score'][:5]}")  # Show as list
print(f"NumPy array of first 5 Math scores: {first_5_math_scores}")      # Show as NumPy array
print(f"Array data type: {first_5_math_scores.dtype}")                   # Show data type
print(f"Array shape: {first_5_math_scores.shape}")                       # Show array dimensions

# Alternative method using array slicing
all_math_scores = np.array(student_data['Math_Score'])  # Create array of all math scores
first_5_alternative = all_math_scores[:5]               # Slice first 5 elements
print(f"Alternative method result: {first_5_alternative}")  # Verify same result

print("\n" + "="*50)
print("PART B: Array Operations")
print("="*50)

# b. Perform operations on the NumPy array

# i) Find the mean of the Math scores
math_mean = np.mean(first_5_math_scores)  # Calculate mean using NumPy function
print(f"i) Mean of first 5 Math scores:")
print(f"   Calculation: ({' + '.join(map(str, first_5_math_scores))}) / {len(first_5_math_scores)}")
print(f"   Mean = {math_mean:.2f}")

# Alternative methods to calculate mean
manual_mean = sum(first_5_math_scores) / len(first_5_math_scores)  # Manual calculation
array_mean_method = first_5_math_scores.mean()                    # Array method
print(f"   Verification - Manual calculation: {manual_mean:.2f}")
print(f"   Verification - Array method: {array_mean_method:.2f}")

# ii) Find the maximum and minimum Math scores
math_max = np.max(first_5_math_scores)    # Find maximum value
math_min = np.min(first_5_math_scores)    # Find minimum value
max_index = np.argmax(first_5_math_scores)  # Find index of maximum value
min_index = np.argmin(first_5_math_scores)  # Find index of minimum value

print(f"\nii) Maximum and Minimum Math scores:")
print(f"    Maximum score: {math_max}")
print(f"    Maximum score student: {student_data['Name'][max_index]} (index {max_index})")
print(f"    Minimum score: {math_min}")
print(f"    Minimum score student: {student_data['Name'][min_index]} (index {min_index})")

# Alternative methods
array_max = first_5_math_scores.max()  # Array method for max
array_min = first_5_math_scores.min()  # Array method for min
print(f"    Verification - Array max method: {array_max}")
print(f"    Verification - Array min method: {array_min}")

print("\n" + "="*50)
print("ADDITIONAL ANALYSIS")
print("="*50)

# Additional useful operations on the array
print("Additional statistical operations:")

# Standard deviation
std_dev = np.std(first_5_math_scores)  # Calculate standard deviation
print(f"Standard deviation: {std_dev:.2f}")

# Variance
variance = np.var(first_5_math_scores)  # Calculate variance
print(f"Variance: {variance:.2f}")

# Median
median = np.median(first_5_math_scores)  # Calculate median
print(f"Median: {median:.2f}")

# Range
score_range = math_max - math_min  # Calculate range
print(f"Range (Max - Min): {score_range}")

# Percentiles
percentile_25 = np.percentile(first_5_math_scores, 25)  # 25th percentile
percentile_75 = np.percentile(first_5_math_scores, 75)  # 75th percentile
print(f"25th percentile: {percentile_25:.2f}")
print(f"75th percentile: {percentile_75:.2f}")

# Sorting operations
sorted_scores = np.sort(first_5_math_scores)           # Sort in ascending order
sorted_indices = np.argsort(first_5_math_scores)       # Get indices that would sort the array
reverse_sorted = np.sort(first_5_math_scores)[::-1]    # Sort in descending order

print(f"\nSorting operations:")
print(f"Original array: {first_5_math_scores}")
print(f"Sorted ascending: {sorted_scores}")
print(f"Sorted descending: {reverse_sorted}")
print(f"Sorting indices: {sorted_indices}")

# Show students in order of performance
print(f"\nStudents ranked by Math scores (descending):")
sorted_names = [student_data['Name'][i] for i in np.argsort(first_5_math_scores)[::-1]]
sorted_scores_desc = np.sort(first_5_math_scores)[::-1]
for i, (name, score) in enumerate(zip(sorted_names, sorted_scores_desc), 1):
    print(f"{i}. {name}: {score}")

# Boolean operations
print(f"\nBoolean operations:")
above_average = first_5_math_scores > math_mean  # Boolean array for scores above average
print(f"Scores above average ({math_mean:.2f}): {above_average}")
print(f"Students above average: {np.sum(above_average)} out of {len(first_5_math_scores)}")

# Find students above average
above_avg_indices = np.where(above_average)[0]  # Get indices where condition is True
print(f"Above average students:")
for idx in above_avg_indices:
    print(f"  {student_data['Name'][idx]}: {first_5_math_scores[idx]}")

# Array manipulation
print(f"\nArray manipulation examples:")
doubled_scores = first_5_math_scores * 2  # Multiply all elements by 2
normalized_scores = (first_5_math_scores - math_mean) / std_dev  # Z-score normalization
print(f"Doubled scores: {doubled_scores}")
print(f"Normalized scores (z-scores): {normalized_scores}")

# Working with all students' data
print("\n" + "="*50)
print("ANALYSIS WITH COMPLETE DATASET")
print("="*50)

# Create 2D array with all scores
all_scores = np.array([
    student_data['Math_Score'],
    student_data['Science_Score'], 
    student_data['English_Score']
])

print(f"All scores as 2D array:")
print(f"Shape: {all_scores.shape}")  # (3 subjects, 6 students)
print(all_scores)

# Subject-wise statistics
subjects = ['Math', 'Science', 'English']
print(f"\nSubject-wise statistics:")
for i, subject in enumerate(subjects):
    subject_scores = all_scores[i]  # Get scores for this subject
    print(f"{subject}:")
    print(f"  Mean: {np.mean(subject_scores):.2f}")
    print(f"  Max: {np.max(subject_scores)} (Student: {student_data['Name'][np.argmax(subject_scores)]})")
    print(f"  Min: {np.min(subject_scores)} (Student: {student_data['Name'][np.argmin(subject_scores)]})")
    print(f"  Std Dev: {np.std(subject_scores):.2f}")

# Student-wise total scores
student_totals = np.sum(all_scores, axis=0)  # Sum across subjects for each student
print(f"\nStudent total scores:")
for i, (name, total) in enumerate(zip(student_data['Name'], student_totals)):
    print(f"{name}: {total} (Average: {total/3:.2f})")

# Find best performing student overall
best_student_idx = np.argmax(student_totals)
print(f"\nBest performing student overall:")
print(f"{student_data['Name'][best_student_idx]} with total score: {student_totals[best_student_idx]}")

print(f"\nNumPy array operations completed successfully!")
```

2.  **Write a Python program that demonstrates key concepts from the
    following topics: Python data structures, functions, and data
    analysis using libraries like NumPy, Pandas, and Matplotlib. The
    program should:**

```{=html}
<!-- -->
```
a)  Define a function called analyze_sales_data() that accepts a list of
    sales figures (integers) and performs the following tasks:

    -   Calculate and return the total, maximum, minimum, and average
        sales from the list.

b)  Create a NumPy array from the given sales figures and perform basic
    statistical operations on the array (sum, mean, median).

c)  Convert the NumPy array into a Pandas DataFrame and create an
    additional column for \"Region\" which is randomly chosen from
    \[\'North\', \'South\', \'East\', \'West\'\].

d)  Plot a bar chart of total sales per region using Matplotlib.

Demonstrate basic error handling by checking if the input list is empty
and raising an appropriate exception.

### Answer

**Comprehensive Python Program for Sales Data Analysis**

```python
import numpy as np           # Import NumPy for numerical operations
import pandas as pd          # Import Pandas for data manipulation
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import random               # Import random for region assignment
from typing import List, Tuple, Dict  # Import for type hints

print("Sales Data Analysis Program")
print("="*50)

# a) Define analyze_sales_data() function with error handling
def analyze_sales_data(sales_list: List[int]) -> Dict[str, float]:
    """
    Analyze sales data and return statistical summary.
    
    Parameters:
    sales_list (List[int]): List of sales figures
    
    Returns:
    Dict[str, float]: Dictionary containing total, max, min, and average sales
    
    Raises:
    ValueError: If the input list is empty
    TypeError: If the input is not a list or contains non-numeric values
    """
    # Error handling: Check if input is a list
    if not isinstance(sales_list, list):
        raise TypeError("Input must be a list of integers")
    
    # Error handling: Check if list is empty
    if len(sales_list) == 0:
        raise ValueError("Sales list cannot be empty")
    
    # Error handling: Check if all elements are numeric
    for i, value in enumerate(sales_list):
        if not isinstance(value, (int, float)):
            raise TypeError(f"All elements must be numeric. Found {type(value)} at index {i}")
    
    # Calculate statistics
    total_sales = sum(sales_list)        # Sum all sales figures
    max_sales = max(sales_list)          # Find maximum sales
    min_sales = min(sales_list)          # Find minimum sales
    avg_sales = total_sales / len(sales_list)  # Calculate average sales
    
    # Create results dictionary
    results = {
        'total': total_sales,
        'maximum': max_sales,
        'minimum': min_sales,
        'average': avg_sales
    }
    
    # Print detailed analysis
    print(f"Sales Data Analysis Results:")
    print(f"  Input data: {sales_list}")
    print(f"  Total Sales: ${total_sales:,}")
    print(f"  Maximum Sales: ${max_sales:,}")
    print(f"  Minimum Sales: ${min_sales:,}")
    print(f"  Average Sales: ${avg_sales:,.2f}")
    print(f"  Number of data points: {len(sales_list)}")
    
    return results

# Test the function with sample data
print("\nStep 1: Testing analyze_sales_data() function")
print("-" * 40)

# Sample sales data
sample_sales = [15000, 22000, 18500, 31000, 27500, 19800, 24000, 29300, 16700, 25600]
print(f"Sample sales data: {sample_sales}")

try:
    # Call the analysis function
    analysis_results = analyze_sales_data(sample_sales)
    print("✓ Function executed successfully!")
    
except Exception as e:
    print(f"✗ Error occurred: {e}")

# Demonstrate error handling
print(f"\nDemonstrating Error Handling:")
print("-" * 40)

# Test with empty list
try:
    empty_result = analyze_sales_data([])
except ValueError as e:
    print(f"✓ Empty list error caught: {e}")

# Test with non-list input
try:
    non_list_result = analyze_sales_data("not a list")
except TypeError as e:
    print(f"✓ Type error caught: {e}")

# Test with non-numeric values
try:
    invalid_data = [1000, 2000, "invalid", 4000]
    invalid_result = analyze_sales_data(invalid_data)
except TypeError as e:
    print(f"✓ Non-numeric error caught: {e}")

# b) Create NumPy array and perform statistical operations
print(f"\n\nStep 2: NumPy Array Statistical Operations")
print("-" * 40)

# Convert sales list to NumPy array
sales_array = np.array(sample_sales)  # Create NumPy array from list
print(f"Original list: {sample_sales}")
print(f"NumPy array: {sales_array}")
print(f"Array shape: {sales_array.shape}")
print(f"Array data type: {sales_array.dtype}")

# Perform statistical operations using NumPy
numpy_sum = np.sum(sales_array)        # Calculate sum using NumPy
numpy_mean = np.mean(sales_array)      # Calculate mean using NumPy
numpy_median = np.median(sales_array)  # Calculate median using NumPy
numpy_std = np.std(sales_array)        # Calculate standard deviation
numpy_var = np.var(sales_array)        # Calculate variance
numpy_min = np.min(sales_array)        # Calculate minimum
numpy_max = np.max(sales_array)        # Calculate maximum

# Display NumPy statistical results
print(f"\nNumPy Statistical Operations:")
print(f"  Sum: ${numpy_sum:,}")
print(f"  Mean: ${numpy_mean:,.2f}")
print(f"  Median: ${numpy_median:,.2f}")
print(f"  Standard Deviation: ${numpy_std:,.2f}")
print(f"  Variance: ${numpy_var:,.2f}")
print(f"  Minimum: ${numpy_min:,}")
print(f"  Maximum: ${numpy_max:,}")

# Additional NumPy operations
percentile_25 = np.percentile(sales_array, 25)  # 25th percentile
percentile_75 = np.percentile(sales_array, 75)  # 75th percentile
print(f"  25th Percentile: ${percentile_25:,.2f}")
print(f"  75th Percentile: ${percentile_75:,.2f}")

# Compare with manual function results
print(f"\nComparison with manual function:")
print(f"  Function total: ${analysis_results['total']:,} | NumPy sum: ${numpy_sum:,}")
print(f"  Function average: ${analysis_results['average']:,.2f} | NumPy mean: ${numpy_mean:,.2f}")
print(f"  Function maximum: ${analysis_results['maximum']:,} | NumPy max: ${numpy_max:,}")
print(f"  Function minimum: ${analysis_results['minimum']:,} | NumPy min: ${numpy_min:,}")

# c) Convert to Pandas DataFrame and add Region column
print(f"\n\nStep 3: Pandas DataFrame Creation and Manipulation")
print("-" * 40)

# Create DataFrame from NumPy array
df = pd.DataFrame(sales_array, columns=['Sales'])  # Create DataFrame with Sales column
print(f"Initial DataFrame shape: {df.shape}")
print(f"Initial DataFrame:")
print(df.head())

# Add Region column with random assignment
regions = ['North', 'South', 'East', 'West']  # Available regions
random.seed(42)  # Set seed for reproducible results

# Method 1: Using random.choice for each row
df['Region'] = [random.choice(regions) for _ in range(len(df))]  # Assign random regions

print(f"\nDataFrame with Region column added:")
print(df)

# Display basic DataFrame information
print(f"\nDataFrame Information:")
print(f"  Shape: {df.shape}")
print(f"  Columns: {list(df.columns)}")
print(f"  Data types:\n{df.dtypes}")

# Display basic statistics
print(f"\nDataFrame Statistics:")
print(df.describe())

# Show region distribution
print(f"\nRegion Distribution:")
region_counts = df['Region'].value_counts()  # Count occurrences of each region
print(region_counts)

# Calculate statistics by region
print(f"\nStatistics by Region:")
region_stats = df.groupby('Region')['Sales'].agg(['count', 'sum', 'mean', 'min', 'max']).round(2)
print(region_stats)

# d) Create bar chart of total sales per region
print(f"\n\nStep 4: Creating Bar Chart Visualization")
print("-" * 40)

# Calculate total sales per region
region_totals = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)  # Group by region and sum
print(f"Total sales by region:")
print(region_totals)

# Create the bar chart
plt.figure(figsize=(12, 8))  # Set figure size

# Create main bar chart
bars = plt.bar(region_totals.index,    # x-axis: region names
              region_totals.values,    # y-axis: total sales
              color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],  # Custom colors
              edgecolor='black',       # Black border around bars
              linewidth=1.5,           # Border thickness
              alpha=0.8)               # Transparency

# Customize the plot
plt.title('Total Sales by Region', fontsize=18, fontweight='bold', pad=20)  # Add title
plt.xlabel('Region', fontsize=14, fontweight='bold')                        # x-axis label
plt.ylabel('Total Sales ($)', fontsize=14, fontweight='bold')               # y-axis label

# Add value labels on top of bars
for bar, value in zip(bars, region_totals.values):
    plt.text(bar.get_x() + bar.get_width()/2,  # x position (center of bar)
             bar.get_height() + 500,            # y position (slightly above bar)
             f'${value:,}',                     # text to display (formatted with commas)
             ha='center',                       # horizontal alignment
             va='bottom',                       # vertical alignment
             fontsize=12,                       # font size
             fontweight='bold')                 # font weight

# Add grid for better readability
plt.grid(True, alpha=0.3, linestyle='--', axis='y')  # Add horizontal grid lines

# Format y-axis to show values in thousands
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Rotate x-axis labels if needed
plt.xticks(rotation=0)  # Keep horizontal for better readability

# Add some styling
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()          # Display the plot

# Additional visualizations
print(f"\nCreating additional visualizations...")

# Create a more comprehensive visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Bar chart of total sales by region
region_totals.plot(kind='bar', ax=ax1, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
ax1.set_title('Total Sales by Region', fontsize=14, fontweight='bold')
ax1.set_xlabel('Region')
ax1.set_ylabel('Total Sales ($)')
ax1.tick_params(axis='x', rotation=45)

# Add value labels
for i, v in enumerate(region_totals.values):
    ax1.text(i, v + 500, f'${v:,}', ha='center', va='bottom', fontweight='bold')

# Plot 2: Pie chart of sales distribution
ax2.pie(region_totals.values, labels=region_totals.index, autopct='%1.1f%%',
        colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'], startangle=90)
ax2.set_title('Sales Distribution by Region', fontsize=14, fontweight='bold')

# Plot 3: Horizontal bar chart of average sales by region
region_avg = df.groupby('Region')['Sales'].mean().sort_values()
region_avg.plot(kind='barh', ax=ax3, color='skyblue', edgecolor='black')
ax3.set_title('Average Sales by Region', fontsize=14, fontweight='bold')
ax3.set_xlabel('Average Sales ($)')

# Plot 4: Scatter plot of sales data with region color coding
region_colors = {'North': '#FF6B6B', 'South': '#4ECDC4', 'East': '#45B7D1', 'West': '#96CEB4'}
for region in regions:
    region_data = df[df['Region'] == region]
    ax4.scatter(region_data.index, region_data['Sales'], 
               label=region, color=region_colors[region], s=60, alpha=0.7)

ax4.set_title('Sales Data Points by Region', fontsize=14, fontweight='bold')
ax4.set_xlabel('Data Point Index')
ax4.set_ylabel('Sales ($)')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Summary and additional analysis
print(f"\n\nSUMMARY AND ADDITIONAL ANALYSIS")
print("="*50)

# Create summary statistics
summary_stats = {
    'Total Data Points': len(df),
    'Total Sales': df['Sales'].sum(),
    'Average Sales': df['Sales'].mean(),
    'Median Sales': df['Sales'].median(),
    'Sales Range': df['Sales'].max() - df['Sales'].min(),
    'Standard Deviation': df['Sales'].std(),
    'Best Performing Region': region_totals.index[0],
    'Worst Performing Region': region_totals.index[-1]
}

print(f"Summary Statistics:")
for key, value in summary_stats.items():
    if isinstance(value, (int, float)) and key not in ['Total Data Points']:
        print(f"  {key}: ${value:,.2f}")
    else:
        print(f"  {key}: {value}")

# Performance analysis by region
print(f"\nDetailed Regional Performance:")
for region in regions:
    region_data = df[df['Region'] == region]['Sales']
    print(f"{region} Region:")
    print(f"  Count: {len(region_data)} sales records")
    print(f"  Total: ${region_data.sum():,}")
    print(f"  Average: ${region_data.mean():,.2f}")
    print(f"  Best Sale: ${region_data.max():,}")
    print(f"  Worst Sale: ${region_data.min():,}")

# Identify top and bottom performers
print(f"\nTop 3 Individual Sales:")
top_sales = df.nlargest(3, 'Sales')
for i, (idx, row) in enumerate(top_sales.iterrows(), 1):
    print(f"  {i}. ${row['Sales']:,} ({row['Region']} Region)")

print(f"\nBottom 3 Individual Sales:")
bottom_sales = df.nsmallest(3, 'Sales')
for i, (idx, row) in enumerate(bottom_sales.iterrows(), 1):
    print(f"  {i}. ${row['Sales']:,} ({row['Region']} Region)")

print(f"\n✓ Sales Data Analysis Program completed successfully!")
print(f"✓ All objectives achieved:")
print(f"  - Function with error handling created and tested")
print(f"  - NumPy statistical operations performed")
print(f"  - Pandas DataFrame created with region assignment")
print(f"  - Multiple visualizations generated")
```

**LAB QUESTION:**

1.  Data are provided with the following arrays representing the scores
    of students in three subjects: Math, Science, and English.

> math_scores = np.array(\[85, 78, 92, 88, 76, 79\])
>
> science_scores = np.array(\[82, 85, 91, 79, 84, 95\])
>
> english_scores = np.array(\[88, 92, 85, 78, 77, 91\])

Write a Python program to perform the following tasks using NumPy:

i\) Create a 2D NumPy array combining the Math, Science, and English
scores of all students.

ii\) Find the mean score for each subject (Math, Science, English) using
the 2D array.

iii\) Calculate the total score of each student by summing their scores
across the three subjects.

iv\) Find the highest total score among all students and the name of the
student with the highest total score. You can assume the students\'
names are:\[\'Alice\', \'Bob\', \'Charlie\', \'David\', \'Eva\',
\'Frank\'\].

### Answer

**Multi-Subject Student Scores Analysis using NumPy**

```python
import numpy as np      # Import NumPy for numerical operations
import pandas as pd     # Import Pandas for data handling
import matplotlib.pyplot as plt  # Import Matplotlib for visualization

print("Multi-Subject Student Scores Analysis")
print("="*50)

# Given data arrays
math_scores = np.array([85, 78, 92, 88, 76, 79])        # Math scores for 6 students
science_scores = np.array([82, 85, 91, 79, 84, 95])     # Science scores for 6 students  
english_scores = np.array([88, 92, 85, 78, 77, 91])     # English scores for 6 students

# Student names as provided
student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']

# Display the input data
print("Input Data:")
print("-" * 20)
print(f"Math scores:    {math_scores}")
print(f"Science scores: {science_scores}")
print(f"English scores: {english_scores}")
print(f"Student names:  {student_names}")

# Verify all arrays have the same length
print(f"\nData validation:")
print(f"Math array length: {len(math_scores)}")
print(f"Science array length: {len(science_scores)}")
print(f"English array length: {len(english_scores)}")
print(f"Number of students: {len(student_names)}")

if len(math_scores) == len(science_scores) == len(english_scores) == len(student_names):
    print("✓ All arrays have matching lengths")
else:
    print("✗ Array lengths don't match!")

print("\n" + "="*60)
print("TASK i) Creating 2D NumPy Array")
print("="*60)

# i) Create a 2D NumPy array combining all subject scores
# Method 1: Using np.array with nested list
scores_2d_method1 = np.array([math_scores, science_scores, english_scores])
print("Method 1 - Using np.array with nested list:")
print(f"Shape: {scores_2d_method1.shape}")  # Should be (3, 6) - 3 subjects, 6 students
print(f"2D Array:\n{scores_2d_method1}")

# Method 2: Using np.vstack (vertical stack)
scores_2d_method2 = np.vstack([math_scores, science_scores, english_scores])
print(f"\nMethod 2 - Using np.vstack:")
print(f"Shape: {scores_2d_method2.shape}")
print(f"2D Array:\n{scores_2d_method2}")

# Method 3: Using np.column_stack (transpose of above)
scores_2d_transposed = np.column_stack([math_scores, science_scores, english_scores])
print(f"\nMethod 3 - Using np.column_stack (students as rows):")
print(f"Shape: {scores_2d_transposed.shape}")  # Should be (6, 3) - 6 students, 3 subjects
print(f"2D Array:\n{scores_2d_transposed}")

# Use the first method for subsequent operations (subjects as rows)
scores_2d = scores_2d_method1
print(f"\nUsing Method 1 for further analysis:")
print(f"Final 2D array shape: {scores_2d.shape}")
print(f"Array representation:")
print(f"Row 0 (Math):    {scores_2d[0]}")
print(f"Row 1 (Science): {scores_2d[1]}")
print(f"Row 2 (English): {scores_2d[2]}")

# Create a labeled version for better understanding
subjects = ['Math', 'Science', 'English']
print(f"\nLabeled view of the 2D array:")
for i, subject in enumerate(subjects):
    print(f"{subject:>8}: {scores_2d[i]}")

print("\n" + "="*60)
print("TASK ii) Finding Mean Score for Each Subject")
print("="*60)

# ii) Find the mean score for each subject using the 2D array
# Calculate mean along axis=1 (across students for each subject)
subject_means = np.mean(scores_2d, axis=1)  # axis=1 means along columns (students)
print("Calculating mean scores for each subject:")
print(f"Using np.mean(scores_2d, axis=1)")
print(f"Result: {subject_means}")

# Display detailed results for each subject
print(f"\nDetailed mean calculations:")
for i, (subject, mean_score) in enumerate(zip(subjects, subject_means)):
    individual_scores = scores_2d[i]  # Get scores for this subject
    manual_mean = np.sum(individual_scores) / len(individual_scores)  # Manual calculation
    print(f"{subject}:")
    print(f"  Scores: {individual_scores}")
    print(f"  Sum: {np.sum(individual_scores)}")
    print(f"  Count: {len(individual_scores)}")
    print(f"  Mean: {mean_score:.2f}")
    print(f"  Manual verification: {manual_mean:.2f}")

# Alternative methods to calculate means
print(f"\nAlternative methods:")
# Method 1: Calculate means individually
math_mean = np.mean(math_scores)
science_mean = np.mean(science_scores)
english_mean = np.mean(english_scores)
print(f"Individual calculations:")
print(f"  Math mean: {math_mean:.2f}")
print(f"  Science mean: {science_mean:.2f}")
print(f"  English mean: {english_mean:.2f}")

# Method 2: Using transposed array
transposed_means = np.mean(scores_2d_transposed, axis=0)  # axis=0 for column means
print(f"Using transposed array: {transposed_means}")

print("\n" + "="*60)
print("TASK iii) Calculating Total Score for Each Student")
print("="*60)

# iii) Calculate the total score of each student
# Sum along axis=0 (across subjects for each student)
student_totals = np.sum(scores_2d, axis=0)  # axis=0 means along rows (subjects)
print("Calculating total scores for each student:")
print(f"Using np.sum(scores_2d, axis=0)")
print(f"Student totals: {student_totals}")

# Display detailed results for each student
print(f"\nDetailed total calculations:")
for i, (name, total) in enumerate(zip(student_names, student_totals)):
    math_score = scores_2d[0, i]      # Math score for student i
    science_score = scores_2d[1, i]   # Science score for student i
    english_score = scores_2d[2, i]   # English score for student i
    manual_total = math_score + science_score + english_score  # Manual calculation
    average = total / 3               # Calculate average
    
    print(f"{name}:")
    print(f"  Math: {math_score}, Science: {science_score}, English: {english_score}")
    print(f"  Total: {total}")
    print(f"  Average: {average:.2f}")
    print(f"  Manual verification: {manual_total}")

# Alternative method using transposed array
alternative_totals = np.sum(scores_2d_transposed, axis=1)
print(f"\nUsing transposed array method: {alternative_totals}")
print(f"Results match: {np.array_equal(student_totals, alternative_totals)}")

print("\n" + "="*60)
print("TASK iv) Finding Highest Total Score and Student")
print("="*60)

# iv) Find the highest total score and corresponding student
highest_total = np.max(student_totals)           # Find maximum total score
best_student_index = np.argmax(student_totals)   # Find index of maximum total
best_student_name = student_names[best_student_index]  # Get student name

print("Finding the best performing student:")
print(f"Student totals: {student_totals}")
print(f"Maximum total score: {highest_total}")
print(f"Index of maximum: {best_student_index}")
print(f"Best student: {best_student_name}")

# Display detailed information about the best student
print(f"\nDetailed information about {best_student_name}:")
print(f"  Math score: {scores_2d[0, best_student_index]}")
print(f"  Science score: {scores_2d[1, best_student_index]}")
print(f"  English score: {scores_2d[2, best_student_index]}")
print(f"  Total score: {highest_total}")
print(f"  Average score: {highest_total / 3:.2f}")

# Find and display rankings
student_rankings = np.argsort(student_totals)[::-1]  # Sort indices in descending order
print(f"\nComplete student rankings:")
for rank, student_idx in enumerate(student_rankings, 1):
    name = student_names[student_idx]
    total = student_totals[student_idx]
    average = total / 3
    print(f"  {rank}. {name}: {total} points (avg: {average:.2f})")

print("\n" + "="*60)
print("ADDITIONAL ANALYSIS")
print("="*60)

# Additional statistical analysis
print("Additional Statistical Analysis:")

# Overall statistics
all_scores_flat = scores_2d.flatten()  # Flatten 2D array to 1D
print(f"\nOverall statistics across all subjects and students:")
print(f"  Total number of scores: {len(all_scores_flat)}")
print(f"  Overall mean: {np.mean(all_scores_flat):.2f}")
print(f"  Overall median: {np.median(all_scores_flat):.2f}")
print(f"  Overall std deviation: {np.std(all_scores_flat):.2f}")
print(f"  Overall min score: {np.min(all_scores_flat)}")
print(f"  Overall max score: {np.max(all_scores_flat)}")

# Subject analysis
print(f"\nSubject analysis:")
for i, subject in enumerate(subjects):
    subject_scores = scores_2d[i]
    print(f"{subject}:")
    print(f"  Mean: {np.mean(subject_scores):.2f}")
    print(f"  Std Dev: {np.std(subject_scores):.2f}")
    print(f"  Min: {np.min(subject_scores)}")
    print(f"  Max: {np.max(subject_scores)}")
    print(f"  Range: {np.max(subject_scores) - np.min(subject_scores)}")

# Find best and worst performers in each subject
print(f"\nBest performers by subject:")
for i, subject in enumerate(subjects):
    best_idx = np.argmax(scores_2d[i])
    best_score = scores_2d[i, best_idx]
    print(f"  {subject}: {student_names[best_idx]} ({best_score} points)")

print(f"\nWorst performers by subject:")
for i, subject in enumerate(subjects):
    worst_idx = np.argmin(scores_2d[i])
    worst_score = scores_2d[i, worst_idx]
    print(f"  {subject}: {student_names[worst_idx]} ({worst_score} points)")

# Create visualization
print(f"\nCreating visualizations...")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Bar chart of student total scores
ax1.bar(student_names, student_totals, color='skyblue', edgecolor='black')
ax1.set_title('Total Scores by Student', fontsize=14, fontweight='bold')
ax1.set_ylabel('Total Score')
ax1.tick_params(axis='x', rotation=45)
# Add value labels
for i, (name, total) in enumerate(zip(student_names, student_totals)):
    ax1.text(i, total + 5, str(total), ha='center', va='bottom', fontweight='bold')

# Plot 2: Bar chart of subject means
ax2.bar(subjects, subject_means, color=['#FF6B6B', '#4ECDC4', '#45B7D1'], edgecolor='black')
ax2.set_title('Average Scores by Subject', fontsize=14, fontweight='bold')
ax2.set_ylabel('Average Score')
# Add value labels
for i, (subject, mean) in enumerate(zip(subjects, subject_means)):
    ax2.text(i, mean + 1, f'{mean:.1f}', ha='center', va='bottom', fontweight='bold')

# Plot 3: Heatmap of scores
im = ax3.imshow(scores_2d, cmap='YlOrRd', aspect='auto')
ax3.set_title('Score Heatmap (Subjects vs Students)', fontsize=14, fontweight='bold')
ax3.set_xlabel('Students')
ax3.set_ylabel('Subjects')
ax3.set_xticks(range(len(student_names)))
ax3.set_xticklabels(student_names, rotation=45)
ax3.set_yticks(range(len(subjects)))
ax3.set_yticklabels(subjects)
# Add score annotations
for i in range(len(subjects)):
    for j in range(len(student_names)):
        ax3.text(j, i, str(scores_2d[i, j]), ha='center', va='center', 
                color='white', fontweight='bold')

# Plot 4: Individual student performance
x = np.arange(len(subjects))
width = 0.1
for i, (name, color) in enumerate(zip(student_names, 
                                     ['red', 'blue', 'green', 'orange', 'purple', 'brown'])):
    student_scores = scores_2d[:, i]
    ax4.bar(x + i*width, student_scores, width, label=name, color=color, alpha=0.7)

ax4.set_title('Individual Performance by Subject', fontsize=14, fontweight='bold')
ax4.set_xlabel('Subjects')
ax4.set_ylabel('Scores')
ax4.set_xticks(x + width * 2.5)
ax4.set_xticklabels(subjects)
ax4.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()

# Create a comprehensive summary DataFrame
print(f"\nCreating comprehensive summary DataFrame:")
summary_df = pd.DataFrame(scores_2d_transposed, 
                         columns=subjects, 
                         index=student_names)
summary_df['Total'] = student_totals
summary_df['Average'] = student_totals / 3
summary_df = summary_df.round(2)

print(f"\nSummary DataFrame:")
print(summary_df)

# Final summary
print(f"\n" + "="*60)
print("FINAL SUMMARY")
print("="*60)
print(f"✓ 2D Array created with shape: {scores_2d.shape}")
print(f"✓ Subject means calculated: Math={subject_means[0]:.2f}, Science={subject_means[1]:.2f}, English={subject_means[2]:.2f}")
print(f"✓ Student totals calculated: {student_totals}")
print(f"✓ Best student identified: {best_student_name} with {highest_total} points")
print(f"✓ Complete analysis with visualizations completed!")
```

**Unit 1:**

Create an Employee dataset for an organization. The data needs to be
analysed. Load the given dataset into a Pandas DataFrame. Perform group
by operations and calculate summary statistics.

Define data and what are the types of data. Display all the rows in the
dataset. Explain how the DataFrame object can give more information
about the data set. Also explain the various approaches in sorting and
filtering methods to be performed on a Panda dataframe. Apply those
various techniques in the given below dataset and derive the values.

Also mention how to get the statistical analysis of the given data.

  --------------------- -------------- ------------------ ----------------
  **StrengthFactor**    **PriceReg**   **ReleaseYear**    **ItemCount**

  682743                44.99          2015               8

  1016014               24.81          2005               39

  340464                46             2013               34

  334011                100            2006               20

  1287938               121.95         2010               28

  1783153               132            2011               33

  2314801               95.95          2010               33

  721111                207.8          2011               57

  436667                119.81         2008               36

  6652211               49.95          2004               19
  --------------------- -------------- ------------------ ----------------

### Answer

**Comprehensive Data Analysis with Pandas DataFrame**

```python
import pandas as pd          # Import Pandas for data analysis
import numpy as np           # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for visualization
import seaborn as sns        # Import Seaborn for advanced visualization

print("Comprehensive Pandas DataFrame Analysis")
print("="*60)

# PART 1: DATA DEFINITION AND TYPES
print("\nPART 1: DATA DEFINITION AND TYPES")
print("-"*40)

print("What is Data?")
print("Data refers to facts, figures, or information that can be processed, analyzed, and interpreted.")
print("Data can exist in various formats and structures, providing insights when properly analyzed.")

print("\nTypes of Data:")
print("1. QUALITATIVE DATA (Categorical):")
print("   - Nominal: Categories without order (e.g., colors, names, gender)")
print("   - Ordinal: Categories with order (e.g., grades, satisfaction levels)")

print("\n2. QUANTITATIVE DATA (Numerical):")
print("   - Discrete: Countable values (e.g., number of students, items)")
print("   - Continuous: Measurable values (e.g., height, temperature, price)")

print("\n3. DATA STRUCTURES:")
print("   - Structured: Organized format (databases, spreadsheets)")
print("   - Semi-structured: Partially organized (JSON, XML)")
print("   - Unstructured: No specific format (text, images, videos)")

# PART 2: CREATE AND LOAD DATASET
print(f"\n\nPART 2: CREATING AND LOADING DATASET")
print("-"*40)

# Create the dataset from the given table
data = {
    'StrengthFactor': [682743, 1016014, 340464, 334011, 1287938, 
                       1783153, 2314801, 721111, 436667, 6652211],
    'PriceReg': [44.99, 24.81, 46.00, 100.00, 121.95, 
                 132.00, 95.95, 207.80, 119.81, 49.95],
    'ReleaseYear': [2015, 2005, 2013, 2006, 2010, 
                    2011, 2010, 2011, 2008, 2004],
    'ItemCount': [8, 39, 34, 20, 28, 33, 33, 57, 36, 19]
}

# Load data into Pandas DataFrame
df = pd.DataFrame(data)  # Create DataFrame from dictionary
print("Dataset created and loaded into Pandas DataFrame:")
print(f"DataFrame type: {type(df)}")
print(f"DataFrame shape: {df.shape} (rows, columns)")

# Display all rows in the dataset
print("\nDisplaying all rows in the dataset:")
print(df)

# Add index starting from 1 for better readability
df.index = range(1, len(df) + 1)  # Set index from 1 to n
print("\nDataset with custom index (1-based):")
print(df)

# PART 3: DATAFRAME INFORMATION AND INSIGHTS
print(f"\n\nPART 3: DATAFRAME OBJECT INFORMATION")
print("-"*40)

print("How DataFrame object provides information about the dataset:")

# Basic information about the DataFrame
print(f"\n1. BASIC INFORMATION:")
print(f"   Shape: {df.shape}")  # Dimensions of the DataFrame
print(f"   Size: {df.size}")    # Total number of elements
print(f"   Columns: {list(df.columns)}")  # Column names
print(f"   Index: {list(df.index)}")      # Row indices

# Data types information
print(f"\n2. DATA TYPES:")
print(df.dtypes)  # Show data type of each column

# More detailed info
print(f"\n3. DETAILED INFORMATION:")
print(df.info())  # Comprehensive information about DataFrame

# Memory usage
print(f"\n4. MEMORY USAGE:")
memory_usage = df.memory_usage(deep=True)  # Memory usage per column
print(memory_usage)
print(f"Total memory usage: {memory_usage.sum()} bytes")

# Check for missing values
print(f"\n5. MISSING VALUES CHECK:")
missing_values = df.isnull().sum()  # Count missing values per column
print(missing_values)
if missing_values.sum() == 0:
    print("✓ No missing values found in the dataset")

# Unique values count
print(f"\n6. UNIQUE VALUES COUNT:")
for column in df.columns:
    unique_count = df[column].nunique()  # Count unique values
    print(f"   {column}: {unique_count} unique values")

# Data type classification for our dataset
print(f"\n7. DATA TYPE CLASSIFICATION FOR OUR DATASET:")
print(f"   StrengthFactor: Quantitative (Discrete) - Count data")
print(f"   PriceReg: Quantitative (Continuous) - Price data")
print(f"   ReleaseYear: Quantitative (Discrete) - Year data")
print(f"   ItemCount: Quantitative (Discrete) - Count data")

# PART 4: STATISTICAL ANALYSIS
print(f"\n\nPART 4: STATISTICAL ANALYSIS")
print("-"*40)

print("Getting statistical analysis of the data:")

# Descriptive statistics
print(f"\n1. DESCRIPTIVE STATISTICS:")
stats = df.describe()  # Generate descriptive statistics
print(stats)

# Detailed statistics for each column
print(f"\n2. DETAILED STATISTICS BY COLUMN:")
for column in df.columns:
    print(f"\n{column}:")
    series = df[column]  # Get column as Series
    print(f"   Count: {series.count()}")           # Non-null count
    print(f"   Mean: {series.mean():.2f}")         # Average
    print(f"   Median: {series.median():.2f}")     # Middle value
    print(f"   Mode: {series.mode().iloc[0]}")     # Most frequent value
    print(f"   Std Dev: {series.std():.2f}")       # Standard deviation
    print(f"   Variance: {series.var():.2f}")      # Variance
    print(f"   Min: {series.min()}")               # Minimum value
    print(f"   Max: {series.max()}")               # Maximum value
    print(f"   Range: {series.max() - series.min()}")  # Range
    print(f"   25th percentile: {series.quantile(0.25):.2f}")
    print(f"   75th percentile: {series.quantile(0.75):.2f}")
    print(f"   Skewness: {series.skew():.2f}")     # Measure of asymmetry
    print(f"   Kurtosis: {series.kurtosis():.2f}") # Measure of tail heaviness

# Correlation analysis
print(f"\n3. CORRELATION ANALYSIS:")
correlation_matrix = df.corr()  # Calculate correlation matrix
print("Correlation matrix:")
print(correlation_matrix)

# PART 5: SORTING METHODS
print(f"\n\nPART 5: SORTING METHODS")
print("-"*40)

print("Various approaches to sorting DataFrames:")

# 1. Sort by single column
print(f"\n1. SORTING BY SINGLE COLUMN:")
print("a) Sort by PriceReg (ascending):")
sorted_by_price_asc = df.sort_values('PriceReg')  # Sort by price ascending
print(sorted_by_price_asc)

print("\nb) Sort by PriceReg (descending):")
sorted_by_price_desc = df.sort_values('PriceReg', ascending=False)  # Sort descending
print(sorted_by_price_desc)

# 2. Sort by multiple columns
print(f"\n2. SORTING BY MULTIPLE COLUMNS:")
print("Sort by ReleaseYear (asc) then by PriceReg (desc):")
sorted_multi = df.sort_values(['ReleaseYear', 'PriceReg'], 
                             ascending=[True, False])  # Mixed sorting
print(sorted_multi)

# 3. Sort by index
print(f"\n3. SORTING BY INDEX:")
print("Sort by index in descending order:")
sorted_by_index = df.sort_index(ascending=False)  # Sort by index
print(sorted_by_index)

# 4. Sort with custom key
print(f"\n4. SORTING WITH CUSTOM CRITERIA:")
print("Sort by StrengthFactor in descending order:")
sorted_strength = df.sort_values('StrengthFactor', ascending=False)
print(sorted_strength[['StrengthFactor', 'PriceReg']])

# PART 6: FILTERING METHODS
print(f"\n\nPART 6: FILTERING METHODS")
print("-"*40)

print("Various approaches to filtering DataFrames:")

# 1. Simple condition filtering
print(f"\n1. SIMPLE CONDITION FILTERING:")
print("a) Items with PriceReg > 100:")
high_price_filter = df[df['PriceReg'] > 100]  # Filter for high prices
print(high_price_filter)

print("\nb) Items released after 2010:")
recent_items = df[df['ReleaseYear'] > 2010]  # Filter for recent items
print(recent_items)

# 2. Multiple condition filtering
print(f"\n2. MULTIPLE CONDITION FILTERING:")
print("Items with PriceReg > 50 AND ReleaseYear >= 2010:")
complex_filter = df[(df['PriceReg'] > 50) & (df['ReleaseYear'] >= 2010)]
print(complex_filter)

print("\nItems with PriceReg < 50 OR ItemCount > 35:")
or_filter = df[(df['PriceReg'] < 50) | (df['ItemCount'] > 35)]
print(or_filter)

# 3. String/categorical filtering (if applicable)
print(f"\n3. VALUE-BASED FILTERING:")
print("Items from specific years [2010, 2011]:")
year_filter = df[df['ReleaseYear'].isin([2010, 2011])]  # Filter for specific values
print(year_filter)

# 4. Range filtering
print(f"\n4. RANGE FILTERING:")
print("Items with ItemCount between 20 and 40:")
range_filter = df[df['ItemCount'].between(20, 40)]  # Range filtering
print(range_filter)

# 5. Top/Bottom filtering
print(f"\n5. TOP/BOTTOM FILTERING:")
print("Top 3 most expensive items:")
top_expensive = df.nlargest(3, 'PriceReg')  # Top 3 by price
print(top_expensive)

print("\nTop 3 items by StrengthFactor:")
top_strength = df.nlargest(3, 'StrengthFactor')
print(top_strength)

print("\nBottom 3 cheapest items:")
bottom_cheap = df.nsmallest(3, 'PriceReg')  # Bottom 3 by price
print(bottom_cheap)

# 6. Query method
print(f"\n6. QUERY METHOD:")
print("Using query method for complex filtering:")
query_result = df.query('PriceReg > 50 and ItemCount < 35')  # Using query syntax
print(query_result)

# PART 7: GROUP BY OPERATIONS
print(f"\n\nPART 7: GROUP BY OPERATIONS")
print("-"*40)

# Since we don't have natural categorical columns, let's create some
df['PriceCategory'] = df['PriceReg'].apply(lambda x: 'Low' if x < 50 
                                          else 'Medium' if x < 100 
                                          else 'High')  # Create price categories

df['YearDecade'] = (df['ReleaseYear'] // 10) * 10  # Group years by decade

print("Added categorical columns for grouping:")
print(f"PriceCategory: {df['PriceCategory'].unique()}")
print(f"YearDecade: {df['YearDecade'].unique()}")

# Group by operations
print(f"\n1. GROUP BY PRICE CATEGORY:")
price_groups = df.groupby('PriceCategory').agg({
    'StrengthFactor': ['count', 'mean', 'sum'],
    'PriceReg': ['mean', 'min', 'max'],
    'ItemCount': ['mean', 'sum']
}).round(2)
print(price_groups)

print(f"\n2. GROUP BY DECADE:")
decade_groups = df.groupby('YearDecade').agg({
    'PriceReg': 'mean',
    'ItemCount': 'sum',
    'StrengthFactor': 'mean'
}).round(2)
print(decade_groups)

print(f"\n3. MULTIPLE GROUP BY:")
multi_groups = df.groupby(['YearDecade', 'PriceCategory']).agg({
    'PriceReg': 'mean',
    'ItemCount': 'count'
}).round(2)
print(multi_groups)

# PART 8: ADVANCED ANALYSIS
print(f"\n\nPART 8: ADVANCED ANALYSIS AND INSIGHTS")
print("-"*40)

# Identify patterns and insights
print(f"\n1. KEY INSIGHTS:")
max_strength_item = df.loc[df['StrengthFactor'].idxmax()]
min_strength_item = df.loc[df['StrengthFactor'].idxmin()]
most_expensive = df.loc[df['PriceReg'].idxmax()]
cheapest = df.loc[df['PriceReg'].idxmin()]

print(f"Strongest item: Index {max_strength_item.name}, StrengthFactor: {max_strength_item['StrengthFactor']:,}")
print(f"Weakest item: Index {min_strength_item.name}, StrengthFactor: {min_strength_item['StrengthFactor']:,}")
print(f"Most expensive: Index {most_expensive.name}, Price: ${most_expensive['PriceReg']}")
print(f"Cheapest: Index {cheapest.name}, Price: ${cheapest['PriceReg']}")

# Price vs Strength analysis
print(f"\n2. PRICE VS STRENGTH ANALYSIS:")
correlation_price_strength = df['PriceReg'].corr(df['StrengthFactor'])
print(f"Correlation between Price and StrengthFactor: {correlation_price_strength:.3f}")

if correlation_price_strength > 0.5:
    print("Strong positive correlation - Higher strength items tend to be more expensive")
elif correlation_price_strength > 0.3:
    print("Moderate positive correlation - Some relationship between strength and price")
else:
    print("Weak correlation - Price and strength are not strongly related")

# Year trend analysis
print(f"\n3. YEAR TREND ANALYSIS:")
year_stats = df.groupby('ReleaseYear').agg({
    'PriceReg': 'mean',
    'StrengthFactor': 'mean',
    'ItemCount': 'mean'
}).round(2)
print("Average values by release year:")
print(year_stats)

# PART 9: VISUALIZATION
print(f"\n\nPART 9: DATA VISUALIZATION")
print("-"*40)

# Create comprehensive visualizations
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Price distribution
df['PriceReg'].hist(bins=10, ax=ax1, color='skyblue', edgecolor='black')
ax1.set_title('Price Distribution', fontweight='bold')
ax1.set_xlabel('Price ($)')
ax1.set_ylabel('Frequency')

# Plot 2: Scatter plot of Price vs StrengthFactor
ax2.scatter(df['StrengthFactor'], df['PriceReg'], color='red', alpha=0.7, s=60)
ax2.set_title('Price vs Strength Factor', fontweight='bold')
ax2.set_xlabel('Strength Factor')
ax2.set_ylabel('Price ($)')

# Add correlation line
z = np.polyfit(df['StrengthFactor'], df['PriceReg'], 1)
p = np.poly1d(z)
ax2.plot(df['StrengthFactor'], p(df['StrengthFactor']), "r--", alpha=0.8)

# Plot 3: Bar chart of ItemCount by ReleaseYear
year_counts = df.groupby('ReleaseYear')['ItemCount'].sum()
year_counts.plot(kind='bar', ax=ax3, color='green', alpha=0.7)
ax3.set_title('Total Item Count by Release Year', fontweight='bold')
ax3.set_xlabel('Release Year')
ax3.set_ylabel('Total Item Count')
ax3.tick_params(axis='x', rotation=45)

# Plot 4: Box plot of Price by Category
df.boxplot(column='PriceReg', by='PriceCategory', ax=ax4)
ax4.set_title('Price Distribution by Category', fontweight='bold')
ax4.set_xlabel('Price Category')
ax4.set_ylabel('Price ($)')

plt.tight_layout()
plt.show()

# FINAL SUMMARY
print(f"\n\nFINAL SUMMARY")
print("="*60)
print(f"✓ Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns")
print(f"✓ Data types identified and analyzed")
print(f"✓ Statistical analysis completed")
print(f"✓ Multiple sorting methods demonstrated")
print(f"✓ Various filtering approaches applied")
print(f"✓ Group by operations performed")
print(f"✓ Advanced insights extracted")
print(f"✓ Visualizations created")
print(f"\nKey Statistics:")
print(f"  Average Price: ${df['PriceReg'].mean():.2f}")
print(f"  Price Range: ${df['PriceReg'].min():.2f} - ${df['PriceReg'].max():.2f}")
print(f"  Average Strength Factor: {df['StrengthFactor'].mean():,.0f}")
print(f"  Total Items: {df['ItemCount'].sum()}")
print(f"  Year Range: {df['ReleaseYear'].min()} - {df['ReleaseYear'].max()}")
```

**Unit 2:**

Create a dataframe using Python for the given table to analyse the
workout sessions in a Fitness center. Perform data preprocessing on the
given data. Explain the various ways to handle the empty data, wrong
data, wrong format and duplicates.

Explain in detail about exploratory data analysis (EDA) and descriptive
statistics.

  ----------------- ----------------- ----------------- -----------------
  Duration          Pulse             Maxpulse          Calories

  60                110               130               409.1

  60                117               145               479

  60                103               135               340

  45                109               175               282.4

  60                98                124               269

  60                                  147               329.3

  60                100               120               

  240               106               128               345.3

  60                104               132               379.3
  ----------------- ----------------- ----------------- -----------------

Apply these various commands on the given dataset and plot the analysis
results.

### Answer

**Comprehensive Fitness Data Analysis with EDA and Data Preprocessing**

```python
import pandas as pd          # Import Pandas for data manipulation
import numpy as np           # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for basic plotting
import seaborn as sns        # Import Seaborn for advanced visualization
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

print("FITNESS CENTER WORKOUT ANALYSIS")
print("="*60)

# PART 1: CREATE DATAFRAME FROM GIVEN DATA
print("\nPART 1: CREATING DATAFRAME FROM GIVEN DATA")
print("-"*50)

# Create the fitness dataset with missing values as shown in the table
fitness_data = {
    'Duration': [60, 60, 60, 45, 60, 60, 60, 240, 60],
    'Pulse': [110, 117, 103, 109, 98, np.nan, 100, 106, 104],  # Missing value in row 6
    'Maxpulse': [130, 145, 135, 175, 124, 147, 120, 128, 132],
    'Calories': [409.1, 479, 340, 282.4, 269, 329.3, np.nan, 345.3, 379.3]  # Missing value in row 7
}

# Create DataFrame
df_original = pd.DataFrame(fitness_data)
df = df_original.copy()  # Work with a copy to preserve original data

print("Original Fitness Dataset:")
print(df)
print(f"\nDataset shape: {df.shape}")
print(f"Dataset info:")
print(df.info())

# PART 2: EXPLORATORY DATA ANALYSIS (EDA) THEORY
print(f"\n\nPART 2: EXPLORATORY DATA ANALYSIS (EDA) - THEORY")
print("-"*50)

print("WHAT IS EXPLORATORY DATA ANALYSIS (EDA)?")
print("="*45)
print("""
EDA is the process of analyzing and investigating datasets to summarize their main 
characteristics, often using visual methods and statistical techniques.

KEY OBJECTIVES OF EDA:
1. Understand the structure and nature of the data
2. Identify patterns, trends, and relationships
3. Detect outliers and anomalies
4. Check assumptions for statistical modeling
5. Generate hypotheses for further investigation
6. Assess data quality and identify issues

MAIN COMPONENTS OF EDA:
1. DESCRIPTIVE STATISTICS
   - Central tendency (mean, median, mode)
   - Dispersion (variance, standard deviation, range)
   - Distribution shape (skewness, kurtosis)
   - Percentiles and quartiles

2. DATA VISUALIZATION
   - Histograms for distribution analysis
   - Box plots for outlier detection
   - Scatter plots for relationships
   - Bar charts for categorical data
   - Correlation heatmaps

3. DATA QUALITY ASSESSMENT
   - Missing value analysis
   - Duplicate detection
   - Outlier identification
   - Data type validation

4. PATTERN IDENTIFICATION
   - Trends over time
   - Correlations between variables
   - Clustering of similar observations
   - Seasonal patterns
""")

print("\nDESCRIPTIVE STATISTICS - DETAILED EXPLANATION:")
print("="*45)
print("""
MEASURES OF CENTRAL TENDENCY:
• Mean: Average value (sum of all values / count)
• Median: Middle value when data is sorted
• Mode: Most frequently occurring value

MEASURES OF DISPERSION:
• Variance: Average squared deviation from mean
• Standard Deviation: Square root of variance
• Range: Difference between max and min values
• Interquartile Range (IQR): Range of middle 50% of data

MEASURES OF SHAPE:
• Skewness: Measure of asymmetry in distribution
  - Positive skew: Tail extends to the right
  - Negative skew: Tail extends to the left
• Kurtosis: Measure of tail heaviness
  - High kurtosis: Heavy tails, sharp peak
  - Low kurtosis: Light tails, flat peak

PERCENTILES AND QUARTILES:
• 25th Percentile (Q1): Value below which 25% of data falls
• 50th Percentile (Q2/Median): Value below which 50% of data falls
• 75th Percentile (Q3): Value below which 75% of data falls
""")

# PART 3: DATA PREPROCESSING - THEORY AND PRACTICE
print(f"\n\nPART 3: DATA PREPROCESSING - THEORY AND PRACTICE")
print("-"*50)

print("DATA PREPROCESSING THEORY:")
print("="*30)
print("""
Data preprocessing is the process of cleaning and transforming raw data 
to make it suitable for analysis and modeling.

MAIN DATA QUALITY ISSUES:

1. MISSING DATA (Empty/Null Values):
   - Completely missing values (NaN, None, NULL)
   - Implicit missing (empty strings, zeros where inappropriate)
   
   HANDLING STRATEGIES:
   a) Deletion Methods:
      - Listwise deletion: Remove entire rows with missing values
      - Pairwise deletion: Exclude missing values from specific calculations
   
   b) Imputation Methods:
      - Mean imputation: Fill with average value
      - Median imputation: Fill with middle value (robust to outliers)
      - Mode imputation: Fill with most frequent value
      - Forward/Backward fill: Use previous/next valid value
      - Interpolation: Estimate based on neighboring values
      - Advanced: ML-based imputation (KNN, regression)

2. WRONG DATA (Incorrect Values):
   - Typos and data entry errors
   - Values outside logical ranges
   - Inconsistent formatting
   
   HANDLING STRATEGIES:
   - Domain knowledge validation
   - Statistical outlier detection
   - Pattern matching and validation rules
   - Cross-reference with external sources

3. WRONG FORMAT:
   - Incorrect data types (strings vs numbers)
   - Date/time format inconsistencies
   - Unit mismatches
   
   HANDLING STRATEGIES:
   - Data type conversion
   - Standardized formatting
   - Unit normalization

4. DUPLICATES:
   - Exact duplicates: Identical rows
   - Near duplicates: Similar but not identical
   
   HANDLING STRATEGIES:
   - Remove exact duplicates
   - Fuzzy matching for near duplicates
   - Keep first/last occurrence
""")

# Practical Implementation
print(f"\nPRACTICAL IMPLEMENTATION:")
print("="*30)

# Step 1: Identify missing values
print("\n1. MISSING DATA ANALYSIS:")
print("Missing values in each column:")
missing_info = df.isnull().sum()
print(missing_info)

missing_percentage = (df.isnull().sum() / len(df)) * 100
print("\nMissing values percentage:")
for col, percent in missing_percentage.items():
    print(f"   {col}: {percent:.1f}%")

# Visualize missing data pattern
print("\nVisualizing missing data pattern...")
plt.figure(figsize=(12, 6))

# Plot 1: Missing data heatmap
plt.subplot(1, 2, 1)
sns.heatmap(df.isnull(), cbar=True, cmap='viridis', yticklabels=False)
plt.title('Missing Data Pattern')
plt.xlabel('Columns')

# Plot 2: Missing data bar chart
plt.subplot(1, 2, 2)
missing_info.plot(kind='bar', color='coral')
plt.title('Missing Values by Column')
plt.ylabel('Count of Missing Values')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Step 2: Handle missing values with different strategies
print("\n2. HANDLING MISSING VALUES:")

# Create copies for different imputation strategies
df_mean = df.copy()
df_median = df.copy()
df_forward = df.copy()
df_interpolate = df.copy()

# Strategy 1: Mean imputation
print("\nStrategy 1 - Mean Imputation:")
for col in df.select_dtypes(include=[np.number]).columns:
    if df[col].isnull().any():
        mean_val = df[col].mean()
        df_mean[col].fillna(mean_val, inplace=True)
        print(f"   {col}: Filled {df[col].isnull().sum()} missing values with mean {mean_val:.2f}")

# Strategy 2: Median imputation
print("\nStrategy 2 - Median Imputation:")
for col in df.select_dtypes(include=[np.number]).columns:
    if df[col].isnull().any():
        median_val = df[col].median()
        df_median[col].fillna(median_val, inplace=True)
        print(f"   {col}: Filled with median {median_val:.2f}")

# Strategy 3: Forward fill
print("\nStrategy 3 - Forward Fill:")
df_forward = df.fillna(method='ffill')
print("   Forward fill applied to all columns")

# Strategy 4: Interpolation
print("\nStrategy 4 - Interpolation:")
df_interpolate = df.interpolate()
print("   Linear interpolation applied")

# Compare strategies
print("\nComparison of imputation strategies:")
print("\nOriginal data with missing values:")
print(df[['Pulse', 'Calories']])

print("\nAfter mean imputation:")
print(df_mean[['Pulse', 'Calories']])

print("\nAfter median imputation:")
print(df_median[['Pulse', 'Calories']])

print("\nAfter interpolation:")
print(df_interpolate[['Pulse', 'Calories']])

# Use median imputation for further analysis (robust to outliers)
df_clean = df_median.copy()

# Step 3: Detect and handle outliers
print("\n3. OUTLIER DETECTION AND HANDLING:")

# Statistical outlier detection using IQR method
def detect_outliers_iqr(data, column):
    """Detect outliers using Interquartile Range method"""
    Q1 = data[column].quantile(0.25)  # First quartile
    Q3 = data[column].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1                     # Interquartile range
    lower_bound = Q1 - 1.5 * IQR      # Lower boundary
    upper_bound = Q3 + 1.5 * IQR      # Upper boundary
    
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

print("Outlier detection using IQR method:")
for col in df_clean.select_dtypes(include=[np.number]).columns:
    outliers, lower, upper = detect_outliers_iqr(df_clean, col)
    print(f"\n{col}:")
    print(f"   Boundaries: [{lower:.2f}, {upper:.2f}]")
    if len(outliers) > 0:
        print(f"   Found {len(outliers)} outliers:")
        print(f"   Outlier values: {outliers[col].tolist()}")
    else:
        print("   No outliers detected")

# Detect outliers using Z-score method
def detect_outliers_zscore(data, column, threshold=3):
    """Detect outliers using Z-score method"""
    z_scores = np.abs((data[column] - data[column].mean()) / data[column].std())
    outliers = data[z_scores > threshold]
    return outliers

print("\nOutlier detection using Z-score method (threshold=3):")
for col in df_clean.select_dtypes(include=[np.number]).columns:
    outliers = detect_outliers_zscore(df_clean, col)
    if len(outliers) > 0:
        print(f"{col}: Found {len(outliers)} outliers")
        print(f"   Outlier values: {outliers[col].tolist()}")
    else:
        print(f"{col}: No outliers detected")

# Step 4: Handle wrong data formats
print("\n4. DATA FORMAT VALIDATION:")

# Check data types
print("Current data types:")
print(df_clean.dtypes)

# Validate logical ranges for fitness data
print("\nLogical range validation:")
validation_rules = {
    'Duration': (1, 600),      # 1 minute to 10 hours
    'Pulse': (40, 220),        # Reasonable heart rate range
    'Maxpulse': (50, 250),     # Maximum heart rate range
    'Calories': (50, 2000)     # Reasonable calorie burn range
}

for col, (min_val, max_val) in validation_rules.items():
    invalid_data = df_clean[(df_clean[col] < min_val) | (df_clean[col] > max_val)]
    if len(invalid_data) > 0:
        print(f"{col}: Found {len(invalid_data)} values outside range [{min_val}, {max_val}]")
        print(f"   Invalid values: {invalid_data[col].tolist()}")
    else:
        print(f"{col}: All values within expected range [{min_val}, {max_val}] ✓")

# Step 5: Handle duplicates
print("\n5. DUPLICATE DETECTION:")

# Check for exact duplicates
duplicates = df_clean.duplicated()
print(f"Exact duplicates found: {duplicates.sum()}")

if duplicates.sum() > 0:
    print("Duplicate rows:")
    print(df_clean[duplicates])
    
    # Remove duplicates
    df_clean = df_clean.drop_duplicates()
    print(f"After removing duplicates: {df_clean.shape}")
else:
    print("No exact duplicates found ✓")

# PART 4: COMPREHENSIVE EDA IMPLEMENTATION
print(f"\n\nPART 4: COMPREHENSIVE EDA IMPLEMENTATION")
print("-"*50)

# Basic statistics
print("\n1. DESCRIPTIVE STATISTICS:")
desc_stats = df_clean.describe()
print(desc_stats)

# Additional statistics
print("\n2. ADDITIONAL STATISTICAL MEASURES:")
for col in df_clean.select_dtypes(include=[np.number]).columns:
    print(f"\n{col}:")
    print(f"   Skewness: {df_clean[col].skew():.3f}")      # Measure of asymmetry
    print(f"   Kurtosis: {df_clean[col].kurtosis():.3f}")  # Measure of tail heaviness
    print(f"   Coefficient of Variation: {(df_clean[col].std()/df_clean[col].mean()):.3f}")

# Correlation analysis
print("\n3. CORRELATION ANALYSIS:")
correlation_matrix = df_clean.corr()
print(correlation_matrix)

# PART 5: COMPREHENSIVE VISUALIZATION
print(f"\n\nPART 5: COMPREHENSIVE VISUALIZATION")
print("-"*50)

# Create comprehensive visualization
fig = plt.figure(figsize=(20, 15))

# 1. Distribution plots
for i, col in enumerate(df_clean.select_dtypes(include=[np.number]).columns):
    plt.subplot(4, 4, i+1)
    df_clean[col].hist(bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title(f'{col} Distribution')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    
    # Add statistics on plot
    mean_val = df_clean[col].mean()
    median_val = df_clean[col].median()
    plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.1f}')
    plt.axvline(median_val, color='green', linestyle='--', label=f'Median: {median_val:.1f}')
    plt.legend(fontsize=8)

# 2. Box plots for outlier visualization
for i, col in enumerate(df_clean.select_dtypes(include=[np.number]).columns):
    plt.subplot(4, 4, i+5)
    df_clean.boxplot(column=col, ax=plt.gca())
    plt.title(f'{col} Box Plot')
    plt.ylabel(col)

# 3. Correlation heatmap
plt.subplot(4, 4, 9)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, fmt='.2f')
plt.title('Correlation Heatmap')

# 4. Scatter plots for relationships
plt.subplot(4, 4, 10)
plt.scatter(df_clean['Duration'], df_clean['Calories'], alpha=0.7, color='red')
plt.title('Duration vs Calories')
plt.xlabel('Duration (minutes)')
plt.ylabel('Calories')

plt.subplot(4, 4, 11)
plt.scatter(df_clean['Pulse'], df_clean['Maxpulse'], alpha=0.7, color='blue')
plt.title('Pulse vs Max Pulse')
plt.xlabel('Pulse')
plt.ylabel('Max Pulse')

plt.subplot(4, 4, 12)
plt.scatter(df_clean['Pulse'], df_clean['Calories'], alpha=0.7, color='green')
plt.title('Pulse vs Calories')
plt.xlabel('Pulse')
plt.ylabel('Calories')

# 5. Pair plot for all relationships
plt.subplot(4, 4, 13)
# Simple correlation scatter
for i, col1 in enumerate(df_clean.columns):
    for j, col2 in enumerate(df_clean.columns):
        if i < j:
            corr = df_clean[col1].corr(df_clean[col2])
            if abs(corr) > 0.3:  # Only show moderate to strong correlations
                plt.text(i, j, f'{col1} vs {col2}\nr={corr:.2f}', 
                        fontsize=8, ha='center', va='center')

plt.title('Strong Correlations Summary')
plt.axis('off')

# 6. Statistical summary visualization
plt.subplot(4, 4, 14)
stats_summary = df_clean.describe().loc[['mean', 'std', 'min', 'max']]
sns.heatmap(stats_summary, annot=True, fmt='.1f', cmap='Blues')
plt.title('Statistical Summary Heatmap')

# 7. Data quality summary
plt.subplot(4, 4, 15)
quality_data = {
    'Original Missing': [df_original[col].isnull().sum() for col in df_original.columns],
    'After Cleaning': [df_clean[col].isnull().sum() for col in df_clean.columns]
}
quality_df = pd.DataFrame(quality_data, index=df_clean.columns)
quality_df.plot(kind='bar', ax=plt.gca())
plt.title('Data Quality Improvement')
plt.ylabel('Missing Values Count')
plt.xticks(rotation=45)
plt.legend()

# 8. Outlier summary
plt.subplot(4, 4, 16)
outlier_counts = []
for col in df_clean.select_dtypes(include=[np.number]).columns:
    outliers, _, _ = detect_outliers_iqr(df_clean, col)
    outlier_counts.append(len(outliers))

plt.bar(df_clean.select_dtypes(include=[np.number]).columns, outlier_counts, 
        color='orange', alpha=0.7)
plt.title('Outlier Counts by Column')
plt.ylabel('Number of Outliers')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# PART 6: ADVANCED EDA INSIGHTS
print(f"\n\nPART 6: ADVANCED EDA INSIGHTS")
print("-"*50)

print("\n1. KEY FINDINGS:")
print("="*20)

# Find patterns and insights
max_calories_idx = df_clean['Calories'].idxmax()
min_calories_idx = df_clean['Calories'].idxmin()
longest_workout_idx = df_clean['Duration'].idxmax()

print(f"Most intense workout (highest calories):")
print(f"   Index {max_calories_idx}: {df_clean.loc[max_calories_idx, 'Calories']:.1f} calories")
print(f"   Duration: {df_clean.loc[max_calories_idx, 'Duration']} minutes")
print(f"   Pulse: {df_clean.loc[max_calories_idx, 'Pulse']:.0f}")

print(f"\nLeast intense workout (lowest calories):")
print(f"   Index {min_calories_idx}: {df_clean.loc[min_calories_idx, 'Calories']:.1f} calories")
print(f"   Duration: {df_clean.loc[min_calories_idx, 'Duration']} minutes")

print(f"\nLongest workout:")
print(f"   Index {longest_workout_idx}: {df_clean.loc[longest_workout_idx, 'Duration']} minutes")
print(f"   Calories burned: {df_clean.loc[longest_workout_idx, 'Calories']:.1f}")

# Calculate efficiency metrics
df_clean['Calories_per_minute'] = df_clean['Calories'] / df_clean['Duration']
df_clean['Pulse_efficiency'] = df_clean['Calories'] / df_clean['Pulse']

print(f"\n2. EFFICIENCY ANALYSIS:")
print("="*25)
print(f"Average calories per minute: {df_clean['Calories_per_minute'].mean():.2f}")
print(f"Most efficient workout: {df_clean['Calories_per_minute'].max():.2f} cal/min")
print(f"Least efficient workout: {df_clean['Calories_per_minute'].min():.2f} cal/min")

# Workout categorization
def categorize_workout(row):
    """Categorize workout based on duration and intensity"""
    if row['Duration'] >= 120:
        return 'Long Duration'
    elif row['Calories_per_minute'] >= 6:
        return 'High Intensity'
    elif row['Calories_per_minute'] >= 4:
        return 'Medium Intensity'
    else:
        return 'Low Intensity'

df_clean['Workout_Category'] = df_clean.apply(categorize_workout, axis=1)

print(f"\n3. WORKOUT CATEGORIZATION:")
print("="*30)
category_stats = df_clean.groupby('Workout_Category').agg({
    'Duration': ['mean', 'count'],
    'Calories': 'mean',
    'Pulse': 'mean',
    'Calories_per_minute': 'mean'
}).round(2)
print(category_stats)

# Recommendations based on analysis
print(f"\n4. DATA-DRIVEN RECOMMENDATIONS:")
print("="*35)

optimal_duration = df_clean.loc[df_clean['Calories_per_minute'].idxmax(), 'Duration']
optimal_pulse = df_clean.loc[df_clean['Calories_per_minute'].idxmax(), 'Pulse']

print(f"• For maximum calorie burn efficiency:")
print(f"  - Optimal workout duration: {optimal_duration} minutes")
print(f"  - Target pulse rate: {optimal_pulse:.0f} bpm")

high_cal_workouts = df_clean[df_clean['Calories'] > df_clean['Calories'].quantile(0.75)]
print(f"• High calorie workouts (top 25%) characteristics:")
print(f"  - Average duration: {high_cal_workouts['Duration'].mean():.1f} minutes")
print(f"  - Average pulse: {high_cal_workouts['Pulse'].mean():.1f} bpm")
print(f"  - Average max pulse: {high_cal_workouts['Maxpulse'].mean():.1f} bpm")

# Final summary
print(f"\n\nFINAL SUMMARY")
print("="*60)
print(f"✓ Dataset successfully cleaned and preprocessed")
print(f"✓ Missing values handled using median imputation")
print(f"✓ Outliers identified and analyzed")
print(f"✓ Data quality validated and improved")  
print(f"✓ Comprehensive EDA completed with insights")
print(f"✓ Visualizations created for all key aspects")

print(f"\nFinal dataset characteristics:")
print(f"  Rows: {df_clean.shape[0]}")
print(f"  Columns: {df_clean.shape[1]}")
print(f"  Missing values: {df_clean.isnull().sum().sum()}")
print(f"  Duplicates: {df_clean.duplicated().sum()}")

print(f"\nKey statistics:")
print(f"  Average workout duration: {df_clean['Duration'].mean():.1f} minutes")
print(f"  Average calories burned: {df_clean['Calories'].mean():.1f}")
print(f"  Average pulse rate: {df_clean['Pulse'].mean():.1f} bpm")
print(f"  Calorie burn efficiency: {df_clean['Calories_per_minute'].mean():.2f} cal/min")

print(f"\n✓ Analysis complete! Data is ready for further modeling and insights.")
```

**Lab question:**

Consider the given employee salary dataset.

+--------+-------------------+----------+-------------+---------------+
| >      | > **E             | >        | >           | > **Salary**  |
| **ID** | xperience_Years** |  **Age** |  **Gender** |               |
+--------+-------------------+----------+-------------+---------------+
| > 1    | > 5               | > 28     | > Female    | > 250000      |
+--------+-------------------+----------+-------------+---------------+
| > 2    | > 1               | > 21     | > Male      | > 50000       |
+--------+-------------------+----------+-------------+---------------+
| > 3    | > 3               | > 23     | > Female    | > 170000      |
+--------+-------------------+----------+-------------+---------------+
| > 4    | > 2               | > 22     | > Male      | > 25000       |
+--------+-------------------+----------+-------------+---------------+
| > 5    | > 1               | > 17     | > Male      | > 10000       |
+--------+-------------------+----------+-------------+---------------+
| > 6    | > 25              | > 62     | > Male      | > 5001000     |
+--------+-------------------+----------+-------------+---------------+
| > 7    | > 19              | > 54     | > Female    | > 800000      |
+--------+-------------------+----------+-------------+---------------+
| > 8    | > 2               | > 21     | > Female    | > 9000        |
+--------+-------------------+----------+-------------+---------------+
| > 9    | > 10              | > 36     | > Female    | > 61500       |
+--------+-------------------+----------+-------------+---------------+
| > 10   | > 15              | > 54     | > Female    | > 650000      |
+--------+-------------------+----------+-------------+---------------+
| > 11   | > 4               | > 26     | > Female    | > 250000      |
+--------+-------------------+----------+-------------+---------------+

Create a NumPy array and perform basic operations including python
basics and control structures. Perform descriptive statistics analysis
and include the correlation, co-variance as well. Plot the analysis
using matplotlib and seaborn. Differentiate the uniqueness of each of
these libraries.

### Answer

**Comprehensive Employee Salary Analysis with NumPy, Statistics, and Visualization**

```python
import numpy as np           # Import NumPy for numerical operations and arrays
import pandas as pd          # Import Pandas for data manipulation
import matplotlib.pyplot as plt  # Import Matplotlib for basic plotting
import seaborn as sns        # Import Seaborn for advanced statistical visualization
from scipy import stats     # Import SciPy for statistical functions
import warnings
warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

print("COMPREHENSIVE EMPLOYEE SALARY ANALYSIS")
print("="*60)

# PART 1: PYTHON BASICS AND DATA CREATION
print("\nPART 1: PYTHON BASICS AND DATA CREATION")
print("-"*50)

# Create the employee dataset using Python basics
print("Creating employee dataset using Python data structures...")

# Using lists (Python basic data structure)
employee_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # List of employee IDs
experience_years = [5, 1, 3, 2, 1, 25, 19, 2, 10, 15, 4]  # Years of experience
ages = [28, 21, 23, 22, 17, 62, 54, 21, 36, 54, 26]  # Employee ages
genders = ['Female', 'Male', 'Female', 'Male', 'Male', 'Male', 
           'Female', 'Female', 'Female', 'Female', 'Female']  # Gender information
salaries = [250000, 50000, 170000, 25000, 10000, 5001000, 
            800000, 9000, 61500, 650000, 250000]  # Salary information

# Using dictionary (Python basic data structure)
employee_data = {
    'ID': employee_ids,
    'Experience_Years': experience_years,
    'Age': ages,
    'Gender': genders,
    'Salary': salaries
}

print(f"Data created using Python basic structures:")
print(f"  Lists: {len(employee_ids)} employees")
print(f"  Dictionary keys: {list(employee_data.keys())}")

# Create Pandas DataFrame for easier manipulation
df = pd.DataFrame(employee_data)  # Convert dictionary to DataFrame
print(f"\nDataFrame created:")
print(df)

# PART 2: NUMPY ARRAY CREATION AND BASIC OPERATIONS
print(f"\n\nPART 2: NUMPY ARRAY CREATION AND BASIC OPERATIONS")
print("-"*50)

# Create NumPy arrays from the data
print("Creating NumPy arrays...")

# Convert numerical data to NumPy arrays
experience_array = np.array(experience_years)  # Convert experience list to NumPy array
age_array = np.array(ages)                     # Convert age list to NumPy array
salary_array = np.array(salaries)             # Convert salary list to NumPy array

print(f"NumPy arrays created:")
print(f"  Experience array: {experience_array}")
print(f"  Age array: {age_array}")
print(f"  Salary array: {salary_array}")

# Display array properties
print(f"\nArray properties:")
print(f"  Experience array shape: {experience_array.shape}")
print(f"  Experience array dtype: {experience_array.dtype}")
print(f"  Age array shape: {age_array.shape}")
print(f"  Salary array shape: {salary_array.shape}")

# Create 2D NumPy array combining all numerical data
numerical_data_2d = np.array([experience_years, ages, salaries])  # Create 2D array
print(f"\n2D Array (3 x {len(employee_ids)}):")
print(f"Shape: {numerical_data_2d.shape}")
print(f"2D Array:\n{numerical_data_2d}")

# Basic NumPy operations
print(f"\nBasic NumPy Operations:")
print("="*30)

# Array arithmetic operations
print(f"1. Arithmetic Operations:")
print(f"   Experience sum: {np.sum(experience_array)}")
print(f"   Experience mean: {np.mean(experience_array):.2f}")
print(f"   Experience max: {np.max(experience_array)}")
print(f"   Experience min: {np.min(experience_array)}")

# Element-wise operations
experience_doubled = experience_array * 2  # Multiply each element by 2
age_plus_ten = age_array + 10             # Add 10 to each element
print(f"\n2. Element-wise Operations:")
print(f"   Original experience: {experience_array}")
print(f"   Experience doubled: {experience_doubled}")
print(f"   Age plus 10: {age_plus_ten}")

# Boolean operations
high_experience = experience_array > 10    # Create boolean array
young_employees = age_array < 30          # Another boolean array
print(f"\n3. Boolean Operations:")
print(f"   High experience (>10 years): {high_experience}")
print(f"   Young employees (<30): {young_employees}")
print(f"   Count of high experience: {np.sum(high_experience)}")
print(f"   Count of young employees: {np.sum(young_employees)}")

# Array indexing and slicing
print(f"\n4. Array Indexing and Slicing:")
print(f"   First 3 salaries: {salary_array[:3]}")
print(f"   Last 3 ages: {age_array[-3:]}")
print(f"   Every 2nd experience: {experience_array[::2]}")

# PART 3: PYTHON CONTROL STRUCTURES
print(f"\n\nPART 3: PYTHON CONTROL STRUCTURES")
print("-"*50)

print("Demonstrating Python control structures with employee data:")

# 1. Conditional statements (if-elif-else)
print(f"\n1. Conditional Statements - Salary Categories:")
def categorize_salary(salary):
    """Categorize salary using if-elif-else structure"""
    if salary < 50000:          # Low salary condition
        return "Low"
    elif salary < 200000:       # Medium salary condition
        return "Medium"
    elif salary < 500000:       # High salary condition
        return "High"
    else:                       # Very high salary condition
        return "Very High"

# Apply categorization to all salaries
salary_categories = []  # Initialize empty list
for salary in salaries:  # Loop through each salary
    category = categorize_salary(salary)  # Get category
    salary_categories.append(category)    # Add to list
    print(f"   Salary {salary:>8}: {category}")

# 2. For loops with different patterns
print(f"\n2. For Loop Patterns:")
print("a) Simple iteration:")
total_experience = 0  # Initialize counter
for exp in experience_years:  # Iterate through experience values
    total_experience += exp   # Add to total
print(f"   Total experience: {total_experience} years")
 print(f"   Employee {i+1}: Age {age}, Salary ${salary:,} (Young)")

# 4. Nested control structures
print(f"\n4. Nested Control Structures - Gender and Experience Analysis:")
gender_experience_analysis = {'Male': [], 'Female': []}  # Dictionary for analysis

for i in range(len(genders)):  # Outer loop through employees
    gender = genders[i]
    exp = experience_years[i]
    
    if gender in gender_experience_analysis:  # Check if gender key exists
        if exp > 5:  # Inner condition for experienced employees
            gender_experience_analysis[gender].append(f"ID{i+1}:Exp({exp})")

for gender, employees in gender_experience_analysis.items():  # Loop through results
    print(f"   {gender} with >5 years experience: {employees}")

# PART 4: DESCRIPTIVE STATISTICS ANALYSIS
print(f"\n\nPART 4: DESCRIPTIVE STATISTICS ANALYSIS")
print("-"*50)

print("Comprehensive statistical analysis:")

# Basic descriptive statistics
print(f"\n1. BASIC DESCRIPTIVE STATISTICS:")
print("="*35)

def calculate_detailed_stats(data, name):
    """Calculate detailed statistics for a dataset"""
    print(f"\n{name} Statistics:")
    print(f"   Count: {len(data)}")                    # Number of observations
    print(f"   Sum: {np.sum(data):,.0f}")              # Total sum
    print(f"   Mean: {np.mean(data):,.2f}")            # Arithmetic mean
    print(f"   Median: {np.median(data):,.2f}")        # Middle value
    print(f"   Mode: {stats.mode(data)[0][0]:,.0f}")   # Most frequent value
    print(f"   Standard Deviation: {np.std(data, ddof=1):,.2f}")  # Sample std dev
    print(f"   Variance: {np.var(data, ddof=1):,.2f}") # Sample variance
    print(f"   Minimum: {np.min(data):,.0f}")          # Minimum value
    print(f"   Maximum: {np.max(data):,.0f}")          # Maximum value
    print(f"   Range: {np.max(data) - np.min(data):,.0f}")  # Range
    print(f"   25th Percentile (Q1): {np.percentile(data, 25):,.2f}")
    print(f"   75th Percentile (Q3): {np.percentile(data, 75):,.2f}")
    print(f"   IQR: {np.percentile(data, 75) - np.percentile(data, 25):,.2f}")
    print(f"   Skewness: {stats.skew(data):.3f}")      # Measure of asymmetry
    print(f"   Kurtosis: {stats.kurtosis(data):.3f}")  # Measure of tail heaviness
    print(f"   Coefficient of Variation: {(np.std(data)/np.mean(data))*100:.2f}%")

# Calculate statistics for each numerical variable
calculate_detailed_stats(experience_years, "EXPERIENCE")
calculate_detailed_stats(ages, "AGE")
calculate_detailed_stats(salaries, "SALARY")

# PART 5: CORRELATION AND COVARIANCE ANALYSIS
print(f"\n\nPART 5: CORRELATION AND COVARIANCE ANALYSIS")
print("-"*50)

print("Relationship analysis between variables:")

# Create DataFrame for easier correlation analysis
df_numeric = pd.DataFrame({
    'Experience': experience_years,
    'Age': ages,
    'Salary': salaries
})

# Correlation analysis
print(f"\n1. CORRELATION ANALYSIS:")
print("="*25)

# Calculate correlation matrix
correlation_matrix = df_numeric.corr()  # Pearson correlation
print("Correlation Matrix (Pearson):")
print(correlation_matrix)

# Manual correlation calculation for verification
def calculate_correlation(x, y):
    """Manually calculate Pearson correlation coefficient"""
    x_mean = np.mean(x)  # Mean of x
    y_mean = np.mean(y)  # Mean of y
    
    # Calculate numerator and denominators
    numerator = np.sum((x - x_mean) * (y - y_mean))
    x_variance = np.sum((x - x_mean) ** 2)
    y_variance = np.sum((y - y_mean) ** 2)
    
    # Calculate correlation coefficient
    correlation = numerator / np.sqrt(x_variance * y_variance)
    return correlation

print(f"\nManual correlation calculations (verification):")
corr_exp_salary = calculate_correlation(experience_array, salary_array)
corr_age_salary = calculate_correlation(age_array, salary_array)
corr_exp_age = calculate_correlation(experience_array, age_array)

print(f"   Experience vs Salary: {corr_exp_salary:.4f}")
print(f"   Age vs Salary: {corr_age_salary:.4f}")
print(f"   Experience vs Age: {corr_exp_age:.4f}")

# Interpretation of correlations
def interpret_correlation(corr_value, var1, var2):
    """Interpret correlation strength"""
    abs_corr = abs(corr_value)
    if abs_corr >= 0.7:
        strength = "Strong"
    elif abs_corr >= 0.3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    direction = "Positive" if corr_value > 0 else "Negative"
    print(f"   {var1} vs {var2}: {strength} {direction} correlation ({corr_value:.3f})")

print(f"\nCorrelation interpretations:")
interpret_correlation(corr_exp_salary, "Experience", "Salary")
interpret_correlation(corr_age_salary, "Age", "Salary")
interpret_correlation(corr_exp_age, "Experience", "Age")

# Covariance analysis
print(f"\n2. COVARIANCE ANALYSIS:")
print("="*25)

# Calculate covariance matrix
covariance_matrix = np.cov([experience_years, ages, salaries])
print("Covariance Matrix:")
print(covariance_matrix)

# Manual covariance calculation
def calculate_covariance(x, y):
    """Manually calculate covariance"""
    x_mean = np.mean(x)  # Mean of x
    y_mean = np.mean(y)  # Mean of y
    
    # Calculate covariance
    covariance = np.sum((x - x_mean) * (y - y_mean)) / (len(x) - 1)
    return covariance

print(f"\nManual covariance calculations:")
cov_exp_salary = calculate_covariance(experience_array, salary_array)
cov_age_salary = calculate_covariance(age_array, salary_array)
cov_exp_age = calculate_covariance(experience_array, age_array)

print(f"   Experience vs Salary: {cov_exp_salary:,.2f}")
print(f"   Age vs Salary: {cov_age_salary:,.2f}")
print(f"   Experience vs Age: {cov_exp_age:,.2f}")

# PART 6: VISUALIZATION COMPARISON - MATPLOTLIB VS SEABORN
print(f"\n\nPART 6: VISUALIZATION - MATPLOTLIB VS SEABORN COMPARISON")
print("-"*60)

print("MATPLOTLIB vs SEABORN - Key Differences:")
print("="*45)
print("""
MATPLOTLIB:
• Low-level plotting library
• Fine-grained control over every aspect
• More code required for complex plots
• Basic statistical plots require manual calculation
• Highly customizable but verbose
• Better for publication-quality figures with specific requirements

SEABORN:
• High-level statistical visualization library
• Built on top of Matplotlib
• Less code for complex statistical plots
• Automatic statistical calculations and annotations
• Better default aesthetics and themes
• Specialized for statistical data visualization
• Integrates well with Pandas DataFrames

WHEN TO USE WHICH:
• Matplotlib: Custom plots, fine control, publication graphics
• Seaborn: Statistical analysis, quick EDA, beautiful defaults
""")

# Create comprehensive visualizations
print(f"\nCreating comprehensive visualizations...")

# Set up the plotting area
fig = plt.figure(figsize=(20, 16))

# MATPLOTLIB EXAMPLES
print(f"\nMATTLOTLIB Examples:")

# 1. Basic histogram with Matplotlib
plt.subplot(4, 4, 1)
plt.hist(salaries, bins=8, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Salary Distribution (Matplotlib)', fontweight='bold')
plt.xlabel('Salary ($)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# 2. Scatter plot with Matplotlib
plt.subplot(4, 4, 2)
plt.scatter(experience_years, salaries, color='red', alpha=0.7, s=60)
plt.title('Experience vs Salary (Matplotlib)', fontweight='bold')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary ($)')
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(experience_years, salaries, 1)
p = np.poly1d(z)
plt.plot(experience_years, p(experience_years), "r--", alpha=0.8)

# 3. Bar plot with Matplotlib
plt.subplot(4, 4, 3)
gender_counts = df['Gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values, color=['pink', 'lightblue'])
plt.title('Gender Distribution (Matplotlib)', fontweight='bold')
plt.xlabel('Gender')
plt.ylabel('Count')

# 4. Box plot with Matplotlib (manual calculation)
plt.subplot(4, 4, 4)
plt.boxplot([salaries], labels=['Salary'])
plt.title('Salary Box Plot (Matplotlib)', fontweight='bold')
plt.ylabel('Salary ($)')

# SEABORN EXAMPLES
print(f"SEABORN Examples:")

# 5. Histogram with Seaborn
plt.subplot(4, 4, 5)
sns.histplot(data=df, x='Salary', bins=8, kde=True)
plt.title('Salary Distribution (Seaborn)', fontweight='bold')

# 6. Scatter plot with Seaborn
plt.subplot(4, 4, 6)
sns.scatterplot(data=df, x='Experience_Years', y='Salary', hue='Gender', s=80)
plt.title('Experience vs Salary (Seaborn)', fontweight='bold')

# 7. Bar plot with Seaborn
plt.subplot(4, 4, 7)
sns.countplot(data=df, x='Gender', palette='Set2')
plt.title('Gender Distribution (Seaborn)', fontweight='bold')

# 8. Box plot with Seaborn
plt.subplot(4, 4, 8)
sns.boxplot(data=df, y='Salary')
plt.title('Salary Box Plot (Seaborn)', fontweight='bold')

# ADVANCED SEABORN VISUALIZATIONS
print(f"Advanced Seaborn Features:")

# 9. Correlation heatmap
plt.subplot(4, 4, 9)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.3f')
plt.title('Correlation Heatmap (Seaborn)', fontweight='bold')

# 10. Pair plot (partial)
plt.subplot(4, 4, 10)
# Since we can't fit full pairplot, show one relationship with regression
sns.regplot(data=df, x='Age', y='Salary', scatter_kws={'alpha':0.7})
plt.title('Age vs Salary with Regression (Seaborn)', fontweight='bold')

# 11. Violin plot
plt.subplot(4, 4, 11)
df['Salary_Category'] = df['Salary'].apply(categorize_salary)
sns.violinplot(data=df, x='Gender', y='Salary', palette='Set1')
plt.title('Salary by Gender (Violin Plot)', fontweight='bold')

# 12. Strip plot
plt.subplot(4, 4, 12)
sns.stripplot(data=df, x='Gender', y='Experience_Years', 
              size=8, alpha=0.7, jitter=True)
plt.title('Experience by Gender (Strip Plot)', fontweight='bold')

# MATPLOTLIB ADVANCED CUSTOMIZATION
print(f"Advanced Matplotlib Customization:")

# 13. Multiple subplots in one
plt.subplot(4, 4, 13)
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))
# This creates a subplot within subplot for demonstration

# 14. Custom styling
plt.subplot(4, 4, 14)
plt.style.use('seaborn-v0_8')  # Use seaborn style in matplotlib
plt.scatter(ages, salaries, c=experience_years, cmap='viridis', s=100, alpha=0.7)
plt.colorbar(label='Experience (Years)')
plt.title('Multi-dimensional Plot (Matplotlib)', fontweight='bold')
plt.xlabel('Age')
plt.ylabel('Salary ($)')

# 15. Statistical summary plot
plt.subplot(4, 4, 15)
stats_data = [np.mean(salaries), np.median(salaries), np.max(salaries), np.min(salaries)]
stats_labels = ['Mean', 'Median', 'Max', 'Min']
colors = ['gold', 'lightgreen', 'coral', 'lightblue']
plt.bar(stats_labels, stats_data, color=colors, alpha=0.8)
plt.title('Salary Statistics (Matplotlib)', fontweight='bold')
plt.ylabel('Salary ($)')
plt.xticks(rotation=45)

# 16. Combined plot
plt.subplot(4, 4, 16)
# Combine multiple plot types
plt.scatter(experience_years, salaries, alpha=0.6, s=60, c='red', label='Data points')
plt.plot(np.unique(experience_years), 
         np.poly1d(np.polyfit(experience_years, salaries, 1))(np.unique(experience_years)),
         'g--', label='Trend line')
plt.axhline(y=np.mean(salaries), color='blue', linestyle=':', label='Mean salary')
plt.title('Combined Analysis (Matplotlib)', fontweight='bold')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary ($)')
plt.legend(fontsize=8)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# PART 7: DETAILED COMPARATIVE ANALYSIS
print(f"\n\nPART 7: DETAILED COMPARATIVE ANALYSIS")
print("-"*50)

# Create separate comparison plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Comparison 1: Basic histogram
ax1.hist(salaries, bins=8, color='skyblue', edgecolor='black', alpha=0.7)
ax1.set_title('Matplotlib: Basic Histogram\n(Manual styling required)', fontweight='bold')
ax1.set_xlabel('Salary ($)')
ax1.set_ylabel('Frequency')
ax1.grid(True, alpha=0.3)

# Seaborn equivalent
sns.histplot(data=df, x='Salary', bins=8, kde=True, ax=ax2)
ax2.set_title('Seaborn: Enhanced Histogram\n(Automatic KDE, better defaults)', fontweight='bold')

# Comparison 2: Correlation visualization
# Matplotlib version (manual)
corr_matrix_manual = np.corrcoef([experience_years, ages, salaries])
im = ax3.imshow(corr_matrix_manual, cmap='coolwarm', vmin=-1, vmax=1)
ax3.set_xticks([0, 1, 2])
ax3.set_yticks([0, 1, 2])
ax3.set_xticklabels(['Experience', 'Age', 'Salary'])
ax3.set_yticklabels(['Experience', 'Age', 'Salary'])
ax3.set_title('Matplotlib: Manual Correlation\n(More code, manual annotations)', fontweight='bold')

# Add correlation values manually
for i in range(3):
    for j in range(3):
        ax3.text(j, i, f'{corr_matrix_manual[i, j]:.2f}', 
                ha='center', va='center', color='white')

# Seaborn version (automatic)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f', ax=ax4)
ax4.set_title('Seaborn: Automatic Correlation\n(Less code, automatic annotations)', fontweight='bold')

plt.tight_layout()
plt.show()

# PART 8: FINAL INSIGHTS AND SUMMARY
print(f"\n\nPART 8: FINAL INSIGHTS AND SUMMARY")
print("-"*50)

print("KEY FINDINGS FROM ANALYSIS:")
print("="*30)

# Advanced analysis using NumPy and statistics
outlier_threshold = np.mean(salaries) + 2 * np.std(salaries)
outliers = np.where(salary_array > outlier_threshold)[0]

print(f"\n1. STATISTICAL INSIGHTS:")
print(f"   • Average salary: ${np.mean(salaries):,.0f}")
print(f"   • Salary standard deviation: ${np.std(salaries):,.0f}")
print(f"   • Outlier threshold (μ + 2σ): ${outlier_threshold:,.0f}")
print(f"   • Number of outliers: {len(outliers)}")
if len(outliers) > 0:
    print(f"   • Outlier employee IDs: {[i+1 for i in outliers]}")

print(f"\n2. CORRELATION INSIGHTS:")
strongest_corr = np.max(np.abs(correlation_matrix.values[np.triu_indices_from(correlation_matrix.values, k=1)]))
print(f"   • Strongest correlation: {strongest_corr:.3f}")
print(f"   • Experience-Salary correlation: {corr_exp_salary:.3f}")
print(f"   • Age-Salary correlation: {corr_age_salary:.3f}")

print(f"\n3. GENDER ANALYSIS:")
male_salaries = [salaries[i] for i in range(len(genders)) if genders[i] == 'Male']
female_salaries = [salaries[i] for i in range(len(genders)) if genders[i] == 'Female']

print(f"   • Male employees: {len(male_salaries)}")
print(f"   • Female employees: {len(female_salaries)}")
print(f"   • Average male salary: ${np.mean(male_salaries):,.0f}")
print(f"   • Average female salary: ${np.mean(female_salaries):,.0f}")

print(f"\n4. EXPERIENCE ANALYSIS:")
high_exp_employees = np.sum(experience_array > 10)
print(f"   • Employees with >10 years experience: {high_exp_employees}")
print(f"   • Average salary of experienced employees: ${np.mean([salaries[i] for i in range(len(experience_years)) if experience_years[i] > 10]):,.0f}")

print(f"\nLIBRARY COMPARISON SUMMARY:")
print("="*35)
print(f"✓ NumPy: Excellent for numerical operations and array manipulations")
print(f"✓ Matplotlib: Best for custom, publication-quality plots with fine control")
print(f"✓ Seaborn: Superior for statistical visualization with minimal code")
print(f"✓ Pandas: Perfect for data manipulation and analysis")

print(f"\n✓ Analysis completed successfully!")
print(f"  - Dataset: {len(employee_ids)} employees analyzed")
print(f"  - NumPy arrays created and manipulated")
print(f"  - Comprehensive statistics calculated")
print(f"  - Correlations and covariances computed")
print(f"  - Multiple visualization techniques demonstrated")
print(f"  - Library differences clearly illustrated")
```

## Summary

I have successfully created a comprehensive question bank with detailed answers for all the FAI (Foundations of AI) questions. Each answer includes:

1. **Detailed theoretical explanations** for concepts
2. **Complete code examples** with extensive comments explaining each line
3. **Practical implementations** demonstrating the concepts
4. **Multiple approaches** and alternative solutions
5. **Comprehensive analysis** and insights
6. **Visualization examples** using matplotlib and seaborn
7. **Error handling** and best practices

The answers cover:
- **Unit I**: Lists, tuples, sets, NumPy arrays, Pandas operations, data manipulation
- **Unit II**: Data cleaning, EDA, matplotlib plotting, statistical analysis
- **Lab Questions**: Practical implementations with NumPy, statistical analysis, and visualization comparisons

Each answer is structured to provide maximum learning value with detailed code comments explaining the purpose and functionality of every line of code.
