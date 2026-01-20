# Classification Algorithms 

## Table of Contents

- [Classification Algorithms](#classification-algorithms)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Common Classification Algorithms](#common-classification-algorithms)
    - [Linear Models](#linear-models)
      - [Logistic Regression](#logistic-regression)
        - [Understanding Probability, Odds, and Log-Odds](#understanding-probability-odds-and-log-odds)
        - [How Logistic Regression Works](#how-logistic-regression-works)
        - [Step-by-Step Process](#step-by-step-process)
        - [Key Properties and Use Cases](#key-properties-and-use-cases)
        - [Example: Bank Loan Default Prediction](#example-bank-loan-default-prediction)
        - [Loss Function and Decision Boundary](#loss-function-and-decision-boundary)
        - [Practical Implementation: Pima Indians Diabetes Prediction](#practical-implementation-pima-indians-diabetes-prediction)
    - [Tree-Based Algorithms](#tree-based-algorithms)
    - [Probabilistic Algorithms](#probabilistic-algorithms)
    - [Instance-Based Algorithms](#instance-based-algorithms)
    - [Neural Network Algorithms](#neural-network-algorithms)  
    - [Ensemble Methods](#ensemble-methods)
  - [Logistic Regression: Theory, Intuition, and Practical Implementation](#logistic-regression-theory-intuition-and-practical-implementation)
    - [Easy Understanding of Logistic Regression](#easy-understanding-of-logistic-regression)
  - [Linear Regression Theory](#linear-regression-theory)
    - [General Form of Linear Regression Model](#general-form-of-linear-regression-model)
    - [Step-by-Step Linear Regression Example](#step-by-step-linear-regression-example)

---

## Introduction

Classification algorithms are a subset of supervised machine learning techniques used to categorize data into predefined classes or labels based on input features. These algorithms learn from labeled training data to make predictions on new, unseen data. Classification is widely used in various applications, including spam detection, image recognition, medical diagnosis, and sentiment analysis.

## Common Classification Algorithms

### Linear Models

#### Logistic Regression

Logistic regression is a fundamental classification algorithm that models the probability that a given input belongs to a particular class. It is especially popular for binary classification tasks, where the goal is to distinguish between two classes (e.g., spam vs. not spam). Logistic regression uses the logistic (sigmoid) function to map any real-valued input into a probability between 0 and 1, representing the model's confidence that the input belongs to the target class.

##### Understanding Probability, Odds, and Log-Odds

- **Probability (`P`)**: The likelihood that the event of interest (e.g., spam) occurs, where \( 0 \leq P \leq 1 \).
- **Probability of the event not happening (`1 - P`)**: The likelihood that the event does not occur (e.g., not spam).
- **Sum of probabilities**:  
    $$ P + (1 - P) = 1 $$
    This ensures the probabilities of all possible outcomes sum to 1.

- **Odds**:  
    The ratio of the probability of the event happening to it not happening:  
    $$ \text{Odds} = \frac{P}{1 - P} $$
    Odds express how much more likely the event is to occur than not.

- **Log-Odds (Logit)**:  
    The logarithm of the odds, which transforms the probability scale (0, 1) to the entire real line \((-\infty, +\infty)\):  
    $$ \text{logit}(P) = \log\left(\frac{P}{1 - P}\right) $$
    Logistic regression models the log-odds as a linear function of the input features.

##### How Logistic Regression Works

1. **Linear Combination of Features**:  
   The model computes a weighted sum of the input features:
   $$
   z = w_0x_0 + w_1x_1 + \ldots + w_nx_n = \mathbf{w}^T \mathbf{x}
   $$


- \( x_0, x_1, \ldots, x_n \): Input features (with \( x_0 \) often set to 1 for the intercept).
- \( w_0, w_1, \ldots, w_n \): Model parameters (weights) learned during training.

This linear combination, \( z = \mathbf{w}^T \mathbf{x} \), represents the influence of each feature on the outcome. Each weight \( w_i \) quantifies how much its corresponding feature \( x_i \) contributes to increasing or decreasing the log-odds of the target class. The intercept term \( w_0 \) allows the model to fit data where the decision boundary does not pass through the origin.

A positive weight increases the log-odds (and thus the probability) of the event as the feature increases, while a negative weight decreases it. The magnitude of each weight reflects the strength of the feature's effect. By combining all features linearly, logistic regression creates a decision boundary (a line, plane, or hyperplane) that separates the classes in the feature space.  
   The linear combination \( z \) represents the log-odds of the event:
   $$
   \text{logit}(P(y=1|x)) = \mathbf{w}^T \mathbf{x}
   $$

3. **Sigmoid Activation**:  
   The log-odds are converted to a probability using the sigmoid function:
   $$
   P(y=1|x) = \sigma(\mathbf{w}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}}
   $$
   This ensures the output is always between 0 and 1.
    #### The S-Curve of the Sigmoid Function

    The sigmoid function produces an "S-shaped" (sigmoid) curve when plotted, smoothly mapping any real-valued input to a value between 0 and 1. This makes it ideal for modeling probabilities in logistic regression.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    z = np.linspace(-10, 10, 200)
    sigmoid = 1 / (1 + np.exp(-z))

    plt.plot(z, sigmoid)
    plt.title("Sigmoid (Logistic) Function")
    plt.xlabel("z")
    plt.ylabel("σ(z)")
    plt.grid(True)
    plt.show()
    ```

    The plot below illustrates the S-curve:

    ![Sigmoid S-Curve](https://upload.wikimedia.org/wikipedia/commons/8/88/Logistic-curve.svg)

    - For large negative values of \( z \), the output approaches 0.
    - For large positive values of \( z \), the output approaches 1.
    - At \( z = 0 \), the output is 0.5.

    This S-curve enables logistic regression to smoothly transition between class predictions, providing a probabilistic interpretation of the model's output.

Understanind Logistic Regression with the below visualization:

![alt text](image-4.png)

##### Step-by-Step Process

###### **Step 1: Input Variables and Coefficients**
- **x₁, x₂, x₃, ..., xₙ** = Input variables (features)
- **w₀, w₁, w₂, ..., wₙ** = Coefficients (weights) indicating how important each variable is to predict the class

###### **Step 2: Linear Combination (Z)**
We sum all the input variables multiplied by their coefficients since it is a linear model:
```
Z = w₀x₀ + w₁x₁ + w₂x₂ + ... + wₙxₙ
```

###### **Step 3: Logistic Function**
This expression Z is now fed into the **logistic function**, which is the inverse of the log function:
```
σ(Z) = 1/(1 + e^(-z))
```
This gives us a **probability value** between 0 and 1.

###### **Step 4: Iterative Learning**
The loop happens until the probability value is within the acceptable threshold and the model converges.

###### **Step 5: Classification Decision**
Finally, we have a **classifier function**:
- If the probability of the class is **greater than 0.5**, then we say it belongs to **class 1**
- If it is **less than 0.5** threshold, then it is **class 0**

```
ŷ = { 1 if σ(Z) ≥ 0.5
    { 0 otherwise
```

### Key Points:
- **Linear Model**: Combines features with weights (just like linear regression)
- **Probability Output**: Sigmoid function converts linear output to probability (0-1)
- **Binary Decision**: Threshold (0.5) determines final classification
- **Iterative Process**: Model learns optimal weights through training loop

##### Key Properties and Use Cases

- **Interpretability**: The weights indicate the influence of each feature on the log-odds of the target class.
- **Probability Estimates**: Outputs are interpretable as probabilities, useful for risk assessment and decision-making.
- **Binary and Multiclass**: Standard logistic regression handles binary classification; extensions (e.g., softmax regression) support multiclass problems.
- **Baseline Model**: Often used as a baseline due to its simplicity and effectiveness on linearly separable data.

Logistic regression is widely used in fields such as healthcare (disease prediction), finance (credit scoring), marketing (customer conversion), and more, wherever interpretable probability estimates are valuable.

##### Example: Bank Loan Default Prediction

Let's consider a practical example using bank data to predict whether a customer will default on a loan. Here, the input feature is the customer's **salary**, and the target is whether they are a **defaulter** (class 1, shown in red) or **non-defaulter** (class 0, shown in blue).

Suppose we plot the data:

- **Red points**: Customers who defaulted on their loans (defaulters)
- **Blue points**: Customers who did not default (non-defaulters)
- **X-axis**: Salary
- **Y-axis**: Probability of default (as predicted by the model)

The logistic regression model fits a curve (the sigmoid function) to estimate the probability of default based on salary. Lower salaries may be associated with a higher probability of default (red), while higher salaries are associated with a lower probability (blue).

Below is a conceptual illustration:

> **Visualization Placeholder:**  
> <img src="image-5.png" alt="Bank Default Example plot" width="600" height="400">
>
> _[Bank Default Example plot would appear here. Imagine a scatter plot with salary on the x-axis and predicted probability of default > on the y-axis. Red points (defaulters) are clustered at lower salaries with higher probabilities, blue points (non-defaulters) at higher salaries with lower probabilities. The S-shaped logistic curve separates the two groups, with a threshold line at probability 0.5 for classification.]_

- The **S-curve** shows how the probability of being a defaulter decreases as salary increases.
- The **threshold** (often 0.5) is used to classify customers:  
    - If the predicted probability is above 0.5, the customer is classified as a defaulter (red).
    - If below 0.5, as a non-defaulter (blue).

This approach allows banks to estimate the risk of default for new applicants based on their salary and make informed lending decisions.

##### Loss Function and Decision Boundary

A key aspect of logistic regression is how it learns the optimal weights. This is achieved by minimizing a loss function, typically the **log loss** (also called binary cross-entropy loss), which measures how well the predicted probabilities match the actual class labels.

##### Log Loss (Binary Cross-Entropy)

The log loss for \( n \) samples is defined as:

$$
\text{logloss} = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
$$

- \( y_i \): Actual class label (0 or 1) for sample \( i \)
- \( p_i \): Predicted probability that sample \( i \) belongs to class 1

- If the model predicts a probability close to the true label, the loss is low.
- If the prediction is far from the true label, the loss is high.

The model adjusts its weights to minimize this loss during training, improving its predictions.

##### Visualizing the Sigmoid and Decision Boundary

Below is a typical whiteboard illustration of the sigmoid function, class separation, and log loss formula:

> **Visualization Placeholder:**
> <img src="image-6.png" alt="Bank Default Example plot" width="600" height="400">

- based on this image 
    1) tbe blue dots are the non-defaulters
    2) the red dots are the defaulters
    3) the x-axis is the salary
    4) the y-axis is the probability of default

Now as per the image the model is predicting the (1) the blue dot as non-defaulter and (2) the blue dot that is closer to the less salary as non defaulter and probability is some arount 0.3 for (2) 

And for the image 4 and 3 that it has predicted 4 (wrongly predicted) as defaulter for the high salary and 3  (correctly predicted) as defaulter for the low salary

- The **S-curve** represents the sigmoid function mapping input values to probabilities.
- Points above the threshold (e.g., 0.5) are classified as one class, below as the other.
- The log loss formula quantifies prediction error.

Now based on the logloss formule for the non-default whoes lable is 1 and for the defaulte whoes lable is 0,

Let's calculate the log loss for all 4 dots using the formula:

$$
\text{logloss} = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
$$

**Step 1: Dot 1 (Non-defaulter, Correctly Predicted)**
- Actual label: y = 1 (non-defaulter)
- Predicted probability: p ≈ 1.0 (correctly predicted as non-defaulter)
- Calculation:
$$
\text{loss} = 1 \times \log(1.0) + (1-1) \times \log(1 - 1.0) \\
= 1 \times 0 + 0 \times \log(0) \\
= 0
$$
**Result: Loss = 0** (Perfect prediction, no error)

**Step 2: Dot 2 (Non-defaulter, Wrongly Predicted)**
- Actual label: y = 1 (non-defaulter)
- Predicted probability: p = 0.3 (wrongly predicted with low confidence)
- Calculation:
$$
\text{loss} = 1 \times \log(0.3) + (1-1) \times \log(1 - 0.3) \\
= 1 \times \log(0.3) + 0 \times \log(0.7) \\
= \log(0.3) ≈ -0.52
$$
**Result: Loss ≈ 0.52** (High error due to wrong prediction)

**Step 3: Dot 3 (Defaulter, Correctly Predicted)**
- Actual label: y = 0 (defaulter)
- Predicted probability: p ≈ 0.0 (correctly predicted as defaulter)
- Calculation:
$$
\text{loss} = 0 \times \log(0.0) + (1-0) \times \log(1 - 0.0) \\
= 0 \times \log(0) + 1 \times \log(1.0) \\
= 0 + 0 = 0
$$
**Result: Loss = 0** (Perfect prediction, no error)

**Step 4: Dot 4 (Defaulter, Wrongly Predicted)**
- Actual label: y = 0 (defaulter) 
- Predicted probability: p = 0.7 (wrongly predicted as non-defaulter with high confidence)
- Calculation:
$$
\text{loss} = 0 \times \log(0.7) + (1-0) \times \log(1 - 0.7) \\
= 0 \times \log(0.7) + 1 \times \log(0.3) \\
= \log(0.3) ≈ -0.52
$$
**Result: Loss ≈ 0.52** (High error due to wrong prediction)

**Step 5: Final Log Loss Calculation (Apply −1/n × Sum)**
Now we apply the complete log loss formula by taking the negative average of all individual losses:

$$
\text{Total Log Loss} = -\frac{1}{n} \sum_{i=1}^{n} \text{individual losses}
$$

Where n = 4 (total number of data points)

$$
\text{Total Log Loss} = -\frac{1}{4} [(-0) + (-0.52) + (-0) + (-0.52)]
$$

$$
= -\frac{1}{4} [-1.04]
$$

$$
= -\frac{-1.04}{4} = \frac{1.04}{4} = 0.26
$$

**Final Result: Total Log Loss = 0.26**

This means our model has an average log loss of 0.26 across all 4 predictions. The lower the log loss, the better the model performance. A perfect model would have a log loss of 0.

This visualization helps understand how logistic regression separates classes and learns from data by minimizing prediction errors.

##### Practical Implementation: Pima Indians Diabetes Prediction

Let's implement logistic regression using the Pima Indians Diabetes dataset to predict whether a person has diabetes based on various health metrics.

#### Dataset Overview

The Pima Indians Diabetes dataset contains health information for predicting diabetes:
- **Features**: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- **Target**: Outcome (0 = No diabetes, 1 = Has diabetes)
- **Dataset size**: 768 samples (500 non-diabetic, 268 diabetic)

#### Step 1: Import Libraries and Load Data

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Define column names
colNames = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
           'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

# Load the dataset
df = pd.read_csv('./pima-indians-diabetes.data.csv', header=None, names=colNames)

# Display first 5 rows
print(df.head())
```

**Sample Data Output:**
```
   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  DiabetesPedigreeFunction  Age  Outcome
0            6      148             72             35        0  33.6                     0.627   50        1
1            1       85             66             29        0  26.6                     0.351   31        0
2            8      183             64              0        0  23.3                     0.672   32        1
3            1       89             66             23       94  28.1                     0.167   21        0
4            0      137             40             35      168  43.1                     2.288   33        1
```

#### Step 2: Explore Class Distribution

```python
# Check class distribution
print(df.groupby('Outcome').count())
```

**Output:**
```
         Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin  BMI  DiabetesPedigreeFunction  Age
Outcome                                                                                                 
0                500      500            500            500      500  500                       500  500
1                268      268            268            268      268  268                       268  268
```

This shows we have **500 non-diabetic** and **268 diabetic** cases.

#### Step 3: Data Visualization

```python
# Create pairplot to visualize relationships between features
sns.pairplot(df)
plt.show()
```

#### Step 4: Prepare Data and Train Model

```python
# Convert to numpy array and separate features from target
array = df.values
X = array[:,:-1]  # All columns except last (features)
Y = array[:,-1]   # Last column (target)

# Split data into training and testing sets (70-30 split)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

# Create and train logistic regression model
clm = LogisticRegression()
clm.fit(x_train, y_train)

# Make predictions on test set
y_predict = clm.predict(x_test)

# Display model coefficients
X_train_columns = colNames[:-1]  # All columns except Outcome
coeff_df = pd.DataFrame(clm.coef_, columns=X_train_columns)
coeff_df['intercept'] = clm.intercept_
print(coeff_df)
```

**Model Coefficients Output:**
```
   Pregnancies   Glucose  BloodPressure  SkinThickness   Insulin       BMI  DiabetesPedigreeFunction       Age  intercept
0     0.056544  0.035585      -0.010878      -0.001791 -0.000989  0.107612                  0.523938  0.035826  -9.390747
```

**Coefficient Interpretation:**
- **Positive coefficients** (Pregnancies, Glucose, BMI, DiabetesPedigreeFunction, Age): Increase diabetes probability
- **Negative coefficients** (BloodPressure, SkinThickness, Insulin): Decrease diabetes probability
- **Glucose (0.035585)** and **BMI (0.107612)** have strong positive effects
- **DiabetesPedigreeFunction (0.523938)** has the strongest positive effect

#### Step 5: Model Evaluation

```python
# Calculate model accuracy
model_score = clm.score(x_test, y_test)
print("Model Accuracy: ", model_score)

# Generate confusion matrix
cm = metrics.confusion_matrix(y_test, y_predict)
print("Confusion Matrix:")
print(cm)
```

**Results:**
```
Model Accuracy: 0.7402597402597403 (74.03%)

Confusion Matrix:
[[121  30]
 [ 30  50]]
```

#### Step 6: Detailed Performance Metrics

From the confusion matrix, we can extract:

**Confusion Matrix Analysis:**
- **True Negatives (TN)**: 121 - Correctly predicted as non-diabetic
- **False Positives (FP)**: 30 - Incorrectly predicted as diabetic (Type I error)
- **False Negatives (FN)**: 30 - Incorrectly predicted as non-diabetic (Type II error)
- **True Positives (TP)**: 50 - Correctly predicted as diabetic

```python
# Calculate detailed metrics
TN, FP, FN, TP = 121, 30, 30, 50

# Accuracy: (TP + TN) / (TP + TN + FP + FN)
accuracy = (TP + TN) / (TP + TN + FP + FN)
print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# Precision: TP / (TP + FP) - Of all positive predictions, how many were correct?
precision = TP / (TP + FP)
print(f"Precision: {precision:.4f} ({precision*100:.2f}%)")

# Recall (Sensitivity): TP / (TP + FN) - Of all actual positives, how many were detected?
recall = TP / (TP + FN)
print(f"Recall: {recall:.4f} ({recall*100:.2f}%)")

# Specificity: TN / (TN + FP) - Of all actual negatives, how many were correctly identified?
specificity = TN / (TN + FP)
print(f"Specificity: {specificity:.4f} ({specificity*100:.2f}%)")

# F1-Score: 2 * (Precision * Recall) / (Precision + Recall)
f1_score = 2 * (precision * recall) / (precision + recall)
print(f"F1-Score: {f1_score:.4f} ({f1_score*100:.2f}%)")
```

**Final Performance Metrics:**
```
Accuracy: 0.7403 (74.03%)
Precision: 0.6250 (62.50%)
Recall: 0.6250 (62.50%)
Specificity: 0.8013 (80.13%)
F1-Score: 0.6250 (62.50%)
```

#### Performance Interpretation:

- **Accuracy (74.03%)**: Overall, the model correctly classifies 74% of cases
- **Precision (62.50%)**: When the model predicts diabetes, it's correct 62.5% of the time
- **Recall (62.50%)**: The model detects 62.5% of all actual diabetes cases
- **Specificity (80.13%)**: The model correctly identifies 80.1% of non-diabetic cases
- **F1-Score (62.50%)**: Balanced measure of precision and recall

**Clinical Implications:**
- **High Specificity**: Good at ruling out diabetes in healthy individuals
- **Moderate Recall**: Misses 37.5% of actual diabetes cases (concerning for medical screening)
- **Equal Precision and Recall**: Balanced performance for both positive and negative predictions

This example demonstrates how logistic regression can be applied to real-world medical prediction problems with interpretable results.

#### Logistic Regression Applications:

**Binary Classification:**
- Medical Diagnosis (disease/no disease)
- Email Spam Detection (spam/not spam)
- Marketing (buy/don't buy)
- Credit Approval (approve/reject)
- Fraud Detection (fraudulent/legitimate)

**Multiclass Classification (with extensions):**
- Image Classification
- Text Classification (topic categorization)
- Multi-level Sentiment Analysis

**Probability Estimation:**
- Risk Assessment in finance
- A/B Testing conversion rates
- Clinical trial success probability

**When to use Logistic Regression:**
- Need probability estimates, not just classifications
- Interpretability is important
- Small to medium datasets
- Features have linear relationship with log-odds
- As baseline before complex algorithms

- **Linear Discriminant Analysis (LDA)**: Finds linear combinations of features for class separation
- **Support Vector Machine (SVM)**: Creates optimal hyperplane to separate classes

### Tree-Based Algorithms

- **Decision Trees**: Uses tree-like model of decisions and their consequences
- **Random Forest**: Ensemble of decision trees with voting mechanism
- **Gradient Boosting**: Sequential ensemble that corrects previous model errors
- **XGBoost**: Optimized gradient boosting framework
- **AdaBoost**: Adaptive boosting that focuses on misclassified examples

### Probabilistic Algorithms

- **Naive Bayes**: Based on Bayes' theorem with independence assumption
- **Gaussian Naive Bayes**: For continuous features with normal distribution
- **Multinomial Naive Bayes**: For discrete features (text classification)

### Instance-Based Algorithms

- **K-Nearest Neighbors (KNN)**: Classifies based on majority vote of k nearest neighbors
- **K-Means**: Clustering algorithm adapted for classification

### Neural Network Algorithms

- **Perceptron**: Single-layer neural network for linearly separable data
- **Multi-Layer Perceptron (MLP)**: Deep neural network with hidden layers
- **Convolutional Neural Networks (CNN)**: Specialized for image classification
- **Recurrent Neural Networks (RNN)**: For sequential data classification

### Ensemble Methods

- **Bagging**: Bootstrap aggregating with parallel model training
- **Voting Classifier**: Combines predictions from multiple algorithms
- **Stacking**: Uses meta-learner to combine base model predictions

## Logistic Regression: Theory, Intuition, and Practical Implementation

### Easy Understanding of Logistic Regression

![alt text](image-18.png)
![alt text](image-19.png)
![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-22.png)
![alt text](image-23.png)
![alt text](image-24.png)
![alt text](image-25.png)
![alt text](image-26.png)
![alt text](image-27.png)

![alt text](image-28.png)
![alt text](image-29.png)
![alt text](image-30.png)
![alt text](image-31.png)
![alt text](image-32.png)
![alt text](image-33.png)
![alt text](image-34.png)
![alt text](image-35.png)
![alt text](image-36.png)

![alt text](image-37.png)
---

## Linear Regression Theory

Linear regression is a fundamental statistical method used to model the relationship between a dependent variable and one or more independent variables. It serves as the foundation for many machine learning algorithms and provides interpretable results for predictive modeling.

### General Form of Linear Regression Model

The general form of a linear regression model can be written as:

$$Y = m_1x_1 + m_2x_2 + m_3x_3 + \ldots + m_nx_n + C + e$$

Where:
- **Y** = Regression/dependent variable (target variable we want to predict)
- **x_i** = Independent/explanatory variables (features/predictors)
- **m_i** = Slope coefficients (weights/parameters)
- **C** = Intercept term (bias)
- **e** = Random/stochastic error term

### 2. Components of Linear Regression Model

The equation above represents the **population/true model** and consists of **two main components**:

#### a) Deterministic Component
$$\text{Deterministic part} = m_1x_1 + m_2x_2 + \ldots + m_nx_n + C$$

This can be simplified as: **mx + c**

This component represents the systematic, predictable relationship between the independent and dependent variables.

#### b) Non-deterministic Component
$$\text{Non-deterministic part} = e$$

This represents the random error term that captures all the variability not explained by the deterministic component.

### 3. Conditional Mean and Expected Value

The expression **mx + c** represents the **conditional mean of y**, denoted as **E(y|x_i)**. 

This means:
- It's the **expected value of y** for a given value of x_i
- It represents the average response of Y for specific values of the independent variables

### 4. Individual vs Population Mean

The expression **y = mx + c** states that:
- An individual value of y_i equals the mean of the population of which it is a member
- **Plus or minus** the random error term 'e'

Therefore: $$y_i = E(y|x_i) + e_i$$

### 5. Coefficient of Correlation - Pearson's Coefficient

The **Pearson's coefficient of correlation** ρ(x,y) measures the linear relationship between two variables x and y. It is calculated using:

$$\rho(x,y) = \frac{\text{Cov}(x,y)}{\sigma_x \times \sigma_y}$$

Where:
- **Cov(x,y)** = Covariance between x and y
- **σ_x** = Standard deviation of x
- **σ_y** = Standard deviation of y

The mathematical formula for the correlation coefficient is:

$$r_{xy} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2} \sqrt{\sum(y_i - \bar{y})^2}}$$

#### Interpretation of Correlation Values:

1. **r ≈ 0 (No Correlation)**
   - Variables have no linear relationship
   - Data points are scattered randomly
   - **Generating linear model makes no sense** - the model will not be reliable
   - For a given value of X, there can be many values of Y
   - **Nonlinear models may be better** in such cases

2. **r ≈ -1 (Strong Negative Correlation)**
   - Perfect negative linear relationship
   - As X increases, Y decreases proportionally
   - Data points form a downward sloping line
   - Strong predictive relationship exists

3. **r ≈ +1 (Strong Positive Correlation)**
   - Perfect positive linear relationship
   - As X increases, Y increases proportionally
   - Data points form an upward sloping line
   - Strong predictive relationship exists

![alt text](image-7.png)

![alt text](image-8.png)

**Important Note** - when r value is close to 0 that does not means is no relation btw x & y it only there is no linear relation btw x & y as we are using linear regression model

#### Key Points about Correlation:

- **Range**: Correlation coefficient always lies between -1 and +1
- **Strength**: |r| closer to 1 indicates stronger linear relationship
- **Direction**: Sign indicates positive or negative relationship
- **Linearity**: Only measures **linear** relationships
- **Causation**: Correlation does not imply causation

#### When to Use Linear Regression Based on Correlation:

- **High correlation (|r| > 0.7)**: Linear regression is appropriate
- **Moderate correlation (0.3 < |r| < 0.7)**: Linear regression may work but consider other factors
- **Low correlation (|r| < 0.3)**: Linear regression may not be the best choice
- **Near zero correlation (r ≈ 0)**: Avoid linear regression, consider nonlinear models

This correlation analysis is crucial before applying linear regression to ensure the model will be meaningful and reliable.

### 6. Coefficient of Determination (R²)

The **coefficient of determination**, denoted as **R²** (R-squared), is a key measure that indicates how well a regression model explains the variability in the dependent variable. It represents the percentage of total variance that is explained by the regression line.

#### Understanding Sum of Squares

To understand R², we need to first understand three types of sum of squares:

**1. Total Sum of Squares (SST)**
- Measures the total variability in the dependent variable Y
- SST = Σ(y_i - ȳ)²
- Represents the total variance around the mean

**2. Sum of Squares due to Regression (SSR)**  
- Measures the variability explained by the regression model
- SSR = Σ(ŷ_i - ȳ)²
- Represents variance explained by the fitted line

**3. Sum of Squares due to Error (SSE)**
- Measures the unexplained variability (residuals)
- SSE = Σ(y_i - ŷ_i)²
- Represents variance not explained by the model

#### Mathematical Relationship

The fundamental relationship is:
$$\text{SST} = \text{SSR} + \text{SSE}$$

The coefficient of determination is calculated as:
$$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}}$$

#### Interpretation of R² Values

**1. Perfect Fit (R² = 1)**
- Every data point lies exactly on the regression line
- SSE = 0 for all data points
- SSR should equal SST (SSR/SST = 1)
- Model explains 100% of the variance

**2. Good Fit (R² close to 1)**
- Most data points lie close to the regression line
- Small SSE relative to SST
- High percentage of variance explained

**3. Poor Fit (R² close to 0)**
- Large SSE relative to SST
- SSR/SST will be close to 0
- Model explains very little variance
- **Red flag**: Poor fit means large errors

#### Key Properties of R²

**Range**: R² is always between 0 and 1
- **R² = 0**: Model explains no variance (horizontal line through mean)
- **R² = 1**: Model explains all variance (perfect fit)
- **0 < R² < 1**: Partial explanation of variance

**Interpretation**: 
- R² = 0.85 means the model explains 85% of the variance in Y
- The remaining 15% is unexplained (error/residual variance)

#### Visual Understanding with Variance Decomposition

Consider two scenarios:

**Point A (High R²)**:
- The regression line explains most of the variance
- Small unexplained area (residual variance)
- Good model fit

**Point B (Low R²)**:
- The regression line explains little variance
- Large unexplained area (light grey region)
- Poor model fit

#### Alternative Name and Formula

**R² is also called "r squared" or "coefficient of determination"**

Alternative formula using correlation coefficient:
$$R^2 = r^2$$

Where r is the Pearson correlation coefficient between observed and predicted values.

#### Model Evaluation Guidelines

**R² Interpretation for Model Quality:**
- **R² > 0.8**: Excellent fit
- **0.6 < R² < 0.8**: Good fit  
- **0.4 < R² < 0.6**: Moderate fit
- **R² < 0.4**: Poor fit (consider other models)

#### Important Notes

1. **SSR/SST Relationship**: In regression analysis, SSR/SST (Sum of Squares Regression over Total) is referred to as R² that professors commonly discuss
2. **Model Selection**: R² helps decide whether your model is a good fit or poor fit
3. **Utility Measure**: R² is always between 0 and 1 and serves as a measure of utility of the regression model
4. **Variance Explanation**: The percentage of total variance represented by the line is the coefficient of determination

This metric is essential for evaluating how well your linear regression model performs and whether it's suitable for making predictions.

### 7. Model Parameters

#### Intercept (C)
- **C** is known as the **intercept**
- Represents the **default value of Y** when all independent parameters are 0
- It's the y-value where the regression line crosses the y-axis

#### Slope Coefficients (m₁, m₂, ..., mₙ)
- Known as **slope coefficients**
- Reflect the **change in Y** for **one unit change** in the corresponding independent variable
- Positive coefficient: Y increases as x increases
- Negative coefficient: Y decreases as x increases

### 8. Primary Objective of Linear Regression

In regression analysis, the primary objective is to **explain the average behavior of Y**:
- How, on average, Y responds to changes in the values of the 'x' variables
- An individual Y value will hover around its mean value
- The model captures the central tendency of the relationship

### 9. Error Term Significance

The error term 'e' is a **catch-all** for all those variables that:
- Cannot be introduced in the model for various reasons
- Are unknown or unmeasured
- Represent random variations
- Account for model limitations

### 10. Types of Linearity

The term "**linear**" in linear regression can be interpreted in **two ways**:

#### a) Linearity in the Variables
- The variables x are **raised to power 1**
- No squared terms, cubic terms, or interaction terms
- Example: Y = 2x₁ + 3x₂ + 5 (linear in variables)

#### b) Linearity in the Parameters
- The coefficients m are **raised to power 1**
- Variables x **can be raised to any power**
- The model is linear with respect to the parameters/coefficients
- Example: Y = 2x₁² + 3x₂³ + 5 (linear in parameters, non-linear in variables)

### 11. Mathematical Representation

For a simple linear regression with one independent variable:
$$Y = mx + c + e$$

For multiple linear regression with n independent variables:
$$Y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \ldots + \beta_nx_n + \epsilon$$

Where:
- β₀ = intercept
- βᵢ = slope coefficients
- ε = error term

### 12. Key Assumptions of Linear Regression

1. **Linearity**: Relationship between X and Y is linear
2. **Independence**: Observations are independent of each other
3. **Homoscedasticity**: Constant variance of errors
4. **Normality**: Errors are normally distributed
5. **No Multicollinearity**: Independent variables are not highly correlated

### 13. Applications of Linear Regression

- **Prediction**: Forecasting future values
- **Inference**: Understanding relationships between variables
- **Feature Selection**: Identifying important predictors
- **Baseline Models**: Starting point for complex algorithms
- **Interpretability**: Understanding coefficient meanings

This theoretical foundation provides the basis for understanding how linear relationships can be modeled and how these concepts extend to more complex algorithms like logistic regression in classification tasks.

## Linear Regression: Theory, Intuition, and Practical Implementation

# IMPORTANT - Easy Understanding of Linear Regression

Linear regression is a fundamental statistical method used to model the relationship between a dependent variable and one or more independent variables. It serves as the foundation for many machine learning algorithms and provides interpretable results for predictive modeling.

### Step-by-Step Linear Regression Example

Let's work through a complete linear regression example with house prices to understand the mathematical concepts.

![alt text](image-9.png)

#### **Problem Setup: House Price Prediction**
We want to predict house prices based on house size using the linear equation:
$$y = mx + b$$

Where:
- **y** = House Price (dependent variable)
- **x** = House Size in sq ft (independent variable)  
- **m** = Slope (price increase per sq ft)
- **b** = Y-intercept (base price)

---

![alt text](image-10.png)

#### **Given Dataset: House Size vs Price**
Our training data consists of 5 houses:

| House Size (x) | House Price (y) | x×y | x² |
|---|---|---|---|
| 500 sq ft | $150,000 | 75,000,000 | 250,000 |
| 800 sq ft | $200,000 | 160,000,000 | 640,000 |
| 1000 sq ft | $250,000 | 250,000,000 | 1,000,000 |
| 1200 sq ft | $280,000 | 336,000,000 | 1,440,000 |
| 1500 sq ft | $320,000 | 480,000,000 | 2,250,000 |
| **Totals (Σ)** | **5000** | **1,200,000** | **1,301,000,000** | **5,580,000** |

**Key observations:**
- As house size increases, price generally increases (positive correlation)
- We need to find the best-fit line through these data points
- n = 5 (number of data points)

---

![alt text](image-11.png)

#### **Step 1: Calculate the Slope (m)**

Using the least squares formula:
$$m = \frac{n\sum(xy) - \sum x \sum y}{n\sum(x^2) - (\sum x)^2}$$

**Substitute our values:**
- n = 5
- Σ(xy) = 1,301,000,000
- Σx = 5,000
- Σy = 1,200,000
- Σ(x²) = 5,580,000

$$m = \frac{5 \times 1,301,000,000 - 5,000 \times 1,200,000}{5 \times 5,580,000 - (5,000)^2}$$

**Calculate numerator:**
$$= 6,505,000,000 - 6,000,000,000 = 505,000,000$$

**Calculate denominator:**
$$= 27,900,000 - 25,000,000 = 2,900,000$$

**Final slope:**
$$m = \frac{505,000,000}{2,900,000} = 174.14$$

**Interpretation:** For every 1 sq ft increase in house size, the price increases by $174.14

---

![alt text](image-12.png)

#### **Step 2: Calculate the Y-Intercept (b)**

Using the formula:
$$b = \frac{\sum y - m \sum x}{n}$$

**Substitute values:**
$$b = \frac{1,200,000 - 174.14 \times 5,000}{5}$$

$$b = \frac{1,200,000 - 870,700}{5} = \frac{329,300}{5} = 65,860$$

**Interpretation:** The base price (when size = 0) is $65,860, representing fixed costs like land, permits, etc.

---

![alt text](image-13.png)

#### **Step 3: Final Linear Regression Equation**

Our complete model is:
$$y = 174.14x + 65,860$$

**Model Validation:**
Let's test with a 1000 sq ft house:
$$y = 174.14 \times 1000 + 65,860 = 240,000$$

**Comparison:**
- **Actual price:** $250,000
- **Predicted price:** $240,000
- **Error:** $10,000 (4% difference) - quite good!

---

![alt text](image-14.png)

#### **Step 4: Understanding Model Performance**

**Key Performance Metrics:**

1. **Mean Absolute Error (MAE):** Average of absolute differences between actual and predicted values
2. **Root Mean Square Error (RMSE):** Square root of average squared differences
3. **R² (Coefficient of Determination):** Percentage of variance explained by the model

**Visual Interpretation:**
- Points close to the line indicate good predictions
- Points far from the line indicate larger errors
- The line represents our best estimate for any house size

---

![alt text](image-15.png)

#### **Step 5: Making Predictions**

Now we can predict prices for new houses:

**Example Predictions:**
- **600 sq ft house:** y = 174.14 × 600 + 65,860 = **$170,344**
- **1300 sq ft house:** y = 174.14 × 1300 + 65,860 = **$292,242**
- **2000 sq ft house:** y = 174.14 × 2000 + 65,860 = **$414,140**

**Important Notes:**
- Predictions are most reliable within the range of training data (500-1500 sq ft)
- Extrapolating beyond this range may be less accurate
- The model assumes a linear relationship continues

---

![alt text](image-16.png)

#### **Step 6: Real-World Considerations**

**Model Limitations:**
1. **Linearity Assumption:** Relationship may not be perfectly linear
2. **Single Variable:** Real estate prices depend on many factors (location, age, condition)
3. **Market Changes:** Economic conditions affect pricing
4. **Outliers:** Unusual properties can skew the model

**Improving the Model:**
- Add more features (bedrooms, bathrooms, location)
- Use multiple linear regression
- Consider polynomial or non-linear relationships
- Collect more data points
- Handle outliers appropriately

**Practical Applications:**
- Real estate valuation
- Investment decisions
- Market analysis
- Automated property pricing systems

This step-by-step approach demonstrates how linear regression transforms raw data into actionable insights through mathematical modeling!

---

# 📚 Linear Regression Question Bank

## 📝 Practical Problems

### Problem 1: Linear Regression (Single Variable) - Given Sample

**A company records advertising spend (in thousands of $) and corresponding sales (in thousands of units).**

**Tasks:**
1. Build a simple linear regression model to predict sales from ad spend.
2. Plot regression line and scatter plot.
3. Predict sales when ad spend = 7 (thousand $).

**Note:** Sample datasets are provided. The values may be extended or modified as needed during implementation.

| Ad_Spend | Sales |
|----------|-------|
| 1        | 1.5   |
| 2        | 1.8   |
| 3        | 2.5   |
| 4        | 3.2   |
| 5        | 3.7   |
| 6        | 4.2   |

---

**Step-by-Step Solution:**

**Step 1: Calculate Basic Statistics**

First, let's calculate the mean values:
- Mean of Ad_Spend (x̄) = (1 + 2 + 3 + 4 + 5 + 6) ÷ 6 = 21 ÷ 6 = 3.5
- Mean of Sales (ȳ) = (1.5 + 1.8 + 2.5 + 3.2 + 3.7 + 4.2) ÷ 6 = 16.9 ÷ 6 = 2.817

**Step 2: Calculate the Slope (m)**

Using the formula: m = Σ(xi - x̄)(yi - ȳ) / Σ(xi - x̄)²

| xi | yi | (xi - x̄) | (yi - ȳ) | (xi - x̄)(yi - ȳ) | (xi - x̄)² |
|----|----|-----------|-----------|--------------------|------------|
| 1  | 1.5| -2.5      | -1.317    | 3.293             | 6.25       |
| 2  | 1.8| -1.5      | -1.017    | 1.526             | 2.25       |
| 3  | 2.5| -0.5      | -0.317    | 0.159             | 0.25       |
| 4  | 3.2| 0.5       | 0.383     | 0.192             | 0.25       |
| 5  | 3.7| 1.5       | 0.883     | 1.325             | 2.25       |
| 6  | 4.2| 2.5       | 1.383     | 3.458             | 6.25       |

Σ(xi - x̄)(yi - ȳ) = 9.953
Σ(xi - x̄)² = 17.5

**Slope (m) = 9.953 ÷ 17.5 = 0.569**

**Step 3: Calculate the Y-Intercept (b)**

Using the formula: b = ȳ - m × x̄
b = 2.817 - (0.569 × 3.5) = 2.817 - 1.992 = 0.825

**Step 4: Linear Regression Equation**

**Sales = 0.569 × Ad_Spend + 0.825**

**Step 5: Prediction for Ad_Spend = 7**

Sales = 0.569 × 7 + 0.825 = 3.983 + 0.825 = **4.808 thousand units**

**Step 6: Model Evaluation**

Calculate R² (coefficient of determination):
- SST = Σ(yi - ȳ)² = 5.657
- SSR = Σ(ŷi - ȳ)² = 5.664  
- **R² = 0.999 (99.9% variance explained)**

**Answer:** The model predicts 4.808 thousand units sales for 7 thousand $ ad spend.

---

### Problem 2: Student Study Hours vs Exam Scores

**A teacher records student study hours and their corresponding exam scores.**

**Tasks:**
1. Build a linear regression model to predict exam scores from study hours.
2. Calculate correlation coefficient and R².
3. Predict the exam score for a student who studies 9 hours.

| Study_Hours | Exam_Score |
|-------------|------------|
| 2           | 45         |
| 4           | 55         |
| 6           | 65         |
| 8           | 75         |
| 10          | 85         |
| 12          | 95         |

---

**Step-by-Step Solution:**

**Step 1: Calculate Basic Statistics**
- Mean Study_Hours (x̄) = (2+4+6+8+10+12) ÷ 6 = 42 ÷ 6 = 7
- Mean Exam_Score (ȳ) = (45+55+65+75+85+95) ÷ 6 = 420 ÷ 6 = 70

**Step 2: Calculate Slope and Intercept**

| xi | yi | (xi - x̄) | (yi - ȳ) | (xi - x̄)(yi - ȳ) | (xi - x̄)² |
|----|----|-----------|-----------|--------------------|------------|
| 2  | 45 | -5        | -25       | 125               | 25         |
| 4  | 55 | -3        | -15       | 45                | 9          |
| 6  | 65 | -1        | -5        | 5                 | 1          |
| 8  | 75 | 1         | 5         | 5                 | 1          |
| 10 | 85 | 3         | 15        | 45                | 9          |
| 12 | 95 | 5         | 25        | 125               | 25         |

- Slope (m) = 350 ÷ 70 = **5**
- Intercept (b) = 70 - (5 × 7) = **35**

**Step 3: Linear Regression Equation**
**Exam_Score = 5 × Study_Hours + 35**

**Step 4: Prediction for 9 Study Hours**
Exam_Score = 5 × 9 + 35 = **80 points**

**Step 5: Correlation and R²**
- Correlation coefficient (r) = 1.0 (perfect positive correlation)
- R² = 1.0 (100% variance explained)

---

### Problem 3: Temperature vs Ice Cream Sales

**An ice cream vendor records daily temperature and ice cream sales.**

**Tasks:**
1. Develop a linear regression model to predict sales from temperature.
2. Interpret the slope and intercept.
3. Predict sales when temperature = 32°C.

| Temperature (°C) | Sales (units) |
|------------------|---------------|
| 20               | 50            |
| 22               | 65            |
| 25               | 85            |
| 28               | 105           |
| 30               | 120           |
| 35               | 150           |

---

**Step-by-Step Solution:**

**Step 1: Calculate Basic Statistics**
- Mean Temperature (x̄) = (20+22+25+28+30+35) ÷ 6 = 160 ÷ 6 = 26.67
- Mean Sales (ȳ) = (50+65+85+105+120+150) ÷ 6 = 575 ÷ 6 = 95.83

**Step 2: Calculate Regression Coefficients**

| xi | yi  | (xi - x̄) | (yi - ȳ) | (xi - x̄)(yi - ȳ) | (xi - x̄)² |
|----|-----|-----------|-----------|--------------------|------------|
| 20 | 50  | -6.67     | -45.83    | 305.5             | 44.49      |
| 22 | 65  | -4.67     | -30.83    | 143.98            | 21.81      |
| 25 | 85  | -1.67     | -10.83    | 18.09             | 2.79       |
| 28 | 105 | 1.33      | 9.17      | 12.20             | 1.77       |
| 30 | 120 | 3.33      | 24.17     | 80.49             | 11.09      |
| 35 | 150 | 8.33      | 54.17     | 451.24            | 69.39      |

- Slope (m) = 1011.5 ÷ 151.34 = **6.69**
- Intercept (b) = 95.83 - (6.69 × 26.67) = **-82.53**

**Step 3: Linear Regression Equation**
**Sales = 6.69 × Temperature - 82.53**

**Step 4: Interpretation**
- **Slope (6.69)**: For every 1°C increase in temperature, ice cream sales increase by 6.69 units
- **Intercept (-82.53)**: Theoretical sales when temperature is 0°C (not meaningful in practice)

**Step 5: Prediction for 32°C**
Sales = 6.69 × 32 - 82.53 = 214.08 - 82.53 = **131.55 units**

---

### Problem 4: Years of Experience vs Salary

**A company records employee years of experience and their annual salaries.**

**Tasks:**
1. Build a linear regression model to predict salary from experience.
2. Calculate performance metrics (R², MSE, RMSE).
3. Predict salary for 7 years of experience.

| Experience (years) | Salary (thousands $) |
|--------------------|----------------------|
| 1                  | 35                   |
| 2                  | 42                   |
| 3                  | 49                   |
| 4                  | 56                   |
| 5                  | 63                   |
| 6                  | 70                   |

---

**Step-by-Step Solution:**

**Step 1: Calculate Basic Statistics**
- Mean Experience (x̄) = (1+2+3+4+5+6) ÷ 6 = 21 ÷ 6 = 3.5
- Mean Salary (ȳ) = (35+42+49+56+63+70) ÷ 6 = 315 ÷ 6 = 52.5

**Step 2: Calculate Regression Coefficients**

| xi | yi | (xi - x̄) | (yi - ȳ) | (xi - x̄)(yi - ȳ) | (xi - x̄)² |
|----|----|-----------|-----------|--------------------|------------|
| 1  | 35 | -2.5      | -17.5     | 43.75             | 6.25       |
| 2  | 42 | -1.5      | -10.5     | 15.75             | 2.25       |
| 3  | 49 | -0.5      | -3.5      | 1.75              | 0.25       |
| 4  | 56 | 0.5       | 3.5       | 1.75              | 0.25       |
| 5  | 63 | 1.5       | 10.5      | 15.75             | 2.25       |
| 6  | 70 | 2.5       | 17.5      | 43.75             | 6.25       |

- Slope (m) = 122.5 ÷ 17.5 = **7**
- Intercept (b) = 52.5 - (7 × 3.5) = **28**

**Step 3: Linear Regression Equation**
**Salary = 7 × Experience + 28**

**Step 4: Performance Metrics**
- Calculate predicted values and residuals:
- MSE = Σ(yi - ŷi)² / n = 0 (perfect fit)
- RMSE = √MSE = 0
- R² = 1.0 (100% variance explained)

**Step 5: Prediction for 7 Years Experience**
Salary = 7 × 7 + 28 = 49 + 28 = **77 thousand $**

---

### Problem 5: Car Age vs Resale Value

**A car dealer records car age and resale values.**

**Tasks:**
1. Create a linear regression model to predict resale value from car age.
2. Analyze the negative relationship between variables.
3. Predict resale value for a 4-year-old car.

| Car_Age (years) | Resale_Value (thousands $) |
|-----------------|----------------------------|
| 1               | 18                         |
| 2               | 15                         |
| 3               | 12                         |
| 5               | 6                          |
| 6               | 3                          |
| 8               | -3                         |

---

**Step-by-Step Solution:**

**Step 1: Calculate Basic Statistics**
- Mean Car_Age (x̄) = (1+2+3+5+6+8) ÷ 6 = 25 ÷ 6 = 4.17
- Mean Resale_Value (ȳ) = (18+15+12+6+3-3) ÷ 6 = 51 ÷ 6 = 8.5

**Step 2: Calculate Regression Coefficients**

| xi | yi | (xi - x̄) | (yi - ȳ) | (xi - x̄)(yi - ȳ) | (xi - x̄)² |
|----|----|-----------|-----------|--------------------|------------|
| 1  | 18 | -3.17     | 9.5       | -30.12            | 10.04      |
| 2  | 15 | -2.17     | 6.5       | -14.11            | 4.71       |
| 3  | 12 | -1.17     | 3.5       | -4.10             | 1.37       |
| 5  | 6  | 0.83      | -2.5      | -2.08             | 0.69       |
| 6  | 3  | 1.83      | -5.5      | -10.07            | 3.35       |
| 8  | -3 | 3.83      | -11.5     | -44.05            | 14.67      |

- Slope (m) = -104.53 ÷ 34.83 = **-3.0**
- Intercept (b) = 8.5 - (-3.0 × 4.17) = **21.01**

**Step 3: Linear Regression Equation**
**Resale_Value = -3.0 × Car_Age + 21.01**

**Step 4: Interpretation**
- **Negative Slope (-3.0)**: Car value decreases by $3,000 per year
- **Intercept (21.01)**: Initial car value when new

**Step 5: Prediction for 4-Year-Old Car**
Resale_Value = -3.0 × 4 + 21.01 = -12 + 21.01 = **$9,010**

---

## Theoretical Questions and Detailed Answers

### Question 1: What is the mathematical formula for linear regression and explain each component?

**Answer:**

**Linear Regression Mathematical Formula:**

For simple linear regression:
$$y = \beta_0 + \beta_1x + \epsilon$$

For multiple linear regression:
$$y = \beta_0 + \beta_1x_1 + \beta_2x_2 + ... + \beta_px_p + \epsilon$$

**Component Breakdown:**

1. **y (Dependent Variable)**
   - **Definition:** The target variable we want to predict
   - **Examples:** House price, student score, sales revenue
   - **Type:** Continuous numerical variable

2. **β₀ (Intercept/Bias Term)**
   - **Definition:** The value of y when all x variables equal zero
   - **Interpretation:** Baseline value of the dependent variable
   - **Mathematical Role:** Shifts the regression line up or down

3. **β₁, β₂, ..., βₚ (Regression Coefficients/Slopes)**
   - **Definition:** Rate of change in y for a unit change in corresponding x
   - **Interpretation:** β₁ means "for every 1 unit increase in x₁, y increases by β₁ units"
   - **Sign Significance:**
     - Positive β: Positive relationship between x and y
     - Negative β: Negative relationship between x and y

4. **x₁, x₂, ..., xₚ (Independent Variables/Features)**
   - **Definition:** Input variables used to predict y
   - **Examples:** House size, location, age for predicting price
   - **Requirements:** Should be linearly related to the target

5. **ε (Error Term/Residual)**
   - **Definition:** Difference between actual and predicted values
   - **Formula:** ε = y_actual - y_predicted
   - **Assumptions:** 
     - Mean = 0
     - Constant variance (homoscedasticity)
     - Normal distribution
     - Independence

**Matrix Form:**
$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

Where:
- **y** is n×1 vector of target values
- **X** is n×(p+1) design matrix (includes intercept column)
- **β** is (p+1)×1 vector of parameters
- **ε** is n×1 vector of errors

**Parameter Estimation (Ordinary Least Squares):**
$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

**Practical Example:**
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# House price prediction: Price = β₀ + β₁×Size + β₂×Rooms
# Sample data
X = np.array([[1500, 3], [2000, 4], [1200, 2], [1800, 3]])  # Size, Rooms
y = np.array([300000, 400000, 250000, 350000])  # Price

model = LinearRegression()
model.fit(X, y)

print(f"Intercept (β₀): ${model.intercept_:,.2f}")
print(f"Size coefficient (β₁): ${model.coef_[0]:.2f} per sq ft")
print(f"Rooms coefficient (β₂): ${model.coef_[1]:,.2f} per room")

# Prediction for 1600 sq ft, 3 rooms house
prediction = model.predict([[1600, 3]])
print(f"Predicted price: ${prediction[0]:,.2f}")
```

This formula forms the foundation for understanding how linear regression models the relationship between independent and dependent variables through a linear combination of features.

### Question 2: What are the main uses and applications of linear regression?

**Answer:**

**Linear Regression Applications - Comprehensive Overview:**

**1. Business and Economics**

**A. Sales Forecasting**
- **Application:** Predict future sales based on advertising spend, seasonality, economic indicators
- **Formula:** Sales = β₀ + β₁×Advertising + β₂×Season + β₃×GDP
- **Example:** Retail company predicting quarterly revenue
```python
# Sales prediction model
sales_features = ['advertising_spend', 'season_index', 'gdp_growth']
sales_model = LinearRegression()
# Predicted sales help in inventory planning and budgeting
```

**B. Price Optimization**
- **Application:** Determine optimal pricing strategy
- **Variables:** Cost, competition, demand elasticity
- **Use Case:** E-commerce dynamic pricing

**C. Financial Analysis**
- **Applications:**
  - Stock price prediction based on market indicators
  - Risk assessment using financial ratios
  - Portfolio optimization
- **Example:** Bank loan approval based on income, credit score, debt-to-income ratio

**2. Real Estate and Property**

**A. Property Valuation**
- **Most Common Application:** Automated Valuation Models (AVMs)
- **Key Features:**
  - Square footage
  - Number of bedrooms/bathrooms
  - Location (zip code, neighborhood)
  - Age of property
  - Recent comparable sales

**Detailed Example:**
```python
# Real estate price prediction
property_features = [
    'sqft', 'bedrooms', 'bathrooms', 'age', 
    'garage', 'pool', 'school_rating', 'crime_rate'
]

# Model: Price = β₀ + β₁×sqft + β₂×bedrooms + ... + β₈×crime_rate
# Interpretation: Each coefficient shows price impact of that feature
```

**B. Rental Market Analysis**
- Rent prediction based on property characteristics
- Market trend analysis
- Investment property evaluation

**3. Healthcare and Medical Research**

**A. Drug Dosage Optimization**
- **Application:** Determine effective drug dosage
- **Variables:** Patient weight, age, kidney function, severity
- **Formula:** Dosage = β₀ + β₁×Weight + β₂×Age + β₃×Kidney_Function

**B. Medical Cost Prediction**
- Predict healthcare costs based on patient characteristics
- Insurance premium calculation
- Hospital resource allocation

**C. Clinical Research**
- Analyze treatment effectiveness
- Dose-response relationships
- Biomarker analysis

**4. Marketing and Advertising**

**A. Marketing Mix Modeling**
- **Objective:** Measure impact of different marketing channels
- **Formula:** Sales = β₀ + β₁×TV + β₂×Digital + β₃×Print + β₄×Radio
- **Benefits:** Budget allocation across channels

**B. Customer Lifetime Value (CLV)**
- Predict long-term customer value
- Variables: Purchase history, demographics, engagement metrics

**C. A/B Testing Analysis**
- Measure impact of website changes
- Email campaign effectiveness
- Ad creative performance

**5. Manufacturing and Quality Control**

**A. Process Optimization**
- **Application:** Optimize manufacturing parameters
- **Variables:** Temperature, pressure, speed, humidity
- **Goal:** Predict product quality or yield

**Example:**
```python
# Manufacturing yield prediction
# Yield = β₀ + β₁×Temperature + β₂×Pressure + β₃×Speed
# Helps optimize settings for maximum output
```

**B. Defect Prediction**
- Predict defect rates based on process variables
- Quality control and Six Sigma initiatives
- Preventive maintenance scheduling

**6. Agriculture and Environmental Science**

**A. Crop Yield Prediction**
- **Variables:** Rainfall, temperature, soil quality, fertilizer amount
- **Application:** Farm planning and insurance
- **Formula:** Yield = β₀ + β₁×Rainfall + β₂×Temperature + β₃×Fertilizer

**B. Environmental Monitoring**
- Air quality prediction
- Climate change analysis
- Resource consumption modeling

**7. Transportation and Logistics**

**A. Traffic Flow Analysis**
- Predict traffic volume based on time, weather, events
- Route optimization
- Infrastructure planning

**B. Fuel Consumption Modeling**
- Vehicle efficiency analysis
- Fleet management optimization
- Environmental impact assessment

**8. Education and Social Sciences**

**A. Student Performance Prediction**
- **Variables:** Study hours, attendance, previous grades, socioeconomic factors
- **Applications:** 
  - Early intervention identification
  - Resource allocation
  - Curriculum effectiveness

**B. Demographic Analysis**
- Population growth prediction
- Social policy impact assessment
- Economic inequality studies

**9. Technology and Software**

**A. Resource Usage Prediction**
- **Application:** Cloud computing resource allocation
- **Variables:** User activity, time of day, application type
- **Benefit:** Cost optimization and performance improvement

**B. Performance Modeling**
- Website load time prediction
- Database query optimization
- System capacity planning

**10. Sports Analytics**

**A. Player Performance Analysis**
- Predict player statistics based on training, health, opponent strength
- Salary negotiation support
- Team composition optimization

**B. Betting and Gaming**
- Odds calculation
- Risk assessment
- Outcome prediction

**11. Practical Implementation Example**

**Complete Business Case: E-commerce Sales Prediction**

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# Sample e-commerce data
data = {
    'advertising_spend': [10000, 15000, 8000, 12000, 20000],
    'website_traffic': [50000, 75000, 40000, 60000, 100000],
    'email_campaigns': [5, 8, 3, 6, 10],
    'seasonal_index': [1.2, 0.8, 1.0, 1.5, 0.9],
    'competitor_price': [99, 105, 95, 100, 110],
    'sales': [100000, 150000, 80000, 120000, 200000]
}

df = pd.DataFrame(data)

# Prepare features and target
features = ['advertising_spend', 'website_traffic', 'email_campaigns', 
           'seasonal_index', 'competitor_price']
X = df[features]
y = df['sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Interpretation
print("Sales Prediction Model Coefficients:")
for feature, coef in zip(features, model.coef_):
    print(f"{feature}: {coef:.2f}")
    
print(f"Intercept: {model.intercept_:.2f}")

# Business insights
print("\nBusiness Insights:")
print(f"- Each $1 in advertising generates ${model.coef_[0]:.2f} in sales")
print(f"- Each visitor generates ${model.coef_[1]:.4f} in sales")
print(f"- Each email campaign generates ${model.coef_[2]:.2f} in sales")
```

**12. Key Advantages for These Applications**

**A. Interpretability**
- Clear understanding of feature impact
- Easy to explain to stakeholders
- Regulatory compliance (e.g., loan approval explanations)

**B. Speed and Efficiency**
- Fast training and prediction
- Suitable for real-time applications
- Low computational requirements

**C. Baseline Performance**
- Good starting point for complex problems
- Benchmark for more sophisticated models
- Often surprisingly effective for linear relationships

**D. Statistical Foundation**
- Well-established theory
- Confidence intervals and hypothesis testing
- Assumption checking and diagnostics

Linear regression's versatility makes it applicable across virtually every industry where quantitative prediction or relationship modeling is needed. Its simplicity, interpretability, and solid statistical foundation ensure it remains a fundamental tool in data science and analytics.

### Question 3: How do you calculate the slope and intercept in linear regression manually?

**Answer:**

**Manual Calculation of Linear Regression Parameters:**

**1. Mathematical Formulas**

For simple linear regression: y = β₀ + β₁x

**Slope (β₁) Formula:**
$$\beta_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

**Alternative slope formula:**
$$\beta_1 = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}$$

**Intercept (β₀) Formula:**
$$\beta_0 = \bar{y} - \beta_1\bar{x}$$

Where:
- **x̄** = mean of x values
- **ȳ** = mean of y values  
- **n** = number of data points

**2. Step-by-Step Manual Calculation**

**Example Dataset:** Hours studied vs Exam score

| Student | Hours (x) | Score (y) |
|---------|-----------|-----------|
| 1       | 2         | 65        |
| 2       | 4         | 75        |
| 3       | 6         | 85        |
| 4       | 8         | 90        |
| 5       | 10        | 95        |

**Step 1: Calculate Means**
```
x̄ = (2 + 4 + 6 + 8 + 10) / 5 = 30 / 5 = 6
ȳ = (65 + 75 + 85 + 90 + 95) / 5 = 410 / 5 = 82
```

**Step 2: Create Calculation Table**

| i | xᵢ | yᵢ | (xᵢ - x̄) | (yᵢ - ȳ) | (xᵢ - x̄)(yᵢ - ȳ) | (xᵢ - x̄)² |
|---|----|----|-----------|-----------|-------------------|------------|
| 1 | 2  | 65 | -4        | -17       | 68                | 16         |
| 2 | 4  | 75 | -2        | -7        | 14                | 4          |
| 3 | 6  | 85 | 0         | 3         | 0                 | 0          |
| 4 | 8  | 90 | 2         | 8         | 16                | 4          |
| 5 | 10 | 95 | 4         | 13        | 52                | 16         |
|**Σ**|**30**|**410**|**0**|**0**|**150**|**40**|

**Step 3: Calculate Slope (β₁)**
$$\beta_1 = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2} = \frac{150}{40} = 3.75$$

**Step 4: Calculate Intercept (β₀)**
$$\beta_0 = \bar{y} - \beta_1\bar{x} = 82 - 3.75 \times 6 = 82 - 22.5 = 59.5$$

**Step 5: Final Regression Equation**
$$y = 59.5 + 3.75x$$

**Interpretation:**
- **Intercept (59.5):** Expected score with 0 hours of study
- **Slope (3.75):** Each additional hour of study increases score by 3.75 points

**3. Alternative Method Using Sums**

**Step 1: Calculate Required Sums**

| i | xᵢ | yᵢ | xᵢ² | xᵢyᵢ |
|---|----|----|-----|------|
| 1 | 2  | 65 | 4   | 130  |
| 2 | 4  | 75 | 16  | 300  |
| 3 | 6  | 85 | 36  | 510  |
| 4 | 8  | 90 | 64  | 720  |
| 5 | 10 | 95 | 100 | 950  |
|**Σ**|**30**|**410**|**220**|**2610**|

**Step 2: Apply Alternative Slope Formula**
$$\beta_1 = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}$$

$$\beta_1 = \frac{5 \times 2610 - 30 \times 410}{5 \times 220 - 30^2}$$

$$\beta_1 = \frac{13050 - 12300}{1100 - 900} = \frac{750}{200} = 3.75$$

**Step 3: Calculate Intercept**
$$\beta_0 = \frac{\sum y - \beta_1 \sum x}{n} = \frac{410 - 3.75 \times 30}{5} = \frac{410 - 112.5}{5} = \frac{297.5}{5} = 59.5$$

**4. Python Implementation for Verification**

```python
import numpy as np

def manual_linear_regression(x, y):
    """
    Calculate linear regression coefficients manually
    """
    n = len(x)
    
    # Method 1: Using means and deviations
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean)**2 for i in range(n))
    
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    
    return intercept, slope

# Example data
x = [2, 4, 6, 8, 10]
y = [65, 75, 85, 90, 95]

# Manual calculation
intercept, slope = manual_linear_regression(x, y)
print(f"Manual Calculation:")
print(f"Intercept (β₀): {intercept}")
print(f"Slope (β₁): {slope}")

# Verify with sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array(x).reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

print(f"\nSklearn Verification:")
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")
```

**5. Complete Manual Calculation Walkthrough**

**Problem:** Car Age vs Resale Value

| Car Age (years) | Resale Value ($1000s) |
|-----------------|----------------------|
| 1               | 18                   |
| 2               | 16                   |
| 3               | 13                   |
| 4               | 10                   |
| 5               | 8                    |

**Manual Solution:**

**Step 1: Set up data**
- x = [1, 2, 3, 4, 5] (age in years)
- y = [18, 16, 13, 10, 8] (value in $1000s)
- n = 5

**Step 2: Calculate means**
- x̄ = (1+2+3+4+5)/5 = 15/5 = 3
- ȳ = (18+16+13+10+8)/5 = 65/5 = 13

**Step 3: Calculate deviations and products**

| i | xᵢ | yᵢ | (xᵢ-x̄) | (yᵢ-ȳ) | (xᵢ-x̄)(yᵢ-ȳ) | (xᵢ-x̄)² |
|---|----|----|---------|---------|----------------|----------|
| 1 | 1  | 18 | -2      | 5       | -10            | 4        |
| 2 | 2  | 16 | -1      | 3       | -3             | 1        |
| 3 | 3  | 13 | 0       | 0       | 0              | 0        |
| 4 | 4  | 10 | 1       | -3      | -3             | 1        |
| 5 | 5  | 8  | 2       | -5      | -10            | 4        |
|**Σ**|-|-|-|-|**-26**|**10**|

**Step 4: Calculate slope**
β₁ = Σ(xᵢ-x̄)(yᵢ-ȳ) / Σ(xᵢ-x̄)² = -26/10 = -2.6

**Step 5: Calculate intercept**
β₀ = ȳ - β₁x̄ = 13 - (-2.6)(3) = 13 + 7.8 = 20.8

**Step 6: Final equation**
**Resale Value = 20.8 - 2.6 × Age**

**Interpretation:**
- **Intercept (20.8):** New car value is $20,800
- **Slope (-2.6):** Car loses $2,600 in value each year

**Step 7: Make predictions**
For a 3-year-old car: Value = 20.8 - 2.6(3) = 20.8 - 7.8 = $13,000

**6. Understanding the Mathematics**

**Why These Formulas Work:**

**A. Least Squares Principle**
- We want to minimize: Σ(yᵢ - ŷᵢ)²
- Where ŷᵢ = β₀ + β₁xᵢ
- Taking derivatives and setting to zero gives our formulas

**B. Geometric Interpretation**
- Slope = Rise/Run = Δy/Δx
- We use weighted average of all individual slopes
- Weights are based on how far x values are from mean

**C. Correlation Connection**
- β₁ = r × (sᵧ/sₓ)
- Where r is correlation coefficient
- sᵧ, sₓ are standard deviations of y and x

**7. Common Calculation Mistakes**

**Mistake 1: Wrong Mean Calculation**
```
# Wrong: Using different sample sizes
x̄ = sum(some_x_values) / len(all_x_values)

# Correct: Same denominator
x̄ = sum(x_values) / len(x_values)
```

**Mistake 2: Sign Errors**
```
# Careful with negative values
(xᵢ - x̄) × (yᵢ - ȳ)
# When both are negative: (-2) × (-3) = +6
# When one is negative: (-2) × (+3) = -6
```

**Mistake 3: Intercept Formula**
```
# Wrong: β₀ = ȳ + β₁x̄
# Correct: β₀ = ȳ - β₁x̄
```

Manual calculation of linear regression parameters provides deep understanding of how the algorithm works and builds intuition for interpreting results in real-world applications.

### Question 4: What are the key performance evaluation metrics for linear regression?

**Answer:**

**Performance Evaluation Metrics for Linear Regression:**

**1. Mean Squared Error (MSE)**

**Formula:**
$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

**Characteristics:**
- **Units:** Squared units of target variable
- **Range:** 0 to ∞ (lower is better)
- **Sensitivity:** Heavily penalizes large errors due to squaring
- **Use Case:** When large errors are particularly undesirable

**Practical Example:**
```python
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# House price prediction example
actual_prices = np.array([300000, 450000, 250000, 600000, 350000])
predicted_prices = np.array([280000, 470000, 240000, 580000, 370000])

mse = mean_squared_error(actual_prices, predicted_prices)
print(f"MSE: ${mse:,.2f}")

# Manual calculation
manual_mse = np.mean((actual_prices - predicted_prices)**2)
print(f"Manual MSE: ${manual_mse:,.2f}")

# Individual squared errors
squared_errors = (actual_prices - predicted_prices)**2
print("Individual squared errors:", squared_errors)
```

**Interpretation:**
- MSE of $400,000,000 means average squared error is $400M
- Square root gives us back original units (RMSE)

**2. Root Mean Squared Error (RMSE)**

**Formula:**
$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2} = \sqrt{MSE}$$

**Advantages:**
- **Same units** as target variable
- **Interpretable magnitude** of typical error
- **Standard metric** for many competitions

**Example:**
```python
from sklearn.metrics import mean_squared_error

rmse = np.sqrt(mean_squared_error(actual_prices, predicted_prices))
print(f"RMSE: ${rmse:,.2f}")

# This means typical prediction error is about $20,000
```

**Business Interpretation:**
- RMSE of $20,000 for house prices: "Typical prediction error is $20K"
- Can compare with average house price to assess relative performance

**3. Mean Absolute Error (MAE)**

**Formula:**
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

**Characteristics:**
- **Units:** Same as target variable
- **Robust to outliers:** Doesn't square the errors
- **Equal penalty:** All errors weighted equally
- **Interpretable:** Average absolute deviation

**Example:**
```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(actual_prices, predicted_prices)
print(f"MAE: ${mae:,.2f}")

# Manual calculation
manual_mae = np.mean(np.abs(actual_prices - predicted_prices))
print(f"Manual MAE: ${manual_mae:,.2f}")

# Individual absolute errors
abs_errors = np.abs(actual_prices - predicted_prices)
print("Individual absolute errors:", abs_errors)
```

**MAE vs RMSE Comparison:**
```python
print(f"MAE: ${mae:,.2f}")
print(f"RMSE: ${rmse:,.2f}")
print(f"RMSE/MAE ratio: {rmse/mae:.2f}")

# When RMSE/MAE ≈ 1: Errors are consistent
# When RMSE/MAE > 1.5: Some large outliers present
```

**4. R-squared (Coefficient of Determination)**

**Formula:**
$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

Where:
- **SS_res:** Sum of squares of residuals (prediction errors)
- **SS_tot:** Total sum of squares (variance from mean)

**Interpretation:**
- **Range:** -∞ to 1 (higher is better)
- **Meaning:** Proportion of variance in y explained by the model
- **R² = 0.85:** Model explains 85% of variance in target variable

**Detailed Example:**
```python
from sklearn.metrics import r2_score

# Calculate R²
r2 = r2_score(actual_prices, predicted_prices)
print(f"R²: {r2:.4f} ({r2*100:.2f}%)")

# Manual calculation
y_mean = np.mean(actual_prices)
ss_tot = np.sum((actual_prices - y_mean)**2)
ss_res = np.sum((actual_prices - predicted_prices)**2)
manual_r2 = 1 - (ss_res / ss_tot)

print(f"Manual R²: {manual_r2:.4f}")
print(f"Model explains {manual_r2*100:.2f}% of price variance")
```

**R² Interpretation Guide:**
- **R² > 0.9:** Excellent fit
- **0.7 < R² < 0.9:** Good fit  
- **0.5 < R² < 0.7:** Moderate fit
- **R² < 0.5:** Poor fit
- **R² < 0:** Model worse than using mean

**5. Adjusted R-squared**

**Formula:**
$$R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

Where:
- **n:** Number of observations
- **p:** Number of predictors

**Purpose:**
- **Penalizes** additional features that don't improve fit
- **Prevents overfitting** in model selection
- **More reliable** for comparing models with different numbers of features

**Example:**
```python
def adjusted_r2(r2, n, p):
    """Calculate adjusted R-squared"""
    return 1 - ((1 - r2) * (n - 1)) / (n - p - 1)

# Example with 5 samples, 2 features
n_samples = len(actual_prices)
n_features = 2
adj_r2 = adjusted_r2(r2, n_samples, n_features)

print(f"R²: {r2:.4f}")
print(f"Adjusted R²: {adj_r2:.4f}")
print(f"Penalty for {n_features} features: {r2 - adj_r2:.4f}")
```

**6. Mean Absolute Percentage Error (MAPE)**

**Formula:**
$$MAPE = \frac{100\%}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$

**Characteristics:**
- **Scale-independent:** Expressed as percentage
- **Interpretable:** Easy to communicate to business stakeholders
- **Problem:** Undefined when actual values are zero

**Example:**
```python
def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mape = mean_absolute_percentage_error(actual_prices, predicted_prices)
print(f"MAPE: {mape:.2f}%")

# Individual percentage errors
pct_errors = np.abs((actual_prices - predicted_prices) / actual_prices) * 100
print("Individual percentage errors:", pct_errors)
```

**MAPE Interpretation:**
- **MAPE < 10%:** Highly accurate
- **10% < MAPE < 20%:** Good accuracy
- **20% < MAPE < 50%:** Reasonable accuracy
- **MAPE > 50%:** Poor accuracy

**7. Comprehensive Evaluation Example**

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Generate sample dataset
np.random.seed(42)
X = np.random.randn(100, 3)  # 3 features
y = 2*X[:, 0] + 3*X[:, 1] - X[:, 2] + np.random.randn(100)*0.5

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Calculate all metrics
def evaluate_regression(y_true, y_pred, dataset_name=""):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    # Avoid division by zero in MAPE
    if np.any(y_true == 0):
        mape = "Undefined (zero values)"
    else:
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    print(f"\n{dataset_name} Performance Metrics:")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R²: {r2:.4f} ({r2*100:.2f}%)")
    if isinstance(mape, float):
        print(f"MAPE: {mape:.2f}%")
    else:
        print(f"MAPE: {mape}")
    
    return {'MSE': mse, 'RMSE': rmse, 'MAE': mae, 'R2': r2, 'MAPE': mape}

# Evaluate on both training and test sets
train_metrics = evaluate_regression(y_train, y_pred_train, "Training")
test_metrics = evaluate_regression(y_test, y_pred_test, "Test")

# Compare training vs test performance
print(f"\nOverfitting Check:")
print(f"Training R²: {train_metrics['R2']:.4f}")
print(f"Test R²: {test_metrics['R2']:.4f}")
print(f"R² Drop: {train_metrics['R2'] - test_metrics['R2']:.4f}")

if train_metrics['R2'] - test_metrics['R2'] > 0.1:
    print("Potential overfitting detected!")
else:
    print("Good generalization.")
```

**8. Residual Analysis**

**Residual Plots for Deeper Insights:**
```python
import matplotlib.pyplot as plt

# Calculate residuals
residuals = y_test - y_pred_test

# Create residual plots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residuals vs Predicted
axes[0, 0].scatter(y_pred_test, residuals, alpha=0.6)
axes[0, 0].axhline(y=0, color='red', linestyle='--')
axes[0, 0].set_xlabel('Predicted Values')
axes[0, 0].set_ylabel('Residuals')
axes[0, 0].set_title('Residuals vs Predicted')

# 2. Q-Q plot for normality
from scipy import stats
stats.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot (Normality Check)')

# 3. Histogram of residuals
axes[1, 0].hist(residuals, bins=15, alpha=0.7, edgecolor='black')
axes[1, 0].set_xlabel('Residuals')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Distribution of Residuals')

# 4. Residuals vs Order (time series check)
axes[1, 1].plot(residuals, 'o-', alpha=0.6)
axes[1, 1].axhline(y=0, color='red', linestyle='--')
axes[1, 1].set_xlabel('Observation Order')
axes[1, 1].set_ylabel('Residuals')
axes[1, 1].set_title('Residuals vs Order')

plt.tight_layout()
plt.show()

# Statistical tests
print("\nResidual Analysis:")
print(f"Mean of residuals: {np.mean(residuals):.6f} (should be ~0)")
print(f"Std of residuals: {np.std(residuals):.4f}")

# Shapiro-Wilk test for normality
stat, p_value = stats.shapiro(residuals)
print(f"Shapiro-Wilk test p-value: {p_value:.4f}")
if p_value > 0.05:
    print("Residuals appear normally distributed")
else:
    print("Residuals may not be normally distributed")
```

**9. Choosing the Right Metric**

**Decision Framework:**

| Use Case | Primary Metric | Reason |
|----------|----------------|---------|
| **General Purpose** | RMSE | Interpretable units, standard choice |
| **Outlier Robust** | MAE | Less sensitive to extreme values |
| **Model Comparison** | Adjusted R² | Accounts for model complexity |
| **Business Communication** | MAPE | Percentage terms easy to understand |
| **Optimization** | MSE | Smooth, differentiable for gradient descent |

**10. Cross-Validation for Robust Evaluation**

```python
from sklearn.model_selection import cross_val_score, cross_validate

# Multiple metrics with cross-validation
scoring = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error']

cv_results = cross_validate(model, X, y, cv=5, scoring=scoring)

print("Cross-Validation Results:")
print(f"R² (mean ± std): {cv_results['test_r2'].mean():.4f} ± {cv_results['test_r2'].std():.4f}")
print(f"MSE (mean ± std): {-cv_results['test_neg_mean_squared_error'].mean():.4f} ± {cv_results['test_neg_mean_squared_error'].std():.4f}")
print(f"MAE (mean ± std): {-cv_results['test_neg_mean_absolute_error'].mean():.4f} ± {cv_results['test_neg_mean_absolute_error'].std():.4f}")
```

Understanding these metrics helps you evaluate model performance comprehensively and choose the best model for your specific use case and business requirements.


