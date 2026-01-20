# Logistic Regression Problem: Student Pass Prediction

## Problem Statement
**Predict whether a student passes an exam based on their score using logistic regression.**

## Given Data

| Student | Score | Passed (1 = Yes, 0 = No) |
|---------|-------|---------------------------|
| A       | 50    | 0                         |
| B       | 60    | 0                         |
| C       | 70    | 1                         |
| D       | 80    | 1                         |
| E       | 85    | 1                         |

## Given Logistic Regression Model
The logistic regression coefficients are:
- **z = β₀ + β₁ × Score**
- **β₀ = -8.5** (intercept)
- **β₁ = 0.1** (coefficient for Score)

## Task
**Calculate the probability of passing for a student who scored 90.**

---

## Solution: Step-by-Step Calculation

### Step 1: Understanding the Logistic Regression Model
The logistic regression model uses the **sigmoid function** to convert a linear combination (z) into a probability:

```
p(Pass) = 1 / (1 + e^(-z))
```

Where:
```
z = β₀ + β₁ × Score
z = -8.5 + 0.1 × Score
```

### Step 2: Calculate z for Score = 90
```
z = β₀ + β₁ × Score
z = -8.5 + 0.1 × 90
z = -8.5 + 9.0
z = 0.5
```

### Step 3: Apply the Sigmoid Function
```
p(Pass) = 1 / (1 + e^(-z))
p(Pass) = 1 / (1 + e^(-0.5))
p(Pass) = 1 / (1 + e^(-0.5))
```

Calculate e^(-0.5):
```
e^(-0.5) = 1/e^(0.5) ≈ 1/1.649 ≈ 0.6065
```

Therefore:
```
p(Pass) = 1 / (1 + 0.6065)
p(Pass) = 1 / 1.6065
p(Pass) ≈ 0.6225
```

### **Final Answer: The probability of passing for a student who scored 90 is approximately 62.25%**

---

## Detailed Analysis

### Verification with Training Data
Let's verify our model with the given training data:

| Student | Score | z = -8.5 + 0.1×Score | p(Pass) = 1/(1+e^(-z)) | Predicted | Actual |
|---------|-------|---------------------|-------------------------|-----------|--------|
| A       | 50    | -8.5 + 5.0 = -3.5   | 1/(1+e^3.5) = 0.029    | 0         | 0 ✓    |
| B       | 60    | -8.5 + 6.0 = -2.5   | 1/(1+e^2.5) = 0.076    | 0         | 0 ✓    |
| C       | 70    | -8.5 + 7.0 = -1.5   | 1/(1+e^1.5) = 0.182    | 0         | 1 ✗    |
| D       | 80    | -8.5 + 8.0 = -0.5   | 1/(1+e^0.5) = 0.378    | 0         | 1 ✗    |
| E       | 85    | -8.5 + 8.5 = 0.0    | 1/(1+e^0) = 0.500      | 1         | 1 ✓    |

**Decision Rule**: If p(Pass) ≥ 0.5, predict Pass (1), otherwise predict Fail (0)

### Key Observations
1. **Students C and D**: The model predicts they won't pass, but they actually did. This suggests the model might need refinement.
2. **Decision Boundary**: At score = 85, probability = 0.5 (exactly at the threshold)
3. **Student with Score 90**: With p = 0.6225, the model predicts this student will pass

### Understanding the Coefficients

#### β₀ = -8.5 (Intercept)
- Represents the log-odds of passing when score = 0
- Negative value indicates very low probability of passing with zero score
- At score = 0: z = -8.5, p(Pass) ≈ 0.0002 (0.02%)

#### β₁ = 0.1 (Score Coefficient)
- For every 1-point increase in score, the log-odds increase by 0.1
- For every 10-point increase in score, the log-odds increase by 1.0
- Positive value indicates higher scores lead to higher probability of passing

### Probability Interpretation
For a student with score 90:
- **62.25% chance of passing**
- **37.75% chance of failing**
- Since 62.25% > 50%, the model predicts: **PASS**

---

## Mathematical Deep Dive

### Why Use Sigmoid Function?
The sigmoid function has several important properties:

1. **Output Range**: Always between 0 and 1 (perfect for probabilities)
2. **S-shaped Curve**: Smooth transition from failure to success
3. **Interpretable**: Provides probability estimates, not just classifications

### Sigmoid Function Behavior
```
Score → z → p(Pass)
40    → -4.5 → 0.011 (1.1%)
50    → -3.5 → 0.029 (2.9%)
60    → -2.5 → 0.076 (7.6%)
70    → -1.5 → 0.182 (18.2%)
80    → -0.5 → 0.378 (37.8%)
85    → 0.0  → 0.500 (50.0%) ← Decision boundary
90    → 0.5  → 0.622 (62.2%) ← Our answer
95    → 1.0  → 0.731 (73.1%)
100   → 1.5  → 0.818 (81.8%)
```

### Visual Representation
```
p(Pass)
   1.0 ┤         ╭─────────
   0.8 ┤       ╭─╯
   0.6 ┤     ╭─╯     ← Score 90 (62.2%)
   0.4 ┤   ╭─╯
   0.2 ┤ ╭─╯
   0.0 ┤─╯
       └─────────────────────
       40  60  80  100  Score
```

---

## Alternative Calculation Methods

### Method 1: Using Natural Logarithm Properties
```
p = 1 / (1 + e^(-0.5))
p = 1 / (1 + 1/e^0.5)
p = e^0.5 / (e^0.5 + 1)
p = 1.649 / (1.649 + 1)
p = 1.649 / 2.649 ≈ 0.6225
```

### Method 2: Using Calculator/Computer
```python
import math
z = 0.5
p = 1 / (1 + math.exp(-z))
print(f"Probability: {p:.4f}")  # Output: 0.6225
```

---

## Model Evaluation

### Accuracy on Training Data
- Correct predictions: 3 out of 5 (60%)
- The model struggles with the middle range (scores 70-80)
- Might benefit from more training data or feature engineering

### Confidence Analysis
For score = 90:
- High confidence prediction (62.25% > 50%)
- Clear lean towards "Pass"
- But not extremely confident (not close to 90%+)

---

## Practical Implications

### For Educational Assessment
1. **Score 90**: Student has good chance of passing (62.25%)
2. **Threshold Score**: Around 85 points for 50-50 chance
3. **High Confidence Pass**: Scores above 95 (>73% probability)

### Model Limitations
1. **Simple Model**: Only considers test score
2. **Limited Data**: Only 5 training examples
3. **Real World**: Other factors matter (study time, attendance, etc.)

---

## Summary

**Answer**: A student who scored 90 has a **62.25% probability of passing** the exam.

**Key Steps**:
1. Calculate z = -8.5 + 0.1(90) = 0.5
2. Apply sigmoid: p = 1/(1 + e^(-0.5)) = 0.6225
3. Interpret: 62.25% chance of passing, so predict "PASS"

This logistic regression model transforms exam scores into pass/fail probabilities using the sigmoid function, providing both a classification (pass/fail) and the confidence level (probability) for that prediction.

---

*Problem solved on: September 13, 2025*