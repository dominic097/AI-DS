# IFS LLT Assignment 2025 - ANSWER SHEET

---

## UNIT 1

### Question 1
**A company wants to evaluate the performance of two teams (Team X and Team Y). The performance score is measured on a scale from 1 to 100, and productivity data for 6 employees from each team is provided below.**

**Data:**
- Team X: 88, 92, 85, 79, 90, 95
- Team Y: 82, 75, 78, 80, 70, 85

**(Note: consider it as population data)**

---

#### i. Calculate the mean, median, and mode (if any) for both teams

**TEAM X:**

**Mean (μ):**
**Formula:** μ = Σx / N

**Step-by-step:**
```
μ = (88 + 92 + 85 + 79 + 90 + 95) / 6
μ = 529 / 6
μ = 88.17
```
**Mean for Team X = 88.17**

**Median:**
**Formula:** For even n, Median = (n/2 term + (n/2 + 1) term) / 2

**Step-by-step:**
1. Arrange in ascending order: 79, 85, 88, 90, 92, 95
2. n = 6 (even)
3. Median = (3rd term + 4th term) / 2
4. Median = (88 + 90) / 2 = 178 / 2 = 89

**Median for Team X = 89**

**Mode:**
- No repeated values
**Mode for Team X = No mode**

---

**TEAM Y:**

**Mean (μ):**
**Formula:** μ = Σx / N

**Step-by-step:**
```
μ = (82 + 75 + 78 + 80 + 70 + 85) / 6
μ = 470 / 6
μ = 78.33
```
**Mean for Team Y = 78.33**

**Median:**
**Step-by-step:**
1. Arrange in ascending order: 70, 75, 78, 80, 82, 85
2. n = 6 (even)
3. Median = (3rd term + 4th term) / 2
4. Median = (78 + 80) / 2 = 158 / 2 = 79

**Median for Team Y = 79**

**Mode:**
- No repeated values
**Mode for Team Y = No mode**

---

#### ii. Compute the range, variance, standard deviation, coefficient of variation

**TEAM X:**

**Range:**
**Formula:** Range = Maximum - Minimum

**Step-by-step:**
```
Range = 95 - 79
Range = 16
```
**Range for Team X = 16**

**Variance (σ²):**
**Formula (Population):** σ² = Σ(x - μ)² / N

**Step-by-step:**

| x | (x - μ) | (x - μ)² |
|---|---------|----------|
| 88 | -0.17 | 0.03 |
| 92 | 3.83 | 14.67 |
| 85 | -3.17 | 10.05 |
| 79 | -9.17 | 84.09 |
| 90 | 1.83 | 3.35 |
| 95 | 6.83 | 46.65 |
| **Sum** | | **158.84** |

```
σ² = 158.84 / 6
σ² = 26.47
```
**Variance for Team X = 26.47**

**Standard Deviation (σ):**
**Formula:** σ = √σ²

**Step-by-step:**
```
σ = √26.47
σ = 5.14
```
**Standard Deviation for Team X = 5.14**

**Coefficient of Variation (CV):**
**Formula:** CV = (σ / μ) × 100

**Step-by-step:**
```
CV = (5.14 / 88.17) × 100
CV = 0.0583 × 100
CV = 5.83%
```
**CV for Team X = 5.83%**

---

**TEAM Y:**

**Range:**
```
Range = 85 - 70
Range = 15
```
**Range for Team Y = 15**

**Variance (σ²):**

| x | (x - μ) | (x - μ)² |
|---|---------|----------|
| 82 | 3.67 | 13.47 |
| 75 | -3.33 | 11.09 |
| 78 | -0.33 | 0.11 |
| 80 | 1.67 | 2.79 |
| 70 | -8.33 | 69.39 |
| 85 | 6.67 | 44.49 |
| **Sum** | | **141.34** |

```
σ² = 141.34 / 6
σ² = 23.56
```
**Variance for Team Y = 23.56**

**Standard Deviation (σ):**
```
σ = √23.56
σ = 4.85
```
**Standard Deviation for Team Y = 4.85**

**Coefficient of Variation (CV):**
```
CV = (4.85 / 78.33) × 100
CV = 0.0619 × 100
CV = 6.19%
```
**CV for Team Y = 6.19%**

---

#### iii. Which team shows higher consistency? Provide statistical justification.

**Answer:**

**Statistical Comparison:**

| Measure | Team X | Team Y |
|---------|--------|--------|
| Standard Deviation | 5.14 | 4.85 |
| Coefficient of Variation | 5.83% | 6.19% |

**Conclusion:**

**Team X shows higher consistency** in employee performance.

**Justification:**
1. **Coefficient of Variation (CV)** is the most appropriate measure for comparing consistency between datasets with different means.
2. Team X has a **lower CV (5.83%)** compared to Team Y (6.19%)
3. A lower CV indicates **less relative variability** and therefore **greater consistency**
4. Although Team Y has a slightly lower standard deviation (4.85 vs 5.14), this is misleading because Team Y also has a lower mean (78.33 vs 88.17)
5. When we account for the mean through CV, Team X demonstrates more consistent performance relative to its average performance level

**Statistical Interpretation:** Team X's employees perform more consistently around their mean performance score of 88.17, with only 5.83% relative variation, making their performance more predictable and reliable.

---

#### iv. Find skewness and kurtosis for given data

**TEAM X:**

**Skewness:**
**Formula (Pearson's Coefficient):** SK = 3(Mean - Median) / SD

**Step-by-step:**
```
SK = 3(88.17 - 89) / 5.14
SK = 3(-0.83) / 5.14
SK = -2.49 / 5.14
SK = -0.48
```
**Skewness for Team X = -0.48** (Slightly negatively skewed)

**Interpretation:** The distribution is slightly skewed to the left, meaning there are slightly more lower values pulling the mean below the median.

**Kurtosis (using moment coefficient):**
**Formula:** Kurtosis = Σ(x - μ)⁴ / (N × σ⁴)

**Step-by-step:**

| x | (x - μ)⁴ |
|---|----------|
| 88 | 0.001 |
| 92 | 215.17 |
| 85 | 101.00 |
| 79 | 7071.03 |
| 90 | 11.22 |
| 95 | 2176.22 |
| **Sum** | **9574.65** |

```
Kurtosis = 9574.65 / (6 × 26.47²)
Kurtosis = 9574.65 / (6 × 700.66)
Kurtosis = 9574.65 / 4203.96
Kurtosis = 2.28
```
**Kurtosis for Team X = 2.28** (Platykurtic - flatter than normal distribution)

---

**TEAM Y:**

**Skewness:**
```
SK = 3(78.33 - 79) / 4.85
SK = 3(-0.67) / 4.85
SK = -2.01 / 4.85
SK = -0.41
```
**Skewness for Team Y = -0.41** (Slightly negatively skewed)

**Kurtosis:**

| x | (x - μ)⁴ |
|---|----------|
| 82 | 181.35 |
| 75 | 122.98 |
| 78 | 0.01 |
| 80 | 7.78 |
| 70 | 4815.06 |
| 85 | 1979.39 |
| **Sum** | **7106.57** |

```
Kurtosis = 7106.57 / (6 × 23.56²)
Kurtosis = 7106.57 / (6 × 555.07)
Kurtosis = 7106.57 / 3330.42
Kurtosis = 2.13
```
**Kurtosis for Team Y = 2.13** (Platykurtic)

---

### Question 2
**A school psychologist is examining the effects of two factors, "Study Hours" and "Sleep Duration," on students' "Exam Scores."**

**Data:**

| Individual | Study Hours | Sleep Duration (hours) | Exam Score (%) |
|------------|-------------|------------------------|----------------|
| 1 | 10 | 7 | 85 |
| 2 | 8 | 6 | 78 |
| 3 | 12 | 5 | 90 |
| 4 | 6 | 8 | 74 |
| 5 | 9 | 6 | 80 |

---

#### a) Compute mean, median, mode, range, variance, and standard deviation for both independent variables

**STUDY HOURS:**

**Mean:**
**Formula:** μ = Σx / N

**Step-by-step:**
```
μ = (10 + 8 + 12 + 6 + 9) / 5
μ = 45 / 5
μ = 9
```
**Mean Study Hours = 9 hours**

**Median:**
**Step-by-step:**
1. Arrange: 6, 8, 9, 10, 12
2. n = 5 (odd)
3. Median = Middle value = 3rd term = 9

**Median Study Hours = 9 hours**

**Mode:**
- No repeated values
**Mode = No mode**

**Range:**
```
Range = 12 - 6 = 6
```
**Range = 6 hours**

**Variance (σ²):**
**Formula:** σ² = Σ(x - μ)² / N

| x | (x - μ) | (x - μ)² |
|---|---------|----------|
| 10 | 1 | 1 |
| 8 | -1 | 1 |
| 12 | 3 | 9 |
| 6 | -3 | 9 |
| 9 | 0 | 0 |
| **Sum** | | **20** |

```
σ² = 20 / 5 = 4
```
**Variance = 4**

**Standard Deviation:**
```
σ = √4 = 2
```
**Standard Deviation = 2 hours**

---

**SLEEP DURATION:**

**Mean:**
```
μ = (7 + 6 + 5 + 8 + 6) / 5
μ = 32 / 5
μ = 6.4
```
**Mean Sleep Duration = 6.4 hours**

**Median:**
1. Arrange: 5, 6, 6, 7, 8
2. Median = 6

**Median = 6 hours**

**Mode:**
- 6 appears twice
**Mode = 6 hours**

**Range:**
```
Range = 8 - 5 = 3
```
**Range = 3 hours**

**Variance:**

| x | (x - μ) | (x - μ)² |
|---|---------|----------|
| 7 | 0.6 | 0.36 |
| 6 | -0.4 | 0.16 |
| 5 | -1.4 | 1.96 |
| 8 | 1.6 | 2.56 |
| 6 | -0.4 | 0.16 |
| **Sum** | | **5.20** |

```
σ² = 5.20 / 5 = 1.04
```
**Variance = 1.04**

**Standard Deviation:**
```
σ = √1.04 = 1.02
```
**Standard Deviation = 1.02 hours**

---

**EXAM SCORE:**

**Mean:**
```
μ = (85 + 78 + 90 + 74 + 80) / 5
μ = 407 / 5
μ = 81.4
```
**Mean Exam Score = 81.4%**

**Median:**
1. Arrange: 74, 78, 80, 85, 90
2. Median = 80

**Median = 80%**

**Mode:**
- No repeated values
**Mode = No mode**

**Range:**
```
Range = 90 - 74 = 16
```
**Range = 16%**

**Variance:**

| x | (x - μ) | (x - μ)² |
|---|---------|----------|
| 85 | 3.6 | 12.96 |
| 78 | -3.4 | 11.56 |
| 90 | 8.6 | 73.96 |
| 74 | -7.4 | 54.76 |
| 80 | -1.4 | 1.96 |
| **Sum** | | **155.20** |

```
σ² = 155.20 / 5 = 31.04
```
**Variance = 31.04**

**Standard Deviation:**
```
σ = √31.04 = 5.57
```
**Standard Deviation = 5.57%**

---

#### b) Determine which independent variable has a stronger relationship with Exam Scores

**METHOD: Correlation Coefficient (Pearson's r)**

**Formula:** r = Σ[(x - x̄)(y - ȳ)] / √[Σ(x - x̄)² × Σ(y - ȳ)²]

---

**CORRELATION: Study Hours vs Exam Score**

| Study Hours (x) | Exam Score (y) | (x - x̄) | (y - ȳ) | (x - x̄)(y - ȳ) | (x - x̄)² | (y - ȳ)² |
|----------------|----------------|----------|----------|------------------|-----------|-----------|
| 10 | 85 | 1 | 3.6 | 3.6 | 1 | 12.96 |
| 8 | 78 | -1 | -3.4 | 3.4 | 1 | 11.56 |
| 12 | 90 | 3 | 8.6 | 25.8 | 9 | 73.96 |
| 6 | 74 | -3 | -7.4 | 22.2 | 9 | 54.76 |
| 9 | 80 | 0 | -1.4 | 0 | 0 | 1.96 |
| **Sum** | | | | **55** | **20** | **155.20** |

**Step-by-step:**
```
r = 55 / √(20 × 155.20)
r = 55 / √3104
r = 55 / 55.71
r = 0.987
```
**Correlation (Study Hours vs Exam Score) = 0.987** (Very strong positive correlation)

---

**CORRELATION: Sleep Duration vs Exam Score**

| Sleep (x) | Exam Score (y) | (x - x̄) | (y - ȳ) | (x - x̄)(y - ȳ) | (x - x̄)² | (y - ȳ)² |
|-----------|----------------|----------|----------|------------------|-----------|-----------|
| 7 | 85 | 0.6 | 3.6 | 2.16 | 0.36 | 12.96 |
| 6 | 78 | -0.4 | -3.4 | 1.36 | 0.16 | 11.56 |
| 5 | 90 | -1.4 | 8.6 | -12.04 | 1.96 | 73.96 |
| 8 | 74 | 1.6 | -7.4 | -11.84 | 2.56 | 54.76 |
| 6 | 80 | -0.4 | -1.4 | 0.56 | 0.16 | 1.96 |
| **Sum** | | | | **-19.8** | **5.20** | **155.20** |

**Step-by-step:**
```
r = -19.8 / √(5.20 × 155.20)
r = -19.8 / √807.04
r = -19.8 / 28.41
r = -0.697
```
**Correlation (Sleep Duration vs Exam Score) = -0.697** (Moderate negative correlation)

---

**CONCLUSION:**

| Variable | Correlation | Strength |
|----------|-------------|----------|
| **Study Hours** | **+0.987** | **Very Strong Positive** |
| Sleep Duration | -0.697 | Moderate Negative |

**Study Hours has a STRONGER relationship with Exam Scores** (r = 0.987)

**Interpretation:**
1. **Study Hours:** As study hours increase, exam scores increase almost perfectly (98.7% of variation explained)
2. **Sleep Duration:** Shows moderate negative correlation, meaning more sleep is associated with lower scores in this small sample (possibly because students who sleep more study less, or students who study most sacrifice sleep)
3. **Statistical Justification:** |0.987| > |0.697|, therefore Study Hours is the stronger predictor

---

#### c) Find skewness and kurtosis for all last three columns

**STUDY HOURS:**

**Skewness:**
**Formula:** SK = 3(Mean - Median) / SD

```
SK = 3(9 - 9) / 2
SK = 0 / 2
SK = 0
```
**Skewness = 0** (Perfectly symmetric)

**Kurtosis:**
**Formula:** Kurt = Σ(x - μ)⁴ / (N × σ⁴)

| x | (x - μ)⁴ |
|---|----------|
| 10 | 1 |
| 8 | 1 |
| 12 | 81 |
| 6 | 81 |
| 9 | 0 |
| **Sum** | **164** |

```
Kurtosis = 164 / (5 × 2⁴)
Kurtosis = 164 / (5 × 16)
Kurtosis = 164 / 80
Kurtosis = 2.05
```
**Kurtosis = 2.05** (Platykurtic - slightly flatter than normal)

---

**SLEEP DURATION:**

**Skewness:**
```
SK = 3(6.4 - 6) / 1.02
SK = 3(0.4) / 1.02
SK = 1.2 / 1.02
SK = 1.18
```
**Skewness = 1.18** (Positively skewed - right tail)

**Kurtosis:**

| x | (x - μ)⁴ |
|---|----------|
| 7 | 0.13 |
| 6 | 0.03 |
| 5 | 3.84 |
| 8 | 6.55 |
| 6 | 0.03 |
| **Sum** | **10.58** |

```
Kurtosis = 10.58 / (5 × 1.04²)
Kurtosis = 10.58 / (5 × 1.08)
Kurtosis = 10.58 / 5.40
Kurtosis = 1.96
```
**Kurtosis = 1.96** (Platykurtic)

---

**EXAM SCORE:**

**Skewness:**
```
SK = 3(81.4 - 80) / 5.57
SK = 3(1.4) / 5.57
SK = 4.2 / 5.57
SK = 0.75
```
**Skewness = 0.75** (Moderately positively skewed)

**Kurtosis:**

| x | (x - μ)⁴ |
|---|----------|
| 85 | 167.96 |
| 78 | 133.63 |
| 90 | 5469.53 |
| 74 | 2998.51 |
| 80 | 3.84 |
| **Sum** | **8773.47** |

```
Kurtosis = 8773.47 / (5 × 31.04²)
Kurtosis = 8773.47 / (5 × 963.48)
Kurtosis = 8773.47 / 4817.40
Kurtosis = 1.82
```
**Kurtosis = 1.82** (Platykurtic)

---

#### d) Compute the correlation and coefficient between dependent and independent variables

**Already computed in part (b):**

**1. Study Hours vs Exam Score:**
- **Correlation Coefficient (r) = 0.987**

**Coefficient of Determination (r²):**
**Formula:** r² = (Correlation Coefficient)²

**Step-by-step:**
```
r² = (0.987)²
r² = 0.974
r² = 97.4%
```
- **Coefficient of Determination (r²) = 0.974 or 97.4%**
- **Interpretation:** 97.4% of the variation in Exam Scores can be explained by Study Hours
- **Unexplained variation:** 2.6% (due to other factors)

**2. Sleep Duration vs Exam Score:**
- **Correlation Coefficient (r) = -0.697**

**Coefficient of Determination (r²):**
**Formula:** r² = (Correlation Coefficient)²

**Step-by-step:**
```
r² = (-0.697)²
r² = 0.486
r² = 48.6%
```
- **Coefficient of Determination (r²) = 0.486 or 48.6%**
- **Interpretation:** 48.6% of the variation in Exam Scores can be explained by Sleep Duration
- **Unexplained variation:** 51.4% (due to other factors)

**Summary Table:**

| Relationship | r | r² | Interpretation |
|--------------|---|----|--------------------|
| Study Hours → Exam Score | +0.987 | 0.974 | Very strong positive |
| Sleep Duration → Exam Score | -0.697 | 0.486 | Moderate negative |

**Covariance Calculations:**

**Covariance (Study Hours, Exam Score):**
**Formula:** Cov(X,Y) = Σ[(x - x̄)(y - ȳ)] / N

```
Cov = 55 / 5 = 11
```
**Covariance = 11**

**Covariance (Sleep Duration, Exam Score):**
```
Cov = -19.8 / 5 = -3.96
```
**Covariance = -3.96**

---

## UNIT 2

### Question 1
**A security system requires users to create a 5-character access code using the letters A-Z (uppercase only). Each character in the code must be a letter, and letters cannot be repeated.**

**Answer:**

This is a **PERMUTATION** problem because:
1. Order matters (ABC is different from BAC)
2. No repetition allowed

**Formula:** P(n, r) = n! / (n - r)!

Where:
- n = total number of letters = 26
- r = positions to fill = 5

**Step-by-step:**
```
P(26, 5) = 26! / (26 - 5)!
P(26, 5) = 26! / 21!
P(26, 5) = 26 × 25 × 24 × 23 × 22
```

**Calculation:**
```
= 26 × 25 = 650
= 650 × 24 = 15,600
= 15,600 × 23 = 358,800
= 358,800 × 22 = 7,893,600
```

**Answer: 7,893,600 possible access codes**

**Alternative thinking:**
- 1st position: 26 choices
- 2nd position: 25 choices (one letter used)
- 3rd position: 24 choices
- 4th position: 23 choices
- 5th position: 22 choices
- Total = 26 × 25 × 24 × 23 × 22 = **7,893,600**

---

### Question 2
**You are organizing a speaker panel for a conference and need to select 4 speakers from a pool of 10 applicants. The order in which the speakers are selected does not matter.**

**Answer:**

This is a **COMBINATION** problem because:
1. Order does NOT matter
2. We're just selecting a group

**Formula:** C(n, r) = n! / [r! × (n - r)!]

Where:
- n = total applicants = 10
- r = speakers to select = 4

**Step-by-step:**
```
C(10, 4) = 10! / [4! × (10 - 4)!]
C(10, 4) = 10! / (4! × 6!)
C(10, 4) = (10 × 9 × 8 × 7 × 6!) / (4! × 6!)
C(10, 4) = (10 × 9 × 8 × 7) / (4 × 3 × 2 × 1)
C(10, 4) = 5040 / 24
C(10, 4) = 210
```

**Answer: 210 different combinations of speakers**

---

### Question 3
**A company produces three types of beverages: A, B, and C. If a defective beverage is discovered, what is the most likely type of beverage (A, B, or C) that it is?**

**Given:**
- P(Defective | A) = 0.02
- P(Defective | B) = 0.05
- P(Defective | C) = 0.01
- P(A | Defective) = 0.2
- P(B | Defective) = 0.3
- P(C | Defective) = 0.35

**Note:** The posterior probabilities don't sum to 1.0 (0.2 + 0.3 + 0.35 = 0.85), which suggests there might be an error in the problem statement. However, we'll work with the given values.

**Answer:**

The question provides **posterior probabilities** (after observing a defective beverage):

| Beverage Type | P(Type \| Defective) | Percentage |
|---------------|---------------------|------------|
| A | 0.2 | 20% |
| B | 0.3 | 30% |
| **C** | **0.35** | **35%** |

**Conclusion: Type C is the most likely beverage** when a defective beverage is discovered.

**Interpretation:**
Even though Type C has the **lowest defect rate** (0.01), it accounts for the **highest proportion of defective beverages found** (35%). This indicates that **Type C is produced in much larger quantities** than Types A and B, making it the most common source of defective beverages despite its lower defect rate.

---

### Question 4
**A community center offers three types of sports activities: Swimming (S), Volleyball (V), and Table Tennis (TT).**

|  | Swimming (S) | Volleyball (V) | Table Tennis (TT) |
|---|---|---|---|
| Adult | 80 | 50 | 40 |
| Teen | 30 | 60 | 20 |
| Child | 40 | 30 | 70 |

---

#### i. Probability that a randomly chosen participant is enrolled in Volleyball (V)

**Formula:** P(V) = Number in Volleyball / Total participants

**Step-by-step:**
```
Total participants = 80 + 50 + 40 + 30 + 60 + 20 + 40 + 30 + 70
Total = 420

Volleyball participants = 50 + 60 + 30 = 140

P(V) = 140 / 420
P(V) = 1/3
P(V) = 0.333
```

**Answer: P(Volleyball) = 0.333 or 33.3% or 1/3**

---

#### ii. Probability that a randomly chosen participant is a Child

**Formula:** P(Child) = Number of children / Total participants

**Step-by-step:**
```
Children = 40 + 30 + 70 = 140

P(Child) = 140 / 420
P(Child) = 1/3
P(Child) = 0.333
```

**Answer: P(Child) = 0.333 or 33.3% or 1/3**

---

#### iii. Probability that a randomly chosen participant is an Adult enrolled in Swimming (S)

**Formula:** P(Adult AND Swimming) = Number of adults in swimming / Total participants

**Step-by-step:**
```
Adults in Swimming = 80

P(Adult AND Swimming) = 80 / 420
P(Adult AND Swimming) = 4/21
P(Adult AND Swimming) = 0.190
```

**Answer: P(Adult AND Swimming) = 0.190 or 19.0% or 4/21**

---

#### iv. Probability that a randomly chosen participant is a Teen enrolled in Table Tennis (TT)

**Formula:** P(Teen AND TT) = Number of teens in table tennis / Total participants

**Step-by-step:**
```
Teens in Table Tennis = 20

P(Teen AND TT) = 20 / 420
P(Teen AND TT) = 1/21
P(Teen AND TT) = 0.048
```

**Answer: P(Teen AND Table Tennis) = 0.048 or 4.8% or 1/21**

---

#### v. Probability that a participant is an Adult given they are enrolled in Volleyball (V)

**Formula:** P(Adult | V) = P(Adult AND V) / P(V)

**Step-by-step:**
```
Adults in Volleyball = 50
Total in Volleyball = 140

P(Adult | V) = 50 / 140
P(Adult | V) = 5/14
P(Adult | V) = 0.357
```

**Answer: P(Adult | Volleyball) = 0.357 or 35.7% or 5/14**

---

### Question 5
**A traffic safety study examines the effect of seatbelt usage on accident outcomes.**

**Data:**

|  | Minor Injury | Serious Injury | Total |
|---|---|---|---|
| **Wearing Seatbelt** | 15 | 5 | 20 |
| **Not Wearing Seatbelt** | 10 | 20 | 30 |
| **Total** | 25 | 25 | 50 |

---

#### i) Odds in favor of minor injury while wearing seatbelt vs serious injury

**Formula:** Odds in favor = P(Success) / P(Failure) = Number of successes / Number of failures

**Step-by-step:**
```
Among seatbelt wearers:
Minor injuries = 15
Serious injuries = 5

Odds in favor = 15 : 5 = 3 : 1
or
Odds = 15/5 = 3
```

**Answer: Odds = 3:1 or 3.0**

**Interpretation:** For every 3 drivers wearing seatbelts who sustain minor injuries, 1 sustains a serious injury.

---

#### ii) Odds against minor injury while NOT wearing seatbelt

**Formula:** Odds against = P(Failure) / P(Success) = Number of failures / Number of successes

**Step-by-step:**
```
Among non-seatbelt wearers:
Minor injuries = 10
Serious injuries = 20

Odds against minor injury = 20 : 10 = 2 : 1
or
Odds against = 20/10 = 2
```

**Answer: Odds against = 2:1 or 2.0**

**Interpretation:** For every 2 drivers not wearing seatbelts who sustain serious injuries, 1 sustains a minor injury.

---

#### iii) Probability of minor injury while wearing seatbelt

**Formula:** P = Number of favorable outcomes / Total outcomes

**Step-by-step:**
```
Among seatbelt wearers:
Minor injuries = 15
Total seatbelt wearers = 20

P(Minor | Seatbelt) = 15/20
P(Minor | Seatbelt) = 0.75
```

**Answer: P(Minor injury | Seatbelt) = 0.75 or 75%**

---

#### iv) Calculate the odds ratio

**Formula:** Odds Ratio (OR) = [Odds of event in Group 1] / [Odds of event in Group 2]

**OR = [a/b] / [c/d] = (a × d) / (b × c)**

Where:
- a = Minor injury with seatbelt = 15
- b = Serious injury with seatbelt = 5
- c = Minor injury without seatbelt = 10
- d = Serious injury without seatbelt = 20

**Step-by-step:**
```
Odds of minor injury with seatbelt = 15/5 = 3
Odds of minor injury without seatbelt = 10/20 = 0.5

OR = 3 / 0.5 = 6

Alternative calculation:
OR = (15 × 20) / (5 × 10)
OR = 300 / 50
OR = 6
```

**Answer: Odds Ratio = 6.0**

---

#### v) What does this odds ratio indicate about seatbelt effectiveness?

**Interpretation of OR = 6.0:**

**Conclusion: Wearing a seatbelt is highly effective in minimizing injury severity.**

**Detailed Explanation:**

1. **Odds Ratio = 6.0** means that the odds of sustaining a minor injury (versus serious injury) are **6 times higher** when wearing a seatbelt compared to not wearing one.

2. **Statistical Significance:**
   - OR > 1 indicates positive association (seatbelts reduce serious injuries)
   - OR = 1 would mean no effect
   - OR < 1 would mean harmful effect

3. **Practical Significance:**
   - Drivers wearing seatbelts have **75% chance** of minor injury vs serious
   - Drivers NOT wearing seatbelts have only **33.3% chance** of minor injury vs serious
   - This represents a **125% increase** in protection

4. **Public Health Implication:**
   - Seatbelts dramatically reduce the severity of injuries in traffic accidents
   - This provides strong evidence for mandatory seatbelt laws
   - The protective effect is substantial and clinically meaningful

**Summary:** The odds ratio of 6.0 provides strong statistical evidence that wearing a seatbelt significantly reduces the risk of serious injury in traffic accidents, confirming the effectiveness of seatbelt usage in improving traffic safety outcomes.

---

### Question 6
**In a volleyball training camp, a player successfully hits the target 14 times out of 20 serves. What is the probability for 60 serves?**

**This follows a BINOMIAL DISTRIBUTION:**

**Formula:** P(X = k) = C(n,k) × p^k × (1-p)^(n-k)

**Given:**
- Success rate: p = 14/20 = 0.7
- Failure rate: q = 1 - p = 0.3
- Number of trials: n = 60

---

#### i. Probability of hitting target for exactly 5 serves (out of 60)

**Formula:** P(X = 5) = C(60,5) × (0.7)^5 × (0.3)^55

**Step-by-step:**
```
C(60,5) = 60!/(5! × 55!) = 5,461,512

P(X = 5) = 5,461,512 × (0.7)^5 × (0.3)^55
P(X = 5) = 5,461,512 × 0.16807 × (1.715 × 10^-26)
P(X = 5) ≈ 1.57 × 10^-18
```

**Answer: P(X = 5) ≈ 0.00000000000000000157** (Extremely unlikely)

**Interpretation:** With a 70% success rate, hitting only 5 out of 60 serves is virtually impossible.

---

#### ii. Probability of hitting target for exactly 45 serves

**Formula:** P(X = 45) = C(60,45) × (0.7)^45 × (0.3)^15

**Step-by-step:**
```
C(60,45) = C(60,15) = 253,338,471,349,988,640

P(X = 45) = C(60,45) × (0.7)^45 × (0.3)^15
```

This requires statistical software or normal approximation.

**Using Normal Approximation:**
- μ = np = 60 × 0.7 = 42
- σ = √(npq) = √(60 × 0.7 × 0.3) = √12.6 = 3.55

**Converting to Z-score:**
```
Z = (X - μ) / σ
Z = (45 - 42) / 3.55
Z = 0.85
```

Using continuity correction for P(X = 45):
```
P(44.5 < X < 45.5)
Z1 = (44.5 - 42) / 3.55 = 0.70
Z2 = (45.5 - 42) / 3.55 = 0.99

P(X = 45) ≈ P(Z < 0.99) - P(Z < 0.70)
P(X = 45) ≈ 0.8389 - 0.7580
P(X = 45) ≈ 0.081
```

**Answer: P(X = 45) ≈ 0.081 or 8.1%**

---

#### iii. Probability of hitting AT MOST 55 serves

**Formula:** P(X ≤ 55) = Σ P(X = k) for k = 0 to 55

**Using Normal Approximation:**
```
μ = 42, σ = 3.55

Z = (55.5 - 42) / 3.55 (with continuity correction)
Z = 13.5 / 3.55
Z = 3.80
```

From Z-table: P(Z < 3.80) ≈ 0.9999

**Answer: P(X ≤ 55) ≈ 0.9999 or 99.99%**

**Interpretation:** It's almost certain (99.99% probability) that the player will hit at most 55 serves out of 60.

---

#### iv. Probability of hitting AT LEAST 2 serves

**Formula:** P(X ≥ 2) = 1 - P(X < 2) = 1 - [P(X=0) + P(X=1)]

**Step-by-step:**

**P(X = 0):**
```
P(X = 0) = C(60,0) × (0.7)^0 × (0.3)^60
P(X = 0) = 1 × 1 × (0.3)^60
P(X = 0) ≈ 4.25 × 10^-26 (essentially 0)
```

**P(X = 1):**
```
P(X = 1) = C(60,1) × (0.7)^1 × (0.3)^59
P(X = 1) = 60 × 0.7 × (0.3)^59
P(X = 1) ≈ 8.91 × 10^-24 (essentially 0)
```

**Therefore:**
```
P(X ≥ 2) = 1 - (essentially 0)
P(X ≥ 2) ≈ 1.0
```

**Answer: P(X ≥ 2) ≈ 1.0 or 100%** (virtually certain)

**Interpretation:** With a 70% success rate, it's virtually guaranteed the player will hit at least 2 targets out of 60 serves.

---

### Question 7
**A local coffee shop receives an average of 15 customer arrivals per hour.**

**This follows a POISSON DISTRIBUTION:**

**Formula:** P(X = k) = (λ^k × e^(-λ)) / k!

Where λ = average rate = 15 customers/hour

---

#### i) Probability of exactly 12 customer arrivals in one hour

**Formula:** P(X = 12) = (15^12 × e^(-15)) / 12!

**Step-by-step:**
```
λ = 15
k = 12
e^(-15) ≈ 3.059 × 10^(-7)
15^12 = 129,746,337,890,625
12! = 479,001,600

P(X = 12) = (129,746,337,890,625 × 3.059 × 10^(-7)) / 479,001,600
P(X = 12) = 39,687,570.89 / 479,001,600
P(X = 12) ≈ 0.0829
```

**Answer: P(X = 12) ≈ 0.0829 or 8.29%**

---

#### ii) Probability of no more than 3 customer arrivals

**Formula:** P(X ≤ 3) = P(X=0) + P(X=1) + P(X=2) + P(X=3)

**Step-by-step:**

**P(X = 0):**
```
P(X = 0) = (15^0 × e^(-15)) / 0!
P(X = 0) = (1 × 3.059 × 10^(-7)) / 1
P(X = 0) ≈ 3.059 × 10^(-7)
```

**P(X = 1):**
```
P(X = 1) = (15^1 × e^(-15)) / 1!
P(X = 1) = 15 × 3.059 × 10^(-7)
P(X = 1) ≈ 4.588 × 10^(-6)
```

**P(X = 2):**
```
P(X = 2) = (15^2 × e^(-15)) / 2!
P(X = 2) = 225 × 3.059 × 10^(-7) / 2
P(X = 2) ≈ 3.441 × 10^(-5)
```

**P(X = 3):**
```
P(X = 3) = (15^3 × e^(-15)) / 3!
P(X = 3) = 3375 × 3.059 × 10^(-7) / 6
P(X = 3) ≈ 1.722 × 10^(-4)
```

**Sum:**
```
P(X ≤ 3) = 3.059×10^(-7) + 4.588×10^(-6) + 3.441×10^(-5) + 1.722×10^(-4)
P(X ≤ 3) ≈ 0.000211
```

**Answer: P(X ≤ 3) ≈ 0.000211 or 0.0211%**

**Interpretation:** With an average of 15 customers per hour, receiving 3 or fewer customers is extremely unlikely (only 0.02% chance).

---

#### iii) Probability of more than 5 arrivals during busiest 2-hour period

**Given:**
- Time period = 2 hours
- New λ = 15 × 2 = 30 customers per 2 hours

**Formula:** P(X > 5) = 1 - P(X ≤ 5)

**Step-by-step:**

For λ = 30, calculating P(X ≤ 5) requires summing probabilities from X=0 to X=5.

**Using Normal Approximation (since λ > 10):**
```
μ = λ = 30
σ = √λ = √30 = 5.48

Using continuity correction:
Z = (5.5 - 30) / 5.48
Z = -24.5 / 5.48
Z = -4.47
```

From Z-table: P(Z < -4.47) ≈ 0.000004

```
P(X > 5) = 1 - P(X ≤ 5)
P(X > 5) ≈ 1 - 0.000004
P(X > 5) ≈ 0.999996
```

**Answer: P(X > 5) ≈ 0.9999 or 99.99%**

**Interpretation:** During a 2-hour period with an average of 30 customers, it's virtually certain (99.99%) that more than 5 customers will arrive.

---

### Question 8
**The yearly salaries at a tech company are normally distributed with mean μ = $75,000 and variance σ² = $4,000,000.**

**Given:**
- μ = $75,000
- σ² = $4,000,000
- σ = √4,000,000 = $2,000

**This follows a NORMAL DISTRIBUTION**

**Formula:** Z = (X - μ) / σ

---

#### I) Probability that salary is more than $78,000

**Formula:** P(X > 78,000) = P(Z > z) = 1 - P(Z ≤ z)

**Step-by-step:**
```
Z = (78,000 - 75,000) / 2,000
Z = 3,000 / 2,000
Z = 1.5
```

From Standard Normal Table:
```
P(Z ≤ 1.5) = 0.9332

P(X > 78,000) = 1 - 0.9332
P(X > 78,000) = 0.0668
```

**Answer: P(X > $78,000) = 0.0668 or 6.68%**

**Interpretation:** About 6.68% of employees earn more than $78,000 per year.

---

#### II) Probability that salary is less than $73,000

**Formula:** P(X < 73,000) = P(Z < z)

**Step-by-step:**
```
Z = (73,000 - 75,000) / 2,000
Z = -2,000 / 2,000
Z = -1.0
```

From Standard Normal Table:
```
P(Z < -1.0) = 0.1587
```

**Answer: P(X < $73,000) = 0.1587 or 15.87%**

**Interpretation:** About 15.87% of employees earn less than $73,000 per year.

---

## UNIT 3 - CONFIDENCE INTERVALS

### Question 1
**Calculate 90%, 95%, 99% confidence intervals for proportion of satisfied customers.**

**Given:**
- Sample size (n) = 300
- Number satisfied (x) = 180
- Population size (N) = 1000
- Sample proportion: p̂ = 180/300 = 0.6

**Formula for Confidence Interval for Proportion:**
**CI = p̂ ± Z × √[p̂(1-p̂)/n]**

---

#### 90% Confidence Interval

**Step-by-step:**

1. **Find Z-value:**
   - For 90% confidence: α = 0.10, α/2 = 0.05
   - Z₀.₀₅ = 1.645

2. **Calculate Standard Error:**
```
SE = √[p̂(1-p̂)/n]
SE = √[0.6 × 0.4 / 300]
SE = √[0.24 / 300]
SE = √0.0008
SE = 0.0283
```

3. **Calculate Margin of Error:**
```
ME = Z × SE
ME = 1.645 × 0.0283
ME = 0.0465
```

4. **Calculate CI:**
```
Lower limit = 0.6 - 0.0465 = 0.5535
Upper limit = 0.6 + 0.0465 = 0.6465
```

**90% CI: (0.5535, 0.6465) or (55.35%, 64.65%)**

---

#### 95% Confidence Interval

**Step-by-step:**

1. **Z-value:** Z₀.₀₂₅ = 1.96

2. **Margin of Error:**
```
ME = 1.96 × 0.0283
ME = 0.0555
```

3. **Calculate CI:**
```
Lower limit = 0.6 - 0.0555 = 0.5445
Upper limit = 0.6 + 0.0555 = 0.6555
```

**95% CI: (0.5445, 0.6555) or (54.45%, 65.55%)**

---

#### 99% Confidence Interval

**Step-by-step:**

1. **Z-value:** Z₀.₀₀₅ = 2.576

2. **Margin of Error:**
```
ME = 2.576 × 0.0283
ME = 0.0729
```

3. **Calculate CI:**
```
Lower limit = 0.6 - 0.0729 = 0.5271
Upper limit = 0.6 + 0.0729 = 0.6729
```

**99% CI: (0.5271, 0.6729) or (52.71%, 67.29%)**

---

**Summary Table:**

| Confidence Level | Z-value | Margin of Error | Confidence Interval |
|-----------------|---------|-----------------|---------------------|
| 90% | 1.645 | 0.0465 | (55.35%, 64.65%) |
| 95% | 1.96 | 0.0555 | (54.45%, 65.55%) |
| 99% | 2.576 | 0.0729 | (52.71%, 67.29%) |

**Interpretation:**
- We are 90% confident that the true proportion of satisfied customers in the population is between 55.35% and 64.65%
- We are 95% confident that the true proportion is between 54.45% and 65.55%
- We are 99% confident that the true proportion is between 52.71% and 67.29%
- Note: As confidence level increases, the interval becomes wider

---

### Question 2
**A company claims average training time is 20 hours/month. Sample of 36 employees shows mean = 22 hours, σ = 6 hours.**

**Given:**
- Claimed μ₀ = 20 hours
- Sample mean (x̄) = 22 hours
- Population SD (σ) = 6 hours
- Sample size (n) = 36
- Normally distributed

**Formula for CI (Z-distribution, known σ):**
**CI = x̄ ± Z × (σ/√n)**

---

#### 90% Confidence Interval

**Step-by-step:**

1. **Z-value:** Z₀.₀₅ = 1.645

2. **Calculate Standard Error:**
```
SE = σ/√n
SE = 6/√36
SE = 6/6
SE = 1
```

3. **Calculate Margin of Error:**
```
ME = Z × SE
ME = 1.645 × 1
ME = 1.645
```

4. **Calculate CI:**
```
Lower limit = 22 - 1.645 = 20.355
Upper limit = 22 + 1.645 = 23.645
```

**90% CI: (20.355, 23.645) hours**

**Conclusion for 90%:** Since the claimed value of 20 hours is within the confidence interval (barely), we **cannot conclude with 90% confidence** that the training time is significantly different from 20 hours.

---

#### 95% Confidence Interval

**Step-by-step:**

1. **Z-value:** Z₀.₀₂₅ = 1.96

2. **Margin of Error:**
```
ME = 1.96 × 1
ME = 1.96
```

3. **Calculate CI:**
```
Lower limit = 22 - 1.96 = 20.04
Upper limit = 22 + 1.96 = 23.96
```

**95% CI: (20.04, 23.96) hours**

**Conclusion for 95%:** Since 20 hours is within the confidence interval, we **cannot conclude with 95% confidence** that the training time is significantly different from 20 hours.

---

#### 99% Confidence Interval

**Step-by-step:**

1. **Z-value:** Z₀.₀₀₅ = 2.576

2. **Margin of Error:**
```
ME = 2.576 × 1
ME = 2.576
```

3. **Calculate CI:**
```
Lower limit = 22 - 2.576 = 19.424
Upper limit = 22 + 2.576 = 24.576
```

**99% CI: (19.424, 24.576) hours**

**Conclusion for 99%:** Since 20 hours is well within the confidence interval, we **cannot conclude with 99% confidence** that the training time is significantly different from 20 hours.

---

**Summary Table:**

| Confidence Level | Z-value | Confidence Interval | Contains 20? | Conclusion |
|-----------------|---------|---------------------|--------------|------------|
| 90% | 1.645 | (20.36, 23.64) | Yes (barely) | Not significantly different |
| 95% | 1.96 | (20.04, 23.96) | Yes | Not significantly different |
| 99% | 2.576 | (19.42, 24.58) | Yes | Not significantly different |

**Overall Conclusion:**
At all confidence levels (90%, 95%, and 99%), the claimed value of 20 hours falls within the confidence interval. Therefore, we **cannot conclude that the average training time is significantly different from 20 hours**. However, the sample mean of 22 hours suggests the actual training time may be slightly higher than claimed.

---

### Question 3
**A researcher assesses a new study method. Sample of 15 students: mean = 78, SD = 10.**

**Given:**
- Sample mean (x̄) = 78
- Sample SD (s) = 10
- Sample size (n) = 15
- Degrees of freedom (df) = n - 1 = 14

**Use t-distribution (small sample, unknown population SD)**

**Formula for CI (t-distribution):**
**CI = x̄ ± t × (s/√n)**

---

#### 90% Confidence Interval

**Step-by-step:**

1. **Find t-value:**
   - df = 14, α/2 = 0.05
   - t₀.₀₅,₁₄ = 1.761

2. **Calculate Standard Error:**
```
SE = s/√n
SE = 10/√15
SE = 10/3.873
SE = 2.582
```

3. **Calculate Margin of Error:**
```
ME = t × SE
ME = 1.761 × 2.582
ME = 4.547
```

4. **Calculate CI:**
```
Lower limit = 78 - 4.547 = 73.453
Upper limit = 78 + 4.547 = 82.547
```

**90% CI: (73.45, 82.55)**

---

#### 95% Confidence Interval

**Step-by-step:**

1. **t-value:** t₀.₀₂₅,₁₄ = 2.145

2. **Margin of Error:**
```
ME = 2.145 × 2.582
ME = 5.539
```

3. **Calculate CI:**
```
Lower limit = 78 - 5.539 = 72.461
Upper limit = 78 + 5.539 = 83.539
```

**95% CI: (72.46, 83.54)**

---

#### 99% Confidence Interval

**Step-by-step:**

1. **t-value:** t₀.₀₀₅,₁₄ = 2.977

2. **Margin of Error:**
```
ME = 2.977 × 2.582
ME = 7.687
```

3. **Calculate CI:**
```
Lower limit = 78 - 7.687 = 70.313
Upper limit = 78 + 7.687 = 85.687
```

**99% CI: (70.31, 85.69)**

---

**Summary Table:**

| Confidence Level | t-value | SE | Margin of Error | Confidence Interval |
|-----------------|---------|----|-----------------|--------------------|
| 90% | 1.761 | 2.582 | 4.547 | (73.45, 82.55) |
| 95% | 2.145 | 2.582 | 5.539 | (72.46, 83.54) |
| 99% | 2.977 | 2.582 | 7.687 | (70.31, 85.69) |

**Interpretation:**
- We are 90% confident that the true average test score for all students using the new study method is between 73.45 and 82.55
- We are 95% confident that the true average is between 72.46 and 83.54
- We are 99% confident that the true average is between 70.31 and 85.69
- Note: t-distribution produces wider intervals than z-distribution due to small sample size and unknown population SD

---

## UNIT 4 - HYPOTHESIS TESTING

### Question 1
**Beverage company claims average sugar content is 15 grams with SD = 3 grams. Sample of 50 cans shows mean = 14 grams. Test at α = 0.05.**

**Given:**
- H₀: μ = 15 grams (claim)
- H₁: μ ≠ 15 grams (two-tailed test)
- x̄ = 14 grams
- σ = 3 grams
- n = 50
- α = 0.05

---

#### METHOD 1: Critical Region Technique

**Formula:** Z = (x̄ - μ₀) / (σ/√n)

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = σ/√n = 3/√50 = 3/7.071 = 0.424

Z = (14 - 15) / 0.424
Z = -1 / 0.424
Z = -2.358
```

2. **Determine critical values:**
   - For α = 0.05 (two-tailed): α/2 = 0.025
   - Critical values: Z = ±1.96
   - Critical region: Z < -1.96 or Z > 1.96

3. **Decision:**
```
Calculated Z = -2.358
Since -2.358 < -1.96, Z falls in critical region
```

**Decision: REJECT H₀**

**Conclusion:** There IS sufficient evidence at 0.05 significance level to conclude that the mean sugar content is significantly different from 15 grams.

---

#### METHOD 2: P-value Technique

**Step-by-step:**

1. **Test statistic:** Z = -2.358 (calculated above)

2. **Find p-value (two-tailed):**
```
P(Z < -2.358) = 0.0092
P-value = 2 × 0.0092 = 0.0184
```

3. **Decision rule:**
```
If p-value < α, reject H₀
0.0184 < 0.05
```

**Decision: REJECT H₀**

**Conclusion:** The p-value of 0.0184 is less than the significance level of 0.05, providing sufficient evidence to reject the null hypothesis.

---

#### METHOD 3: Confidence Interval Technique

**Step-by-step:**

1. **Calculate 95% CI:**
```
CI = x̄ ± Z₀.₀₂₅ × SE
CI = 14 ± 1.96 × 0.424
CI = 14 ± 0.831
CI = (13.169, 14.831)
```

2. **Decision:**
```
Hypothesized value = 15 grams
95% CI = (13.169, 14.831)
15 is NOT in the interval
```

**Decision: REJECT H₀**

**Conclusion:** Since the claimed value of 15 grams does not fall within the 95% confidence interval, we reject the null hypothesis.

---

**Summary:**

| Method | Test Statistic | Critical Value/P-value/CI | Decision |
|--------|----------------|---------------------------|----------|
| Critical Region | Z = -2.358 | ±1.96 | Reject H₀ |
| P-value | Z = -2.358 | p = 0.0184 | Reject H₀ |
| Confidence Interval | x̄ = 14 | (13.17, 14.83) | Reject H₀ |

**Final Conclusion:** All three methods lead to the same conclusion. There is sufficient statistical evidence at the 0.05 significance level to conclude that the average sugar content is significantly different from the claimed 15 grams. The actual sugar content appears to be lower than claimed (around 14 grams).

---

### Question 2
**Electronics manufacturer claims battery life is at least 20 hours. Sample of 30 shows mean = 18 hours, SD = 4 hours. Test at α = 0.05.**

**Given:**
- H₀: μ ≥ 20 hours (claim)
- H₁: μ < 20 hours (left-tailed test)
- x̄ = 18 hours
- s = 4 hours
- n = 30
- α = 0.05

**Use Z-test (n ≥ 30, approximate with s)**

---

#### METHOD 1: Critical Region Technique

**Formula:** Z = (x̄ - μ₀) / (s/√n)

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = s/√n = 4/√30 = 4/5.477 = 0.730

Z = (18 - 20) / 0.730
Z = -2 / 0.730
Z = -2.739
```

2. **Determine critical value:**
   - Left-tailed test, α = 0.05
   - Critical value: Z = -1.645
   - Critical region: Z < -1.645

3. **Decision:**
```
Calculated Z = -2.739
Since -2.739 < -1.645, Z falls in critical region
```

**Decision: REJECT H₀**

**Conclusion:** There IS sufficient evidence at 0.05 significance level to conclude that the average battery life is less than 20 hours. The manufacturer's claim is NOT supported.

---

#### METHOD 2: P-value Technique

**Step-by-step:**

1. **Test statistic:** Z = -2.739

2. **Find p-value (left-tailed):**
```
P(Z < -2.739) = 0.0031
P-value = 0.0031
```

3. **Decision:**
```
P-value (0.0031) < α (0.05)
```

**Decision: REJECT H₀**

**Conclusion:** The p-value of 0.0031 indicates strong evidence against the null hypothesis. There is only a 0.31% chance of observing such a low sample mean if the true mean were 20 hours or more.

---

#### METHOD 3: Confidence Interval Technique

**Step-by-step:**

1. **Calculate 95% CI (one-sided):**
```
For left-tailed test, use upper bound:
Upper bound = x̄ + Z₀.₀₅ × SE
Upper bound = 18 + 1.645 × 0.730
Upper bound = 18 + 1.201
Upper bound = 19.201

CI: (-∞, 19.201)
```

2. **Decision:**
```
Hypothesized minimum value = 20 hours
Upper bound of CI = 19.201 hours
20 > 19.201 (20 is not in the interval)
```

**Decision: REJECT H₀**

**Conclusion:** Since the claimed minimum value of 20 hours exceeds the upper confidence limit, we reject the claim that battery life is at least 20 hours.

---

**Summary:**

| Method | Test Statistic | Critical Value/P-value/CI | Decision |
|--------|----------------|---------------------------|----------|
| Critical Region | Z = -2.739 | -1.645 | Reject H₀ |
| P-value | Z = -2.739 | p = 0.0031 | Reject H₀ |
| Confidence Interval | x̄ = 18 | (-∞, 19.20) | Reject H₀ |

**Final Conclusion:** All three methods provide strong evidence to reject the manufacturer's claim. The average battery life is significantly less than 20 hours, with the sample suggesting an average of approximately 18 hours. The manufacturer's claim that battery life is "at least 20 hours" is not supported by the data.

---

### Question 3
**Health organization states average daily water intake should be at least 3 liters. Study of 40 adults shows mean = 2.5 liters, SD = 0.8 liters. Test at α = 0.01.**

**Given:**
- H₀: μ ≥ 3 liters (claim)
- H₁: μ < 3 liters (left-tailed test)
- x̄ = 2.5 liters
- s = 0.8 liters
- n = 40
- α = 0.01

**Use Z-test (n ≥ 30)**

---

#### Using All Three Methods:

**Test Statistic:**
```
SE = s/√n = 0.8/√40 = 0.8/6.325 = 0.1265

Z = (2.5 - 3) / 0.1265
Z = -0.5 / 0.1265
Z = -3.953
```

---

#### METHOD 1: Critical Region Technique

**Step-by-step:**

1. **Critical value:**
   - Left-tailed, α = 0.01
   - Z₀.₀₁ = -2.326
   - Critical region: Z < -2.326

2. **Decision:**
```
Z = -3.953 < -2.326
Falls in critical region
```

**Decision: REJECT H₀**

---

#### METHOD 2: P-value Technique

**Step-by-step:**

1. **P-value:**
```
P(Z < -3.953) ≈ 0.00004
P-value = 0.00004
```

2. **Decision:**
```
0.00004 < 0.01
```

**Decision: REJECT H₀**

---

#### METHOD 3: Confidence Interval Technique

**Step-by-step:**

1. **99% CI (one-sided):**
```
Upper bound = x̄ + Z₀.₀₁ × SE
Upper bound = 2.5 + 2.326 × 0.1265
Upper bound = 2.5 + 0.294
Upper bound = 2.794

CI: (-∞, 2.794)
```

2. **Decision:**
```
3 liters > 2.794 liters
Not in interval
```

**Decision: REJECT H₀**

---

**Summary:**

| Method | Value | Decision |
|--------|-------|----------|
| Critical Region | Z = -3.953 < -2.326 | Reject H₀ |
| P-value | p = 0.00004 < 0.01 | Reject H₀ |
| Confidence Interval | 3 ∉ (-∞, 2.79) | Reject H₀ |

**Conclusion:** There is **very strong evidence** (p < 0.0001) at the 0.01 significance level to conclude that the average daily water intake is significantly less than the recommended 3 liters. The actual average appears to be around 2.5 liters, which is substantially below the health organization's recommendation. This suggests a need for public health interventions to increase water consumption.

---

### Question 4
**A bakery claims average weight of a dozen cookies is 300 grams. Sample of 20 batches shows mean = 295 grams, SD = 10 grams. Test at α = 0.05.**

**Given:**
- H₀: μ = 300 grams (claim)
- H₁: μ ≠ 300 grams (two-tailed test)
- x̄ = 295 grams
- s = 10 grams
- n = 20
- α = 0.05
- df = n - 1 = 19

**Use t-test (small sample, n < 30)**

---

#### Using Critical Region Technique

**Formula:** t = (x̄ - μ₀) / (s/√n)

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = s/√n = 10/√20 = 10/4.472 = 2.236

t = (295 - 300) / 2.236
t = -5 / 2.236
t = -2.236
```

2. **Determine critical values:**
   - Two-tailed test, α = 0.05, df = 19
   - t₀.₀₂₅,₁₉ = ±2.093
   - Critical region: t < -2.093 or t > 2.093

3. **Decision:**
```
Calculated t = -2.236
Since -2.236 < -2.093, t falls in critical region
```

**Decision: REJECT H₀**

**Conclusion:** There IS sufficient evidence at the 0.05 significance level to conclude that the average weight of a dozen cookies is significantly different from 300 grams. The actual weight appears to be less than claimed (around 295 grams).

---

### Question 5
**Light bulb manufacturer claims bulbs last at least 1000 hours. Sample of 15 bulbs shows mean = 950 hours, SD = 50 hours. Test at α = 0.01.**

**Given:**
- H₀: μ ≥ 1000 hours (claim)
- H₁: μ < 1000 hours (left-tailed test)
- x̄ = 950 hours
- s = 50 hours
- n = 15
- α = 0.01
- df = 14

---

#### Using P-value Technique

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = s/√n = 50/√15 = 50/3.873 = 12.91

t = (950 - 1000) / 12.91
t = -50 / 12.91
t = -3.872
```

2. **Find p-value:**
   - For t = -3.872 with df = 14
   - Using t-table: P(t < -3.872) ≈ 0.0008
   - P-value ≈ 0.0008 (one-tailed)

3. **Decision:**
```
P-value (0.0008) < α (0.01)
```

**Decision: REJECT H₀**

**Conclusion:** There is very strong evidence (p = 0.0008) to conclude that the average lifespan of bulbs is significantly less than 1000 hours. The manufacturer's claim is NOT supported by the data.

---

### Question 6
**Fitness program claims average weight loss is at least 4 kg. Study of 12 participants shows mean = 5.5 kg, SD = 1.5 kg. Test at α = 0.05.**

**Given:**
- H₀: μ ≤ 4 kg
- H₁: μ > 4 kg (right-tailed test)
- x̄ = 5.5 kg
- s = 1.5 kg
- n = 12
- α = 0.05
- df = 11

---

#### Using Confidence Interval Technique

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = s/√n = 1.5/√12 = 1.5/3.464 = 0.433

t = (5.5 - 4) / 0.433
t = 1.5 / 0.433
t = 3.464
```

2. **Calculate 95% CI (one-sided, lower bound):**
```
For right-tailed test:
Lower bound = x̄ - t₀.₀₅,₁₁ × SE
t₀.₀₅,₁₁ = 1.796

Lower bound = 5.5 - 1.796 × 0.433
Lower bound = 5.5 - 0.778
Lower bound = 4.722

CI: (4.722, ∞)
```

3. **Decision:**
```
Hypothesized value = 4 kg
Lower bound = 4.722 kg
4 < 4.722 (4 is not in the interval)
```

**Decision: REJECT H₀**

**Conclusion:** Since the hypothesized minimum value of 4 kg is below the lower confidence limit of 4.722 kg, we have sufficient evidence to support the claim that the average weight loss is greater than 4 kg. The fitness program appears to be effective.

---

### Question 7
**School claims at least 30% participate in extracurricular activities. Sample of 200 students shows 50 participate. Test at α = 0.01.**

**Given:**
- H₀: p ≥ 0.30 (claim)
- H₁: p < 0.30 (left-tailed test)
- x = 50, n = 200
- p̂ = 50/200 = 0.25
- p₀ = 0.30
- α = 0.01

---

#### Using Critical Region Technique

**Formula:** Z = (p̂ - p₀) / √[p₀(1-p₀)/n]

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = √[p₀(1-p₀)/n]
SE = √[0.30 × 0.70 / 200]
SE = √[0.21 / 200]
SE = √0.00105
SE = 0.0324

Z = (0.25 - 0.30) / 0.0324
Z = -0.05 / 0.0324
Z = -1.543
```

2. **Determine critical value:**
   - Left-tailed, α = 0.01
   - Z₀.₀₁ = -2.326
   - Critical region: Z < -2.326

3. **Decision:**
```
Z = -1.543 > -2.326
Does NOT fall in critical region
```

**Decision: FAIL TO REJECT H₀**

**Conclusion:** There is NOT sufficient evidence at the 0.01 significance level to conclude that the proportion of students participating in extracurricular activities is less than 30%. The school's claim is supported.

---

### Question 8
**Survey found 60% prefer coffee over tea. Sample of 150 shows 70 prefer coffee. Test at α = 0.05.**

**Given:**
- H₀: p = 0.60 (claim)
- H₁: p ≠ 0.60 (two-tailed test)
- x = 70, n = 150
- p̂ = 70/150 = 0.467
- p₀ = 0.60
- α = 0.05

---

#### Using P-value Technique

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = √[p₀(1-p₀)/n]
SE = √[0.60 × 0.40 / 150]
SE = √[0.24 / 150]
SE = √0.0016
SE = 0.04

Z = (0.467 - 0.60) / 0.04
Z = -0.133 / 0.04
Z = -3.325
```

2. **Find p-value (two-tailed):**
```
P(Z < -3.325) = 0.0004
P-value = 2 × 0.0004 = 0.0008
```

3. **Decision:**
```
P-value (0.0008) < α (0.05)
```

**Decision: REJECT H₀**

**Conclusion:** There is strong evidence (p = 0.0008) to conclude that the proportion of people who prefer coffee is significantly different from 60%. The actual proportion appears to be around 46.7%, which is substantially lower than the claimed 60%.

---

### Question 9
**Health department claims more than 25% of adults are physically active. Survey of 400 shows 120 are active. Test at α = 0.05.**

**Given:**
- H₀: p ≤ 0.25
- H₁: p > 0.25 (right-tailed test)
- x = 120, n = 400
- p̂ = 120/400 = 0.30
- p₀ = 0.25
- α = 0.05

---

#### Using Confidence Interval Technique

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = √[p₀(1-p₀)/n]
SE = √[0.25 × 0.75 / 400]
SE = √[0.1875 / 400]
SE = √0.00046875
SE = 0.0217

Z = (0.30 - 0.25) / 0.0217
Z = 0.05 / 0.0217
Z = 2.304
```

2. **Calculate 95% CI (one-sided, lower bound):**
```
Using p̂ for CI:
SE_CI = √[p̂(1-p̂)/n] = √[0.30 × 0.70 / 400] = 0.0229

Lower bound = p̂ - Z₀.₀₅ × SE_CI
Lower bound = 0.30 - 1.645 × 0.0229
Lower bound = 0.30 - 0.0377
Lower bound = 0.2623

CI: (0.2623, ∞) or (26.23%, ∞)
```

3. **Decision:**
```
Hypothesized value = 0.25 (25%)
Lower bound = 0.2623 (26.23%)
0.25 < 0.2623 (claim value not in interval)
```

**Decision: REJECT H₀**

**Conclusion:** There is sufficient evidence at the 0.05 significance level to support the claim that the proportion of physically active adults is greater than 25%. The data suggests approximately 30% are physically active.

---

### Question 10
**Manufacturer claims Battery A lasts longer than Battery B. Battery A: n=50, x̄=280, s=20. Battery B: n=40, x̄=260, s=25. Test at α = 0.05.**

**Given:**
- H₀: μ₁ ≤ μ₂
- H₁: μ₁ > μ₂ (right-tailed test)
- Battery A: n₁ = 50, x̄₁ = 280, s₁ = 20
- Battery B: n₂ = 40, x̄₂ = 260, s₂ = 25
- α = 0.05

**Use two-sample Z-test (large samples)**

---

#### Using Critical Region Technique

**Formula:** Z = (x̄₁ - x̄₂) / √[(s₁²/n₁) + (s₂²/n₂)]

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = √[(s₁²/n₁) + (s₂²/n₂)]
SE = √[(20²/50) + (25²/40)]
SE = √[(400/50) + (625/40)]
SE = √[8 + 15.625]
SE = √23.625
SE = 4.861

Z = (280 - 260) / 4.861
Z = 20 / 4.861
Z = 4.114
```

2. **Determine critical value:**
   - Right-tailed test, α = 0.05
   - Z₀.₀₅ = 1.645
   - Critical region: Z > 1.645

3. **Decision:**
```
Z = 4.114 > 1.645
Falls in critical region
```

**Decision: REJECT H₀**

**Conclusion:** There is very strong evidence (Z = 4.114) at the 0.05 significance level to support the claim that Battery A lasts longer than Battery B. The difference of 20 hours is statistically significant.

---

### Question 11
**Compare sugar content in two cereal brands. Brand X: n=30, x̄=12, s=3. Brand Y: n=25, x̄=10, s=4. Test at α = 0.01.**

**Given:**
- H₀: μ₁ = μ₂
- H₁: μ₁ ≠ μ₂ (two-tailed test)
- Brand X: n₁ = 30, x̄₁ = 12, s₁ = 3
- Brand Y: n₂ = 25, x̄₂ = 10, s₂ = 4
- α = 0.01

---

#### Using P-value Technique

**Step-by-step:**

1. **Calculate test statistic:**
```
SE = √[(s₁²/n₁) + (s₂²/n₂)]
SE = √[(3²/30) + (4²/25)]
SE = √[(9/30) + (16/25)]
SE = √[0.3 + 0.64]
SE = √0.94
SE = 0.970

Z = (12 - 10) / 0.970
Z = 2 / 0.970
Z = 2.062
```

2. **Find p-value (two-tailed):**
```
P(Z > 2.062) = 0.0197
P-value = 2 × 0.0197 = 0.0394
```

3. **Decision:**
```
P-value (0.0394) > α (0.01)
```

**Decision: FAIL TO REJECT H₀**

**Conclusion:** There is NOT sufficient evidence at the 0.01 significance level to conclude that the average sugar content is different between Brand X and Brand Y. Although Brand X appears to have higher sugar content (12g vs 10g), this difference is not statistically significant at the very strict 0.01 level.

---

### Question 12
**Compare two promotional strategies. Strategy 1: 45, 50, 55, 40, 60. Strategy 2: 55, 60, 65, 57, 62. Test at α = 0.01.**

**Given:**
- Strategy 1: 45, 50, 55, 40, 60
- Strategy 2: 55, 60, 65, 57, 62
- α = 0.01

**This is a two-sample t-test (small samples, independent groups)**

---

#### Using Critical Region Technique

**Step-by-step:**

1. **Calculate sample statistics:**

**Strategy 1:**
```
x̄₁ = (45 + 50 + 55 + 40 + 60) / 5 = 250 / 5 = 50
n₁ = 5

Variance calculation:
(45-50)² = 25
(50-50)² = 0
(55-50)² = 25
(40-50)² = 100
(60-50)² = 100
Sum = 250

s₁² = 250 / (5-1) = 250 / 4 = 62.5
s₁ = 7.91
```

**Strategy 2:**
```
x̄₂ = (55 + 60 + 65 + 57 + 62) / 5 = 299 / 5 = 59.8
n₂ = 5

Variance calculation:
(55-59.8)² = 23.04
(60-59.8)² = 0.04
(65-59.8)² = 27.04
(57-59.8)² = 7.84
(62-59.8)² = 4.84
Sum = 62.8

s₂² = 62.8 / 4 = 15.7
s₂ = 3.96
```

2. **Calculate pooled standard deviation:**
```
sp² = [(n₁-1)s₁² + (n₂-1)s₂²] / (n₁ + n₂ - 2)
sp² = [(4 × 62.5) + (4 × 15.7)] / 8
sp² = [250 + 62.8] / 8
sp² = 312.8 / 8
sp² = 39.1

sp = 6.253
```

3. **Calculate test statistic:**
```
SE = sp × √(1/n₁ + 1/n₂)
SE = 6.253 × √(1/5 + 1/5)
SE = 6.253 × √0.4
SE = 6.253 × 0.632
SE = 3.952

t = (x̄₁ - x̄₂) / SE
t = (50 - 59.8) / 3.952
t = -9.8 / 3.952
t = -2.479
```

4. **Determine critical values:**
   - Two-tailed test, α = 0.01, df = 5 + 5 - 2 = 8
   - t₀.₀₀₅,₈ = ±3.355
   - Critical region: t < -3.355 or t > 3.355

5. **Decision:**
```
t = -2.479
-3.355 < -2.479 < 3.355
Does NOT fall in critical region
```

**Decision: FAIL TO REJECT H₀**

**Conclusion:** There is NOT sufficient evidence at the 0.01 significance level to conclude that one promotional strategy leads to significantly higher average sales than the other. While Strategy 2 shows higher sales (59.8 vs 50), the difference is not statistically significant at the very strict 0.01 level.

---

### Question 13
**Test effectiveness of new study technique. 15 students before/after scores. Test at α = 0.01.**

**Given:**
- Before: 70, 75, 80, 85, 90, 65, 75, 80, 85, 78, 88, 92, 84, 76, 82
- After: 78, 80, 85, 90, 94, 70, 80, 84, 89, 82, 90, 95, 88, 80, 86
- H₀: μd ≤ 0 (no improvement)
- H₁: μd > 0 (improvement) (right-tailed test)
- α = 0.01, n = 15, df = 14

**This is a paired sample t-test**

---

#### Using Critical Region Technique

**Step-by-step:**

1. **Calculate differences (After - Before):**

| Student | Before | After | d = After - Before |
|---------|--------|-------|-------------------|
| 1 | 70 | 78 | 8 |
| 2 | 75 | 80 | 5 |
| 3 | 80 | 85 | 5 |
| 4 | 85 | 90 | 5 |
| 5 | 90 | 94 | 4 |
| 6 | 65 | 70 | 5 |
| 7 | 75 | 80 | 5 |
| 8 | 80 | 84 | 4 |
| 9 | 85 | 89 | 4 |
| 10 | 78 | 82 | 4 |
| 11 | 88 | 90 | 2 |
| 12 | 92 | 95 | 3 |
| 13 | 84 | 88 | 4 |
| 14 | 76 | 80 | 4 |
| 15 | 82 | 86 | 4 |

2. **Calculate mean difference:**
```
Σd = 8+5+5+5+4+5+5+4+4+4+2+3+4+4+4 = 66
d̄ = 66 / 15 = 4.4
```

3. **Calculate standard deviation of differences:**
```
(d - d̄)²:
(8-4.4)² = 12.96
(5-4.4)² = 0.36
(5-4.4)² = 0.36
(5-4.4)² = 0.36
(4-4.4)² = 0.16
(5-4.4)² = 0.36
(5-4.4)² = 0.36
(4-4.4)² = 0.16
(4-4.4)² = 0.16
(4-4.4)² = 0.16
(2-4.4)² = 5.76
(3-4.4)² = 1.96
(4-4.4)² = 0.16
(4-4.4)² = 0.16
(4-4.4)² = 0.16
Sum = 23.6

sd² = 23.6 / 14 = 1.686
sd = 1.299
```

4. **Calculate test statistic:**
```
SE = sd/√n = 1.299/√15 = 1.299/3.873 = 0.335

t = (d̄ - 0) / SE
t = 4.4 / 0.335
t = 13.134
```

5. **Determine critical value:**
   - Right-tailed, α = 0.01, df = 14
   - t₀.₀₁,₁₄ = 2.624
   - Critical region: t > 2.624

6. **Decision:**
```
t = 13.134 > 2.624
Falls in critical region
```

**Decision: REJECT H₀**

**Conclusion:** There is extremely strong evidence (t = 13.134) at the 0.01 significance level to conclude that the new study technique significantly improves students' test scores. The average improvement is 4.4 points, which is highly statistically significant.

---

### Question 14
**Health program weight loss. 10 participants before/after weights. Test at α = 0.05.**

**Given:**
- Before: 80, 75, 90, 85, 70, 95, 88, 82, 77, 92
- After: 78, 74, 85, 82, 68, 91, 86, 80, 75, 90
- H₀: μd ≤ 0 (no weight loss)
- H₁: μd > 0 (weight loss) (right-tailed test)
- α = 0.05, n = 10, df = 9

**Paired sample t-test**

---

**Step-by-step:**

1. **Calculate differences (Before - After):**

| Participant | Before | After | d = Before - After |
|------------|--------|-------|-------------------|
| 1 | 80 | 78 | 2 |
| 2 | 75 | 74 | 1 |
| 3 | 90 | 85 | 5 |
| 4 | 85 | 82 | 3 |
| 5 | 70 | 68 | 2 |
| 6 | 95 | 91 | 4 |
| 7 | 88 | 86 | 2 |
| 8 | 82 | 80 | 2 |
| 9 | 77 | 75 | 2 |
| 10 | 92 | 90 | 2 |

2. **Calculate statistics:**
```
Σd = 2+1+5+3+2+4+2+2+2+2 = 25
d̄ = 25 / 10 = 2.5

Calculate variance:
(2-2.5)² = 0.25
(1-2.5)² = 2.25
(5-2.5)² = 6.25
(3-2.5)² = 0.25
(2-2.5)² = 0.25
(4-2.5)² = 2.25
(2-2.5)² = 0.25
(2-2.5)² = 0.25
(2-2.5)² = 0.25
(2-2.5)² = 0.25
Sum = 12.5

sd² = 12.5 / 9 = 1.389
sd = 1.178
```

3. **Calculate test statistic:**
```
SE = sd/√n = 1.178/√10 = 1.178/3.162 = 0.373

t = 2.5 / 0.373 = 6.702
```

4. **Critical value:**
   - t₀.₀₅,₉ = 1.833
   - Critical region: t > 1.833

5. **Decision:**
```
t = 6.702 > 1.833
REJECT H₀
```

**Conclusion:** There is very strong evidence (t = 6.702, p < 0.001) at the 0.05 significance level to conclude that the health program has resulted in significant weight loss. The average weight loss is 2.5 kg.

---

### Question 15
**City A vs City B smokers proportion. City A: 80/200. City B: 50/250. Test at α = 0.05.**

**Given:**
- H₀: p₁ ≤ p₂
- H₁: p₁ > p₂ (right-tailed test)
- City A: x₁ = 80, n₁ = 200, p̂₁ = 0.40
- City B: x₂ = 50, n₂ = 250, p̂₂ = 0.20
- α = 0.05

---

#### Using Critical Region Technique

**Step-by-step:**

1. **Calculate pooled proportion:**
```
p̂ = (x₁ + x₂) / (n₁ + n₂)
p̂ = (80 + 50) / (200 + 250)
p̂ = 130 / 450
p̂ = 0.289
```

2. **Calculate test statistic:**
```
SE = √[p̂(1-p̂)(1/n₁ + 1/n₂)]
SE = √[0.289 × 0.711 × (1/200 + 1/250)]
SE = √[0.205 × (0.005 + 0.004)]
SE = √[0.205 × 0.009]
SE = √0.001845
SE = 0.043

Z = (p̂₁ - p̂₂) / SE
Z = (0.40 - 0.20) / 0.043
Z = 0.20 / 0.043
Z = 4.651
```

3. **Determine critical value:**
   - Right-tailed, α = 0.05
   - Z₀.₀₅ = 1.645
   - Critical region: Z > 1.645

4. **Decision:**
```
Z = 4.651 > 1.645
Falls in critical region
```

**Decision: REJECT H₀**

**Conclusion:** There is very strong evidence (Z = 4.651) at the 0.05 significance level to support the claim that the proportion of smokers in City A (40%) is significantly higher than in City B (20%).

---

### Question 16
**Same as Question 15, but using P-value technique**

**Given:** Same data as Question 15
- Z = 4.651 (calculated above)

---

#### Using P-value Technique

**Step-by-step:**

1. **Test statistic:** Z = 4.651 (from Question 15)

2. **Find p-value (right-tailed):**
```
P(Z > 4.651) ≈ 0.000002
P-value ≈ 0.000002 (essentially 0)
```

3. **Decision:**
```
P-value (0.000002) < α (0.05)
```

**Decision: REJECT H₀**

**Conclusion:** The p-value is extremely small (p < 0.000002), providing overwhelming evidence to support the claim that the proportion of smokers in City A is significantly higher than in City B. The difference of 20 percentage points (40% vs 20%) is highly statistically significant.

---

### Question 17
**Marketing campaign in two regions. Region 1: 150/500. Region 2: 180/600. Test at α = 0.01.**

**Given:**
- H₀: p₁ = p₂
- H₁: p₁ ≠ p₂ (two-tailed test)
- Region 1: x₁ = 150, n₁ = 500, p̂₁ = 0.30
- Region 2: x₂ = 180, n₂ = 600, p̂₂ = 0.30
- α = 0.01

---

#### Using P-value Technique

**Step-by-step:**

1. **Calculate pooled proportion:**
```
p̂ = (x₁ + x₂) / (n₁ + n₂)
p̂ = (150 + 180) / (500 + 600)
p̂ = 330 / 1100
p̂ = 0.30
```

2. **Calculate test statistic:**
```
SE = √[p̂(1-p̂)(1/n₁ + 1/n₂)]
SE = √[0.30 × 0.70 × (1/500 + 1/600)]
SE = √[0.21 × (0.002 + 0.00167)]
SE = √[0.21 × 0.00367]
SE = √0.000771
SE = 0.0278

Z = (p̂₁ - p̂₂) / SE
Z = (0.30 - 0.30) / 0.0278
Z = 0 / 0.0278
Z = 0
```

3. **Find p-value (two-tailed):**
```
P(Z = 0) = 0.50
P-value = 2 × 0.50 = 1.00
```

4. **Decision:**
```
P-value (1.00) > α (0.01)
```

**Decision: FAIL TO REJECT H₀**

**Conclusion:** There is NO evidence (p = 1.00) at the 0.01 significance level to suggest that the proportions of individuals expressing a positive opinion differ between the two regions. Both regions show exactly 30% positive opinion, indicating the marketing campaign has equal effectiveness in both regions.

---

**END OF UNIT 4 - ALL QUESTIONS COMPLETED**

---
