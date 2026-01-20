# 21CSC529T - Inferential Statistics - CYCLE TEST I
## Set-B - ANSWER SHEET

---

## Question 1

### Part a) Hospital Daily Admissions Comparison

**Given Data:**

|  | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
|---|---|---|---|---|---|
| **Emergency** | 25 | 30 | 22 | 28 | 24 |
| **General** | 20 | 15 | 18 | 22 | 25 |

---

#### i. Calculate measures of central tendency (6 marks)

### **EMERGENCY DEPARTMENT:**

**1. Mean (μ):**
**Formula:** μ = Σx / N

**Step-by-step:**
```
μ = (25 + 30 + 22 + 28 + 24) / 5
μ = 129 / 5
μ = 25.8
```
**Mean for Emergency = 25.8 admissions per day**

**2. Median:**
**Formula:** For odd n, Median = Middle value after arranging in order

**Step-by-step:**
1. Arrange in ascending order: 22, 24, 25, 28, 30
2. n = 5 (odd)
3. Median = 3rd value = 25

**Median for Emergency = 25 admissions**

**3. Mode:**
**Definition:** Most frequently occurring value

**Step-by-step:**
1. Check frequency of each value
2. All values appear only once: 22, 24, 25, 28, 30

**Mode for Emergency = No mode** (all values unique)

---

### **GENERAL DEPARTMENT:**

**1. Mean (μ):**
**Formula:** μ = Σx / N

**Step-by-step:**
```
μ = (20 + 15 + 18 + 22 + 25) / 5
μ = 100 / 5
μ = 20
```
**Mean for General = 20 admissions per day**

**2. Median:**
**Step-by-step:**
1. Arrange in ascending order: 15, 18, 20, 22, 25
2. n = 5 (odd)
3. Median = 3rd value = 20

**Median for General = 20 admissions**

**3. Mode:**
1. Check frequency of each value
2. All values appear only once: 15, 18, 20, 22, 25

**Mode for General = No mode** (all values unique)

---

**Summary Table - Central Tendency:**

| Measure | Emergency Department | General Department |
|---------|---------------------|-------------------|
| **Mean** | 25.8 admissions | 20.0 admissions |
| **Median** | 25 admissions | 20 admissions |
| **Mode** | No mode | No mode |

**Interpretation:**
- Emergency department has **higher average admissions** (25.8 vs 20.0)
- Emergency's mean is slightly higher than median, suggesting slight positive skew
- General's mean equals median, suggesting **symmetric distribution**
- Emergency handles approximately **29% more admissions** than General [(25.8-20)/20 × 100]

---

#### ii. Compute measures of dispersion (6 marks)

### **EMERGENCY DEPARTMENT:**

**1. Range:**
**Formula:** Range = Maximum - Minimum

**Step-by-step:**
```
Range = 30 - 22
Range = 8
```
**Range for Emergency = 8 admissions**

**2. Variance (σ²):**
**Formula (Population):** σ² = Σ(x - μ)² / N

**Step-by-step calculation:**

| Day | Admissions (x) | (x - μ) | (x - μ)² |
|-----|---------------|---------|----------|
| 1 | 25 | 25 - 25.8 = -0.8 | 0.64 |
| 2 | 30 | 30 - 25.8 = 4.2 | 17.64 |
| 3 | 22 | 22 - 25.8 = -3.8 | 14.44 |
| 4 | 28 | 28 - 25.8 = 2.2 | 4.84 |
| 5 | 24 | 24 - 25.8 = -1.8 | 3.24 |
| **Sum** | **129** | **0** | **40.80** |

```
σ² = 40.80 / 5
σ² = 8.16
```
**Variance for Emergency = 8.16** (squared admissions)

**3. Standard Deviation (σ):**
**Formula:** σ = √σ²

**Step-by-step:**
```
σ = √8.16
σ = 2.86
```
**Standard Deviation for Emergency = 2.86 admissions**

**4. Quartile Deviation (QD):**
**Formula:** QD = (Q3 - Q1) / 2

**Step-by-step:**
Data in order: 22, 24, 25, 28, 30

```
Q1 = 1st quartile position = (5+1) × 0.25 = 1.5th position
Q1 = 22 + 0.5(24-22) = 22 + 1 = 23

Q3 = 3rd quartile position = (5+1) × 0.75 = 4.5th position
Q3 = 28 + 0.5(30-28) = 28 + 1 = 29

QD = (29 - 23) / 2 = 6/2 = 3
```
**Quartile Deviation for Emergency = 3**

**5. Interquartile Range (IQR):**
**Formula:** IQR = Q3 - Q1

```
IQR = 29 - 23 = 6
```
**IQR for Emergency = 6 admissions**

---

### **GENERAL DEPARTMENT:**

**1. Range:**
```
Range = 25 - 15
Range = 10
```
**Range for General = 10 admissions**

**2. Variance (σ²):**

| Day | Admissions (x) | (x - μ) | (x - μ)² |
|-----|---------------|---------|----------|
| 1 | 20 | 20 - 20 = 0 | 0 |
| 2 | 15 | 15 - 20 = -5 | 25 |
| 3 | 18 | 18 - 20 = -2 | 4 |
| 4 | 22 | 22 - 20 = 2 | 4 |
| 5 | 25 | 25 - 20 = 5 | 25 |
| **Sum** | **100** | **0** | **58** |

```
σ² = 58 / 5
σ² = 11.6
```
**Variance for General = 11.6**

**3. Standard Deviation:**
```
σ = √11.6
σ = 3.41
```
**Standard Deviation for General = 3.41 admissions**

**4. Quartile Deviation:**
Data in order: 15, 18, 20, 22, 25

```
Q1 = 15 + 0.5(18-15) = 15 + 1.5 = 16.5
Q3 = 22 + 0.5(25-22) = 22 + 1.5 = 23.5

QD = (23.5 - 16.5) / 2 = 7/2 = 3.5
```
**Quartile Deviation for General = 3.5**

**5. Interquartile Range:**
```
IQR = 23.5 - 16.5 = 7
```
**IQR for General = 7 admissions**

---

**Summary Table - Dispersion Measures:**

| Measure | Emergency | General |
|---------|-----------|---------|
| **Range** | 8 | 10 |
| **Variance (σ²)** | 8.16 | 11.6 |
| **Standard Deviation (σ)** | 2.86 | 3.41 |
| **Quartile Deviation** | 3 | 3.5 |
| **IQR** | 6 | 7 |

**Interpretation:**
- **General department has higher dispersion** across all measures
- Emergency admissions are more **consistent and predictable** (lower SD: 2.86 vs 3.41)
- General department has wider spread in admissions (range of 10 vs 8)
- Emergency's lower variance (8.16 vs 11.6) indicates **more stable daily admissions**

---

#### iii. Calculate coefficient of variation (3 marks)

**Coefficient of Variation (CV)**
**Formula:** CV = (σ / μ) × 100%

This is a **relative measure of dispersion** that allows comparison between datasets with different means.

---

**EMERGENCY DEPARTMENT:**

**Step-by-step:**
```
Given:
σ = 2.86
μ = 25.8

CV = (2.86 / 25.8) × 100
CV = 0.1109 × 100
CV = 11.09%
```
**CV for Emergency = 11.09%**

---

**GENERAL DEPARTMENT:**

**Step-by-step:**
```
Given:
σ = 3.41
μ = 20.0

CV = (3.41 / 20.0) × 100
CV = 0.1705 × 100
CV = 17.05%
```
**CV for General = 17.05%**

---

**Comparison Table:**

| Department | Mean (μ) | SD (σ) | CV (%) |
|------------|----------|--------|--------|
| **Emergency** | 25.8 | 2.86 | **11.09%** |
| **General** | 20.0 | 3.41 | **17.05%** |

---

**Detailed Analysis:**

**1. Which department is more consistent?**
- **Emergency Department is more consistent** (CV = 11.09%)
- General Department is less consistent (CV = 17.05%)
- Difference: 17.05% - 11.09% = **5.96% higher variability** in General

**2. What does this mean?**
- Emergency has **35% less relative variability** than General [(17.05-11.09)/17.05 × 100]
- For every 100 admissions, Emergency varies by approximately 11, while General varies by 17
- Emergency department's **admissions are more predictable**

**3. Practical Implications:**

**For Emergency Department:**
- ✓ More **stable staffing requirements**
- ✓ Better **resource planning**
- ✓ More **predictable workload**
- ✓ Easier capacity management

**For General Department:**
- ✗ Higher variability requires **flexible staffing**
- ✗ More difficult to **predict resource needs**
- ✗ Greater fluctuation in daily workload
- ✗ Needs buffer capacity for peak days

**4. Statistical Significance:**
- CV difference of 5.96% is **substantial** in healthcare context
- Emergency's consistency (CV < 15%) is considered **good** for planning
- General's variability (CV > 15%) suggests need for investigation
- Possible factors: elective procedures, scheduled admissions, day-of-week effects

**Conclusion:**
The **Emergency Department demonstrates significantly better consistency** with a Coefficient of Variation of 11.09%, making its daily admissions approximately **35% more predictable** than the General Department's CV of 17.05%. This higher consistency facilitates better resource allocation, staffing decisions, and operational planning for the Emergency Department.

---

### Part b) Differences between Skewness and Kurtosis (5 marks)

**Answer:**

Both skewness and kurtosis are measures of the **shape of a distribution**, but they measure **different aspects** of that shape.

---

## **1. SKEWNESS**

### **Definition:**
Skewness measures the **asymmetry** or **lack of symmetry** in a probability distribution. It indicates whether data points are concentrated more on one side of the mean.

### **Formula:**

**Pearson's Coefficient of Skewness (Method 1):**
```
SK = 3(Mean - Median) / Standard Deviation
```

**Moment Coefficient of Skewness (Method 2):**
```
SK = [Σ(x - μ)³ / N] / σ³
```

### **Types of Skewness:**

**1. Positive Skewness (Right-skewed):**
- **Relationship:** Mean > Median > Mode
- **Tail:** Long tail extends to the right
- **SK value:** SK > 0
- **Shape:** Peak on left, tail on right

**Example:** Income distribution
- Data: $20K, $25K, $30K, $35K, $40K, $200K
- Mean = $58K (pulled up by $200K)
- Median = $32.5K
- Most people earn around $20-40K, few earn very high (billionaires)

**2. Negative Skewness (Left-skewed):**
- **Relationship:** Mode > Median > Mean
- **Tail:** Long tail extends to the left
- **SK value:** SK < 0
- **Shape:** Peak on right, tail on left

**Example:** Age at death in developed countries
- Most people die around 75-85 years
- Few die young (accidents, diseases)
- Creates left tail

**3. Zero Skewness (Symmetric):**
- **Relationship:** Mean = Median = Mode
- **Tail:** Balanced on both sides
- **SK value:** SK = 0
- **Shape:** Normal distribution (bell curve)

**Example:** Heights in a population, IQ scores

### **Interpretation Guidelines:**

| SK Value | Interpretation |
|----------|----------------|
| SK = 0 | Perfectly symmetric |
| -0.5 < SK < 0.5 | Approximately symmetric |
| 0.5 < SK < 1 | Moderately positively skewed |
| SK > 1 | Highly positively skewed |
| -1 < SK < -0.5 | Moderately negatively skewed |
| SK < -1 | Highly negatively skewed |

---

## **2. KURTOSIS**

### **Definition:**
Kurtosis measures the **"tailedness"** or **peakedness** of a distribution. It indicates how much of the variance is due to extreme deviations (outliers) versus more frequent modest deviations.

### **Formula:**

**Moment Coefficient of Kurtosis:**
```
Kurt = [Σ(x - μ)⁴ / N] / σ⁴
```

**Excess Kurtosis:**
```
Excess Kurtosis = Kurt - 3
```
(Normal distribution has kurtosis = 3, so excess = 0)

### **Types of Kurtosis:**

**1. Leptokurtic (High Kurtosis):**
- **Kurt value:** > 3 (Excess > 0)
- **Shape:** Sharp peak, heavy tails
- **Characteristics:**
  - More outliers than normal
  - Data concentrated around mean
  - Higher probability of extreme values

**Example:** Stock returns during volatile periods
- Most days have small changes (sharp peak)
- Occasional crash days with huge losses (fat tails)

**2. Mesokurtic (Normal Kurtosis):**
- **Kurt value:** = 3 (Excess = 0)
- **Shape:** Normal bell curve
- **Characteristics:**
  - Standard normal distribution
  - Moderate peak and tails

**Example:** Heights, test scores under normal conditions

**3. Platykurtic (Low Kurtosis):**
- **Kurt value:** < 3 (Excess < 0)
- **Shape:** Flat peak, thin tails
- **Characteristics:**
  - Fewer outliers
  - Data more evenly distributed
  - Lower probability of extremes

**Example:** Uniform distribution (rolling a fair die)
- All outcomes equally likely (1,2,3,4,5,6)
- No peak, flat distribution

### **Interpretation Guidelines:**

| Kurt Value | Excess Kurt | Interpretation |
|------------|-------------|----------------|
| Kurt = 3 | 0 | Mesokurtic (normal) |
| Kurt > 3 | > 0 | Leptokurtic (heavy tails, more outliers) |
| Kurt < 3 | < 0 | Platykurtic (light tails, fewer outliers) |

---

## **3. KEY DIFFERENCES BETWEEN SKEWNESS AND KURTOSIS**

| Aspect | Skewness | Kurtosis |
|--------|----------|----------|
| **Measures** | Asymmetry (direction) | Tailedness/Peakedness |
| **What it shows** | Where data is concentrated | How extreme the outliers are |
| **Direction** | Left or right | Peak height and tail weight |
| **Formula order** | 3rd moment | 4th moment |
| **Zero means** | Symmetric distribution | Normal distribution (mesokurtic) |
| **Positive value** | Right tail longer | More peaked, heavier tails |
| **Negative value** | Left tail longer | Flatter, lighter tails |
| **Affects** | Mean vs Median relationship | Risk of extreme values |

---

## **4. SIGNIFICANCE AND IMPORTANCE**

### **Significance of Skewness:**

**1. Choice of Central Tendency Measure:**
- Positively skewed: Use **median** (mean inflated by outliers)
- Symmetric: Use **mean** (most efficient)
- Negatively skewed: Use **median** (mean deflated)

**2. Statistical Testing:**
- Many statistical tests assume **normality** (SK ≈ 0)
- High skewness violates normality assumption
- May need data **transformation** (log, square root)

**3. Business Applications:**
- **Income data:** Always positively skewed, affects policy decisions
- **Product lifespan:** Helps in warranty planning
- **Customer spending:** Identifies spending patterns

**4. Interpretation of Results:**
- Helps understand whether **exceptional cases** exist
- Guides whether to use **parametric or non-parametric tests**

---

### **Significance of Kurtosis:**

**1. Risk Assessment:**
- **High kurtosis (leptokurtic):** Higher risk of extreme events
- Important in **finance** (stock market crashes)
- Critical for **insurance** (catastrophic claims)

**2. Quality Control:**
- Leptokurtic: Process has occasional **extreme defects**
- Platykurtic: Process output is **very uniform**
- Helps identify **process stability**

**3. Outlier Detection:**
- High kurtosis signals presence of **significant outliers**
- Guides whether outliers are **natural or errors**
- Affects **data cleaning** decisions

**4. Model Selection:**
- Normal distribution assumption (Kurt = 3)
- High kurtosis: Consider **heavy-tailed distributions** (t-distribution)
- Affects **prediction intervals** and confidence levels

---

## **5. COMPREHENSIVE EXAMPLE**

**Dataset: Exam Scores**

**Data A:** 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95
**Data B:** 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75
**Data C:** 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120

**Analysis:**

| Dataset | Mean | Median | Skewness | Kurtosis | Interpretation |
|---------|------|--------|----------|----------|----------------|
| **A** | 70 | 70 | ~0 | ~-1.2 | Symmetric, uniform (platykurtic) |
| **B** | 70 | 70 | ~0 | ~-1.0 | Symmetric, tightly clustered |
| **C** | 70 | 70 | ~0 | ~-1.2 | Symmetric, very spread out |

**Insights:**
- All three have **same mean and median** (70)
- All are **symmetric** (SK ≈ 0)
- But **different kurtosis** tells us about spread and outliers
- Cannot be distinguished by mean/median alone!

---

## **6. PRACTICAL APPLICATIONS**

### **Finance:**
- **Skewness:** Identifies asymmetric return distributions
  - Positive skew: Occasional large gains
  - Negative skew: Occasional large losses (market crashes)
- **Kurtosis:** Measures tail risk (black swan events)
  - High kurtosis: Higher probability of extreme losses

### **Healthcare:**
- **Skewness:** Hospital stay duration (usually right-skewed)
  - Most patients: short stays
  - Few patients: very long stays
- **Kurtosis:** Disease outbreak patterns
  - High kurtosis: Occasional severe outbreaks

### **Manufacturing:**
- **Skewness:** Product defect rates
  - Helps identify systematic bias in production
- **Kurtosis:** Measurement precision
  - High kurtosis: Some measurements very far from specification

### **Education:**
- **Skewness:** Test difficulty assessment
  - Left-skewed: Test too easy (ceiling effect)
  - Right-skewed: Test too hard (floor effect)
- **Kurtosis:** Item discrimination
  - High kurtosis: Questions separate students well

---

## **7. HOW THEY WORK TOGETHER**

Both measures provide **complementary information**:

**Example: Income Distribution**
- **Skewness = +2.5** (highly right-skewed)
  - Tells us: Few very wealthy people, most earn less
- **Kurtosis = 8** (leptokurtic)
  - Tells us: Not only is it skewed, but there are extreme billionaires (fat right tail)

**Without both:**
- Skewness alone: Know it's asymmetric, but not about extremes
- Kurtosis alone: Know about extremes, but not about direction

---

## **CONCLUSION**

| Measure | Primary Question | Practical Impact |
|---------|-----------------|------------------|
| **Skewness** | "Is my data balanced?" | Choose appropriate statistics (mean vs median) |
| **Kurtosis** | "How extreme are my outliers?" | Assess risk of rare events |

**Key Takeaway:**
- **Skewness** tells you **where** the bulk of your data lies (left, center, or right)
- **Kurtosis** tells you **how much** you should worry about extreme values (outliers)

Both are essential for:
- **Understanding data distribution**
- **Choosing appropriate statistical methods**
- **Making informed decisions**
- **Risk assessment and management**

In practice, always examine **both measures together** with visual tools (histograms, box plots) for complete understanding of your data's shape and behavior.

---

## Question 2

### Part a) Music Festival Probability (5 marks)

**Given Data:**

|  | Rock | Pop | Jazz | Total |
|---|---|---|---|---|
| **Adult** | 70 | 50 | 30 | 150 |
| **Teen** | 60 | 80 | 40 | 180 |
| **Child** | 50 | 30 | 60 | 140 |
| **Total** | **180** | **160** | **130** | **470** |

---

#### i. Probability that a randomly chosen attendee is enrolled in Pop

**Formula:** P(Pop) = Number in Pop / Total attendees

**Step-by-step:**
```
Total attendees = 70 + 50 + 30 + 60 + 80 + 40 + 50 + 30 + 60
Total = 470

Pop attendees = 50 + 80 + 30 = 160

P(Pop) = 160 / 470
P(Pop) = 16/47
P(Pop) = 0.340
```

**Answer: P(Pop) = 0.340 or 34.0% or 16/47**

---

#### ii. Probability that a randomly chosen attendee is a Teen

**Formula:** P(Teen) = Number of teens / Total attendees

**Step-by-step:**
```
Teens = 60 + 80 + 40 = 180

P(Teen) = 180 / 470
P(Teen) = 18/47
P(Teen) = 0.383
```

**Answer: P(Teen) = 0.383 or 38.3% or 18/47**

---

#### iii. Probability that an attendee is an Adult who prefers Rock

**Formula:** P(Adult AND Rock) = Number of adults preferring rock / Total

**Step-by-step:**
```
Adults preferring Rock = 70

P(Adult AND Rock) = 70 / 470
P(Adult AND Rock) = 7/47
P(Adult AND Rock) = 0.149
```

**Answer: P(Adult AND Rock) = 0.149 or 14.9% or 7/47**

---

#### iv. Probability that an attendee is a Child who enjoys Jazz

**Formula:** P(Child AND Jazz) = Number of children enjoying jazz / Total

**Step-by-step:**
```
Children enjoying Jazz = 60

P(Child AND Jazz) = 60 / 470
P(Child AND Jazz) = 6/47
P(Child AND Jazz) = 0.128
```

**Answer: P(Child AND Jazz) = 0.128 or 12.8% or 6/47**

---

#### v. Probability that an attendee is an Adult given they prefer Rock

**Formula:** P(Adult | Rock) = P(Adult AND Rock) / P(Rock)

This is **CONDITIONAL PROBABILITY**

**Step-by-step:**
```
Adults preferring Rock = 70
Total Rock attendees = 180

P(Adult | Rock) = 70 / 180
P(Adult | Rock) = 7/18
P(Adult | Rock) = 0.389
```

**Answer: P(Adult | Rock) = 0.389 or 38.9% or 7/18**

---

**Summary Table:**

| Question | Formula | Calculation | Probability | Percentage |
|----------|---------|-------------|-------------|------------|
| i. P(Pop) | 160/470 | 16/47 | 0.340 | 34.0% |
| ii. P(Teen) | 180/470 | 18/47 | 0.383 | 38.3% |
| iii. P(Adult ∩ Rock) | 70/470 | 7/47 | 0.149 | 14.9% |
| iv. P(Child ∩ Jazz) | 60/470 | 6/47 | 0.128 | 12.8% |
| v. P(Adult \| Rock) | 70/180 | 7/18 | 0.389 | 38.9% |

---

### Part b) Clothing Manufacturer Defective Items (10 marks)

**Given Information:**

**Defect Rates (Prior Probabilities):**
- P(Defective | Shirt) = 0.02
- P(Defective | Pants) = 0.03
- P(Defective | Jacket) = 0.04

**Posterior Probabilities (Given directly):**
- P(Shirt | Defective) = 0.5
- P(Pants | Defective) = 0.3
- P(Jacket | Defective) = 0.2

**Question:** What is the most likely type of defective garment?

---

#### **METHOD 1: Direct Answer from Given Posterior Probabilities**

**Step-by-step:**

The question provides **posterior probabilities** (probabilities AFTER observing a defective item):

```
P(Shirt | Defective) = 0.5 = 50%
P(Pants | Defective) = 0.3 = 30%
P(Jacket | Defective) = 0.2 = 20%
```

**Comparison:**
```
Shirt: 50% (highest)
Pants: 30%
Jacket: 20% (lowest)
```

**Answer: SHIRT is the most likely type of defective garment (50% probability)**

---

#### **METHOD 2: Understanding Through Bayes' Theorem**

Let's understand **why** this result makes sense using **Bayes' Theorem**.

**Bayes' Theorem Formula:**
```
P(Item | Defective) = [P(Defective | Item) × P(Item)] / P(Defective)
```

---

**Step 1: Work backwards to find production proportions**

Let P(Shirt) = pS, P(Pants) = pP, P(Jacket) = pJ

**From Bayes' theorem:**
```
P(Shirt | Defective) = [P(Def | Shirt) × P(Shirt)] / P(Defective)
0.5 = (0.02 × pS) / P(Defective)

P(Pants | Defective) = [P(Def | Pants) × P(Pants)] / P(Defective)
0.3 = (0.03 × pP) / P(Defective)

P(Jacket | Defective) = [P(Def | Jacket) × P(Jacket)] / P(Defective)
0.2 = (0.04 × pJ) / P(Defective)
```

---

**Step 2: Find relative production proportions**

**Divide first equation by second:**
```
0.5/0.3 = (0.02 × pS)/(0.03 × pP)
1.667 = 0.02pS / 0.03pP
1.667 × 0.03pP = 0.02pS
0.05pP = 0.02pS
pS = 2.5pP
```

**Shirts are produced at 2.5 times the rate of Pants**

**Divide first equation by third:**
```
0.5/0.2 = (0.02 × pS)/(0.04 × pJ)
2.5 = 0.02pS / 0.04pJ
2.5 × 0.04pJ = 0.02pS
0.1pJ = 0.02pS
pS = 5pJ
```

**Shirts are produced at 5 times the rate of Jackets**

---

**Step 3: Calculate actual production proportions**

**Let's set:** pJ = 1 unit (base)

Then:
- pS = 5pJ = 5 units
- pS = 2.5pP → 5 = 2.5pP → pP = 2 units

**Production proportions:**
```
Shirts: 5 units
Pants: 2 units
Jackets: 1 unit
Total: 8 units
```

**Normalized probabilities:**
```
P(Shirt) = 5/8 = 0.625 = 62.5%
P(Pants) = 2/8 = 0.250 = 25.0%
P(Jacket) = 1/8 = 0.125 = 12.5%
```

---

**Step 4: Calculate overall defect rate**

**Formula:** P(Defective) = Σ [P(Def | Item) × P(Item)]

**Step-by-step:**
```
P(Defective) = P(Def|Shirt)×P(Shirt) + P(Def|Pants)×P(Pants) + P(Def|Jacket)×P(Jacket)

P(Defective) = (0.02 × 0.625) + (0.03 × 0.25) + (0.04 × 0.125)
P(Defective) = 0.0125 + 0.0075 + 0.005
P(Defective) = 0.025 or 2.5%
```

**Overall defect rate = 2.5%**

---

**Step 5: Verify using Bayes' Theorem**

**For Shirts:**
```
P(Shirt | Defective) = (0.02 × 0.625) / 0.025
P(Shirt | Defective) = 0.0125 / 0.025
P(Shirt | Defective) = 0.5 ✓
```

**For Pants:**
```
P(Pants | Defective) = (0.03 × 0.25) / 0.025
P(Pants | Defective) = 0.0075 / 0.025
P(Pants | Defective) = 0.3 ✓
```

**For Jackets:**
```
P(Jacket | Defective) = (0.04 × 0.125) / 0.025
P(Jacket | Defective) = 0.005 / 0.025
P(Jacket | Defective) = 0.2 ✓
```

**All posterior probabilities verified!**

---

#### **Detailed Analysis and Interpretation**

**1. Production Volume Analysis:**

| Garment | Defect Rate | Production Volume | Contribution to Defects |
|---------|-------------|-------------------|-------------------------|
| Shirt | 2% (lowest) | 62.5% (highest) | 0.02 × 0.625 = 0.0125 |
| Pants | 3% (medium) | 25.0% (medium) | 0.03 × 0.25 = 0.0075 |
| Jacket | 4% (highest) | 12.5% (lowest) | 0.04 × 0.125 = 0.005 |

**Key Insight:** Even though shirts have the **lowest defect rate** (2%), they account for **50% of all defective items** because they are produced in **much larger quantities** (62.5% of production).

---

**2. Why is this counterintuitive?**

**Intuitive (wrong) thinking:**
"Jackets have 4% defect rate, highest among all, so most defects should be jackets"

**Reality:**
- Jackets: 4% defect rate × 12.5% production = 0.5% of total production is defective jackets
- Shirts: 2% defect rate × 62.5% production = 1.25% of total production is defective shirts

**Shirts contribute MORE defective items** despite lower defect rate!

---

**3. Practical Business Implications:**

**For Quality Control Manager:**

**Priority 1: Shirts (50% of defects)**
- Highest absolute number of defects
- Even small improvement has big impact
- Focus here yields maximum defect reduction

**Priority 2: Pants (30% of defects)**
- Moderate defect contribution
- Medium defect rate and volume
- Secondary focus area

**Priority 3: Jackets (20% of defects)**
- Highest defect rate BUT lowest volume
- Smallest absolute defect contribution
- Consider: Is 4% acceptable for premium item?

---

**4. Quality Improvement Strategies:**

**Scenario A: Reduce Shirt defects from 2% to 1%**
```
New defect contribution = 0.01 × 0.625 = 0.00625
Reduction = 0.0125 - 0.00625 = 0.00625
Overall defect rate: 2.5% → 2.0% (20% improvement!)
```

**Scenario B: Reduce Jacket defects from 4% to 2%**
```
New defect contribution = 0.02 × 0.125 = 0.0025
Reduction = 0.005 - 0.0025 = 0.0025
Overall defect rate: 2.5% → 2.4% (4% improvement)
```

**Conclusion:** Improving shirt quality has **5 times more impact** than improving jacket quality!

---

**5. Bayesian Reasoning Lesson:**

This problem demonstrates a key principle:
**"The most common source of defects is not necessarily the item with highest defect rate"**

**Factors that matter:**
1. **Defect rate** (quality)
2. **Production volume** (quantity)
3. **Combined effect** determines actual impact

---

#### **Final Answer:**

**SHIRT is the most likely type of defective garment.**

**Complete Summary:**

When a defective item is selected from the production line:
- **50% probability it's a Shirt**
- **30% probability it's Pants**
- **20% probability it's a Jacket**

**Explanation:**
Despite shirts having the **lowest defect rate** (2%), they account for **half of all defective items** because they represent **62.5% of total production**. The combination of moderate quality issues with very high volume makes shirts the dominant source of defects.

**Quality Control Recommendation:**
Focus quality improvement efforts on **shirts first**, as even small improvements in shirt defect rates will have the largest impact on overall defect reduction. A 1% reduction in shirt defects has the same impact as a 2% reduction in jacket defects, due to the volume difference.

---

### Part c) Non-Probabilistic Sampling Techniques (5 marks)

**Answer:**

#### **NON-PROBABILISTIC (NON-RANDOM) SAMPLING TECHNIQUES**

Non-probabilistic sampling is a sampling method where **not all members of the population have a known or equal chance of being selected**. Selection is based on **researcher judgment, convenience, or specific criteria** rather than random selection.

**Key Characteristic:** Cannot make statistical inferences or generalizations to the population with known confidence levels.

---

### **1. CONVENIENCE SAMPLING (ACCIDENTAL SAMPLING)**

**Definition:**
Selecting participants who are **easily accessible** and available to the researcher. The sample is chosen based on convenience rather than any specific criteria.

**Method:**
- Researcher selects individuals who are easy to reach
- No randomization or systematic approach
- "First come, first served" basis

**Example 1: Mall Survey**
A market researcher stands at a shopping mall entrance and surveys the first 100 people who walk by between 2-4 PM on a Tuesday afternoon.

**Why it's convenient:**
- Easy to collect data quickly
- Low cost
- Minimal effort required

**Example 2: University Research**
A psychology professor surveys students in their own class for a study on stress levels.

**Example 3: Online Poll**
A website asks visitors to participate in a survey - only those who happen to visit and choose to respond are included.

**Advantages:**
- Very quick and cheap
- Easy to administer
- Requires minimal planning
- Good for pilot studies

**Disadvantages:**
- High selection bias
- Not representative of population
- Cannot generalize findings
- May miss important subgroups
- Depends on researcher location/timing

**When to use:**
- Pilot studies or preliminary research
- Exploratory research
- Very limited budget/time
- When generalization is not important

---

### **2. PURPOSIVE SAMPLING (JUDGMENTAL SAMPLING)**

**Definition:**
Researcher uses their **judgment and expertise** to deliberately select participants who they believe will provide the most valuable information for the study.

**Method:**
- Researcher sets specific criteria
- Handpicks participants based on characteristics
- Targets individuals with specific knowledge or experience

**Example 1: Expert Opinions**
A researcher studying AI ethics interviews **20 leading AI researchers** from top universities, selecting them based on their publications and expertise.

**Selection criteria:**
- At least 10 publications in AI ethics
- PhD in Computer Science or Philosophy
- Working at top-tier institution

**Example 2: Medical Study**
A clinical trial on a new diabetes drug specifically recruits patients who:
- Have Type 2 diabetes for 5+ years
- Are on current medication but poorly controlled
- Age 40-65
- No other major health conditions

**Example 3: Market Research**
A company developing luxury watches interviews **high-income professionals** (income >$200K) who already own luxury brands, as they are the target market.

**Advantages:**
- Targets most relevant participants
- Expert knowledge ensures quality sample
- Efficient for specialized topics
- Logical and practical
- Lower costs than random sampling

**Disadvantages:**
- Researcher bias in selection
- Not representative
- Difficult to defend selection decisions
- Cannot calculate sampling error
- Findings may not generalize

**When to use:**
- Studying rare or specific populations
- Expert opinions needed
- Limited resources
- Exploratory or qualitative research
- Case studies

---

### **3. QUOTA SAMPLING**

**Definition:**
Population is divided into **mutually exclusive subgroups** (quotas), and the researcher non-randomly selects a **predetermined number** from each subgroup to match population proportions.

**Method:**
1. Identify important characteristics (age, gender, income)
2. Determine population proportions
3. Set quotas for each subgroup
4. Non-randomly fill each quota until complete

**Example 1: Political Poll**
A city has 60% Female, 40% Male population. Poll 500 people:
- **Quota:** 300 females, 200 males
- **Method:** Survey people at train station until quotas filled
- Keep surveying women until reach 300, men until reach 200
- Stop once both quotas met

**Example 2: Market Research - Age Groups**
Survey 400 consumers matching city demographics:

| Age Group | Population % | Quota | How to Fill |
|-----------|--------------|-------|-------------|
| 18-30 | 30% | 120 | Survey at university campuses |
| 31-50 | 40% | 160 | Survey at business districts |
| 51-70 | 25% | 100 | Survey at community centers |
| 70+ | 5% | 20 | Survey at senior centers |

**Example 3: Product Testing**
Testing a new smartphone - need diverse users:

| User Type | Quota | Selection Method |
|-----------|-------|------------------|
| Tech enthusiasts | 40 | Contact tech bloggers |
| Average users | 60 | Survey at phone stores |
| Senior citizens | 20 | Community centers |
| Students | 30 | University campus |

**Advantages:**
- Ensures representation of subgroups
- More representative than convenience sampling
- No sampling frame needed
- Cheaper than stratified random sampling
- Quick to administer
- Easy to understand and implement

**Disadvantages:**
- Not random within quotas (selection bias)
- Cannot calculate sampling error
- Researcher may fill quotas conveniently
- Not statistically valid
- Difficult to verify independence

**When to use:**
- Market research and opinion polls
- When stratified random sampling too expensive
- Need quick, reasonably representative sample
- Population characteristics well known

**Difference from Stratified Sampling:**
- **Stratified:** Random selection within each stratum (probabilistic)
- **Quota:** Non-random selection within each quota (non-probabilistic)

---

### **4. SNOWBALL SAMPLING (CHAIN REFERRAL SAMPLING)**

**Definition:**
Existing participants **recruit future participants** from their acquaintances. Sample "snowballs" or grows through referrals.

**Method:**
1. Identify a few initial participants (seeds)
2. Ask them to refer others who meet criteria
3. Contact referred individuals
4. Ask new participants to refer more
5. Continue until desired sample size reached

**Example 1: Hidden Populations**
Studying **illegal drug users**:
- Find 3 initial participants through rehabilitation center
- Ask each to refer 2-3 friends who also use drugs
- Contact referred individuals, ensure confidentiality
- Ask them to refer others
- Build network of 50-100 participants

**Why snowball?** Drug users are hidden, no sampling frame exists, they trust referrals from friends.

**Example 2: Rare Diseases**
Research on patients with **rare genetic disorder** (affects 1 in 100,000):
- Contact patient support group, find 5 patients
- Ask them if they know other patients
- Patients refer others from online communities
- Build sample of 30 patients globally

**Example 3: Social Network Study**
Studying **startup founders' networks**:
- Interview 2 successful startup founders
- Ask: "Who are 3 other founders you respect and learn from?"
- Interview referred founders
- Map the network of entrepreneurial connections

**Example 4: Homeless Population**
Surveying **homeless individuals** in a city:
- Contact social workers, meet 10 homeless people
- Build trust, ask them to introduce researcher to others
- Use referrals to access hard-to-reach individuals
- Many homeless people know others in similar situations

**Advantages:**
- **Only practical method** for hidden populations
- Lower cost than trying to find rare individuals randomly
- Builds trust through referrals
- Can access hard-to-reach groups
- Utilizes social networks effectively

**Disadvantages:**
- **Severe selection bias** (samples from same network)
- Not representative of all subgroups
- May miss isolated individuals
- Cannot calculate sampling error
- Difficult to determine when to stop
- May lack diversity (everyone knows each other)

**When to use:**
- Hidden or hard-to-reach populations (drug users, sex workers)
- Rare diseases or conditions
- Marginalized communities (illegal immigrants)
- Sensitive topics requiring trust
- No sampling frame available
- Social network research

---

### **5. VOLUNTEER SAMPLING (SELF-SELECTION SAMPLING)**

**Definition:**
Participants **volunteer themselves** to be part of the study, usually in response to an advertisement or invitation.

**Method:**
- Post advertisement or invitation
- Participants decide whether to join
- No selection by researcher
- Open to anyone who responds

**Example 1: Online Survey**
University posts on social media:
- "Take our 10-minute survey on social media usage!"
- "Win $50 Amazon gift card (prize draw)"
- 2,000 people voluntarily complete survey
- Sample = those who saw ad AND chose to respond

**Example 2: Clinical Trial**
Hospital advertises:
- "Volunteers needed for diabetes medication trial"
- "Compensation: $500, Free health monitoring"
- Diabetic patients call in to volunteer
- 100 participants self-select into trial

**Example 3: Psychology Experiment**
Professor posts on university bulletin board:
- "Participate in memory research study"
- "Earn course credit"
- Students voluntarily sign up
- 50 students self-select

**Example 4: Product Beta Testing**
Tech company announces:
- "Join beta test for our new app!"
- Enthusiastic users volunteer
- Sample = tech-savvy early adopters (not average users)

**Advantages:**
- Easy to recruit participants
- Motivated participants (less dropout)
- Low cost
- Quick to organize
- Ethical (fully voluntary)

**Disadvantages:**
- **Extreme self-selection bias**
- Volunteers differ systematically from non-volunteers
- Not representative
- May attract specific personality types (more extroverted, more interested)
- Cannot generalize findings

**Self-selection bias example:**
Survey on "satisfaction with healthcare":
- Happy patients more likely to respond
- Angry patients may be too busy or not motivated
- Result: Overestimates satisfaction

**When to use:**
- Need motivated participants
- Ethical concerns require full consent
- Testing products with early adopters
- Limited recruitment resources
- Exploratory studies

---

## **COMPARISON TABLE**

| Method | Basis of Selection | Cost | Bias Level | Best For |
|--------|-------------------|------|------------|----------|
| **Convenience** | Availability/accessibility | Very Low | Very High | Pilot studies, quick feedback |
| **Purposive** | Researcher judgment | Low | High | Expert opinions, specific criteria |
| **Quota** | Fill predetermined quotas | Medium | Medium-High | Market research, demographics |
| **Snowball** | Referrals from participants | Low | High | Hidden/rare populations |
| **Volunteer** | Self-selection | Very Low | Very High | Motivated participants needed |

---

## **ADVANTAGES AND DISADVANTAGES SUMMARY**

### **General Advantages of Non-Probabilistic Sampling:**
1. ✓ **Cost-effective** - cheaper than random sampling
2. ✓ **Fast** - quicker to organize and complete
3. ✓ **Practical** - feasible when random sampling impossible
4. ✓ **Flexible** - can adapt during data collection
5. ✓ **Access** - reaches hidden or rare populations

### **General Disadvantages:**
1. ✗ **Selection bias** - systematic exclusion of certain groups
2. ✗ **Not representative** - cannot generalize to population
3. ✗ **No statistical validity** - cannot calculate confidence intervals
4. ✗ **Cannot estimate sampling error**
5. ✗ **Researcher influence** - subjective selection decisions

---

## **WHEN TO USE NON-PROBABILISTIC SAMPLING**

**Appropriate situations:**
1. **Exploratory research** - generating hypotheses
2. **Qualitative studies** - in-depth understanding
3. **Pilot studies** - testing questionnaires
4. **Hidden populations** - no sampling frame
5. **Very limited budget** - cannot afford random sampling
6. **Time constraints** - need quick results
7. **Theoretical sampling** - testing specific theories

**Inappropriate situations:**
1. Generalizing to entire population
2. Estimating population parameters with precision
3. Hypothesis testing requiring statistical inference
4. Policy decisions affecting large groups
5. Situations requiring unbiased estimates

---

## **CONCLUSION**

Non-probabilistic sampling methods are **practical tools** when randomization is impossible or unnecessary. While they **sacrifice statistical rigor and representativeness**, they offer **speed, cost-effectiveness, and access to hard-to-reach populations**.

**Key principle:** Choose the sampling method based on:
- Research objectives
- Available resources
- Population characteristics
- Required precision
- Generalizability needs

For **exploratory, qualitative, or practical constraints**, non-probabilistic methods are appropriate and valuable. For **confirmatory research requiring generalization**, probabilistic methods are essential.

---

## Question 3

### Part a) Fitness Research - Diet Quality vs Exercise Frequency (10 marks)

**Given Data:**

| S.No | Diet Quality (1-10) | Exercise Frequency (days/week) | Fitness Level Score (0-100) |
|------|---------------------|-------------------------------|----------------------------|
| 1 | 8 | 4 | 85 |
| 2 | 5 | 2 | 60 |
| 3 | 9 | 5 | 90 |
| 4 | 6 | 3 | 70 |
| 5 | 4 | 1 | 50 |

**Question:** Determine which independent variable (Diet Quality or Exercise Frequency) has a stronger relationship with Fitness Level.

---

#### **METHOD: Pearson Correlation Coefficient**

**Formula:** r = Σ[(x - x̄)(y - ȳ)] / √[Σ(x - x̄)² × Σ(y - ȳ)²]

---

### **CORRELATION 1: Diet Quality vs Fitness Level**

**Step 1: Calculate means**
```
Mean Diet Quality (x̄) = (8 + 5 + 9 + 6 + 4) / 5 = 32/5 = 6.4
Mean Fitness Level (ȳ) = (85 + 60 + 90 + 70 + 50) / 5 = 355/5 = 71
```

**Step 2: Create calculation table**

| Diet (x) | Fitness (y) | (x - x̄) | (y - ȳ) | (x - x̄)(y - ȳ) | (x - x̄)² | (y - ȳ)² |
|----------|-------------|----------|----------|------------------|-----------|-----------|
| 8 | 85 | 1.6 | 14 | 22.4 | 2.56 | 196 |
| 5 | 60 | -1.4 | -11 | 15.4 | 1.96 | 121 |
| 9 | 90 | 2.6 | 19 | 49.4 | 6.76 | 361 |
| 6 | 70 | -0.4 | -1 | 0.4 | 0.16 | 1 |
| 4 | 50 | -2.4 | -21 | 50.4 | 5.76 | 441 |
| **Sum** | | **0** | **0** | **137.6** | **17.2** | **1120** |

**Step 3: Calculate correlation**
```
r = Σ[(x - x̄)(y - ȳ)] / √[Σ(x - x̄)² × Σ(y - ȳ)²]
r = 137.6 / √(17.2 × 1120)
r = 137.6 / √19264
r = 137.6 / 138.79
r = 0.991
```

**Correlation (Diet Quality vs Fitness Level) = +0.991**

**Interpretation:** **Near-perfect positive correlation** - as diet quality increases, fitness level increases almost proportionally.

---

### **CORRELATION 2: Exercise Frequency vs Fitness Level**

**Step 1: Calculate means**
```
Mean Exercise Frequency (x̄) = (4 + 2 + 5 + 3 + 1) / 5 = 15/5 = 3
Mean Fitness Level (ȳ) = 71 (same as before)
```

**Step 2: Create calculation table**

| Exercise (x) | Fitness (y) | (x - x̄) | (y - ȳ) | (x - x̄)(y - ȳ) | (x - x̄)² | (y - ȳ)² |
|--------------|-------------|----------|----------|------------------|-----------|-----------|
| 4 | 85 | 1 | 14 | 14 | 1 | 196 |
| 2 | 60 | -1 | -11 | 11 | 1 | 121 |
| 5 | 90 | 2 | 19 | 38 | 4 | 361 |
| 3 | 70 | 0 | -1 | 0 | 0 | 1 |
| 1 | 50 | -2 | -21 | 42 | 4 | 441 |
| **Sum** | | **0** | **0** | **105** | **10** | **1120** |

**Step 3: Calculate correlation**
```
r = 105 / √(10 × 1120)
r = 105 / √11200
r = 105 / 105.83
r = 0.992
```

**Correlation (Exercise Frequency vs Fitness Level) = +0.992**

**Interpretation:** **Near-perfect positive correlation** - as exercise frequency increases, fitness level increases almost proportionally.

---

### **COEFFICIENT OF DETERMINATION**

**For Diet Quality:**
```
r² = (0.991)²
r² = 0.982
r² = 98.2%
```
**Interpretation:** 98.2% of variation in Fitness Level explained by Diet Quality.

**For Exercise Frequency:**
```
r² = (0.992)²
r² = 0.984
r² = 98.4%
```
**Interpretation:** 98.4% of variation in Fitness Level explained by Exercise Frequency.

---

### **COMPARISON AND FINAL ANSWER**

**Summary Table:**

| Independent Variable | Correlation (r) | |r| | r² | Relationship |
|---------------------|-----------------|------|-----|--------------|
| Diet Quality | +0.991 | 0.991 | 98.2% | Near-perfect Positive |
| **Exercise Frequency** | **+0.992** | **0.992** | **98.4%** | **Near-perfect Positive** |

---

### **CONCLUSION**

**EXERCISE FREQUENCY has a (slightly) stronger relationship with Fitness Level.**

**Statistical Justification:**

**1. Correlation Magnitude:**
- |r_exercise| = 0.992 > |r_diet| = 0.991
- Exercise Frequency has marginally stronger linear relationship

**2. Coefficient of Determination:**
- r²_exercise = 98.4% > r²_diet = 98.2%
- Exercise Frequency explains **0.2% more variation** in Fitness Level

**3. Practical Interpretation:**
- **Both variables are extremely strong predictors** (r > 0.99)
- The difference is **negligible** (0.001 difference in correlation)
- In practical terms, **both are equally important**

**4. Unexplained Variation:**
- Exercise model: 1.6% unexplained
- Diet model: 1.8% unexplained
- Difference: Only 0.2% (minimal)

**5. Statistical vs Practical Significance:**
- **Statistically:** Exercise Frequency is slightly stronger
- **Practically:** The difference is **not meaningful**
- **Both factors are critical** for fitness

---

### **DETAILED ANALYSIS**

**Pattern Observation:**
Looking at the data:
```
Individual 1: Diet=8, Exercise=4, Fitness=85
Individual 2: Diet=5, Exercise=2, Fitness=60
Individual 3: Diet=9, Exercise=5, Fitness=90
Individual 4: Diet=6, Exercise=3, Fitness=70
Individual 5: Diet=4, Exercise=1, Fitness=50
```

**Key Insights:**
1. **Perfect ranking:** Both Diet and Exercise rank individuals identically
2. **Coordinated behavior:** People with better diets also exercise more
3. **Linear relationship:** Each point increase in Diet/Exercise corresponds to predictable Fitness increase

**Approximate relationships:**
- Diet Quality: Each 1-point increase ≈ 8-point Fitness increase
- Exercise Frequency: Each 1-day increase ≈ 10-point Fitness increase

---

### **RECOMMENDATIONS**

**For Fitness Programs:**

**1. Both factors are critical:**
- Cannot prioritize one over the other
- Near-perfect correlations for both

**2. Integrated approach needed:**
- Diet and Exercise work together
- High correlation between Diet and Exercise (r ≈ 0.99)
- They are **not independent** in this data

**3. Practical interventions:**
- Improve Diet Quality: Target 7-9 on 10-point scale
- Exercise Frequency: Aim for 4-5 days per week
- Combined effect likely greater than individual effects

**4. Consider multivariate analysis:**
- Since both are so highly correlated, may have **multicollinearity**
- Consider **multiple regression** to see independent effects:
  - Fitness = β₀ + β₁(Diet) + β₂(Exercise) + ε

**5. Sample size consideration:**
- Only 5 individuals - very small sample
- Correlations may be inflated
- Need larger study to confirm findings

---

### **FINAL ANSWER:**

**Exercise Frequency has a marginally stronger relationship with Fitness Level (r = 0.992) compared to Diet Quality (r = 0.991).**

However, the difference is **practically negligible** (only 0.001). Both variables demonstrate **near-perfect positive correlations**, explaining over 98% of the variation in Fitness Level.

**Conclusion:** In practical terms, **both Diet Quality and Exercise Frequency are equally important** predictors of Fitness Level. A comprehensive fitness program should address **both factors simultaneously** rather than prioritizing one over the other. The extremely high correlations (r > 0.99) suggest that individuals who maintain good diet quality also tend to exercise regularly, indicating these behaviors are **strongly linked and mutually reinforcing**.

**Recommendation:** Future research should use larger samples and multivariate techniques to understand the independent and interactive effects of these variables on fitness outcomes.

---

### Part b) Calculate Quartiles and IQR (5 marks)

**Given Dataset:** [12, 15, 22, 25, 29, 34, 38]

---

#### **Step 1: Verify data is sorted**

Data: 12, 15, 22, 25, 29, 34, 38 ✓ (already in ascending order)

n = 7 (odd number of values)

---

#### **Step 2: Calculate Q1 (First Quartile)**

**Formula:** Q1 = Value at position (n+1) × 0.25

**Step-by-step:**
```
Position of Q1 = (7+1) × 0.25
Position = 8 × 0.25
Position = 2

Q1 = 2nd value = 15
```

**Q1 = 15**

---

#### **Step 3: Calculate Q2 (Second Quartile / Median)**

**Formula:** Q2 = Value at position (n+1) × 0.5

For odd n, median is the middle value.

**Step-by-step:**
```
Position of Q2 = (7+1) × 0.5
Position = 8 × 0.5
Position = 4

Q2 = 4th value = 25
```

**Q2 = 25**

---

#### **Step 4: Calculate Q3 (Third Quartile)**

**Formula:** Q3 = Value at position (n+1) × 0.75

**Step-by-step:**
```
Position of Q3 = (7+1) × 0.75
Position = 8 × 0.75
Position = 6

Q3 = 6th value = 34
```

**Q3 = 34**

---

#### **Step 5: Calculate IQR (Interquartile Range)**

**Formula:** IQR = Q3 - Q1

**Step-by-step:**
```
IQR = 34 - 15
IQR = 19
```

**IQR = 19**

---

#### **SUMMARY OF RESULTS**

**5-Number Summary:**

| Statistic | Value | Position | Interpretation |
|-----------|-------|----------|----------------|
| **Minimum** | 12 | 1st value | Lowest value in dataset |
| **Q1** | 15 | 2nd value | 25% of data ≤ 15 |
| **Q2 (Median)** | 25 | 4th value (middle) | 50% of data ≤ 25 |
| **Q3** | 34 | 6th value | 75% of data ≤ 34 |
| **Maximum** | 38 | 7th value | Highest value in dataset |
| **IQR** | 19 | Q3 - Q1 | Middle 50% spread |

---

#### **VISUAL REPRESENTATION**

**Box Plot Structure:**
```
    12          15        25        34          38
    |-----------|---------|---------|-----------|
  Min          Q1       Q2(Med)    Q3         Max
                 |<------ IQR ----->|
                        = 19
```

---

#### **INTERPRETATION**

**1. Q1 = 15:**
- 25% of values are ≤ 15
- These are: 12, 15
- Represents the **lower quarter** of the data

**2. Q2 = 25:**
- 50% of values are ≤ 25
- This is the **median** (middle value)
- Divides data into two equal halves

**3. Q3 = 34:**
- 75% of values are ≤ 34
- These are: 12, 15, 22, 25, 29, 34
- Represents the **upper three-quarters** of the data

**4. IQR = 19:**
- The **middle 50%** of data spans 19 units
- Range from Q1 (15) to Q3 (34)
- Measures spread of central data
- **Not affected by extreme values** (outliers)

---

#### **OUTLIER DETECTION**

**Formula for outliers:**
- **Lower fence:** Q1 - 1.5 × IQR
- **Upper fence:** Q3 + 1.5 × IQR

**Calculate:**
```
Lower fence = 15 - 1.5 × 19
Lower fence = 15 - 28.5
Lower fence = -13.5

Upper fence = 34 + 1.5 × 19
Upper fence = 34 + 28.5
Upper fence = 62.5
```

**Check for outliers:**
- All values: 12, 15, 22, 25, 29, 34, 38
- All fall within [-13.5, 62.5]
- **No outliers detected** ✓

---

#### **ADDITIONAL ANALYSIS**

**1. Symmetry:**
- Q2 - Q1 = 25 - 15 = **10** (lower half spread)
- Q3 - Q2 = 34 - 25 = **9** (upper half spread)
- Difference: 10 vs 9 (very close)
- **Distribution is approximately symmetric**

**2. Spread:**
- **Range** = Max - Min = 38 - 12 = **26**
- **IQR** = 19
- IQR captures 73% of range (19/26)
- Data is **fairly concentrated** around median

**3. Quartile Distances:**
- Distance from Min to Q1 = 15 - 12 = **3**
- Distance from Q1 to Q2 = 25 - 15 = **10**
- Distance from Q2 to Q3 = 34 - 25 = **9**
- Distance from Q3 to Max = 38 - 34 = **4**

**Pattern:** Middle two quartiles (Q1-Q2, Q2-Q3) have most spread (10 and 9), while outer quartiles (Min-Q1, Q3-Max) are more compressed (3 and 4).

---

#### **PRACTICAL APPLICATIONS**

**1. Robust Measure:**
- IQR is **resistant to outliers**
- Better than range for skewed data
- Used in box plots for visualization

**2. Quality Control:**
- Control limits often set at Q1 - 1.5×IQR and Q3 + 1.5×IQR
- Values outside are flagged for investigation

**3. Comparison:**
- IQR allows comparison between datasets with different scales
- Relative measure of dispersion

**4. Data Cleaning:**
- Outlier detection using 1.5×IQR rule (Tukey's method)
- Helps identify data entry errors

---

#### **FINAL ANSWER**

**Quartiles:**
- **Q1 = 15**
- **Q2 = 25**
- **Q3 = 34**

**Interquartile Range:**
- **IQR = 19**

**Interpretation:** The middle 50% of the data values range from 15 to 34, spanning 19 units. The distribution is approximately symmetric with no outliers detected. The IQR of 19 indicates moderate spread in the central portion of the dataset.

---

### Part c) Choir Committee Combination (5 marks)

**Question:** A local choir has 12 members, and they want to form a committee of 5 members to organize an upcoming concert. How many different ways can the choir members form this committee?

**Answer:**

This is a **COMBINATION** problem because:
1. **Order does NOT matter** (committee members are equal)
2. We are **selecting** 5 members from 12
3. No repetition (each member selected once)
4. {Member A, B, C, D, E} is the **same committee** as {Member E, D, C, B, A}

---

#### **Formula: Combination**

**General Formula:**
```
C(n, r) = n! / [r! × (n - r)!]
```

**Alternative notation:**
```
ⁿCᵣ or (n choose r) or "n choose r"
```

Where:
- n = total number of items = 12 members
- r = number of items to select = 5 members
- ! = factorial

---

#### **Step-by-step Solution:**

**Step 1: Identify the values**
```
n = 12 choir members
r = 5 committee members
```

**Step 2: Apply the combination formula**
```
C(12, 5) = 12! / [5! × (12 - 5)!]
C(12, 5) = 12! / [5! × 7!]
```

**Step 3: Simplify factorials**

Instead of calculating full factorials, we can simplify:
```
C(12, 5) = (12 × 11 × 10 × 9 × 8 × 7!) / (5! × 7!)
```

The 7! cancels out:
```
C(12, 5) = (12 × 11 × 10 × 9 × 8) / 5!
C(12, 5) = (12 × 11 × 10 × 9 × 8) / (5 × 4 × 3 × 2 × 1)
```

**Step 4: Calculate numerator**
```
12 × 11 = 132
132 × 10 = 1,320
1,320 × 9 = 11,880
11,880 × 8 = 95,040
```

**Numerator = 95,040**

**Step 5: Calculate denominator**
```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

**Denominator = 120**

**Step 6: Final division**
```
C(12, 5) = 95,040 / 120
C(12, 5) = 792
```

---

#### **ANSWER: 792 different ways**

The choir can form the committee in **792 different ways**.

---

#### **VERIFICATION**

Let's verify using the symmetry property: C(n, r) = C(n, n-r)

```
C(12, 5) = C(12, 7)

C(12, 7) = 12! / (7! × 5!)
C(12, 7) = 95,040 / 120
C(12, 7) = 792 ✓
```

**Verification successful!**

---

#### **WHY COMBINATION (not Permutation)?**

**Key Question:** Does the **order of selection** matter?

**In this problem:**
- Committee with {Alice, Bob, Carol, David, Eve} is the **same** as {Eve, David, Carol, Bob, Alice}
- All members have **equal roles** in committee
- No hierarchy or ordering
- We're just forming a **group**

**If it were Permutation (order matters):**
```
P(12, 5) = 12! / (12-5)!
P(12, 5) = 12! / 7!
P(12, 5) = 12 × 11 × 10 × 9 × 8
P(12, 5) = 95,040
```

This would be if positions like President, Vice President, Secretary, Treasurer, Member were assigned (ordered).

**Relationship:**
```
P(n, r) = r! × C(n, r)
95,040 = 120 × 792 ✓
```

Each combination can be arranged in 5! = 120 ways, so permutations = 120 × combinations.

---

#### **PRACTICAL UNDERSTANDING**

**Example with small numbers:**
If we had 4 members {A, B, C, D} and wanted to select 2:

**All possible combinations:**
1. {A, B}
2. {A, C}
3. {A, D}
4. {B, C}
5. {B, D}
6. {C, D}

**Count = 6**

**Verify:** C(4, 2) = 4!/(2!×2!) = 24/(2×2) = 24/4 = 6 ✓

---

#### **ALTERNATIVE CALCULATION METHOD**

**Pascal's Triangle approach:**
```
C(12, 5) = C(11, 4) + C(11, 5)
```

But direct calculation is more practical for this problem.

---

#### **APPLICATIONS**

**1. Real-world scenarios:**
- Forming teams from employees
- Selecting jury members from a pool
- Choosing lottery numbers
- Creating product combinations
- Selecting pizza toppings

**2. Related problems:**
- If committee needs a chairperson: 792 × 5 = 3,960 ways (select committee, then choose chair)
- If 2 members must be included: C(10, 3) = 120 ways (select 3 from remaining 10)
- If certain members cannot serve together: More complex (inclusion-exclusion principle)

---

#### **MATHEMATICAL PROPERTIES**

**1. Symmetry:**
```
C(12, 5) = C(12, 7) = 792
```
Selecting 5 members = Selecting 7 members to exclude

**2. Sum property:**
```
C(12, 0) + C(12, 1) + ... + C(12, 12) = 2^12 = 4,096
```
Total number of all possible committees (any size)

**3. Pascal's identity:**
```
C(12, 5) = C(11, 4) + C(11, 5)
792 = 330 + 462
792 = 792 ✓
```

---

#### **SUMMARY**

**Problem Type:** Combination (order doesn't matter)

**Formula used:** C(n, r) = n! / [r! × (n-r)!]

**Calculation:** C(12, 5) = 95,040 / 120 = **792**

**Answer:** The choir members can form the committee in **792 different ways**.

**Interpretation:** Out of 12 members, there are exactly 792 unique groups of 5 members that can be selected. Each group is considered different based only on its membership, not on the order in which members are selected or listed.

---

**END OF ANSWER SHEET - SET B**

---
