# 📊 Complete Statistics Formula Guide with Examples

**Comprehensive Reference for AI&DS Statistics**  
*Last Updated: September 2025*

---

## 📋 **TABLE OF CONTENTS**

1. [Complete Formulas by Data Type](#1-complete-formulas-by-data-type)
2. [Normal Distribution](#2-normal-distribution)
3. [Central Limit Theorem & Z-Scores](#3-central-limit-theorem--z-scores)
4. [Measures of Central Tendency](#4-measures-of-central-tendency)
5. [Measures of Variability](#5-measures-of-variability)
6. [Measures of Dispersion](#6-measures-of-dispersion)
7. [Sampling Methods](#7-sampling-methods)
8. [Calculator Functions (Casio FX-991CW)](#8-calculator-functions-casio-fx-991cw)
9. [Quick Reference Tables](#9-quick-reference-tables)

---

## 1. Complete Formulas by Data Type

### **📊 MEAN CALCULATIONS**

#### **A. Ungrouped Data**
**Formula:**
```
x̄ = Σx / n
```

**Where:**
- x̄ = Sample mean (arithmetic average)
- Σx = Sum of all individual data values
- n = Total number of data points in the sample

**Explanation:** Add all values and divide by the count. This gives the central value around which data clusters.

**Example:**
Data: 2, 4, 6, 8, 10
- Σx = 2 + 4 + 6 + 8 + 10 = 30
- n = 5 (five data points)
- x̄ = 30/5 = 6

**Casio FX-991CW:** [MODE][3][1] → Enter each value [=] → [SHIFT][1][1][=]

---

#### **B. Ungrouped Data with Frequency**
**Formula:**
```
x̄ = Σ(f × x) / Σf
```

**Where:**
- x̄ = Sample mean
- f = Frequency of each distinct value
- x = Each distinct data value
- Σ(f × x) = Sum of (frequency × value) for all distinct values
- Σf = Total frequency (sum of all frequencies)

**Explanation:** When data values repeat, multiply each value by its frequency, sum these products, then divide by total frequency.

**Example:**
| Value (x) | Frequency (f) | f × x |
|-----------|---------------|-------|
| 2         | 3             | 6     |
| 4         | 5             | 20    |
| 6         | 2             | 12    |
| **Total** | **Σf = 10**   | **Σ(f×x) = 38** |

- x̄ = 38/10 = 3.8

**Casio FX-991CW:** [MODE][3][1] → Enter [value][×][frequency][=] for each → [SHIFT][1][1][=]

---

#### **C. Grouped Data**
**Formula:**
```
x̄ = Σ(f × x) / Σf
```

**Where:**
- x̄ = Sample mean
- f = Frequency of each class interval
- x = Class midpoint = (Lower class limit + Upper class limit) / 2
- Σ(f × x) = Sum of (frequency × midpoint) for all classes
- Σf = Total frequency across all classes

**Explanation:** For grouped data, use class midpoints as representative values since we don't know exact values within each class.

**Example:**
| Class Interval | Midpoint (x) | Frequency (f) | f × x |
|----------------|--------------|---------------|-------|
| 0-10           | 5            | 4             | 20    |
| 10-20          | 15           | 6             | 90    |
| 20-30          | 25           | 3             | 75    |
| **Total**      | **-**        | **Σf = 13**   | **Σ(f×x) = 185** |

- x̄ = 185/13 = 14.23

---

### **📊 MEDIAN CALCULATIONS**

#### **A. Ungrouped Data**
**Formula:**
```
For Odd n: Median = x((n+1)/2)
For Even n: Median = [x(n/2) + x((n/2)+1)] / 2
```

**Where:**
- n = Total number of data points
- x(position) = Value at the specified position in ordered data
- (n+1)/2 = Position of median when n is odd
- n/2 and (n/2)+1 = Positions of two middle values when n is even

**Explanation:** Median is the middle value that divides ordered data into two equal halves. For even numbers of values, take average of two middle values.

**Example 1 (Odd n):**
Data: 1, 3, 5, 7, 9 (n = 5)
- Position = (5+1)/2 = 3rd position
- Median = 5

**Example 2 (Even n):**
Data: 2, 4, 6, 8 (n = 4)
- Positions = 4/2 = 2nd and 3rd positions
- Median = (4+6)/2 = 5

---

#### **B. Ungrouped Data with Frequency**
**Formula:**
```
Step 1: Median Position = (N+1)/2
Step 2: Create cumulative frequency table
Step 3: Find value where cumulative frequency ≥ median position
```

**Where:**
- N = Σf = Total frequency (sum of all frequencies)
- Cumulative frequency = Running total of frequencies up to each value
- Median position = Location of the middle value in the ordered dataset

**Explanation:** Use cumulative frequency to locate which value contains the median position.

**Example:**
| Value | Frequency | Cumulative Frequency |
|-------|-----------|---------------------|
| 1     | 2         | 2                   |
| 2     | 5         | 7 ← Contains position 5.5 |
| 3     | 3         | 10                  |

- N = 10, Median Position = (10+1)/2 = 5.5
- Cumulative frequency 7 first exceeds 5.5
- Median = 2

---

#### **C. Grouped Data**
**Formula:**
```
Median = L + [(n/2 - CF)/f] × h
```

**Where:**
- L = Lower boundary of the median class
- n = Total frequency (Σf)
- n/2 = Position where median lies
- CF = Cumulative frequency before the median class
- f = Frequency of the median class
- h = Class width (upper limit - lower limit)

**Explanation:** Assumes values are evenly distributed within the median class. We interpolate to find the exact median position.

**Example:**
| Class   | Frequency | Cumulative Frequency |
|---------|-----------|---------------------|
| 0-10    | 8         | 8                   |
| 10-20   | 12        | 20 ← Median class   |
| 20-30   | 5         | 25                  |

- n = 25, n/2 = 12.5 (median position)
- Median class: 10-20 (CF = 20 first exceeds 12.5)
- L = 10, CF = 8, f = 12, h = 10
- Median = 10 + [(12.5-8)/12] × 10 = 10 + 3.75 = 13.75

---

### **📊 MODE CALCULATIONS**

#### **A. Ungrouped Data**
**Formula:**
```
Mode = Value with highest frequency
```

**Where:**
- Frequency = Number of times each value appears
- Mode = The most frequently occurring value(s)

**Explanation:** Mode represents the most common value in the dataset. A dataset can have no mode, one mode (unimodal), or multiple modes (bimodal, multimodal).

**Example:**
Data: 1, 2, 2, 3, 3, 3, 4
- Value 3 appears 3 times (highest frequency)
- Mode = 3

---

#### **B. Ungrouped Data with Frequency**
**Formula:**
```
Mode = Value corresponding to maximum frequency
```

**Where:**
- Maximum frequency = Highest value in the frequency column
- Corresponding value = The data value with this maximum frequency

**Explanation:** Directly identify the value with the highest frequency from the frequency table.

**Example:**
| Value | Frequency |
|-------|-----------|
| 1     | 2         |
| 2     | 7 ← Max   |
| 3     | 4         |

Mode = 2 (has frequency of 7)

---

#### **C. Grouped Data**
**Formula:**
```
Mode = L + [(f₁-f₀)/(2f₁-f₀-f₂)] × h
```

**Where:**
- L = Lower boundary of the modal class
- f₁ = Frequency of the modal class (highest frequency)
- f₀ = Frequency of the class immediately before the modal class
- f₂ = Frequency of the class immediately after the modal class
- h = Class width of the modal class
- 2f₁-f₀-f₂ = Denominator ensuring proper weighting

**Explanation:** Since we don't know exact values within classes, we estimate the mode's position within the modal class based on frequencies of adjacent classes.

**Example:**
| Class   | Frequency |
|---------|-----------|
| 0-10    | 5         | ← f₀
| 10-20   | 15        | ← f₁ (Modal class)
| 20-30   | 8         | ← f₂

- L = 10, f₁ = 15, f₀ = 5, f₂ = 8, h = 10
- Mode = 10 + [(15-5)/(2×15-5-8)] × 10
- Mode = 10 + [10/17] × 10 = 10 + 5.88 = 15.88

---

### **📊 STANDARD DEVIATION CALCULATIONS**

#### **A. Ungrouped Data**
**Population Formula:**
```
σ = √[Σ(x-μ)²/N]
```

**Sample Formula:**
```
s = √[Σ(x-x̄)²/(n-1)]
```

**Where:**
- σ = Population standard deviation
- s = Sample standard deviation
- x = Individual data values
- μ = Population mean
- x̄ = Sample mean
- N = Population size
- n = Sample size
- (n-1) = Degrees of freedom (Bessel's correction for unbiased estimation)
- Σ(x-μ)² = Sum of squared deviations from population mean
- Σ(x-x̄)² = Sum of squared deviations from sample mean

**Explanation:** Standard deviation measures the average distance of data points from the mean. Population uses N, sample uses (n-1) to correct for bias.

**Example:**
Data: 2, 4, 6, 8, 10 (x̄ = 6)

| x | x-x̄ | (x-x̄)² |
|---|-----|--------|
| 2 | -4  | 16     |
| 4 | -2  | 4      |
| 6 | 0   | 0      |
| 8 | 2   | 4      |
| 10| 4   | 16     |
|**Total**|**-**|**Σ(x-x̄)² = 40**|

- Population SD: σ = √(40/5) = √8 = 2.83
- Sample SD: s = √(40/4) = √10 = 3.16

---

#### **B. Ungrouped Data with Frequency**
**Formula:**
```
σ = √[Σf(x-x̄)²/Σf]
```

**Where:**
- f = Frequency of each distinct value
- x = Each distinct data value
- x̄ = Weighted mean calculated as Σ(fx)/Σf
- Σf = Total frequency
- f(x-x̄)² = Frequency times squared deviation for each value

**Explanation:** Each squared deviation is weighted by its frequency since values appear multiple times.

**Example:**
Given x̄ = 3.8 from previous frequency example:

| x | f | x-x̄ | (x-x̄)² | f(x-x̄)² |
|---|---|-----|--------|----------|
| 2 | 3 | -1.8| 3.24   | 9.72     |
| 4 | 5 | 0.2 | 0.04   | 0.20     |
| 6 | 2 | 2.2 | 4.84   | 9.68     |
|**Total**|**10**|**-**|**-**|**Σf(x-x̄)² = 19.60**|

- σ = √(19.60/10) = √1.96 = 1.40

---

#### **C. Grouped Data**
**Formula:**
```
σ = √[Σf(x-x̄)²/Σf]
```

**Where:**
- f = Frequency of each class
- x = Class midpoint for each interval
- x̄ = Mean calculated using class midpoints
- Σf = Total frequency across all classes
- f(x-x̄)² = Frequency times squared deviation of midpoint from mean

**Explanation:** Use class midpoints as representative values for calculating deviations, assuming uniform distribution within each class.

**Example:**
Using x̄ = 14.23 from previous grouped data example:

| Class | Midpoint(x) | f | x-x̄ | (x-x̄)² | f(x-x̄)² |
|-------|-------------|---|-----|--------|----------|
| 0-10  | 5           | 4 | -9.23| 85.19  | 340.76   |
| 10-20 | 15          | 6 | 0.77 | 0.59   | 3.54     |
| 20-30 | 25          | 3 | 10.77| 116.00 | 348.00   |
|**Total**|**-**      |**13**|**-**|**-**|**Σf(x-x̄)² = 692.30**|

- σ = √(692.30/13) = √53.25 = 7.30

---

## 2. Normal Distribution

### **A. Standard Normal Distribution (Z-Distribution)**

**Formula:**
```
f(z) = (1/√2π) × e^(-z²/2)
```

**Explanation:** This is the probability density function for a standard normal distribution with mean=0 and standard deviation=1.

**Example:**
Find the probability density at z = 1:
- f(1) = (1/√2π) × e^(-1²/2)
- f(1) = (1/2.507) × e^(-0.5)
- f(1) = 0.399 × 0.606 = 0.242

### **B. General Normal Distribution**

**Formula:**
```
f(x) = (1/(σ√2π)) × e^(-(x-μ)²/(2σ²))
```

**Explanation:** This gives the probability density for any normal distribution with mean μ and standard deviation σ.

**Example:**
For a normal distribution with μ = 50, σ = 10, find f(60):
- f(60) = (1/(10√2π)) × e^(-(60-50)²/(2×10²))
- f(60) = (1/25.066) × e^(-100/200)
- f(60) = 0.0399 × e^(-0.5) = 0.0242

### **C. Standardization (Z-Score)**

**Formula:**
```
Z = (x - μ)/σ

For Sample Mean:
Z = (x̄ - μ)/(σ/√n)
```

**Explanation:** Converts any normal distribution to standard normal (mean=0, sd=1) for probability calculations.

**Example:**
Given: μ = 100, σ = 15, x = 115
- Z = (115 - 100)/15 = 15/15 = 1.0
- This means x=115 is 1 standard deviation above the mean

**Casio FX-991CW:** [SHIFT] [STAT] → Select normal distribution functions

---

## 2. Normal Distribution

### **A. Standard Normal Distribution (Z-Distribution)**

**Formula:**
```
f(z) = (1/√2π) × e^(-z²/2)
```

**Where:**
- f(z) = Probability density function value at point z
- z = Standard normal variable (mean = 0, standard deviation = 1)
- π = Mathematical constant (≈ 3.14159)
- e = Euler's number (≈ 2.71828)
- √2π = Normalization constant (≈ 2.507)
- e^(-z²/2) = Exponential term that creates the bell curve shape

**Explanation:** This formula gives the height of the standard normal curve at any point z. The total area under the curve equals 1, representing 100% probability.

**Example:**
Find the probability density at z = 1:
- f(1) = (1/√2π) × e^(-1²/2)
- f(1) = (1/2.507) × e^(-0.5)
- f(1) = 0.399 × 0.606 = 0.242

**Interpretation:** The curve height at z = 1 is 0.242, indicating this is a moderately likely value.

---

### **B. General Normal Distribution**

**Formula:**
```
f(x) = (1/(σ√2π)) × e^(-(x-μ)²/(2σ²))
```

**Where:**
- f(x) = Probability density function value at point x
- x = Any value from the normal distribution
- μ = Population mean (center of distribution)
- σ = Population standard deviation (spread of distribution)
- σ√2π = Normalization factor adjusted for scale
- (x-μ)² = Squared distance from mean
- 2σ² = Variance multiplied by 2 (spread parameter)

**Explanation:** This extends the standard normal to any normal distribution with mean μ and standard deviation σ. The shape remains the same, but location and scale change.

**Example:**
For μ = 50, σ = 10, find f(60):
- f(60) = (1/(10√2π)) × e^(-(60-50)²/(2×10²))
- f(60) = (1/25.066) × e^(-100/200)
- f(60) = 0.0399 × e^(-0.5) = 0.0242

---

### **C. Standardization (Z-Score)**

**Individual Value Formula:**
```
Z = (x - μ)/σ
```

**Sample Mean Formula:**
```
Z = (x̄ - μ)/(σ/√n)
```

**Where:**
- Z = Standard score (number of standard deviations from mean)
- x = Individual observation value
- x̄ = Sample mean
- μ = Population mean
- σ = Population standard deviation
- n = Sample size
- σ/√n = Standard error of the mean

**Explanation:** Z-score converts any normal distribution to standard normal, allowing use of standard normal tables for probability calculations.

**Example:**
Given: μ = 100, σ = 15, x = 115
- Z = (115 - 100)/15 = 15/15 = 1.0
- Interpretation: x=115 is exactly 1 standard deviation above the mean

**Casio FX-991CW:** Calculate manually or use [SHIFT][STAT] for normal distribution functions

---

## 3. Central Limit Theorem & Z-Scores

### **A. Central Limit Theorem**

**Formula:**
```
X̄ ~ N(μ, σ²/n)

Standard Error: SE = σ/√n
```

**Explanation:** For large samples (n≥30), sample means follow a normal distribution regardless of the population distribution.

**Example:**
Population: μ = 50, σ = 12, sample size n = 36
- Mean of sample means = μ = 50
- Standard error = σ/√n = 12/√36 = 12/6 = 2
- Sample means follow N(50, 2²)

### **B. Z-Score for Sample Means**

**Formula:**
```
Z = (X̄ - μ)/(σ/√n)
```

**Explanation:** Tests how far a sample mean is from the population mean in terms of standard errors.

**Example:**
If X̄ = 53, μ = 50, σ = 12, n = 36:
- Z = (53 - 50)/(12/√36) = 3/2 = 1.5
- Sample mean is 1.5 standard errors above population mean

**Casio FX-991CW:** Calculate SE first: [12] [÷] [√] [36] [=], then Z-score

### **C. Critical Z-Values**

| Confidence Level | α | Z-value |
|------------------|---|---------|
| 90% | 0.10 | ±1.645 |
| 95% | 0.05 | ±1.96 |
| 99% | 0.01 | ±2.576 |

---

## 3. Central Limit Theorem & Z-Scores

### **A. Central Limit Theorem**

**Formula:**
```
X̄ ~ N(μ, σ²/n)
```

**Standard Error Formula:**
```
SE = σ/√n
```

**Where:**
- X̄ = Sample mean (random variable)
- ~ = "Follows" or "is distributed as"
- N(μ, σ²/n) = Normal distribution with mean μ and variance σ²/n
- μ = Population mean (center of sample mean distribution)
- σ² = Population variance
- n = Sample size
- σ²/n = Variance of sample mean distribution
- SE = Standard error (standard deviation of sample means)
- σ = Population standard deviation
- √n = Square root of sample size (reduces variability)

**Explanation:** For large samples (n≥30), sample means follow a normal distribution regardless of the original population distribution. Larger samples produce sample means closer to the population mean.

**Example:**
Population: μ = 50, σ = 12, sample size n = 36
- Mean of sample means = μ = 50
- Variance of sample means = σ²/n = 144/36 = 4
- Standard error = σ/√n = 12/√36 = 12/6 = 2
- Sample means follow N(50, 4) or equivalently N(50, 2²)

---

### **B. Z-Score for Sample Means**

**Formula:**
```
Z = (X̄ - μ)/(σ/√n)
```

**Alternative Form:**
```
Z = (X̄ - μ)/SE
```

**Where:**
- Z = Standardized score for sample mean
- X̄ = Observed sample mean
- μ = Expected population mean
- σ/√n = Standard error of the mean
- SE = Standard error (same as σ/√n)

**Explanation:** Tests how many standard errors a sample mean is away from the expected population mean. Used for hypothesis testing and confidence intervals.

**Example:**
If X̄ = 53, μ = 50, σ = 12, n = 36:
- SE = 12/√36 = 2
- Z = (53 - 50)/2 = 3/2 = 1.5
- Interpretation: Sample mean is 1.5 standard errors above the population mean

**Casio FX-991CW:** 
1. Calculate SE: [12][÷][√][36][=] → Store result [STO][A]
2. Calculate Z: [(][53][-][50][)][÷][RCL][A][=]

---

### **C. Critical Z-Values**

**Formula for Confidence Level:**
```
Confidence Level = (1 - α) × 100%
Z = Z(α/2)
```

**Where:**
- α = Significance level (probability of error)
- α/2 = Half of significance level (for two-tailed tests)
- Z(α/2) = Critical Z-value that leaves α/2 in each tail
- 1-α = Confidence coefficient

**Common Critical Values:**

| Confidence Level | α | α/2 | Z-value |
|------------------|---|-----|---------|
| 90% | 0.10 | 0.05 | ±1.645 |
| 95% | 0.05 | 0.025 | ±1.96 |
| 99% | 0.01 | 0.005 | ±2.576 |

**Explanation:** Critical values define the boundaries for confidence intervals and hypothesis tests. Higher confidence requires larger Z-values.

---

## 4. Measures of Central Tendency

### **A. Population Mean (μ) - DETAILED EXAMPLES**

**Formula:**
```
μ = Σx/N
```

**Where:**
- μ = Population mean (true average of entire population)
- Σx = Sum of all individual values in the population
- N = Total population size (number of all members)

**Explanation:** The arithmetic average of every single member in the complete population. This is a parameter (fixed value) that describes the population's center.

**Example 1: Simple Data Set**
**Data:** Test scores of 8 students: 85, 92, 78, 96, 88, 91, 83, 87

**Step-by-step Solution:**
1. **Identify the data:** N = 8 students (complete population)
2. **Sum all values:** Σx = 85 + 92 + 78 + 96 + 88 + 91 + 83 + 87 = 700
3. **Apply formula:** μ = Σx/N = 700/8 = 87.5
4. **Conclusion:** The population mean test score is 87.5 points

**Example 2: Grouped Data**
**Data:** Weekly sales data from all 5 company branches
| Branch | Sales ($000) |
|--------|--------------|
| A      | 45           |
| B      | 52           |
| C      | 38           |
| D      | 61           |
| E      | 49           |

**Step-by-step Solution:**
1. **Identify population:** N = 5 branches (all branches)
2. **Sum all values:** Σx = 45 + 52 + 38 + 61 + 49 = 245
3. **Apply formula:** μ = 245/5 = 49
4. **Conclusion:** The average weekly sales across all branches is $49,000

**Casio FX-991CW:** 
1. [MODE][3][1] (1-VAR statistics)
2. Enter each value: [85][=][92][=][78][=][96][=][88][=][91][=][83][=][87][=]
3. [SHIFT][1][1][=] → Shows mean = 87.5

### **B. Sample Mean (x̄) - DETAILED EXAMPLES**

**Formula:**
```
x̄ = Σx/n
```

**Where:**
- x̄ = Sample mean (average of sample data)
- Σx = Sum of all values in the sample
- n = Sample size (number of observations in sample)

**Explanation:** The arithmetic average of values in a sample, used to estimate the unknown population mean. This is a statistic (varies from sample to sample).

**Example 1: Customer Satisfaction Sample**
**Data:** Satisfaction scores from 6 randomly selected customers: 4.2, 3.8, 4.6, 4.1, 3.9, 4.4

**Step-by-step Solution:**
1. **Identify sample:** n = 6 customers (sample from larger customer base)
2. **Sum all values:** Σx = 4.2 + 3.8 + 4.6 + 4.1 + 3.9 + 4.4 = 25.0
3. **Apply formula:** x̄ = 25.0/6 = 4.17
4. **Conclusion:** The sample mean satisfaction score is 4.17/5.0

**Example 2: Quality Control Sample**
**Data:** Product weights (grams) from sample of 8 items: 502, 498, 505, 501, 499, 503, 500, 497

**Step-by-step Solution:**
1. **Identify sample:** n = 8 items (from production batch)
2. **Sum all values:** Σx = 502 + 498 + 505 + 501 + 499 + 503 + 500 + 497 = 4005
3. **Apply formula:** x̄ = 4005/8 = 500.625
4. **Conclusion:** The sample mean weight is 500.625 grams

**Note:** This sample mean (500.625g) estimates the population mean, but may differ from the true μ.

**Casio FX-991CW:** Same steps as population mean, result displays as x̄

### **C. Median - DETAILED EXAMPLES**

**Formula:**
```
For Odd n: Median = x((n+1)/2)
For Even n: Median = [x(n/2) + x(n/2+1)]/2
```

**Where:**
- n = Total number of data points
- x(position) = Value at the specified position in ordered data
- (n+1)/2 = Position of median when n is odd
- n/2 and (n/2)+1 = Positions of two middle values when n is even

**Explanation:** Median is the middle value that divides ordered data into two equal halves. For even numbers of values, take average of two middle values.

**Example 1: Odd Number of Values**
**Data:** Heights of 9 students (cm): 165, 170, 158, 180, 175, 162, 168, 172, 177

**Step-by-step Solution:**
1. **Arrange in ascending order:** 158, 162, 165, 168, 170, 172, 175, 177, 180
2. **Find position:** n = 9 (odd), so position = (9+1)/2 = 5th term
3. **Identify median:** The 5th value = 170
4. **Conclusion:** The median height is 170 cm

**Example 2: Even Number of Values**
**Data:** Monthly sales ($1000s): 45, 52, 38, 61, 49, 55, 42, 58

**Step-by-step Solution:**
1. **Arrange in ascending order:** 38, 42, 45, 49, 52, 55, 58, 61
2. **Find positions:** n = 8 (even), so positions = 4th and 5th terms
3. **Identify values:** 4th term = 49, 5th term = 52
4. **Calculate median:** (49 + 52)/2 = 101/2 = 50.5
5. **Conclusion:** The median monthly sales is $50,500

**Example 3: Grouped Data**
**Data:**
| Age Group | Frequency | Cumulative Frequency |
|-----------|-----------|---------------------|
| 20-30     | 8         | 8                   |
| 30-40     | 15        | 23                  |
| 40-50     | 20        | 43                  |
| 50-60     | 12        | 55                  |

**Formula for Grouped Data:**
```
Median = L + [(N/2 - CF)/f] × h
```

**Step-by-step Solution:**
1. **Find N/2:** N = 55, so N/2 = 27.5
2. **Locate median class:** 27.5 falls in 40-50 (CF = 43 > 27.5)
3. **Apply formula:** Median = L + [(N/2 - CF)/f] × h
   - L = 40 (lower boundary of median class)
   - CF = 23 (cumulative frequency before median class)
   - f = 20 (frequency of median class)
   - h = 10 (class width)
4. **Calculate:** Median = 40 + [(27.5 - 23)/20] × 10 = 40 + (4.5/20) × 10 = 40 + 2.25 = 42.25
5. **Conclusion:** The median age is 42.25 years

### **D. Mode - DETAILED EXAMPLES**

**Definition:** The value that appears most frequently in a dataset

**Example 1: Simple Data**
**Data:** Shoe sizes sold in one day: 7, 8, 9, 8, 10, 8, 7, 9, 8, 11

**Step-by-step Solution:**
1. **Count frequencies:**
   - Size 7: 2 times
   - Size 8: 4 times
   - Size 9: 2 times
   - Size 10: 1 time
   - Size 11: 1 time
2. **Identify highest frequency:** Size 8 appears 4 times (most frequent)
3. **Conclusion:** The mode is size 8 (unimodal distribution)

**Example 2: Multiple Modes**
**Data:** Product ratings: 3, 4, 5, 4, 3, 5, 2, 4, 3, 5

**Step-by-step Solution:**
1. **Count frequencies:**
   - Rating 2: 1 time
   - Rating 3: 3 times
   - Rating 4: 3 times
   - Rating 5: 3 times
2. **Identify highest frequencies:** Ratings 3, 4, and 5 each appear 3 times
3. **Conclusion:** The data is trimodal with modes at 3, 4, and 5

**Example 3: Grouped Data**
**Data:**
| Score Range | Frequency |
|-------------|-----------|
| 60-70       | 5         |
| 70-80       | 12        |
| 80-90       | 18        |
| 90-100      | 8         |

**Formula for Grouped Data:**
```
Mode = L + [(f₁-f₀)/(2f₁-f₀-f₂)] × h
```

**Where:**
- L = Lower boundary of the modal class
- f₁ = Frequency of the modal class (highest frequency)
- f₀ = Frequency of the class immediately before the modal class
- f₂ = Frequency of the class immediately after the modal class
- h = Class width of the modal class

**Step-by-step Solution:**
1. **Identify modal class:** 80-90 has highest frequency (18)
2. **Identify required values:**
   - L = 80 (lower boundary of modal class)
   - f₁ = 18 (frequency of modal class)
   - f₀ = 12 (frequency of class before modal class: 70-80)
   - f₂ = 8 (frequency of class after modal class: 90-100)
   - h = 10 (class width: 90-80)
3. **Apply formula:** Mode = L + [(f₁-f₀)/(2f₁-f₀-f₂)] × h
4. **Calculate:** Mode = 80 + [(18-12)/(2×18-12-8)] × 10
   - Mode = 80 + [6/(36-20)] × 10 
   - Mode = 80 + (6/16) × 10 
   - Mode = 80 + 3.75 = 83.75
5. **Conclusion:** The modal score is 83.75

### **COMPARISON EXAMPLE - ALL MEASURES TOGETHER**

**Data:** Daily temperatures (°F) for one week: 72, 75, 73, 78, 75, 74, 77

**Complete Analysis:**

**MEAN Calculation:**
1. **Sum all values:** 72 + 75 + 73 + 78 + 75 + 74 + 77 = 524
2. **Apply formula:** Mean = 524/7 = 74.86°F
3. **Interpretation:** Average temperature for the week

**MEDIAN Calculation:**
1. **Arrange in order:** 72, 73, 74, 75, 75, 77, 78
2. **Find position:** n = 7 (odd), position = (7+1)/2 = 4th term
3. **Identify median:** 4th value = 75°F
4. **Interpretation:** Middle temperature when arranged in order

**MODE Calculation:**
1. **Count frequencies:** 72(1), 73(1), 74(1), 75(2), 77(1), 78(1)
2. **Identify most frequent:** 75 appears twice (most frequent)
3. **Result:** Mode = 75°F
4. **Interpretation:** Most common temperature during the week

**SUMMARY COMPARISON:**
- **Mean = 74.86°F** (affected by all values, provides overall average)
- **Median = 75°F** (middle value, not affected by extremes)
- **Mode = 75°F** (most common temperature)

**Business Insights:**
- The mean (74.86°F) is slightly lower than median/mode due to the lower value (72°F)
- Median and mode being equal (75°F) suggests relatively symmetric distribution
- The small difference between all three measures indicates consistent temperatures
- Median = (7+12)/2 = 19/2 = 9.5

### **D. Mode**

**Explanation:** The most frequently occurring value in the dataset.

**Example:**
Data: 5, 7, 7, 8, 7, 9
- Mode = 7 (appears 3 times)

### **E. Geometric Mean**

**Formula:**
```
GM = ⁿ√(x₁ × x₂ × ... × xₙ)
GM = (∏xi)^(1/n)
```

**Explanation:** Used for growth rates, percentages, and ratios.

**Example:**
Growth rates: 10%, 20%, -5% → Convert to: 1.10, 1.20, 0.95
- GM = ∛(1.10 × 1.20 × 0.95) = ∛1.254 = 1.078
- Average growth rate = 7.8%

**Casio FX-991CW:** [1.10] [×] [1.20] [×] [0.95] [=] [SHIFT] [x^(1/y)] [3] [=]

### **F. Harmonic Mean**

**Formula:**
```
HM = n/Σ(1/xi)
```

**Explanation:** Used for rates and ratios (speed, prices per unit).

**Example:**
Speeds: 60 mph, 40 mph for equal distances
- HM = 2/(1/60 + 1/40) = 2/(0.0167 + 0.025) = 2/0.0417 = 48 mph

---

## 4. Measures of Central Tendency

### **A. Population Mean (μ)**

**Formula:**
```
μ = Σx/N
```

**Where:**
- μ = Population mean (true average of entire population)
- Σx = Sum of all individual values in the population
- N = Total population size (number of all members)

**Explanation:** The arithmetic average of every single member in the complete population. This is a parameter (fixed value) that describes the population's center.

**Example:**
Population data: 10, 15, 20, 25, 30
- Σx = 10+15+20+25+30 = 100
- N = 5 (all population members)
- μ = 100/5 = 20

**Casio FX-991CW:** 
1. [MODE][3][1] (1-VAR statistics)
2. Enter each value: [10][=][15][=][20][=][25][=][30][=]
3. [SHIFT][1][1][=] → Shows mean = 20

---

### **B. Sample Mean (x̄)**

**Formula:**
```
x̄ = Σx/n
```

**Where:**
- x̄ = Sample mean (average of sample data)
- Σx = Sum of all values in the sample
- n = Sample size (number of observations in sample)

**Explanation:** The arithmetic average of values in a sample, used to estimate the unknown population mean. This is a statistic (varies from sample to sample).

**Example:**
Sample data: 12, 18, 22, 28
- Σx = 12+18+22+28 = 80
- n = 4 (sample observations)
- x̄ = 80/4 = 20

**Note:** This sample mean (20) estimates the population mean, but may differ from the true μ.

---

### **C. Geometric Mean**

**Formula:**
```
GM = ⁿ√(x₁ × x₂ × ... × xₙ)
GM = (∏xi)^(1/n)
```

**Where:**
- GM = Geometric mean
- n = Number of values
- x₁, x₂, ..., xₙ = Individual data values (all must be positive)
- ∏xi = Product of all values (multiply all together)
- ⁿ√ = nth root
- 1/n = Reciprocal of sample size (fractional exponent)

**Explanation:** Used for growth rates, percentages, and ratios. Geometric mean is always less than or equal to arithmetic mean.

**Example:**
Growth rates: 10%, 20%, -5% → Convert to multipliers: 1.10, 1.20, 0.95
- Product = 1.10 × 1.20 × 0.95 = 1.254
- GM = ∛1.254 = (1.254)^(1/3) = 1.078
- Average growth rate = 1.078 - 1 = 0.078 = 7.8%

**Casio FX-991CW:** [1.10][×][1.20][×][0.95][=][SHIFT][x^(1/y)][3][=]

---

### **D. Harmonic Mean**

**Formula:**
```
HM = n/Σ(1/xi)
```

**Where:**
- HM = Harmonic mean
- n = Number of values
- xi = Individual data values (all must be positive)
- 1/xi = Reciprocal of each value
- Σ(1/xi) = Sum of all reciprocals

**Explanation:** Used for rates and ratios, especially when dealing with time, speed, or prices per unit. Harmonic mean is always less than geometric and arithmetic means.

**Example:**
Speeds for equal distances: 60 mph, 40 mph
- Reciprocals: 1/60 = 0.0167, 1/40 = 0.025
- Sum of reciprocals = 0.0167 + 0.025 = 0.0417
- HM = 2/0.0417 = 48 mph

**Interpretation:** Average speed for the entire trip is 48 mph, not 50 mph (arithmetic mean).

---

## 5. Measures of Variability

### **A. Population Variance (σ²)**

**Formula:**
```
σ² = Σ(x - μ)²/N

Alternative: σ² = [Σx² - (Σx)²/N]/N
```

**Explanation:** Measures how spread out the population data is around the mean.

**Example:**
Data: 2, 4, 6, 8 (μ = 5)
- σ² = [(2-5)² + (4-5)² + (6-5)² + (8-5)²]/4
- σ² = [9 + 1 + 1 + 9]/4 = 20/4 = 5

**Alternative method:**
- Σx = 20, Σx² = 120, N = 4
- σ² = [120 - (20)²/4]/4 = [120 - 100]/4 = 5

### **B. Sample Variance (s²)**

**Formula:**
```
s² = Σ(x - x̄)²/(n-1)

Alternative: s² = [Σx² - (Σx)²/n]/(n-1)
```

**Explanation:** Estimates population variance using sample data. Uses (n-1) for unbiased estimation.

**Example:**
Sample: 2, 4, 6, 8 (x̄ = 5)
- s² = [(2-5)² + (4-5)² + (6-5)² + (8-5)²]/(4-1)
- s² = [9 + 1 + 1 + 9]/3 = 20/3 = 6.67

**Casio FX-991CW:** After entering data, [SHIFT] [1] [4] [3] [=] → Shows σₙ₋₁ = √6.67 = 2.58

### **C. Population Standard Deviation (σ)**

**Formula:**
```
σ = √[Σ(x - μ)²/N]
```

**Explanation:** Square root of variance; measures spread in original units.

**Example:**
From previous variance example: σ = √5 = 2.24

### **D. Sample Standard Deviation (s)**

**Formula:**
```
s = √[Σ(x - x̄)²/(n-1)]
```

**Explanation:** Square root of sample variance; estimates population standard deviation.

**Example:**
From previous variance example: s = √6.67 = 2.58

### **E. Mean Deviation**

**Formula:**
```
MD = Σ|x - x̄|/n
```

**Explanation:** Average of absolute deviations from mean; less affected by extreme values.

**Example:**
Data: 2, 4, 6, 8 (x̄ = 5)
- MD = [|2-5| + |4-5| + |6-5| + |8-5|]/4
- MD = [3 + 1 + 1 + 3]/4 = 8/4 = 2

### **F. Coefficient of Variation**

**Formula:**
```
CV = (σ/μ) × 100%

For Sample: CV = (s/x̄) × 100%
```

**Explanation:** Relative measure of variability; useful for comparing different datasets.

**Example:**
Dataset A: μ = 50, σ = 10 → CV = (10/50) × 100% = 20%
Dataset B: μ = 200, σ = 30 → CV = (30/200) × 100% = 15%
Dataset B is relatively less variable despite higher absolute variation.

---

## 5. Measures of Variability

### **A. Population Variance (σ²)**

**Primary Formula:**
```
σ² = Σ(x - μ)²/N
```

**Computational Formula:**
```
σ² = [Σx² - (Σx)²/N]/N
```

**Where:**
- σ² = Population variance (measure of population spread)
- x = Individual data values
- μ = Population mean
- N = Population size
- (x - μ) = Deviation of each value from population mean
- (x - μ)² = Squared deviation (always positive)
- Σ(x - μ)² = Sum of all squared deviations
- Σx² = Sum of squared individual values
- (Σx)² = Square of the sum of all values

**Explanation:** Variance measures the average squared distance of data points from the mean. Squaring eliminates negative values and emphasizes larger deviations.

**Example:**
Data: 2, 4, 6, 8 (μ = 5)

Using Primary Formula:
| x | x-μ | (x-μ)² |
|---|-----|--------|
| 2 | -3  | 9      |
| 4 | -1  | 1      |
| 6 | 1   | 1      |
| 8 | 3   | 9      |
|**Total**|**-**|**20**|

σ² = 20/4 = 5

Using Computational Formula:
- Σx = 20, Σx² = 4+16+36+64 = 120, N = 4
- σ² = [120 - (20)²/4]/4 = [120 - 100]/4 = 5

---

### **B. Sample Variance (s²)**

**Primary Formula:**
```
s² = Σ(x - x̄)²/(n-1)
```

**Computational Formula:**
```
s² = [Σx² - (Σx)²/n]/(n-1)
```

**Where:**
- s² = Sample variance (estimate of population variance)
- x̄ = Sample mean
- n = Sample size
- (n-1) = Degrees of freedom (Bessel's correction)
- Σ(x - x̄)² = Sum of squared deviations from sample mean

**Explanation:** Uses (n-1) instead of n to provide an unbiased estimate of population variance. This corrects for the tendency of sample variance to underestimate population variance.

**Why (n-1)?** When we use the sample mean instead of the true population mean, we lose one degree of freedom because the deviations are constrained to sum to zero.

**Example:**
Same data: 2, 4, 6, 8 (x̄ = 5)
- Using same squared deviations: Σ(x-x̄)² = 20
- s² = 20/(4-1) = 20/3 = 6.67

**Note:** Sample variance (6.67) is larger than population variance (5.0) due to the (n-1) correction.

---

### **C. Standard Deviation**

**Population Standard Deviation:**
```
σ = √[Σ(x - μ)²/N]
```

**Sample Standard Deviation:**
```
s = √[Σ(x - x̄)²/(n-1)]
```

**Where:**
- σ = Population standard deviation
- s = Sample standard deviation
- √ = Square root (returns units to original scale)

**Explanation:** Standard deviation is the square root of variance, expressing spread in the same units as the original data. More intuitive than variance for interpretation.

**Example:**
From previous variance examples:
- Population SD: σ = √5 = 2.24
- Sample SD: s = √6.67 = 2.58

**Interpretation:** Data points typically deviate about 2.24 units from the population mean.

**Casio FX-991CW:** 
- Sample SD: [SHIFT][1][4][3][=] → Shows σₙ₋₁
- Population SD: [SHIFT][1][4][4][=] → Shows σₙ

---

### **D. Mean Deviation**

**Formula:**
```
MD = Σ|x - x̄|/n
```

**Where:**
- MD = Mean deviation (average absolute deviation)
- |x - x̄| = Absolute value of deviation from mean
- Σ|x - x̄| = Sum of absolute deviations (no squaring)
- n = Number of observations

**Explanation:** Average of absolute deviations from the mean. Less sensitive to extreme values than standard deviation because it doesn't square the deviations.

**Example:**
Data: 2, 4, 6, 8 (x̄ = 5)

| x | x-x̄ | |x-x̄| |
|---|-----|-------|
| 2 | -3  | 3     |
| 4 | -1  | 1     |
| 6 | 1   | 1     |
| 8 | 3   | 3     |
|**Total**|**-**|**8**|

MD = 8/4 = 2

**Comparison:** Mean deviation (2.0) is smaller than standard deviation (2.58) because squaring emphasizes larger deviations more.

---

### **E. Coefficient of Variation**

**Formula:**
```
CV = (σ/μ) × 100%

For Sample: CV = (s/x̄) × 100%
```

**Where:**
- CV = Coefficient of variation (relative variability)
- σ = Population standard deviation
- μ = Population mean
- s = Sample standard deviation
- x̄ = Sample mean
- 100% = Converts to percentage

**Explanation:** Expresses variability relative to the mean, allowing comparison between datasets with different units or scales. Higher CV indicates more relative variability.

**Example:**
Dataset A: μ = 50, σ = 10
- CV_A = (10/50) × 100% = 20%

Dataset B: μ = 200, σ = 30
- CV_B = (30/200) × 100% = 15%

**Interpretation:** Despite having higher absolute variability (σ = 30 vs 10), Dataset B is relatively less variable (15% vs 20%).

---

## 6. Measures of Dispersion

### **A. Range**

**Formula:**
```
Range = Maximum Value - Minimum Value
```

**Explanation:** Simplest measure of spread; difference between extreme values.

**Example:**
Data: 15, 23, 27, 31, 45
- Range = 45 - 15 = 30

### **B. Quartiles**

**Formulas:**
```
Q₁ position = (n+1) × 1/4
Q₂ position = (n+1) × 2/4 (Median)
Q₃ position = (n+1) × 3/4
```

**Explanation:** Divide data into four equal parts; Q2 is the median.

**Example:**
Data: 10, 15, 20, 25, 30, 35, 40 (n=7)
- Q₁ position = (7+1)/4 = 2nd value → Q₁ = 15
- Q₂ position = (7+1)/2 = 4th value → Q₂ = 25
- Q₃ position = 3(7+1)/4 = 6th value → Q₃ = 35

### **C. Interquartile Range (IQR)**

**Formula:**
```
IQR = Q₃ - Q₁
```

**Explanation:** Range of middle 50% of data; robust to outliers.

**Example:**
From previous example: IQR = 35 - 15 = 20

### **D. Outlier Detection**

**Formula:**
```
Lower Fence = Q₁ - 1.5 × IQR
Upper Fence = Q₃ + 1.5 × IQR
```

**Explanation:** Values beyond fences are potential outliers.

**Example:**
Q₁ = 15, Q₃ = 35, IQR = 20
- Lower Fence = 15 - 1.5(20) = 15 - 30 = -15
- Upper Fence = 35 + 1.5(20) = 35 + 30 = 65
- Any values < -15 or > 65 are outliers

---

## 6. Measures of Dispersion

### **A. Range**

**Formula:**
```
Range = Maximum Value - Minimum Value
```

**Where:**
- Maximum Value = Largest observation in the dataset
- Minimum Value = Smallest observation in the dataset
- Range = Total spread from lowest to highest value

**Explanation:** Simplest measure of spread, showing the total span of data. However, it's sensitive to outliers and ignores the distribution of values between extremes.

**Example:**
Data: 15, 23, 27, 31, 45
- Maximum = 45
- Minimum = 15
- Range = 45 - 15 = 30

**Limitation:** If data were 15, 23, 27, 31, 100, range would be 85, but this doesn't reflect that most data is clustered between 15-31.

---

### **B. Quartiles**

**Position Formulas:**
```
Q₁ position = (n+1) × 1/4
Q₂ position = (n+1) × 2/4
Q₃ position = (n+1) × 3/4
```

**Where:**
- Q₁ = First quartile (25th percentile)
- Q₂ = Second quartile (median, 50th percentile)
- Q₃ = Third quartile (75th percentile)
- n = Number of observations
- (n+1) = Ensures proper positioning in ordered data
- 1/4, 2/4, 3/4 = Fractions dividing data into quarters

**Explanation:** Quartiles divide ordered data into four equal parts. 25% of data falls below Q₁, 50% below Q₂, and 75% below Q₃.

**Example:**
Data: 10, 15, 20, 25, 30, 35, 40 (n = 7)
- Q₁ position = (7+1) × 1/4 = 2nd value → Q₁ = 15
- Q₂ position = (7+1) × 2/4 = 4th value → Q₂ = 25 (median)
- Q₃ position = (7+1) × 3/4 = 6th value → Q₃ = 35

**Interpretation:** 25% of values ≤ 15, 50% ≤ 25, 75% ≤ 35

---

### **C. Interquartile Range (IQR)**

**Formula:**
```
IQR = Q₃ - Q₁
```

**Where:**
- IQR = Interquartile range (middle 50% spread)
- Q₃ = Third quartile (75th percentile)
- Q₁ = First quartile (25th percentile)

**Explanation:** Measures the spread of the middle 50% of data, making it robust to outliers. IQR contains the central half of all observations.

**Example:**
From previous quartile example:
- Q₃ = 35, Q₁ = 15
- IQR = 35 - 15 = 20

**Interpretation:** The middle 50% of data spans 20 units, from 15 to 35.

**Advantage:** Unlike range, IQR is not affected by extreme values in the first and fourth quartiles.

---

### **D. Outlier Detection**

**Fence Formulas:**
```
Lower Fence = Q₁ - 1.5 × IQR
Upper Fence = Q₃ + 1.5 × IQR
```

**Outlier Criteria:**
```
Outlier if: x < Lower Fence OR x > Upper Fence
```

**Where:**
- Lower Fence = Boundary below which values are considered outliers
- Upper Fence = Boundary above which values are considered outliers
- 1.5 = Standard multiplier (Tukey's criterion)
- 1.5 × IQR = Extension beyond quartiles to define "unusual" values

**Explanation:** Values beyond these fences are considered unusually far from the central data cluster. The 1.5 × IQR rule is a standard convention.

**Example:**
Using previous data: Q₁ = 15, Q₃ = 35, IQR = 20
- Lower Fence = 15 - 1.5(20) = 15 - 30 = -15
- Upper Fence = 35 + 1.5(20) = 35 + 30 = 65

**Outlier Assessment:**
Any value < -15 or > 65 would be considered an outlier.
For data: 10, 15, 20, 25, 30, 35, 40
- All values fall between -15 and 65 → No outliers detected

**Example with Outlier:**
If data included value 80: Since 80 > 65, it would be flagged as an outlier.

---

### **E. Box Plot (Five-Number Summary)**

**Components:**
```
Five-Number Summary: Min, Q₁, Median, Q₃, Max
```

**Where:**
- Min = Minimum value (excluding outliers)
- Q₁ = First quartile
- Median = Second quartile (Q₂)
- Q₃ = Third quartile
- Max = Maximum value (excluding outliers)

**Explanation:** Box plots visually display the five-number summary, showing data distribution, central tendency, spread, and outliers in a single graph.

**Example:**
Data: 10, 15, 20, 25, 30, 35, 40
- Min = 10, Q₁ = 15, Median = 25, Q₃ = 35, Max = 40
- Box extends from Q₁ to Q₃ (the IQR)
- Line in box shows median position
- Whiskers extend to Min and Max (if no outliers)

---

## 7. Sampling Methods

### **A. Simple Random Sampling**

**Formula:**
```
P(selecting specific sample) = 1/C(N,n)

Where C(N,n) = N!/(n!(N-n)!)
```

**Explanation:** Every possible sample has equal probability of selection.

**Example:**
Population of 10, sample of 3:
- Total possible samples = C(10,3) = 10!/(3!×7!) = 120
- Probability of any specific sample = 1/120 = 0.0083

### **B. Sample Size Calculation**

**Formula:**
```
n = (Z²α/2 × σ²)/E²

Where E = Margin of Error
```

**Explanation:** Determines required sample size for desired precision.

**Example:**
Want 95% confidence, σ = 10, margin of error = 2:
- n = (1.96² × 10²)/2² = (3.84 × 100)/4 = 96 samples needed

---

## 7. Sampling Methods

### **A. Simple Random Sampling**

**Probability Formula:**
```
P(selecting specific sample) = 1/C(N,n)
```

**Combination Formula:**
```
C(N,n) = N!/(n!(N-n)!)
```

**Where:**
- P = Probability of selecting any specific sample
- C(N,n) = Number of possible combinations
- N = Population size (total number of units)
- n = Sample size (number of units to select)
- N! = N factorial (N × (N-1) × (N-2) × ... × 1)
- n! = n factorial
- (N-n)! = Factorial of the difference

**Explanation:** Every possible sample of size n has an equal probability of being selected. This ensures unbiased representation of the population.

**Example:**
Population of 10 students, sample of 3:
- Total possible samples = C(10,3) = 10!/(3! × 7!)
- C(10,3) = (10 × 9 × 8)/(3 × 2 × 1) = 720/6 = 120
- Probability of any specific sample = 1/120 = 0.0083 or 0.83%

**Interpretation:** Each possible combination of 3 students has a 0.83% chance of being selected.

---

### **B. Sample Size Calculation**

**Formula for Mean Estimation:**
```
n = (Z²(α/2) × σ²)/E²
```

**Where:**
- n = Required sample size
- Z(α/2) = Critical Z-value for desired confidence level
- α = Significance level (1 - confidence level)
- σ² = Population variance
- σ = Population standard deviation
- E = Margin of error (maximum acceptable difference from true mean)
- E² = Squared margin of error

**Explanation:** Determines the minimum sample size needed to estimate the population mean with specified precision and confidence.

**Example:**
Want 95% confidence, σ = 10, margin of error = 2:
- Confidence level = 95% → α = 0.05 → Z(0.025) = 1.96
- n = (1.96² × 10²)/2²
- n = (3.8416 × 100)/4 = 384.16/4 = 96.04
- Required sample size = 97 (round up to next integer)

**Interpretation:** Need at least 97 observations to be 95% confident that sample mean is within ±2 units of true population mean.

---

### **C. Confidence Interval for Mean**

**Formula:**
```
CI = x̄ ± Z(α/2) × (σ/√n)
```

**Margin of Error Formula:**
```
ME = Z(α/2) × (σ/√n)
```

**Where:**
- CI = Confidence interval
- x̄ = Sample mean
- ± = Plus or minus (creates interval)
- Z(α/2) = Critical value for desired confidence level
- σ/√n = Standard error of the mean
- ME = Margin of error (half-width of interval)

**Explanation:** Provides a range of plausible values for the population mean based on sample data. Higher confidence requires wider intervals.

**Example:**
Sample: x̄ = 52, σ = 8, n = 64, want 95% confidence
- Standard error = 8/√64 = 8/8 = 1
- Z(0.025) = 1.96
- ME = 1.96 × 1 = 1.96
- CI = 52 ± 1.96 = [50.04, 53.96]

**Interpretation:** We are 95% confident that the true population mean lies between 50.04 and 53.96.

---

## 8. Calculator Functions (Casio FX-991CW)

### **Statistical Mode Setup**
1. [MODE] [STAT] [1-VAR] for single variable
2. Enter data: [value] [=] for each data point
3. [AC] to clear current calculation (keeps data)
4. [SHIFT] [9] [3] [=] to clear all data

### **Key Statistical Functions**
| Function | Key Sequence | Output |
|----------|--------------|--------|
| Sample Mean | [SHIFT] [1] [4] [2] [=] | x̄ |
| Sample Std Dev | [SHIFT] [1] [4] [3] [=] | σₙ₋₁ |
| Population Std Dev | [SHIFT] [1] [4] [4] [=] | σₙ |
| Sample Size | [SHIFT] [1] [4] [1] [=] | n |
| Sum of x | [SHIFT] [1] [4] [5] [=] | Σx |
| Sum of x² | [SHIFT] [1] [4] [6] [=] | Σx² |

### **Random Number Generation**
- [SHIFT] [RAN#] [=] → Generates random decimal (0-1)
- [RAN#] [×] [100] [=] → Random percentage (0-100)

---

## 8. Calculator Functions (Casio FX-991CW)

### **Statistical Mode Setup**

**Mode Selection:**
```
[MODE] → [3] → [1] (1-VAR Statistics)
```

**Where:**
- [MODE] = Access calculator's different operating modes
- [3] = Statistics mode menu
- [1] = Single variable statistics (1-VAR)

**Data Entry Methods:**

**Method 1: Individual Values**
```
[value] [=] for each data point
```

**Method 2: Value with Frequency**
```
[value] [×] [frequency] [=]
```

**Example:**
For data: 2, 2, 2, 4, 4, 6
- Method 1: [2][=][2][=][2][=][4][=][4][=][6][=]
- Method 2: [2][×][3][=][4][×][2][=][6][×][1][=]

---

### **Key Statistical Functions**

| **Function** | **Key Sequence** | **Symbol** | **Meaning** |
|--------------|------------------|------------|-------------|
| **Sample Size** | [SHIFT][1][1][=] | n | Number of data points |
| **Sample Mean** | [SHIFT][1][2][=] | x̄ | Arithmetic average |
| **Sample Std Dev** | [SHIFT][1][3][=] | σₙ₋₁ | Standard deviation (n-1) |
| **Population Std Dev** | [SHIFT][1][4][=] | σₙ | Standard deviation (n) |
| **Sum of Values** | [SHIFT][1][5][=] | Σx | Total of all values |
| **Sum of Squares** | [SHIFT][1][6][=] | Σx² | Sum of squared values |

**Explanation:**
- **σₙ₋₁**: Use for sample data (divides by n-1)
- **σₙ**: Use for population data (divides by n)
- **Σx**: Useful for checking data entry accuracy
- **Σx²**: Needed for manual variance calculations

---

### **Memory Functions for Complex Calculations**

**Storing Values:**
```
[result] [STO] [variable] = Store in memory
[RCL] [variable] = Recall from memory
```

**Available Variables:** A, B, C, D, E, F, X, Y, M

**Example - Z-Score Calculation:**
```
Step 1: Calculate and store mean
[SHIFT][1][2][=] [STO][A]

Step 2: Calculate and store standard deviation  
[SHIFT][1][3][=] [STO][B]

Step 3: Calculate Z-score for value x
([value] - [RCL][A]) ÷ [RCL][B] [=]
```

---

### **Clearing Functions**

| **Purpose** | **Key Sequence** | **Effect** |
|-------------|------------------|-----------|
| **Clear calculation** | [AC] | Clears current calculation, keeps data |
| **Clear all data** | [SHIFT][9][3][=] | Removes all statistical data |
| **Clear memory** | [SHIFT][9][2][=] | Clears all stored variables |

**Important:** Always clear data before starting new problems to avoid mixing datasets.

---

### **Random Number Generation**

**Basic Random Number:**
```
[SHIFT] [RAN#] [=]
```
**Output:** Random decimal between 0 and 1

**Random Percentage:**
```
[RAN#] [×] [100] [=]
```
**Output:** Random number between 0 and 100

**Random Integer in Range:**
```
[RAN#] [×] [range] [+] [minimum] [=]
```

**Example:** Random integer from 1 to 10:
```
[RAN#] [×] [10] [+] [1] [=]
```

---

### **Error Prevention Tips**

**Before Calculation:**
1. ✅ Clear previous data: [SHIFT][9][3][=]
2. ✅ Set correct mode: [MODE][3][1]
3. ✅ Check display shows "1-VAR"

**During Data Entry:**
1. ✅ Verify data entry with [SHIFT][1][5][=] (sum check)
2. ✅ Check sample size with [SHIFT][1][1][=]
3. ✅ Use [AC] to clear mistakes, not [SHIFT][9][3]

**After Calculation:**
1. ✅ Verify results make sense given data
2. ✅ Check units match original data
3. ✅ Cross-verify critical calculations manually

---

## 9. Quick Reference Tables

### **📊 Complete Formula Summary by Data Type**

| **Statistic** | **Ungrouped** | **Ungrouped + Freq** | **Grouped Data** |
|---------------|---------------|---------------------|------------------|
| **Mean** | x̄ = Σx/n | x̄ = Σ(fx)/Σf | x̄ = Σ(fx)/Σf |
| **Median** | Position (n+1)/2 | Cumulative frequency | L + [(n/2-CF)/f] × h |
| **Mode** | Most frequent value | Value with max frequency | L + [(f₁-f₀)/(2f₁-f₀-f₂)] × h |
| **Std Dev** | √[Σ(x-x̄)²/(n-1)] | √[Σf(x-x̄)²/Σf] | √[Σf(x-x̄)²/Σf] |

---

### **Population vs Sample Formulas**

| **Measure** | **Population** | **Sample** | **Key Difference** |
|-------------|----------------|------------|-------------------|
| **Mean** | μ = Σx/N | x̄ = Σx/n | Parameter vs Statistic |
| **Variance** | σ² = Σ(x-μ)²/N | s² = Σ(x-x̄)²/(n-1) | N vs (n-1) denominator |
| **Std Dev** | σ = √[Σ(x-μ)²/N] | s = √[Σ(x-x̄)²/(n-1)] | Bessel's correction |
| **Purpose** | Describes population | Estimates population | Fixed vs Variable |

**Key Insight:** Sample statistics use (n-1) to provide unbiased estimates of population parameters.

---

### **When to Use Each Type of Mean**

| **Mean Type** | **Formula** | **Best Used For** | **Example Applications** |
|---------------|-------------|-------------------|-------------------------|
| **Arithmetic** | Σx/n | General average | Test scores, heights, temperatures |
| **Geometric** | ⁿ√(x₁×x₂×...×xₙ) | Growth rates, ratios | Investment returns, population growth |
| **Harmonic** | n/Σ(1/x) | Rates, speeds | Average speed, price per unit |

**Selection Rule:** 
- Arithmetic: Most common situations
- Geometric: When dealing with percentages or multiplicative processes
- Harmonic: When averaging rates or ratios

---

### **Normal Distribution Properties**

| **Range** | **Percentage of Data** | **Z-Score Range** |
|-----------|------------------------|-------------------|
| μ ± 1σ | 68.27% | -1.00 to +1.00 |
| μ ± 2σ | 95.45% | -2.00 to +2.00 |
| μ ± 3σ | 99.73% | -3.00 to +3.00 |

**Empirical Rule:** Nearly all data (99.7%) falls within 3 standard deviations of the mean.

---

### **Critical Z-Values for Confidence Intervals**

| **Confidence Level** | **α** | **α/2** | **Z-Value** | **Usage** |
|---------------------|-------|---------|-------------|-----------|
| 90% | 0.10 | 0.05 | ±1.645 | Less precision, narrower interval |
| 95% | 0.05 | 0.025 | ±1.96 | Standard choice for most studies |
| 99% | 0.01 | 0.005 | ±2.576 | High precision, wider interval |
| 99.9% | 0.001 | 0.0005 | ±3.291 | Very high precision |

**Trade-off:** Higher confidence requires wider intervals (less precision).

---

### **Measures of Spread Comparison**

| **Measure** | **Formula** | **Advantages** | **Disadvantages** |
|-------------|-------------|----------------|-------------------|
| **Range** | Max - Min | Simple to calculate | Sensitive to outliers |
| **IQR** | Q₃ - Q₁ | Robust to outliers | Ignores tails of distribution |
| **Variance** | Σ(x-μ)²/N | Uses all data points | Units are squared |
| **Std Dev** | √Variance | Same units as data | Sensitive to outliers |
| **CV** | (σ/μ) × 100% | Relative measure | Requires positive mean |

**Selection Guide:**
- **Range**: Quick assessment, small datasets
- **IQR**: Skewed data, presence of outliers
- **Standard Deviation**: Normal data, detailed analysis
- **CV**: Comparing different scales or units

---

### **Data Type Identification Guide**

| **Data Characteristics** | **Type** | **Formula Set to Use** |
|-------------------------|----------|------------------------|
| Individual values listed | Ungrouped | Basic formulas (Σx/n) |
| Values with frequencies | Ungrouped + Freq | Weighted formulas (Σfx/Σf) |
| Class intervals given | Grouped | Midpoint formulas |
| Complete population | Population | Use N, μ, σ |
| Sample from population | Sample | Use n, x̄, s |

---

### **Calculator Function Quick Access**

| **Need** | **Key Sequence** | **When to Use** |
|----------|------------------|-----------------|
| **Enter Mode** | [MODE][3][1] | Start any statistical calculation |
| **Clear Data** | [SHIFT][9][3][=] | Between different problems |
| **Sample Mean** | [SHIFT][1][2][=] | Most common average |
| **Sample SD** | [SHIFT][1][3][=] | Estimating population spread |
| **Population SD** | [SHIFT][1][4][=] | Known population data |
| **Data Count** | [SHIFT][1][1][=] | Verify data entry |

---

## 📚 **COMPREHENSIVE EXAM CHECKLIST**

### **Problem-Solving Strategy**

**Step 1: Identify Data Type**
- ✅ Individual values → Ungrouped
- ✅ Values with frequencies → Ungrouped with frequency
- ✅ Class intervals → Grouped data
- ✅ Sample or population? → Choose appropriate formulas

**Step 2: Choose Appropriate Measure**
- ✅ Central tendency: Mean, median, or mode?
- ✅ Variability: Range, IQR, standard deviation, or CV?
- ✅ Position: Quartiles, percentiles, or Z-scores?

**Step 3: Calculator Setup**
- ✅ Clear previous data: [SHIFT][9][3][=]
- ✅ Set statistics mode: [MODE][3][1]
- ✅ Verify correct mode displayed

**Step 4: Execute Calculation**
- ✅ Enter data systematically
- ✅ Double-check critical values
- ✅ Use appropriate formula or function

**Step 5: Interpret Results**
- ✅ Check reasonableness of answer
- ✅ Include proper units
- ✅ State conclusion in context
- ✅ Consider practical implications

---

### **Common Error Prevention**

**Data Entry Errors:**
- ✅ Count data points after entry
- ✅ Verify sum matches expected value
- ✅ Check for typos in large numbers

**Formula Selection Errors:**
- ✅ Population (N) vs Sample (n-1) denominators
- ✅ Grouped data requires midpoints
- ✅ Frequency data needs weighted formulas

**Interpretation Errors:**
- ✅ Units match original data
- ✅ Sample statistics estimate population parameters
- ✅ Confidence intervals provide ranges, not exact values

---

**💡 Master Strategy:**
1. **Understand the context** before choosing formulas
2. **Practice with your calculator** until functions become automatic
3. **Always verify** results make practical sense
4. **Interpret statistically** and **explain practically**
5. **Check your work** using alternative methods when possible

---

*This complete guide provides all essential statistical formulas with detailed explanations of every component. Master these concepts and you'll excel in any statistics application!* 📊✨
