# Linear and Non-Linear Regression - 31 Aug 2025

## Introduction to Regression

**Regression** is a supervised machine learning technique used to predict continuous numerical values (dependent variable) based on one or more input features (independent variables).

### Key Concepts:
- **Dependent Variable (Y)**: The target variable we want to predict
- **Independent Variables (X)**: The input features used for prediction
- **Relationship**: Mathematical function that describes how X relates to Y

### Example:
```
Predicting house prices:
- Y (dependent): House price ($)
- X (independent): Size, location, bedrooms, age, etc.
- Goal: Find function f(X) = Y
```

## Linear Regression

### What is Linear Regression?

**Linear regression** assumes a linear relationship between input features and the target variable. It tries to find the best straight line (or hyperplane in higher dimensions) that fits through the data points.

### Mathematical Foundation

#### **Simple Linear Regression (One Feature):**
```
Y = β₀ + β₁X + ε

Where:
- Y = predicted value
- β₀ = y-intercept (bias term)
- β₁ = slope (coefficient)
- X = input feature
- ε = error term
```

#### **Multiple Linear Regression (Multiple Features):**
```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε

Example:
House Price = β₀ + β₁(Size) + β₂(Bedrooms) + β₃(Age) + ε
```

### Visual Understanding

#### **Simple Linear Regression:**
```
Price
  ^
  |     •
  |   /   •
  | /       •
|/___________> Size
Best fit line: Y = 50000 + 100*Size
```

#### **Multiple Linear Regression (2D visualization):**
```
In 3D space:
- X₁ = Size (x-axis)
- X₂ = Bedrooms (y-axis)  
- Y = Price (z-axis)
Best fit = a plane through the 3D space
```

### How Linear Regression Works

#### **1. Cost Function (Mean Squared Error):**
```
MSE = (1/n) × Σ(Actual - Predicted)²

Goal: Minimize this error by finding best β values
```

#### **2. Normal Equation (Closed-form solution):**
```
β = (X^T × X)^(-1) × X^T × Y

Where:
- X^T = transpose of feature matrix
- (X^T × X)^(-1) = inverse of matrix multiplication
```

#### **3. Gradient Descent (Iterative solution):**
```
Process:
1. Start with random β values
2. Calculate predictions and error
3. Update β to reduce error
4. Repeat until convergence

β = β - α × (∂MSE/∂β)
Where α = learning rate
```

### Types of Linear Regression

#### **1. Simple Linear Regression**
- **One input feature**
- **Example**: Predicting salary based on years of experience
- **Equation**: Salary = β₀ + β₁ × Experience

#### **2. Multiple Linear Regression**
- **Multiple input features**
- **Example**: Predicting house price based on size, bedrooms, location
- **Equation**: Price = β₀ + β₁×Size + β₂×Bedrooms + β₃×Location

#### **3. Polynomial Regression**
- **Linear in parameters, but can model curves**
- **Transform features**: X, X², X³, etc.
- **Example**: Y = β₀ + β₁X + β₂X² + β₃X³
- **Still linear regression!** (linear in coefficients)

### Assumptions of Linear Regression

#### **1. Linearity**
- **Assumption**: Relationship between X and Y is linear
- **Check**: Scatter plot should show linear pattern
- **Violation**: Curved relationships in residual plots

#### **2. Independence**
- **Assumption**: Observations are independent of each other
- **Check**: No patterns in residuals over time/order
- **Violation**: Time series data with temporal dependence

#### **3. Homoscedasticity (Constant Variance)**
- **Assumption**: Error variance is constant across all levels of X
- **Check**: Residual plot should show constant spread
- **Violation**: Fan-shaped residual pattern

#### **4. Normality of Residuals**
- **Assumption**: Errors are normally distributed
- **Check**: Q-Q plot of residuals, histogram
- **Violation**: Skewed residual distribution

#### **5. No Multicollinearity**
- **Assumption**: Input features are not highly correlated with each other
- **Check**: Correlation matrix, Variance Inflation Factor (VIF)
- **Violation**: VIF > 5-10 indicates multicollinearity

### Advantages of Linear Regression

✅ **Simple and Interpretable**: Easy to understand coefficients  
✅ **Fast Training**: Closed-form solution available  
✅ **No Hyperparameters**: No tuning required for basic version  
✅ **Baseline Model**: Good starting point for regression problems  
✅ **Statistical Inference**: P-values, confidence intervals available  
✅ **Less Prone to Overfitting**: Especially with regularization  

### Disadvantages of Linear Regression

❌ **Assumes Linearity**: Cannot capture complex non-linear relationships  
❌ **Sensitive to Outliers**: Extreme values can skew the line significantly  
❌ **Feature Engineering Required**: Need to create polynomial/interaction terms manually  
❌ **Multicollinearity Issues**: Correlated features cause problems  
❌ **Homoscedasticity Assumption**: Constant variance often violated in real data  

### Regularization in Linear Regression

#### **Why Regularization?**
- **Overfitting**: Model memorizes training data, poor generalization
- **Multicollinearity**: Highly correlated features cause unstable coefficients
- **High Dimensionality**: More features than samples

#### **1. Ridge Regression (L2 Regularization)**

**Mathematical Formula:**
```
Cost = MSE + α × Σ(βᵢ)²

Where:
- α = regularization strength (hyperparameter)
- Σ(βᵢ)² = sum of squared coefficients
```

**How it works:**
- Adds penalty for large coefficients
- Shrinks coefficients toward zero (but not exactly zero)
- Handles multicollinearity well

**When to use:**
- All features potentially relevant
- Multicollinearity present
- Want to keep all features

#### **2. Lasso Regression (L1 Regularization)**

**Mathematical Formula:**
```
Cost = MSE + α × Σ|βᵢ|

Where:
- α = regularization strength
- Σ|βᵢ| = sum of absolute coefficients
```

**How it works:**
- Adds penalty for absolute coefficient values
- Can shrink coefficients to exactly zero (feature selection)
- Performs automatic feature selection

**When to use:**
- Want automatic feature selection
- Suspect some features are irrelevant
- Prefer simpler, sparse models

#### **3. Elastic Net (L1 + L2 Regularization)**

**Mathematical Formula:**
```
Cost = MSE + α₁ × Σ|βᵢ| + α₂ × Σ(βᵢ)²

Combines both L1 and L2 penalties
```

**How it works:**
- Balances Ridge and Lasso benefits
- Can select features while handling multicollinearity
- More stable than Lasso with correlated features

**When to use:**
- Want both feature selection and multicollinearity handling
- Have groups of correlated features
- Need balance between sparsity and stability

### Real-World Applications

#### **Business Applications:**
- **Sales Forecasting**: Predict sales based on marketing spend, seasonality
- **Risk Assessment**: Credit scoring using income, employment history
- **Pricing Models**: Determine product prices based on costs, competition
- **Demand Prediction**: Forecast demand using historical data, external factors

#### **Scientific Applications:**
- **Medical Research**: Predict treatment outcomes based on patient characteristics
- **Economics**: Model GDP growth using various economic indicators
- **Environmental**: Predict pollution levels using weather, traffic data
- **Agriculture**: Crop yield prediction using weather, soil conditions

## Non-Linear Regression

### What is Non-Linear Regression?

**Non-linear regression** models relationships where the output is not a linear combination of input features. The relationship between X and Y follows a curved, exponential, logarithmic, or other non-linear pattern.

### Why Use Non-Linear Regression?

#### **Limitations of Linear Models:**
```
Linear Model Limitation:
X: [1, 2, 3, 4, 5]
Y: [1, 4, 9, 16, 25] (Y = X²)

Linear fit: Y = 5X - 5 (poor fit)
Non-linear fit: Y = X² (perfect fit)
```

#### **Real-World Non-Linear Relationships:**
- **Exponential Growth**: Population growth, viral spread, compound interest
- **Logarithmic**: Learning curves, diminishing returns
- **Polynomial**: Physical phenomena, engineering relationships
- **Sinusoidal**: Seasonal patterns, periodic behavior

### Types of Non-Linear Regression

#### **1. Polynomial Regression**

**Definition**: Uses polynomial terms (X², X³, etc.) while remaining linear in coefficients

**Mathematical Form:**
```
Y = β₀ + β₁X + β₂X² + β₃X³ + ... + βₙXⁿ

Example (Quadratic):
Y = β₀ + β₁X + β₂X²
```

**Example Application:**
```
Projectile Motion:
Height = β₀ + β₁×Time + β₂×Time²

Where β₂ is negative (gravity effect)
```

**Pros:**
- Still uses linear regression algorithms
- Can model curved relationships
- Easy to interpret lower-order terms

**Cons:**
- High-degree polynomials can overfit
- Extrapolation beyond data range is dangerous
- Can be unstable at boundaries

#### **2. Exponential Regression**

**Mathematical Forms:**
```
Exponential Growth: Y = a × e^(bX)
Exponential Decay: Y = a × e^(-bX)
Power Law: Y = a × X^b
```

**Examples:**
```
Population Growth: Population = P₀ × e^(rt)
Radioactive Decay: Amount = A₀ × e^(-λt)
Power Law: Metabolic Rate = a × Mass^0.75
```

**Applications:**
- Population dynamics
- Radioactive decay
- Compound interest
- Viral spread models

#### **3. Logarithmic Regression**

**Mathematical Form:**
```
Y = a + b × ln(X)
Y = a + b × log(X)
```

**Example:**
```
Learning Curve: Performance = a + b × ln(Practice_Hours)
Shows diminishing returns - each additional hour helps less
```

**Applications:**
- Learning curves
- Diminishing returns in economics
- Signal processing
- Psychological models

#### **4. Logistic/Sigmoid Regression**

**Mathematical Form:**
```
Y = L / (1 + e^(-k(X-x₀)))

Where:
- L = maximum value (carrying capacity)
- k = growth rate
- x₀ = midpoint
```

**S-Shaped Curve:**
```
     L |     ___
       |    /
       |   /
       |  /
     0 |_/_________ X
       
Growth starts slow, accelerates, then plateaus
```

**Applications:**
- Population growth with carrying capacity
- Technology adoption curves
- Market saturation models
- Biological growth processes

### Advanced Non-Linear Methods

#### **1. Decision Trees for Regression**

**How it works:**
- Splits data based on feature values
- Creates regions with constant predictions
- Can capture complex non-linear patterns

**Advantages:**
- No assumptions about relationship form
- Handles mixed data types
- Automatic feature selection
- Easy to interpret

**Disadvantages:**
- Can overfit easily
- Unstable (small data changes cause large tree changes)
- Biased toward features with many possible splits

#### **2. Random Forest Regression**

**How it works:**
- Combines multiple decision trees
- Each tree trained on random subset of data and features
- Final prediction = average of all tree predictions

**Advantages:**
- Reduces overfitting compared to single trees
- Handles non-linear relationships well
- Provides feature importance scores
- Works with missing values

**Example:**
```
Forest of 100 trees:
Tree 1 predicts: $250,000
Tree 2 predicts: $245,000
Tree 3 predicts: $255,000
...
Tree 100 predicts: $248,000

Final prediction: Average = $249,500
```

#### **3. Support Vector Regression (SVR)**

**How it works:**
- Uses kernel functions to map data to higher dimensions
- Finds optimal hyperplane in higher-dimensional space
- Common kernels: RBF (Gaussian), polynomial, sigmoid

**Kernel Trick:**
```
Original space: Cannot separate with line
Higher dimension: Can separate with hyperplane
Map back: Creates non-linear boundary in original space
```

**Advantages:**
- Effective in high dimensions
- Memory efficient
- Versatile (different kernel functions)

**Disadvantages:**
- No probabilistic output
- Sensitive to feature scaling
- Hard to interpret

#### **4. Neural Networks for Regression**

**How it works:**
- Multiple layers of interconnected nodes
- Each node applies non-linear activation function
- Can approximate any continuous function (universal approximator)

**Simple Neural Network:**
```
Input → Hidden Layer → Output
X₁ ──→ [Neuron] ──→ Ŷ
X₂ ──→ [Neuron] ──→
X₃ ──→ [Neuron] ──→
```

**Advantages:**
- Can model extremely complex relationships
- Automatic feature engineering
- Works with large datasets

**Disadvantages:**
- Black box (hard to interpret)
- Requires lots of data
- Prone to overfitting
- Many hyperparameters to tune

### Choosing Between Linear and Non-Linear

#### **Decision Framework:**

| Factor | Linear Regression | Non-Linear Regression |
|--------|-------------------|----------------------|
| **Relationship Type** | Straight-line patterns | Curved, complex patterns |
| **Interpretability** | High (clear coefficients) | Low to moderate |
| **Training Speed** | Very fast | Slower |
| **Data Requirements** | Small to moderate | Moderate to large |
| **Overfitting Risk** | Low (with regularization) | Higher |
| **Feature Engineering** | Manual (polynomials, interactions) | Automatic |
| **Extrapolation** | More reliable | Less reliable |

#### **When to Choose Linear:**
✅ Relationship appears linear in scatter plots  
✅ Need interpretable model for business decisions  
✅ Limited data available  
✅ Fast training/prediction required  
✅ Stable, reliable predictions needed  
✅ Statistical inference required (p-values, confidence intervals)  

#### **When to Choose Non-Linear:**
✅ Clear non-linear patterns in data  
✅ Accuracy more important than interpretability  
✅ Sufficient data for training  
✅ Complex feature interactions expected  
✅ Domain knowledge suggests non-linear relationships  

### Model Selection Process

#### **Step 1: Exploratory Data Analysis**
```python
# Visualize relationships
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plots for each feature vs target
for feature in features:
    plt.scatter(X[feature], y)
    plt.xlabel(feature)
    plt.ylabel('Target')
    plt.title(f'{feature} vs Target')
    plt.show()

# Correlation matrix
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True)
```

#### **Step 2: Start Simple**
```python
# Always start with linear regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Fit linear model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)

# Evaluate
mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

print(f"Linear Regression - MSE: {mse_linear:.2f}, R²: {r2_linear:.2f}")
```

#### **Step 3: Try Polynomial Features**
```python
from sklearn.preprocessing import PolynomialFeatures

# Create polynomial features
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

# Fit polynomial regression
poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)
y_pred_poly = poly_model.predict(X_poly_test)

# Evaluate
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print(f"Polynomial Regression - MSE: {mse_poly:.2f}, R²: {r2_poly:.2f}")
```

#### **Step 4: Try Non-Linear Methods**
```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# SVR with RBF kernel
svr_model = SVR(kernel='rbf', C=1.0, gamma='scale')
svr_model.fit(X_train, y_train)
y_pred_svr = svr_model.predict(X_test)

# Evaluate
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

mse_svr = mean_squared_error(y_test, y_pred_svr)
r2_svr = r2_score(y_test, y_pred_svr)

print(f"Random Forest - MSE: {mse_rf:.2f}, R²: {r2_rf:.2f}")
print(f"SVR - MSE: {mse_svr:.2f}, R²: {r2_svr:.2f}")
```

#### **Step 5: Model Comparison**
```python
import pandas as pd

# Compare all models
results = pd.DataFrame({
    'Model': ['Linear', 'Polynomial', 'Random Forest', 'SVR'],
    'MSE': [mse_linear, mse_poly, mse_rf, mse_svr],
    'R²': [r2_linear, r2_poly, r2_rf, r2_svr]
})

results = results.sort_values('MSE')
print(results)
```

### Evaluation Metrics

#### **Mean Squared Error (MSE):**
```
MSE = (1/n) × Σ(actual - predicted)²

- Penalizes large errors more heavily
- Same units as target variable squared
- Lower is better
```

#### **Root Mean Squared Error (RMSE):**
```
RMSE = √MSE

- Same units as target variable
- Interpretable in original scale
- Lower is better
```

#### **Mean Absolute Error (MAE):**
```
MAE = (1/n) × Σ|actual - predicted|

- Less sensitive to outliers than MSE
- Same units as target variable
- Lower is better
```

#### **R-squared (Coefficient of Determination):**
```
R² = 1 - (SS_res / SS_tot)

Where:
- SS_res = Σ(actual - predicted)²
- SS_tot = Σ(actual - mean)²

- Range: 0 to 1 (higher is better)
- Proportion of variance explained
- 1 = perfect prediction, 0 = no better than mean
```

### Best Practices

#### **Data Preprocessing:**
✅ **Scale features**: Especially important for SVR, neural networks  
✅ **Handle missing values**: Use appropriate imputation methods  
✅ **Remove outliers**: Can significantly affect linear models  
✅ **Feature engineering**: Create domain-specific features  

#### **Model Selection:**
✅ **Cross-validation**: Use k-fold CV for robust evaluation  
✅ **Train/Validation/Test split**: Prevent overfitting  
✅ **Regularization**: Apply when appropriate  
✅ **Hyperparameter tuning**: Use grid search or random search  

#### **Model Interpretation:**
✅ **Residual analysis**: Check assumptions, identify patterns  
✅ **Feature importance**: Understand which features matter  
✅ **Partial dependence plots**: Visualize feature effects  
✅ **Learning curves**: Diagnose bias/variance issues  

### Common Pitfalls and Solutions

#### **Overfitting:**
- **Problem**: Model performs well on training but poorly on test data
- **Solutions**: Regularization, cross-validation, simpler models, more data

#### **Underfitting:**
- **Problem**: Model too simple, poor performance on both training and test
- **Solutions**: More complex models, feature engineering, polynomial terms

#### **Extrapolation:**
- **Problem**: Predictions outside training data range are unreliable
- **Solutions**: Collect more diverse data, understand model limitations

#### **Multicollinearity:**
- **Problem**: Highly correlated features cause unstable coefficients
- **Solutions**: Ridge regression, feature selection, PCA

#### **Non-constant Variance:**
- **Problem**: Error variance changes across prediction range
- **Solutions**: Transform target variable (log, sqrt), weighted regression

### Summary

#### **Linear Regression:**
- **Best for**: Simple, interpretable relationships
- **Advantages**: Fast, interpretable, statistical inference
- **Disadvantages**: Limited to linear relationships
- **Use when**: Need interpretability, linear patterns, small datasets

#### **Non-Linear Regression:**
- **Best for**: Complex, curved relationships
- **Advantages**: Flexible, can model complex patterns
- **Disadvantages**: Less interpretable, prone to overfitting
- **Use when**: Complex patterns, accuracy priority, sufficient data

#### **Key Takeaway:**
Start simple with linear regression, then increase complexity as needed. Always validate with proper train/test splits and cross-validation.
