


1) Apply the K-Nearest Neighbor (KNN) algorithm to a given dataset of your choice (you may assume a small dataset). Demonstrate how the classification is performed for a new test sample when k = 5. Show all distance calculations, neighbour selection, and final class prediction.


----
K-Nearest Neighbor is a **supervised machine learning algorithm** used for both classification and regression tasks. It's a non-parametric, instance-based (lazy learning) algorithm.

### How KNN Works

1. **Choose K**: Select the number of neighbors (K value)
2. **Calculate Distance**: Compute distance between test point and all training points
3. **Find Neighbors**: Identify K nearest neighbors
4. **Vote/Average**:
    - **Classification**: Majority vote of K neighbors
    - **Regression**: Average of K neighbors' values

### Guidelines:

- **Small K** (e.g., K=1):
    
    - ✅ Captures fine patterns
    - ❌ Sensitive to noise/outliers
    - ❌ High variance, low bias
- **Large K**:
    
    - ✅ More robust to noise
    - ✅ Smoother decision boundaries
    - ❌ May miss local patterns
    - ❌ Low variance, high bias
- **Optimal K**: Use cross-validation
    
- **Rule of thumb**: K = √n (where n = number of samples)
    
- **Best practice**: Use odd K for binary classification to avoid ties

## Advantages ✅

1. **Simple to understand and implement**
2. **No training phase** (lazy learner)
3. **Non-parametric** (no assumptions about data distribution)
4. **Effective for multi-class problems**
5. **Naturally handles multi-class cases**
6. **Can be used for both classification and regression**

## Disadvantages ❌

1. **Computationally expensive** (O(n) prediction time)
2. **Memory intensive** (stores entire dataset)
3. **Slow for large datasets**
4. **Sensitive to feature scaling**
5. **Curse of dimensionality** (poor performance in high dimensions)
6. **Sensitive to irrelevant features**
7. **Requires careful selection of K**


---
---
---
**ANS:** 

# K-Nearest Neighbor (KNN) Algorithm Demonstration

## Dataset Selection

We'll use a small dataset of **fruit classification** based on two features:
- **Weight (grams)**
- **Sweetness (scale 1-10)**

### Training Dataset

| ID | Weight (g) | Sweetness | Class (Fruit) |
|----|-----------|-----------|---------------|
| 1  | 150       | 7         | Apple         |
| 2  | 170       | 8         | Apple         |
| 3  | 140       | 6         | Apple         |
| 4  | 30        | 9         | Grape         |
| 5  | 35        | 10        | Grape         |
| 6  | 32        | 8         | Grape         |
| 7  | 180       | 4         | Lemon         |
| 8  | 190       | 3         | Lemon         |
| 9  | 175       | 5         | Lemon         |
| 10 | 160       | 7         | Apple         |

### Test Sample

We want to classify a new fruit with:
- **Weight = 155 grams**
- **Sweetness = 7**

**Question:** What fruit is this? (Using k = 5)

---

## Step 1: Feature Normalization

To ensure both features contribute equally, we'll normalize the data using Min-Max scaling:

**Formula:** `X_normalized = (X - X_min) / (X_max - X_min)`

### Weight Normalization
- Min = 30, Max = 190
- Range = 160

### Sweetness Normalization
- Min = 3, Max = 10
- Range = 7

### Normalized Training Data

| ID | Weight (normalized) | Sweetness (normalized) | Class  |
|----|---------------------|------------------------|--------|
| 1  | (150-30)/160 = 0.75 | (7-3)/7 = 0.571       | Apple  |
| 2  | (170-30)/160 = 0.875| (8-3)/7 = 0.714       | Apple  |
| 3  | (140-30)/160 = 0.688| (6-3)/7 = 0.429       | Apple  |
| 4  | (30-30)/160 = 0.000 | (9-3)/7 = 0.857       | Grape  |
| 5  | (35-30)/160 = 0.031 | (10-3)/7 = 1.000      | Grape  |
| 6  | (32-30)/160 = 0.013 | (8-3)/7 = 0.714       | Grape  |
| 7  | (180-30)/160 = 0.938| (4-3)/7 = 0.143       | Lemon  |
| 8  | (190-30)/160 = 1.000| (3-3)/7 = 0.000       | Lemon  |
| 9  | (175-30)/160 = 0.906| (5-3)/7 = 0.286       | Lemon  |
| 10 | (160-30)/160 = 0.813| (7-3)/7 = 0.571       | Apple  |

### Normalized Test Sample
- **Weight:** (155-30)/160 = **0.781**
- **Sweetness:** (7-3)/7 = **0.571**

---

## Step 2: Distance Calculation

We'll use **Euclidean Distance** formula:

**d = √[(x₁ - x₂)² + (y₁ - y₂)²]**

### Calculating Distance from Test Sample to Each Training Point

**Test Point:** (0.781, 0.571)

#### Distance to Point 1 (Apple: 0.75, 0.571):
```
d₁ = √[(0.781 - 0.75)² + (0.571 - 0.571)²]
d₁ = √[(0.031)² + (0)²]
d₁ = √[0.000961 + 0]
d₁ = 0.031
```

#### Distance to Point 2 (Apple: 0.875, 0.714):
```
d₂ = √[(0.781 - 0.875)² + (0.571 - 0.714)²]
d₂ = √[(-0.094)² + (-0.143)²]
d₂ = √[0.008836 + 0.020449]
d₂ = √0.029285
d₂ = 0.171
```

#### Distance to Point 3 (Apple: 0.688, 0.429):
```
d₃ = √[(0.781 - 0.688)² + (0.571 - 0.429)²]
d₃ = √[(0.093)² + (0.142)²]
d₃ = √[0.008649 + 0.020164]
d₃ = √0.028813
d₃ = 0.170
```

#### Distance to Point 4 (Grape: 0.000, 0.857):
```
d₄ = √[(0.781 - 0.000)² + (0.571 - 0.857)²]
d₄ = √[(0.781)² + (-0.286)²]
d₄ = √[0.609961 + 0.081796]
d₄ = √0.691757
d₄ = 0.832
```

#### Distance to Point 5 (Grape: 0.031, 1.000):
```
d₅ = √[(0.781 - 0.031)² + (0.571 - 1.000)²]
d₅ = √[(0.750)² + (-0.429)²]
d₅ = √[0.5625 + 0.184041]
d₅ = √0.746541
d₅ = 0.864
```

#### Distance to Point 6 (Grape: 0.013, 0.714):
```
d₆ = √[(0.781 - 0.013)² + (0.571 - 0.714)²]
d₆ = √[(0.768)² + (-0.143)²]
d₆ = √[0.589824 + 0.020449]
d₆ = √0.610273
d₆ = 0.781
```

#### Distance to Point 7 (Lemon: 0.938, 0.143):
```
d₇ = √[(0.781 - 0.938)² + (0.571 - 0.143)²]
d₇ = √[(-0.157)² + (0.428)²]
d₇ = √[0.024649 + 0.183184]
d₇ = √0.207833
d₇ = 0.456
```

#### Distance to Point 8 (Lemon: 1.000, 0.000):
```
d₈ = √[(0.781 - 1.000)² + (0.571 - 0.000)²]
d₈ = √[(-0.219)² + (0.571)²]
d₈ = √[0.047961 + 0.326041]
d₈ = √0.374002
d₈ = 0.612
```

#### Distance to Point 9 (Lemon: 0.906, 0.286):
```
d₉ = √[(0.781 - 0.906)² + (0.571 - 0.286)²]
d₉ = √[(-0.125)² + (0.285)²]
d₉ = √[0.015625 + 0.081225]
d₉ = √0.09685
d₉ = 0.311
```

#### Distance to Point 10 (Apple: 0.813, 0.571):
```
d₁₀ = √[(0.781 - 0.813)² + (0.571 - 0.571)²]
d₁₀ = √[(-0.032)² + (0)²]
d₁₀ = √[0.001024 + 0]
d₁₀ = 0.032
```

---

## Step 3: Sort Distances

### All Distances Summary

| Rank | Point ID | Distance | Class  |
|------|----------|----------|--------|
| 1    | 1        | 0.031    | Apple  |
| 2    | 10       | 0.032    | Apple  |
| 3    | 3        | 0.170    | Apple  |
| 4    | 2        | 0.171    | Apple  |
| 5    | 9        | 0.311    | Lemon  |
| 6    | 7        | 0.456    | Lemon  |
| 7    | 8        | 0.612    | Lemon  |
| 8    | 6        | 0.781    | Grape  |
| 9    | 4        | 0.832    | Grape  |
| 10   | 5        | 0.864    | Grape  |

---

## Step 4: Select K Nearest Neighbors (k=5)

### The 5 Nearest Neighbors

| Rank | Point ID | Distance | Class  |
|------|----------|----------|--------|
| 1    | 1        | 0.031    | **Apple**  |
| 2    | 10       | 0.032    | **Apple**  |
| 3    | 3        | 0.170    | **Apple**  |
| 4    | 2        | 0.171    | **Apple**  |
| 5    | 9        | 0.311    | **Lemon**  |

---

## Step 5: Vote and Predict Class

### Class Count from 5 Nearest Neighbors

- **Apple:** 4 votes (Points 1, 10, 3, 2)
- **Lemon:** 1 vote (Point 9)
- **Grape:** 0 votes

### Majority Voting

**Winner: Apple (4 out of 5 votes = 80%)**

---

## Final Prediction

### ✅ Classification Result

**The test sample with Weight = 155g and Sweetness = 7 is classified as: APPLE**

### Confidence Level

- **Apple:** 80% (4/5 neighbors)
- **Lemon:** 20% (1/5 neighbors)
- **Grape:** 0% (0/5 neighbors)

---


2) ![[Pasted image 20251114121449.png]]

An email filtering system uses Naïve Bayes to classify messages as **Spam** or **Not Spam** based on the presence of certain words.

---

## Training Dataset

| Email | Contains 'Offer' | Contains 'Win' | Spam |
| ----- | ---------------- | -------------- | ---- |
| E1    | Yes              | Yes            | Yes  |
| E2    | No               | Yes            | Yes  |
| E3    | Yes              | No             | No   |
| E4    | No               | No             | No   |

---

## Step 1: Calculate Prior Probabilities

### Count Class Labels

- **Total emails:** 4
- **Spam emails:** 2 (E1, E2)
- **Not Spam emails:** 2 (E3, E4)

### Prior Probabilities


```
P(Spam) = Number of Spam emails / Total emails
P(Spam) = 2/4 = 0.5

P(Not Spam) = Number of Not Spam emails / Total emails
P(Not Spam) = 2/4 = 0.5
```

**Results:**

- **P(Spam) = 0.5 (50%)**
- **P(Not Spam) = 0.5 (50%)**

---

## i) Calculate Conditional Probabilities

### Analysis of Training Data by Class

#### SPAM Class (E1, E2):

| Email | Offer | Win |
| ----- | ----- | --- |
| E1    | Yes   | Yes |
| E2    | No    | Yes |

#### NOT SPAM Class (E3, E4):

|Email|Offer|Win|
|---|---|---|
|E3|Yes|No|
|E4|No|No|

---

### Calculating P(Offer | Spam)

```
Spam emails with 'Offer' = Yes: E1 (1 email)
Total Spam emails: 2

P(Offer = Yes | Spam) = 1/2 = 0.5
```

### Calculating P(Win | Spam)

```
Spam emails with 'Win' = Yes: E1, E2 (2 emails)
Total Spam emails: 2

P(Win = Yes | Spam) = 2/2 = 1.0
```

### Calculating P(Offer | Not Spam)

```
Not Spam emails with 'Offer' = Yes: E3 (1 email)
Total Not Spam emails: 2

P(Offer = Yes | Not Spam) = 1/2 = 0.5
```

### Calculating P(Win | Not Spam)

```
Not Spam emails with 'Win' = Yes: None (0 emails)
Total Not Spam emails: 2

P(Win = Yes | Not Spam) = 0/2 = 0.0
```

---

## ✅ Answer to Part (i): Conditional Probabilities

| Probability                    | Calculation | **Value** |
| ------------------------------ | ----------- | --------- |
| **P(Offer = Yes \| Spam)**     | 1/2         | **0.5**   |
| **P(Win = Yes \| Spam)**       | 2/2         | **1.0**   |
| **P(Offer = Yes \| Not Spam)** | 1/2         | **0.5**   |
| **P(Win = Yes \| Not Spam)**   | 0/2         | **0.0**   |

---

## ii) & iii) Classification of New Email

### Test Email Features:

- **Offer = Yes**
- **Win = Yes**

We need to calculate **P(Spam | Email)** and **P(Not Spam | Email)** using Bayes' Theorem.

---

### Bayes' Theorem Formula

```
P(Class | Features) = [P(Class) × P(Features | Class)] / P(Features)
```

For Naïve Bayes with **independence assumption**:

```
P(Class | Offer, Win) = [P(Class) × P(Offer | Class) × P(Win | Class)] / P(Offer, Win)
```

---

### Calculate P(Spam | Offer=Yes, Win=Yes)

Using Naïve Bayes formula:

```
P(Spam | Offer=Yes, Win=Yes) ∝ P(Spam) × P(Offer=Yes | Spam) × P(Win=Yes | Spam)

P(Spam | Offer=Yes, Win=Yes) ∝ 0.5 × 0.5 × 1.0

P(Spam | Offer=Yes, Win=Yes) ∝ 0.25
```

---

### Calculate P(Not Spam | Offer=Yes, Win=Yes)

```
P(Not Spam | Offer=Yes, Win=Yes) ∝ P(Not Spam) × P(Offer=Yes | Not Spam) × P(Win=Yes | Not Spam)

P(Not Spam | Offer=Yes, Win=Yes) ∝ 0.5 × 0.5 × 0.0

P(Not Spam | Offer=Yes, Win=Yes) ∝ 0.0
```

---

### Normalization

To get actual probabilities, we normalize:

```
Total = 0.25 + 0.0 = 0.25

P(Spam | Email) = 0.25 / 0.25 = 1.0

P(Not Spam | Email) = 0.0 / 0.25 = 0.0
```

---

## ✅ Answer to Parts (ii) & (iii): Posterior Probabilities

### Detailed Calculation Summary

|Class|Prior P(Class)|P(Offer=Yes\|Class)|P(Win=Yes\|Class)|Product|Normalized|
|---|---|---|---|---|---|
|**Spam**|0.5|0.5|1.0|0.5 × 0.5 × 1.0 = **0.25**|**1.0**|
|**Not Spam**|0.5|0.5|0.0|0.5 × 0.5 × 0.0 = **0.0**|**0.0**|

### Final Results:


```
P(Spam | Offer=Yes, Win=Yes) = 1.0 (100%)

P(Not Spam | Offer=Yes, Win=Yes) = 0.0 (0%)
```

---

## iv) Class Prediction and Independence Assumption

### 🎯 Class Prediction


**The email is classified as: SPAM**

**Reasoning:**

- P(Spam | Email) = 1.0 (100%)
- P(Not Spam | Email) = 0.0 (0%)

Since P(Spam | Email) > P(Not Spam | Email), the email is predicted to be **SPAM**.

The key factor here is that **P(Win=Yes | Not Spam) = 0.0**, meaning in our training data, no legitimate emails contained the word "Win". This makes it impossible for the new email to be classified as "Not Spam" when it contains "Win".

----
----
---


3) Analyze the differences among Gaussian, Multinomial, and Bernoulli Naïve Bayes classifiers. Using a real-world scenario (e.g., email classification, sensor data, or text classification), justify which Naïve Bayes variant is most suitable and why.
## Real-World Scenario: Email Spam Detection System

### Problem Statement
Build an intelligent email filtering system that automatically classifies incoming emails as **SPAM** or **HAM** (legitimate) to protect users from unwanted messages, phishing attempts, and malicious content.

### Why This Matters
- 📧 **85 billion+ spam emails** sent daily worldwide
- 💰 Costs businesses **$20.5 billion annually** in lost productivity
- 🎯 **45% of all emails** are spam
- 🔒 Critical for cybersecurity and user experience

---

## Dataset Description

### Real Email Dataset
We'll use a realistic email dataset with various characteristics:

```python
# Sample emails with realistic content
spam_emails = [
    "WINNER! You've won $5,000,000! Click here to claim your prize now!",
    "FREE VIAGRA! Best prices online! No prescription needed! Order now!",
    "Congratulations! You've been selected for a FREE iPhone 15! Claim within 24 hours!",
    "Make $10,000 per week working from home! No experience needed! Click here!",
    "URGENT: Your bank account has been compromised! Verify your details immediately!",
    "Hot singles in your area want to meet you! Click here now!",
    "Lose 30 pounds in 30 days! Revolutionary weight loss secret revealed!",
    "Your package is waiting! Click to track your delivery and claim your item!",
    "GET RICH QUICK! Invest in cryptocurrency now! 500% returns guaranteed!",
    "FREE LOTTERY TICKET! Win millions! Enter now! Limited time offer!"
]

legitimate_emails = [
    "Hi John, the quarterly sales meeting is scheduled for next Tuesday at 3 PM.",
    "Your Amazon order #12345 has been shipped and will arrive by Friday.",
    "Reminder: Your dentist appointment is tomorrow at 10:30 AM.",
    "Thanks for joining our team call today. Here are the meeting notes.",
    "Your credit card statement for March is now available online.",
    "Project update: The website redesign is 75% complete. Review attached.",
    "Mom's birthday dinner is on Saturday at 7 PM. Please confirm attendance.",
    "Your subscription renewal is due next month. No action needed now.",
    "The conference room is booked for your presentation on Thursday.",
    "Thank you for your purchase. Your receipt is attached to this email."
]
```

### Feature Characteristics

| Characteristic | Spam Emails | Legitimate Emails |
|---------------|-------------|-------------------|
| **Tone** | Urgent, promotional | Professional, informative |
| **Keywords** | WIN, FREE, CLICK, URGENT, $$ | Meeting, order, reminder, thanks |
| **Punctuation** | Multiple exclamation marks!!! | Standard punctuation |
| **Capitalization** | ALL CAPS frequently | Normal sentence case |
| **Content** | Money, prizes, offers | Appointments, orders, work |

---

## Analyzing All Three Naïve Bayes Variants

### 1. Gaussian Naïve Bayes ❌ NOT SUITABLE

#### Why It Doesn't Work for Email Classification

**Gaussian NB assumes continuous features with normal distribution.**

```python
# What Gaussian NB expects:
Feature 1 (e.g., Temperature): 72.5°F, 68.3°F, 75.1°F
Feature 2 (e.g., Humidity): 45.2%, 52.8%, 48.9%

# What we have in emails:
"FREE VIAGRA! Click now!" → How to convert to continuous values?
```

#### Problems with Email Text:

1. **Text is categorical, not continuous**
   - Words are discrete tokens, not measurements
   - "FREE" is not a number on a continuous scale

2. **No natural normal distribution**
   - Word frequencies don't follow Gaussian curves
   - Word presence/absence is binary or count-based

3. **Would require artificial conversion**
   ```python
   # Bad approach:
   feature_1 = len(email)  # Email length
   feature_2 = count_capitals(email)  # Number of capital letters
   feature_3 = count_exclamations(email)  # Exclamation marks
   
   # Problems:
   # - Loses actual word information
   # - No way to know which words appear
   # - Can't detect "FREE" or "VIAGRA" keywords
   ```

**Verdict: ❌ Completely inappropriate for email text classification**

---

### 2. Bernoulli Naïve Bayes ⚠️ PARTIALLY SUITABLE

#### How It Works for Email Classification

**Bernoulli NB uses binary features (present/absent).**

```python
# Email: "FREE prize! Click here!"
# Vocabulary: [free, prize, click, urgent, meeting, order]

Feature representation:
free: 1      (present)
prize: 1     (present)
click: 1     (present)
urgent: 0    (absent)
meeting: 0   (absent)
order: 0     (absent)
```

#### Advantages:

✅ **Explicitly models absence**
```python
P(spam | email) considers:
- Words that ARE present: "free", "prize"
- Words that ARE NOT present: "meeting", "order"

The absence of "meeting" is informative!
→ Legitimate emails often contain "meeting"
→ Not having it increases spam probability
```

✅ **Works with sparse data**
- Most emails contain only small fraction of total vocabulary
- Binary representation is memory-efficient

✅ **Good for short texts**
- Simple presence/absence sufficient for brief messages

#### Disadvantages:

❌ **Loses frequency information**
```python
Email 1: "FREE"           → free: 1
Email 2: "FREE FREE FREE" → free: 1

Both treated identically!
But Email 2 is more likely spam (repetitive keywords)
```

❌ **Can't distinguish intensity**
```python
"Click here" → click: 1
"Click here! Click now! CLICK!!!" → click: 1

Aggressive repetition is lost!
```

❌ **Less effective for longer documents**
- Email newsletters, long messages lose nuance

**Verdict: ⚠️ Works, but not optimal for email spam detection**

---

### 3. Multinomial Naïve Bayes ✅ BEST CHOICE

#### Why It's Perfect for Email Classification

**Multinomial NB uses word frequency counts.**

```python
# Email: "FREE prize! Click here! FREE offer! Click now!"
# Vocabulary: [free, prize, click, offer, here, now]

Feature representation (word counts):
free: 2    (appears twice)
prize: 1   (appears once)
click: 2   (appears twice)
offer: 1   (appears once)
here: 1    (appears once)
now: 1     (appears once)
```

#### Advantages:

✅ **Captures word frequency**
```python
Spam characteristic: Repetitive promotional words
"FREE FREE FREE" → free: 3 (strong spam signal)
"free" → free: 1 (weaker signal)

Multinomial NB captures this intensity!
```

✅ **Natural fit for text data**
```python
# Text naturally produces count data:
Email → Tokenization → Word counts

This is exactly what Multinomial NB expects!
```

✅ **Handles large vocabularies**
- Efficient with 10,000+ unique words
- Scales well to real-world email systems

✅ **Industry standard**
- Used by Gmail, Outlook, Yahoo Mail
- Proven effectiveness in production

✅ **Works with TF-IDF**
```python
# Can use sophisticated text features:
- Term Frequency (TF): How often word appears
- Inverse Document Frequency (IDF): How rare/important word is
- TF-IDF: Combined measure of importance

Multinomial NB works seamlessly with these!
```

**Verdict: ✅ Optimal choice for email spam classification**



----
----
----


4) A data scientist is working on three models for classifying medical test results: KNN (k=5) Gaussian Naïve Bayes SVM with RBF kernel Assume given is a small dataset with numeric features,
		a. Which algorithm handles non-linear boundaries best and why? 
		b. Which algorithm is most sensitive to irrelevant features? 
		c. Which algorithm performs better when data is small and has missing values? 
	## ANSWER

### a) Which algorithm handles non-linear boundaries best and why?

**Answer: SVM with RBF kernel**

**Explanation:**

SVM with RBF (Radial Basis Function) kernel is the best algorithm for handling non-linear boundaries among the three options.

**Reasons:**

1. **Kernel Trick:**
   - RBF kernel implicitly maps data to infinite-dimensional feature space
   - Can create complex, non-linear decision boundaries
   - Mathematical formula: K(x, x') = exp(-γ||x - x'||²)
   - This allows SVM to separate classes that are not linearly separable in original space

2. **Flexibility:**
   - RBF kernel can model any shape of decision boundary (circular, elliptical, irregular)
   - The gamma (γ) parameter controls the smoothness and complexity of the boundary
   - Can handle highly complex non-linear patterns in medical data

3. **Comparison with other algorithms:**
   
   **KNN (k=5):**
   - Can handle non-linear boundaries to some extent
   - Creates boundaries based on local neighborhoods
   - But boundaries are not smooth and depend heavily on k value
   - Less effective than SVM with RBF for complex patterns
   
   **Gaussian Naïve Bayes:**
   - Assumes features follow Gaussian distribution within each class
   - Creates simple, smooth boundaries (typically elliptical/quadratic)
   - Limited to relatively simple non-linear boundaries
   - Strong independence assumption restricts complexity

**Example in Medical Context:**
```
Medical test scenario: Classifying disease risk based on blood pressure 
and cholesterol levels

Disease boundary might be:
- Not a straight line (non-linear)
- Circular or elliptical region in feature space

SVM with RBF kernel can capture this complex boundary perfectly,
while Gaussian NB would approximate with elliptical shape and
KNN would create jagged boundaries.
```

**Conclusion:** SVM with RBF kernel handles non-linear boundaries best due to its ability to map data to higher dimensions and create arbitrarily complex decision boundaries through the kernel trick.

---

### b) Which algorithm is most sensitive to irrelevant features?

**Answer: KNN (k=5)**

**Explanation:**

KNN is the most sensitive to irrelevant features among the three algorithms.

**Reasons:**

1. **Distance-Based Calculation:**
   - KNN uses distance metrics (typically Euclidean distance) to find nearest neighbors
   - Distance formula: d = √[(x₁-y₁)² + (x₂-y₂)² + ... + (xₙ-yₙ)²]
   - Every feature contributes equally to distance calculation
   - Irrelevant features add noise to the distance measure

2. **Impact of Irrelevant Features:**
   ```
   Example with 2 relevant + 2 irrelevant features:
   
   Relevant features:
   - Blood glucose: Patient A = 120, Patient B = 125 (difference = 5)
   - Blood pressure: Patient A = 140, Patient B = 145 (difference = 5)
   
   Irrelevant features:
   - Shoe size: Patient A = 8, Patient B = 10 (difference = 2)
   - Height in cm: Patient A = 170, Patient B = 180 (difference = 10)
   
   Total distance = √(5² + 5² + 2² + 10²) = √154 ≈ 12.4
   
   Without irrelevant features: √(5² + 5²) = √50 ≈ 7.1
   
   The irrelevant features significantly distort the distance!
   Patients who are actually similar (close glucose and BP values)
   may be classified as distant due to irrelevant features.
   ```

3. **Curse of Dimensionality:**
   - As number of features increases, distances become meaningless
   - All points become equidistant in high dimensions
   - KNN performance degrades rapidly with irrelevant features

4. **Comparison with other algorithms:**
   
   **SVM with RBF kernel:**
   - Less sensitive to irrelevant features
   - Margin maximization focuses on discriminative features
   - Can ignore features that don't contribute to separation
   - Regularization parameter C helps control overfitting
   
   **Gaussian Naïve Bayes:**
   - Moderately sensitive to irrelevant features
   - Each feature contributes independently to classification
   - But probabilistic framework provides some robustness
   - Irrelevant features have low discriminative probability

**Real-World Impact in Medical Tests:**
```
Medical dataset with 10 features:
- 3 relevant: glucose, insulin, BMI
- 7 irrelevant: patient ID, appointment time, hospital code, etc.

KNN will treat all 10 features equally in distance calculation,
leading to poor classification because irrelevant features dominate
the distance metric and obscure true similarity patterns.
```

**Conclusion:** KNN is most sensitive to irrelevant features because it uses distance-based computation where all features contribute equally, causing irrelevant features to add noise and degrade classification accuracy.

---

### c) Which algorithm performs better when data is small and has missing values?

**Answer: Gaussian Naïve Bayes**

**Explanation:**

Gaussian Naïve Bayes performs best with small datasets and missing values.

**Reasons:**

**1. Performance with Small Datasets:**

a) **Low Parameter Complexity:**
   - For each class, only needs to estimate mean (μ) and variance (σ²) per feature
   - Parameters required = 2 × (number of features) × (number of classes)
   ```
   Example: 5 features, 2 classes
   Parameters = 2 × 5 × 2 = 20 parameters only
   
   Very few parameters → less data needed for reliable estimation
   ```

b) **Strong Independence Assumption:**
   - Assumes features are independent given the class
   - Simplifies model → reduces data requirements
   - Can learn from limited samples

c) **Probabilistic Framework:**
   - Works well even with limited training samples per class
   - Provides probability estimates, not just hard classifications
   - Naturally handles uncertainty in small datasets

**2. Handling Missing Values:**

a) **Feature Independence Property:**
   ```
   Classification formula:
   P(Class|x₁,x₂,x₃) ∝ P(Class) × P(x₁|Class) × P(x₂|Class) × P(x₃|Class)
   
   If x₂ is missing:
   P(Class|x₁,x₃) ∝ P(Class) × P(x₁|Class) × P(x₃|Class)
   
   Simply skip the missing feature!
   Other features still contribute to classification.
   ```

b) **Easy Missing Value Treatment:**
   - Can ignore missing features during prediction
   - Each feature contributes independently
   - No need for imputation (filling missing values)
   - No cascade effects from missing data

c) **Robust Probability Estimation:**
   - Missing values don't break the model
   - Can still make predictions with partial information

**3. Comparison with Other Algorithms:**

**KNN (k=5):**
- ❌ **Struggles with small datasets:**
  - Needs sufficient neighbors for reliable classification
  - With k=5, needs at least 5-10 samples per class minimum
  - Performance degrades rapidly with limited data
  
- ❌ **Poor with missing values:**
  - Distance calculation requires all features
  - Cannot compute distance with missing values
  - Must use imputation (mean/median filling) → adds bias
  ```
  Distance = √[(x₁-y₁)² + (x₂-y₂)² + ... + (xₙ-yₙ)²]
  
  If x₂ is missing, cannot calculate distance!
  Imputation required but unreliable with small data.
  ```

**SVM with RBF kernel:**
- ❌ **Needs sufficient data:**
  - Requires enough support vectors for reliable boundaries
  - Overfits easily on small datasets
  - Needs cross-validation for hyperparameter tuning (needs data)
  - RBF kernel adds complexity → needs more samples
  
- ❌ **Cannot handle missing values directly:**
  - Kernel computation requires complete feature vectors
  - K(x,x') = exp(-γ||x-x'||²) needs all dimensions
  - Must use imputation → unreliable with small data
  - No native mechanism for missing data


---
---
---

5) ![[Pasted image 20251114125217.png]]
**ANS**: 
**New Customer:** Income = 40, Spending = 15

**Training Data:**

- C1: (20, 5) → Low
- C2: (25, 7) → Low
- C3: (50, 20) → High
- C4: (55, 22) → High
- C5: (30, 10) → Low

---

## (a) Calculate Euclidean Distance

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#a-calculate-euclidean-distance)

**Formula:** d = √[(x₁-x₂)² + (y₁-y₂)²]

**New Customer = (40, 15)**

**Distance to C1 (20, 5):**

```
d₁ = √[(40-20)² + (15-5)²]
   = √[20² + 10²]
   = √[400 + 100]
   = √500
   = 22.36
```

**Distance to C2 (25, 7):**

```
d₂ = √[(40-25)² + (15-7)²]
   = √[15² + 8²]
   = √[225 + 64]
   = √289
   = 17.0
```

**Distance to C3 (50, 20):**

```
d₃ = √[(40-50)² + (15-20)²]
   = √[(-10)² + (-5)²]
   = √[100 + 25]
   = √125
   = 11.18
```

**Distance to C4 (55, 22):**

```
d₄ = √[(40-55)² + (15-22)²]
   = √[(-15)² + (-7)²]
   = √[225 + 49]
   = √274
   = 16.55
```

**Distance to C5 (30, 10):**

```
d₅ = √[(40-30)² + (15-10)²]
   = √[10² + 5²]
   = √[100 + 25]
   = √125
   = 11.18
```

---

## (b) Predict Class when K=3

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#b-predict-class-when-k3)

**Step 1: Sort distances (smallest to largest)**

|Rank|Customer|Distance|Class|
|---|---|---|---|
|1|C3|11.18|High|
|2|C5|11.18|Low|
|3|C4|16.55|High|
|4|C2|17.0|Low|
|5|C1|22.36|Low|

**Step 2: Select K=3 nearest neighbors**

- C3: High (distance = 11.18)
- C5: Low (distance = 11.18)
- C4: High (distance = 16.55)

**Step 3: Majority voting**

- High: 2 votes (C3, C4)
- Low: 1 vote (C5)

**Prediction: HIGH SPENDER** ✓

---

## (c) Manhattan Distance (5 Marks)

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#c-manhattan-distance-5-marks)

**Formula:** d = |x₁-x₂| + |y₁-y₂|

**Distance to C1:**

```
d₁ = |40-20| + |15-5|
   = 20 + 10
   = 30
```

**Distance to C2:**

```
d₂ = |40-25| + |15-7|
   = 15 + 8
   = 23
```

**Distance to C3:**

```
d₃ = |40-50| + |15-20|
   = 10 + 5
   = 15
```

**Distance to C4:**

```
d₄ = |40-55| + |15-22|
   = 15 + 7
   = 22
```

**Distance to C5:**

```
d₅ = |40-30| + |15-10|
   = 10 + 5
   = 15
```

**Sorted Manhattan Distances:**

|Rank|Customer|Distance|Class|
|---|---|---|---|
|1|C3|15|High|
|2|C5|15|Low|
|3|C4|22|High|
|4|C2|23|Low|
|5|C1|30|Low|

**K=3 Nearest Neighbors:**

- C3: High
- C5: Low
- C4: High

**Voting:** High = 2, Low = 1

**Prediction: HIGH SPENDER** ✓

**Comparison:**

- **Euclidean Distance:** HIGH SPENDER
- **Manhattan Distance:** HIGH SPENDER
- **Result:** SAME prediction with both metrics
- **Reason:** Both metrics identified C3, C5, C4 as nearest neighbors, so majority vote is identical.

---

## (d) Feature Scaling and K Selection

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#d-feature-scaling-and-k-selection)

### How Feature Scaling Affects KNN:

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#how-feature-scaling-affects-knn)

**1. Without Normalization:**

```
Income scale: 20-55 (range = 35)
Spending scale: 5-22 (range = 17)

Problem: Income dominates distance calculation because larger values
```

**Example:**

```
Distance = √[(40-30)² + (15-10)²]
         = √[100 + 25]
         
Income difference (10)² = 100 → dominates
Spending difference (5)² = 25 → less impact
```

**2. With Normalization (Min-Max):**

```
Normalized = (value - min)/(max - min)

Income: (40-20)/(55-20) = 20/35 = 0.57
Spending: (15-5)/(22-5) = 10/17 = 0.59

Now both features on scale [0,1] → equal contribution
```

**Impact:**

- Scaling ensures all features contribute equally
- Without scaling, features with larger ranges dominate
- Can change nearest neighbors and final prediction

### What Happens When K is Too Small or Too Large:

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#what-happens-when-k-is-too-small-or-too-large)

**K Too Small (K=1):**

- **Problem:** Overfitting
- **Effect:** Very sensitive to noise
- Decision boundary is irregular
- Example: If one outlier exists, it affects prediction
- High variance, low bias

**K Too Large (K = total training samples):**

- **Problem:** Underfitting
- **Effect:** Always predicts majority class
- Ignores local patterns
- Example: If K=5 (all training data), always predicts Low (3 Low vs 2 High)
- Low variance, high bias

**Optimal K:**

- Usually √n (where n = training samples)
- Here: √5 ≈ 2-3
- Use cross-validation to find best K
- Typically odd number to avoid ties

---

## (e) Real-World Application of KNN

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#e-real-world-application-of-knn)

**Application: Recommendation Systems (e-commerce like Amazon/Flipkart)**

**How it works:**

1. Find K customers most similar to current user (based on purchase history, ratings)
2. Recommend products that similar customers bought
3. Example: "Customers who bought this also bought..."

**Why KNN is preferred here:**

1. **No Training Phase:**
    
    - New products/users added instantly
    - No model retraining needed
    - Updates in real-time
2. **Simple and Interpretable:**
    
    - Easy to explain: "Customers like you bought this"
    - Transparent recommendations
3. **Handles Dynamic Data:**
    
    - User preferences change frequently
    - KNN adapts immediately with new data
    - No complex model updates
4. **Works with Multiple Features:**
    
    - Age, location, purchase history, browsing behavior
    - All contribute to similarity calculation
5. **Good for Cold Start:**
    
    - For new users, use demographic similarity
    - For new products, use product feature similarity

**Other Applications:**

- **Medical Diagnosis:** Find similar patient cases
- **Credit Scoring:** Find similar customers for loan approval
- **Image Recognition:** Find similar images

---

## Summary Table

[](https://github.com/copilot/c/770da0d0-eb7b-4304-88d3-8ef7bc41a129#summary-table)

|Metric|K=3 Neighbors|Prediction|
|---|---|---|
|**Euclidean**|C3(11.18), C5(11.18), C4(16.55)|HIGH|
|**Manhattan**|C3(15), C5(15), C4(22)|HIGH|

**Key Points to Remember:**

- Euclidean: √[(x₁-x₂)² + (y₁-y₂)²]
- Manhattan: |x₁-x₂| + |y₁-y₂|
- Always sort distances → pick K smallest → majority vote
- Normalize features for equal contribution
- K too small = overfitting, K too large = underfitting



6) ![[Pasted image 20251114125256.png]]
## Part 1: Concept of Decision Tree Classifier

### Definition:
A Decision Tree is a supervised learning algorithm that splits data into brancheBetter generalization
s based on feature values to make predictions. It resembles an inverted tree structure with:
- **Root Node:** Starting point (entire dataset)
- **Internal Nodes:** Decision points (feature tests)
- **Branches:** Outcomes of tests
- **Leaf Nodes:** Final predictions (class labels)

### How It Works:
1. Select best feature to split data (using Information Gain)
2. Create branches for each value of that feature
3. Repeat recursively for each branch
4. Stop when all instances in a node belong to same class

### Key Advantages:
- Easy to understand and interpret
- Handles both numerical and categorical data
- No need for data normalization
- Shows feature importance clearly

---

## Part 2: Construct Decision Tree Using Information Gain

### Given Dataset Summary:
- Total instances: 10
- Yes (Play Golf): 6
- No (Don't Play): 4
- Features: Outlook, Temperature, Humidity, Wind

---

### Step 1: Calculate Root Entropy

**Formula:** Entropy(S) = -∑ pᵢ log₂(pᵢ)

```
Total = 10 instances
Yes = 6, No = 4

Entropy(S) = -(6/10)log₂(6/10) - (4/10)log₂(4/10)
           = -(0.6)log₂(0.6) - (0.4)log₂(0.4)
           = -(0.6)(-0.737) - (0.4)(-1.322)
           = 0.442 + 0.529
           = 0.971
```

**Root Entropy = 0.971**

---

### Step 2: Calculate Information Gain for Each Feature

**Formula:** Gain(S,A) = Entropy(S) - ∑ (|Sᵥ|/|S|) × Entropy(Sᵥ)

---

#### (a) Information Gain for OUTLOOK

**Outlook values:** Sunny, Overcast, Rain

**Sunny (D1, D2, D8, D9):**
- Total: 4
- Yes: 1 (D9)
- No: 3 (D1, D2, D8)
```
Entropy(Sunny) = -(1/4)log₂(1/4) - (3/4)log₂(3/4)
                = -(0.25)(-2) - (0.75)(-0.415)
                = 0.5 + 0.311
                = 0.811
```

**Overcast (D3, D7):**
- Total: 2
- Yes: 2 (D3, D7)
- No: 0
```
Entropy(Overcast) = -(2/2)log₂(2/2) - 0
                   = -1 × 0
                   = 0
```

**Rain (D4, D5, D6, D10):**
- Total: 4
- Yes: 3 (D4, D5, D10)
- No: 1 (D6)
```
Entropy(Rain) = -(3/4)log₂(3/4) - (1/4)log₂(1/4)
               = -(0.75)(-0.415) - (0.25)(-2)
               = 0.311 + 0.5
               = 0.811
```

**Information Gain (Outlook):**
```
Gain(Outlook) = 0.971 - [(4/10)×0.811 + (2/10)×0 + (4/10)×0.811]
              = 0.971 - [0.324 + 0 + 0.324]
              = 0.971 - 0.648
              = 0.323
```

---

#### (b) Information Gain for HUMIDITY

**Humidity values:** High, Normal

**High (D1, D2, D3, D4, D8):**
- Total: 5
- Yes: 2 (D3, D4)
- No: 3 (D1, D2, D8)
```
Entropy(High) = -(2/5)log₂(2/5) - (3/5)log₂(3/5)
               = -(0.4)(-1.322) - (0.6)(-0.737)
               = 0.529 + 0.442
               = 0.971
```

**Normal (D5, D6, D7, D9, D10):**
- Total: 5
- Yes: 4 (D5, D7, D9, D10)
- No: 1 (D6)
```
Entropy(Normal) = -(4/5)log₂(4/5) - (1/5)log₂(1/5)
                 = -(0.8)(-0.322) - (0.2)(-2.322)
                 = 0.258 + 0.464
                 = 0.722
```

**Information Gain (Humidity):**
```
Gain(Humidity) = 0.971 - [(5/10)×0.971 + (5/10)×0.722]
                = 0.971 - [0.486 + 0.361]
                = 0.971 - 0.847
                = 0.124
```

---

#### (c) Information Gain for WIND

**Wind values:** Weak, Strong

**Weak (D1, D3, D4, D5, D8, D9, D10):**
- Total: 7
- Yes: 5 (D3, D4, D5, D9, D10)
- No: 2 (D1, D8)
```
Entropy(Weak) = -(5/7)log₂(5/7) - (2/7)log₂(2/7)
               = -(0.714)(-0.485) - (0.286)(-1.807)
               = 0.346 + 0.517
               = 0.863
```

**Strong (D2, D6, D7):**
- Total: 3
- Yes: 1 (D7)
- No: 2 (D2, D6)
```
Entropy(Strong) = -(1/3)log₂(1/3) - (2/3)log₂(2/3)
                 = -(0.333)(-1.585) - (0.667)(-0.585)
                 = 0.528 + 0.390
                 = 0.918
```

**Information Gain (Wind):**
```
Gain(Wind) = 0.971 - [(7/10)×0.863 + (3/10)×0.918]
            = 0.971 - [0.604 + 0.275]
            = 0.971 - 0.879
            = 0.092
```

---

### Step 3: Select Best Feature (Root Node)

**Information Gain Summary:**
| Feature | Information Gain |
|---------|-----------------|
| **Outlook** | **0.323** ✓ (Highest) |
| Humidity | 0.124 |
| Wind | 0.092 |

**Root Node = OUTLOOK** (highest Information Gain)

---

### Step 4: Build Tree Branches

#### Branch 1: Outlook = Overcast
- Instances: D3, D7
- All are "Yes"
- **Leaf Node: Yes** ✓ (Pure node)

#### Branch 2: Outlook = Sunny
- Instances: D1, D2, D8, D9
- Yes: 1, No: 3
- Need further split

**Check remaining features for Sunny subset:**

For **Humidity** on Sunny instances:
- High (D1, D2, D8): All "No"
- Normal (D9): "Yes"

**Split on Humidity:**
- If Humidity = High → **No**
- If Humidity = Normal → **Yes**

#### Branch 3: Outlook = Rain
- Instances: D4, D5, D6, D10
- Yes: 3, No: 1
- Need further split

**Check Wind for Rain instances:**
- Weak (D4, D5, D10): All "Yes"
- Strong (D6): "No"

**Split on Wind:**
- If Wind = Weak → **Yes**
- If Wind = Strong → **No**

---

### Final Decision Tree:

```
                    [Outlook]
                   /    |    \
                  /     |     \
              Sunny  Overcast  Rain
                /       |        \
               /        |         \
        [Humidity]     Yes     [Wind]
          /    \                /    \
         /      \              /      \
      High    Normal        Weak    Strong
       |         |           |         |
      No        Yes         Yes        No
```

**Tree in Text Format:**
```
Root: Outlook
├─ Overcast → Yes
├─ Sunny
│  └─ Humidity
│     ├─ High → No
│     └─ Normal → Yes
└─ Rain
   └─ Wind
      ├─ Weak → Yes
      └─ Strong → No
```

---

## Part 3: How Decision Trees Handle Overfitting

### What is Overfitting?
Overfitting occurs when a decision tree becomes too complex, memorizing training data including noise, resulting in poor performance on new data.

**Signs of Overfitting:**
- Very deep tree with many branches
- Each leaf has very few instances (sometimes just 1)
- 100% accuracy on training data but poor on test data
- Tree captures noise instead of patterns

---

### Techniques to Handle Overfitting:

#### 1. **Pre-Pruning (Early Stopping)**

Stop growing the tree early based on criteria:

**a) Maximum Depth:**
- Limit tree depth (e.g., max depth = 5)
- Prevents overly complex trees

**b) Minimum Samples Split:**
- Don't split if node has fewer than N instances
- Example: If node has < 5 samples, make it leaf

**c) Minimum Samples per Leaf:**
- Each leaf must have at least N instances
- Prevents leaves with 1-2 samples

**d) Minimum Information Gain:**
- Only split if Information Gain > threshold
- Example: Only split if gain > 0.01
- Stops splitting when improvement is minimal

**Example:**
```
Without pre-pruning: Tree depth = 8, 100% training accuracy
With pre-pruning (max_depth=3): Tree depth = 3, 95% training, 
                                 92% test accuracy (better generalization)
```

---

#### 2. **Post-Pruning (Tree Pruning)**

Grow full tree first, then remove unnecessary branches:

**Process:**
1. Build complete tree (may overfit)
2. Evaluate each subtree's performance
3. Replace subtree with leaf if it improves validation accuracy
4. Continue until no improvement

**Cost-Complexity Pruning:**
```
For each node, calculate:
Cost = Error Rate + α × (Number of leaves)

Where α = complexity parameter

If replacing subtree with leaf reduces cost → prune it
```

**Example:**
```
Original tree: 20 leaves, 98% training accuracy, 85% test accuracy
After pruning: 8 leaves, 95% training accuracy, 90% test accuracy
Result: Better generalization, simpler model
```

---

#### 3. **Setting Minimum Information Gain Threshold**

Only split if Information Gain is significant:

```
If Gain(feature) < threshold (e.g., 0.01):
    Don't split, make it a leaf node
```

**Benefit:** Prevents splits that barely improve classification

---

#### 4. **Cross-Validation**

Use k-fold cross-validation to:
- Find optimal tree parameters (depth, min_samples)
- Validate tree performance on unseen data
- Select best model that generalizes well

---

#### 5. **Ensemble Methods**

**Random Forest:**
- Build multiple decision trees
- Each tree trained on random subset of data
- Average predictions (reduces overfitting of individual trees)

**Advantages:**
- Reduces variance
- More robust than single tree
- Better generalization

---



7) Differentiate Bagging and Boosting techniques in the machine learning model. Discuss briefly the Adaboost algorithm with suitable example
   

---

## Part 1: Differentiate Bagging and Boosting

### Bagging (Bootstrap Aggregating)

Bagging is an ensemble technique that trains multiple models **independently in parallel** on different random subsets of data (with replacement) and combines their predictions through **equal-weight voting or averaging**. Its primary goal is to **reduce variance** and prevent overfitting. Each model is trained on a bootstrap sample (random sampling with replacement from original data), and all models contribute equally to the final prediction. The most popular example is **Random Forest**, which builds multiple decision trees on different data samples and averages their predictions.

**Example:** Imagine predicting house prices using 100 decision trees. Bagging creates 100 different datasets by randomly sampling the original data (some houses appear multiple times, some don't). Each tree trains independently on its dataset. Final prediction = average of all 100 predictions. If Tree 1 predicts ₹50L, Tree 2 predicts ₹48L, and Tree 3 predicts ₹52L, the final prediction is ₹50L (average). This reduces the impact of any single overfitted tree.

---

### Boosting

Boosting is an ensemble technique that trains models **sequentially**, where each new model focuses on **correcting the mistakes** of previous models. Its primary goal is to **reduce bias** by converting weak learners into a strong classifier. Unlike bagging, training data is **reweighted** after each iteration—misclassified samples get higher weights so the next model focuses more on difficult cases. Models are also given **different importance weights** based on their accuracy (better models have more influence). Popular algorithms include **AdaBoost** and **Gradient Boosting**.

**Example:** Using the same house price prediction, Boosting works differently. Model 1 trains on original data and makes some errors (predicts ₹30L for a ₹50L house). Model 2 then focuses specifically on the houses Model 1 got wrong by increasing their importance. Model 3 corrects remaining errors from Models 1 and 2. Final prediction = weighted combination where more accurate models have higher say: Final = 0.8×Model1 + 0.5×Model2 + 0.9×Model3. Model 3 (most accurate, weight 0.9) influences the result most.

---

### Key Differences

| **Aspect** | **Bagging** | **Boosting** |
|------------|-------------|--------------|
| **Training** | Parallel (independent) | Sequential (dependent) |
| **Data Sampling** | Random with replacement (bootstrap) | Weighted based on previous errors |
| **Model Weights** | Equal for all models | Different (accurate models weighted more) |
| **Goal** | Reduce variance (overfitting) | Reduce bias (underfitting) |
| **Focus** | All samples treated equally | Focuses on difficult/misclassified samples |
| **Speed** | Faster (parallel training) | Slower (sequential training) |
| **Example** | Random Forest | AdaBoost, XGBoost |
| **Final Prediction** | Simple majority vote/average | Weighted vote based on model accuracy |

---

### Practical Example: Medical Diagnosis

**Scenario:** Classifying patients as "Disease" or "Healthy" from 1000 patient records.

**Bagging Approach (Random Forest):**
- Create 10 bootstrap samples (each with 1000 randomly selected patients, some repeated)
- Train 10 decision trees independently
- Patient X tested: 7 trees predict "Disease", 3 predict "Healthy"
- Final: **Disease** (majority vote: 7 > 3)
- **Benefit:** If one tree overfits, others balance it out

**Boosting Approach (AdaBoost):**
- Model 1 trains on original data, misclassifies 50 difficult patients
- Those 50 patients get 5× higher weight for Model 2
- Model 2 focuses on those 50, correctly classifies 40, still misses 10
- Those 10 get even higher weight for Model 3
- Final prediction = 0.7×Model1 + 0.5×Model2 + 0.9×Model3
- **Benefit:** Learns difficult cases that single model would miss

---

## Part 2: AdaBoost Algorithm

### What is AdaBoost?

**AdaBoost (Adaptive Boosting)** is a boosting algorithm that combines multiple weak learners (typically decision stumps - trees with depth 1) into a strong classifier by:
1. Training models sequentially
2. Increasing weights of misclassified samples
3. Giving more importance to better models

---

### AdaBoost Algorithm Steps

**Input:**
- Training data: (x₁,y₁), (x₂,y₂), ..., (xₙ,yₙ)
- Number of weak learners: T

**Process:**

**Step 1: Initialize Weights**
```
Set equal weight for all samples:
wᵢ = 1/N for i = 1 to N

Where N = total training samples
```

**Step 2: For each iteration t = 1 to T:**

**2a) Train Weak Learner**
```
Train model hₜ on weighted training data
(Samples with higher weights are more important)
```

**2b) Calculate Error**
```
εₜ = Σ wᵢ × I(hₜ(xᵢ) ≠ yᵢ)

Where:
- εₜ = weighted error of model t
- I() = indicator function (1 if wrong, 0 if correct)
- Sum only over misclassified samples
```

**2c) Calculate Model Weight (Importance)**
```
αₜ = ½ ln((1 - εₜ)/εₜ)

Where:
- αₜ = weight/importance of model t
- Lower error → Higher αₜ (model gets more say)
- εₜ < 0.5 required (better than random)
```

**2d) Update Sample Weights**
```
For each sample i:
wᵢ = wᵢ × exp(αₜ × I(hₜ(xᵢ) ≠ yᵢ))

Then normalize:
wᵢ = wᵢ / Σ wⱼ

Effect:
- Correct predictions: Weight stays same or decreases
- Wrong predictions: Weight increases exponentially
```

**Step 3: Final Prediction**
```
H(x) = sign(Σ αₜ × hₜ(x))

Weighted majority vote:
- Each model votes with weight αₜ
- Sum all weighted votes
- Sign determines final class
```

---

### AdaBoost Example

**Problem:** Classify students as Pass/Fail based on Study Hours and Sleep Hours

**Training Data:**

| Student | Study Hours | Sleep Hours | Result |
|---------|-------------|-------------|--------|
| S1 | 2 | 8 | Fail |
| S2 | 3 | 7 | Fail |
| S3 | 5 | 6 | Pass |
| S4 | 6 | 5 | Pass |
| S5 | 7 | 4 | Pass |

**Notation:** Pass = +1, Fail = -1

---

#### **Iteration 1:**

**Step 1.1: Initialize Weights**
```
All samples get equal weight:
w₁ = [0.2, 0.2, 0.2, 0.2, 0.2]
(Each = 1/5 = 0.2)
```

**Step 1.2: Train Weak Learner h₁**
```
Decision Stump: "If Study Hours > 4 → Pass, else Fail"

Predictions:
S1: Study=2 → Predict Fail → Actual Fail ✓
S2: Study=3 → Predict Fail → Actual Pass ✗ (WRONG)
S3: Study=5 → Predict Pass → Actual Pass ✓
S4: Study=6 → Predict Pass → Actual Pass ✓
S5: Study=7 → Predict Pass → Actual Pass ✓
```

**Step 1.3: Calculate Error**
```
ε₁ = Σ (weights of misclassified)
   = 0.2 (only S2 wrong)
```

**Step 1.4: Calculate Model Weight**
```
α₁ = ½ ln((1 - 0.2)/0.2)
   = ½ ln(4)
   = ½ × 1.386
   = 0.693

Model 1 importance = 0.693
```

**Step 1.5: Update Sample Weights**
```
For correctly classified (S1, S3, S4, S5):
w = 0.2 × exp(-0.693) = 0.2 × 0.5 = 0.1

For misclassified (S2):
w = 0.2 × exp(0.693) = 0.2 × 2 = 0.4

Before normalization: [0.1, 0.4, 0.1, 0.1, 0.1]
Sum = 0.8

After normalization:
w₂ = [0.125, 0.5, 0.125, 0.125, 0.125]

S2 now has weight 0.5 (50% of total) - very important!
```

---

#### **Iteration 2:**

**Step 2.1: Train Weak Learner h₂**
```
Now training with weights: [0.125, 0.5, 0.125, 0.125, 0.125]
S2 is 4× more important than others

New Decision Stump: "If Sleep Hours < 7 → Pass, else Fail"

Predictions:
S1: Sleep=8 → Predict Fail → Actual Fail ✓
S2: Sleep=7 → Predict Fail → Actual Fail ✓ (Now correct!)
S3: Sleep=6 → Predict Pass → Actual Pass ✓
S4: Sleep=5 → Predict Pass → Actual Pass ✓
S5: Sleep=4 → Predict Pass → Actual Pass ✓
```

**Step 2.2: Calculate Error**
```
Assume S1 is misclassified:
ε₂ = 0.125
```

**Step 2.3: Calculate Model Weight**
```
α₂ = ½ ln((1 - 0.125)/0.125)
   = ½ ln(7)
   = 0.973

Model 2 importance = 0.973 (higher than Model 1)
```

**Step 2.4: Update Weights**
```
Continue process...
w₃ = [higher for S1, lower for others]
```

---

#### **Iteration 3:**

**Train h₃** focusing on remaining difficult samples, calculate α₃

---

### **Final AdaBoost Classifier**

After 3 iterations:

**Model 1:** h₁(x) = "Study > 4?" with weight α₁ = 0.693
**Model 2:** h₂(x) = "Sleep < 7?" with weight α₂ = 0.973
**Model 3:** h₃(x) = Combined rule with weight α₃ = 0.856

**Final Prediction Formula:**
```
H(x) = sign(0.693×h₁(x) + 0.973×h₂(x) + 0.856×h₃(x))
```

**Example Prediction for New Student:**
```
New: Study Hours = 4, Sleep Hours = 6

h₁(x): Study > 4? No → Predict Fail (-1)
h₂(x): Sleep < 7? Yes → Predict Pass (+1)
h₃(x): Combined rule → Predict Pass (+1)

Weighted Sum:
= 0.693×(-1) + 0.973×(+1) + 0.856×(+1)
= -0.693 + 0.973 + 0.856
= 1.136

sign(1.136) = +1 → Predict PASS ✓

Models 2 and 3 (higher accuracy, higher weights) override Model 1
```

---

### Why AdaBoost Works

**1. Adaptive Learning:**
- Each model focuses on samples previous models got wrong
- Weights increase for difficult samples
- No sample is ignored

**2. Weak to Strong:**
```
Individual stump accuracy: ~60%
Combined AdaBoost accuracy: ~95%
Multiple weak learners → one strong classifier
```

**3. Model Quality Matters:**
- Better models (lower error) get higher weight α
- Poor models contribute less to final decision
- Automatic quality control

---

### Advantages & Disadvantages

**Advantages:**
✅ Simple to implement
✅ No complex parameter tuning
✅ Works with any weak learner
✅ Reduces bias effectively
✅ Performs feature selection automatically

**Disadvantages:**
❌ Sensitive to noisy data and outliers
❌ Slower than bagging (sequential)
❌ Can overfit with too many iterations
❌ Requires error < 0.5 for each weak learner

---

## Summary

### Bagging vs Boosting Quick Recap

| Technique | Training | Goal | Example |
|-----------|----------|------|---------|
| **Bagging** | Parallel | Reduce variance | Random Forest |
| **Boosting** | Sequential | Reduce bias | AdaBoost |

### AdaBoost Quick Recap

**Key Formulas:**
```
αₜ = ½ ln((1 - εₜ)/εₜ)        ← Model weight
wᵢ = wᵢ × exp(αₜ × error)     ← Sample weight update
H(x) = sign(Σ αₜ×hₜ(x))       ← Final prediction
```

**Process:**
1. Start with equal weights (1/N)
2. Train weak learner on weighted data
3. Calculate error and model weight
4. Increase weights of misclassified samples
5. Repeat T times
6. Combine with weighted voting

---
---
---


8) ![[Pasted image 20251114131112.png]]

## (a) Calculate Gini Index for Parent Node (Root)

### Gini Index Formula:
```
Gini(D) = 1 - Σ(pᵢ)²

Where:
pᵢ = probability of class i
```

### Calculation:

**Step 1: Calculate class probabilities**
```
Total samples = 7
Buy = Yes: 4 samples → p(Yes) = 4/7 = 0.571
Buy = No: 3 samples → p(No) = 3/7 = 0.429
```

**Step 2: Apply Gini formula**
```
Gini(Root) = 1 - [p(Yes)² + p(No)²]
           = 1 - [(4/7)² + (3/7)²]
           = 1 - [(0.571)² + (0.429)²]
           = 1 - [0.326 + 0.184]
           = 1 - 0.510
           = 0.490
```

**Answer: Gini Index of Parent Node = 0.490**

---

## (b) Compute Gini Index for Each Possible Split

### Split 1: Based on AGE GROUP

**Age Group has 3 values:** Young, Middle, Senior

**Visual Tree Structure:**
```
                    ROOT (7 samples)
                    Yes:4, No:3
                    Gini = 0.490
                         |
                   Split by AGE
                         |
         ┌───────────────┼───────────────┐
         │               │               │
      Young           Middle          Senior
    (C1, C2)        (C3, C4)      (C5, C6, C7)
    Yes:0, No:2     Yes:2, No:0   Yes:2, No:1
    Gini = 0        Gini = 0      Gini = 0.445
```

---

#### **Branch 1: Age = Young (C1, C2)**

**Samples:** 2
**Yes:** 0
**No:** 2

```
p(Yes) = 0/2 = 0
p(No) = 2/2 = 1

Gini(Young) = 1 - [0² + 1²]
            = 1 - [0 + 1]
            = 1 - 1
            = 0
```

**Gini(Young) = 0** (Pure node - all No)

---

#### **Branch 2: Age = Middle (C3, C4)**

**Samples:** 2
**Yes:** 2 (C3, C4)
**No:** 0

```
p(Yes) = 2/2 = 1
p(No) = 0/2 = 0

Gini(Middle) = 1 - [1² + 0²]
             = 1 - [1 + 0]
             = 1 - 1
             = 0
```

**Gini(Middle) = 0** (Pure node - all Yes)

---

#### **Branch 3: Age = Senior (C5, C6, C7)**

**Samples:** 3
**Yes:** 2 (C5, C6)
**No:** 1 (C7)

```
p(Yes) = 2/3 = 0.667
p(No) = 1/3 = 0.333

Gini(Senior) = 1 - [(2/3)² + (1/3)²]
             = 1 - [(0.667)² + (0.333)²]
             = 1 - [0.444 + 0.111]
             = 1 - 0.555
             = 0.445
```

**Gini(Senior) = 0.445**

---

#### **Weighted Gini Index for Age Group Split:**

```
Gini(Age Group) = Σ (nᵢ/n) × Gini(i)

Where:
nᵢ = samples in branch i
n = total samples

Gini(Age Group) = (2/7)×Gini(Young) + (2/7)×Gini(Middle) + (3/7)×Gini(Senior)
                = (2/7)×0 + (2/7)×0 + (3/7)×0.445
                = 0 + 0 + 0.191
                = 0.191
```

**Answer: Gini(Age Group) = 0.191**

**Visual Calculation:**
```
Weighted Average:

Young (2/7):   0.286 × 0.000 = 0.000
               ▓▓▓▓▓▓▓▓▓▓▓▓
Middle (2/7):  0.286 × 0.000 = 0.000
               ▓▓▓▓▓▓▓▓▓▓▓▓
Senior (3/7):  0.429 × 0.445 = 0.191
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
               ─────────────────────
               Total Gini = 0.191
```

---

### Split 2: Based on INCOME LEVEL

**Income Level has 3 values:** Low, Medium, High

**Visual Tree Structure:**
```
                    ROOT (7 samples)
                    Yes:4, No:3
                    Gini = 0.490
                         |
                   Split by INCOME
                         |
         ┌───────────────┼───────────────┐
         │               │               │
       Low            Medium           High
  (C1, C3, C7)       (C2, C5)       (C4, C6)
  Yes:1, No:2        Yes:1, No:1    Yes:2, No:0
  Gini = 0.445       Gini = 0.500   Gini = 0
```

---


---

#### **Branch 1: Income = Low (C1, C3, C7)**

**Samples:** 3
**Yes:** 1 (C3)
**No:** 2 (C1, C7)

```
p(Yes) = 1/3 = 0.333
p(No) = 2/3 = 0.667

Gini(Low) = 1 - [(1/3)² + (2/3)²]
          = 1 - [(0.333)² + (0.667)²]
          = 1 - [0.111 + 0.444]
          = 1 - 0.555
          = 0.445
```

**Gini(Low) = 0.445**

---

#### **Branch 2: Income = Medium (C2, C5)**

**Samples:** 2
**Yes:** 1 (C5)
**No:** 1 (C2)

```
p(Yes) = 1/2 = 0.5
p(No) = 1/2 = 0.5

Gini(Medium) = 1 - [(1/2)² + (1/2)²]
             = 1 - [0.25 + 0.25]
             = 1 - 0.5
             = 0.5
```

**Gini(Medium) = 0.5**

---

#### **Branch 3: Income = High (C4, C6)**

**Samples:** 2
**Yes:** 2 (C4, C6)
**No:** 0

```
p(Yes) = 2/2 = 1
p(No) = 0/2 = 0

Gini(High) = 1 - [1² + 0²]
           = 1 - [1 + 0]
           = 1 - 1
           = 0
```

**Gini(High) = 0** (Pure node - all Yes)

---

#### **Weighted Gini Index for Income Level Split:**

```
Gini(Income Level) = (3/7)×Gini(Low) + (2/7)×Gini(Medium) + (2/7)×Gini(High)
                   = (3/7)×0.445 + (2/7)×0.5 + (2/7)×0
                   = 0.191 + 0.143 + 0
                   = 0.334
```

**Answer: Gini(Income Level) = 0.334**

**Visual Calculation:**
```
Weighted Average:

Low (3/7):     0.429 × 0.445 = 0.191
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
Medium (2/7):  0.286 × 0.500 = 0.143
               ▓▓▓▓▓▓▓▓▓▓▓▓
High (2/7):    0.286 × 0.000 = 0.000
               ▓▓▓▓▓▓▓▓▓▓▓▓
               ─────────────────────
               Total Gini = 0.334
```

---


## (c) Determine Best Attribute to Split

### Comparison of Gini Index Values:

| Attribute | Weighted Gini Index |
|-----------|---------------------|
| **Age Group** | **0.191** ✓ (Lower) |
| **Income Level** | 0.334 |

### Decision Rule:
**Choose the attribute with the LOWEST Gini Index** (maximum purity/minimum impurity)

### Gini Gain (Optional Calculation):
```
Gini Gain = Gini(Parent) - Gini(Split)

For Age Group:
Gini Gain = 0.490 - 0.191 = 0.299 ✓ (Higher gain)

For Income Level:
Gini Gain = 0.490 - 0.334 = 0.156
```

**Answer: Best Attribute to Split = AGE GROUP**

**Reason:** Age Group has lower Gini Index (0.191 < 0.334), meaning it creates purer child nodes and better separates the classes.

---

### Resulting CART Tree (First Split):

```
                    [Root]
                   Age Group?
                  /    |     \
                 /     |      \
            Young   Middle   Senior
              |       |         |
             No      Yes     [Further split]
          (C1,C2)  (C3,C4)   (C5,C6,C7)
          Pure     Pure      Not pure
                             (Gini=0.445)
```

**Explanation:**
- Young branch: All customers don't buy → Leaf node: **No**
- Middle branch: All customers buy → Leaf node: **Yes**
- Senior branch: Mixed (2 Yes, 1 No) → Needs further splitting

---

## (d) What Happens if Both Attributes Had Same Gini Value?

### Scenario:
If Gini(Age Group) = Gini(Income Level) = 0.191 (same value)

### Solution Approaches:

**1. Arbitrary Selection:**
- Choose any one attribute randomly
- Both provide equal information gain
- Decision is equivalent in terms of impurity reduction

**2. Tie-Breaking Criteria:**

**a) Choose attribute that appears first alphabetically:**
- Between "Age Group" and "Income Level"
- "Age Group" comes first → Select Age Group

**b) Choose attribute with fewer categories:**
- If one has fewer values, prefer it for simpler tree
- Example: If Age (3 values) vs Income (5 values) → Choose Age

**c) Domain knowledge:**
- Use business logic/expert opinion
- Example: In retail, Age might be more important → Choose Age

**d) Look at variance/distribution:**
- Choose attribute with more balanced split
- Avoid attributes that create highly imbalanced branches

**3. Try Both (Best Practice):**
- Build trees with both attributes as root
- Compare overall tree performance on validation data
- Choose the one with better accuracy

**Example:**
```
If both give Gini = 0.191:

Option 1: Root = Age Group → Tree1 (depth, accuracy)
Option 2: Root = Income → Tree2 (depth, accuracy)

Select tree with better test accuracy or simpler structure
```

**Answer:** If both attributes have the same Gini value, we can:
1. Select arbitrarily (both are equally good)
2. Use tie-breaking rules (alphabetical, fewer categories, domain knowledge)
3. Build both trees and compare performance
4. Choose based on interpretability and business requirements

---

## (e) Two Advantages of CART over ID3 or C4.5

### Advantage 1: Handles Both Classification and Regression

**CART:**
- Can handle **classification** problems (categorical target: Yes/No, Cat/Dog)
- Can handle **regression** problems (continuous target: price, temperature)
- Uses Gini Index for classification
- Uses variance reduction for regression

**ID3/C4.5:**
- Only handles **classification** problems
- Cannot predict continuous values
- Limited to categorical outputs

**Example:**
```
Problem 1: Predict if customer buys (Yes/No)
- CART: ✓ Can handle
- ID3/C4.5: ✓ Can handle

Problem 2: Predict customer's purchase amount (₹500, ₹1200, etc.)
- CART: ✓ Can handle (regression)
- ID3/C4.5: ✗ Cannot handle directly
```

---

### Advantage 2: Handles Missing Values Better

**CART:**
- Has **surrogate splits** mechanism
- Finds alternative splits that achieve similar results
- If primary attribute is missing, uses surrogate attribute
- More robust to incomplete data

**ID3/C4.5:**
- C4.5 handles missing values but less sophisticatedly
- ID3 struggles significantly with missing data
- May need preprocessing (imputation)

**Example:**
```
Dataset with missing Age values:

CART approach:
- Primary split: Age Group
- Surrogate split: Income Level (gives similar classification)
- If Age missing, use Income instead
- Seamless handling

ID3 approach:
- Must either:
  a) Remove samples with missing Age
  b) Impute Age values (fill with mean/mode)
  c) Create "Missing" category
- Less elegant solution
```

---
---
---


9) Describe the random forest algorithm with example and justify the hyper parameter importance?

## 1. What is Random Forest?

**Random Forest** is an ensemble learning method that builds multiple decision trees on random subsets of data and features, then combines their predictions through majority voting (classification) or averaging (regression).

**Key Components:**
1. **Bagging (Bootstrap Aggregating):** Creates random training subsets
2. **Random Feature Selection:** Uses random features at each split
3. **Voting/Averaging:** Combines predictions from all trees

---

## 2. How Random Forest Works

### Algorithm Steps:

**Step 1: Bootstrap Sampling**
- From dataset with N samples, create T bootstrap samples
- Each sample: randomly select N samples with replacement

**Step 2: Build Decision Trees**
- For each bootstrap sample, build a decision tree
- At each node: randomly select m features (m < total features)
- Split on best feature among these m features only
- Grow tree fully (no pruning)

**Step 3: Make Predictions**
- Pass new data through all T trees
- **Classification:** Majority vote wins
- **Regression:** Average all predictions

---

## 3. Example: Student Pass/Fail Prediction

### Training Data:

| Student | Study Hrs | Sleep Hrs | Attendance% | Pass |
|---------|-----------|-----------|-------------|------|
| S1 | 2 | 8 | 60 | No |
| S2 | 3 | 7 | 65 | No |
| S3 | 5 | 6 | 80 | Yes |
| S4 | 6 | 5 | 85 | Yes |
| S5 | 7 | 4 | 90 | Yes |

**Total Features:** 3 (Study Hrs, Sleep Hrs, Attendance%)
**Target:** Pass (Yes/No)
**max_features = 2** (randomly select 2 out of 3 features at each split)

---

### Building Random Forest (3 Trees):

#### **Tree 1: First Decision Tree**

**Bootstrap Sample 1:** [S1, S2, S3, S3, S5] (S3 appears twice, S4 is missing)

| Student | Study Hrs | Sleep Hrs | Attendance% | Pass |
|---------|-----------|-----------|-------------|------|
| S1 | 2 | 8 | 60 | No |
| S2 | 3 | 7 | 65 | No |
| S3 | 5 | 6 | 80 | Yes |
| S3 | 5 | 6 | 80 | Yes |
| S5 | 7 | 4 | 90 | Yes |

**Random Features Selected at Root:** [Study Hrs, Attendance%]
- Sleep Hrs is NOT considered (randomly excluded)

**Finding Best Split:**
```
Test Attendance% > 75:
  Left (≤75):  S1(No), S2(No) → Pure No
  Right (>75): S3(Yes), S3(Yes), S5(Yes) → Pure Yes
  Perfect split! ✓

Test Study Hrs > 4:
  Left (≤4):   S1(No), S2(No) → Pure No
  Right (>4):  S3(Yes), S3(Yes), S5(Yes) → Pure Yes
  Also good, but Attendance% chosen
```

**Tree 1 Structure:**
```
                ┌─────────────────────┐
                │   ROOT (n=5)        │
                │   Yes:3, No:2       │
                │   Features: Study,  │
                │   Attendance%       │
                └──────────┬──────────┘
                           │
                   Attendance% > 75?
                           │
            ┌──────────────┴──────────────┐
            │                             │
            NO                           YES
            │                             │
    ┌───────▼────────┐         ┌─────────▼────────┐
    │ LEFT (n=2)     │         │ RIGHT (n=3)      │
    │ Attendance≤75  │         │ Attendance>75    │
    │ S1(No), S2(No) │         │ S3(Yes), S3(Yes) │
    │                │         │ S5(Yes)          │
    │ Pure Node ✓    │         │ Pure Node ✓      │
    └────────┬───────┘         └─────────┬────────┘
             │                           │
             ▼                           ▼
        Predict: NO                 Predict: YES
```

**Decision Rule:** 
```
IF Attendance% > 75:
    Predict YES
ELSE:
    Predict NO
```

---

#### **Tree 2: Second Decision Tree**

**Bootstrap Sample 2:** [S1, S3, S4, S4, S5] (S4 appears twice, S2 is missing)

| Student | Study Hrs | Sleep Hrs | Attendance% | Pass |
|---------|-----------|-----------|-------------|------|
| S1 | 2 | 8 | 60 | No |
| S3 | 5 | 6 | 80 | Yes |
| S4 | 6 | 5 | 85 | Yes |
| S4 | 6 | 5 | 85 | Yes |
| S5 | 7 | 4 | 90 | Yes |

**Random Features Selected at Root:** [Study Hrs, Sleep Hrs]
- Attendance% is NOT considered (randomly excluded)

**Finding Best Split:**
```
Test Study Hrs > 4:
  Left (≤4):   S1(No) → Pure No
  Right (>4):  S3(Yes), S4(Yes), S4(Yes), S5(Yes) → Pure Yes
  Perfect split! ✓

Test Sleep Hrs < 7:
  Left (<7):   S3(Yes), S4(Yes), S4(Yes), S5(Yes) → Pure Yes
  Right (≥7):  S1(No) → Pure No
  Also good, but Study Hrs chosen
```

**Tree 2 Structure:**
```
                ┌─────────────────────┐
                │   ROOT (n=5)        │
                │   Yes:4, No:1       │
                │   Features: Study,  │
                │   Sleep Hrs         │
                └──────────┬──────────┘
                           │
                    Study Hrs > 4?
                           │
            ┌──────────────┴──────────────┐
            │                             │
            NO                           YES
            │                             │
    ┌───────▼────────┐         ┌─────────▼────────┐
    │ LEFT (n=1)     │         │ RIGHT (n=4)      │
    │ Study≤4        │         │ Study>4          │
    │ S1(No)         │         │ S3(Yes), S4(Yes) │
    │                │         │ S4(Yes), S5(Yes) │
    │ Pure Node ✓    │         │ Pure Node ✓      │
    └────────┬───────┘         └─────────┬────────┘
             │                           │
             ▼                           ▼
        Predict: NO                 Predict: YES
```

**Decision Rule:**
```
IF Study Hrs > 4:
    Predict YES
ELSE:
    Predict NO
```

---

#### **Tree 3: Third Decision Tree**

**Bootstrap Sample 3:** [S2, S3, S4, S5, S5] (S5 appears twice, S1 is missing)

| Student | Study Hrs | Sleep Hrs | Attendance% | Pass |
|---------|-----------|-----------|-------------|------|
| S2 | 3 | 7 | 65 | No |
| S3 | 5 | 6 | 80 | Yes |
| S4 | 6 | 5 | 85 | Yes |
| S5 | 7 | 4 | 90 | Yes |
| S5 | 7 | 4 | 90 | Yes |

**Random Features Selected at Root:** [Sleep Hrs, Attendance%]
- Study Hrs is NOT considered (randomly excluded)

**Finding Best Split:**
```
Test Sleep Hrs < 7:
  Left (<7):   S3(Yes), S4(Yes), S5(Yes), S5(Yes) → Pure Yes
  Right (≥7):  S2(No) → Pure No
  Perfect split! ✓

Test Attendance% > 70:
  Left (≤70):  S2(No) → Pure No
  Right (>70): S3(Yes), S4(Yes), S5(Yes), S5(Yes) → Pure Yes
  Also good, but Sleep Hrs chosen
```

**Tree 3 Structure:**
```
                ┌─────────────────────┐
                │   ROOT (n=5)        │
                │   Yes:4, No:1       │
                │   Features: Sleep,  │
                │   Attendance%       │
                └──────────┬──────────┘
                           │
                    Sleep Hrs < 7?
                           │
            ┌──────────────┴──────────────┐
            │                             │
           YES                            NO
            │                             │
    ┌───────▼────────┐         ┌─────────▼────────┐
    │ LEFT (n=4)     │         │ RIGHT (n=1)      │
    │ Sleep<7        │         │ Sleep≥7          │
    │ S3(Yes),S4(Yes)│         │ S2(No)           │
    │ S5(Yes),S5(Yes)│         │                  │
    │ Pure Node ✓    │         │ Pure Node ✓      │
    └────────┬───────┘         └─────────┬────────┘
             │                           │
             ▼                           ▼
        Predict: YES                Predict: NO
```

**Decision Rule:**
```
IF Sleep Hrs < 7:
    Predict YES
ELSE:
    Predict NO
```

---

### Key Observations About Tree Diversity:

**Why Trees Are Different:**

1. **Different Training Data:**
   - Tree 1 has S3 twice, missing S4
   - Tree 2 has S4 twice, missing S2
   - Tree 3 has S5 twice, missing S1

2. **Different Random Features:**
   - Tree 1 considers: Study Hrs + Attendance%
   - Tree 2 considers: Study Hrs + Sleep Hrs
   - Tree 3 considers: Sleep Hrs + Attendance%

3. **Different Split Rules:**
   - Tree 1 splits on: Attendance% > 75
   - Tree 2 splits on: Study Hrs > 4
   - Tree 3 splits on: Sleep Hrs < 7

**Result:** Three diverse trees that look at data differently!

---

### Making Prediction with Complete Random Forest:

**New Student:** Study Hrs=6, Sleep Hrs=6, Attendance=85%

```
┌─────────────────────────────────────────────────────────┐
│                    NEW STUDENT                          │
│  Study Hrs: 6  |  Sleep Hrs: 6  |  Attendance: 85%     │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
    ┌───────┐         ┌───────┐       ┌───────┐
    │Tree 1 │         │Tree 2 │       │Tree 3 │
    └───┬───┘         └───┬───┘       └───┬───┘
        │                 │                 │
        ▼                 ▼                 ▼
```

**Tree 1 Evaluation:**
```
Attendance(85%) > 75?
YES → Go to right branch
Prediction: YES ✓
```

**Tree 2 Evaluation:**
```
Study Hrs(6) > 4?
YES → Go to right branch
Prediction: YES ✓
```

**Tree 3 Evaluation:**
```
Sleep Hrs(6) < 7?
YES → Go to left branch
Prediction: YES ✓
```

**Final Voting:**
```
┌──────────────────────────┐
│   VOTING PROCESS         │
├──────────────────────────┤
│ Tree 1 votes: YES (1)    │
│ Tree 2 votes: YES (1)    │
│ Tree 3 votes: YES (1)    │
├──────────────────────────┤
│ Total:                   │
│   YES: 3 votes (100%)    │
│   NO:  0 votes (0%)      │
└──────────────────────────┘

Final Prediction: YES (Pass) ✓
Confidence: 3/3 = 100%
```

---

### Visual Summary of Random Forest Process:

```
ORIGINAL DATA (5 students)
        │
        ├─── Bootstrap Sample 1 ──► Tree 1 ──► Vote: YES
        │    [S1,S2,S3,S3,S5]      (Attendance)
        │
        ├─── Bootstrap Sample 2 ──► Tree 2 ──► Vote: YES
        │    [S1,S3,S4,S4,S5]      (Study Hrs)
        │
        └─── Bootstrap Sample 3 ──► Tree 3 ──► Vote: YES
             [S2,S3,S4,S5,S5]      (Sleep Hrs)
                                           │
                                           ▼
                                    MAJORITY VOTE
                                           │
                                           ▼
                                   Final: YES (3/3)
```

---

## 4. Hyperparameter Importance

### **1. n_estimators (Number of Trees)**

**Definition:** Total number of decision trees in the forest

**Default:** 100

**Importance:**
- **Low value (10-50):** Underfitting, low accuracy, high variance
- **Optimal (100-300):** Good balance of accuracy and speed
- **High value (500+):** Minimal accuracy gain, high computational cost

**Justification:**
- More trees → Better accuracy (up to saturation point)
- More trees → More computational time
- Sweet spot: 100-300 trees

**Example:**
```
n_estimators=50:  Accuracy=88%, Time=5s
n_estimators=100: Accuracy=93%, Time=10s ✓
n_estimators=500: Accuracy=94%, Time=50s (diminishing returns)
```

---

### **2. max_features (Features per Split)**

**Definition:** Number of features to consider when looking for best split

**Options:** 
- **'sqrt':** √(total features) — default for classification
- **'log2':** log₂(total features)
- **Integer or float:** Specific number or fraction

**Importance:**
- **Too few:** High diversity but weak individual trees
- **Optimal ('sqrt'):** Good balance of diversity and performance
- **Too many (all features):** Low diversity, trees become similar

**Justification:**
- Controls tree diversity
- Lower value → More randomness → Less tree correlation
- Higher value → Less randomness → More correlated trees
- 'sqrt' provides optimal trade-off

**Example (16 features):**
```
max_features='sqrt' (4): Accuracy=93%, Diversity=High ✓
max_features='log2' (4): Accuracy=92%, Diversity=High
max_features=8:          Accuracy=90%, Diversity=Medium
max_features=16 (all):   Accuracy=88%, Diversity=Low (overfitting)
```

**In Our Example:**
- Total features = 3
- max_features = 2 (we used 2 out of 3 at each split)
- This created diversity: each tree used different feature combinations

---

### **3. max_depth (Maximum Tree Depth)**

**Definition:** Maximum depth of each decision tree

**Default:** None (unlimited)

**Importance:**
- **Shallow (5-10):** Fast, less overfitting, may underfit
- **None (unlimited):** Captures complex patterns, Random Forest prevents overfitting
- **Too deep:** Slow training and prediction

**Justification:**
- Controls tree complexity
- None is usually fine because Random Forest averages out overfitting
- Limit depth only if computational resources are constrained

**Example:**
```
max_depth=5:    Accuracy=85%, Time=3s (underfitting)
max_depth=10:   Accuracy=91%, Time=8s
max_depth=None: Accuracy=93%, Time=15s ✓
```

**In Our Example:**
- All three trees had depth = 1 (only root split)
- This was sufficient because data was simple
- In real scenarios, trees grow deeper

---

### **4. min_samples_split**

**Definition:** Minimum samples required to split an internal node

**Default:** 2

**Importance:**
- **Low (2):** Allows very detailed splits, may overfit
- **High (20-50):** Creates simpler trees, better generalization
- Controls tree granularity

**Justification:**
- Prevents overfitting by stopping splits on small nodes
- Higher value → Simpler tree → Better generalization
- Lower value → Complex tree → May capture noise

**Example:**
```
min_samples_split=2:  Training=99%, Test=90% (overfitting)
min_samples_split=10: Training=95%, Test=93% ✓
min_samples_split=50: Training=88%, Test=87% (underfitting)
```

---

### **5. min_samples_leaf**

**Definition:** Minimum samples required in a leaf node

**Default:** 1

**Importance:**
- **Value=1:** Can have single-sample leaves (may overfit)
- **Higher (5-20):** Smoother decision boundaries, better generalization
- Directly controls overfitting

**Justification:**
- Forces leaves to have minimum samples
- Prevents memorization of individual training samples
- Smooths the decision boundaries

---

### **6. bootstrap**

**Definition:** Whether to use bootstrap sampling

**Default:** True

**Importance:**
- **True:** Each tree sees different data → High diversity → Core of Random Forest
- **False:** All trees see same data → Low diversity → Not recommended

**Justification:**
- Bootstrap sampling is fundamental to Random Forest
- Creates diversity among trees
- Should always be True for proper Random Forest

**In Our Example:**
- bootstrap=True created different samples for each tree
- Tree 1, 2, 3 had different training data
- This diversity led to robust predictions

---

### **7. n_jobs**

**Definition:** Number of CPU cores to use for parallel processing

**Default:** 1

**Importance:**
- **1:** Sequential processing (slow)
- **-1:** Uses all available cores (fast)
- **No impact on accuracy, only speed**

**Justification:**
- Trees are independent, can be built in parallel
- Dramatically reduces training time
- Always set to -1 for faster training

**Example (100 trees, 4 cores):**
```
n_jobs=1:  Time=100s
n_jobs=-1: Time=28s ✓ (3.6× faster)
```

---

## Summary

### **Random Forest in 3 Points:**
1. Builds multiple trees on random data samples (bootstrap)
2. Uses random feature subsets at each split
3. Combines predictions through voting/averaging

### **Top 3 Hyperparameters:**
1. **n_estimators:** Controls number of trees (more = better, 100-300)
2. **max_features:** Controls diversity ('sqrt' optimal for classification)
3. **max_depth:** Controls complexity (None usually best)

### **Key Justifications:**
- **n_estimators:** Directly impacts accuracy through ensemble size
- **max_features:** Balances tree diversity and individual tree performance
- **Depth/samples:** Control overfitting vs underfitting trade-off
- **n_jobs:** No accuracy impact, only speeds up training

---
