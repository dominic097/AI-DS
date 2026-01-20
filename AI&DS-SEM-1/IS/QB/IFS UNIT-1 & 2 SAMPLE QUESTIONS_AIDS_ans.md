# IFS UNIT-1 & 2 SAMPLE QUESTIONS - ANSWER SHEET

## Question 1
**Calculate mean, median, mode, range, quartile deviation, standard deviation, variance and the coefficient of quartile deviation, standard deviation, coefficient of variation, measures of skewness and measures of kurtosis for the following data. Also find the Covariance & Correlation Co-efficient.**

| Sales | 15 | 18 | 25 | 27 | 30 | 35 |
|---|---|---|---|---|---|---|
| Expenditure | 50 | 65 | 82 | 95 | 110 | 120 |

**Answer:**

**For Sales (X):**
- **Mean (X̄)** = (15 + 18 + 25 + 27 + 30 + 35) / 6 = 150 / 6 = **25**
- **Median**: Arrange in order: 15, 18, 25, 27, 30, 35
  - Median = (25 + 27) / 2 = **26**
- **Mode**: No repeated values, so **No mode**
- **Range** = Maximum - Minimum = 35 - 15 = **20**

**For Expenditure (Y):**
- **Mean (Ȳ)** = (50 + 65 + 82 + 95 + 110 + 120) / 6 = 522 / 6 = **87**
- **Median**: 50, 65, 82, 95, 110, 120
  - Median = (82 + 95) / 2 = **88.5**
- **Mode**: **No mode**
- **Range** = 120 - 50 = **70**

**Variance for Sales:**
- Deviations from mean: -10, -7, 0, 2, 5, 10
- Squared deviations: 100, 49, 0, 4, 25, 100
- Variance (σ²) = 278 / 6 = **46.33**

**Standard Deviation for Sales:**
- σ = √46.33 = **6.81**

**Variance for Expenditure:**
- Deviations: -37, -22, -5, 8, 23, 33
- Squared deviations: 1369, 484, 25, 64, 529, 1089
- Variance = 3560 / 6 = **593.33**

**Standard Deviation for Expenditure:**
- σ = √593.33 = **24.36**

**Quartiles for Sales:**
- Q1 = 18, Q2 = 26, Q3 = 30
- **Quartile Deviation** = (Q3 - Q1) / 2 = (30 - 18) / 2 = **6**
- **Coefficient of Quartile Deviation** = (Q3 - Q1) / (Q3 + Q1) = 12/48 = **0.25**

**Coefficient of Variation:**
- **CV for Sales** = (σ/X̄) × 100 = (6.81/25) × 100 = **27.24%**
- **CV for Expenditure** = (24.36/87) × 100 = **28.0%**

**Covariance:**
- Cov(X,Y) = Σ[(Xi - X̄)(Yi - Ȳ)] / n
- = [(-10)(-37) + (-7)(-22) + (0)(-5) + (2)(8) + (5)(23) + (10)(33)] / 6
- = [370 + 154 + 0 + 16 + 115 + 330] / 6
- = 985 / 6 = **164.17**

**Correlation Coefficient:**
- r = Cov(X,Y) / (σx × σy)
- r = 164.17 / (6.81 × 24.36)
- r = 164.17 / 165.89 = **0.989**
- This indicates a **very strong positive correlation**.

**Coefficient of Skewness:**
- Pearson's Coefficient = 3(Mean - Median) / SD
- For Sales: 3(25 - 26) / 6.81 = **-0.44** (slightly negatively skewed)
- For Expenditure: 3(87 - 88.5) / 24.36 = **-0.18** (nearly symmetric)

**Kurtosis**: For small datasets, kurtosis calculation requires fourth moment. Generally classified as:
- Mesokurtic (normal distribution) if ≈ 3
- The given data appears to be **mesokurtic** based on distribution pattern.

---

## Question 2
**Calculate 5 point summary for the given data. Also find quartile ranges and IQR for given data.**

| X | 1 | 3 | 5 | 7 | 8 | 10 |
|---|---|---|---|---|---|---|
| Y | 8 | 12 | 15 | 17 | 18 | 20 |

**Answer:**

**For X:**
- **Minimum** = 1
- **Q1 (First Quartile)** = Position (6+1)×0.25 = 1.75 → Q1 = 1 + 0.75(3-1) = **2.5**
- **Q2 (Median)** = (5 + 7) / 2 = **6**
- **Q3 (Third Quartile)** = Position (6+1)×0.75 = 5.25 → Q3 = 8 + 0.25(10-8) = **8.5**
- **Maximum** = 10

**5-Point Summary for X: (1, 2.5, 6, 8.5, 10)**

**IQR for X** = Q3 - Q1 = 8.5 - 2.5 = **6**

**For Y:**
- **Minimum** = 8
- **Q1** = 8 + 0.75(12-8) = **11**
- **Q2 (Median)** = (15 + 17) / 2 = **16**
- **Q3** = 18 + 0.25(20-18) = **18.5**
- **Maximum** = 20

**5-Point Summary for Y: (8, 11, 16, 18.5, 20)**

**IQR for Y** = Q3 - Q1 = 18.5 - 11 = **7.5**

---

## Question 3
**The competitors in a musical contest were ranked by 3 judges. Which pair of judges have more or less the same taste in music?**

| S.No. | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Rank by Judge A | 6 | 5 | 3 | 10 | 2 | 4 | 9 | 7 | 8 | 1 |
| Rank by Judge B | 5 | 8 | 4 | 7 | 10 | 2 | 1 | 6 | 9 | 3 |
| Rank by Judge C | 4 | 9 | 8 | 1 | 2 | 3 | 10 | 5 | 7 | 6 |

**Answer:**

Using **Spearman's Rank Correlation Coefficient**: rs = 1 - (6Σd²) / (n(n²-1))

**For Judges A and B:**
| d (A-B) | 1 | -3 | -1 | 3 | -8 | 2 | 8 | 1 | -1 | -2 |
|---|---|---|---|---|---|---|---|---|---|---|
| d² | 1 | 9 | 1 | 9 | 64 | 4 | 64 | 1 | 1 | 4 |

Σd² = 158
rs(A,B) = 1 - (6 × 158) / (10 × 99) = 1 - 948/990 = 1 - 0.958 = **0.042**

**For Judges A and C:**
| d (A-C) | 2 | -4 | -5 | 9 | 0 | 1 | -1 | 2 | 1 | -5 |
|---|---|---|---|---|---|---|---|---|---|---|
| d² | 4 | 16 | 25 | 81 | 0 | 1 | 1 | 4 | 1 | 25 |

Σd² = 158
rs(A,C) = 1 - (6 × 158) / 990 = **0.042**

**For Judges B and C:**
| d (B-C) | 1 | -1 | -4 | 6 | 8 | -1 | -9 | 1 | 2 | -3 |
|---|---|---|---|---|---|---|---|---|---|---|
| d² | 1 | 1 | 16 | 36 | 64 | 1 | 81 | 1 | 4 | 9 |

Σd² = 214
rs(B,C) = 1 - (6 × 214) / 990 = 1 - 1284/990 = 1 - 1.297 = **-0.297**

**Conclusion:** **Judges A and C** have more or less the same taste in music (both have correlation = 0.042), while Judge B has different taste from both A and C.

---

## Question 4
**Find the probability of drawing two red balls in succession from a bag containing 3 red and 6 black balls when (i) the ball that is drawn first is replaced, (ii) it is not replaced.**

**Answer:**

Total balls = 3 red + 6 black = 9 balls

**(i) With Replacement:**
- P(1st red) = 3/9 = 1/3
- P(2nd red | 1st red) = 3/9 = 1/3 (ball is replaced)
- P(both red) = (1/3) × (1/3) = **1/9 ≈ 0.111**

**(ii) Without Replacement:**
- P(1st red) = 3/9 = 1/3
- P(2nd red | 1st red) = 2/8 = 1/4 (one red ball removed)
- P(both red) = (1/3) × (1/4) = **1/12 ≈ 0.0833**

---

## Question 5
**A bag contains 3 red and 4 white balls. Two draws are made without replacement; what is the probability that both the balls are red?**

**Answer:**

Total balls = 3 red + 4 white = 7 balls

- P(1st red) = 3/7
- P(2nd red | 1st red) = 2/6 = 1/3
- P(both red) = (3/7) × (1/3) = **3/21 = 1/7 ≈ 0.143**

---

## Question 6
**Box 1 contains 1000 bulbs of which 10% are defective. Box 2 contains 2000 bulbs of which 5% are defective. Two bulbs are drawn (without replacement) from a randomly selected box.**

**(i) Find the probability that both bulbs are defective**
**(ii) Assuming that both are defective, find the probability that they came from box 1.**

**Answer:**

**Given:**
- Box 1: 1000 bulbs, 10% defective = 100 defective, 900 good
- Box 2: 2000 bulbs, 5% defective = 100 defective, 1900 good
- P(Box 1) = P(Box 2) = 0.5

**(i) P(both defective):**

From Box 1:
- P(both defective | Box 1) = (100/1000) × (99/999) = 0.1 × 0.099 = 0.0099

From Box 2:
- P(both defective | Box 2) = (100/2000) × (99/1999) = 0.05 × 0.0495 = 0.002475

P(both defective) = P(Box 1) × P(both def | Box 1) + P(Box 2) × P(both def | Box 2)
= 0.5 × 0.0099 + 0.5 × 0.002475
= 0.00495 + 0.0012375
= **0.0062 or 0.62%**

**(ii) P(Box 1 | both defective):**

Using Bayes' theorem:
P(Box 1 | both def) = P(both def | Box 1) × P(Box 1) / P(both def)
= (0.0099 × 0.5) / 0.0062
= 0.00495 / 0.0062
= **0.798 or 79.8%**

---

## Question 7
**Explain various types of sampling with examples**

**Answer:**

Sampling is the process of selecting a subset of individuals from a population to estimate characteristics of the whole population.

**1. Probability Sampling Methods:**

**a) Simple Random Sampling:**
- Every member has equal chance of selection
- **Example:** Drawing names from a hat; using random number generator to select 100 students from 1000

**b) Systematic Sampling:**
- Select every kth element from the population
- **Example:** Selecting every 10th person from a membership list

**c) Stratified Sampling:**
- Population divided into homogeneous subgroups (strata), then random sampling from each
- **Example:** Dividing students by year (freshman, sophomore, etc.) and sampling from each group proportionally

**d) Cluster Sampling:**
- Population divided into clusters, randomly select clusters, then sample all or some within selected clusters
- **Example:** Selecting random schools from a district, then surveying all students in selected schools

**2. Non-Probability Sampling Methods:**

**a) Convenience Sampling:**
- Select easily accessible subjects
- **Example:** Surveying people at a shopping mall entrance

**b) Purposive/Judgmental Sampling:**
- Researcher uses judgment to select subjects
- **Example:** Selecting experienced doctors for a medical study

**c) Quota Sampling:**
- Select subjects to fill quotas for subgroups
- **Example:** Ensuring 50 males and 50 females in a survey

**d) Snowball Sampling:**
- Existing subjects recruit future subjects
- **Example:** Drug users referring other drug users for a study

**Advantages & Disadvantages:**
- Probability sampling provides statistical validity but may be expensive
- Non-probability sampling is cheaper and faster but may introduce bias

---

## Question 8
**Explain different types of probability with example**

**Answer:**

**1. Classical (Theoretical) Probability:**
- Based on equally likely outcomes
- P(E) = Number of favorable outcomes / Total number of possible outcomes
- **Example:** Probability of rolling a 4 on a fair die = 1/6

**2. Empirical (Experimental) Probability:**
- Based on observations or experiments
- P(E) = Number of times event occurs / Total number of trials
- **Example:** Flipping a coin 100 times and getting 53 heads, P(Heads) = 53/100 = 0.53

**3. Subjective Probability:**
- Based on personal judgment, intuition, or experience
- **Example:** A doctor estimating 70% chance of patient recovery based on experience

**4. Conditional Probability:**
- Probability of event A given event B has occurred
- P(A|B) = P(A ∩ B) / P(B)
- **Example:** Probability of rain today given it rained yesterday

**5. Joint Probability:**
- Probability of two events occurring together
- P(A ∩ B)
- **Example:** Probability of drawing a red card that is also a king from a deck

**6. Marginal Probability:**
- Probability of a single event regardless of other events
- **Example:** Total probability of selecting a male from a population

**7. Complementary Probability:**
- P(A') = 1 - P(A)
- **Example:** If P(passing exam) = 0.8, then P(failing) = 0.2

**Key Probability Rules:**
- **Addition Rule:** P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- **Multiplication Rule:** P(A ∩ B) = P(A) × P(B|A)
- For independent events: P(A ∩ B) = P(A) × P(B)

---

## Question 9
**Explain about different measure of central tendency, dispersion and distribution with example**

**Answer:**

### **A. Measures of Central Tendency:**

**1. Mean (Arithmetic Average):**
- Sum of all values divided by number of values
- Formula: X̄ = ΣX / n
- **Example:** Scores: 10, 20, 30, 40, 50 → Mean = 150/5 = 30
- **Advantage:** Uses all data points
- **Disadvantage:** Affected by outliers

**2. Median:**
- Middle value when data is arranged in order
- **Example:** 10, 20, 30, 40, 50 → Median = 30
- **Advantage:** Not affected by outliers
- **Disadvantage:** Ignores extreme values

**3. Mode:**
- Most frequently occurring value
- **Example:** 10, 20, 20, 30, 40 → Mode = 20
- **Advantage:** Can be used for categorical data
- **Disadvantage:** May not exist or may have multiple modes

### **B. Measures of Dispersion:**

**1. Range:**
- Difference between maximum and minimum
- **Example:** 10, 20, 30, 40, 50 → Range = 50 - 10 = 40
- **Limitation:** Only uses two values

**2. Variance (σ²):**
- Average of squared deviations from mean
- Formula: σ² = Σ(X - X̄)² / n
- **Example:** For {10, 20, 30}, mean = 20
  - Variance = [(10-20)² + (20-20)² + (30-20)²] / 3 = 200/3 = 66.67

**3. Standard Deviation (σ):**
- Square root of variance
- **Example:** σ = √66.67 = 8.16
- **Advantage:** Same unit as original data

**4. Coefficient of Variation (CV):**
- (SD / Mean) × 100
- **Example:** CV = (8.16/20) × 100 = 40.8%
- **Use:** Comparing variability between different datasets

**5. Quartile Deviation:**
- (Q3 - Q1) / 2
- Measures spread of middle 50% of data

**6. Interquartile Range (IQR):**
- Q3 - Q1
- Used to identify outliers

### **C. Measures of Distribution:**

**1. Skewness (Asymmetry):**

**Types:**
- **Positive Skew (Right-skewed):** Mean > Median > Mode
  - Tail extends to right
  - **Example:** Income distribution (few very high earners)

- **Negative Skew (Left-skewed):** Mode > Median > Mean
  - Tail extends to left
  - **Example:** Age at retirement (most retire around 65, few retire early)

- **Symmetric:** Mean = Median = Mode
  - **Example:** Height distribution in a population

**Coefficient of Skewness:**
- Pearson's: SK = 3(Mean - Median) / SD
- SK = 0: Symmetric
- SK > 0: Positively skewed
- SK < 0: Negatively skewed

**2. Kurtosis (Peakedness):**

**Types:**
- **Leptokurtic:** Sharp peak, heavy tails (Kurtosis > 3)
  - **Example:** Stock returns during volatile periods

- **Mesokurtic:** Normal distribution (Kurtosis = 3)
  - **Example:** Heights, test scores

- **Platykurtic:** Flat peak, light tails (Kurtosis < 3)
  - **Example:** Uniform distribution

**Practical Applications:**
- **Quality Control:** Use mean and SD to set control limits
- **Finance:** Use variance to measure investment risk
- **Research:** Check skewness and kurtosis to determine appropriate statistical tests

---

## Question 10
**A factory produces three types of electronic devices - X, Y, and Z. The probability of producing a defective device of type X is 0.01, of type Y is 0.04, and of type Z is 0.02. If a defective device has been identified, the probability that it is a type X device is 0.5, the probability for type Y is 0.3, and for type Z is 0.2. If a defective device is picked up from the factory, what is the most likely type of device?**

**Answer:**

**Given:**
- P(Defective | X) = 0.01
- P(Defective | Y) = 0.04
- P(Defective | Z) = 0.02
- P(X | Defective) = 0.5
- P(Y | Defective) = 0.3
- P(Z | Defective) = 0.2

**Analysis:**
The question already provides the posterior probabilities:
- P(X | Defective) = 0.5 = **50%**
- P(Y | Defective) = 0.3 = **30%**
- P(Z | Defective) = 0.2 = **20%**

**Conclusion:**
Since P(X | Defective) = 0.5 is the highest probability, **Type X is the most likely device** when a defective device is picked.

This might seem counterintuitive since Type Y has the highest defect rate (0.04), but it indicates that **Type X devices are produced in much larger quantities** than the other types, making them the most likely source of any randomly selected defective device.

---

## Question 11
**A quality control department inspects three types of food products - D, E, and F. The probability of finding a defective product of type D is 0.03, of type E is 0.01, and of type F is 0.04. If a defective product is found, the probability that it is a type D product is 0.2, that it is type E is 0.5, and type F is 0.3. If a defective product is selected, what is the most likely type of food product it belongs to?**

**Answer:**

**Given Posterior Probabilities:**
- P(D | Defective) = 0.2 = **20%**
- P(E | Defective) = 0.5 = **50%**
- P(F | Defective) = 0.3 = **30%**

**Analysis:**
Comparing the posterior probabilities:
- Type E: 50% (highest)
- Type F: 30%
- Type D: 20%

**Conclusion:**
**Type E is the most likely type of food product** when a defective product is selected, with a 50% probability.

Despite Type E having the lowest defect rate (0.01), it accounts for half of all defective products found. This indicates that **Type E products are produced in significantly larger quantities** compared to Types D and F, making them the dominant contributor to the overall defective product pool.

---

## Question 12
**A certain building has an average of 2 fire alarm activations per week. What is the probability that exactly 3 fire alarms will activate in a week?**

**Answer:**

This follows a **Poisson Distribution**: P(X = k) = (λᵏ × e⁻λ) / k!

**Given:**
- λ (average rate) = 2 activations per week
- k (desired occurrences) = 3

**Calculation:**
P(X = 3) = (2³ × e⁻²) / 3!
= (8 × e⁻²) / 6
= 8 × 0.1353 / 6
= 1.0824 / 6
= **0.1804 or 18.04%**

**Conclusion:**
The probability of exactly 3 fire alarm activations in a week is approximately **18.04%** or about **0.18**.

---

## Question 13
**A coffee shop receives an average of 10 customers every hour. What is the probability that exactly 15 customers will arrive in a given hour?**

**Answer:**

Using **Poisson Distribution**: P(X = k) = (λᵏ × e⁻λ) / k!

**Given:**
- λ = 10 customers per hour
- k = 15 customers

**Calculation:**
P(X = 15) = (10¹⁵ × e⁻¹⁰) / 15!

Step by step:
- e⁻¹⁰ ≈ 0.0000454
- 10¹⁵ = 1,000,000,000,000,000
- 15! = 1,307,674,368,000

P(X = 15) = (10¹⁵ × 0.0000454) / 1,307,674,368,000
= 45,400,000,000 / 1,307,674,368,000
= **0.0347 or 3.47%**

**Conclusion:**
The probability of exactly 15 customers arriving in a given hour is approximately **3.47%** or about **0.035**.

This is relatively low because 15 is significantly higher than the average of 10 customers per hour.

---

## Question 14
**A nutritionist is investigating the impact of two factors "Calorie Intake" and "Exercise Hours" on individuals' Weight Loss Progress". The following data is collected for 4 individuals over a specific time period. Determine which independent variable (Calorie Intake or Exercise Hours) has a stronger relationship with Weight Loss Progress.**

| Individual | Calorie Intake | Exercise Hours | Weight Loss (kg) |
|---|---|---|---|
| 1 | 2500 | 2 | 1 |
| 2 | 2200 | 4 | 2 |
| 3 | 2000 | 6 | 4 |
| 4 | 1800 | 8 | 6 |

**Answer:**

We'll calculate the **correlation coefficient** for both relationships.

**1. Correlation between Calorie Intake and Weight Loss:**

| Calorie Intake (X) | Weight Loss (Y) | X - X̄ | Y - Ȳ | (X-X̄)(Y-Ȳ) | (X-X̄)² | (Y-Ȳ)² |
|---|---|---|---|---|---|---|
| 2500 | 1 | 375 | -2.25 | -843.75 | 140625 | 5.0625 |
| 2200 | 2 | 75 | -1.25 | -93.75 | 5625 | 1.5625 |
| 2000 | 4 | -125 | 0.75 | -93.75 | 15625 | 0.5625 |
| 1800 | 6 | -325 | 2.75 | -893.75 | 105625 | 7.5625 |

- X̄ = 2125, Ȳ = 3.25
- Σ(X-X̄)(Y-Ȳ) = -1925
- Σ(X-X̄)² = 267500
- Σ(Y-Ȳ)² = 14.75

r₁ = -1925 / √(267500 × 14.75)
= -1925 / √3945625
= -1925 / 1986.36
= **-0.969**

**2. Correlation between Exercise Hours and Weight Loss:**

| Exercise Hours (X) | Weight Loss (Y) | X - X̄ | Y - Ȳ | (X-X̄)(Y-Ȳ) | (X-X̄)² | (Y-Ȳ)² |
|---|---|---|---|---|---|---|
| 2 | 1 | -3 | -2.25 | 6.75 | 9 | 5.0625 |
| 4 | 2 | -1 | -1.25 | 1.25 | 1 | 1.5625 |
| 6 | 4 | 1 | 0.75 | 0.75 | 1 | 0.5625 |
| 8 | 6 | 3 | 2.75 | 8.25 | 9 | 7.5625 |

- X̄ = 5, Ȳ = 3.25
- Σ(X-X̄)(Y-Ȳ) = 17
- Σ(X-X̄)² = 20
- Σ(Y-Ȳ)² = 14.75

r₂ = 17 / √(20 × 14.75)
= 17 / √295
= 17 / 17.18
= **+0.989**

**Conclusion:**

| Variable | Correlation Coefficient | Strength |
|---|---|---|
| Calorie Intake | -0.969 | Very strong negative |
| Exercise Hours | +0.989 | Very strong positive |

**Exercise Hours has a stronger relationship with Weight Loss Progress** (r = 0.989), showing a nearly perfect positive correlation. This means that as exercise hours increase, weight loss increases proportionally.

Calorie Intake also shows a very strong relationship (r = -0.969), but it's negative, meaning lower calorie intake is associated with higher weight loss.

In terms of **absolute strength**: |0.989| > |0.969|, so **Exercise Hours is slightly stronger**.

---

## Question 15
**For the given data:**

|  | Mathematics (M) | Science (S) | Arts (A) |
|---|---|---|---|
| Male | 30 | 50 | 20 |
| Female | 20 | 30 | 50 |

**A. What is the probability that a randomly chosen student is enrolled in Science (S)?**

**Answer:**
Total students = 30 + 50 + 20 + 20 + 30 + 50 = 200
Students in Science = 50 + 30 = 80
P(Science) = 80/200 = **0.4 or 40%**

**B. What is the probability that a randomly chosen student is Female?**

**Answer:**
Total females = 20 + 30 + 50 = 100
P(Female) = 100/200 = **0.5 or 50%**

**C. What is the probability that a randomly chosen student is a Male enrolled in Mathematics (M)?**

**Answer:**
Males in Mathematics = 30
P(Male AND Math) = 30/200 = **0.15 or 15%**

**D. What is the probability that a randomly chosen student is a Female enrolled in Arts (A)?**

**Answer:**
Females in Arts = 50
P(Female AND Arts) = 50/200 = **0.25 or 25%**

**E. What is the probability that a student is Male given that the student is enrolled in Science (S)?**

**Answer:**
This is conditional probability: P(Male | Science)
Males in Science = 50
Total in Science = 80
P(Male | Science) = 50/80 = **0.625 or 62.5%**

**F. What is the probability that a student is enrolled in Mathematics (M) given that the student is Female?**

**Answer:**
P(Math | Female)
Females in Math = 20
Total females = 100
P(Math | Female) = 20/100 = **0.2 or 20%**

---

## Question 16
**For the given data find:**

|  | Cars | Motorcycles | Bicycles |
|---|---|---|---|
| Families with Children | 90 | 30 | 20 |
| Families without Children | 80 | 50 | 30 |

**a. What is the probability that a randomly selected family owns a motorcycle?**

**Answer:**
Total families = 90 + 30 + 20 + 80 + 50 + 30 = 300
Families with motorcycles = 30 + 50 = 80
P(Motorcycle) = 80/300 = **0.267 or 26.7%**

**b. What is the probability that a randomly selected family has children?**

**Answer:**
Families with children = 90 + 30 + 20 = 140
P(Children) = 140/300 = **0.467 or 46.7%**

**c. What is the probability that a randomly chosen family owns a car and has children?**

**Answer:**
Families with car AND children = 90
P(Car AND Children) = 90/300 = **0.3 or 30%**

**d. What is the probability that a randomly chosen family owns a bicycle and does not have children?**

**Answer:**
Families with bicycle AND no children = 30
P(Bicycle AND No Children) = 30/300 = **0.1 or 10%**

**e. What is the probability that a family has children given that they own a car?**

**Answer:**
P(Children | Car)
Families with cars = 90 + 80 = 170
Families with cars AND children = 90
P(Children | Car) = 90/170 = **0.529 or 52.9%**

**f. What is the probability that a family owns a motorcycle given that they do not have children?**

**Answer:**
P(Motorcycle | No Children)
Families without children = 80 + 50 + 30 = 160
Families with motorcycle AND no children = 50
P(Motorcycle | No Children) = 50/160 = **0.3125 or 31.25%**

---

## Question 21
**A factory manufactures light bulbs, and it is known that the probability of a light bulb being defective is 0.01. If the factory produces 1000 light bulbs, what is the probability that two randomly selected light bulbs from this production run are both defective, both non-defective, one defective and other non defective?**

**Answer:**

**Given:**
- Total bulbs = 1000
- P(Defective) = 0.01, so Expected defective bulbs = 1000 × 0.01 = 10
- P(Non-defective) = 0.99, so Expected non-defective bulbs = 990

**Sampling without replacement:**

**a) Both defective:**
P(Both Defective) = (10/1000) × (9/999)
= 0.01 × 0.009009
= **0.00009009 or 0.009%**

**b) Both non-defective:**
P(Both Non-defective) = (990/1000) × (989/999)
= 0.99 × 0.98999
= **0.98009 or 98.01%**

**c) One defective and one non-defective:**

This can happen in two ways:
- First defective, second non-defective: (10/1000) × (990/999)
- First non-defective, second defective: (990/1000) × (10/999)

P(One of each) = (10/1000) × (990/999) + (990/1000) × (10/999)
= 2 × (10/1000) × (990/999)
= 2 × 0.01 × 0.99099
= **0.01982 or 1.98%**

**Verification:** 0.00009 + 0.98009 + 0.01982 ≈ 1.0 ✓

---

## Question 22
**In a card game, the outcomes of drawing a card from a standard deck of 52 playing cards can be classified as winning and losing outcomes. If you draw a card, what is the probability that the card drawn is either a King or a Queen?**

**Answer:**

**Given:**
- Standard deck = 52 cards
- Number of Kings = 4
- Number of Queens = 4
- These are mutually exclusive events (a card cannot be both King and Queen)

**Using Addition Rule:**
P(King OR Queen) = P(King) + P(Queen)
= 4/52 + 4/52
= 8/52
= **2/13 ≈ 0.154 or 15.4%**

**Conclusion:**
The probability of drawing either a King or a Queen is **2/13 or approximately 15.4%**.

---

## Question 23
**In a school, students can enroll in multiple clubs. The probability that a student is a member of the Art Club is 0.4, and the probability that a student is a member of the Music Club is 0.5. If the probability that a student is a member of both clubs is 0.2, what is the probability that a randomly selected student is a member of at least one of the clubs?**

**Answer:**

**Given:**
- P(Art) = 0.4
- P(Music) = 0.5
- P(Art AND Music) = 0.2

**Using Addition Rule for Non-Mutually Exclusive Events:**
P(Art OR Music) = P(Art) + P(Music) - P(Art AND Music)
= 0.4 + 0.5 - 0.2
= **0.7 or 70%**

**Verification using Venn Diagram:**
- Only Art: 0.4 - 0.2 = 0.2
- Only Music: 0.5 - 0.2 = 0.3
- Both: 0.2
- Total: 0.2 + 0.3 + 0.2 = 0.7 ✓

**Conclusion:**
The probability that a randomly selected student is a member of at least one club (Art or Music or both) is **0.7 or 70%**.

---

**END OF ANSWER SHEET**
