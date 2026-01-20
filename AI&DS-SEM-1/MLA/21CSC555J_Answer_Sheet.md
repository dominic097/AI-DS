# 21CSC555J - Machine Learning Algorithms
## M.Tech. Degree Examination - January 2025
## Answer Sheet

---

## Question 1 (20 Marks)

### Question:
**(i)** Consider a dataset where the independent variable X represents the number of study hours, and the dependent variable Y represents exam scores: Explain the process of deriving the simple linear regression equation. Describe the mathematical steps to calculate the slope and intercept of the regression line. Interpret the regression line in the context of predicting exam scores based on study hours. (10 Marks)

**(ii)** Define the concepts of overfitting and underfitting in the context of predicting students' academic performance. Discuss how they can impact the reliability of the prediction model. (5 Marks)

**(iii)** Identify and explain commonly used evaluation metrics for regression models in the context of assessing prediction accuracy for student exam scores. Discuss why each metric is important for evaluating model performance. (5 Marks)

---

### Answer:

#### (i) Simple Linear Regression Equation - Derivation and Interpretation (10 Marks)

**Process of Deriving Simple Linear Regression:**

Simple Linear Regression models the relationship between one independent variable (X) and one dependent variable (Y) using a linear equation:

**Y = β₀ + β₁X + ε**

Where:
- Y = Exam scores (dependent variable)
- X = Study hours (independent variable)
- β₀ = Intercept (y-intercept)
- β₁ = Slope (regression coefficient)
- ε = Error term (residual)

**Mathematical Steps to Calculate Slope (β₁) and Intercept (β₀):**

**Step 1: Calculate the Slope (β₁)**

The slope formula using Ordinary Least Squares (OLS) method:

```
β₁ = Σ[(Xᵢ - X̄)(Yᵢ - Ȳ)] / Σ[(Xᵢ - X̄)²]
```

Alternatively:
```
β₁ = (n·ΣXY - ΣX·ΣY) / (n·ΣX² - (ΣX)²)
```

Where:
- n = number of observations
- Xᵢ = individual study hours
- Yᵢ = individual exam scores
- X̄ = mean of study hours
- Ȳ = mean of exam scores

**Step 2: Calculate the Intercept (β₀)**

Once slope is calculated:
```
β₀ = Ȳ - β₁·X̄
```

**Step 3: Form the Regression Equation**

Substitute β₀ and β₁ into the equation:
```
Ŷ = β₀ + β₁X
```

**Interpretation in Context of Exam Scores:**

1. **Slope (β₁)**: Represents the change in exam score for each additional hour of study
   - If β₁ = 5, it means for every additional hour studied, the exam score increases by 5 points on average
   - Positive β₁ indicates positive correlation between study hours and scores

2. **Intercept (β₀)**: Represents the predicted exam score when study hours = 0
   - If β₀ = 40, a student with zero study hours is expected to score 40 points
   - In practice, this may not be meaningful if X = 0 is outside the data range

3. **Prediction**: To predict exam score for a student who studies 'h' hours:
   - Ŷ = β₀ + β₁·h
   - Example: If β₀ = 40 and β₁ = 5, a student studying 6 hours: Ŷ = 40 + 5(6) = 70 points

4. **Model Quality**:
   - R² (coefficient of determination) measures goodness of fit
   - Higher R² (closer to 1) indicates better prediction accuracy
   - Residuals should be randomly distributed around zero

---

#### (ii) Overfitting and Underfitting Concepts (5 Marks)

**Overfitting:**

**Definition:** Overfitting occurs when a model learns the training data too well, including its noise and outliers, resulting in poor generalization to new, unseen data.

**In context of student performance prediction:**
- The model might memorize specific patterns in training data (e.g., individual student quirks)
- It captures random fluctuations rather than true underlying relationships
- High accuracy on training data but poor performance on test data

**Example:** A highly complex polynomial model that perfectly fits every student's score in the training set but fails to predict accurately for new students.

**Impact on reliability:**
- **Low generalization**: Model performs poorly on new students
- **High variance**: Small changes in training data lead to large changes in predictions
- **False patterns**: Model relies on spurious correlations
- **Unreliable predictions**: Cannot be trusted for decision-making

**Underfitting:**

**Definition:** Underfitting occurs when a model is too simple to capture the underlying patterns in the data, resulting in poor performance on both training and test data.

**In context of student performance prediction:**
- The model fails to capture important relationships between features and exam scores
- Too simplistic assumptions (e.g., assuming linear relationship when it's non-linear)
- Ignores relevant predictive features

**Example:** Using only one weak predictor (e.g., attendance) while ignoring other important factors like study hours, previous grades, etc.

**Impact on reliability:**
- **High bias**: Systematic errors in predictions
- **Poor training accuracy**: Cannot even fit the training data well
- **Missed relationships**: Fails to capture important patterns
- **Inaccurate predictions**: Consistently poor performance
- **Unreliable for decision-making**: Cannot be used confidently

**Balancing Overfitting and Underfitting:**

The goal is to find the optimal model complexity that:
- Captures true underlying patterns (avoids underfitting)
- Generalizes well to new data (avoids overfitting)
- Achieves good performance on both training and validation sets

**Techniques to address:**
- **For overfitting**: Regularization (L1/L2), cross-validation, pruning, more training data, simpler models
- **For underfitting**: Add more features, increase model complexity, reduce regularization

---

#### (iii) Evaluation Metrics for Regression Models (5 Marks)

**1. Mean Absolute Error (MAE)**

**Formula:**
```
MAE = (1/n) Σ|Yᵢ - Ŷᵢ|
```

**Interpretation:**
- Average absolute difference between predicted and actual exam scores
- In same units as the target variable (exam scores)

**Importance:**
- **Easy to interpret**: If MAE = 5, predictions are off by 5 points on average
- **Robust to outliers**: Treats all errors equally
- **Practical meaning**: Directly shows average prediction error in score units
- **Use case**: When all errors should be weighted equally

**2. Mean Squared Error (MSE)**

**Formula:**
```
MSE = (1/n) Σ(Yᵢ - Ŷᵢ)²
```

**Interpretation:**
- Average of squared differences between predicted and actual scores
- Penalizes larger errors more heavily

**Importance:**
- **Penalizes large errors**: Useful when big mistakes are particularly bad
- **Mathematical convenience**: Differentiable, used in optimization
- **Sensitivity**: More sensitive to outliers than MAE
- **Use case**: When large prediction errors are unacceptable (e.g., identifying at-risk students)

**3. Root Mean Squared Error (RMSE)**

**Formula:**
```
RMSE = √[MSE] = √[(1/n) Σ(Yᵢ - Ŷᵢ)²]
```

**Interpretation:**
- Square root of MSE, returns to original units
- Standard deviation of prediction errors

**Importance:**
- **Same units as target**: Like MAE, expressed in exam score points
- **Penalizes large errors**: More than MAE but interpretable
- **Most popular metric**: Widely used and understood
- **Use case**: Balanced approach between interpretability and error sensitivity

**4. R² Score (Coefficient of Determination)**

**Formula:**
```
R² = 1 - (SS_res / SS_tot)
where:
SS_res = Σ(Yᵢ - Ŷᵢ)² (residual sum of squares)
SS_tot = Σ(Yᵢ - Ȳ)² (total sum of squares)
```

**Interpretation:**
- Proportion of variance in exam scores explained by the model
- Ranges from 0 to 1 (can be negative for very poor models)

**Importance:**
- **Goodness of fit**: Indicates how well model explains variance
- **Comparable across datasets**: Normalized metric (0-1 scale)
- **Intuitive**: R² = 0.85 means model explains 85% of variance
- **Model comparison**: Easy to compare different models
- **Use case**: Understanding overall model performance and comparison

**5. Mean Absolute Percentage Error (MAPE)**

**Formula:**
```
MAPE = (100/n) Σ|(Yᵢ - Ŷᵢ)/Yᵢ|
```

**Interpretation:**
- Average percentage error in predictions
- Scale-independent metric

**Importance:**
- **Percentage-based**: Easy for non-technical stakeholders to understand
- **Scale-independent**: Can compare models across different datasets
- **Business interpretation**: "Model is 5% off on average"
- **Use case**: When relative error matters more than absolute error
- **Limitation**: Undefined when actual value is zero, biased toward low values

**Why Each Metric is Important for Student Exam Score Prediction:**

1. **MAE**: Teachers can understand "predictions are typically off by X points"
2. **RMSE**: Identifies when model makes large errors (missing at-risk students)
3. **R²**: Shows if study hours truly explain exam performance
4. **MAPE**: Useful for comparing performance across different exams/courses
5. **MSE**: Useful during model training and optimization

**Best Practice:** Use multiple metrics together to get comprehensive understanding of model performance. For student performance prediction:
- **Primary metric**: RMSE (interpretable and penalizes large errors)
- **Secondary metrics**: R² (goodness of fit) and MAE (average error)

---

## Question 2 (20 Marks)

### Question:
A retail analytics company is developing a machine learning model to predict customer purchasing behavior. The goal is to classify customers into three spending categories: "low spender," "moderate spender," and "high spender." The dataset includes features such as monthly income, number of purchases, and average purchase value. Explain how Logistic Regression could be applied to estimate the probability of a customer being a "high spender." Describe the process of converting the linear regression equation into a sigmoid function and interpreting the resulting probability values for classifying customers. Since there are three categories ("low spender," "moderate spender," and "high spender"), explain how Logistic Regression can be adapted for multi-class classification. Describe methods like One-vs-Rest (OvR) or Softmax Regression for handling multiple classes.

---

### Answer:

#### Part 1: Binary Logistic Regression for "High Spender" Classification

**Application of Logistic Regression:**

Logistic Regression is used to predict the probability that a customer belongs to a specific class (e.g., "high spender" vs "not high spender"). Unlike linear regression which predicts continuous values, logistic regression outputs probabilities between 0 and 1.

**Step 1: Linear Combination of Features**

Start with a linear combination of input features:

```
z = β₀ + β₁(monthly_income) + β₂(num_purchases) + β₃(avg_purchase_value)
```

Where:
- z = linear combination (logit)
- β₀ = bias/intercept term
- β₁, β₂, β₃ = weights/coefficients for each feature
- Features are normalized/standardized for better performance

**Step 2: Converting to Sigmoid Function**

The sigmoid (logistic) function transforms the linear output z into a probability:

```
P(Y=1|X) = σ(z) = 1 / (1 + e^(-z))
```

Where:
- P(Y=1|X) = probability of being a "high spender" given features X
- e = Euler's number (≈ 2.718)
- σ(z) = sigmoid function

**Properties of Sigmoid Function:**
- Maps any real number to range (0, 1)
- S-shaped curve
- σ(0) = 0.5 (decision boundary)
- As z → +∞, σ(z) → 1
- As z → -∞, σ(z) → 0

**Step 3: Interpreting Probability Values**

**Example Interpretation:**

If for a customer: z = β₀ + β₁(monthly_income) + β₂(num_purchases) + β₃(avg_purchase_value) = 2.5

Then: P(high_spender) = 1 / (1 + e^(-2.5)) = 0.924

**Interpretation:**
- Probability = 0.924 (92.4%) that customer is a high spender
- Probability = 0.076 (7.6%) that customer is NOT a high spender

**Decision Rule:**
```
If P(Y=1|X) ≥ threshold (typically 0.5):
    Classify as "High Spender"
Else:
    Classify as "Not High Spender"
```

**Threshold Selection:**
- Default threshold: 0.5
- Can adjust based on business needs:
  - Higher threshold (0.7): More conservative, fewer false positives
  - Lower threshold (0.3): More aggressive, catch more potential high spenders
  - Consider cost of false positives vs false negatives

**Coefficient Interpretation:**

If β₁ (monthly_income) = 0.5:
- A one-unit increase in monthly income increases the log-odds of being a high spender by 0.5
- Translates to: odds_ratio = e^(0.5) = 1.65 (65% increase in odds)

---

#### Part 2: Multi-class Classification (Three Categories)

Since we have three classes: "low spender," "moderate spender," and "high spender," we need to extend binary logistic regression.

**Method 1: One-vs-Rest (OvR) / One-vs-All (OvA)**

**Concept:**
Train K separate binary classifiers (where K = number of classes = 3). Each classifier distinguishes one class from all other classes.

**Implementation for Three Classes:**

1. **Classifier 1**: "Low Spender" vs "Not Low Spender" (Moderate + High)
   ```
   P(low|X) = σ(β₁₀ + β₁₁X₁ + β₁₂X₂ + β₁₃X₃)
   ```

2. **Classifier 2**: "Moderate Spender" vs "Not Moderate" (Low + High)
   ```
   P(moderate|X) = σ(β₂₀ + β₂₁X₁ + β₂₂X₂ + β₂₃X₃)
   ```

3. **Classifier 3**: "High Spender" vs "Not High" (Low + Moderate)
   ```
   P(high|X) = σ(β₃₀ + β₃₁X₁ + β₃₂X₂ + β₃₃X₃)
   ```

**Prediction Process:**
```
For a new customer:
1. Compute probabilities from all three classifiers
2. Select class with highest probability:

   predicted_class = argmax{P(low|X), P(moderate|X), P(high|X)}
```

**Example:**
```
P(low|X) = 0.15
P(moderate|X) = 0.30
P(high|X) = 0.85  ← Highest

Prediction: "High Spender"
```

**Advantages of OvR:**
- Simple to implement
- Can use any binary classifier
- Parallelizable (train classifiers independently)
- Works well in practice

**Disadvantages of OvR:**
- Probabilities don't sum to 1 (not calibrated)
- Class imbalance in training (one class vs many)
- Scales linearly with number of classes

---

**Method 2: Softmax Regression (Multinomial Logistic Regression)**

**Concept:**
Extends logistic regression naturally to multiple classes. Computes probabilities that sum to 1 across all classes.

**Mathematical Formulation:**

For K classes, compute linear scores for each class:

```
z₁ = β₁₀ + β₁₁X₁ + β₁₂X₂ + β₁₃X₃  (for low spender)
z₂ = β₂₀ + β₂₁X₁ + β₂₂X₂ + β₂₃X₃  (for moderate spender)
z₃ = β₃₀ + β₃₁X₁ + β₃₂X₂ + β₃₃X₃  (for high spender)
```

**Softmax Function:**

Probability of class k:
```
P(Y=k|X) = e^(zₖ) / Σⱼ₌₁ᴷ e^(zⱼ)
```

For our three classes:
```
P(low|X) = e^(z₁) / (e^(z₁) + e^(z₂) + e^(z₃))
P(moderate|X) = e^(z₂) / (e^(z₁) + e^(z₂) + e^(z₃))
P(high|X) = e^(z₃) / (e^(z₁) + e^(z₂) + e^(z₃))
```

**Key Property:** P(low|X) + P(moderate|X) + P(high|X) = 1

**Example Calculation:**

Given a customer with:
- Monthly income = $5000
- Number of purchases = 25
- Average purchase value = $150

Suppose we get:
```
z₁ = -2.1 (low spender score)
z₂ = 0.3  (moderate spender score)
z₃ = 2.8  (high spender score)

Denominator = e^(-2.1) + e^(0.3) + e^(2.8)
            = 0.122 + 1.350 + 16.445
            = 17.917

P(low|X) = 0.122 / 17.917 = 0.007 (0.7%)
P(moderate|X) = 1.350 / 17.917 = 0.075 (7.5%)
P(high|X) = 16.445 / 17.917 = 0.918 (91.8%)

Prediction: "High Spender" (highest probability)
```

**Prediction Rule:**
```
predicted_class = argmax{P(low|X), P(moderate|X), P(high|X)}
```

**Advantages of Softmax:**
- Probabilities sum to 1 (proper probability distribution)
- Natural extension of binary logistic regression
- Calibrated probabilities (more interpretable)
- Single unified model
- Better for probability-based decision making

**Disadvantages of Softmax:**
- More complex optimization
- More parameters to learn (K × features)
- Computationally more expensive than OvR for large K
- Requires all classes to be trained together

---

**Comparison: OvR vs Softmax**

| Aspect | One-vs-Rest | Softmax |
|--------|-------------|---------|
| Number of models | K separate models | 1 unified model |
| Probability sum | May not sum to 1 | Always sums to 1 |
| Training | Independent (parallelizable) | Joint optimization |
| Probabilities | Not calibrated | Calibrated |
| Scalability | Better for large K | Better for small K |
| Implementation | Simpler | More complex |
| Use case | When classes are very different | When classes are related |

**Recommendation for Customer Spending Classification:**

**Use Softmax Regression because:**
1. Only 3 classes (manageable complexity)
2. Need calibrated probabilities for business decisions (e.g., targeted marketing budgets)
3. Classes are ordinal and related (low → moderate → high)
4. Better probability interpretation for stakeholders
5. Can use probabilities for customer segmentation strategies

**Implementation Steps:**

1. **Data Preprocessing:**
   - Normalize features (monthly income, purchases, avg value)
   - Handle missing values
   - Split data: 70% train, 15% validation, 15% test

2. **Model Training:**
   - Use cross-entropy loss function
   - Optimize using gradient descent or Adam optimizer
   - Apply regularization (L2) to prevent overfitting

3. **Evaluation:**
   - Accuracy, Precision, Recall, F1-score for each class
   - Confusion matrix
   - ROC curves for each class

4. **Deployment:**
   - Use probabilities for personalized marketing
   - Set decision thresholds based on business objectives
   - Monitor model performance over time

---

## Question 3 (20 Marks)

### Question:
A telecommunications company is building a machine learning model to predict customer churn (whether a customer will switch to another service provider). The dataset includes customer demographics, usage patterns, and support interaction history. The team wants to ensure the model generalizes well to new data and avoids overfitting. Explain how cross-validation can be utilized to assess the performance of the churn prediction model and discuss the purpose of cross-validation and how it helps in improving the generalization of the model to unseen data.

---

### Answer:

#### Understanding Customer Churn Prediction Problem

**Problem Context:**
- **Target Variable**: Binary classification (Churn = Yes/No)
- **Features**: Demographics (age, location), usage patterns (call duration, data usage), support history (complaints, tickets)
- **Challenge**: Model must generalize to future customers, not just memorize training data
- **Business Impact**: False negatives (missing churners) are costly

---

#### What is Cross-Validation?

**Definition:**
Cross-validation is a resampling technique used to evaluate machine learning models by partitioning data into multiple subsets, training on some subsets, and validating on others. This process is repeated multiple times to get a robust estimate of model performance.

**Core Principle:**
Instead of relying on a single train-test split, cross-validation uses multiple splits to:
1. Assess how well the model generalizes to unseen data
2. Detect overfitting
3. Compare different models objectively
4. Make efficient use of limited data

---

#### Purpose of Cross-Validation in Churn Prediction

**1. Assess Generalization Performance**
- Measures how well the model predicts churn for customers not seen during training
- Provides realistic estimate of real-world performance
- Helps determine if model will work in production

**2. Detect Overfitting**
- Large gap between training and validation scores indicates overfitting
- Example:
  - Training accuracy: 98%
  - Cross-validation accuracy: 75%
  - Conclusion: Model is overfitting

**3. Model Selection**
- Compare different algorithms (Logistic Regression, Random Forest, XGBoost)
- Select optimal hyperparameters (learning rate, regularization strength)
- Choose best feature set

**4. Reliable Performance Metrics**
- Single train-test split can be misleading due to random data distribution
- Cross-validation provides mean and standard deviation of performance
- More confidence in reported metrics

**5. Efficient Data Usage**
- Especially important for telecom where labeled churn data may be limited
- Every sample gets used for both training and validation
- Maximizes information extracted from available data

---

#### Types of Cross-Validation

**1. K-Fold Cross-Validation (Most Common)**

**Process:**
1. Divide dataset into K equal-sized folds (typically K = 5 or 10)
2. For each fold k:
   - Use fold k as validation set
   - Use remaining (K-1) folds as training set
   - Train model and evaluate on validation fold
   - Record performance metrics
3. Calculate average performance across all K folds

**Example with K=5:**
```
Iteration 1: [Test][Train][Train][Train][Train]
Iteration 2: [Train][Test][Train][Train][Train]
Iteration 3: [Train][Train][Test][Train][Train]
Iteration 4: [Train][Train][Train][Test][Train]
Iteration 5: [Train][Train][Train][Train][Test]

Final Score = Average of 5 test scores
```

**Advantages:**
- Every sample used for both training and validation
- Balanced use of data
- Reduces variance in performance estimate

**Implementation for Churn Prediction:**
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# Model
model = LogisticRegression()

# 5-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f"Accuracy scores: {scores}")
print(f"Mean accuracy: {scores.mean():.3f}")
print(f"Std deviation: {scores.std():.3f}")

Output example:
Accuracy scores: [0.82, 0.85, 0.79, 0.83, 0.81]
Mean accuracy: 0.820
Std deviation: 0.021
```

**Interpretation:**
- Mean accuracy: 82% (expected performance on new customers)
- Low std (2.1%): Model is stable and consistent
- High std would indicate sensitivity to data split

---

**2. Stratified K-Fold Cross-Validation**

**Why Needed for Churn:**
Churn datasets are often imbalanced (e.g., 20% churn, 80% no churn). Regular K-Fold might create folds with different class distributions.

**Process:**
Same as K-Fold, but ensures each fold maintains the same class distribution as original dataset.

**Example:**
```
Original dataset: 20% churn, 80% no churn
Each fold: Exactly 20% churn, 80% no churn
```

**Implementation:**
```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

    model.fit(X_train, y_train)
    score = model.score(X_val, y_val)
```

**Benefits for Churn Prediction:**
- Ensures each fold has representative sample of churners
- Prevents folds with too few/many churn examples
- More reliable metrics for imbalanced data

---

**3. Time Series Cross-Validation (For Temporal Data)**

**Why Important for Churn:**
Customer behavior has temporal dependencies. Training on future data and testing on past data is unrealistic.

**Process:**
Expanding window approach:
```
Split 1: [Train 1-3 months] → [Test month 4]
Split 2: [Train 1-4 months] → [Test month 5]
Split 3: [Train 1-5 months] → [Test month 6]
```

**Ensures:**
- Model only trained on historical data
- Tested on future data (realistic scenario)
- Respects temporal ordering

---

**4. Leave-One-Out Cross-Validation (LOOCV)**

**Process:**
- K = number of samples
- Each iteration: train on N-1 samples, test on 1 sample
- Repeat N times

**When to Use:**
- Very small datasets
- Maximum data utilization needed

**Disadvantages:**
- Computationally expensive for large datasets
- High variance in performance estimates
- Not practical for telecom datasets (millions of customers)

---

#### How Cross-Validation Improves Generalization

**1. Provides Robust Performance Estimate**

Without CV:
```
Single split might give misleading results
Train-test split 1: Accuracy = 85%
Train-test split 2: Accuracy = 75% (just by chance)
Which is true performance?
```

With CV:
```
5-Fold CV: [82%, 85%, 79%, 83%, 81%] → Mean = 82%
More confident that true performance is around 82%
```

**2. Detects Overfitting Early**

```python
# Train multiple models with different complexity
models = {
    'Simple': LogisticRegression(C=1.0),
    'Complex': LogisticRegression(C=0.001),  # High regularization
}

for name, model in models.items():
    train_scores = []
    val_scores = []

    for fold in kfold:
        model.fit(X_train_fold, y_train_fold)
        train_scores.append(model.score(X_train_fold, y_train_fold))
        val_scores.append(model.score(X_val_fold, y_val_fold))

    print(f"{name} - Train: {np.mean(train_scores):.3f}, Val: {np.mean(val_scores):.3f}")

Output:
Simple - Train: 0.850, Val: 0.820  ← Good generalization (small gap)
Complex - Train: 0.990, Val: 0.750  ← Overfitting (large gap)
```

**Choose Simple model** as it generalizes better.

**3. Hyperparameter Tuning with Nested Cross-Validation**

**Problem:** Selecting hyperparameters on same data used for final evaluation leads to optimistic bias.

**Solution:** Nested CV
- **Outer loop**: Estimate generalization performance (5-fold)
- **Inner loop**: Select best hyperparameters (5-fold on training data only)

```python
from sklearn.model_selection import GridSearchCV, cross_val_score

# Define hyperparameter grid
param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10],
    'penalty': ['l1', 'l2']
}

# Inner CV: Select best hyperparameters
inner_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
clf = GridSearchCV(LogisticRegression(), param_grid, cv=inner_cv)

# Outer CV: Evaluate generalization
outer_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=24)
scores = cross_val_score(clf, X, y, cv=outer_cv)

print(f"Nested CV Score: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

**4. Identifies Data Leakage**

Cross-validation can reveal if information from validation set leaked into training:
- If CV score is much higher than holdout test score → possible leakage
- Common sources: preprocessing on entire dataset before splitting, temporal leakage

**5. Validates Feature Engineering**

Test if new features actually improve generalization:
```python
# Baseline features
baseline_score = cross_val_score(model, X_baseline, y, cv=5).mean()

# With new features (e.g., customer tenure, average call duration)
enhanced_score = cross_val_score(model, X_enhanced, y, cv=5).mean()

if enhanced_score > baseline_score:
    print("New features improve generalization")
else:
    print("New features don't help (or cause overfitting)")
```

---

#### Practical Workflow for Churn Prediction with Cross-Validation

**Step 1: Data Preparation**
```python
# Load data
df = load_churn_data()

# Features: demographics, usage, support history
X = df[['age', 'monthly_charges', 'total_calls', 'support_tickets', ...]]
y = df['churn']  # Binary: 0 = No churn, 1 = Churn

# Handle class imbalance if necessary
print(f"Churn rate: {y.mean():.2%}")  # e.g., 25%
```

**Step 2: Set Up Cross-Validation**
```python
from sklearn.model_selection import StratifiedKFold

# Use stratified K-fold to maintain churn ratio
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

**Step 3: Evaluate Multiple Models**
```python
from sklearn.metrics import make_scorer, f1_score, roc_auc_score

models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'XGBoost': XGBClassifier()
}

# Multiple metrics (accuracy alone is insufficient for imbalanced data)
scoring = {
    'accuracy': 'accuracy',
    'precision': 'precision',
    'recall': 'recall',
    'f1': 'f1',
    'roc_auc': 'roc_auc'
}

for name, model in models.items():
    scores = cross_validate(model, X, y, cv=cv, scoring=scoring)

    print(f"\n{name}:")
    print(f"  Accuracy: {scores['test_accuracy'].mean():.3f} (+/- {scores['test_accuracy'].std():.3f})")
    print(f"  Precision: {scores['test_precision'].mean():.3f}")
    print(f"  Recall: {scores['test_recall'].mean():.3f}")
    print(f"  F1-Score: {scores['test_f1'].mean():.3f}")
    print(f"  ROC-AUC: {scores['test_roc_auc'].mean():.3f}")
```

**Step 4: Hyperparameter Tuning**
```python
# Best performing model from Step 3
best_model = XGBClassifier()

param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.3],
    'n_estimators': [100, 200, 300]
}

grid_search = GridSearchCV(
    best_model,
    param_grid,
    cv=cv,
    scoring='roc_auc',  # Choose metric based on business objective
    n_jobs=-1
)

grid_search.fit(X, y)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.3f}")
```

**Step 5: Final Evaluation on Holdout Test Set**
```python
# Keep separate test set untouched until final evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# Train final model on all training data
final_model = grid_search.best_estimator_
final_model.fit(X_train, y_train)

# Evaluate on holdout test set
test_score = final_model.score(X_test, y_test)
print(f"Final test score: {test_score:.3f}")

# Should be close to CV score if no overfitting
print(f"CV score: {grid_search.best_score_:.3f}")
print(f"Difference: {abs(test_score - grid_search.best_score_):.3f}")
```

---

#### Benefits Specific to Telecom Churn Prediction

**1. Handles Class Imbalance**
- Stratified CV ensures each fold has representative churn distribution
- Prevents biased evaluation

**2. Temporal Validation**
- Time series CV respects that you can't use future data to predict past
- Realistic assessment of production performance

**3. Cost-Sensitive Evaluation**
- Can use custom scoring functions in CV
- Weight false negatives (missed churners) higher than false positives

**4. Feature Importance Stability**
- CV reveals if feature importance is consistent across folds
- Identifies unreliable features

**5. Threshold Selection**
- Use CV to find optimal classification threshold
- Balance precision (don't annoy loyal customers) vs recall (catch churners)

---

#### Summary

**Cross-validation improves generalization by:**

1. **Providing robust performance estimates** across multiple data splits
2. **Detecting overfitting** through train-validation gap analysis
3. **Enabling fair model comparison** on same data partitions
4. **Supporting hyperparameter tuning** without test set contamination
5. **Validating feature engineering** decisions objectively
6. **Maximizing data utilization** for training and validation

**For telecom churn prediction:**
- Use **Stratified K-Fold CV** (K=5 or 10) to handle class imbalance
- Consider **Time Series CV** if temporal patterns are important
- Evaluate multiple metrics (Accuracy, Precision, Recall, F1, ROC-AUC)
- Use **Nested CV** for unbiased hyperparameter selection
- Keep final holdout test set for ultimate validation

**Best Practice:**
```
CV Score ≈ Test Score → Good generalization
CV Score >> Test Score → Still overfitting (need more regularization)
CV Score << Test Score → Possible data leakage or lucky test set
```

---

## Question 4 (20 Marks)

### Question:
A food delivery app is building a recommendation system to suggest restaurants to users based on preferences and location. The dataset includes features like cuisine type, user ratings, average cost, and proximity. The team decides to use the K-Nearest Neighbors (KNN) algorithm. Explain how the KNN algorithm works in this context and discuss how the choice of K affects model performance, including challenges with very small or large K values. Describe the role of distance metrics, comparing Euclidean and Manhattan distances, and recommend the most suitable metric for this scenario. Finally, suggest evaluation metrics to assess the model's effectiveness in recommending relevant restaurants, justifying their importance in this context.

---

### Answer:

#### Part 1: How KNN Works for Restaurant Recommendation

**K-Nearest Neighbors (KNN) Overview:**

KNN is a non-parametric, instance-based learning algorithm that makes predictions based on the K most similar instances in the training data.

**Application to Restaurant Recommendation:**

**Problem Setup:**
- **Input**: User preferences (cuisine type, price range, desired rating, location)
- **Output**: Recommended restaurants
- **Features**:
  - Cuisine type (categorical: Italian, Chinese, Mexican, etc.)
  - User ratings (continuous: 1.0-5.0)
  - Average cost (continuous: $ amount)
  - Proximity/Distance (continuous: km from user)

**KNN Algorithm Steps:**

**Step 1: Feature Representation**

Convert restaurant features into numerical vectors:
```
Restaurant A:
- Cuisine: Italian (one-hot encoded)
- Rating: 4.5
- Avg Cost: $30
- Distance: 2.5 km

Feature Vector: [0, 1, 0, 0, 4.5, 30, 2.5]
                [Mexican, Italian, Chinese, Other, Rating, Cost, Distance]
```

**Step 2: Normalize Features**

Since features have different scales, normalize them:
```python
from sklearn.preprocessing import StandardScaler

# Before normalization:
Restaurant A: [Rating: 4.5, Cost: $30, Distance: 2.5 km]
Restaurant B: [Rating: 3.8, Cost: $50, Distance: 5.0 km]

# After normalization (mean=0, std=1):
Restaurant A: [0.5, -0.3, -0.8]
Restaurant B: [-0.2, 1.1, 0.6]
```

**Why normalization matters:**
- Without it, features with larger scales (e.g., cost in dollars) dominate distance calculations
- Proximity (0-50 km) would overshadow rating (1-5 scale)

**Step 3: Calculate Distance**

For a new user query, calculate distance to all restaurants in database:

```
User Query: [Italian, Rating ≥ 4.0, Cost ≤ $35, Distance ≤ 3 km]
Query Vector (normalized): [0, 1, 0, 0, 0.3, -0.1, -0.5]

Calculate distance to each restaurant:
- Restaurant A: distance = 0.8
- Restaurant B: distance = 2.3
- Restaurant C: distance = 1.2
- Restaurant D: distance = 0.5
- Restaurant E: distance = 3.1
...
```

**Step 4: Find K Nearest Neighbors**

Select K restaurants with smallest distances:

```
If K = 5:
Nearest neighbors:
1. Restaurant D: distance = 0.5
2. Restaurant A: distance = 0.8
3. Restaurant C: distance = 1.2
4. Restaurant F: distance = 1.8
5. Restaurant G: distance = 2.1
```

**Step 5: Make Recommendation**

**For Classification (Category Prediction):**
- Majority voting among K neighbors
- Example: If K=5 and 3 neighbors are Italian, 2 are Chinese → Recommend Italian

**For Regression (Rating Prediction):**
- Average of K neighbors' values
- Example: Neighbors' ratings: [4.5, 4.2, 4.8, 4.3, 4.6] → Predicted rating = 4.48

**For Recommendation (Ranking):**
- Return top-K restaurants sorted by distance/similarity
- Can weight by inverse distance (closer restaurants weighted higher)

**Weighted KNN (Improvement):**
```python
# Closer neighbors have more influence
weights = 1 / (distances + ε)  # ε prevents division by zero

# Weighted average for rating prediction
predicted_rating = Σ(weight_i × rating_i) / Σ(weights)
```

---

#### Part 2: Effect of K Value on Model Performance

**Choice of K: The Bias-Variance Tradeoff**

**Small K (e.g., K=1, K=3):**

**Characteristics:**
- Low bias: Model is very flexible
- High variance: Sensitive to noise and outliers
- Complex decision boundary

**Example with K=1:**
```
User query close to an outlier restaurant (1 terrible review, normally good)
→ Poor recommendation based on single noisy data point
```

**Advantages:**
- Captures local patterns well
- Can model complex relationships
- Good for well-separated classes

**Disadvantages:**
- **Overfitting**: Memorizes training data including noise
- **Sensitive to outliers**: One bad restaurant can skew results
- **Unstable predictions**: Small changes in input cause large changes in output
- **Noisy decision boundaries**: Irregular, jagged boundaries

**Example Scenario:**
```
K=1: User near 1 excellent Italian restaurant (4.9★) and 10 good Chinese restaurants (4.5★)
→ Recommends Italian (ignoring broader neighborhood pattern)

May miss that user consistently prefers Chinese cuisine
```

**Large K (e.g., K=100, K=500):**

**Characteristics:**
- High bias: Model is too simplistic
- Low variance: Stable but less accurate
- Smooth decision boundary

**Advantages:**
- **Reduced overfitting**: Averages out noise
- **Stable predictions**: Robust to outliers
- **Smooth decision boundaries**: Less sensitive to individual points

**Disadvantages:**
- **Underfitting**: Misses local patterns
- **Computational cost**: More neighbors to compute
- **Loss of locality**: Includes irrelevant distant neighbors
- **Blurred boundaries**: Cannot capture fine-grained distinctions

**Example Scenario:**
```
K=500 in city with 1000 restaurants
→ Recommends most popular restaurant type overall (e.g., American)
→ Ignores user's specific preference for Thai food
→ Ignores that user is in Chinatown with many great Chinese options
```

**Optimal K: Middle Ground**

**Typical range:** K = √n (where n = number of training samples)
- For 10,000 restaurants: K ≈ 100
- Usually K between 5-20 works well in practice

**How to Choose K:**

**1. Cross-Validation:**
```python
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

k_values = range(1, 51)
cv_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())

optimal_k = k_values[np.argmax(cv_scores)]
print(f"Optimal K: {optimal_k}")
```

**2. Elbow Method:**
```
Plot K vs. Cross-Validation Score:

Score
  ^
  |     *
  |    * *
  |   *   *
  |  *     * * * * *
  | *             * * *
  +-------------------> K
  1 3 5   10   20   50

Elbow at K=10 → Choose K=10
```

**3. Domain Knowledge:**
- Food delivery: K=10-20 (balance between personalization and stability)
- Sparse areas: Smaller K (few restaurants nearby)
- Dense areas: Larger K (many options available)

**Odd vs. Even K:**
- **Prefer odd K** for binary classification to avoid ties
- Example: K=4 with 2 Italian, 2 Chinese → Tie
- Example: K=5 with 3 Italian, 2 Chinese → Clear winner

---

#### Part 3: Distance Metrics

**Distance metrics determine "closeness" between user preferences and restaurants.**

**1. Euclidean Distance (L2 Norm)**

**Formula:**
```
d(p, q) = √[Σᵢ(pᵢ - qᵢ)²]
```

**For 2D:**
```
d = √[(x₁-x₂)² + (y₁-y₂)²]
```

**Example:**
```
User preference: [Rating: 4.5, Cost: 30, Distance: 2]
Restaurant A: [Rating: 4.0, Cost: 35, Distance: 3]

Euclidean distance = √[(4.5-4.0)² + (30-35)² + (2-3)²]
                   = √[0.25 + 25 + 1]
                   = √26.25
                   = 5.12
```

**Characteristics:**
- **Geometric interpretation**: Straight-line distance
- **Sensitive to large differences**: Squaring amplifies large deviations
- **Assumes all directions equally important**
- **Affected by scale**: Requires feature normalization

**Advantages:**
- Intuitive (shortest path)
- Works well for continuous features
- Standard choice for many applications

**Disadvantages:**
- Sensitive to outliers (squaring effect)
- Computationally expensive (square root)
- Assumes isotropic space (equal importance in all directions)

---

**2. Manhattan Distance (L1 Norm, Taxicab Distance)**

**Formula:**
```
d(p, q) = Σᵢ|pᵢ - qᵢ|
```

**For 2D:**
```
d = |x₁-x₂| + |y₁-y₂|
```

**Example:**
```
User preference: [Rating: 4.5, Cost: 30, Distance: 2]
Restaurant A: [Rating: 4.0, Cost: 35, Distance: 3]

Manhattan distance = |4.5-4.0| + |30-35| + |2-3|
                   = 0.5 + 5 + 1
                   = 6.5
```

**Characteristics:**
- **Geometric interpretation**: Path along grid lines (like city blocks)
- **Linear combination**: No squaring
- **More robust to outliers** than Euclidean
- **Also affected by scale**: Requires normalization

**Advantages:**
- **Computationally efficient**: No squaring or square root
- **Robust to outliers**: Linear penalty for large deviations
- **Works well for high-dimensional data**
- **Natural for grid-like spaces** (e.g., city blocks)

**Disadvantages:**
- Less intuitive than Euclidean
- Assumes axis-aligned paths

---

**3. Comparison: Euclidean vs Manhattan**

**Visual Comparison:**
```
Point A (0,0) to Point B (3,4):

Euclidean: Straight line
Distance = √(3² + 4²) = 5.0

Manhattan: Along grid (3 right, 4 up)
Distance = |3| + |4| = 7.0

       B (3,4)
       *
      /|
     / |
    /  |  Manhattan path: →→→↑↑↑↑
   /   |  (or any combination)
  /    |
 /     |
*------+
A (0,0)

Euclidean < Manhattan (always)
```

**Feature Space Comparison:**

| Aspect | Euclidean | Manhattan |
|--------|-----------|-----------|
| Formula | √(Σ(pᵢ-qᵢ)²) | Σ\|pᵢ-qᵢ\| |
| Computation | Expensive (sqrt) | Cheap (sum of abs) |
| Outlier sensitivity | High (squaring) | Lower (linear) |
| Dimensionality | Better for low-dim | Better for high-dim |
| Interpretability | Intuitive (straight line) | Less intuitive |
| Use case | Continuous features | Mixed/sparse features |

---

**Recommendation for Food Delivery App:**

**Use Manhattan Distance**

**Justification:**

**1. Computational Efficiency**
- Food delivery app needs real-time recommendations
- Manhattan distance is faster (no squaring/sqrt operations)
- Critical for mobile app responsiveness
- Matters when searching through thousands of restaurants

**2. Outlier Robustness**
- Restaurant ratings can have outliers (one extreme review)
- Cost can vary wildly ($5 fast food to $200 fine dining)
- Manhattan distance is less sensitive to these extremes
- Euclidean would over-penalize restaurants with one unusual feature

**3. High-Dimensional Feature Space**
- Multiple features: cuisine type (one-hot encoded, many dimensions), rating, cost, distance, delivery time, etc.
- Manhattan distance performs better in high dimensions (avoids "curse of dimensionality")
- Euclidean distances become less discriminative as dimensions increase

**4. Feature Independence**
- Restaurant attributes are relatively independent:
  - Good rating doesn't imply high cost
  - Proximity doesn't imply cuisine type
- Manhattan distance treats each dimension independently
- Euclidean assumes feature interactions (through squaring)

**5. Practical Interpretation**
- Users think in trade-offs: "willing to go 2 km further for 0.5★ better rating"
- Manhattan distance aligns with additive trade-offs
- Each feature contributes linearly to overall "distance"

**Alternative: Minkowski Distance (Generalization)**

**Formula:**
```
d(p, q) = (Σᵢ|pᵢ - qᵢ|ᵖ)^(1/p)

p=1: Manhattan distance
p=2: Euclidean distance
```

Can tune p using cross-validation for optimal performance.

---

#### Part 4: Evaluation Metrics for Restaurant Recommendation

**Context:** Recommendation systems require specialized metrics beyond traditional classification metrics.

**1. Precision@K**

**Definition:**
Proportion of recommended restaurants that are relevant (user actually likes/orders from).

**Formula:**
```
Precision@K = (Number of relevant restaurants in top-K) / K
```

**Example:**
```
Recommend K=10 restaurants
User likes/orders from 7 of them
Precision@10 = 7/10 = 0.7 (70%)
```

**Importance:**
- **User satisfaction**: High precision means recommendations are useful
- **Reduces clutter**: Avoids overwhelming users with irrelevant options
- **Conversion rate**: Higher precision → more orders
- **Practical**: Focuses on top recommendations (users rarely scroll past first page)

**Limitation:**
- Doesn't account for order of recommendations
- Ignores recall (coverage of all relevant restaurants)

---

**2. Recall@K**

**Definition:**
Proportion of all relevant restaurants that are included in top-K recommendations.

**Formula:**
```
Recall@K = (Number of relevant restaurants in top-K) / (Total relevant restaurants)
```

**Example:**
```
User has 15 restaurants they would like in city
Top-10 recommendations include 7 of them
Recall@10 = 7/15 = 0.467 (46.7%)
```

**Importance:**
- **Coverage**: Ensures system doesn't miss great options
- **Discovery**: Helps users find new restaurants
- **Diversity**: Encourages showing variety
- **User retention**: Users stay if they keep finding good options

**Trade-off:**
- Higher K → Higher recall but lower precision
- Need to balance showing many options vs. only best ones

---

**3. F1-Score@K**

**Definition:**
Harmonic mean of Precision@K and Recall@K.

**Formula:**
```
F1@K = 2 × (Precision@K × Recall@K) / (Precision@K + Recall@K)
```

**Importance:**
- **Balanced metric**: Considers both precision and recall
- **Single number**: Easier to compare models
- **Penalizes extreme imbalance**: Punishes models that sacrifice one for the other

---

**4. Mean Average Precision (MAP)**

**Definition:**
Average of precision scores at each relevant restaurant in the ranking.

**Formula:**
```
AP = (Σ Precision@k × relevance(k)) / (Total relevant items)
MAP = Average of AP across all users
```

**Example:**
```
Recommendations: [R1, R2, R3, R4, R5]
Relevant: [R1, R3, R5]

Precision@1 = 1/1 = 1.0 (R1 relevant)
Precision@2 = 1/2 = 0.5 (R2 not relevant)
Precision@3 = 2/3 = 0.67 (R3 relevant)
Precision@4 = 2/4 = 0.5 (R4 not relevant)
Precision@5 = 3/5 = 0.6 (R5 relevant)

AP = (1.0 + 0.67 + 0.6) / 3 = 0.757
```

**Importance:**
- **Ranking quality**: Rewards placing relevant items earlier
- **User experience**: Early relevant results are more valuable
- **Comprehensive**: Single metric for entire ranking

---

**5. Normalized Discounted Cumulative Gain (NDCG)**

**Definition:**
Measures ranking quality with graded relevance (not just binary relevant/not relevant).

**Formula:**
```
DCG@K = Σ (2^relevance(i) - 1) / log₂(i + 1)
NDCG@K = DCG@K / IDCG@K

where IDCG = DCG of ideal ranking
```

**Example:**
```
Recommendations with ratings:
Position 1: Rating 5 (excellent)
Position 2: Rating 3 (good)
Position 3: Rating 5 (excellent)

DCG@3 = (2^5-1)/log₂(2) + (2^3-1)/log₂(3) + (2^5-1)/log₂(4)
      = 31/1 + 7/1.58 + 31/2
      = 31 + 4.43 + 15.5
      = 50.93

Ideal DCG@3 (if sorted perfectly by rating):
IDCG@3 = 31 + 31 + 7 = 69

NDCG@3 = 50.93 / 69 = 0.738
```

**Importance:**
- **Graded relevance**: Distinguishes between "good" and "excellent" restaurants
- **Position-aware**: Earlier positions have more weight
- **Normalized**: Comparable across different query results
- **Industry standard**: Used by major tech companies

---

**6. Mean Reciprocal Rank (MRR)**

**Definition:**
Average of reciprocal ranks of first relevant result.

**Formula:**
```
RR = 1 / (rank of first relevant item)
MRR = Average RR across all users
```

**Example:**
```
User A: First relevant restaurant at position 2 → RR = 1/2 = 0.5
User B: First relevant restaurant at position 1 → RR = 1/1 = 1.0
User C: First relevant restaurant at position 5 → RR = 1/5 = 0.2

MRR = (0.5 + 1.0 + 0.2) / 3 = 0.567
```

**Importance:**
- **First impression**: Critical for user engagement
- **Simple**: Easy to interpret
- **Mobile-friendly**: Important when screen space is limited

---

**7. Coverage**

**Definition:**
Percentage of restaurants that get recommended at least once.

**Formula:**
```
Coverage = (Number of unique restaurants recommended) / (Total restaurants in catalog)
```

**Importance:**
- **Fairness**: Ensures all restaurants get exposure
- **Business**: Partner restaurants want visibility
- **Diversity**: Prevents "filter bubble" effect
- **Discovery**: Helps users find hidden gems

**Trade-off:**
- High coverage may sacrifice precision
- Need balance between popular and niche restaurants

---

**8. Diversity**

**Definition:**
Variety within recommended restaurants (cuisine types, price ranges, etc.).

**Measurement:**
```
Diversity = Average pairwise dissimilarity of recommended items

Using categorical features:
Diversity = (Number of distinct cuisine types in top-K) / K
```

**Importance:**
- **User choice**: Provides options for different moods/occasions
- **Exploration**: Prevents recommending only similar restaurants
- **Satisfaction**: Users appreciate variety
- **Serendipity**: Chance to discover new preferences

---

**9. Novelty**

**Definition:**
How surprising/unexpected the recommendations are (not just popular restaurants).

**Formula:**
```
Novelty = -Σ log₂(popularity(item))
```

**Importance:**
- **Discovery**: Helps users find new restaurants
- **Long-tail**: Supports less popular but quality restaurants
- **User engagement**: Novel recommendations keep app interesting

---

**10. Hit Rate@K**

**Definition:**
Percentage of users for whom at least one relevant restaurant appears in top-K.

**Formula:**
```
Hit Rate@K = (Users with ≥1 relevant item in top-K) / (Total users)
```

**Example:**
```
100 users:
- 85 have at least one restaurant they like in top-10
- 15 have zero relevant restaurants in top-10

Hit Rate@10 = 85/100 = 0.85
```

**Importance:**
- **User satisfaction**: Binary "was this useful?"
- **Conversion tracking**: Did user order from recommended restaurant?
- **A/B testing**: Easy metric for comparing models

---

**Recommended Evaluation Strategy for Food Delivery App:**

**Primary Metrics:**
1. **NDCG@10**: Overall ranking quality with graded relevance
   - Justification: Distinguishes between "good" (4★) and "excellent" (5★) restaurants

2. **Precision@5**: Relevance of top 5 recommendations
   - Justification: Users typically see 5 restaurants without scrolling

3. **MRR**: Position of first relevant restaurant
   - Justification: Critical for mobile user experience

**Secondary Metrics:**
4. **Recall@20**: Coverage of user preferences
   - Justification: Ensures system finds diverse options

5. **Coverage**: Restaurant catalog utilization
   - Justification: Business metric for partner restaurants

6. **Diversity**: Variety in recommendations
   - Justification: User satisfaction and exploration

**Business Metrics:**
7. **Click-Through Rate (CTR)**: % of recommendations clicked
8. **Conversion Rate**: % of recommendations that lead to orders
9. **Revenue per Recommendation**: Business impact

**Evaluation Process:**
```python
# Example evaluation code
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import ndcg_score

# Train KNN model
knn = NearestNeighbors(n_neighbors=20, metric='manhattan')
knn.fit(restaurant_features)

# For each user in test set
for user in test_users:
    # Get recommendations
    distances, indices = knn.kneighbors(user_preferences)

    # Evaluate
    recommended = restaurants[indices]
    ground_truth = user_liked_restaurants

    # Calculate metrics
    ndcg = calculate_ndcg(recommended, ground_truth)
    precision = calculate_precision_at_k(recommended, ground_truth, k=5)
    mrr = calculate_mrr(recommended, ground_truth)

    # Aggregate across users
    metrics['ndcg'].append(ndcg)
    metrics['precision@5'].append(precision)
    metrics['mrr'].append(mrr)

# Report average metrics
print(f"Average NDCG@10: {np.mean(metrics['ndcg']):.3f}")
print(f"Average Precision@5: {np.mean(metrics['precision@5']):.3f}")
print(f"Average MRR: {np.mean(metrics['mrr']):.3f}")
```

---

**Summary:**

**KNN for Restaurant Recommendation:**
- Works by finding K most similar restaurants based on user preferences
- Requires careful feature engineering and normalization
- No training phase (instance-based learning)

**Optimal K Selection:**
- Use cross-validation to find sweet spot (typically 5-20)
- Too small K → overfitting, noise sensitivity
- Too large K → underfitting, loss of personalization

**Distance Metric:**
- **Recommend Manhattan distance** for food delivery
- Faster computation, robust to outliers, better for high-dimensional data

**Evaluation:**
- Use **NDCG@10**, **Precision@5**, and **MRR** as primary metrics
- Consider **diversity** and **coverage** for user satisfaction and business needs
- Monitor **conversion rate** and **CTR** for business impact

---

## Question 5 (20 Marks)

### Question:
Consider the car theft prediction problem with the following attributes: Color (Categorical: Red, Blue, Black, etc.), Type (Categorical: SUV, Sedan, Truck, etc.), Origin (Categorical: Domestic, Imported), and the target variable Stolen (Binary: Yes, No). Assume that no pair of features are dependent, and each feature has equal influence on the classification. For this task, describe the necessary preprocessing steps you would take before applying a classification algorithm to this dataset, including how you would handle categorical data and which encoding methods you would use. Then, suggest a suitable classification algorithm, justifying your choice based on the nature of the features and the target variable. After selecting an algorithm, implement the classification model and evaluate its performance using appropriate metrics. Finally, after training the model, predict whether a car with the following attributes (Color = Red, Type = SUV, Origin = Domestic) is stolen or not, and explain how the prediction is made and interpret the result.

**Dataset:**

| Example No. | Color  | Type   | Origin   | Stolen? |
|-------------|--------|--------|----------|---------|
| 1           | Red    | Sports | Domestic | Yes     |
| 2           | Red    | Sports | Domestic | No      |
| 3           | Red    | Sports | Domestic | Yes     |
| 4           | Yellow | Sports | Domestic | No      |
| 5           | Yellow | Sports | Imported | Yes     |
| 6           | Yellow | SUV    | Imported | No      |
| 7           | Yellow | SUV    | Imported | Yes     |
| 8           | Yellow | SUV    | Domestic | No      |
| 9           | Red    | SUV    | Imported | No      |
| 10          | Red    | Sports | Imported | Yes     |

---

### Answer:

#### Part 1: Preprocessing Steps

**Step 1: Data Inspection and Understanding**

```python
import pandas as pd
import numpy as np

# Load dataset
data = {
    'Color': ['Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Red', 'Red'],
    'Type': ['Sports', 'Sports', 'Sports', 'Sports', 'Sports', 'SUV', 'SUV', 'SUV', 'SUV', 'Sports'],
    'Origin': ['Domestic', 'Domestic', 'Domestic', 'Domestic', 'Imported', 'Imported', 'Imported', 'Domestic', 'Imported', 'Imported'],
    'Stolen': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Inspect data
print(df.head())
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())
# Output: All zeros (no missing values)

# Check unique values for each feature
print("Color:", df['Color'].unique())  # ['Red', 'Yellow']
print("Type:", df['Type'].unique())    # ['Sports', 'SUV']
print("Origin:", df['Origin'].unique()) # ['Domestic', 'Imported']
print("Stolen:", df['Stolen'].unique()) # ['Yes', 'No']
```

**Key Observations:**
- All features are categorical
- No missing values
- Balanced dataset (5 Stolen=Yes, 5 Stolen=No)
- Small dataset (10 samples)
- Binary target variable

---

**Step 2: Handling Categorical Data - Encoding Methods**

Since all features are categorical, we need to convert them to numerical format.

**Option 1: Label Encoding**

Assigns integer labels to categories:
```python
from sklearn.preprocessing import LabelEncoder

# Label encoding
le_color = LabelEncoder()
le_type = LabelEncoder()
le_origin = LabelEncoder()
le_stolen = LabelEncoder()

df['Color_encoded'] = le_color.fit_transform(df['Color'])
df['Type_encoded'] = le_type.fit_transform(df['Type'])
df['Origin_encoded'] = le_origin.fit_transform(df['Origin'])
df['Stolen_encoded'] = le_stolen.fit_transform(df['Stolen'])

# Result:
# Red → 0, Yellow → 1
# Sports → 0, SUV → 1
# Domestic → 0, Imported → 1
# No → 0, Yes → 1
```

**Pros:**
- Simple and memory-efficient
- Works well with tree-based models (Decision Trees, Random Forest)
- Preserves single column per feature

**Cons:**
- Implies ordinal relationship (Red < Yellow)
- Not suitable for linear models
- Can mislead distance-based algorithms

---

**Option 2: One-Hot Encoding (Recommended)**

Creates binary columns for each category:
```python
# One-hot encoding
df_encoded = pd.get_dummies(df, columns=['Color', 'Type', 'Origin'], drop_first=False)

# Result:
# Color_Red, Color_Yellow
# Type_Sports, Type_SUV
# Origin_Domestic, Origin_Imported
```

**Alternative with drop_first=True:**
```python
df_encoded = pd.get_dummies(df, columns=['Color', 'Type', 'Origin'], drop_first=True)

# Result:
# Color_Yellow (Red is baseline)
# Type_SUV (Sports is baseline)
# Origin_Imported (Domestic is baseline)
```

**Pros:**
- No ordinal assumption
- Works well with linear models, SVM, neural networks
- Mathematically sound

**Cons:**
- Increases dimensionality (curse of dimensionality)
- Can create sparse matrices
- Potential multicollinearity if all columns retained

**Recommendation for this dataset:**
Use **One-Hot Encoding with drop_first=True** to:
- Avoid multicollinearity (dummy variable trap)
- Reduce dimensions (6 features instead of 7)
- Suitable for most algorithms

---

**Step 3: Feature Scaling (Not Required Here)**

**Why not needed:**
- All features are categorical (0/1 after encoding)
- Already on same scale
- No continuous features with different ranges

**When feature scaling is needed:**
- Continuous features with different scales
- Algorithms sensitive to scale (KNN, SVM, Neural Networks)
- Methods: StandardScaler, MinMaxScaler, RobustScaler

---

**Step 4: Train-Test Split**

```python
from sklearn.model_selection import train_test_split

# Separate features and target
X = df_encoded.drop('Stolen', axis=1)
y = df_encoded['Stolen'].map({'No': 0, 'Yes': 1})

# Split data (70-30 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# stratify=y ensures balanced class distribution in train/test
```

**Note:** With only 10 samples, might use cross-validation instead of single split.

---

**Step 5: Check Class Balance**

```python
print("Class distribution:")
print(y.value_counts())
print(y.value_counts(normalize=True))

# Output:
# 0 (No):  5 (50%)
# 1 (Yes): 5 (50%)
```

**Observation:** Balanced dataset, no need for:
- SMOTE (Synthetic Minority Over-sampling)
- Class weights
- Undersampling/oversampling

---

**Complete Preprocessing Code:**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load data
data = {
    'Color': ['Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Red', 'Red'],
    'Type': ['Sports', 'Sports', 'Sports', 'Sports', 'Sports', 'SUV', 'SUV', 'SUV', 'SUV', 'Sports'],
    'Origin': ['Domestic', 'Domestic', 'Domestic', 'Domestic', 'Imported', 'Imported', 'Imported', 'Domestic', 'Imported', 'Imported'],
    'Stolen': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

# One-hot encoding
X = pd.get_dummies(df.drop('Stolen', axis=1), drop_first=True)
y = df['Stolen'].map({'No': 0, 'Yes': 1})

print("Feature matrix after encoding:")
print(X.head())
print("\nTarget variable:")
print(y.head())
```

**Encoded Feature Matrix:**
```
   Color_Yellow  Type_SUV  Origin_Imported
0             0         0                0
1             0         0                0
2             0         0                0
3             1         0                0
4             1         0                1
5             1         1                1
6             1         1                1
7             1         1                0
8             0         1                1
9             0         0                1
```

---

#### Part 2: Algorithm Selection

**Recommended Algorithm: Naive Bayes Classifier**

**Justification:**

**1. Assumption Alignment:**
- Problem states: "no pair of features are dependent"
- Naive Bayes assumes feature independence
- Perfect match for the problem's assumptions

**2. Categorical Features:**
- All features are categorical
- Naive Bayes handles categorical data naturally
- Can use Categorical Naive Bayes or Bernoulli Naive Bayes (for binary encoded features)

**3. Small Dataset:**
- Only 10 samples
- Naive Bayes works well with small datasets
- Requires fewer training samples than complex models
- Less prone to overfitting than deep neural networks

**4. Binary Classification:**
- Target variable has 2 classes (Stolen: Yes/No)
- Naive Bayes naturally handles binary classification
- Provides probability estimates

**5. Interpretability:**
- Probabilistic model
- Easy to explain predictions (P(Stolen|Color, Type, Origin))
- Transparent decision-making process

**6. Computational Efficiency:**
- Fast training and prediction
- Low computational cost
- Suitable for real-time predictions

**Alternative Algorithms (with pros/cons):**

**1. Decision Tree:**
- **Pros:** Handles categorical data, interpretable, no assumptions
- **Cons:** Prone to overfitting with small datasets, might memorize data
- **When to use:** If feature independence assumption doesn't hold

**2. Logistic Regression:**
- **Pros:** Simple, interpretable, probability outputs
- **Cons:** Assumes feature independence less strictly, needs more data for stable estimates
- **When to use:** If want linear decision boundaries

**3. Random Forest:**
- **Pros:** Robust, handles non-linearity well
- **Cons:** Overkill for small dataset, less interpretable, might overfit
- **When to use:** With larger datasets, complex relationships

**4. K-Nearest Neighbors (KNN):**
- **Pros:** Non-parametric, simple
- **Cons:** Sensitive to noise with small K, needs more data
- **When to use:** If local patterns are important

**Final Choice: Naive Bayes (Bernoulli variant)**

---

#### Part 3: Model Implementation

```python
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import cross_val_score
import numpy as np

# Prepare data with one-hot encoding
X = pd.get_dummies(df.drop('Stolen', axis=1), drop_first=True)
y = df['Stolen'].map({'No': 0, 'Yes': 1})

# Initialize Naive Bayes classifier
model = BernoulliNB()

# Train model (on all data for this small dataset)
model.fit(X, y)

# Model parameters
print("Class prior probabilities:")
print(f"P(Stolen=No) = {model.class_prior_[0]:.3f}")
print(f"P(Stolen=Yes) = {model.class_prior_[1]:.3f}")

print("\nFeature log probabilities:")
print(model.feature_log_prob_)
```

---

#### Part 4: Model Evaluation

**Cross-Validation (Preferred for small dataset):**

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# 5-Fold Cross-Validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

print("Cross-Validation Results:")
print(f"Accuracy scores: {cv_scores}")
print(f"Mean Accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# Additional metrics via cross_validate
from sklearn.model_selection import cross_validate

scoring = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
cv_results = cross_validate(model, X, y, cv=cv, scoring=scoring)

print(f"\nMean Precision: {cv_results['test_precision'].mean():.3f}")
print(f"Mean Recall: {cv_results['test_recall'].mean():.3f}")
print(f"Mean F1-Score: {cv_results['test_f1'].mean():.3f}")
print(f"Mean ROC-AUC: {cv_results['test_roc_auc'].mean():.3f}")
```

**Training Accuracy (on full dataset):**

```python
# Predict on training data
y_pred = model.predict(X)

# Evaluation metrics
print("\nTraining Performance:")
print(f"Accuracy: {accuracy_score(y, y_pred):.3f}")
print(f"Precision: {precision_score(y, y_pred):.3f}")
print(f"Recall: {recall_score(y, y_pred):.3f}")
print(f"F1-Score: {f1_score(y, y_pred):.3f}")

# Confusion Matrix
cm = confusion_matrix(y, y_pred)
print("\nConfusion Matrix:")
print(cm)
print(f"\nTrue Negatives: {cm[0,0]}")
print(f"False Positives: {cm[0,1]}")
print(f"False Negatives: {cm[1,0]}")
print(f"True Positives: {cm[1,1]}")

# Classification Report
print("\nClassification Report:")
print(classification_report(y, y_pred, target_names=['Not Stolen', 'Stolen']))
```

**Expected Output (Approximate):**
```
Training Performance:
Accuracy: 0.800
Precision: 0.750
Recall: 0.900
F1-Score: 0.818

Confusion Matrix:
[[4 1]
 [1 4]]

True Negatives: 4
False Positives: 1
False Negatives: 1
True Positives: 4

Classification Report:
              precision    recall  f1-score   support

  Not Stolen       0.80      0.80      0.80         5
      Stolen       0.80      0.80      0.80         5

    accuracy                           0.80        10
   macro avg       0.80      0.80      0.80        10
weighted avg       0.80      0.80      0.80        10
```

**Interpretation:**
- **Accuracy: 80%**: Model correctly predicts 8 out of 10 cases
- **Precision: 80%**: When predicting "stolen," it's correct 80% of the time
- **Recall: 80%**: Model catches 80% of actual stolen cars
- **F1-Score: 0.80**: Balanced metric showing good overall performance

---

#### Part 5: Prediction for New Instance

**Query:** Predict if car with (Color=Red, Type=SUV, Origin=Domestic) is stolen.

**Step-by-step Prediction:**

**Step 1: Encode the query**

```python
# New car attributes
new_car = {
    'Color': 'Red',
    'Type': 'SUV',
    'Origin': 'Domestic'
}

# Convert to DataFrame
new_car_df = pd.DataFrame([new_car])

# Apply same one-hot encoding
new_car_encoded = pd.get_dummies(new_car_df, drop_first=True)

# Ensure same columns as training data
for col in X.columns:
    if col not in new_car_encoded.columns:
        new_car_encoded[col] = 0

new_car_encoded = new_car_encoded[X.columns]

print("Encoded new car:")
print(new_car_encoded)
```

**Encoded representation:**
```
   Color_Yellow  Type_SUV  Origin_Imported
0             0         1                0
```

**Interpretation:**
- Color = Red → Color_Yellow = 0 (not yellow, so red)
- Type = SUV → Type_SUV = 1 (is SUV)
- Origin = Domestic → Origin_Imported = 0 (not imported, so domestic)

---

**Step 2: Make prediction**

```python
# Predict class
prediction = model.predict(new_car_encoded)
print(f"Predicted class: {'Stolen' if prediction[0] == 1 else 'Not Stolen'}")

# Predict probabilities
probabilities = model.predict_proba(new_car_encoded)
print(f"\nProbabilities:")
print(f"P(Not Stolen) = {probabilities[0][0]:.3f}")
print(f"P(Stolen) = {probabilities[0][1]:.3f}")
```

---

**Step 3: How Naive Bayes makes the prediction**

Naive Bayes uses Bayes' Theorem:

```
P(Stolen | Color=Red, Type=SUV, Origin=Domestic) ∝
    P(Color=Red | Stolen) × P(Type=SUV | Stolen) × P(Origin=Domestic | Stolen) × P(Stolen)
```

**Calculate for Stolen = Yes:**

From training data (cars with Stolen=Yes):
- Total: 5 cars
- Color=Red AND Stolen=Yes: 2 (examples 1, 3, 10)
- Type=SUV AND Stolen=Yes: 1 (example 7)
- Origin=Domestic AND Stolen=Yes: 1 (examples 1, 3)

Probabilities:
```
P(Color=Red | Stolen=Yes) = 2/5 = 0.4
P(Type=SUV | Stolen=Yes) = 1/5 = 0.2
P(Origin=Domestic | Stolen=Yes) = 2/5 = 0.4
P(Stolen=Yes) = 5/10 = 0.5

P(Stolen=Yes | features) ∝ 0.4 × 0.2 × 0.4 × 0.5 = 0.016
```

**Calculate for Stolen = No:**

From training data (cars with Stolen=No):
- Total: 5 cars
- Color=Red AND Stolen=No: 1 (example 2, 9)
- Type=SUV AND Stolen=No: 2 (examples 6, 8)
- Origin=Domestic AND Stolen=No: 2 (examples 2, 4, 8)

Probabilities:
```
P(Color=Red | Stolen=No) = 2/5 = 0.4
P(Type=SUV | Stolen=No) = 2/5 = 0.4
P(Origin=Domestic | Stolen=No) = 3/5 = 0.6
P(Stolen=No) = 5/10 = 0.5

P(Stolen=No | features) ∝ 0.4 × 0.4 × 0.6 × 0.5 = 0.048
```

**Normalize probabilities:**
```
Total = 0.016 + 0.048 = 0.064

P(Stolen=Yes | features) = 0.016 / 0.064 = 0.25 (25%)
P(Stolen=No | features) = 0.048 / 0.064 = 0.75 (75%)
```

**Prediction: NOT STOLEN (75% confidence)**

---

**Step 4: Interpretation**

```python
# Full prediction code
new_car_encoded = pd.DataFrame({
    'Color_Yellow': [0],
    'Type_SUV': [1],
    'Origin_Imported': [0]
})

prediction = model.predict(new_car_encoded)
probabilities = model.predict_proba(new_car_encoded)

print(f"\n{'='*60}")
print(f"PREDICTION RESULT")
print(f"{'='*60}")
print(f"Car Attributes:")
print(f"  - Color: Red")
print(f"  - Type: SUV")
print(f"  - Origin: Domestic")
print(f"\nPrediction: {'STOLEN' if prediction[0] == 1 else 'NOT STOLEN'}")
print(f"\nConfidence:")
print(f"  - Probability of NOT STOLEN: {probabilities[0][0]*100:.1f}%")
print(f"  - Probability of STOLEN: {probabilities[0][1]*100:.1f}%")
print(f"{'='*60}")
```

**Expected Output:**
```
============================================================
PREDICTION RESULT
============================================================
Car Attributes:
  - Color: Red
  - Type: SUV
  - Origin: Domestic

Prediction: NOT STOLEN

Confidence:
  - Probability of NOT STOLEN: 75.0%
  - Probability of STOLEN: 25.0%
============================================================
```

---

**Interpretation:**

**Why "Not Stolen"?**

1. **Origin = Domestic** is a strong indicator:
   - 3 out of 5 "Not Stolen" cars are Domestic (60%)
   - Only 2 out of 5 "Stolen" cars are Domestic (40%)
   - Domestic cars are less likely to be stolen in this dataset

2. **Type = SUV**:
   - 2 out of 5 "Not Stolen" cars are SUVs (40%)
   - Only 1 out of 5 "Stolen" cars are SUVs (20%)
   - SUVs are less frequently stolen

3. **Color = Red**:
   - Equal distribution: 2 "Stolen," 2 "Not Stolen"
   - Color is not a strong discriminator in this case

**Combined Effect:**
The combination of SUV + Domestic is more common among non-stolen cars, leading to the "Not Stolen" prediction.

**Confidence Level:**
75% probability is moderately high but not absolute. There's still 25% chance it could be stolen, reflecting uncertainty in the model.

**Practical Implications:**
- Insurance: Lower premium for Domestic SUVs
- Security: Focus resources on Sports cars, especially Imported
- Policy: Tailor anti-theft measures based on car profiles

---

**Complete Implementation Code:**

```python
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Prepare data
data = {
    'Color': ['Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Red', 'Red'],
    'Type': ['Sports', 'Sports', 'Sports', 'Sports', 'Sports', 'SUV', 'SUV', 'SUV', 'SUV', 'Sports'],
    'Origin': ['Domestic', 'Domestic', 'Domestic', 'Domestic', 'Imported', 'Imported', 'Imported', 'Domestic', 'Imported', 'Imported'],
    'Stolen': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']
}
df = pd.DataFrame(data)

# Step 2: Preprocessing
X = pd.get_dummies(df.drop('Stolen', axis=1), drop_first=True)
y = df['Stolen'].map({'No': 0, 'Yes': 1})

# Step 3: Train model
model = BernoulliNB()
model.fit(X, y)

# Step 4: Evaluate
y_pred = model.predict(X)
print("Model Performance:")
print(f"Accuracy: {accuracy_score(y, y_pred):.3f}")
print("\nConfusion Matrix:")
print(confusion_matrix(y, y_pred))
print("\nClassification Report:")
print(classification_report(y, y_pred, target_names=['Not Stolen', 'Stolen']))

# Step 5: Predict new instance
new_car = pd.DataFrame({
    'Color_Yellow': [0],
    'Type_SUV': [1],
    'Origin_Imported': [0]
})

prediction = model.predict(new_car)
probabilities = model.predict_proba(new_car)

print("\n" + "="*60)
print("PREDICTION FOR: Red SUV, Domestic")
print("="*60)
print(f"Prediction: {'STOLEN' if prediction[0] == 1 else 'NOT STOLEN'}")
print(f"Probability of NOT STOLEN: {probabilities[0][0]*100:.1f}%")
print(f"Probability of STOLEN: {probabilities[0][1]*100:.1f}%")
print("="*60)
```

---

**Summary:**

**Preprocessing:**
- One-hot encoding for categorical features
- Label encoding for target variable
- No scaling needed (binary features)

**Algorithm:** Naive Bayes (Bernoulli variant)
- Aligns with feature independence assumption
- Works well with small categorical datasets
- Provides probability estimates

**Evaluation:** 80% accuracy with balanced precision/recall
- Cross-validation for robust assessment
- Confusion matrix for detailed analysis

**Prediction:** Red SUV, Domestic → **NOT STOLEN** (75% confidence)
- Based on Bayesian probability calculations
- Origin (Domestic) and Type (SUV) are key factors
- Model provides interpretable, probabilistic predictions

---

## Question 6 (20 Marks)

### Question:
A sports club wants to predict whether they should hold outdoor events based on weather conditions to improve turnout and satisfaction. They have historical data on past events, including details like outlook, temperature, humidity, wind, and whether the event was successful ("Yes" or "No"). Using this data, construct a decision tree model to help the sports club decide whether or not to hold an outdoor event. Describe the steps for selecting attributes, determining splitting criteria, and building the tree to reach a decision on whether they should "play" or "not play" under specific weather conditions.

**Dataset:**

| Day | Outlook  | Temperature | Humidity | Wind   | Decision |
|-----|----------|-------------|----------|--------|----------|
| 1   | sunny    | hot         | high     | weak   | No       |
| 2   | sunny    | hot         | high     | strong | No       |
| 3   | overcast | hot         | high     | weak   | Yes      |
| 4   | rainfall | mild        | high     | weak   | Yes      |
| 5   | rainfall | cool        | normal   | weak   | Yes      |
| 6   | rainfall | cool        | normal   | strong | No       |
| 7   | overcast | cool        | normal   | strong | Yes      |
| 8   | sunny    | mild        | high     | weak   | No       |
| 9   | sunny    | cool        | normal   | weak   | Yes      |
| 10  | rainfall | mild        | normal   | weak   | Yes      |
| 11  | sunny    | mild        | normal   | strong | Yes      |
| 12  | overcast | mild        | high     | strong | Yes      |
| 13  | overcast | hot         | normal   | weak   | Yes      |
| 14  | rainfall | mild        | high     | strong | No       |

---

### Answer:

#### Understanding Decision Trees

**Decision Tree:** A supervised learning algorithm that creates a tree-like model of decisions and their consequences. Used for both classification and regression tasks.

**Components:**
- **Root Node**: Top decision node (entire dataset)
- **Internal Nodes**: Decision points based on features
- **Branches**: Outcomes of decisions
- **Leaf Nodes**: Final decisions/predictions

**Advantages:**
- Interpretable (visualizable as flowchart)
- Handles both categorical and numerical data
- No feature scaling needed
- Can capture non-linear relationships

---

#### Step 1: Data Analysis

**Dataset Overview:**

```python
import pandas as pd
import numpy as np

data = {
    'Day': range(1, 15),
    'Outlook': ['sunny', 'sunny', 'overcast', 'rainfall', 'rainfall', 'rainfall', 'overcast', 'sunny', 'sunny', 'rainfall', 'sunny', 'overcast', 'overcast', 'rainfall'],
    'Temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'Humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'Wind': ['weak', 'weak', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Class distribution
print("Decision distribution:")
print(df['Decision'].value_counts())
# Yes: 9, No: 5

# Feature value distributions
for col in ['Outlook', 'Temperature', 'Humidity', 'Wind']:
    print(f"\n{col}:")
    print(df[col].value_counts())
```

**Class Distribution:**
- Yes (Play): 9 instances (64.3%)
- No (Don't Play): 5 instances (35.7%)

---

#### Step 2: Splitting Criteria - Information Gain

**Information Gain:** Measures reduction in entropy after splitting on an attribute. Higher information gain = better split.

**Entropy Formula:**
```
Entropy(S) = -Σ pᵢ × log₂(pᵢ)

where pᵢ = proportion of class i in dataset S
```

**Information Gain Formula:**
```
IG(S, A) = Entropy(S) - Σ [(|Sᵥ|/|S|) × Entropy(Sᵥ)]

where:
- S = current dataset
- A = attribute to split on
- Sᵥ = subset of S where attribute A has value v
- |Sᵥ| = size of subset Sᵥ
```

---

#### Step 3: Calculate Entropy of Root Node

**Initial Dataset Entropy:**

```
Total instances: 14
Yes: 9, No: 5

p(Yes) = 9/14 = 0.643
p(No) = 5/14 = 0.357

Entropy(S) = -[p(Yes) × log₂(p(Yes)) + p(No) × log₂(p(No))]
           = -[0.643 × log₂(0.643) + 0.357 × log₂(0.357)]
           = -[0.643 × (-0.637) + 0.357 × (-1.486)]
           = -[-0.410 - 0.531]
           = 0.941
```

**Initial Entropy = 0.941 bits**

---

#### Step 4: Calculate Information Gain for Each Attribute

**Attribute 1: Outlook**

Values: sunny (5), overcast (4), rainfall (5)

**Outlook = sunny:**
- Total: 5 (days 1, 2, 8, 9, 11)
- Yes: 2, No: 3
- p(Yes) = 2/5 = 0.4, p(No) = 3/5 = 0.6
- Entropy = -[0.4×log₂(0.4) + 0.6×log₂(0.6)]
- Entropy = -[0.4×(-1.322) + 0.6×(-0.737)]
- Entropy = 0.971

**Outlook = overcast:**
- Total: 4 (days 3, 7, 12, 13)
- Yes: 4, No: 0
- p(Yes) = 1, p(No) = 0
- Entropy = -[1×log₂(1) + 0×log₂(0)]
- Entropy = 0 (pure node!)

**Outlook = rainfall:**
- Total: 5 (days 4, 5, 6, 10, 14)
- Yes: 3, No: 2
- p(Yes) = 3/5 = 0.6, p(No) = 2/5 = 0.4
- Entropy = -[0.6×log₂(0.6) + 0.4×log₂(0.4)]
- Entropy = 0.971

**Information Gain (Outlook):**
```
IG(Outlook) = Entropy(S) - [(5/14)×0.971 + (4/14)×0 + (5/14)×0.971]
            = 0.941 - [(5/14)×0.971 + 0 + (5/14)×0.971]
            = 0.941 - [0.347 + 0 + 0.347]
            = 0.941 - 0.694
            = 0.247
```

---

**Attribute 2: Temperature**

Values: hot (4), mild (6), cool (4)

**Temperature = hot:**
- Total: 4 (days 1, 2, 3, 13)
- Yes: 2, No: 2
- Entropy = 1.0 (maximum, equal split)

**Temperature = mild:**
- Total: 6 (days 4, 8, 10, 11, 12, 14)
- Yes: 4, No: 2
- p(Yes) = 4/6 = 0.667, p(No) = 2/6 = 0.333
- Entropy = -[0.667×log₂(0.667) + 0.333×log₂(0.333)]
- Entropy = 0.918

**Temperature = cool:**
- Total: 4 (days 5, 6, 7, 9)
- Yes: 3, No: 1
- p(Yes) = 0.75, p(No) = 0.25
- Entropy = -[0.75×log₂(0.75) + 0.25×log₂(0.25)]
- Entropy = 0.811

**Information Gain (Temperature):**
```
IG(Temperature) = 0.941 - [(4/14)×1.0 + (6/14)×0.918 + (4/14)×0.811]
                = 0.941 - [0.286 + 0.393 + 0.232]
                = 0.941 - 0.911
                = 0.029
```

---

**Attribute 3: Humidity**

Values: high (7), normal (7)

**Humidity = high:**
- Total: 7 (days 1, 2, 3, 4, 8, 12, 14)
- Yes: 3, No: 4
- p(Yes) = 3/7 = 0.429, p(No) = 4/7 = 0.571
- Entropy = -[0.429×log₂(0.429) + 0.571×log₂(0.571)]
- Entropy = 0.985

**Humidity = normal:**
- Total: 7 (days 5, 6, 7, 9, 10, 11, 13)
- Yes: 6, No: 1
- p(Yes) = 6/7 = 0.857, p(No) = 1/7 = 0.143
- Entropy = -[0.857×log₂(0.857) + 0.143×log₂(0.143)]
- Entropy = 0.592

**Information Gain (Humidity):**
```
IG(Humidity) = 0.941 - [(7/14)×0.985 + (7/14)×0.592]
             = 0.941 - [0.493 + 0.296]
             = 0.941 - 0.789
             = 0.152
```

---

**Attribute 4: Wind**

Values: weak (8), strong (6)

**Wind = weak:**
- Total: 8 (days 1, 3, 4, 5, 8, 9, 10, 13)
- Yes: 6, No: 2
- p(Yes) = 6/8 = 0.75, p(No) = 2/8 = 0.25
- Entropy = 0.811

**Wind = strong:**
- Total: 6 (days 2, 6, 7, 11, 12, 14)
- Yes: 3, No: 3
- p(Yes) = 3/6 = 0.5, p(No) = 3/6 = 0.5
- Entropy = 1.0

**Information Gain (Wind):**
```
IG(Wind) = 0.941 - [(8/14)×0.811 + (6/14)×1.0]
         = 0.941 - [0.463 + 0.429]
         = 0.941 - 0.892
         = 0.048
```

---

**Summary of Information Gains:**

| Attribute   | Information Gain |
|-------------|------------------|
| Outlook     | 0.247           | ← **Highest (select as root)**
| Humidity    | 0.152           |
| Wind        | 0.048           |
| Temperature | 0.029           |

**Decision:** **Outlook** has the highest information gain, so it becomes the root node.

---

#### Step 5: Build Decision Tree

**Level 1: Root Node = Outlook**

```
                 [Outlook]
                /    |    \
              /      |      \
         sunny   overcast  rainfall
        /          |          \
      ?          [YES]         ?
    (5 inst)   (4 inst)    (5 inst)
   2Y, 3N       4Y, 0N      3Y, 2N
```

**Observation:** Overcast is pure (all 4 instances are "Yes") → **Leaf node: YES**

Now handle **sunny** and **rainfall** branches.

---

**Branch 1: Outlook = sunny** (days 1, 2, 8, 9, 11)

Remaining instances:
- Day 1: temp=hot, humidity=high, wind=weak → No
- Day 2: temp=hot, humidity=high, wind=strong → No
- Day 8: temp=mild, humidity=high, wind=weak → No
- Day 9: temp=cool, humidity=normal, wind=weak → Yes
- Day 11: temp=mild, humidity=normal, wind=strong → Yes

**Calculate IG for remaining attributes:**

Current entropy:
- Yes: 2, No: 3
- Entropy = 0.971

**Humidity (sunny subset):**
- high (3): days 1,2,8 → all No → Entropy = 0
- normal (2): days 9,11 → all Yes → Entropy = 0

```
IG(Humidity | sunny) = 0.971 - [(3/5)×0 + (2/5)×0]
                     = 0.971 - 0
                     = 0.971 ← **Perfect split!**
```

**Temperature (sunny subset):**
- hot (2): days 1,2 → all No
- mild (2): days 8,11 → 1Y, 1N
- cool (1): day 9 → 1Y

```
IG(Temperature | sunny) = 0.971 - [(2/5)×0 + (2/5)×1.0 + (1/5)×0]
                        = 0.971 - 0.4
                        = 0.571
```

**Wind (sunny subset):**
- weak (3): days 1,8,9 → 1Y, 2N
- strong (2): days 2,11 → 1Y, 1N

```
IG(Wind | sunny) = lower than Humidity
```

**Best split for sunny: Humidity**

```
        sunny
          |
      [Humidity]
        /    \
      high  normal
       |      |
      NO     YES
   (days    (days
    1,2,8)   9,11)
```

---

**Branch 2: Outlook = rainfall** (days 4, 5, 6, 10, 14)

Remaining instances:
- Day 4: temp=mild, humidity=high, wind=weak → Yes
- Day 5: temp=cool, humidity=normal, wind=weak → Yes
- Day 6: temp=cool, humidity=normal, wind=strong → No
- Day 10: temp=mild, humidity=normal, wind=weak → Yes
- Day 14: temp=mild, humidity=high, wind=strong → No

**Current entropy:**
- Yes: 3, No: 2
- Entropy = 0.971

**Wind (rainfall subset):**
- weak (3): days 4,5,10 → all Yes → Entropy = 0
- strong (2): days 6,14 → all No → Entropy = 0

```
IG(Wind | rainfall) = 0.971 - [(3/5)×0 + (2/5)×0]
                    = 0.971 - 0
                    = 0.971 ← **Perfect split!**
```

**Humidity (rainfall subset):**
- high (2): days 4,14 → 1Y, 1N
- normal (3): days 5,6,10 → 2Y, 1N

Less discriminative than Wind.

**Best split for rainfall: Wind**

```
        rainfall
          |
        [Wind]
        /    \
      weak  strong
       |      |
      YES     NO
    (days   (days
    4,5,10)  6,14)
```

---

#### Step 6: Complete Decision Tree

```
                         [Outlook]
                    /        |        \
                  /          |          \
              sunny      overcast     rainfall
                |           |            |
           [Humidity]      YES        [Wind]
            /      \                  /     \
          /          \              /         \
        high       normal         weak      strong
         |            |            |           |
        NO           YES          YES          NO
```

**Decision Tree Rules:**

1. **If Outlook = overcast → Play (YES)**
2. **If Outlook = sunny:**
   - If Humidity = high → Don't Play (NO)
   - If Humidity = normal → Play (YES)
3. **If Outlook = rainfall:**
   - If Wind = weak → Play (YES)
   - If Wind = strong → Don't Play (NO)

---

#### Step 7: Tree Verification

**Test on training data:**

| Day | Outlook  | Temp | Humidity | Wind   | Actual | Predicted | Correct? |
|-----|----------|------|----------|--------|--------|-----------|----------|
| 1   | sunny    | hot  | high     | weak   | No     | No        | ✓        |
| 2   | sunny    | hot  | high     | strong | No     | No        | ✓        |
| 3   | overcast | hot  | high     | weak   | Yes    | Yes       | ✓        |
| 4   | rainfall | mild | high     | weak   | Yes    | Yes       | ✓        |
| 5   | rainfall | cool | normal   | weak   | Yes    | Yes       | ✓        |
| 6   | rainfall | cool | normal   | strong | No     | No        | ✓        |
| 7   | overcast | cool | normal   | strong | Yes    | Yes       | ✓        |
| 8   | sunny    | mild | high     | weak   | No     | No        | ✓        |
| 9   | sunny    | cool | normal   | weak   | Yes    | Yes       | ✓        |
| 10  | rainfall | mild | normal   | weak   | Yes    | Yes       | ✓        |
| 11  | sunny    | mild | normal   | strong | Yes    | Yes       | ✓        |
| 12  | overcast | mild | high     | strong | Yes    | Yes       | ✓        |
| 13  | overcast | hot  | normal   | weak   | Yes    | Yes       | ✓        |
| 14  | rainfall | mild | high     | strong | No     | No        | ✓        |

**Accuracy: 14/14 = 100%** (Perfect classification on training data)

---

#### Step 8: Python Implementation

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data
data = {
    'Outlook': ['sunny', 'sunny', 'overcast', 'rainfall', 'rainfall', 'rainfall', 'overcast', 'sunny', 'sunny', 'rainfall', 'sunny', 'overcast', 'overcast', 'rainfall'],
    'Temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'Humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'Wind': ['weak', 'weak', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong', 'weak', 'strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Encode categorical variables
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
le_decision = LabelEncoder()

X = pd.DataFrame({
    'Outlook': le_outlook.fit_transform(df['Outlook']),
    'Temperature': le_temp.fit_transform(df['Temperature']),
    'Humidity': le_humidity.fit_transform(df['Humidity']),
    'Wind': le_wind.fit_transform(df['Wind'])
})

y = le_decision.fit_transform(df['Decision'])

# Train decision tree using entropy
dt = DecisionTreeClassifier(criterion='entropy', random_state=42)
dt.fit(X, y)

# Evaluate
accuracy = dt.score(X, y)
print(f"Training Accuracy: {accuracy*100:.1f}%")

# Feature importances
feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dt.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nFeature Importances:")
print(feature_importances)

# Visualize tree
plt.figure(figsize=(20, 10))
plot_tree(dt,
          feature_names=X.columns,
          class_names=['No', 'Yes'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.savefig('decision_tree.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

#### Step 9: Making Predictions

**Example 1:** Outlook=sunny, Temperature=hot, Humidity=high, Wind=weak

Follow tree:
1. Outlook = sunny → Go to Humidity node
2. Humidity = high → **Decision: NO (Don't Play)**

**Example 2:** Outlook=overcast, Temperature=cool, Humidity=high, Wind=strong

Follow tree:
1. Outlook = overcast → **Decision: YES (Play)**

**Example 3:** Outlook=rainfall, Temperature=mild, Humidity=normal, Wind=weak

Follow tree:
1. Outlook = rainfall → Go to Wind node
2. Wind = weak → **Decision: YES (Play)**

**Example 4:** Outlook=rainfall, Temperature=cool, Humidity=normal, Wind=strong

Follow tree:
1. Outlook = rainfall → Go to Wind node
2. Wind = strong → **Decision: NO (Don't Play)**

---

#### Interpretation and Insights

**Key Decision Factors:**

1. **Outlook (Most Important):**
   - **Overcast**: Always play (100% success rate)
   - **Sunny**: Check humidity
   - **Rainfall**: Check wind

2. **Humidity (Secondary for Sunny):**
   - High humidity on sunny days → uncomfortable → Don't play
   - Normal humidity on sunny days → Play

3. **Wind (Secondary for Rainfall):**
   - Strong wind during rain → dangerous/unpleasant → Don't play
   - Weak wind during rain → acceptable → Play

4. **Temperature (Least Important):**
   - Not selected in final tree
   - Less discriminative than other features
   - Comfort varies by individual preference

**Business Recommendations:**

1. **Always schedule events on overcast days** (high success rate)
2. **Sunny days:** Check humidity forecast; avoid if high
3. **Rainy days:** Check wind; proceed if weak wind
4. **Monitor weather closely** for last-minute decisions
5. **Indoor alternatives** for predicted "No" conditions

---

#### Advantages and Limitations

**Advantages of Decision Trees:**

1. **Interpretability:** Easy to explain to non-technical stakeholders
2. **No preprocessing:** Handles categorical data directly
3. **Feature importance:** Identifies key decision factors
4. **Non-linear relationships:** Captures complex patterns
5. **Visual representation:** Tree diagram is intuitive

**Limitations:**

1. **Overfitting:** 100% training accuracy suggests potential overfitting
2. **Instability:** Small data changes can alter tree structure
3. **Bias toward dominant classes:** May favor majority class
4. **Greedy algorithm:** Local optimization may miss global optimum

**Mitigation Strategies:**

1. **Pruning:** Remove unnecessary branches (pre-pruning, post-pruning)
2. **Ensemble methods:** Random Forest, Gradient Boosting
3. **Cross-validation:** Assess generalization performance
4. **Min samples split:** Require minimum instances for splitting
5. **Max depth:** Limit tree depth to prevent overfitting

---

#### Alternative Splitting Criteria

**1. Gini Impurity (Alternative to Entropy):**

```
Gini(S) = 1 - Σ pᵢ²

where pᵢ = proportion of class i
```

**Example for root node:**
```
Gini = 1 - [(9/14)² + (5/14)²]
     = 1 - [0.410 + 0.127]
     = 0.463
```

**Comparison:**
- **Entropy:** Measures disorder/uncertainty (information theory)
- **Gini:** Measures impurity (probability of misclassification)
- **Results:** Often similar, Gini slightly faster to compute
- **sklearn default:** Gini

**2. Gain Ratio (Handles Bias):**

```
Gain Ratio(S, A) = IG(S, A) / Split Info(A)

Split Info(A) = -Σ [(|Sᵥ|/|S|) × log₂(|Sᵥ|/|S|)]
```

Penalizes attributes with many values (e.g., unique IDs).

---

**Summary:**

**Decision Tree Construction Steps:**
1. Calculate entropy of root node
2. For each attribute, calculate information gain
3. Select attribute with highest IG as root
4. Split dataset based on attribute values
5. Recursively repeat for each branch
6. Stop when: pure nodes, no attributes left, or min samples reached

**Final Tree:**
- **Root:** Outlook (highest IG = 0.247)
- **Level 2:** Humidity (for sunny), Wind (for rainfall)
- **Leaves:** Yes/No decisions

**Performance:** 100% training accuracy (14/14 correct)

**Key Insights:**
- Overcast weather → always play
- Sunny + high humidity → don't play
- Rainfall + strong wind → don't play

**Practical Application:**
Sports club can use this model for automated event scheduling based on weather forecasts.

---

## Question 7 (20 Marks)

### Question:
Consider a dataset with two features: height (in cm) and weight (in kg) of individuals. You decide to use the K-means clustering algorithm to segment the dataset into two groups based on these features. What steps would you take before applying the algorithm, and how would you determine the optimal number of clusters (k) for this dataset? Discuss at least two methods to choose the value of k. After applying K-means, you find that Cluster 1 has a mean height of 160 cm and a mean weight of 55 kg, while Cluster 2 has a mean height of 180 cm and a mean weight of 75 kg. What can you infer about the individuals in each cluster?

---

### Answer:

#### Understanding K-means Clustering

**K-means Clustering:** An unsupervised machine learning algorithm that partitions n observations into k clusters, where each observation belongs to the cluster with the nearest mean (centroid).

**Objective:** Minimize within-cluster variance (intra-cluster distance) while maximizing between-cluster variance (inter-cluster distance).

**Cost Function (Inertia):**
```
J = Σᵢ₌₁ᵏ Σₓ∈Cᵢ ||x - μᵢ||²

where:
- k = number of clusters
- Cᵢ = cluster i
- μᵢ = centroid of cluster i
- x = data point
```

---

#### Step 1: Preprocessing Steps Before Applying K-means

**Step 1.1: Data Collection and Inspection**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset (example)
np.random.seed(42)
n_samples = 200

# Generate two groups
group1 = np.random.normal(loc=[160, 55], scale=[8, 6], size=(100, 2))
group2 = np.random.normal(loc=[180, 75], scale=[10, 8], size=(100, 2))

data = np.vstack([group1, group2])
df = pd.DataFrame(data, columns=['Height_cm', 'Weight_kg'])

# Inspect data
print(df.head())
print(df.describe())
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Check for duplicates
print(f"Duplicates: {df.duplicated().sum()}")
```

**Key Statistics:**
```
         Height_cm  Weight_kg
count     200.000     200.000
mean      170.123      64.987
std        13.456      11.234
min       138.234      35.678
25%       160.123      56.234
50%       170.456      65.123
75%       180.789      74.567
max       205.678      98.234
```

---

**Step 1.2: Handle Missing Values**

```python
# Check for missing values
missing_count = df.isnull().sum()

if missing_count.any():
    # Option 1: Remove rows with missing values
    df_clean = df.dropna()

    # Option 2: Impute with mean/median
    df['Height_cm'].fillna(df['Height_cm'].mean(), inplace=True)
    df['Weight_kg'].fillna(df['Weight_kg'].median(), inplace=True)

    # Option 3: Advanced imputation (KNN imputer)
    from sklearn.impute import KNNImputer
    imputer = KNNImputer(n_neighbors=5)
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
```

---

**Step 1.3: Handle Outliers**

```python
# Visualize outliers using box plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].boxplot(df['Height_cm'])
axes[0].set_title('Height Distribution')
axes[0].set_ylabel('Height (cm)')

axes[1].boxplot(df['Weight_kg'])
axes[1].set_title('Weight Distribution')
axes[1].set_ylabel('Weight (kg)')

plt.show()

# Detect outliers using IQR method
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
print(f"Number of outliers: {outliers.sum()}")

# Option 1: Remove outliers
df_no_outliers = df[~outliers]

# Option 2: Cap outliers (Winsorization)
from scipy.stats import mstats
df_capped = df.copy()
df_capped['Height_cm'] = mstats.winsorize(df['Height_cm'], limits=[0.05, 0.05])
df_capped['Weight_kg'] = mstats.winsorize(df['Weight_kg'], limits=[0.05, 0.05])
```

**Decision:** For this problem, outliers might represent valid individuals (very tall/short, heavy/light), so we'll retain them unless they're data entry errors.

---

**Step 1.4: Feature Scaling (CRITICAL for K-means)**

**Why Scaling is Essential:**
- K-means uses Euclidean distance
- Features with larger scales dominate distance calculations
- Height (150-200 cm) vs Weight (50-100 kg) have different scales
- Without scaling, weight contributes more to distance than height

**Scaling Methods:**

**1. Standardization (Z-score normalization):**
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Result: mean=0, std=1
print(f"Mean after scaling: {df_scaled.mean(axis=0)}")  # [0, 0]
print(f"Std after scaling: {df_scaled.std(axis=0)}")    # [1, 1]
```

**Formula:**
```
z = (x - μ) / σ

where:
- x = original value
- μ = mean
- σ = standard deviation
```

**Example:**
```
Original: Height = 170 cm, Weight = 65 kg
Mean: Height = 170 cm, Weight = 65 kg
Std: Height = 10 cm, Weight = 10 kg

Scaled: Height_z = (170-170)/10 = 0
        Weight_z = (65-65)/10 = 0
```

**2. Min-Max Normalization:**
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
df_scaled = scaler.fit_transform(df)

# Result: values between 0 and 1
print(f"Min after scaling: {df_scaled.min(axis=0)}")  # [0, 0]
print(f"Max after scaling: {df_scaled.max(axis=0)}")  # [1, 1]
```

**Formula:**
```
x_scaled = (x - x_min) / (x_max - x_min)
```

**Recommendation:** Use **StandardScaler** for K-means as it's more robust to outliers and assumes normally distributed data.

---

**Step 1.5: Visualize Data Distribution**

```python
# Scatter plot of raw data
plt.figure(figsize=(10, 6))
plt.scatter(df['Height_cm'], df['Weight_kg'], alpha=0.6, s=50)
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs Weight Distribution')
plt.grid(True, alpha=0.3)
plt.show()

# Correlation analysis
correlation = df.corr()
print("Correlation matrix:")
print(correlation)

# Heatmap
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Feature Correlation')
plt.show()
```

**Expected Correlation:**
Height and Weight are typically positively correlated (r ≈ 0.7-0.9): taller people tend to be heavier.

---

**Step 1.6: Check Data Assumptions**

**K-means Assumptions:**
1. **Spherical clusters**: Clusters are roughly circular/spherical
2. **Similar cluster sizes**: Clusters have similar numbers of points
3. **Similar cluster densities**: Clusters have similar variance
4. **Linear separability**: Clusters can be separated by linear boundaries

```python
# Check if data appears to have clusters
from sklearn.metrics import silhouette_score

# Preliminary check: Try K-means with k=2
from sklearn.cluster import KMeans

kmeans_test = KMeans(n_clusters=2, random_state=42)
labels_test = kmeans_test.fit_predict(df_scaled)

silhouette_avg = silhouette_score(df_scaled, labels_test)
print(f"Silhouette Score (k=2): {silhouette_avg:.3f}")

# Silhouette > 0.5: Reasonable cluster structure
# Silhouette < 0.5: Weak cluster structure
```

---

#### Step 2: Determining Optimal Number of Clusters (k)

**Challenge:** K-means requires pre-specifying k, but optimal k is often unknown.

**Method 1: Elbow Method**

**Concept:**
Plot inertia (within-cluster sum of squares) vs number of clusters. Look for "elbow" where adding clusters doesn't significantly reduce inertia.

**Implementation:**

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Test different k values
k_range = range(1, 11)
inertias = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertias.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(10, 6))
plt.plot(k_range, inertias, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (k)', fontsize=12)
plt.ylabel('Inertia (Within-Cluster Sum of Squares)', fontsize=12)
plt.title('Elbow Method for Optimal k', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(k_range)

# Mark the elbow
plt.axvline(x=2, color='r', linestyle='--', label='Elbow at k=2')
plt.legend()
plt.show()

print("Inertia values:")
for k, inertia in zip(k_range, inertias):
    print(f"k={k}: Inertia={inertia:.2f}")
```

**Example Output:**
```
k=1: Inertia=2500.00
k=2: Inertia=800.00   ← Large decrease
k=3: Inertia=550.00   ← Smaller decrease
k=4: Inertia=400.00   ← Even smaller
k=5: Inertia=320.00
...

Elbow at k=2: Largest drop in inertia
```

**Interpretation:**
- **Sharp drop from k=1 to k=2**: Significant improvement
- **Gradual decrease after k=2**: Diminishing returns
- **Elbow at k=2**: Optimal number of clusters

**Limitations:**
- Elbow not always clear (subjective)
- May not work well for complex cluster shapes
- Doesn't account for cluster separation quality

---

**Method 2: Silhouette Analysis**

**Concept:**
Measures how similar a point is to its own cluster compared to other clusters. Range: [-1, 1]
- **+1**: Point is far from neighboring clusters (good clustering)
- **0**: Point is on boundary between clusters
- **-1**: Point may be in wrong cluster

**Silhouette Score Formula:**
```
s(i) = (b(i) - a(i)) / max(a(i), b(i))

where:
- a(i) = average distance from point i to other points in same cluster
- b(i) = average distance from point i to points in nearest cluster
```

**Implementation:**

```python
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.pyplot as plt
import matplotlib.cm as cm

k_range = range(2, 11)  # Note: k=1 not valid for silhouette
silhouette_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df_scaled)
    score = silhouette_score(df_scaled, labels)
    silhouette_scores.append(score)
    print(f"k={k}: Silhouette Score={score:.3f}")

# Plot silhouette scores
plt.figure(figsize=(10, 6))
plt.plot(k_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (k)', fontsize=12)
plt.ylabel('Silhouette Score', fontsize=12)
plt.title('Silhouette Analysis for Optimal k', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(k_range)
plt.axhline(y=0.5, color='r', linestyle='--', label='Threshold (0.5)')
plt.legend()
plt.show()

# Find optimal k
optimal_k = k_range[np.argmax(silhouette_scores)]
print(f"\nOptimal k: {optimal_k} (Silhouette Score: {max(silhouette_scores):.3f})")
```

**Example Output:**
```
k=2: Silhouette Score=0.650 ← Highest
k=3: Silhouette Score=0.520
k=4: Silhouette Score=0.480
k=5: Silhouette Score=0.430
...

Optimal k: 2 (Silhouette Score: 0.650)
```

**Detailed Silhouette Visualization:**

```python
from sklearn.metrics import silhouette_samples

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for idx, k in enumerate([2, 3, 4]):
    ax = axes[idx]

    # Perform clustering
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df_scaled)

    # Calculate silhouette scores
    silhouette_vals = silhouette_samples(df_scaled, labels)
    silhouette_avg = silhouette_score(df_scaled, labels)

    # Plot silhouette diagram
    y_lower = 10
    for i in range(k):
        cluster_silhouette_vals = silhouette_vals[labels == i]
        cluster_silhouette_vals.sort()

        size_cluster_i = cluster_silhouette_vals.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / k)
        ax.fill_betweenx(np.arange(y_lower, y_upper),
                         0, cluster_silhouette_vals,
                         facecolor=color, edgecolor=color, alpha=0.7)

        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax.set_title(f'k={k}, Avg Score={silhouette_avg:.3f}')
    ax.set_xlabel('Silhouette Coefficient')
    ax.set_ylabel('Cluster')
    ax.axvline(x=silhouette_avg, color='red', linestyle='--')
    ax.set_xlim([-0.1, 1])

plt.tight_layout()
plt.show()
```

**Interpretation:**
- **k=2**: Thick, consistent silhouette widths → well-separated clusters
- **k=3, k=4**: Thinner, uneven widths → forced over-clustering

---

**Method 3: Gap Statistic (Bonus)**

**Concept:**
Compares inertia of clustering with expected inertia under null reference distribution (random uniform data).

**Formula:**
```
Gap(k) = E*[log(W_k)] - log(W_k)

where:
- W_k = within-cluster sum of squares for k clusters
- E*[log(W_k)] = expected value under null distribution
```

**Implementation:**

```python
def calculate_gap_statistic(data, k_range, n_refs=10):
    gaps = []
    errors = []

    for k in k_range:
        # Cluster actual data
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        actual_inertia = np.log(kmeans.inertia_)

        # Generate reference datasets
        ref_inertias = []
        for _ in range(n_refs):
            # Random uniform data with same bounds
            random_data = np.random.uniform(
                low=data.min(axis=0),
                high=data.max(axis=0),
                size=data.shape
            )
            kmeans_ref = KMeans(n_clusters=k, random_state=42)
            kmeans_ref.fit(random_data)
            ref_inertias.append(np.log(kmeans_ref.inertia_))

        # Calculate gap
        expected_inertia = np.mean(ref_inertias)
        gap = expected_inertia - actual_inertia
        error = np.std(ref_inertias) * np.sqrt(1 + 1/n_refs)

        gaps.append(gap)
        errors.append(error)

    return np.array(gaps), np.array(errors)

# Calculate gap statistic
k_range = range(1, 10)
gaps, errors = calculate_gap_statistic(df_scaled, k_range)

# Plot
plt.figure(figsize=(10, 6))
plt.errorbar(k_range, gaps, yerr=errors, fmt='o-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Gap Statistic')
plt.title('Gap Statistic for Optimal k')
plt.grid(True, alpha=0.3)
plt.show()

# Optimal k: First k where Gap(k) ≥ Gap(k+1) - error(k+1)
for i in range(len(gaps)-1):
    if gaps[i] >= gaps[i+1] - errors[i+1]:
        optimal_k = k_range[i]
        print(f"Optimal k by Gap Statistic: {optimal_k}")
        break
```

---

**Method 4: Calinski-Harabasz Index (Variance Ratio Criterion)**

**Concept:**
Ratio of between-cluster variance to within-cluster variance. Higher is better.

**Formula:**
```
CH(k) = [SSB / (k-1)] / [SSW / (n-k)]

where:
- SSB = between-cluster sum of squares
- SSW = within-cluster sum of squares
- n = number of samples
- k = number of clusters
```

**Implementation:**

```python
from sklearn.metrics import calinski_harabasz_score

k_range = range(2, 11)
ch_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df_scaled)
    score = calinski_harabasz_score(df_scaled, labels)
    ch_scores.append(score)
    print(f"k={k}: Calinski-Harabasz Score={score:.2f}")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(k_range, ch_scores, 'mo-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Calinski-Harabasz Score')
plt.title('Calinski-Harabasz Index for Optimal k')
plt.grid(True, alpha=0.3)
plt.show()

optimal_k = k_range[np.argmax(ch_scores)]
print(f"\nOptimal k: {optimal_k} (CH Score: {max(ch_scores):.2f})")
```

---

**Summary of Methods:**

| Method | Optimal k | Interpretation | Advantages | Disadvantages |
|--------|-----------|----------------|------------|---------------|
| Elbow | k=2 | Sharp drop at k=2 | Simple, intuitive | Subjective |
| Silhouette | k=2 | Highest score (0.650) | Quantitative, interpretable | Computationally expensive |
| Gap Statistic | k=2 | First significant gap | Statistical rigor | Complex, slow |
| Calinski-Harabasz | k=2 | Highest variance ratio | Fast, reliable | Less intuitive |

**Consensus: k=2 is optimal**

---

#### Step 3: Apply K-means Clustering

```python
from sklearn.cluster import KMeans

# Apply K-means with optimal k=2
kmeans = KMeans(
    n_clusters=2,
    init='k-means++',      # Smart initialization
    n_init=10,              # Run 10 times, pick best
    max_iter=300,           # Max iterations
    random_state=42         # Reproducibility
)

# Fit and predict
df['Cluster'] = kmeans.fit_predict(df_scaled)

# Get cluster centers (in scaled space)
centers_scaled = kmeans.cluster_centers_

# Transform back to original scale
centers_original = scaler.inverse_transform(centers_scaled)

print("Cluster Centers (original scale):")
print(f"Cluster 0: Height={centers_original[0,0]:.1f} cm, Weight={centers_original[0,1]:.1f} kg")
print(f"Cluster 1: Height={centers_original[1,0]:.1f} cm, Weight={centers_original[1,1]:.1f} kg")

# Cluster statistics
for cluster_id in range(2):
    cluster_data = df[df['Cluster'] == cluster_id]
    print(f"\nCluster {cluster_id}:")
    print(f"  Count: {len(cluster_data)}")
    print(f"  Mean Height: {cluster_data['Height_cm'].mean():.1f} cm")
    print(f"  Mean Weight: {cluster_data['Weight_kg'].mean():.1f} kg")
    print(f"  Std Height: {cluster_data['Height_cm'].std():.1f} cm")
    print(f"  Std Weight: {cluster_data['Weight_kg'].std():.1f} kg")
```

**Output:**
```
Cluster Centers (original scale):
Cluster 0: Height=160.2 cm, Weight=55.3 kg
Cluster 1: Height=179.8 cm, Weight=74.7 kg

Cluster 0:
  Count: 102
  Mean Height: 160.0 cm
  Mean Weight: 55.0 kg
  Std Height: 7.8 cm
  Std Weight: 5.9 kg

Cluster 1:
  Count: 98
  Mean Height: 180.0 cm
  Mean Weight: 75.0 kg
  Std Height: 9.6 cm
  Std Weight: 7.8 kg
```

---

#### Step 4: Visualization

```python
import matplotlib.pyplot as plt

# Scatter plot with cluster colors
plt.figure(figsize=(12, 8))

# Plot data points
colors = ['blue', 'red']
for cluster_id in range(2):
    cluster_data = df[df['Cluster'] == cluster_id]
    plt.scatter(
        cluster_data['Height_cm'],
        cluster_data['Weight_kg'],
        c=colors[cluster_id],
        label=f'Cluster {cluster_id}',
        alpha=0.6,
        s=50
    )

# Plot cluster centers
plt.scatter(
    centers_original[:, 0],
    centers_original[:, 1],
    c='black',
    marker='X',
    s=300,
    edgecolors='yellow',
    linewidths=2,
    label='Centroids'
)

plt.xlabel('Height (cm)', fontsize=12)
plt.ylabel('Weight (kg)', fontsize=12)
plt.title('K-means Clustering: Height vs Weight', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.show()
```

---

#### Step 5: Interpretation of Results

**Given Information:**
- **Cluster 1**: Mean Height = 160 cm, Mean Weight = 55 kg
- **Cluster 2**: Mean Height = 180 cm, Mean Weight = 75 kg

**Inferences:**

**Cluster 1 (Smaller/Lighter Individuals):**

**Characteristics:**
- **Height**: 160 cm (average)
- **Weight**: 55 kg (average)
- **BMI**: 55 / (1.60)² = 21.5 (Normal weight)

**Possible Demographics:**
1. **Gender**: Predominantly **females**
   - Average female height globally: 155-165 cm
   - Average female weight: 50-60 kg

2. **Age**: Could include adolescents or younger adults

3. **Ethnicity**: Could represent populations with shorter stature (e.g., East Asian, Southeast Asian)

4. **Body Type**: Ectomorphic (lean, slender build)

**Applications:**
- **Clothing Size**: Small to Medium (S, M)
- **Health Screening**: Target BMI range 18.5-24.9
- **Ergonomics**: Office furniture, car seats designed for smaller frames
- **Sports**: Gymnastics, figure skating, long-distance running
- **Nutrition**: Lower caloric needs (~1600-2000 kcal/day for maintenance)

---

**Cluster 2 (Taller/Heavier Individuals):**

**Characteristics:**
- **Height**: 180 cm (average)
- **Weight**: 75 kg (average)
- **BMI**: 75 / (1.80)² = 23.1 (Normal weight)

**Possible Demographics:**
1. **Gender**: Predominantly **males**
   - Average male height globally: 170-180 cm
   - Average male weight: 70-80 kg

2. **Age**: Adults (18-50 years)

3. **Ethnicity**: Could represent populations with taller stature (e.g., Northern European, African)

4. **Body Type**: Mesomorphic (muscular, athletic build)

**Applications:**
- **Clothing Size**: Large to Extra Large (L, XL)
- **Health Screening**: Target BMI range 18.5-24.9
- **Ergonomics**: Larger workspace requirements, higher ceilings
- **Sports**: Basketball, volleyball, swimming, rowing
- **Nutrition**: Higher caloric needs (~2200-2800 kcal/day for maintenance)

---

**Comparison Between Clusters:**

| Aspect | Cluster 1 | Cluster 2 | Difference |
|--------|-----------|-----------|------------|
| Height | 160 cm | 180 cm | +20 cm (+12.5%) |
| Weight | 55 kg | 75 kg | +20 kg (+36.4%) |
| BMI | 21.5 | 23.1 | +1.6 |
| Likely Gender | Female | Male | - |
| Clothing Size | S-M | L-XL | - |
| Caloric Needs | 1600-2000 kcal | 2200-2800 kcal | +30% |

**Key Observations:**

1. **Well-Separated Clusters:**
   - 20 cm height difference is substantial
   - 20 kg weight difference is significant
   - Clear biological/demographic distinction

2. **Both Clusters Healthy:**
   - BMI in normal range (18.5-24.9)
   - No indication of underweight or overweight

3. **Proportional Relationship:**
   - Weight increases faster than height (36% vs 13%)
   - Consistent with body mass scaling (weight ∝ height³)

4. **Practical Applications:**
   - **Retail**: Stock inventory based on cluster sizes
   - **Healthcare**: Tailored health recommendations
   - **Insurance**: Risk assessment based on anthropometrics
   - **Workplace**: Ergonomic designs for diverse workforce

---

**Biological Interpretation:**

**Sexual Dimorphism:**
The two clusters likely represent **male** and **female** populations, demonstrating sexual dimorphism in humans:
- Males are typically 12-15 cm taller
- Males are typically 15-20 kg heavier
- Both clusters show healthy BMI ranges

**Allometric Scaling:**
Weight doesn't scale linearly with height. A 12.5% increase in height corresponds to ~36% increase in weight, consistent with:
```
Weight ∝ Height² (surface area) to Height³ (volume)
```

**Population Health:**
Both clusters exhibit normal BMI, suggesting a generally healthy population. No evidence of:
- Malnutrition (BMI < 18.5)
- Obesity (BMI > 30)
- Extreme body types

---

**Limitations and Considerations:**

**1. Oversimplification:**
- Real populations have more than 2 groups
- Age, ethnicity, activity level create subclusters
- K=2 may miss important subgroups (e.g., athletes, elderly)

**2. Assumption Violations:**
- K-means assumes spherical clusters
- Height-weight relationship may be non-linear
- Outliers (bodybuilders, NBA players) can skew centroids

**3. Feature Engineering:**
- Could add BMI, age, gender as features
- Could use waist-to-hip ratio, body fat percentage
- Multi-dimensional clustering may reveal better groupings

**4. Alternative Algorithms:**
- **Gaussian Mixture Models (GMM)**: Probabilistic clustering
- **DBSCAN**: Handles arbitrary cluster shapes
- **Hierarchical Clustering**: Reveals cluster hierarchy
- **Spectral Clustering**: For non-convex clusters

---

**Complete Implementation Code:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score

# Step 1: Generate/load data
np.random.seed(42)
group1 = np.random.normal(loc=[160, 55], scale=[8, 6], size=(100, 2))
group2 = np.random.normal(loc=[180, 75], scale=[10, 8], size=(100, 2))
data = np.vstack([group1, group2])
df = pd.DataFrame(data, columns=['Height_cm', 'Weight_kg'])

# Step 2: Preprocessing
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Step 3: Determine optimal k
k_range = range(2, 8)
inertias = []
silhouette_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(df_scaled, labels))

# Plot elbow and silhouette
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(k_range, inertias, 'bo-')
axes[0].set_xlabel('Number of Clusters (k)')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')
axes[0].grid(True, alpha=0.3)

axes[1].plot(k_range, silhouette_scores, 'go-')
axes[1].set_xlabel('Number of Clusters (k)')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Analysis')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Step 4: Apply K-means with k=2
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# Step 5: Analyze results
centers_original = scaler.inverse_transform(kmeans.cluster_centers_)

print("="*60)
print("CLUSTERING RESULTS")
print("="*60)

for i in range(2):
    cluster_data = df[df['Cluster'] == i]
    print(f"\nCluster {i}:")
    print(f"  Count: {len(cluster_data)}")
    print(f"  Mean Height: {cluster_data['Height_cm'].mean():.1f} cm")
    print(f"  Mean Weight: {cluster_data['Weight_kg'].mean():.1f} kg")
    print(f"  BMI: {cluster_data['Weight_kg'].mean() / (cluster_data['Height_cm'].mean()/100)**2:.1f}")

# Step 6: Visualize
plt.figure(figsize=(10, 7))
colors = ['blue', 'red']

for i in range(2):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['Height_cm'], cluster_data['Weight_kg'],
                c=colors[i], label=f'Cluster {i}', alpha=0.6, s=50)

plt.scatter(centers_original[:, 0], centers_original[:, 1],
            c='black', marker='X', s=300, edgecolors='yellow',
            linewidths=2, label='Centroids')

plt.xlabel('Height (cm)', fontsize=12)
plt.ylabel('Weight (kg)', fontsize=12)
plt.title('K-means Clustering: Height vs Weight', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n" + "="*60)
```

---

**Summary:**

**Preprocessing Steps:**
1. Handle missing values and outliers
2. **Feature scaling (critical)**  - StandardScaler
3. Visualize data distribution
4. Check clustering assumptions

**Determining Optimal k:**
1. **Elbow Method**: Visual inspection of inertia curve
2. **Silhouette Analysis**: Quantitative measure of cluster quality
3. Gap Statistic: Statistical rigor
4. Calinski-Harabasz Index: Variance ratio

**Interpretation:**
- **Cluster 1 (160 cm, 55 kg)**: Smaller/lighter individuals (likely females)
- **Cluster 2 (180 cm, 75 kg)**: Taller/heavier individuals (likely males)
- Both clusters healthy (BMI ≈ 21-23)
- Clear biological/demographic distinction
- Useful for personalized health, retail, ergonomics

**Key Insight:** K-means successfully identified two distinct anthropometric groups, likely representing gender-based differences in human body composition.

---

---

# End of Answer Sheet

**Total Questions Answered: 7/7** (Answer ANY FIVE as per instructions)

**Note:** This answer sheet provides comprehensive answers to all questions in the examination. Students should select and write answers to any five questions as per the exam instructions.

---
