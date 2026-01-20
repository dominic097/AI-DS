# 21CSC529T - Inferential Statistics - CYCLE TEST I
## Set-A - ANSWER SHEET

---

## Question 1

### Part a) Store Sales Performance Comparison

**Given Data:**
- Store 1: 120, 130, 150, 140, 160 (in thousands of dollars)
- Store 2: 115, 125, 135, 128, 140 (in thousands of dollars)

---

#### i. Calculate mean, median, and mode for both stores (5 marks)

**STORE 1:**

**Mean:**
**Formula:** μ = Σx / N

**Step-by-step:**
```
μ = (120 + 130 + 150 + 140 + 160) / 5
μ = 700 / 5
μ = 140
```
**Mean for Store 1 = $140,000**

**Median:**
**Formula:** For odd n, Median = Middle value

**Step-by-step:**
1. Arrange in ascending order: 120, 130, 140, 150, 160
2. n = 5 (odd)
3. Median = 3rd term = 140

**Median for Store 1 = $140,000**

**Mode:**
- Checking for repeated values: All values are unique
**Mode for Store 1 = No mode**

---

**STORE 2:**

**Mean:**
**Formula:** μ = Σx / N

**Step-by-step:**
```
μ = (115 + 125 + 135 + 128 + 140) / 5
μ = 643 / 5
μ = 128.6
```
**Mean for Store 2 = $128,600**

**Median:**
**Step-by-step:**
1. Arrange in ascending order: 115, 125, 128, 135, 140
2. n = 5 (odd)
3. Median = 3rd term = 128

**Median for Store 2 = $128,000**

**Mode:**
- All values are unique
**Mode for Store 2 = No mode**

---

**Summary Table:**

| Measure | Store 1 | Store 2 |
|---------|---------|---------|
| Mean | $140,000 | $128,600 |
| Median | $140,000 | $128,000 |
| Mode | No mode | No mode |

**Interpretation:**
- Store 1 has higher average sales ($140,000) compared to Store 2 ($128,600)
- Store 1's mean equals its median, suggesting a symmetric distribution
- Store 2's mean is slightly higher than its median, suggesting slight positive skew

---

#### ii. Compute range, variance, and standard deviation (7 marks)

**STORE 1:**

**Range:**
**Formula:** Range = Maximum - Minimum

**Step-by-step:**
```
Range = 160 - 120
Range = 40
```
**Range for Store 1 = $40,000**

**Variance (σ²):**
**Formula (Population):** σ² = Σ(x - μ)² / N

**Step-by-step:**

| Sales (x) | (x - μ) | (x - μ)² |
|-----------|---------|----------|
| 120 | -20 | 400 |
| 130 | -10 | 100 |
| 150 | 10 | 100 |
| 140 | 0 | 0 |
| 160 | 20 | 400 |
| **Sum** | **0** | **1000** |

```
σ² = 1000 / 5
σ² = 200
```
**Variance for Store 1 = 200 (in squared thousands)** = **$200,000,000**

**Standard Deviation (σ):**
**Formula:** σ = √σ²

**Step-by-step:**
```
σ = √200
σ = 14.14
```
**Standard Deviation for Store 1 = $14,140** (or 14.14 thousands)

**Coefficient of Variation (CV):**
**Formula:** CV = (σ / μ) × 100

```
CV = (14.14 / 140) × 100
CV = 10.1%
```
**CV for Store 1 = 10.1%**

---

**STORE 2:**

**Range:**
```
Range = 140 - 115
Range = 25
```
**Range for Store 2 = $25,000**

**Variance:**

| Sales (x) | (x - μ) | (x - μ)² |
|-----------|---------|----------|
| 115 | -13.6 | 184.96 |
| 125 | -3.6 | 12.96 |
| 135 | 6.4 | 40.96 |
| 128 | -0.6 | 0.36 |
| 140 | 11.4 | 129.96 |
| **Sum** | **0** | **369.20** |

```
σ² = 369.20 / 5
σ² = 73.84
```
**Variance for Store 2 = 73.84** (in squared thousands)

**Standard Deviation:**
```
σ = √73.84
σ = 8.59
```
**Standard Deviation for Store 2 = $8,590** (or 8.59 thousands)

**Coefficient of Variation:**
```
CV = (8.59 / 128.6) × 100
CV = 6.68%
```
**CV for Store 2 = 6.68%**

---

**Summary Table:**

| Measure | Store 1 | Store 2 |
|---------|---------|---------|
| Range | $40,000 | $25,000 |
| Variance (σ²) | 200 | 73.84 |
| Standard Deviation (σ) | $14,140 | $8,590 |
| Coefficient of Variation | 10.1% | 6.68% |

---

#### iii. Which store shows higher consistency? (3 marks)

**Answer: Store 2 shows higher consistency in sales.**

**Statistical Justification:**

**1. Coefficient of Variation (CV) Comparison:**
- Store 1: CV = 10.1%
- Store 2: CV = 6.68%

**The Coefficient of Variation is the most appropriate measure** for comparing consistency between datasets, as it provides a standardized measure of dispersion relative to the mean.

**2. Analysis:**
- **Store 2 has a lower CV (6.68%)**, which indicates **less relative variability**
- A lower CV means the sales figures are more consistent and clustered around the mean
- Store 2's sales representatives show more uniform performance

**3. Supporting Evidence:**
- **Range:** Store 2 has a smaller range ($25,000 vs $40,000), indicating less spread
- **Standard Deviation:** Store 2 has lower SD ($8,590 vs $14,140), showing less absolute variation
- **Relative Dispersion:** When adjusted for mean differences, Store 2 is more consistent

**4. Practical Interpretation:**
- Store 2's sales are more predictable and reliable
- Store 1 has more variability, suggesting some sales representatives significantly outperform or underperform others
- From a management perspective, Store 2's consistency suggests more stable business operations

**Conclusion:**
**Store 2 demonstrates higher consistency** with 6.68% relative variation compared to Store 1's 10.1%, making it approximately **34% more consistent** in sales performance [(10.1 - 6.68)/10.1 × 100 = 33.9%].

---

### Part b) Differences between Correlation and Covariance (5 marks)

**Answer:**

#### **1. COVARIANCE**

**Definition:**
Covariance measures the **direction** of the linear relationship between two variables and indicates how two variables change together.

**Formula:**
- **Population:** Cov(X,Y) = Σ[(Xi - μx)(Yi - μy)] / N
- **Sample:** Cov(X,Y) = Σ[(Xi - x̄)(Yi - ȳ)] / (n-1)

**Characteristics:**
- **Range:** -∞ to +∞ (unbounded)
- **Unit:** Product of the units of X and Y
- **Interpretation:**
  - Positive covariance: Variables move in same direction
  - Negative covariance: Variables move in opposite directions
  - Zero covariance: No linear relationship

**Example:**
If X = Height (cm) and Y = Weight (kg), then Cov(X,Y) might be +150 kg·cm

---

#### **2. CORRELATION**

**Definition:**
Correlation is a **standardized measure** of the linear relationship between two variables. It measures both the **strength and direction** of the relationship.

**Formula (Pearson's Correlation Coefficient):**
```
r = Cov(X,Y) / (σx × σy)
```
Where σx and σy are standard deviations of X and Y

**Characteristics:**
- **Range:** -1 to +1 (bounded and dimensionless)
- **Unit:** Unitless (dimensionless)
- **Interpretation:**
  - r = +1: Perfect positive correlation
  - r = -1: Perfect negative correlation
  - r = 0: No linear correlation
  - |r| > 0.7: Strong correlation
  - 0.3 < |r| < 0.7: Moderate correlation
  - |r| < 0.3: Weak correlation

**Example:**
For the same height-weight data, r = 0.85 (strong positive correlation)

---

#### **3. KEY DIFFERENCES**

| Aspect | Covariance | Correlation |
|--------|-----------|-------------|
| **Definition** | Measures direction only | Measures direction AND strength |
| **Range** | -∞ to +∞ | -1 to +1 |
| **Units** | Has units (product of variable units) | Dimensionless |
| **Standardization** | Not standardized | Standardized |
| **Comparability** | Cannot compare across different datasets | Can compare across datasets |
| **Interpretation** | Difficult to interpret magnitude | Easy to interpret (0 to 1 scale) |
| **Scale dependency** | Depends on scale of variables | Independent of scale |

---

#### **4. RELATIONSHIP BETWEEN THEM**

**Mathematical Relationship:**
```
Correlation (r) = Covariance / (SD of X × SD of Y)
```

Correlation is essentially **normalized covariance**.

---

#### **5. IMPORTANCE AND APPLICATIONS**

**Importance of Covariance:**
1. **Portfolio Theory:** Used in finance to measure how assets move together
2. **Multivariate Analysis:** Foundation for principal component analysis (PCA)
3. **Statistical Modeling:** Used in covariance matrices for multivariate distributions
4. **Formula Component:** Building block for calculating correlation

**Importance of Correlation:**
1. **Predictive Modeling:** Determines which variables to include in regression models
2. **Feature Selection:** Identifies redundant features in machine learning
3. **Hypothesis Testing:** Tests for relationships between variables
4. **Quality Control:** Monitors relationships between process variables
5. **Standardized Comparison:** Allows comparison of relationships across different studies
6. **Causality Investigation:** First step in establishing potential causal relationships

**Practical Example:**

Suppose we analyze the relationship between:
- **Study Hours (X)** and **Exam Scores (Y)**

**Covariance might be:**
- Cov(X,Y) = 15 hour·points

**Problem:** Is 15 large or small? Hard to tell!

**Correlation would be:**
- r = 0.85

**Interpretation:** This is a strong positive relationship (easy to understand!)

---

#### **6. WHEN TO USE WHICH**

**Use Covariance when:**
- You need the actual magnitude for calculations (e.g., portfolio variance)
- Working with variance-covariance matrices
- The scale of measurement is consistent

**Use Correlation when:**
- You want to understand the strength of relationship
- Comparing relationships across different variable pairs
- Communicating results to non-technical audiences
- Performing hypothesis tests about relationships

**Conclusion:**
While covariance provides the **direction** of a relationship, correlation provides both **direction and strength** in an easily interpretable, standardized format. In practice, **correlation is preferred for interpretation**, while **covariance is essential for certain calculations** in multivariate statistics and portfolio theory.

---

## Question 2

### Part a) Sports Activities Probability (5 marks)

**Given Data:**

|  | Football (F) | Basketball (B) | Tennis (T) | Total |
|---|---|---|---|---|
| Adult | 50 | 30 | 20 | 100 |
| Teen | 40 | 50 | 30 | 120 |
| Child | 50 | 40 | 60 | 150 |
| **Total** | **140** | **120** | **110** | **370** |

---

#### i. Probability that a randomly chosen participant is enrolled in Basketball (B)

**Formula:** P(B) = Number in Basketball / Total participants

**Step-by-step:**
```
Total participants = 50 + 30 + 20 + 40 + 50 + 30 + 50 + 40 + 60
Total = 370

Basketball participants = 30 + 50 + 40 = 120

P(B) = 120 / 370
P(B) = 12/37
P(B) = 0.324
```

**Answer: P(Basketball) = 0.324 or 32.4% or 12/37**

---

#### ii. Probability that a randomly chosen participant is a Teen

**Formula:** P(Teen) = Number of teens / Total participants

**Step-by-step:**
```
Teens = 40 + 50 + 30 = 120

P(Teen) = 120 / 370
P(Teen) = 12/37
P(Teen) = 0.324
```

**Answer: P(Teen) = 0.324 or 32.4% or 12/37**

---

#### iii. Probability that a participant is an Adult enrolled in Football (F)

**Formula:** P(Adult AND Football) = Number of adults in football / Total

**Step-by-step:**
```
Adults in Football = 50

P(Adult AND Football) = 50 / 370
P(Adult AND Football) = 5/37
P(Adult AND Football) = 0.135
```

**Answer: P(Adult AND Football) = 0.135 or 13.5% or 5/37**

---

#### iv. Probability that a participant is a Child enrolled in Tennis (T)

**Formula:** P(Child AND Tennis) = Number of children in tennis / Total

**Step-by-step:**
```
Children in Tennis = 60

P(Child AND Tennis) = 60 / 370
P(Child AND Tennis) = 6/37
P(Child AND Tennis) = 0.162
```

**Answer: P(Child AND Tennis) = 0.162 or 16.2% or 6/37**

---

#### v. Probability that a participant is an Adult given they are enrolled in Football (F)

**Formula:** P(Adult | Football) = P(Adult AND Football) / P(Football)

This is **CONDITIONAL PROBABILITY**

**Step-by-step:**
```
Adults in Football = 50
Total in Football = 140

P(Adult | Football) = 50 / 140
P(Adult | Football) = 5/14
P(Adult | Football) = 0.357
```

**Answer: P(Adult | Football) = 0.357 or 35.7% or 5/14**

---

**Summary Table:**

| Question | Formula | Probability | Percentage |
|----------|---------|-------------|------------|
| i. P(Basketball) | 120/370 | 12/37 | 32.4% |
| ii. P(Teen) | 120/370 | 12/37 | 32.4% |
| iii. P(Adult AND Football) | 50/370 | 5/37 | 13.5% |
| iv. P(Child AND Tennis) | 60/370 | 6/37 | 16.2% |
| v. P(Adult \| Football) | 50/140 | 5/14 | 35.7% |

---

### Part b) Sports Equipment Defective Items - Bayes' Theorem (10 marks)

**Given Information:**

**Prior Probabilities (Defect Rates):**
- P(Defective | Football) = 0.01
- P(Defective | Basketball) = 0.02
- P(Defective | Baseball) = 0.03

**Posterior Probabilities (Given):**
- P(Football | Defective) = 0.4
- P(Basketball | Defective) = 0.4
- P(Baseball | Defective) = 0.2

**Question:** What is the most likely type of defective item?

---

#### **Understanding the Problem:**

We are given **posterior probabilities** directly, which tell us that **after observing a defective item**, the probabilities are:
- 40% chance it's a Football
- 40% chance it's a Basketball
- 20% chance it's a Baseball

---

#### **Method 1: Direct Answer from Given Posterior Probabilities**

**Step-by-step:**
```
P(Football | Defective) = 0.4 = 40%
P(Basketball | Defective) = 0.4 = 40%
P(Baseball | Defective) = 0.2 = 20%
```

**Comparison:**
- Football and Basketball are **equally likely** (both 40%)
- Baseball is least likely (20%)

**Answer: Footballs and Basketballs are equally most likely** (both 40% probability)

---

#### **Method 2: Understanding Through Bayes' Theorem**

Even though posterior probabilities are given, let's understand **why** these values make sense using **Bayes' Theorem**.

**Bayes' Theorem Formula:**
```
P(Item | Defective) = [P(Defective | Item) × P(Item)] / P(Defective)
```

**Step-by-step:**

**1. Let's work backwards to find production proportions:**

We know:
- P(Football | Defective) = 0.4
- P(Defective | Football) = 0.01

Let P(Football) = pF, P(Basketball) = pB, P(Baseball) = pBa

**From Bayes' theorem:**
```
0.4 = (0.01 × pF) / P(Defective)
0.4 = (0.02 × pB) / P(Defective)
0.2 = (0.03 × pBa) / P(Defective)
```

**2. Dividing first two equations:**
```
0.4/0.4 = (0.01 × pF)/(0.02 × pB)
1 = 0.01pF / 0.02pB
pF = 2pB
```

This means **Footballs are produced at twice the rate of Basketballs**.

**3. Dividing first and third equations:**
```
0.4/0.2 = (0.01 × pF)/(0.03 × pBa)
2 = 0.01pF / 0.03pBa
0.06pBa = 0.01pF
pBa = pF/6
```

**4. If we assume production proportions:**
Let's say pB = 1 unit, then:
- pF = 2 units
- pBa = 2/6 = 0.33 units

Normalizing (so they sum to 1):
```
Total = 2 + 1 + 0.33 = 3.33
P(Football) = 2/3.33 = 0.60
P(Basketball) = 1/3.33 = 0.30
P(Baseball) = 0.33/3.33 = 0.10
```

**5. Calculate P(Defective):**
```
P(Defective) = P(D|F)×P(F) + P(D|B)×P(B) + P(D|Ba)×P(Ba)
P(Defective) = 0.01×0.60 + 0.02×0.30 + 0.03×0.10
P(Defective) = 0.006 + 0.006 + 0.003
P(Defective) = 0.015 or 1.5%
```

**6. Verify using Bayes' Theorem:**
```
P(Football | Defective) = (0.01 × 0.60) / 0.015 = 0.006/0.015 = 0.4 ✓
P(Basketball | Defective) = (0.02 × 0.30) / 0.015 = 0.006/0.015 = 0.4 ✓
P(Baseball | Defective) = (0.03 × 0.10) / 0.015 = 0.003/0.015 = 0.2 ✓
```

---

#### **Interpretation and Analysis:**

**Key Insights:**

1. **Why are Football and Basketball equally likely despite different defect rates?**
   - Footballs have a **lower defect rate** (1%) but are **produced in larger quantities** (60% of production)
   - Basketballs have a **higher defect rate** (2%) but **lower production volume** (30% of production)
   - These factors balance out: 0.01 × 60 = 0.02 × 30 = 0.6

2. **Why is Baseball least likely?**
   - Despite having the **highest defect rate** (3%)
   - It has the **lowest production volume** (10%)
   - Net contribution to defectives: 0.03 × 10 = 0.3

3. **Production vs Quality Trade-off:**
   - High production volume can offset low defect rate
   - This explains why Football (1% defect, high volume) equals Basketball (2% defect, medium volume)

---

#### **Decision Tree Visualization:**

```
Defective Item Found
    ├─→ 40% Football (despite only 1% defect rate → high production)
    ├─→ 40% Basketball (2% defect rate → medium production)
    └─→ 20% Baseball (3% defect rate → low production)
```

---

#### **Final Answer:**

**Most Likely Type of Defective Item: FOOTBALL or BASKETBALL (equally likely at 40% each)**

**Complete Answer:**
"When a defective item is picked from the manufacturing line, it is **equally likely to be either a Football or a Basketball**, with each having a **40% probability**. Baseball is the least likely at only 20%.

This result is counterintuitive because while Basketballs have double the defect rate of Footballs (2% vs 1%), Footballs are produced at double the rate of Basketballs, resulting in equal contributions to the defective item pool.

From a **quality control perspective**, both Football and Basketball production lines require equal attention, even though Basketballs have a higher defect rate, because the volume of Football production compensates for its lower defect rate."

---

### Part c) Measures of Central Tendency (5 marks)

**Answer:**

#### **MEASURES OF CENTRAL TENDENCY**

Central tendency measures describe the **center** or **typical value** of a dataset. They provide a single value that represents the entire distribution.

---

### **1. MEAN (ARITHMETIC AVERAGE)**

**Definition:**
The sum of all values divided by the number of values.

**Formula:**
- **Population Mean:** μ = Σx / N
- **Sample Mean:** x̄ = Σx / n

**Example:**
Test scores of 5 students: 70, 75, 80, 85, 90

```
Mean = (70 + 75 + 80 + 85 + 90) / 5
Mean = 400 / 5
Mean = 80
```

**Characteristics:**
- Uses **all data points**
- **Sensitive to outliers**
- Most commonly used measure
- Can be used for **further calculations**

**When to use:**
- Data is normally distributed
- No extreme outliers
- Interval or ratio scale data

**Advantages:**
- Mathematical properties allow advanced calculations
- Minimizes squared deviations
- Widely understood

**Disadvantages:**
- Affected by extreme values
- May not represent typical value with skewed data

---

### **2. MEDIAN**

**Definition:**
The middle value when data is arranged in order.

**Formula:**
- **Odd n:** Median = Middle value = value at position (n+1)/2
- **Even n:** Median = Average of two middle values = [value at n/2 + value at (n/2 + 1)] / 2

**Example 1 (Odd n):**
Salaries (in thousands): 30, 35, 40, 45, 200

```
Arrange: 30, 35, 40, 45, 200
n = 5 (odd)
Median = 3rd value = 40
```

Note: Mean would be 70, but median (40) better represents typical salary

**Example 2 (Even n):**
House prices (in lakhs): 25, 30, 35, 40, 45, 50

```
n = 6 (even)
Median = (35 + 40) / 2 = 37.5
```

**Characteristics:**
- **Not affected by outliers**
- Divides data into two equal halves
- Represents the 50th percentile

**When to use:**
- Data has outliers
- Skewed distributions
- Ordinal, interval, or ratio data

**Advantages:**
- Robust to outliers
- Better for skewed data
- Easy to understand

**Disadvantages:**
- Ignores extreme values
- Cannot be used in further mathematical calculations
- Less efficient for small samples

---

### **3. MODE**

**Definition:**
The value that appears most frequently in the dataset.

**Formula:**
Mode = Value with highest frequency

**Example 1 (Unimodal):**
Shoe sizes sold: 7, 8, 8, 9, 9, 9, 10, 11

```
Frequency count:
7: 1 time
8: 2 times
9: 3 times (highest)
10: 1 time
11: 1 time

Mode = 9
```

**Example 2 (Bimodal):**
Test scores: 70, 75, 75, 80, 85, 85, 90

```
Both 75 and 85 appear twice
Mode = 75 and 85 (bimodal)
```

**Example 3 (No mode):**
Values: 10, 20, 30, 40, 50 (all appear once)
Mode = No mode

**Types:**
- **Unimodal:** One mode
- **Bimodal:** Two modes
- **Multimodal:** More than two modes
- **No mode:** All values appear equally

**Characteristics:**
- Can be used with **categorical data**
- May not exist or may not be unique
- Not affected by extreme values

**When to use:**
- Categorical/nominal data
- Finding most common category
- Discrete data with repeated values

**Advantages:**
- Only measure for nominal data
- Easy to identify
- Not affected by outliers

**Disadvantages:**
- May not exist
- May have multiple modes
- Ignores most of the data
- Not useful for continuous data without grouping

---

### **COMPREHENSIVE EXAMPLE**

**Scenario:** Monthly income (in thousands) of 9 employees:

**Data:** 20, 22, 25, 25, 30, 35, 40, 45, 200

**Calculate all three measures:**

**1. Mean:**
```
μ = (20 + 22 + 25 + 25 + 30 + 35 + 40 + 45 + 200) / 9
μ = 442 / 9
μ = 49.11
```
**Mean = $49,110**

**2. Median:**
```
Already arranged: 20, 22, 25, 25, 30, 35, 40, 45, 200
n = 9 (odd)
Median = 5th value = 30
```
**Median = $30,000**

**3. Mode:**
```
25 appears twice (most frequent)
```
**Mode = $25,000**

---

### **COMPARISON AND INTERPRETATION**

| Measure | Value | What it tells us |
|---------|-------|------------------|
| Mean | $49,110 | Pulled up by one high salary ($200k) |
| Median | $30,000 | Typical employee salary |
| Mode | $25,000 | Most common salary |

**Analysis:**
- **Mean > Median > Mode** indicates **positive skew** (right-skewed distribution)
- The CEO's salary ($200k) inflates the mean
- **Median ($30k) best represents the typical employee**
- Mode ($25k) shows the entry-level salary

---

### **CHOOSING THE RIGHT MEASURE**

| Situation | Best Measure | Reason |
|-----------|--------------|--------|
| Normal distribution | **Mean** | Utilizes all data efficiently |
| Skewed distribution | **Median** | Resistant to outliers |
| Categorical data | **Mode** | Only applicable measure |
| Income/wealth data | **Median** | Avoids influence of extremely rich |
| Academic performance | **Mean** | Fair representation of overall performance |
| Customer ratings | **Mode** | Identifies most common opinion |
| House prices | **Median** | Reduces effect of luxury properties |

---

### **RELATIONSHIP IN DIFFERENT DISTRIBUTIONS**

**1. Symmetric Distribution (Normal):**
```
Mean = Median = Mode
```

**2. Positively Skewed (Right-skewed):**
```
Mode < Median < Mean
```

**3. Negatively Skewed (Left-skewed):**
```
Mean < Median < Mode
```

---

### **PRACTICAL APPLICATIONS**

**Business:**
- **Mean:** Calculate average revenue, costs, profits
- **Median:** Determine typical salary, house prices (avoids billionaire effect)
- **Mode:** Find best-selling product, most common customer complaint

**Education:**
- **Mean:** Calculate class average for grades
- **Median:** Identify middle-performing student
- **Mode:** Find most common answer on multiple-choice test

**Healthcare:**
- **Mean:** Average recovery time, drug dosage
- **Median:** Typical patient wait time (avoids outlier effect)
- **Mode:** Most common blood type, frequent symptoms

---

**Conclusion:**
Each measure of central tendency provides different insights into data. The **choice depends on the data distribution, presence of outliers, and the specific question being answered**. Using multiple measures together provides a more complete picture of the data's central location.

---

## Question 3

### Part a) Health Researcher - Sleep Duration and Stress Level (10 marks)

**Given Data:**

| S.No | Sleep Duration (hours) | Stress Level (1-10) | Mental Well-Being Score (0-100) |
|------|------------------------|---------------------|----------------------------------|
| 1 | 8 | 3 | 80 |
| 2 | 7 | 5 | 75 |
| 3 | 8 | 2 | 90 |
| 4 | 6 | 5 | 75 |
| 5 | 4 | 9 | 60 |

**Question:** Determine which independent variable (Sleep Duration or Stress Level) has a stronger relationship with Mental Well-Being.

---

#### **METHOD: Pearson Correlation Coefficient**

**Formula:** r = Σ[(x - x̄)(y - ȳ)] / √[Σ(x - x̄)² × Σ(y - ȳ)²]

---

### **CORRELATION 1: Sleep Duration vs Mental Well-Being**

**Step 1: Calculate means**
```
Mean Sleep Duration (x̄) = (8 + 7 + 8 + 6 + 4) / 5 = 33/5 = 6.6 hours
Mean Mental Well-Being (ȳ) = (80 + 75 + 90 + 75 + 60) / 5 = 380/5 = 76
```

**Step 2: Create calculation table**

| Sleep (x) | Well-Being (y) | (x - x̄) | (y - ȳ) | (x - x̄)(y - ȳ) | (x - x̄)² | (y - ȳ)² |
|-----------|----------------|----------|----------|------------------|-----------|-----------|
| 8 | 80 | 1.4 | 4 | 5.6 | 1.96 | 16 |
| 7 | 75 | 0.4 | -1 | -0.4 | 0.16 | 1 |
| 8 | 90 | 1.4 | 14 | 19.6 | 1.96 | 196 |
| 6 | 75 | -0.6 | -1 | 0.6 | 0.36 | 1 |
| 4 | 60 | -2.6 | -16 | 41.6 | 6.76 | 256 |
| **Sum** | | | | **67** | **11.2** | **470** |

**Step 3: Calculate correlation**
```
r = Σ[(x - x̄)(y - ȳ)] / √[Σ(x - x̄)² × Σ(y - ȳ)²]
r = 67 / √(11.2 × 470)
r = 67 / √5264
r = 67 / 72.55
r = 0.923
```

**Correlation (Sleep Duration vs Mental Well-Being) = +0.923**

**Interpretation:** Very strong positive correlation - as sleep duration increases, mental well-being increases.

---

### **CORRELATION 2: Stress Level vs Mental Well-Being**

**Step 1: Calculate means**
```
Mean Stress Level (x̄) = (3 + 5 + 2 + 5 + 9) / 5 = 24/5 = 4.8
Mean Mental Well-Being (ȳ) = 76 (same as before)
```

**Step 2: Create calculation table**

| Stress (x) | Well-Being (y) | (x - x̄) | (y - ȳ) | (x - x̄)(y - ȳ) | (x - x̄)² | (y - ȳ)² |
|------------|----------------|----------|----------|------------------|-----------|-----------|
| 3 | 80 | -1.8 | 4 | -7.2 | 3.24 | 16 |
| 5 | 75 | 0.2 | -1 | -0.2 | 0.04 | 1 |
| 2 | 90 | -2.8 | 14 | -39.2 | 7.84 | 196 |
| 5 | 75 | 0.2 | -1 | -0.2 | 0.04 | 1 |
| 9 | 60 | 4.2 | -16 | -67.2 | 17.64 | 256 |
| **Sum** | | | | **-113.8** | **28.8** | **470** |

**Step 3: Calculate correlation**
```
r = -113.8 / √(28.8 × 470)
r = -113.8 / √13536
r = -113.8 / 116.36
r = -0.978
```

**Correlation (Stress Level vs Mental Well-Being) = -0.978**

**Interpretation:** Very strong negative correlation - as stress level increases, mental well-being decreases.

---

### **COEFFICIENT OF DETERMINATION**

**For Sleep Duration:**
```
r² = (0.923)²
r² = 0.852 or 85.2%
```
**Interpretation:** 85.2% of the variation in Mental Well-Being can be explained by Sleep Duration.

**For Stress Level:**
```
r² = (-0.978)²
r² = 0.957 or 95.7%
```
**Interpretation:** 95.7% of the variation in Mental Well-Being can be explained by Stress Level.

---

### **COMPARISON AND FINAL ANSWER**

**Summary Table:**

| Independent Variable | Correlation (r) | |r| | r² | Relationship |
|---------------------|-----------------|------|-----|--------------|
| Sleep Duration | +0.923 | 0.923 | 85.2% | Strong Positive |
| **Stress Level** | **-0.978** | **0.978** | **95.7%** | **Very Strong Negative** |

---

### **CONCLUSION**

**STRESS LEVEL has a stronger relationship with Mental Well-Being.**

**Statistical Justification:**

1. **Correlation Magnitude:**
   - |r_stress| = 0.978 > |r_sleep| = 0.923
   - Stress Level has a slightly stronger linear relationship

2. **Coefficient of Determination:**
   - r²_stress = 95.7% > r²_sleep = 85.2%
   - Stress Level explains **10.5% more variation** in Mental Well-Being

3. **Practical Difference:**
   - **Stress Level** accounts for 95.7% of Mental Well-Being variation
   - **Sleep Duration** accounts for 85.2% of Mental Well-Being variation
   - The remaining unexplained variation: 4.3% vs 14.8%

4. **Direction of Relationships:**
   - **Sleep Duration:** Positive relationship (more sleep → better well-being)
   - **Stress Level:** Negative relationship (more stress → worse well-being)

5. **Interpretation:**
   - Both variables are important predictors
   - **Stress Level is the slightly stronger predictor**
   - The near-perfect correlation (-0.978) suggests Stress Level is an **excellent predictor**
   - Every 1-unit increase in stress corresponds to approximately 6-point decrease in well-being

---

### **RECOMMENDATIONS FOR MENTAL HEALTH:**

Based on this analysis:

1. **Primary Focus:** **Stress management** should be the primary intervention (stronger predictor)
2. **Secondary Focus:** Adequate sleep duration is also crucial (strong predictor)
3. **Holistic Approach:** Both factors are highly important - interventions should address both
4. **Predictive Power:** You can predict Mental Well-Being with 95.7% accuracy using Stress Level alone

---

### Part b) Probabilistic Sampling Techniques (5 marks)

**Answer:**

#### **PROBABILISTIC SAMPLING TECHNIQUES**

Probabilistic (or Probability) sampling is a sampling method where **every member of the population has a known, non-zero probability of being selected**. This allows for **statistical inference** and **generalization** to the population.

---

### **1. SIMPLE RANDOM SAMPLING (SRS)**

**Definition:**
Every member of the population has an **equal chance** of being selected. Each possible sample of size n has the same probability of being chosen.

**Method:**
- Assign numbers to all population members
- Use random number generator or lottery method to select sample

**Formula for probability:**
```
P(selecting any individual) = n / N
where n = sample size, N = population size
```

**Example:**
A university has 10,000 students. To survey 500 students:
- Assign ID numbers 1-10,000 to all students
- Use random number generator to select 500 numbers
- Survey students with those ID numbers
- Each student has 500/10,000 = 5% chance of selection

**Advantages:**
- Unbiased representation
- Simple to understand
- Eliminates selection bias
- Allows statistical inference

**Disadvantages:**
- Requires complete population list
- May miss important subgroups
- Can be expensive if population is geographically dispersed
- May not be practical for large populations

**When to use:**
- Homogeneous population
- Complete sampling frame available
- No specific subgroups of interest

---

### **2. SYSTEMATIC SAMPLING**

**Definition:**
Select every **kth member** from the population after a random start.

**Method:**
1. Calculate sampling interval: k = N/n
2. Randomly select starting point between 1 and k
3. Select every kth member thereafter

**Formula:**
```
Sampling interval (k) = Population size (N) / Sample size (n)
```

**Example:**
A factory wants to inspect 50 products from a production run of 1000:
- k = 1000/50 = 20
- Randomly select starting point: suppose it's 7
- Select products numbered: 7, 27, 47, 67, 87, ..., 987
- Every 20th product after the 7th

**Advantages:**
- Easier than SRS (no need for random numbers for each selection)
- Spreads sample evenly across population
- Less time-consuming
- Good for populations arranged in lists

**Disadvantages:**
- Risk of periodicity (if population has hidden pattern matching k)
- Once starting point is chosen, rest is determined
- If list has ordering, may introduce bias

**When to use:**
- Population list is available
- No periodic patterns in population
- Sampling from assembly line or production process

---

### **3. STRATIFIED SAMPLING**

**Definition:**
Divide population into **homogeneous subgroups (strata)** based on certain characteristics, then randomly sample from each stratum.

**Method:**
1. Divide population into mutually exclusive strata
2. Randomly sample from each stratum
3. Can use proportionate or disproportionate allocation

**Types:**

**a) Proportionate Stratified Sampling:**
```
Sample from each stratum = (Stratum size / Population size) × Total sample size
```

**b) Disproportionate Stratified Sampling:**
- Over-sample smaller strata for comparison
- Or allocate based on variance within strata

**Example:**
A college has 5,000 students: 2,000 freshmen, 1,500 sophomores, 1,000 juniors, 500 seniors. To sample 500 students:

**Proportionate allocation:**
- Freshmen: (2000/5000) × 500 = 200
- Sophomores: (1500/5000) × 500 = 150
- Juniors: (1000/5000) × 500 = 100
- Seniors: (500/5000) × 500 = 50

Randomly select the calculated number from each year.

**Advantages:**
- Ensures representation of all subgroups
- Increases precision/reduces sampling error
- Allows comparison between strata
- More efficient than SRS for heterogeneous populations

**Disadvantages:**
- Requires knowledge of population characteristics
- More complex to administer
- Need to identify appropriate strata
- Requires sampling frame for each stratum

**When to use:**
- Population is heterogeneous
- Subgroup comparisons needed
- Known important population characteristics

---

### **4. CLUSTER SAMPLING**

**Definition:**
Divide population into **clusters (groups)**, randomly select some clusters, then sample **all members** (one-stage) or some members (two-stage) from selected clusters.

**Method:**
1. Divide population into clusters (usually geographic)
2. Randomly select clusters
3. Survey all or some members from selected clusters

**Formula:**
```
Number of clusters to select = (Desired sample size) / (Average cluster size)
```

**Example:**
Survey high school students across a state with 500 schools:
- **Clusters:** Each school is a cluster
- **One-stage:** Randomly select 25 schools, survey ALL students in those 25 schools
- **Two-stage:** Randomly select 50 schools, then randomly select 30 students from each school

**Practical Example:**
Market research company wants to survey 1,000 households in a city:
- Divide city into 100 neighborhoods (clusters)
- Randomly select 10 neighborhoods
- Survey 100 households from each selected neighborhood

**Advantages:**
- Cost-effective (geographically concentrated)
- Practical when population is spread out
- Doesn't require complete population list
- Easier to administer

**Disadvantages:**
- Higher sampling error than SRS or stratified (if clusters are heterogeneous)
- Clusters should be heterogeneous internally
- Less precise than other methods
- Risk of cluster selection bias

**When to use:**
- Geographically dispersed population
- High costs of travel/contact
- No complete sampling frame available
- Natural groupings exist (schools, hospitals, villages)

---

### **5. MULTI-STAGE SAMPLING**

**Definition:**
Sampling conducted in **multiple stages**, combining different sampling techniques at each stage.

**Method:**
1. **Stage 1:** Select primary sampling units (PSUs) - usually larger clusters
2. **Stage 2:** Select secondary sampling units (SSUs) from selected PSUs
3. **Stage 3:** (if needed) Select tertiary units, and so on
4. Different sampling methods can be used at each stage

**Example:**
National health survey:
- **Stage 1:** Randomly select 20 states (cluster sampling)
- **Stage 2:** Randomly select 5 districts from each selected state (cluster sampling)
- **Stage 3:** Randomly select 10 villages/towns from each district (cluster sampling)
- **Stage 4:** Randomly select 50 households from each village (systematic sampling)
- **Stage 5:** Select all adults from selected households

**Real-world Example:**
Election polling across India:
- **Stage 1:** Stratify states by region, randomly select states
- **Stage 2:** Cluster sample constituencies within selected states
- **Stage 3:** Stratify by urban/rural, randomly select polling booths
- **Stage 4:** Systematically sample voters from each booth

**Advantages:**
- Very practical for large populations
- Cost-effective
- Flexible (can combine methods)
- Feasible when complete list unavailable

**Disadvantages:**
- More complex design
- Higher sampling error (multiple stages compound error)
- Difficult to calculate sampling error
- Requires careful planning

**When to use:**
- Very large, geographically dispersed populations
- National or international surveys
- When single-stage sampling is impractical
- Limited budget with wide geographic scope

---

### **COMPARISON TABLE**

| Method | Selection Process | Complexity | Cost | Precision | When to Use |
|--------|------------------|------------|------|-----------|-------------|
| **Simple Random** | Each member equal chance | Low | Medium | High | Small, homogeneous population |
| **Systematic** | Every kth member | Low | Low | High | Ordered list available |
| **Stratified** | Random from each stratum | Medium | Medium | Very High | Heterogeneous population |
| **Cluster** | Random clusters, all/some members | Medium | Low | Medium | Geographically dispersed |
| **Multi-stage** | Multiple stages of sampling | High | Low | Low-Medium | Very large population |

---

### **CHOOSING THE RIGHT METHOD**

| Scenario | Best Method | Reason |
|----------|-------------|--------|
| National census | Multi-stage | Large, geographically dispersed |
| Quality control on assembly line | Systematic | Products in sequence |
| Student performance by gender/year | Stratified | Ensure subgroup representation |
| Village health survey in district | Cluster | Concentrated sampling reduces cost |
| Employee satisfaction in small company | Simple Random | Small, homogeneous group |

---

**Conclusion:**
Probabilistic sampling methods provide a **scientific basis for making inferences** about populations. The choice depends on **population characteristics, available resources, required precision, and research objectives**. In practice, **multi-stage and stratified sampling** are most common in large-scale surveys due to their balance of cost, practicality, and statistical rigor.

---

### Part c) Restaurant Menu Arrangement - Permutation (5 marks)

**Question:** A restaurant has 5 unique dishes. The chef wants to create a tasting menu by selecting and arranging 3 out of these 5 dishes. How many different ways can the chef arrange the selected dishes?

**Answer:**

This is a **PERMUTATION** problem because:
1. **Order matters** (Dish A → Dish B → Dish C is different from Dish C → Dish B → Dish A)
2. We are **selecting AND arranging** 3 dishes from 5
3. **No repetition** (each dish can only appear once)

---

#### **Formula: Permutation**

**General Formula:**
```
P(n, r) = n! / (n - r)!
```

Where:
- n = total number of items = 5 dishes
- r = number of items to arrange = 3 dishes
- ! = factorial

---

#### **Step-by-step Solution:**

**Step 1: Identify the values**
```
n = 5 dishes
r = 3 positions on tasting menu
```

**Step 2: Apply the permutation formula**
```
P(5, 3) = 5! / (5 - 3)!
P(5, 3) = 5! / 2!
```

**Step 3: Calculate factorials**
```
5! = 5 × 4 × 3 × 2 × 1 = 120
2! = 2 × 1 = 2
```

**Step 4: Divide**
```
P(5, 3) = 120 / 2
P(5, 3) = 60
```

---

#### **Alternative Method (Multiplication Principle):**

**Think of filling 3 positions sequentially:**

```
Position 1: 5 choices (can choose any of the 5 dishes)
Position 2: 4 choices (one dish already used)
Position 3: 3 choices (two dishes already used)

Total arrangements = 5 × 4 × 3 = 60
```

---

#### **Verification:**

Both methods give the same answer:
- **Formula method:** 5!/2! = 120/2 = 60
- **Multiplication principle:** 5 × 4 × 3 = 60

**Answer: 60 different ways**

---

#### **Detailed Explanation:**

**Example with actual dishes:**
Let's say the 5 dishes are:
- A = Appetizer
- B = Soup
- C = Salad
- D = Main Course
- E = Dessert

**Some possible 3-dish tasting menus:**
1. A-B-C (different from C-B-A)
2. A-B-D
3. A-B-E
4. A-C-D
...
60. E-D-C

---

#### **Why ORDER Matters:**

The **sequence** of serving matters in a tasting menu:
- **A → B → C**: Light appetizer, then soup, then salad
- **C → B → A**: Salad first, then soup, then appetizer

These create **different dining experiences**, so they count as different arrangements.

---

#### **Contrast with COMBINATION:**

**If order didn't matter** (just selecting 3 dishes, not arranging):

**Formula:** C(n, r) = n! / [r! × (n-r)!]

```
C(5, 3) = 5! / (3! × 2!)
C(5, 3) = 120 / (6 × 2)
C(5, 3) = 120 / 12
C(5, 3) = 10
```

**Comparison:**
- **Permutation** (order matters): 60 ways
- **Combination** (order doesn't matter): 10 ways
- **Relationship:** P(5,3) = C(5,3) × 3! = 10 × 6 = 60

---

#### **Practical Application:**

**For the Restaurant:**
- The chef has **60 different tasting menu sequences** to choose from
- Each arrangement creates a unique culinary journey
- The chef might consider:
  - Flavor progression (light to heavy)
  - Color presentation
  - Cooking technique variety
  - Guest preferences

**General Applications of Permutations:**
1. **Event scheduling:** Order of speakers at a conference
2. **Sports:** Batting order in cricket/baseball
3. **Music:** Setlist order for a concert
4. **Transportation:** Route sequencing for deliveries
5. **Password creation:** Arrangement of characters

---

#### **Mathematical Properties:**

**Relation to Factorials:**
```
P(n, r) = n × (n-1) × (n-2) × ... × (n-r+1)
P(5, 3) = 5 × 4 × 3 = 60
```

**Special Cases:**
- P(n, n) = n! (arranging all items)
- P(n, 1) = n (selecting one item)
- P(n, 0) = 1 (arranging zero items)

---

### **FINAL ANSWER**

**The chef can arrange the 3 selected dishes in 60 different ways.**

**Formula used:** P(5, 3) = 5!/(5-3)! = 5!/2! = 60

**Calculation:** 5 × 4 × 3 = 60

---

**END OF ANSWER SHEET - SET A**

---
