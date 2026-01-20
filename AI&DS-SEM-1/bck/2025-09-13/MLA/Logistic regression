# Logistic Regression - Comprehensive Study Notes

## Table of Contents
1. [Introduction](#introduction)
2. [Mathematical Foundation](#mathematical-foundation)
3. [The Sigmoid Function](#the-sigmoid-function)
4. [Cost Function](#cost-function)
5. [Gradient Descent](#gradient-descent)
6. [Example Walkthrough: Email Spam Detection](#example-walkthrough-email-spam-detection)
7. [Implementation Steps](#implementation-steps)
8. [Evaluation Metrics](#evaluation-metrics)
9. [Advantages and Disadvantages](#advantages-and-disadvantages)
10. [Key Differences from Linear Regression](#key-differences-from-linear-regression)

---

## Introduction

**Logistic Regression** is a statistical method used for **binary classification** problems. Despite its name containing "regression," it's actually a classification algorithm that predicts the probability of an instance belonging to a particular category.

### Real-World Example: Email Spam Detection
Throughout these notes, we'll use **email spam detection** as our consistent example:
- **Problem**: Classify emails as "Spam" (1) or "Not Spam" (0)
- **Features**: Number of suspicious keywords, email length, sender reputation score
- **Goal**: Predict probability that an email is spam

---

## Mathematical Foundation

### Linear vs Logistic Regression

**Linear Regression**: 
```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```
- Output: Continuous values (can be any real number)
- Problem: For classification, we need probabilities (0 to 1)

**Logistic Regression**:
```
p = 1 / (1 + e^(-(β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ)))
```
- Output: Probability values between 0 and 1
- Uses sigmoid function to transform linear combination

### Our Spam Detection Model
```
p(spam) = 1 / (1 + e^(-(β₀ + β₁×keywords + β₂×length + β₃×reputation)))
```

Where:
- `keywords`: Number of suspicious words in email
- `length`: Email length (in characters)
- `reputation`: Sender reputation score (0-10)

---

## The Sigmoid Function

### Mathematical Definition
```
σ(z) = 1 / (1 + e^(-z))
```

Where `z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ` (linear combination)

### Key Properties
1. **Output Range**: Always between 0 and 1
2. **S-shaped Curve**: Smooth transition from 0 to 1
3. **Threshold**: At z = 0, σ(z) = 0.5

### Spam Detection Example
Let's say we have an email with:
- 5 suspicious keywords
- 1000 characters length
- Sender reputation: 3

If our learned parameters are: β₀ = -2, β₁ = 0.8, β₂ = 0.001, β₃ = -0.5

```
z = -2 + 0.8(5) + 0.001(1000) + (-0.5)(3)
z = -2 + 4 + 1 - 1.5 = 1.5

p(spam) = 1 / (1 + e^(-1.5)) = 1 / (1 + 0.223) = 0.818
```

**Result**: 81.8% probability this email is spam

### Sigmoid Function Visualization
```
p(spam)
   1.0 ┤     ╭─────────
   0.9 ┤   ╭─╯
   0.8 ┤  ╭╯           ← Our example (z=1.5, p=0.818)
   0.7 ┤ ╭╯
   0.6 ┤╭╯
   0.5 ┼╯              ← Decision boundary (z=0, p=0.5)
   0.4 ┤╲
   0.3 ┤ ╲╮
   0.2 ┤  ╲╮
   0.1 ┤   ╲─╮
   0.0 ┤     ╲─────────
       └────────────────
      -4  -2   0   2   4  z
```

---

## Cost Function

### Why Not Mean Squared Error?
Mean Squared Error (used in linear regression) creates a **non-convex** cost function for logistic regression, leading to multiple local minima.

### Log-Likelihood Cost Function
For logistic regression, we use:

```
Cost(h_θ(x), y) = {
  -log(h_θ(x))     if y = 1
  -log(1 - h_θ(x)) if y = 0
}
```

**Simplified form**:
```
J(θ) = -(1/m) Σ[y*log(h_θ(x)) + (1-y)*log(1-h_θ(x))]
```

### Spam Detection Cost Calculation

Let's say we have 3 training emails:

| Email | Keywords | Length | Reputation | Actual Label (y) | Predicted p(spam) |
|-------|----------|--------|------------|------------------|-------------------|
| 1     | 8        | 500    | 2          | 1 (Spam)         | 0.9               |
| 2     | 1        | 1500   | 8          | 0 (Not Spam)     | 0.1               |
| 3     | 4        | 800    | 5          | 1 (Spam)         | 0.7               |

**Cost Calculation**:
```
Email 1: y=1, h=0.9 → Cost = -log(0.9) = 0.105
Email 2: y=0, h=0.1 → Cost = -log(1-0.1) = -log(0.9) = 0.105  
Email 3: y=1, h=0.7 → Cost = -log(0.7) = 0.357

Total Cost J(θ) = (0.105 + 0.105 + 0.357) / 3 = 0.189
```

### Cost Function Intuition
- **When y=1 (Spam)**: Cost increases as predicted probability decreases
- **When y=0 (Not Spam)**: Cost increases as predicted probability increases
- **Perfect prediction**: Cost = 0
- **Wrong prediction**: Cost → ∞

---

## Gradient Descent

### Update Rule
```
θⱼ := θⱼ - α * ∂J(θ)/∂θⱼ
```

Where the partial derivative is:
```
∂J(θ)/∂θⱼ = (1/m) Σ(h_θ(xⁱ) - yⁱ) * xⱼⁱ
```

### Spam Detection Gradient Descent Example

**Current parameters**: θ₀ = -2, θ₁ = 0.8, θ₂ = 0.001, θ₃ = -0.5
**Learning rate**: α = 0.01

For our 3 training examples:

| Email | x₀ | x₁ | x₂   | x₃ | y | h_θ(x) | Error |
|-------|----|----|------|----|----|--------|-------|
| 1     | 1  | 8  | 500  | 2  | 1  | 0.9    | -0.1  |
| 2     | 1  | 1  | 1500 | 8  | 0  | 0.1    | 0.1   |
| 3     | 1  | 4  | 800  | 5  | 1  | 0.7    | -0.3  |

**Gradient calculations**:
```
∂J/∂θ₀ = (1/3)[(-0.1×1) + (0.1×1) + (-0.3×1)] = -0.1
∂J/∂θ₁ = (1/3)[(-0.1×8) + (0.1×1) + (-0.3×4)] = -0.7
∂J/∂θ₂ = (1/3)[(-0.1×500) + (0.1×1500) + (-0.3×800)] = -13.33
∂J/∂θ₃ = (1/3)[(-0.1×2) + (0.1×8) + (-0.3×5)] = -0.2
```

**Parameter updates**:
```
θ₀ := -2 - 0.01×(-0.1) = -1.999
θ₁ := 0.8 - 0.01×(-0.7) = 0.807
θ₂ := 0.001 - 0.01×(-13.33) = 0.134
θ₃ := -0.5 - 0.01×(-0.2) = -0.498
```

---

## Example Walkthrough: Email Spam Detection

### Dataset
Let's create a small dataset with 6 emails:

| Email ID | Keywords | Length | Reputation | Label |
|----------|----------|--------|------------|-------|
| 1        | 10       | 300    | 1          | 1     |
| 2        | 2        | 1200   | 9          | 0     |
| 3        | 7        | 600    | 3          | 1     |
| 4        | 1        | 1800   | 8          | 0     |
| 5        | 6        | 450    | 4          | 1     |
| 6        | 0        | 2000   | 10         | 0     |

### Step-by-Step Solution

#### Step 1: Initialize Parameters
```
θ₀ = 0, θ₁ = 0, θ₂ = 0, θ₃ = 0
```

#### Step 2: Calculate Initial Predictions
For all emails: z = 0, so p = 1/(1+e⁰) = 0.5

#### Step 3: Calculate Initial Cost
```
J(θ) = -(1/6) Σ[y*log(0.5) + (1-y)*log(0.5)]
J(θ) = -(1/6) × 6 × log(0.5) = log(2) ≈ 0.693
```

#### Step 4: Gradient Descent Iterations

**Iteration 1:**
- Calculate gradients for all parameters
- Update parameters using learning rate α = 0.1
- New cost: ~0.65

**Iteration 100:**
- Parameters converge to approximately:
  - θ₀ = -1.5 (intercept)
  - θ₁ = 0.6 (keywords coefficient)
  - θ₂ = 0.002 (length coefficient)  
  - θ₃ = -0.4 (reputation coefficient)

#### Step 5: Final Model
```
p(spam) = 1 / (1 + e^(-(-1.5 + 0.6×keywords + 0.002×length - 0.4×reputation)))
```

### Making Predictions

**New email**: 5 keywords, 800 characters, reputation = 6
```
z = -1.5 + 0.6(5) + 0.002(800) - 0.4(6)
z = -1.5 + 3 + 1.6 - 2.4 = 0.7

p(spam) = 1 / (1 + e^(-0.7)) = 0.668
```

**Decision**: Since p > 0.5, classify as SPAM

---

## Implementation Steps

### 1. Data Preprocessing
```python
# Normalize features (important for gradient descent)
keywords_norm = (keywords - mean_keywords) / std_keywords
length_norm = (length - mean_length) / std_length
reputation_norm = (reputation - mean_reputation) / std_reputation
```

### 2. Feature Matrix Creation
```python
# X matrix with bias term
X = [[1, keywords_norm[i], length_norm[i], reputation_norm[i]] 
     for i in range(n_samples)]
```

### 3. Sigmoid Function Implementation
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

### 4. Cost Function Implementation
```python
def cost_function(X, y, theta):
    m = len(y)
    h = sigmoid(X @ theta)
    cost = -(1/m) * (y @ np.log(h) + (1-y) @ np.log(1-h))
    return cost
```

### 5. Gradient Descent Implementation
```python
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    costs = []
    
    for i in range(iterations):
        h = sigmoid(X @ theta)
        gradient = (1/m) * X.T @ (h - y)
        theta = theta - alpha * gradient
        costs.append(cost_function(X, y, theta))
    
    return theta, costs
```

---

## Evaluation Metrics

Using our spam detection example with test predictions:

### Confusion Matrix
```
                 Predicted
                Spam  Not Spam
Actual   Spam    85      15     (100 actual spam)
      Not Spam  10      190     (200 actual not spam)
```

### Key Metrics

#### 1. Accuracy
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
Accuracy = (85 + 190) / (85 + 190 + 10 + 15) = 275/300 = 0.917 (91.7%)
```

#### 2. Precision
```
Precision = TP / (TP + FP)
Precision = 85 / (85 + 10) = 85/95 = 0.895 (89.5%)
```
*"Of all emails predicted as spam, 89.5% actually were spam"*

#### 3. Recall (Sensitivity)
```
Recall = TP / (TP + FN)
Recall = 85 / (85 + 15) = 85/100 = 0.85 (85%)
```
*"Of all actual spam emails, we correctly identified 85%"*

#### 4. Specificity
```
Specificity = TN / (TN + FP)
Specificity = 190 / (190 + 10) = 190/200 = 0.95 (95%)
```
*"Of all legitimate emails, 95% were correctly classified"*

#### 5. F1-Score
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
F1 = 2 × (0.895 × 0.85) / (0.895 + 0.85) = 0.872 (87.2%)
```

### ROC Curve Analysis
By varying the decision threshold (default 0.5), we can plot:
- **X-axis**: False Positive Rate = FP/(FP+TN)
- **Y-axis**: True Positive Rate = TP/(TP+FN)

**For our spam detector:**
- Threshold 0.3: Higher recall (catch more spam) but more false positives
- Threshold 0.7: Higher precision (fewer false alarms) but miss some spam
- Threshold 0.5: Balanced approach

---

## Advantages and Disadvantages

### Advantages
1. **Probabilistic Output**: Provides probability estimates, not just classifications
   - *Example*: "80% chance this email is spam" vs just "spam/not spam"

2. **No Assumptions about Data Distribution**: Works with any feature distribution
   - *Example*: Email length can be exponentially distributed, keywords can be Poisson

3. **Fast Training and Prediction**: Computationally efficient
   - *Example*: Can classify thousands of emails per second

4. **Interpretable Coefficients**: 
   - θ₁ = 0.6 means each additional keyword increases log-odds of spam by 0.6
   - θ₃ = -0.4 means higher reputation decreases spam probability

5. **No Feature Scaling Required**: (though it helps with convergence)

### Disadvantages
1. **Linear Decision Boundary**: Cannot capture complex relationships
   - *Example*: Cannot learn "emails with 2-4 keywords AND high reputation are spam"

2. **Sensitive to Outliers**: Extreme values can skew the model
   - *Example*: One email with 1000 keywords might distort the keyword coefficient

3. **Requires Large Sample Size**: Needs sufficient data for stable results
   - *Example*: Need hundreds of spam/not-spam examples for reliable parameters

4. **Independence Assumption**: Assumes features don't interact
   - *Example*: Cannot capture that "short emails with many keywords" are especially suspicious

---

## Key Differences from Linear Regression

| Aspect | Linear Regression | Logistic Regression |
|--------|------------------|-------------------|
| **Purpose** | Predicting continuous values | Binary classification |
| **Output** | Any real number | Probability (0 to 1) |
| **Function** | Linear: y = θ₀ + θ₁x₁ + ... | Sigmoid: p = 1/(1+e^(-z)) |
| **Cost Function** | Mean Squared Error | Log-likelihood |
| **Example Output** | "Email has 47.3 spam words" | "82% probability email is spam" |

### Email Example Comparison

**Same input**: Email with 5 keywords, 1000 chars, reputation 3

**Linear Regression**: 
- Output: 1.2 (meaningless for classification)
- Interpretation: Cannot determine spam/not spam

**Logistic Regression**: 
- Output: 0.82 (82% probability)
- Interpretation: Likely spam, classify as spam

---

## Summary

Logistic Regression transforms the linear regression framework to solve classification problems by:

1. **Using the sigmoid function** to convert linear combinations to probabilities
2. **Employing log-likelihood cost function** for proper optimization
3. **Applying gradient descent** to find optimal parameters
4. **Providing probabilistic interpretations** for better decision making

Our spam detection example demonstrates how a simple set of features (keywords, length, reputation) can be combined using logistic regression to make intelligent classification decisions with quantified confidence levels.

The key insight is that logistic regression doesn't just tell us "spam" or "not spam" – it tells us "how confident we are" in that decision, enabling more nuanced email filtering strategies.

---

*Last Updated: September 13, 2025*