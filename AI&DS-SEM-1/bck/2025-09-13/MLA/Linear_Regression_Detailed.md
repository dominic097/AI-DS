# 📈 Linear Regression: Complete Guide with House Price Prediction

## 🎯 Table of Contents
1. [Introduction to Linear Regression](#introduction)
2. [Mathematical Foundation](#mathematical-foundation)
3. [Formula Breakdown](#formula-breakdown)
4. [House Price Prediction Example](#house-price-example)
5. [Step-by-Step Calculation](#step-by-step-calculation)
6. [Implementation and Code](#implementation)

---

## 🔍 Introduction to Linear Regression {#introduction}

**Linear Regression** is one of the most fundamental and widely used algorithms in machine learning and statistics. It models the relationship between a dependent variable (target) and one or more independent variables (features) using a linear equation.

### 📋 **Key Characteristics:**
- **Supervised Learning**: Requires labeled training data
- **Regression Algorithm**: Predicts continuous numerical values
- **Linear Relationship**: Assumes linear relationship between features and target
- **Interpretable**: Easy to understand and explain results
- **Foundation**: Forms the basis for many advanced algorithms

### 🎯 **When to Use Linear Regression:**
- **Continuous target variables**: House prices, sales revenue, temperature
- **Linear relationships**: When features have linear correlation with target
- **Baseline models**: Quick benchmark for more complex algorithms
- **Feature importance**: Understanding which features matter most
- **Prediction intervals**: When you need confidence in predictions

---

## 📐 Mathematical Foundation {#mathematical-foundation}

### 🔢 **Simple Linear Regression Equation:**

The fundamental equation for simple linear regression (one feature) is:

```
y = mx + b
```

Where:
- **y** = Dependent variable (target/output) - what we want to predict
- **x** = Independent variable (feature/input) - what we use to predict
- **m** = Slope of the line - how much y changes for each unit change in x
- **b** = Y-intercept - the value of y when x = 0

### 🎯 **Multiple Linear Regression Equation:**

For multiple features, the equation extends to:

```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
```

Where:
- **β₀** = Intercept term (bias)
- **β₁, β₂, ..., βₙ** = Coefficients for each feature
- **x₁, x₂, ..., xₙ** = Feature values
- **ε** = Error term (residual)

---

## 🧮 Formula Breakdown {#formula-breakdown}

### 📊 **Calculating the Slope (m)**

The slope formula determines how steep the line is:

```
m = [n∑(xy) - ∑x∑y] / [n∑(x²) - (∑x)²]
```

**Step-by-Step Breakdown:**

1. **n** = Number of data points
2. **∑(xy)** = Sum of (x × y) for each data point
3. **∑x** = Sum of all x values
4. **∑y** = Sum of all y values
5. **∑(x²)** = Sum of x² for each data point
6. **(∑x)²** = Square of the sum of x values

**What the slope tells us:**
- **Positive slope**: As x increases, y increases
- **Negative slope**: As x increases, y decreases
- **Steep slope**: Strong relationship between x and y
- **Flat slope**: Weak relationship between x and y

### 📍 **Calculating the Y-Intercept (b)**

The y-intercept formula finds where the line crosses the y-axis:

```
b = [∑y - m∑x] / n
```

**Step-by-Step Breakdown:**

1. **∑y** = Sum of all y values
2. **m** = Slope (calculated above)
3. **∑x** = Sum of all x values
4. **n** = Number of data points

**Alternative formula:**
```
b = ȳ - m × x̄
```

Where:
- **ȳ** = Mean of y values
- **x̄** = Mean of x values

**What the intercept tells us:**
- **The baseline value** when all features are zero
- **Starting point** of our prediction line
- **May or may not** have real-world meaning depending on context

---

## 🏠 House Price Prediction Example {#house-price-example}

### 📊 **Dataset Overview**

Let's work with the house price prediction example shown in your image:

| House Size (Sq ft) | House Price ($) |
|-------------------|-----------------|
| 500               | 150,000         |
| 800               | 200,000         |
| 1000              | 250,000         |
| 1200              | 280,000         |
| 1500              | 320,000         |

### 🎯 **Problem Statement:**
**Predict house prices based on house size using linear regression**

**Assumptions:**
- Linear relationship between house size and price
- Larger houses generally cost more
- Relationship is consistent across the dataset

### 📈 **Visual Interpretation:**
From the scatter plot, we can observe:
- **Positive correlation**: As house size increases, price increases
- **Linear trend**: Points roughly follow a straight line
- **Some variation**: Not all points lie exactly on the line (natural variation)

---

## 🔢 Step-by-Step Calculation {#step-by-step-calculation}

Let's manually calculate the linear regression coefficients using our house price data:

### **Step 1: Organize the Data**

| x (Size) | y (Price) | xy        | x²      |
|----------|-----------|-----------|---------|
| 500      | 150,000   | 75,000,000| 250,000 |
| 800      | 200,000   | 160,000,000| 640,000 |
| 1000     | 250,000   | 250,000,000| 1,000,000|
| 1200     | 280,000   | 336,000,000| 1,440,000|
| 1500     | 320,000   | 480,000,000| 2,250,000|

### **Step 2: Calculate Required Sums**

```
n = 5 (number of data points)
∑x = 500 + 800 + 1000 + 1200 + 1500 = 5,000
∑y = 150,000 + 200,000 + 250,000 + 280,000 + 320,000 = 1,200,000
∑(xy) = 75,000,000 + 160,000,000 + 250,000,000 + 336,000,000 + 480,000,000 = 1,301,000,000
∑(x²) = 250,000 + 640,000 + 1,000,000 + 1,440,000 + 2,250,000 = 5,580,000
(∑x)² = 5,000² = 25,000,000
```

### **Step 3: Calculate the Slope (m)**

```
m = [n∑(xy) - ∑x∑y] / [n∑(x²) - (∑x)²]

Numerator = n∑(xy) - ∑x∑y
         = 5 × 1,301,000,000 - 5,000 × 1,200,000
         = 6,505,000,000 - 6,000,000,000
         = 505,000,000

Denominator = n∑(x²) - (∑x)²
            = 5 × 5,580,000 - 25,000,000
            = 27,900,000 - 25,000,000
            = 2,900,000

m = 505,000,000 / 2,900,000 = 174.14 (approximately)
```

**Interpretation**: For every 1 square foot increase in house size, the price increases by approximately $174.14

### **Step 4: Calculate the Y-Intercept (b)**

```
b = [∑y - m∑x] / n
  = [1,200,000 - 174.14 × 5,000] / 5
  = [1,200,000 - 870,700] / 5
  = 329,300 / 5
  = 65,860
```

**Interpretation**: The base price of a house (when size = 0) is approximately $65,860. This represents fixed costs like land value, basic structure, etc.

### **Step 5: Final Linear Regression Equation**

```
House Price = 174.14 × House Size + 65,860
```

or in general form:
```
y = 174.14x + 65,860
```

### **Step 6: Making Predictions**

**Example Predictions:**
- **For 900 sq ft house**: Price = 174.14 × 900 + 65,860 = $222,586
- **For 1300 sq ft house**: Price = 174.14 × 1300 + 65,860 = $292,242
- **For 2000 sq ft house**: Price = 174.14 × 2000 + 65,860 = $414,140

---

## 📊 **Model Evaluation Metrics**

### **1. Mean Squared Error (MSE)**
```
MSE = (1/n) × ∑(yᵢ - ŷᵢ)²
```
- Measures average squared difference between actual and predicted values
- Penalizes larger errors more heavily
- Units are squared (price²)

### **2. Root Mean Squared Error (RMSE)**
```
RMSE = √MSE
```
- Square root of MSE
- Same units as the target variable (price)
- Easier to interpret than MSE

### **3. Mean Absolute Error (MAE)**
```
MAE = (1/n) × ∑|yᵢ - ŷᵢ|
```
- Average absolute difference between actual and predicted values
- Less sensitive to outliers than MSE
- Same units as target variable

### **4. R-squared (Coefficient of Determination)**
```
R² = 1 - (SSres/SStot)
```
Where:
- **SSres** = Sum of squares of residuals = ∑(yᵢ - ŷᵢ)²
- **SStot** = Total sum of squares = ∑(yᵢ - ȳ)²

**Interpretation:**
- **R² = 1**: Perfect fit (model explains 100% of variance)
- **R² = 0**: Model is no better than using the mean
- **R² < 0**: Model is worse than using the mean

---

## 🔍 **Assumptions of Linear Regression**

### **1. Linearity**
- The relationship between features and target is linear
- **Check**: Scatter plots, residual plots
- **Solution**: Feature transformation, polynomial features

### **2. Independence**
- Observations are independent of each other
- **Check**: Domain knowledge, time series plots
- **Solution**: Time series methods, clustered standard errors

### **3. Homoscedasticity**
- Constant variance of residuals across all levels of features
- **Check**: Residual plots, Breusch-Pagan test
- **Solution**: Weighted least squares, robust standard errors

### **4. Normality of Residuals**
- Residuals are normally distributed
- **Check**: Q-Q plots, Shapiro-Wilk test
- **Solution**: Data transformation, robust regression

### **5. No Multicollinearity**
- Features are not highly correlated with each other
- **Check**: Correlation matrix, VIF (Variance Inflation Factor)
- **Solution**: Feature selection, ridge regression

---

## 🚀 **Advantages and Disadvantages**

### ✅ **Advantages:**
- **Simple and fast**: Easy to implement and computationally efficient
- **Interpretable**: Coefficients have clear meaning
- **No hyperparameters**: No complex tuning required
- **Baseline**: Good starting point for any regression problem
- **Statistical inference**: Provides confidence intervals and p-values
- **Feature importance**: Coefficients indicate feature importance

### ❌ **Disadvantages:**
- **Linear assumption**: Can't capture non-linear relationships
- **Sensitive to outliers**: Outliers can significantly affect the model
- **Feature scaling**: Requires feature scaling for fair coefficient comparison
- **Overfitting**: Can overfit with many features relative to samples
- **Assumptions**: Requires several statistical assumptions to be met

---

## 🛠 **Implementation and Code**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("🏠 LINEAR REGRESSION: HOUSE PRICE PREDICTION")
print("=" * 60)

# ============================================================================
# 1. DATA PREPARATION
# ============================================================================

# Create the house price dataset from the example
data = {
    'House_Size_SqFt': [500, 800, 1000, 1200, 1500],
    'House_Price_USD': [150000, 200000, 250000, 280000, 320000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("\n📊 DATASET OVERVIEW")
print("-" * 30)
print(df)
print(f"\nDataset Shape: {df.shape}")
print(f"Number of samples: {len(df)}")

# Basic statistics
print("\n📈 DESCRIPTIVE STATISTICS")
print("-" * 40)
print(df.describe())

# ============================================================================
# 2. EXPLORATORY DATA ANALYSIS
# ============================================================================

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('House Price Analysis', fontsize=16, fontweight='bold')

# Scatter plot
axes[0, 0].scatter(df['House_Size_SqFt'], df['House_Price_USD'], 
                   color='blue', s=100, alpha=0.7, edgecolors='black')
axes[0, 0].set_xlabel('House Size (Sq Ft)')
axes[0, 0].set_ylabel('House Price (USD)')
axes[0, 0].set_title('House Size vs Price')
axes[0, 0].grid(True, alpha=0.3)

# Add correlation coefficient
correlation = df['House_Size_SqFt'].corr(df['House_Price_USD'])
axes[0, 0].text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
                transform=axes[0, 0].transAxes, fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# Distribution of house sizes
axes[0, 1].hist(df['House_Size_SqFt'], bins=5, color='skyblue', 
                alpha=0.7, edgecolor='black')
axes[0, 1].set_xlabel('House Size (Sq Ft)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Distribution of House Sizes')
axes[0, 1].grid(True, alpha=0.3)

# Distribution of house prices
axes[1, 0].hist(df['House_Price_USD'], bins=5, color='lightgreen', 
                alpha=0.7, edgecolor='black')
axes[1, 0].set_xlabel('House Price (USD)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Distribution of House Prices')
axes[1, 0].grid(True, alpha=0.3)

# Box plot for house prices
axes[1, 1].boxplot(df['House_Price_USD'])
axes[1, 1].set_ylabel('House Price (USD)')
axes[1, 1].set_title('House Price Distribution (Box Plot)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================================
# 3. MANUAL CALCULATION OF LINEAR REGRESSION COEFFICIENTS
# ============================================================================

print("\n🧮 MANUAL CALCULATION OF LINEAR REGRESSION")
print("=" * 50)

# Extract features and target
X_manual = df['House_Size_SqFt'].values
y_manual = df['House_Price_USD'].values
n = len(X_manual)

print(f"Number of data points (n): {n}")

# Calculate required sums
sum_x = np.sum(X_manual)
sum_y = np.sum(y_manual)
sum_xy = np.sum(X_manual * y_manual)
sum_x_squared = np.sum(X_manual ** 2)
sum_x_whole_squared = sum_x ** 2

print(f"\n📊 CALCULATION COMPONENTS:")
print(f"∑x = {sum_x:,}")
print(f"∑y = {sum_y:,}")
print(f"∑(xy) = {sum_xy:,}")
print(f"∑(x²) = {sum_x_squared:,}")
print(f"(∑x)² = {sum_x_whole_squared:,}")

# Calculate slope (m)
numerator_slope = n * sum_xy - sum_x * sum_y
denominator_slope = n * sum_x_squared - sum_x_whole_squared
slope_m = numerator_slope / denominator_slope

print(f"\n📈 SLOPE CALCULATION:")
print(f"Numerator = n∑(xy) - ∑x∑y = {n} × {sum_xy:,} - {sum_x:,} × {sum_y:,}")
print(f"         = {n * sum_xy:,} - {sum_x * sum_y:,} = {numerator_slope:,}")
print(f"Denominator = n∑(x²) - (∑x)² = {n} × {sum_x_squared:,} - {sum_x_whole_squared:,}")
print(f"           = {n * sum_x_squared:,} - {sum_x_whole_squared:,} = {denominator_slope:,}")
print(f"Slope (m) = {numerator_slope:,} / {denominator_slope:,} = {slope_m:.2f}")

# Calculate y-intercept (b)
intercept_b = (sum_y - slope_m * sum_x) / n

print(f"\n📍 Y-INTERCEPT CALCULATION:")
print(f"b = (∑y - m∑x) / n")
print(f"  = ({sum_y:,} - {slope_m:.2f} × {sum_x:,}) / {n}")
print(f"  = ({sum_y:,} - {slope_m * sum_x:,.2f}) / {n}")
print(f"  = {sum_y - slope_m * sum_x:,.2f} / {n}")
print(f"  = {intercept_b:,.2f}")

print(f"\n🎯 FINAL LINEAR REGRESSION EQUATION:")
print(f"House Price = {slope_m:.2f} × House Size + {intercept_b:,.2f}")
print(f"y = {slope_m:.2f}x + {intercept_b:,.2f}")

# ============================================================================
# 4. SKLEARN IMPLEMENTATION
# ============================================================================

print("\n🤖 SCIKIT-LEARN IMPLEMENTATION")
print("=" * 40)

# Prepare data for sklearn
X = df[['House_Size_SqFt']]  # Features (2D array)
y = df['House_Price_USD']    # Target (1D array)

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Get coefficients
sklearn_slope = model.coef_[0]
sklearn_intercept = model.intercept_

print(f"Sklearn Slope: {sklearn_slope:.2f}")
print(f"Sklearn Intercept: {sklearn_intercept:,.2f}")
print(f"Manual Slope: {slope_m:.2f}")
print(f"Manual Intercept: {intercept_b:,.2f}")

# Verify our manual calculations match sklearn
print(f"\n✅ VERIFICATION:")
print(f"Slope difference: {abs(sklearn_slope - slope_m):.6f}")
print(f"Intercept difference: {abs(sklearn_intercept - intercept_b):.6f}")

# ============================================================================
# 5. MAKING PREDICTIONS
# ============================================================================

print("\n🔮 MAKING PREDICTIONS")
print("=" * 30)

# Predict on training data
y_pred_train = model.predict(X)

# Create prediction table
prediction_df = pd.DataFrame({
    'Actual_Size': X.iloc[:, 0],
    'Actual_Price': y,
    'Predicted_Price': y_pred_train,
    'Residual': y - y_pred_train,
    'Absolute_Error': np.abs(y - y_pred_train)
})

print("📊 TRAINING PREDICTIONS:")
print(prediction_df.round(2))

# Make predictions for new house sizes
new_sizes = np.array([[600], [900], [1300], [1800], [2000]])
new_predictions = model.predict(new_sizes)

print(f"\n🏠 NEW HOUSE PRICE PREDICTIONS:")
print("-" * 40)
for size, price in zip(new_sizes.flatten(), new_predictions):
    print(f"House Size: {size:4d} sq ft → Predicted Price: ${price:,.0f}")

# ============================================================================
# 6. MODEL EVALUATION
# ============================================================================

print("\n📊 MODEL EVALUATION METRICS")
print("=" * 40)

# Calculate evaluation metrics
mse = mean_squared_error(y, y_pred_train)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred_train)
r2 = r2_score(y, y_pred_train)

# Manual R-squared calculation for verification
ss_res = np.sum((y - y_pred_train) ** 2)  # Sum of squares of residuals
ss_tot = np.sum((y - np.mean(y)) ** 2)    # Total sum of squares
r2_manual = 1 - (ss_res / ss_tot)

print(f"Mean Squared Error (MSE): {mse:,.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")
print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"R-squared (R²): {r2:.4f}")
print(f"R-squared (Manual): {r2_manual:.4f}")

# Interpret R-squared
print(f"\n📈 MODEL INTERPRETATION:")
print(f"The model explains {r2*100:.1f}% of the variance in house prices")
print(f"Average prediction error: ±${rmse:,.0f}")

# ============================================================================
# 7. ADVANCED VISUALIZATION
# ============================================================================

# Create comprehensive visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Linear Regression Analysis: House Price Prediction', 
             fontsize=16, fontweight='bold')

# 1. Regression line plot
x_range = np.linspace(X.min(), X.max() + 500, 100).reshape(-1, 1)
y_range_pred = model.predict(x_range)

axes[0, 0].scatter(X, y, color='blue', s=100, alpha=0.7, 
                   edgecolors='black', label='Actual Data', zorder=5)
axes[0, 0].plot(x_range, y_range_pred, color='red', linewidth=2, 
                label=f'Regression Line\ny = {sklearn_slope:.1f}x + {sklearn_intercept:,.0f}')
axes[0, 0].scatter(X, y_pred_train, color='orange', s=80, alpha=0.8, 
                   edgecolors='black', marker='^', label='Predictions')

# Add prediction lines
for i in range(len(X)):
    axes[0, 0].plot([X.iloc[i, 0], X.iloc[i, 0]], [y.iloc[i], y_pred_train[i]], 
                    'gray', linestyle='--', alpha=0.5)

axes[0, 0].set_xlabel('House Size (Sq Ft)')
axes[0, 0].set_ylabel('House Price (USD)')
axes[0, 0].set_title('Linear Regression Fit')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Add R² annotation
axes[0, 0].text(0.05, 0.95, f'R² = {r2:.3f}\nRMSE = ${rmse:,.0f}', 
                transform=axes[0, 0].transAxes, fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# 2. Residuals plot
residuals = y - y_pred_train
axes[0, 1].scatter(y_pred_train, residuals, color='green', s=100, 
                   alpha=0.7, edgecolors='black')
axes[0, 1].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0, 1].set_xlabel('Predicted Prices')
axes[0, 1].set_ylabel('Residuals')
axes[0, 1].set_title('Residuals vs Predicted')
axes[0, 1].grid(True, alpha=0.3)

# Add residual statistics
residual_std = np.std(residuals)
axes[0, 1].text(0.05, 0.95, f'Residual Std: ${residual_std:,.0f}', 
                transform=axes[0, 1].transAxes, fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))

# 3. Actual vs Predicted
min_val = min(y.min(), y_pred_train.min())
max_val = max(y.max(), y_pred_train.max())
axes[1, 0].scatter(y, y_pred_train, color='purple', s=100, 
                   alpha=0.7, edgecolors='black')
axes[1, 0].plot([min_val, max_val], [min_val, max_val], 
                'red', linestyle='--', linewidth=2, label='Perfect Prediction')
axes[1, 0].set_xlabel('Actual Prices')
axes[1, 0].set_ylabel('Predicted Prices')
axes[1, 0].set_title('Actual vs Predicted Prices')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. Feature importance (coefficient visualization)
coef_data = pd.DataFrame({
    'Feature': ['House Size (per sq ft)'],
    'Coefficient': [sklearn_slope],
    'Interpretation': [f'${sklearn_slope:.0f} per sq ft']
})

bars = axes[1, 1].bar(coef_data['Feature'], coef_data['Coefficient'], 
                      color='coral', alpha=0.7, edgecolor='black')
axes[1, 1].set_ylabel('Coefficient Value')
axes[1, 1].set_title('Feature Coefficient')
axes[1, 1].grid(True, alpha=0.3)

# Add value labels on bars
for bar, value in zip(bars, coef_data['Coefficient']):
    height = bar.get_height()
    axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                    f'${value:.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# ============================================================================
# 8. EXTENDED ANALYSIS
# ============================================================================

print("\n🔍 EXTENDED ANALYSIS")
print("=" * 30)

# Create extended dataset with more realistic features
np.random.seed(42)
extended_data = {
    'House_Size_SqFt': np.random.randint(400, 3000, 50),
    'Bedrooms': np.random.randint(1, 6, 50),
    'Bathrooms': np.random.randint(1, 4, 50),
    'Age_Years': np.random.randint(0, 50, 50),
    'Garage_Cars': np.random.randint(0, 3, 50)
}

# Create more realistic house prices with some noise
extended_df = pd.DataFrame(extended_data)
extended_df['House_Price_USD'] = (
    extended_df['House_Size_SqFt'] * 150 +
    extended_df['Bedrooms'] * 10000 +
    extended_df['Bathrooms'] * 15000 -
    extended_df['Age_Years'] * 1000 +
    extended_df['Garage_Cars'] * 8000 +
    np.random.normal(0, 20000, 50) +
    50000
)

print("📊 EXTENDED DATASET OVERVIEW:")
print("-" * 35)
print(extended_df.head())
print(f"\nDataset Shape: {extended_df.shape}")

# Multiple linear regression
print("\n🔄 MULTIPLE LINEAR REGRESSION")
print("-" * 35)

X_multi = extended_df[['House_Size_SqFt', 'Bedrooms', 'Bathrooms', 'Age_Years', 'Garage_Cars']]
y_multi = extended_df['House_Price_USD']

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X_multi, y_multi, 
                                                    test_size=0.2, random_state=42)

# Fit multiple linear regression
multi_model = LinearRegression()
multi_model.fit(X_train, y_train)

# Make predictions
y_pred_multi_train = multi_model.predict(X_train)
y_pred_multi_test = multi_model.predict(X_test)

# Evaluate multiple linear regression
mse_multi_train = mean_squared_error(y_train, y_pred_multi_train)
mse_multi_test = mean_squared_error(y_test, y_pred_multi_test)
r2_multi_train = r2_score(y_train, y_pred_multi_train)
r2_multi_test = r2_score(y_test, y_pred_multi_test)

print(f"Training R²: {r2_multi_train:.3f}")
print(f"Testing R²: {r2_multi_test:.3f}")
print(f"Training RMSE: ${np.sqrt(mse_multi_train):,.0f}")
print(f"Testing RMSE: ${np.sqrt(mse_multi_test):,.0f}")

# Feature importance
feature_importance = pd.DataFrame({
    'Feature': X_multi.columns,
    'Coefficient': multi_model.coef_,
    'Abs_Coefficient': np.abs(multi_model.coef_)
}).sort_values('Abs_Coefficient', ascending=False)

print(f"\n📊 FEATURE IMPORTANCE (Multiple Regression):")
print("-" * 50)
for _, row in feature_importance.iterrows():
    print(f"{row['Feature']:15}: {row['Coefficient']:8.1f} "
          f"({'positive' if row['Coefficient'] > 0 else 'negative'} impact)")

# ============================================================================
# 9. MODEL ASSUMPTIONS CHECK
# ============================================================================

print("\n🔍 CHECKING LINEAR REGRESSION ASSUMPTIONS")
print("=" * 50)

# Using the simple model for assumption checking
residuals_check = y - y_pred_train

# 1. Linearity check
print("1. LINEARITY:")
print("   ✓ Visual inspection shows linear relationship in scatter plot")

# 2. Independence
print("\n2. INDEPENDENCE:")
print("   ✓ Assuming house sales are independent observations")

# 3. Homoscedasticity (constant variance)
print("\n3. HOMOSCEDASTICITY:")
print("   ✓ Check residuals plot - should show constant variance")

# 4. Normality of residuals
from scipy import stats
shapiro_stat, shapiro_p = stats.shapiro(residuals_check)
print(f"\n4. NORMALITY OF RESIDUALS:")
print(f"   Shapiro-Wilk test: statistic = {shapiro_stat:.3f}, p-value = {shapiro_p:.3f}")
if shapiro_p > 0.05:
    print("   ✓ Residuals appear to be normally distributed")
else:
    print("   ⚠ Residuals may not be normally distributed")

# ============================================================================
# 10. FINAL SUMMARY AND RECOMMENDATIONS
# ============================================================================

print("\n" + "="*70)
print("📋 FINAL SUMMARY AND RECOMMENDATIONS")
print("="*70)

print(f"""
🎯 MODEL PERFORMANCE:
   • R-squared: {r2:.3f} ({r2*100:.1f}% of variance explained)
   • RMSE: ${rmse:,.0f} (average prediction error)
   • MAE: ${mae:,.0f} (average absolute error)

📈 KEY INSIGHTS:
   • Strong positive relationship between house size and price
   • Price increases by ${slope_m:.0f} per square foot
   • Base price (intercept): ${intercept_b:,.0f}
   • Model performs well with high R-squared value

🔧 PRACTICAL APPLICATIONS:
   • Real estate valuation and pricing
   • Investment property analysis
   • Market trend analysis
   • Budget planning for home buyers

⚠️  LIMITATIONS AND CONSIDERATIONS:
   • Model assumes linear relationship (may not hold for all ranges)
   • Limited to one feature (size) - other factors affect price
   • Based on small sample size - more data would improve reliability
   • Market conditions, location, and other factors not considered

🚀 RECOMMENDATIONS FOR IMPROVEMENT:
   • Collect more data points for better model reliability
   • Include additional features (location, bedrooms, bathrooms, age)
   • Consider polynomial features for non-linear relationships
   • Validate model on out-of-sample data
   • Monitor model performance over time as market conditions change
""")

print("="*70)
print("✅ ANALYSIS COMPLETE!")
print("="*70)
```

This comprehensive guide provides:

1. **Complete theoretical foundation** with detailed mathematical explanations
2. **Step-by-step formula breakdown** with real calculations
3. **Practical house price prediction example** with actual numbers
4. **Full implementation** with both manual calculations and scikit-learn
5. **Extensive visualizations** for better understanding
6. **Model evaluation** and interpretation
7. **Assumption checking** and validation
8. **Extended analysis** with multiple features
9. **Best practices** and recommendations

The code is heavily commented and provides a complete learning resource for understanding linear regression from theory to practice.
