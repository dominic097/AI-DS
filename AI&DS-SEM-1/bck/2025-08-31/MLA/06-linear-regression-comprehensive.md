# Linear Regression - 31 Aug 2025

## Introduction to Linear Regression

**Linear Regression** is one of the most fundamental and widely used supervised machine learning algorithms for predicting continuous numerical values. It assumes a linear relationship between input features (independent variables) and the target variable (dependent variable).

### Core Concept

Linear regression finds the best-fitting straight line (or hyperplane in multiple dimensions) through the data points that minimizes the prediction error.

### Key Terminology

- **Dependent Variable (Y)**: The target variable we want to predict
- **Independent Variables (X)**: Input features used for prediction  
- **Coefficients (β)**: Parameters that define the linear relationship
- **Intercept (β₀)**: Y-axis intercept (bias term)
- **Residuals (ε)**: Prediction errors (actual - predicted)

### Real-World Example
```
Predicting House Prices:
- Y (target): House price ($)
- X₁: Square footage
- X₂: Number of bedrooms
- X₃: Age of house
- X₄: Distance to city center

Goal: Find the linear equation that best predicts price
```

## Mathematical Foundation

### Simple Linear Regression (One Feature)

**Mathematical Equation:**
```
Y = β₀ + β₁X + ε

Where:
- Y = predicted value
- β₀ = y-intercept (value when X = 0)
- β₁ = slope (change in Y per unit change in X)
- X = input feature
- ε = error term (residual)
```

**Example:**
```
House Price = 50,000 + 100 × Square_Footage

Interpretation:
- Base price: $50,000 (β₀)
- Each sq ft adds: $100 (β₁)
- 1,500 sq ft house: $50,000 + 100×1,500 = $200,000
```

### Multiple Linear Regression

**Mathematical Equation:**
```
Y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + ... + βₙXₙ + ε

Matrix Form:
Y = Xβ + ε

Where:
- X = feature matrix (n_samples × n_features)
- β = coefficient vector
- Y = target vector
```

**Example:**
```
House Price = β₀ + β₁(Size) + β₂(Bedrooms) + β₃(Age) + β₄(Distance)
            = 30,000 + 120(Size) + 15,000(Bedrooms) - 500(Age) - 2(Distance)

Interpretation:
- Base price: $30,000
- Each sq ft: +$120
- Each bedroom: +$15,000
- Each year older: -$500
- Each mile from city: -$2
```

## How Linear Regression Works

### The Learning Process

#### Step 1: Define the Cost Function
**Mean Squared Error (MSE):**
```
MSE = (1/n) × Σᵢ₌₁ⁿ (yᵢ - ŷᵢ)²

Where:
- n = number of samples
- yᵢ = actual value for sample i
- ŷᵢ = predicted value for sample i
```

**Why MSE?**
- Differentiable (enables gradient-based optimization)
- Penalizes larger errors more heavily
- Mathematically convenient

#### Step 2: Find Optimal Coefficients

**Method 1: Normal Equation (Closed-form Solution)**
```
β = (X᷀X)⁻¹X᷀Y

Where:
- X᷀ = transpose of feature matrix
- (X᷀X)⁻¹ = inverse of matrix multiplication
- Direct calculation of optimal coefficients
```

**Advantages:**
- Exact solution (no iterations)
- No hyperparameters to tune
- Always finds global minimum

**Disadvantages:**
- Computationally expensive for large datasets (O(n³))
- Requires matrix inversion (may not exist)
- Memory intensive

**Method 2: Gradient Descent (Iterative Solution)**
```
Repeat until convergence:
β = β - α × ∇MSE(β)

Where:
- α = learning rate (hyperparameter)
- ∇MSE(β) = gradient of cost function
```

**Gradient Calculation:**
```
∂MSE/∂β = (2/n) × X᷀(Xβ - Y)
```

**Advantages:**
- Works with large datasets
- Scalable to many features
- Can handle streaming data

**Disadvantages:**
- Requires hyperparameter tuning (learning rate)
- May converge slowly
- Can get stuck in local minima (though MSE is convex)

### Visual Understanding

#### Simple Linear Regression Visualization
```
Price ($000s)
    400 |
        |    •
    300 |  •   •
        |     •
    200 |  •
        | •
    100 |
        |________________
         1000  2000  3000
           Size (sq ft)

Best fit line: Price = 50 + 0.12 × Size
```

#### Residual Analysis
```
Residuals = Actual - Predicted

Good Model (Random pattern):
Residuals
    +30 |  •    •
        |    •
      0 |  •  • •  •
        |•      •
    -30 |    •
        |________________
           Predicted Values

Bad Model (Pattern visible):
Residuals  
    +30 |      • •
        |    •     •
      0 |  •         •
        |•             •
    -30 |  •         •
        |________________
           Predicted Values
```

## Types of Linear Regression

### 1. Simple Linear Regression

**Use Case:** One independent variable predicts one dependent variable

**Example Applications:**
- Years of experience → Salary
- Temperature → Ice cream sales
- Study hours → Test score
- Advertising spend → Sales

**Python Implementation:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [5]])  # Years of experience
y = np.array([30000, 35000, 40000, 45000, 50000])  # Salary

# Fit model
model = LinearRegression()
model.fit(X, y)

# Get coefficients
intercept = model.intercept_  # β₀
slope = model.coef_[0]       # β₁

print(f"Salary = {intercept} + {slope} × Experience")
# Output: Salary = 25000 + 5000 × Experience
```

### 2. Multiple Linear Regression

**Use Case:** Multiple independent variables predict one dependent variable

**Example Applications:**
- House features → Price
- Student attributes → GPA
- Marketing channels → Sales
- Economic indicators → Stock price

**Feature Interaction:**
```python
# Basic multiple regression
X = [[1500, 3, 10], [2000, 4, 5], [1200, 2, 15]]  # Size, Bedrooms, Age
y = [200000, 280000, 180000]  # Price

model.fit(X, y)
# Price = β₀ + β₁×Size + β₂×Bedrooms + β₃×Age
```

### 3. Polynomial Linear Regression

**Concept:** Still linear in coefficients, but uses polynomial features

**Mathematical Form:**
```
Y = β₀ + β₁X + β₂X² + β₃X³ + ... + βₙXⁿ

Still a linear regression problem!
(Linear in coefficients β₀, β₁, β₂, ...)
```

**Example:**
```python
from sklearn.preprocessing import PolynomialFeatures

# Original feature: [1, 2, 3, 4, 5]
# Polynomial features (degree=2): [1, 1², 2, 2², 3, 3², ...]
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model.fit(X_poly, y)
# Now can model curved relationships!
```

**Applications:**
- Projectile motion (quadratic)
- Economic relationships (diminishing returns)
- Growth models (various polynomial orders)

## Assumptions of Linear Regression

### 1. Linearity

**Assumption:** The relationship between independent and dependent variables is linear.

**How to Check:**
```python
import matplotlib.pyplot as plt

# Scatter plot of each feature vs target
for i, feature in enumerate(feature_names):
    plt.scatter(X[:, i], y)
    plt.xlabel(feature)
    plt.ylabel('Target')
    plt.title(f'{feature} vs Target')
    plt.show()
```

**Violation Signs:**
- Curved patterns in scatter plots
- Non-random patterns in residual plots

**Solutions if Violated:**
- Transform features (log, sqrt, polynomial)
- Use non-linear regression methods
- Add interaction terms

### 2. Independence of Observations

**Assumption:** Observations are independent of each other.

**How to Check:**
- Domain knowledge (are samples related?)
- Durbin-Watson test for autocorrelation
- Plot residuals vs observation order

**Violation Examples:**
- Time series data (temporal dependence)
- Clustered data (spatial dependence)
- Repeated measures (same subjects)

**Solutions if Violated:**
- Use time series methods
- Add time/cluster controls
- Mixed-effects models

### 3. Homoscedasticity (Constant Variance)

**Assumption:** Residuals have constant variance across all levels of independent variables.

**How to Check:**
```python
# Residual vs fitted plot
residuals = y_actual - y_predicted
plt.scatter(y_predicted, residuals)
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residuals vs Fitted')
plt.show()

# Should show random scatter around y=0
```

**Violation Signs (Heteroscedasticity):**
- Fan-shaped residual pattern
- Residual variance increases/decreases with fitted values

**Solutions if Violated:**
- Transform target variable (log, sqrt)
- Weighted least squares
- Robust standard errors
- Use different algorithms

### 4. Normality of Residuals

**Assumption:** Residuals are normally distributed.

**How to Check:**
```python
import scipy.stats as stats

# Q-Q plot
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.show()

# Shapiro-Wilk test
statistic, p_value = stats.shapiro(residuals)
print(f"Shapiro-Wilk test: p-value = {p_value}")
# p-value > 0.05 suggests normal distribution
```

**Violation Signs:**
- Q-Q plot deviates from straight line
- Histogram of residuals is skewed
- Failed normality tests

**Solutions if Violated:**
- Transform target variable
- Use robust regression methods
- Larger sample sizes (Central Limit Theorem)

### 5. No Multicollinearity

**Assumption:** Independent variables are not highly correlated with each other.

**How to Check:**
```python
import pandas as pd

# Correlation matrix
correlation_matrix = pd.DataFrame(X).corr()
print(correlation_matrix)

# Variance Inflation Factor (VIF)
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_data = pd.DataFrame()
vif_data["Feature"] = feature_names
vif_data["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
print(vif_data)

# VIF > 5 indicates multicollinearity
# VIF > 10 indicates severe multicollinearity
```

**Violation Signs:**
- High correlation between features (|r| > 0.8)
- High VIF values (> 5-10)
- Unstable coefficients with small data changes

**Solutions if Violated:**
- Remove highly correlated features
- Principal Component Analysis (PCA)
- Ridge regression (L2 regularization)
- Domain knowledge feature selection

## Regularization Techniques

### Why Regularization?

**Problems with Standard Linear Regression:**
- **Overfitting**: Model memorizes training data, poor generalization
- **Multicollinearity**: Unstable coefficients when features are correlated
- **High Dimensionality**: More features than samples (p > n problem)

### Ridge Regression (L2 Regularization)

**Mathematical Formula:**
```
Cost = MSE + α × Σᵢ₌₁ⁿ βᵢ²

Where:
- α = regularization strength (hyperparameter ≥ 0)
- Σβᵢ² = sum of squared coefficients
```

**How it Works:**
1. Adds penalty for large coefficients
2. Shrinks coefficients toward zero (but not exactly zero)
3. Reduces model complexity and overfitting

**Effect on Coefficients:**
```
α = 0 (no regularization): Coefficients can be very large
α = small: Slight shrinkage of coefficients
α = large: Heavy shrinkage, coefficients approach zero
α = ∞: All coefficients become zero (model predicts mean)
```

**Python Implementation:**
```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Try different alpha values
alphas = [0.01, 0.1, 1, 10, 100]
cv_scores = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    scores = cross_val_score(ridge, X, y, cv=5, scoring='neg_mean_squared_error')
    cv_scores.append(-scores.mean())

# Choose alpha with best cross-validation score
best_alpha = alphas[np.argmin(cv_scores)]
print(f"Best alpha: {best_alpha}")
```

**When to Use Ridge:**
- All features potentially relevant
- Multicollinearity present
- Want to keep all features (no feature selection)
- Stable, smooth coefficient shrinkage desired

### Lasso Regression (L1 Regularization)

**Mathematical Formula:**
```
Cost = MSE + α × Σᵢ₌₁ⁿ |βᵢ|

Where:
- α = regularization strength
- Σ|βᵢ| = sum of absolute values of coefficients
```

**How it Works:**
1. Adds penalty for absolute coefficient values
2. Can shrink coefficients to exactly zero
3. Performs automatic feature selection

**Feature Selection Property:**
```
Lasso path (as α increases):
α = 0: All features included
α = small: Some coefficients shrink
α = medium: Some coefficients become exactly zero
α = large: More coefficients become zero
α = very large: Only intercept remains
```

**Python Implementation:**
```python
from sklearn.linear_model import Lasso, LassoCV

# Automatic alpha selection with cross-validation
lasso_cv = LassoCV(cv=5, random_state=42)
lasso_cv.fit(X, y)

print(f"Best alpha: {lasso_cv.alpha_}")
print(f"Features selected: {sum(lasso_cv.coef_ != 0)}")

# Get selected features
selected_features = [i for i, coef in enumerate(lasso_cv.coef_) if coef != 0]
print(f"Selected feature indices: {selected_features}")
```

**When to Use Lasso:**
- Want automatic feature selection
- Suspect some features are irrelevant
- Prefer sparse models (fewer features)
- Interpretability is important

### Elastic Net (L1 + L2 Regularization)

**Mathematical Formula:**
```
Cost = MSE + α₁ × Σ|βᵢ| + α₂ × Σβᵢ²

Or equivalently:
Cost = MSE + α × [l1_ratio × Σ|βᵢ| + (1-l1_ratio) × Σβᵢ²]

Where:
- α = overall regularization strength
- l1_ratio = balance between L1 and L2 (0 to 1)
```

**How it Works:**
- Combines Ridge and Lasso benefits
- Can select features while handling multicollinearity
- More stable than Lasso when features are correlated

**Parameter Interpretation:**
```
l1_ratio = 0: Pure Ridge regression
l1_ratio = 1: Pure Lasso regression
l1_ratio = 0.5: Equal mix of L1 and L2
```

**Python Implementation:**
```python
from sklearn.linear_model import ElasticNetCV

# Grid search over both alpha and l1_ratio
elastic_cv = ElasticNetCV(
    cv=5, 
    l1_ratio=[.1, .5, .7, .9, .95, .99, 1],
    random_state=42
)
elastic_cv.fit(X, y)

print(f"Best alpha: {elastic_cv.alpha_}")
print(f"Best l1_ratio: {elastic_cv.l1_ratio_}")
```

**When to Use Elastic Net:**
- Want both feature selection and multicollinearity handling
- Have groups of correlated features
- Need balance between sparsity and stability
- Lasso is too unstable

### Comparison of Regularization Methods

| Aspect | Ridge | Lasso | Elastic Net |
|--------|-------|-------|-------------|
| **Penalty** | L2 (squared) | L1 (absolute) | L1 + L2 |
| **Feature Selection** | No | Yes | Yes |
| **Coefficient Shrinkage** | Smooth | Sharp (to zero) | Balanced |
| **Multicollinearity** | Handles well | Can be unstable | Handles well |
| **Sparse Solutions** | No | Yes | Yes |
| **Grouped Features** | Shrinks together | Picks one arbitrarily | Selects groups |

## Model Evaluation and Diagnostics

### Performance Metrics

#### 1. Mean Squared Error (MSE)
```
MSE = (1/n) × Σ(actual - predicted)²

Interpretation:
- Average squared prediction error
- Units: target variable squared
- Range: 0 to ∞ (lower is better)
- Heavily penalizes large errors
```

#### 2. Root Mean Squared Error (RMSE)
```
RMSE = √MSE

Interpretation:
- Average prediction error in original units
- Same units as target variable
- Range: 0 to ∞ (lower is better)
- More interpretable than MSE
```

#### 3. Mean Absolute Error (MAE)
```
MAE = (1/n) × Σ|actual - predicted|

Interpretation:
- Average absolute prediction error
- Less sensitive to outliers than MSE/RMSE
- Same units as target variable
- Range: 0 to ∞ (lower is better)
```

#### 4. R-squared (Coefficient of Determination)
```
R² = 1 - (SS_residual / SS_total)

Where:
- SS_residual = Σ(actual - predicted)²
- SS_total = Σ(actual - mean)²

Interpretation:
- Proportion of variance explained by model
- Range: -∞ to 1 (higher is better)
- R² = 1: Perfect prediction
- R² = 0: No better than predicting mean
- R² < 0: Worse than predicting mean
```

#### 5. Adjusted R-squared
```
Adj R² = 1 - [(1 - R²) × (n - 1) / (n - p - 1)]

Where:
- n = number of observations
- p = number of predictors

Interpretation:
- Adjusts R² for number of features
- Penalizes adding irrelevant features
- Better for model comparison
```

### Residual Analysis

#### Purpose of Residual Analysis
- Validate model assumptions
- Identify patterns missed by model
- Detect outliers and influential points
- Guide model improvements

#### 1. Residuals vs Fitted Plot
```python
residuals = y_actual - y_predicted
fitted = y_predicted

plt.scatter(fitted, residuals, alpha=0.7)
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residuals vs Fitted')
plt.show()

# Good model: Random scatter around y=0
# Bad model: Clear patterns (curved, funnel-shaped, etc.)
```

#### 2. Q-Q Plot (Normal Probability Plot)
```python
import scipy.stats as stats

stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot of Residuals')
plt.show()

# Good model: Points follow diagonal line
# Bad model: Systematic deviations from line
```

#### 3. Scale-Location Plot
```python
import numpy as np

standardized_residuals = residuals / np.std(residuals)
sqrt_abs_residuals = np.sqrt(np.abs(standardized_residuals))

plt.scatter(fitted, sqrt_abs_residuals, alpha=0.7)
plt.xlabel('Fitted Values')
plt.ylabel('√|Standardized Residuals|')
plt.title('Scale-Location Plot')
plt.show()

# Good model: Horizontal line with random scatter
# Bad model: Trend (increasing/decreasing spread)
```

#### 4. Leverage and Cook's Distance
```python
from statsmodels.stats.outliers_influence import OLSInfluence

# Fit using statsmodels for diagnostic statistics
import statsmodels.api as sm

X_with_const = sm.add_constant(X)  # Add intercept
model_sm = sm.OLS(y, X_with_const).fit()
influence = OLSInfluence(model_sm)

# Get diagnostic measures
leverage = influence.hat_matrix_diag
cooks_d = influence.cooks_distance[0]

# Plot leverage vs residuals
plt.scatter(leverage, residuals, alpha=0.7)
plt.xlabel('Leverage')
plt.ylabel('Residuals')
plt.title('Leverage vs Residuals')
plt.show()

# High leverage + large residual = influential point
```

### Cross-Validation

#### Why Cross-Validation?
- Assess model generalization ability
- Prevent overfitting
- Select hyperparameters
- Compare different models

#### K-Fold Cross-Validation
```python
from sklearn.model_selection import cross_val_score, KFold

# 5-fold cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='neg_mean_squared_error')

print(f"CV RMSE: {np.sqrt(-scores.mean()):.2f} (+/- {np.sqrt(scores.std() * 2):.2f})")
```

#### Leave-One-Out Cross-Validation (LOOCV)
```python
from sklearn.model_selection import LeaveOneOut

loo = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loo, scoring='neg_mean_squared_error')
print(f"LOOCV RMSE: {np.sqrt(-scores.mean()):.2f}")
```

## Feature Engineering for Linear Regression

### 1. Feature Scaling

**Why Scale Features?**
- Different units and ranges can dominate
- Regularization treats all features equally
- Gradient descent converges faster
- Interpretation of coefficients

**Methods:**

#### Standardization (Z-score normalization)
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Each feature: mean = 0, std = 1
# Formula: (x - mean) / std
```

#### Min-Max Normalization
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Each feature: range [0, 1]
# Formula: (x - min) / (max - min)
```

### 2. Polynomial Features

**Creating Polynomial Terms:**
```python
from sklearn.preprocessing import PolynomialFeatures

# Degree 2 polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Original features: [x1, x2]
# Polynomial features: [x1, x2, x1², x1*x2, x2²]
```

**Interaction Terms:**
```python
# Only interaction terms, no polynomial
poly_interaction = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_interaction = poly_interaction.fit_transform(X)

# Original features: [x1, x2, x3]
# Interaction features: [x1, x2, x3, x1*x2, x1*x3, x2*x3]
```

### 3. Feature Transformation

**Log Transformation:**
```python
import numpy as np

# For right-skewed features
X_log = np.log(X + 1)  # +1 to handle zeros

# For target variable (multiplicative relationships)
y_log = np.log(y)
```

**Square Root Transformation:**
```python
# For count data or right-skewed features
X_sqrt = np.sqrt(X)
```

**Box-Cox Transformation:**
```python
from scipy.stats import boxcox

# Automatically find optimal transformation
X_transformed, lambda_optimal = boxcox(X + 1)  # +1 for positive values
```

### 4. Handling Categorical Variables

**One-Hot Encoding:**
```python
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Using pandas get_dummies
df_encoded = pd.get_dummies(df, columns=['category_column'], drop_first=True)

# Using sklearn OneHotEncoder
encoder = OneHotEncoder(drop='first', sparse=False)
X_encoded = encoder.fit_transform(X_categorical)
```

**Label Encoding (for ordinal variables):**
```python
from sklearn.preprocessing import LabelEncoder

# For ordinal categories: Low < Medium < High
label_encoder = LabelEncoder()
X_encoded = label_encoder.fit_transform(['Low', 'Medium', 'High', 'Medium'])
# Output: [0, 1, 2, 1]
```

## Real-World Applications

### 1. Sales Forecasting

**Business Problem:** Predict monthly sales based on marketing spend

```python
# Features: TV ads, Radio ads, Newspaper ads, Season, Previous sales
# Target: Current month sales

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score

# Load and prepare data
df = pd.read_csv('sales_data.csv')
X = df[['tv_ads', 'radio_ads', 'newspaper_ads', 'season', 'prev_sales']]
y = df['current_sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fit model
model = Ridge(alpha=1.0)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")

# Interpret coefficients
feature_names = X.columns
coefficients = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': model.coef_
}).sort_values('Coefficient', key=abs, ascending=False)

print("\nFeature Importance (by coefficient magnitude):")
print(coefficients)
```

### 2. Real Estate Price Prediction

**Business Problem:** Estimate house prices for real estate valuation

```python
# Features: Size, bedrooms, bathrooms, age, location scores
# Target: Sale price

# Feature engineering for real estate
def engineer_features(df):
    # Create new features
    df['price_per_sqft'] = df['size'] / df['price']  # Only if price known
    df['rooms_total'] = df['bedrooms'] + df['bathrooms']
    df['age_category'] = pd.cut(df['age'], bins=[0, 5, 15, 30, 100], 
                               labels=['New', 'Recent', 'Mature', 'Old'])
    
    # Handle location as categorical
    df_encoded = pd.get_dummies(df, columns=['neighborhood'], drop_first=True)
    
    return df_encoded

# Polynomial features for size (diminishing returns)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X[['size']])

# Combine with other features
X_combined = np.hstack([X_poly, X_other_features])
```

### 3. Marketing Mix Modeling

**Business Problem:** Understand contribution of different marketing channels

```python
# Adstock transformation for advertising carryover effects
def adstock_transform(x, decay_rate=0.5):
    """Apply adstock transformation to account for carryover effects"""
    adstocked = np.zeros_like(x)
    adstocked[0] = x[0]
    
    for i in range(1, len(x)):
        adstocked[i] = x[i] + decay_rate * adstocked[i-1]
    
    return adstocked

# Apply to advertising channels
df['tv_adstock'] = adstock_transform(df['tv_spend'])
df['digital_adstock'] = adstock_transform(df['digital_spend'])
df['radio_adstock'] = adstock_transform(df['radio_spend'])

# Saturation curves for diminishing returns
def saturation_transform(x, alpha=0.5):
    """Apply saturation transformation"""
    return x ** alpha

df['tv_saturated'] = saturation_transform(df['tv_adstock'])
df['digital_saturated'] = saturation_transform(df['digital_adstock'])
```

## Best Practices and Common Pitfalls

### Best Practices

#### 1. Data Preparation
✅ **Handle missing values appropriately**
✅ **Scale features when using regularization**
✅ **Check for and handle outliers**
✅ **Validate assumptions before modeling**
✅ **Create meaningful feature interactions**

#### 2. Model Building
✅ **Start simple, add complexity gradually**
✅ **Use cross-validation for model selection**
✅ **Regularize when appropriate**
✅ **Document feature engineering steps**
✅ **Keep holdout test set for final evaluation**

#### 3. Model Interpretation
✅ **Examine coefficient signs and magnitudes**
✅ **Calculate confidence intervals for coefficients**
✅ **Use standardized coefficients for comparison**
✅ **Consider business context in interpretation**
✅ **Validate insights with domain experts**

### Common Pitfalls and Solutions

#### 1. Overfitting
**Problem:** Model performs well on training but poorly on test data
**Solutions:**
- Use regularization (Ridge, Lasso, Elastic Net)
- Cross-validation for hyperparameter tuning
- Feature selection to reduce complexity
- Collect more training data

#### 2. Multicollinearity
**Problem:** Highly correlated features cause unstable coefficients
**Detection:** High VIF values (>5-10), high feature correlations
**Solutions:**
- Remove highly correlated features
- Use Ridge regression
- Principal Component Analysis (PCA)
- Domain knowledge for feature selection

#### 3. Non-linear Relationships
**Problem:** Linear model can't capture curved relationships
**Detection:** Curved patterns in residual plots
**Solutions:**
- Polynomial features
- Feature transformations (log, sqrt)
- Interaction terms
- Consider non-linear methods

#### 4. Outliers and Influential Points
**Problem:** Extreme values skew the regression line
**Detection:** Cook's distance, leverage plots, residual analysis
**Solutions:**
- Investigate outliers (data errors vs true extremes)
- Robust regression methods
- Transform variables
- Use models less sensitive to outliers

#### 5. Assumption Violations

**Heteroscedasticity (Non-constant variance):**
- Transform target variable
- Weighted least squares
- Robust standard errors

**Non-normal residuals:**
- Transform target variable
- Use bootstrap confidence intervals
- Consider generalized linear models

**Autocorrelation (time series data):**
- Include lagged variables
- Use time series methods
- Account for seasonality

### Model Deployment Considerations

#### 1. Feature Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Create preprocessing pipeline
numeric_features = ['feature1', 'feature2', 'feature3']
categorical_features = ['category1', 'category2']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ]
)

# Complete pipeline
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', Ridge(alpha=1.0))
])

# Fit pipeline
model_pipeline.fit(X_train, y_train)

# Now preprocessing and prediction are combined
predictions = model_pipeline.predict(X_new)
```

#### 2. Model Monitoring
- Track prediction accuracy over time
- Monitor feature drift (input distribution changes)
- Set up alerts for unusual predictions
- Regular model retraining schedule

#### 3. Interpretability for Business
```python
# Get feature importance from coefficients
feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': model.coef_,
    'Abs_Coefficient': np.abs(model.coef_)
}).sort_values('Abs_Coefficient', ascending=False)

# Calculate prediction intervals
from scipy import stats
prediction = model.predict(X_new)
mse = mean_squared_error(y_test, model.predict(X_test))
std_error = np.sqrt(mse)

# 95% prediction interval
confidence_level = 0.95
t_value = stats.t.ppf((1 + confidence_level) / 2, df=len(y_test)-len(X.columns)-1)
margin_of_error = t_value * std_error

prediction_interval = (prediction - margin_of_error, prediction + margin_of_error)
```

## Summary

### Key Strengths of Linear Regression
✅ **Simplicity and Interpretability**: Easy to understand and explain  
✅ **Fast Training and Prediction**: Efficient for large datasets  
✅ **Statistical Foundation**: Rich theory for inference and testing  
✅ **No Hyperparameters**: Basic version requires no tuning  
✅ **Baseline Performance**: Good starting point for regression problems  
✅ **Feature Importance**: Clear understanding of variable relationships  

### Key Limitations
❌ **Linear Assumption**: Cannot capture complex non-linear patterns  
❌ **Sensitive to Outliers**: Extreme values can significantly impact model  
❌ **Requires Feature Engineering**: Manual creation of interactions/polynomials  
❌ **Assumption Dependent**: Performance degrades when assumptions violated  
❌ **Limited Complexity**: May underfit complex real-world relationships  

### When to Use Linear Regression
- **Interpretability is crucial** (business decisions, scientific research)
- **Linear relationships** apparent in data
- **Quick baseline** needed for comparison
- **Small to medium datasets** where complex methods may overfit
- **Statistical inference** required (confidence intervals, hypothesis testing)
- **Real-time predictions** needed (fast inference)

### Next Steps
After mastering linear regression, consider:
1. **Regularization techniques** (Ridge, Lasso, Elastic Net)
2. **Non-linear methods** (Polynomial, Decision Trees, Neural Networks)
3. **Advanced topics** (Bayesian linear regression, Mixed-effects models)
4. **Domain-specific applications** (Time series, Survival analysis)
