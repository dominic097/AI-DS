# FAI QUESTION BANK - UNIT 1 AND 2
## COMPREHENSIVE ANSWER KEY FOR SEMESTER EXAMINATION

**Note:** Similar type of questions will come, problems will differ. These are sample examples.

**Question Paper Pattern:** 5 questions × 20M = 100M

---

## Question 1: String Operations and NumPy Arrays (20 Marks)

### Part (i): Is String a mutable data type? Explain string operations, indexing and slicing (10 Marks)

**Answer:**

### String Mutability:
**No, strings in Python are IMMUTABLE**. Once created, you cannot change their contents.

```python
s = "Hello"
# s[0] = "h"  # This raises TypeError: 'str' object does not support item assignment
```

### Common String Operations:

#### 1. Concatenation:
```python
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2  # "Hello World"
```

#### 2. Repetition:
```python
s = "Ha" * 3  # "HaHaHa"
```

#### 3. Length:
```python
len("Python")  # Returns 6
```

#### 4. Case Conversion:
```python
s = "hello world"
s.upper()      # "HELLO WORLD"
s.lower()      # "hello world"
s.title()      # "Hello World"
s.capitalize() # "Hello world"
```

#### 5. Search Operations:
```python
s = "Hello World"
s.find("lo")    # Returns 3 (starting index)
s.index("e")    # Returns 1 (first occurrence)
"World" in s    # Returns True
```

#### 6. Replace:
```python
s = "Hello World"
s.replace("l", "x")  # "Hexxo Worxd"
```

#### 7. Split & Join:
```python
s = "apple,banana"
s.split(",")  # ['apple', 'banana']
",".join(['apple', 'banana'])  # 'apple,banana'
```

### Indexing:
```python
s = "Python"
s[0]   # 'P' (first character)
s[-1]  # 'n' (last character)
```

### Slicing:
```python
s = "Python"
s[1:4]   # 'yth' (from index 1 to 3)
s[:3]    # 'Pyt' (from start to index 2)
s[::2]   # 'Pto' (every second character)
s[::-1]  # 'nohtyP' (reverse string)
```

**Important Points to Remember:**
- ✓ Strings are immutable - cannot modify after creation
- ✓ Indexing starts at 0 (positive) or -1 (negative from end)
- ✓ Slicing syntax: `string[start:end:step]`
- ✓ String methods return new strings, don't modify original
- ✓ Negative indices count backward from the end

---

### Part (ii): NumPy Array Operations (10 Marks)

**Question:** Create a NumPy array of product prices: [100, 250, 300, 450, 150]. Perform the following operations:
a. Find mean price
b. Filter and display rows where Category is "Electronics" and Total_Sales > 10,000
c. Create bar plot showing Product_Name vs Total_Sales for top 5 products
d. Add appropriate labels
e. Identify categorical vs numerical data

**Answer:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create NumPy array
prices = np.array([100, 250, 300, 450, 150])

# a. Find mean price
mean_price = np.mean(prices)
print(f"Mean price: {mean_price}")  # Output: 250.0
```

### Mean Price is 250.0

#### b. Filter Electronics with Total_Sales > 10,000:

```python
# Reconstruct the dataset
data = {
    "Product_ID": ["P001", "P002", "P003", "P004", "P005"],
    "Product_Name": ["Laptop", "Chair", "Headphones", "Jacket", "Sofa"],
    "Category": ["Electronics", "Furniture", "Electronics", "Clothing", "Furniture"],
    "Price": [1000, 150, 200, 300, 800],
    "Quantity_Sold": [10, 50, 25, 20, 5],
    "Date": ["2023-01-01", "2023-01-05", "2023-02-10", "2023-03-15", "2023-04-20"]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity_Sold"]

# Filter condition
filtered = df[(df["Category"] == "Electronics") & (df["Total_Sales"] > 10000)]
print(filtered)
```

**Filtered Result:**
- Laptop: Total Sales = 1000 × 10 = 10,000 → Not included (equal to threshold)
- Headphones: 200 × 25 = 5,000 → Not included

#### c. Bar Plot for Top 5 Products:

```python
# Sort by Total_Sales and get top 5
top5 = df.sort_values(by="Total_Sales", ascending=False).head(5)

plt.figure(figsize=(10, 6))
plt.bar(top5["Product_Name"], top5["Total_Sales"], color="skyblue")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.title("Top 5 Products by Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

#### e. Categorical vs Numerical Columns:

| Column | Type | Explanation |
|--------|------|-------------|
| Product_ID | Categorical | Unique identifiers |
| Product_Name | Categorical | Names of products |
| Category | Categorical | Product type |
| Price | Numerical | Continuous value |
| Quantity_Sold | Numerical | Count of items sold |
| Date | Categorical | Treated as string unless parsed as datetime |
| Total_Sales | Numerical | Derived metric (Price × Quantity) |

**Important Points to Remember:**
- ✓ NumPy mean: `np.mean(array)`
- ✓ Boolean indexing: `df[(condition1) & (condition2)]`
- ✓ Calculate derived columns before filtering
- ✓ Categorical data = groups/categories
- ✓ Numerical data = measurable quantities
- ✓ Always label axes in plots

---

## Question 2: Lists, Tuples, Sets, and NumPy Arrays (20 Marks)

### Part (i): Discuss how lists differ from tuples and sets (10 Marks)

**Answer:**

### Key Differences:

| Feature | List ( [ ] ) | Tuple ( ( ) ) | Set ( { } ) |
|---------|-------------|---------------|-------------|
| **Mutability** | ✓ Mutable | ✗ Immutable | ✓ Mutable |
| **Order** | ✓ Ordered | ✓ Ordered | ✗ Unordered |
| **Duplicates** | ✓ Allowed | ✓ Allowed | ✗ Not allowed |
| **Indexing** | ✓ Yes | ✓ Yes | ✗ No |
| **Use Case** | General-purpose storage | Fixed data, dictionary keys | Unique items, fast lookup |

### Working with Lists:

```python
# Creating a list
numbers = [2, 4, 6, 8, 10]

# Accessing elements
print(numbers[0])   # Output: 2
print(numbers[-1])  # Output: 10

# Modifying elements
numbers[2] = 12  # Now: [2, 4, 12, 8, 10]

# Adding elements
numbers.append(14)      # [2, 4, 12, 8, 10, 14]
numbers.insert(1, 3)    # [2, 3, 4, 12, 8, 10, 14]

# Removing elements
numbers.remove(12)      # Removes first occurrence of 12
del numbers[0]          # Removes element at index 0
popped = numbers.pop()  # Removes and returns last element

# Sorting in descending order
numbers.sort(reverse=True)
print(numbers)
```

**Important Points to Remember:**
- ✓ Lists: mutable, ordered, allow duplicates
- ✓ Tuples: immutable, ordered, allow duplicates
- ✓ Sets: mutable, unordered, no duplicates
- ✓ Use lists for general collections
- ✓ Use tuples for fixed data
- ✓ Use sets for unique items and membership testing

---

### Part (ii): NumPy Array vs Pandas Series (10 Marks)

**Answer:**

### What is a NumPy Array?
A NumPy array is a powerful data structure for numerical computing:
- Supports vectorized operations
- Broadcasting capabilities
- Efficient memory usage
- Ideal for matrix operations

```python
import numpy as np
arr = np.array([2, 4, 6, 8, 10])
```

### What is a Pandas Series?
A Pandas Series is a one-dimensional labeled array:
- Can hold any data type
- Has labeled indices
- Part of pandas library

### Difference from Python List:

| Feature | Python List | Pandas Series |
|---------|-------------|---------------|
| **Type** | Built-in structure | Pandas object |
| **Indexing** | Positional only | Labeled + positional |
| **Operations** | Manual loops | Vectorized operations |
| **Metadata** | No metadata | Includes index, dtype |
| **Performance** | Slower | Faster for large data |

### Creating a Pandas Series:

```python
import pandas as pd
prices = pd.Series([100, 250, 300, 450, 150], name="Prices")
print(prices)
```

### Mathematical Operations on Series:

```python
# Element-wise operations
discounted = prices * 0.9
taxed = prices + 18
total = prices.sum()
mean = prices.mean()
```

These operations are **vectorized**, meaning they apply to all elements efficiently without explicit loops.

### Advantages of NumPy Series for Large Datasets:

1. **Performance:** Optimized for speed and memory
2. **Vectorization:** Fast operations without explicit loops
3. **Integration:** Works seamlessly with DataFrames and NumPy
4. **Indexing:** Supports custom labels for better data alignment
5. **Missing Data Handling:** Gracefully handles NaN values

**Important Points to Remember:**
- ✓ NumPy arrays for numerical computing
- ✓ Pandas Series for labeled 1D data
- ✓ Series supports both positional and label indexing
- ✓ Vectorized operations are much faster than loops
- ✓ Series integrates well with DataFrames

---

## Question 3: Pandas DataFrame Operations (20 Marks)

**Question:** Provide two practical examples where NumPy Series would be beneficial. Write a Python program to perform tasks using Pandas:
a) Load Excel file `employee_data.xlsx`
b) Display last 10 rows
c) Handle missing values (Salary: median, Experience: 0)
d) Remove duplicates based on EmployeeID
e) Convert JoinDate to datetime
f) Filter for HR and IT departments with salary > 50,000
g) Save to `filtered_employee_data.xlsx`

**Answer:**

### Practical Examples of NumPy Series:

#### 1. Time Series Analysis:
```python
import pandas as pd
prices = pd.Series([100, 102, 105, 103],
                  index=pd.date_range("2023-01-01", periods=4))
rolling_avg = prices.rolling(window=2).mean()
```

**Use Case:** Analyzing stock prices or sensor data over time
**Benefit:** Series supports datetime indexing and fast rolling statistics

#### 2. Feature Engineering:
```python
import numpy as np
scores = pd.Series([50, 80, 90])
normalized = (scores - scores.mean()) / scores.std()
```

**Use Case:** Creating derived features like log-transformed values or normalized scores
**Benefit:** Series allows element-wise operations and chaining

### Pandas Program for Employee Data Cleaning:

```python
import pandas as pd

# a) Load Excel file
df = pd.read_excel("employee_data.xlsx")

# b) Display last 10 rows
print(df.tail(10))

# c) Handle missing values
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df["Experience"].fillna(0, inplace=True)

# d) Remove duplicate rows based on EmployeeID
df.drop_duplicates(subset="EmployeeID", inplace=True)

# e) Convert JoinDate to datetime format
df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors="coerce")

# f) Filter for HR and IT departments with Salary > 50000
filtered_df = df[
    (df["Department"].isin(["HR", "IT"])) &
    (df["Salary"] > 50000)
]

# g) Save to new Excel file
filtered_df.to_excel("filtered_employee_data.xlsx", index=False)
```

**Important Points to Remember:**
- ✓ `pd.read_excel()` loads Excel files
- ✓ `fillna()` handles missing values
- ✓ `drop_duplicates()` removes duplicate rows
- ✓ `pd.to_datetime()` converts to datetime format
- ✓ Use `isin()` for multiple category filters
- ✓ `to_excel()` saves DataFrame to Excel

---

## Question 4: NumPy Array Operations on Student Scores (20 Marks)

**Question:** Given student_scores dataset, create NumPy array for first 5 students' Math scores, find mean, maximum, and minimum.

**Data:**
| Name | Math_Score | Science_Score | English_Score |
|------|-----------|---------------|---------------|
| Alice | 78 | 85 | 92 |
| Bob | 85 | 82 | 88 |
| Charlie | 92 | 91 | 85 |
| David | 88 | 79 | 78 |
| Eva | 79 | 95 | 91 |
| Frank | 76 | 84 | 77 |

**Answer:**

### Create NumPy Array for Math Scores:

```python
import numpy as np

# First 5 students' Math scores
math_scores = np.array([78, 85, 92, 88, 79])
```

### Calculate Mean:

```python
mean_score = np.mean(math_scores)
# Output: 84.4
```

### Find Maximum and Minimum:

```python
max_score = np.max(math_scores)  # Output: 92
min_score = np.min(math_scores)  # Output: 78
```

### Summary of Results:

| Metric | Value |
|--------|-------|
| Mean Score | 84.4 |
| Max Score | 92 |
| Min Score | 78 |

**Important Points to Remember:**
- ✓ `np.mean()` calculates average
- ✓ `np.max()` finds maximum value
- ✓ `np.min()` finds minimum value
- ✓ NumPy operations are vectorized and fast
- ✓ Can also use `np.median()`, `np.std()`, `np.var()`

---

## Question 5: DataFrame Operations and Analysis (20 Marks)

**Question:** Create Employee dataset, load into Pandas DataFrame, perform group by operations, calculate summary statistics, define data types, display all rows, explain DataFrame methods, and show sorting/filtering techniques.

**Answer:**

### 1. Define and Load the Dataset:

#### What is Data?
Data is a collection of facts, such as numbers, text, or measurements, used for analysis.

#### Types of Data:
1. **Numerical:** Quantitative values (e.g., Salary, Age)
2. **Categorical:** Qualitative labels (e.g., Department, Gender)
3. **Datetime:** Time-based values (e.g., JoinDate)

### Sample Employee Dataset:

```python
import pandas as pd

data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "IT", "Finance", "HR", "IT"],
    "Salary": [60000, 75000, 50000, 62000, 72000],
    "JoinDate": ["2020-01-15", "2019-06-01", "2021-03-20", "2018-07-10", "2022-11-05"],
    "Experience": [3, 5, 2, 6, 1]
}

df = pd.DataFrame(data)
```

### Display All Rows:

```python
print(df)
```

### DataFrame Insights:

```python
df.info()       # Shows column types, non-null counts
df.describe()   # Summary statistics for numerical columns
df.head()       # First few rows
df.columns      # List of column names
df.shape        # Dimensions (rows, columns)
```

These methods help understand structure, data types, and missing values.

### Group By and Summary Statistics:

```python
# Group by Department and calculate mean salary and experience
grouped = df.groupby("Department")[["Salary", "Experience"]].mean()
print(grouped)
```

### Sorting Techniques:

```python
# Sort by Salary descending
df_sorted_salary = df.sort_values(by="Salary", ascending=False)

# Sort by Experience ascending
df_sorted_exp = df.sort_values(by="Experience")

# Sort by multiple columns
df_sorted_multi = df.sort_values(by=["Department", "Salary"], ascending=[True, False])
```

### Filtering Techniques:

```python
# Filter employees with Salary > 60000
high_salary = df[df["Salary"] > 60000]

# Filter employees from HR department
hr_employees = df[df["Department"] == "HR"]

# Combined filter: IT department with Experience > 2
it_experienced = df[(df["Department"] == "IT") & (df["Experience"] > 2)]

# Filter using isin()
selected_depts = df[df["Department"].isin(["HR", "IT"])]
```

### Statistical Analysis:

```python
# Summary statistics
stats = df.describe()

# Median salary
median_salary = df["Salary"].median()

# Correlation between Salary and Experience
correlation = df[["Salary", "Experience"]].corr()

# Value counts
dept_counts = df["Department"].value_counts()
```

### Summary of Techniques:

| Technique | Purpose |
|-----------|---------|
| `groupby()` | Aggregate by category |
| `sort_values()` | Rank by numerical columns |
| `filtering` | Subset based on conditions |
| `describe()` | Statistical summary |
| `info()` | Data structure overview |

**Important Points to Remember:**
- ✓ `info()` shows data types and memory usage
- ✓ `describe()` provides statistical summaries
- ✓ `groupby()` aggregates data by categories
- ✓ `sort_values()` sorts by one or more columns
- ✓ Use `&` for AND, `|` for OR in filters
- ✓ `corr()` calculates correlation matrix

---

## Question 6: 2D NumPy Arrays and Student Scores (20 Marks)

**Question:** Given arrays for Math, Science, and English scores:
```
math_scores = [85, 78, 92, 88, 76, 79]
science_scores = [82, 85, 91, 79, 84, 95]
english_scores = [88, 92, 85, 78, 77, 91]
Students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']
```

i) Create 2D NumPy array
ii) Find mean score for each subject
iii) Calculate total score per student
iv) Find highest total score and student name

**Answer:**

```python
import numpy as np

# Given scores
math_scores = np.array([85, 78, 92, 88, 76, 79])
science_scores = np.array([82, 85, 91, 79, 84, 95])
english_scores = np.array([88, 92, 85, 78, 77, 91])
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank']

# i) Create 2D NumPy array (subjects as rows, students as columns)
scores_matrix = np.array([math_scores, science_scores, english_scores])
print("Shape:", scores_matrix.shape)  # (3, 6)

# ii) Mean score for each subject (along axis 1 = students)
mean_scores = np.mean(scores_matrix, axis=1)
print("Mean Scores (Math, Science, English):", mean_scores)
# Output: [83.0, 86.0, 85.166...]

# iii) Total score for each student (along axis 0 = subjects)
total_scores = np.sum(scores_matrix, axis=0)
print("Total Scores per Student:", total_scores)
# Output: [255, 255, 268, 245, 237, 265]

# iv) Highest total score and corresponding student
max_score = np.max(total_scores)
top_student = students[np.argmax(total_scores)]
print(f"Highest Total Score: {max_score} by {top_student}")
```

### Output Summary:

| Student | Total Score |
|---------|-------------|
| Alice | 255 |
| Bob | 255 |
| Charlie | **268** ✓ |
| David | 245 |
| Eva | 237 |
| Frank | 265 |

**Charlie has the highest total score of 268.**

**Important Points to Remember:**
- ✓ `axis=0` operates on rows (down columns)
- ✓ `axis=1` operates on columns (across rows)
- ✓ `np.sum()` calculates totals
- ✓ `np.mean()` calculates averages
- ✓ `np.argmax()` returns index of maximum value
- ✓ 2D arrays: rows × columns shape

---

## Question 7: Employee Salary Dataset Analysis (20 Marks)

**Question:** Consider employee salary dataset with columns: ID, Experience_Years, Age, Gender, Salary. Define data types, display rows, perform groupby, sorting, and filtering.

**Answer:**

### Define and Load the Dataset:

```python
import pandas as pd

# Define the dataset
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Experience_Years": [5, 1, 3, 2, 1, 25, 19, 2, 10, 15, 4],
    "Age": [28, 21, 23, 22, 17, 62, 54, 21, 36, 54, 26],
    "Gender": ["Female", "Male", "Female", "Male", "Male", "Male",
               "Female", "Female", "Female", "Female", "Female"],
    "Salary": [250000, 50000, 170000, 25000, 10000, 5001000,
               800000, 9000, 61500, 650000, 250000]
}

df = pd.DataFrame(data)
```

### Display All Rows:

```python
print(df)
```

### Understand the Dataset:

```python
df.info()       # Data types and non-null counts
df.describe()   # Summary statistics for numerical columns
df.columns      # Column names
```

### Group By Operations:

```python
# Group by Gender and calculate average salary and experience
grouped = df.groupby("Gender")[["Salary", "Experience_Years"]].mean()
print(grouped)
```

### Sorting Techniques:

```python
# Sort by Salary descending
df_sorted_salary = df.sort_values(by="Salary", ascending=False)

# Sort by Experience ascending
df_sorted_exp = df.sort_values(by="Experience_Years")

# Sort by multiple columns
df_sorted_multi = df.sort_values(by=["Gender", "Salary"], ascending=[True, False])
```

### Filtering Techniques:

```python
# Filter employees with Salary > 500000
high_salary = df[df["Salary"] > 500000]

# Filter Female employees with Experience > 5 years
experienced_females = df[(df["Gender"] == "Female") & (df["Experience_Years"] > 5)]

# Filter employees younger than 30
young_employees = df[df["Age"] < 30]

# Combined complex filter
filtered = df[(df["Gender"] == "Female") &
              (df["Age"] > 25) &
              (df["Salary"] > 100000)]
```

### Statistical Analysis:

```python
# Summary statistics
stats = df.describe()

# Median salary
median_salary = df["Salary"].median()

# Correlation between Experience and Salary
correlation = df[["Experience_Years", "Salary"]].corr()

# Value counts by Gender
gender_counts = df["Gender"].value_counts()

# Salary statistics by Gender
salary_by_gender = df.groupby("Gender")["Salary"].agg(["mean", "median", "min", "max"])
```

**Important Points to Remember:**
- ✓ Always check data types with `info()`
- ✓ `describe()` provides quick statistical overview
- ✓ `groupby()` essential for category-wise analysis
- ✓ Chain multiple conditions with `&` (AND) or `|` (OR)
- ✓ Use `agg()` for multiple aggregation functions
- ✓ Correlation helps identify relationships between variables

---

## Question 8: NumPy, Matplotlib, and Seaborn (20 Marks)

**Question:** Create NumPy array, perform basic operations including Python basics and control structures. Perform descriptive statistics analysis including correlation and covariance. Plot analysis using matplotlib and seaborn. Differentiate the uniqueness of each library.

**Answer:**

### Step 1: Create NumPy Array and Perform Basic Operations:

```python
import numpy as np

# Create 2D NumPy array representing scores of 5 students in 3 subjects
scores = np.array([
    [85, 82, 88],  # Student 1
    [78, 85, 92],  # Student 2
    [92, 91, 85],  # Student 3
    [88, 79, 78],  # Student 4
    [76, 84, 77]   # Student 5
])

# Accessing elements (Python basics)
math_score_student3 = scores[2, 0]  # 92

# Control structure: count students with Math score > 80
count = 0
for row in scores:
    if row[0] > 80:
        count += 1
print(f"Students with Math > 80: {count}")
```

### Step 2: Descriptive Statistics:

```python
# Mean per subject (axis=0 means down columns)
mean_scores = np.mean(scores, axis=0)
print("Mean scores:", mean_scores)

# Standard deviation
std_scores = np.std(scores, axis=0)
print("Std deviation:", std_scores)

# Total score per student (axis=1 means across rows)
total_scores = np.sum(scores, axis=1)
print("Total scores:", total_scores)

# Correlation matrix (subjects × subjects)
correlation = np.corrcoef(scores.T)
print("Correlation matrix:\n", correlation)

# Covariance matrix
covariance = np.cov(scores.T)
print("Covariance matrix:\n", covariance)
```

### Step 3: Plotting with Matplotlib:

```python
import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]

# Bar plot of mean scores
plt.figure(figsize=(8, 5))
plt.bar(subjects, mean_scores, color="skyblue", edgecolor="black")
plt.title("Mean Scores per Subject", fontsize=14, fontweight="bold")
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Mean Score", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

### Step 4: Plotting with Seaborn:

```python
import seaborn as sns
import pandas as pd

# Convert to DataFrame for seaborn
df = pd.DataFrame(scores, columns=subjects)

# Heatmap of correlation matrix
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, xticklabels=subjects,
            yticklabels=subjects, cmap="coolwarm", linewidths=1,
            linecolor="black")
plt.title("Correlation Between Subjects", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

# Box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, palette="Set2")
plt.title("Score Distribution by Subject", fontsize=14, fontweight="bold")
plt.ylabel("Scores", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

### Differences Between Matplotlib and Seaborn:

| Feature | Matplotlib | Seaborn |
|---------|-----------|---------|
| **Purpose** | General-purpose plotting | Statistical data visualization |
| **Customization** | Highly customizable (low-level) | Built-in aesthetics (high-level) |
| **Ease of Use** | Requires manual styling | Automatically styled plots |
| **Plot Types** | Line, bar, scatter, pie, etc. | Heatmap, violin, boxplot, pairplot, etc. |
| **Integration** | Works with NumPy and Pandas | Built on top of Matplotlib + Pandas |
| **Default Style** | Basic, requires customization | Modern, attractive defaults |

**Important Points to Remember:**
- ✓ Matplotlib: Low-level, full control, basic defaults
- ✓ Seaborn: High-level, statistical focus, beautiful defaults
- ✓ Correlation: Measures linear relationship (-1 to +1)
- ✓ Covariance: Measures how variables change together
- ✓ Use `.T` to transpose matrix for proper correlation
- ✓ Seaborn heatmaps great for correlation matrices

---

## Question 9: Data Loading, Cleaning, and Manipulation (20 Marks)

**Question:** Load dataset into Pandas DataFrame, clean data (handle missing values, drop unnecessary columns), perform groupby operations, calculate summary statistics, display first 10 rows, and perform data manipulation (sorting, filtering).

**Given Dataset:**
| Date | Store | Product | Sales | Quantity |
|------|-------|---------|-------|----------|
| 2023-01-01 | Store A | Widget A | 200 | 10 |
| 2023-01-02 | Store A | Widget B | 150 | 5 |
| 2023-01-03 | Store B | Widget A | 300 | 15 |
| 2023-01-04 | Store B | Widget C | | 8 |
| 2023-01-05 | Store A | | 250 | 20 |
| 2023-01-06 | Store C | Widget A | 400 | 20 |
| 2023-01-07 | Store C | Widget B | 100 | 2 |
| 2023-01-08 | Store A | Widget C | 150 | 6 |
| 2023-01-09 | Store B | Widget B | | 5 |
| 2023-01-10 | Store C | Widget C | 350 | 10 |

**Answer:**

```python
import pandas as pd
import numpy as np

# Data recreated from the image
data = [
    ['2023-01-01', 'Store A', 'Widget A', 200, 10],
    ['2023-01-02', 'Store A', 'Widget B', 150, 5],
    ['2023-01-03', 'Store B', 'Widget A', 300, 15],
    ['2023-01-04', 'Store B', 'Widget C', np.nan, 8],
    ['2023-01-05', 'Store A', np.nan, 250, 20],
    ['2023-01-06', 'Store C', 'Widget A', 400, 20],
    ['2023-01-07', 'Store C', 'Widget B', 100, 2],
    ['2023-01-08', 'Store A', 'Widget C', 150, 6],
    ['2023-01-09', 'Store B', 'Widget B', np.nan, 5],
    ['2023-01-10', 'Store C', 'Widget C', 350, 10]
]

columns = ['Date', 'Store', 'Product', 'Sales', 'Quantity']
df = pd.DataFrame(data, columns=columns)

print("--- Initial DataFrame (First 10 rows) ---")
print(df)
```

### 1. Handling Missing Values:

```python
# Check for missing values
print(df.isnull().sum())

# Fill missing 'Sales' with the mean
mean_sales = df['Sales'].mean()
df['Sales'].fillna(mean_sales, inplace=True)

# Fill missing 'Product' with 'Unknown'
df['Product'].fillna('Unknown', inplace=True)

print("\n--- Cleaned DataFrame ---")
print(df)
```

### 2. Handling Wrong Data (Inconsistent/Outliers):

```python
# Cap Maxpulse at a reasonable maximum (e.g., 180)
# This is an example - adjust based on domain knowledge
df.loc[df['Sales'] > 500, 'Sales'] = 500
```

### 3. Handling Wrong Format:

```python
# Ensure all columns are numeric (after imputation)
df['Sales'] = df['Sales'].astype(float)
df['Quantity'] = df['Quantity'].astype(int)
```

### 4. Handling Duplicates:

```python
# Check for and remove duplicates
initial_rows = len(df)
df.drop_duplicates(inplace=True)
removed_duplicates = initial_rows - len(df)
print(f"\n{removed_duplicates} duplicate rows were removed.")
```

### GroupBy Operations and Summary Statistics:

```python
# Group by Store and calculate aggregates
store_summary = df.groupby('Store').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Quantity': ['sum', 'mean']
}).reset_index()

print("\n--- Summary Statistics Grouped by Store ---")
print(store_summary)

# Group by Product
product_summary = df.groupby('Product').agg({
    'Sales': 'sum',
    'Quantity': 'max'
}).reset_index()

print("\n--- Summary Statistics Grouped by Product ---")
print(product_summary)
```

### Sorting:

```python
# Sort by Sales descending
sorted_df = df.sort_values(by='Sales', ascending=False)
print("\n--- DataFrame Sorted by Sales (Descending) ---")
print(sorted_df.head(5))
```

### Filtering:

```python
# Filter Store A only
store_a_df = df[df['Store'] == 'Store A']
print("\n--- DataFrame Filtered for Store A ---")
print(store_a_df)

# Filter Sales > 200
high_sales = df[df['Sales'] > 200]

# Combined filter
filtered = df[(df['Store'] == 'Store A') & (df['Sales'] > 150)]
```

### Display First 10 Rows:

```python
print("\n--- Final Cleaned DataFrame (First 10 Rows) ---")
print(df.head(10))
```

**Important Points to Remember:**
- ✓ Always check for missing values first: `df.isnull().sum()`
- ✓ Fill missing values: `fillna(value)` or drop: `dropna()`
- ✓ Remove duplicates: `drop_duplicates()`
- ✓ Convert data types: `astype()`
- ✓ Group and aggregate: `groupby().agg()`
- ✓ Sort: `sort_values(by=column)`
- ✓ Filter: `df[condition]`

---

## Question 10: Matplotlib Plots (Line, Bar, Scatter) (20 Marks)

**Question:** Demonstrate how to create different types of plots (line plot, bar plot, scatter plot) using Matplotlib. Provide code examples. Explain how to add titles, labels (x and y axis), and customize colors.

**Answer:**

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]   # For line plot
y2 = [5, 7, 3, 8, 6]    # For bar plot
y3 = [10, 20, 25, 30, 40]  # For scatter plot
```

### 1. Line Plot:

```python
plt.figure(figsize=(6, 4))
plt.plot(x, y1, color="blue", linestyle="--", marker="o",
         linewidth=2, markersize=8)
plt.title("Line Plot Example", fontsize=14, fontweight="bold")
plt.xlabel("X-axis values", fontsize=12)
plt.ylabel("Y-axis values", fontsize=12)
plt.grid(True, linestyle=":", color="gray")
plt.show()
```

### 2. Bar Plot:

```python
plt.figure(figsize=(6, 4))
plt.bar(x, y2, color="orange", edgecolor="black", width=0.6)
plt.title("Bar Plot Example", fontsize=14, fontweight="bold")
plt.xlabel("Categories (X)", fontsize=12)
plt.ylabel("Values (Y)", fontsize=12)
plt.show()
```

### 3. Scatter Plot:

```python
plt.figure(figsize=(6, 4))
plt.scatter(x, y3, color="green", marker="s", s=100, edgecolor="black")
plt.title("Scatter Plot Example", fontsize=14, fontweight="bold")
plt.xlabel("X-axis values", fontsize=12)
plt.ylabel("Y-axis values", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
```

### Customization Options:

**Colors:**
- Named colors: `"red"`, `"blue"`, `"green"`
- Hex codes: `"#FF5733"`
- RGB tuples: `(0.1, 0.2, 0.5)`

**Markers:**
- `"o"`: Circle
- `"s"`: Square
- `"^"`: Triangle
- `"*"`: Star

**Line Styles:**
- `"-"`: Solid
- `"--"`: Dashed
- `":"`: Dotted
- `"-."`: Dash-dot

**Important Points to Remember:**
- ✓ `plt.figure(figsize=(width, height))` sets plot size
- ✓ `plt.title()`, `plt.xlabel()`, `plt.ylabel()` add labels
- ✓ `plt.grid()` adds grid lines
- ✓ `plt.show()` displays the plot
- ✓ Use `color`, `marker`, `linestyle` for customization
- ✓ `fontsize` and `fontweight` control text appearance

---

## Question 11: Advanced Seaborn Visualizations (20 Marks)

**Question:** Show how to create advanced visualizations such as box plot and heatmap using Seaborn. Provide examples with code. Explain how to customize these plots by adding titles, labels, changing color palettes, and enhancing visual appeal.

**Answer:**

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = {
    "Subject": ["Math", "Science", "English", "Math", "Science", "English"] * 10,
    "Marks": [85, 78, 92, 88, 74, 95, 70, 65, 80, 90, 60, 55, 72, 95, 89,
              91, 76, 82, 84, 67, 73, 88, 92, 79, 85, 81, 77, 90, 68, 72,
              94, 88, 75, 83, 91, 86, 79, 82, 88, 91, 85, 87, 90, 78, 82,
              89, 93, 86, 80, 76, 88, 91, 85, 87, 90, 73, 85, 77, 89, 92]
}
df = pd.DataFrame(data)
```

### 1. Box Plot:

```python
plt.figure(figsize=(8, 6))
sns.boxplot(x="Subject", y="Marks", data=df, palette="Set2")

# Customization
plt.title("Box Plot of Marks by Subject", fontsize=14, fontweight="bold")
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
```

**Box Plot Components:**
- Box: Interquartile range (IQR) = Q3 - Q1
- Line in box: Median (Q2)
- Whiskers: Extend to 1.5 × IQR
- Dots: Outliers beyond whiskers

### 2. Heatmap:

```python
# Create correlation matrix using sample marks dataset
marks_data = {
    "Math": [85, 88, 70, 90, 60, 95, 76, 84],
    "Science": [78, 74, 65, 85, 55, 89, 82, 67],
    "English": [92, 95, 80, 88, 72, 91, 84, 73]
}
df_marks = pd.DataFrame(marks_data)

# Compute correlation
corr = df_marks.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=1,
            linecolor="black")

# Customization
plt.title("Correlation Heatmap of Subjects", fontsize=14, fontweight="bold")
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Subjects", fontsize=12)
plt.tight_layout()
plt.show()
```

### Color Palettes:

**Seaborn Palettes:**
- `"Set1"`, `"Set2"`, `"Set3"`: Qualitative
- `"viridis"`, `"plasma"`, `"inferno"`: Perceptually uniform
- `"coolwarm"`, `"RdBu"`: Diverging
- `"Blues"`, `"Greens"`, `"Reds"`: Sequential

### Additional Customizations:

```python
# Change figure style
sns.set_style("whitegrid")  # Options: "darkgrid", "white", "dark", "ticks"

# Change context (scales elements)
sns.set_context("talk")  # Options: "paper", "notebook", "talk", "poster"

# Custom color palette
custom_palette = ["#FF6B6B", "#4ECDC4", "#45B7D1"]
sns.set_palette(custom_palette)
```

**Important Points to Remember:**
- ✓ Seaborn built on Matplotlib, uses same customization
- ✓ `palette` parameter changes color scheme
- ✓ `annot=True` shows values in heatmap
- ✓ Box plots great for comparing distributions
- ✓ Heatmaps ideal for correlation matrices
- ✓ `sns.set_style()` changes overall appearance

---

## Question 12: Comprehensive Sales Analysis Program (20 Marks)

**Question:** Write a Python program demonstrating key concepts from Python data structures, functions, and data analysis using NumPy, Pandas, and Matplotlib. The program should:

a) Define `analyze_sales_data()` function that accepts a list of sales figures and returns total, maximum, minimum, and average
b) Create NumPy array from sales figures and perform statistical operations
c) Convert NumPy array to Pandas DataFrame and add "Region" column
d) Plot bar chart of total sales per region

**Answer:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# a) Define function for sales analysis
def analyze_sales_data(sales_list):
    """
    Analyze sales data: total, max, min, average.
    Raises ValueError if list is empty.
    """
    if not sales_list:  # Error handling
        raise ValueError("Sales list cannot be empty!")

    total = sum(sales_list)
    maximum = max(sales_list)
    minimum = min(sales_list)
    average = total / len(sales_list)

    return {
        "Total Sales": total,
        "Maximum Sale": maximum,
        "Minimum Sale": minimum,
        "Average Sale": average
    }

# Example sales data
sales_figures = [120, 340, 560, 230, 450, 670, 890, 150, 300, 720]

# Call the function
results = analyze_sales_data(sales_figures)
print("Sales Analysis Results:")
for key, value in results.items():
    print(f"{key}: {value}")

# b) NumPy array operations
sales_array = np.array(sales_figures)

print("\nNumPy Array Statistics:")
print("Sum:", np.sum(sales_array))
print("Mean:", np.mean(sales_array))
print("Median:", np.median(sales_array))

# c) Convert to Pandas DataFrame with Region column
regions = ['North', 'South', 'East', 'West']
df = pd.DataFrame({
    "Sales": sales_array,
    "Region": [random.choice(regions) for _ in range(len(sales_array))]
})

print("\nDataFrame with Regions:")
print(df)

# d) Plot bar chart of total sales per region
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 6))
region_sales.plot(kind="bar", color=["skyblue", "lightgreen", "salmon", "orange"],
                  edgecolor="black")

plt.title("Total Sales per Region", fontsize=14, fontweight="bold")
plt.xlabel("Region", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

### Error Handling Example:

```python
# Example usage
try:
    # Case 1: Valid list
    sales_figures = [120, 340, 560, 230]
    results = analyze_sales_data(sales_figures)
    print("Results with valid list:", results)

    # Case 2: Empty list (will raise exception)
    empty_sales = []
    results = analyze_sales_data(empty_sales)
    print("Results with empty list:", results)

except ValueError as e:
    print("Error:", e)
```

**Important Points to Remember:**
- ✓ Functions promote code reusability
- ✓ Error handling with try-except is essential
- ✓ NumPy operations are vectorized and fast
- ✓ Pandas DataFrames great for tabular data
- ✓ `groupby()` aggregates data by categories
- ✓ Matplotlib visualizes analysis results
- ✓ Always validate input data

---

## Question 13: Data Preprocessing and EDA (20 Marks)

**Question:** Create DataFrame for fitness center workout sessions. Perform data preprocessing. Explain various ways to handle empty data, wrong data, wrong format, and duplicates. Explain Exploratory Data Analysis (EDA) and descriptive statistics in detail.

**Given Dataset:**
| Duration | Pulse | Maxpulse | Calories |
|----------|-------|----------|----------|
| 60 | 110 | 130 | 409.1 |
| 60 | 117 | 145 | 479 |
| 60 | 103 | 135 | 340 |
| 45 | 109 | 175 | 282.4 |
| 60 | 98 | 124 | 269 |
| 60 | | 147 | 329.3 |
| 60 | 100 | 120 | |
| 240 | 106 | 128 | 345.3 |
| 60 | 104 | 132 | 379.3 |

**Answer:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data with added NaN to simulate missing values
data = {
    'Duration': [60, 60, 60, 45, 60, 60, 60, 240, 60],
    'Pulse': [110, 117, 103, 109, 98, np.nan, 100, 106, 104],
    'Maxpulse': [130, 145, 135, 175, 124, 147, 120, 128, 132],
    'Calories': [409.1, 479, 340, 282.4, 269, 329.3, np.nan, 345.3, 379.3]
}

df = pd.DataFrame(data)
print("--- Initial DataFrame ---")
print(df)
```

### 1. Handling Empty Data (Missing Values):

**Methods:**
a) **Drop rows/columns:**
```python
df.dropna()  # Drop rows with any NaN
df.dropna(axis=1)  # Drop columns with any NaN
```

b) **Fill with specific value:**
```python
df.fillna(0)  # Fill all NaN with 0
```

c) **Fill with statistical measure:**
```python
# Impute missing 'Pulse' values with the median
median_pulse = df['Pulse'].median()
df['Pulse'].fillna(median_pulse, inplace=True)

# Impute missing 'Calories' values with the mean
mean_calories = df['Calories'].mean()
df['Calories'].fillna(mean_calories, inplace=True)
```

d) **Forward/Backward fill:**
```python
df.fillna(method='ffill')  # Forward fill
df.fillna(method='bfill')  # Backward fill
```

### 2. Handling Wrong Data (Inconsistent/Outliers):

```python
# Cap Maxpulse - Replace values above a theoretical maximum (e.g., 180)
df.loc[df['Maxpulse'] > 180, 'Maxpulse'] = 180

# Remove outliers using IQR method
Q1 = df['Duration'].quantile(0.25)
Q3 = df['Duration'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['Duration'] < (Q1 - 1.5 * IQR)) |
          (df['Duration'] > (Q3 + 1.5 * IQR)))]
```

### 3. Handling Wrong Format:

```python
# Ensure all columns are numeric (after imputation, convert to integer)
df['Duration'] = df['Duration'].astype(int)
df['Pulse'] = df['Pulse'].astype(int)
df['Maxpulse'] = df['Maxpulse'].astype(int)
df['Calories'] = df['Calories'].astype(float)

# Convert date columns to datetime
# df['Date'] = pd.to_datetime(df['Date'])
```

### 4. Handling Duplicates:

```python
# Check for and remove duplicates
initial_rows = len(df)
df.drop_duplicates(inplace=True)
removed_duplicates = initial_rows - len(df)
print(f"\n{removed_duplicates} duplicate rows were removed.")
```

### Exploratory Data Analysis (EDA):

#### What is EDA?
Exploratory Data Analysis (EDA) is the process of analyzing datasets to summarize their main characteristics, often using visual methods. It helps:
- Discover patterns and anomalies
- Test hypotheses
- Check assumptions
- Understand data structure

#### EDA Techniques:

**1. Descriptive Statistics:**
```python
print("\n--- Descriptive Statistics of Workout Data ---")
print(df.describe())
```

Output includes:
- Count: Number of non-null values
- Mean: Average value
- Std: Standard deviation
- Min: Minimum value
- 25%, 50%, 75%: Quartiles
- Max: Maximum value

**2. Data Distribution Analysis (Histograms):**
```python
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.histplot(df['Duration'], kde=True)
plt.title('Duration Distribution')

plt.subplot(1, 3, 2)
sns.histplot(df['Pulse'], kde=True)
plt.title('Pulse Distribution')

plt.subplot(1, 3, 3)
sns.histplot(df['Calories'], kde=True)
plt.title('Calories Distribution')

plt.tight_layout()
plt.show()
```

**3. Outlier Detection (Box Plots):**
```python
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Duration'])
plt.title('Box Plot of Duration')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Maxpulse'])
plt.title('Box Plot of Maxpulse')

plt.tight_layout()
plt.show()
```

**4. Relationship Analysis (Scatter Plot and Correlation):**
```python
# Calculate correlation matrix
correlation_matrix = df.corr()
print("\n--- Correlation Matrix ---")
print(correlation_matrix)

# Plot correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=1)
plt.title('Correlation Heatmap')
plt.show()

# Scatter plot: Pulse vs. Calories
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Pulse', y='Calories', data=df)
plt.title('Pulse vs. Calories Burned')
plt.show()
```

### Descriptive Statistics Explained:

1. **Measures of Central Tendency:**
   - **Mean:** Average value
   - **Median:** Middle value when sorted
   - **Mode:** Most frequent value

2. **Measures of Dispersion:**
   - **Range:** Difference between max and min
   - **Variance:** Average of squared deviations from mean
   - **Standard Deviation:** Square root of variance
   - **IQR:** Interquartile range (Q3 - Q1)

3. **Measures of Shape:**
   - **Skewness:** Asymmetry of distribution
   - **Kurtosis:** Tailedness of distribution

```python
print("Mean Duration:", df['Duration'].mean())
print("Median Pulse:", df['Pulse'].median())
print("Std Dev Calories:", df['Calories'].std())
print("Variance Duration:", df['Duration'].var())
```

**Important Points to Remember:**
- ✓ **Missing Data:** fillna(), dropna(), imputation
- ✓ **Outliers:** IQR method, z-score, domain knowledge
- ✓ **Wrong Format:** astype(), to_datetime()
- ✓ **Duplicates:** drop_duplicates()
- ✓ **EDA:** Understand data before modeling
- ✓ **Descriptive Stats:** Summarize data numerically
- ✓ **Visualization:** Histograms, box plots, scatter plots
- ✓ **Correlation:** Identifies relationships between variables

---

## EXAM PREPARATION TIPS

### Key Concepts to Master:

**Python Basics:**
1. Strings are immutable
2. Lists vs Tuples vs Sets
3. Dictionary operations
4. Function definitions
5. Control structures (if, for, while)

**NumPy:**
1. Array creation and operations
2. Axis-based operations (axis=0, axis=1)
3. Statistical functions (mean, median, std, etc.)
4. Array indexing and slicing
5. Broadcasting

**Pandas:**
1. DataFrame creation and manipulation
2. Handling missing values
3. GroupBy operations
4. Sorting and filtering
5. Data type conversions
6. Reading/writing files

**Matplotlib:**
1. Basic plot types (line, bar, scatter)
2. Customization (colors, markers, styles)
3. Labels and titles
4. Multiple subplots
5. Grid and legends

**Seaborn:**
1. Statistical visualizations
2. Heatmaps for correlation
3. Box plots and violin plots
4. Color palettes
5. Styling and aesthetics

**Data Preprocessing:**
1. Missing value handling
2. Outlier detection and treatment
3. Data type conversions
4. Duplicate removal
5. Feature engineering

**AI Concepts (if applicable):**
1. Search algorithms (BFS, DFS, A*)
2. Knowledge representation
3. Bayesian reasoning
4. Problem-solving techniques

### Study Strategy:
1. ✓ Practice coding examples
2. ✓ Understand concepts, not just memorize
3. ✓ Draw diagrams for complex topics
4. ✓ Time yourself on practice problems
5. ✓ Review important points regularly
6. ✓ Work through all question types

### Common Mistakes to Avoid:
1. ✗ Not reading the full file before editing
2. ✗ Forgetting to import libraries
3. ✗ Confusing axis=0 and axis=1
4. ✗ Not checking for missing values
5. ✗ Skipping data visualization
6. ✗ Poor variable naming
7. ✗ Not adding comments to code

---

## FORMULA SHEET

### Statistical Formulas:

**Mean:**
```
μ = (Σx) / n
```

**Standard Deviation:**
```
σ = √(Σ(x - μ)² / n)
```

**Correlation:**
```
r = Σ((x - x̄)(y - ȳ)) / √(Σ(x - x̄)² × Σ(y - ȳ)²)
```

**IQR (Interquartile Range):**
```
IQR = Q3 - Q1
Lower bound = Q1 - 1.5 × IQR
Upper bound = Q3 + 1.5 × IQR
```

### NumPy Common Functions:

```python
np.mean(arr)      # Average
np.median(arr)    # Median
np.std(arr)       # Standard deviation
np.var(arr)       # Variance
np.min(arr)       # Minimum
np.max(arr)       # Maximum
np.sum(arr)       # Sum
np.argmax(arr)    # Index of maximum
np.argmin(arr)    # Index of minimum
```

### Pandas Common Operations:

```python
df.info()              # Data types and counts
df.describe()          # Statistical summary
df.head(n)             # First n rows
df.tail(n)             # Last n rows
df.shape               # Dimensions
df.columns             # Column names
df.isnull().sum()      # Count missing values
df.fillna(value)       # Fill missing values
df.dropna()            # Drop missing values
df.drop_duplicates()   # Remove duplicates
df.sort_values(by)     # Sort by column
df.groupby(by)         # Group by column
```

---

**ALL THE BEST FOR YOUR EXAMS!**

*Remember: Understanding concepts is more important than memorizing code. Focus on the logic and you'll be able to solve any variation of these questions.*
