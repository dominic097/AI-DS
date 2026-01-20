The **Normal Distribution** (also called **Gaussian Distribution** or **Bell Curve** is a continuous probability distribution that is symmetrical around its mean. It's the most important probability distribution in statistics because many natural phenomena follow this pattern.

**Key fact**: The normal distribution describes data where most values cluster around a central mean, with values tapering off symmetrically on both sides.

## **The Formula**

The probability density function of a normal distribution is:

```
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)²/(2σ²))
```

![[Pasted image 20251106233819.png]]


## Cumulative Distribution Function (CDF)

The cumulative distribution function gives the probability that a random variable X is less than or equal to x:

![[Pasted image 20251106234104.png]]

Where:

- **x** = the value of the variable
- **μ** (mu) = mean (center of distribution)
- **σ** (sigma) = standard deviation (spread of distribution)
- **π** ≈ 3.14159
- **e** ≈ 2.71828

**Note**: In practice, we rarely use this formula directly. Instead, we use Z-scores and standard normal tables!

---

## **Parameters**

### **μ (Mean)**

- Center of the distribution
- Shifts the curve left or right
- Can be any real number

### **σ (Standard Deviation)**

- Spread or width of the distribution
- Larger σ = wider, flatter curve
- Smaller σ = narrower, taller curve
- Must be positive (σ > 0)

**Notation**: X ~ N(μ, σ²) means "X follows a normal distribution with mean μ and variance σ²"

---

## **The Empirical Rule (68-95-99.7 Rule)**

This is the most important property of normal distribution:



```
68% of data falls within 1 standard deviation of the mean (μ ± 1σ)
95% of data falls within 2 standard deviations of the mean (μ ± 2σ)
99.7% of data falls within 3 standard deviations of the mean (μ ± 3σ)
```

**Visual representation**:



```
μ - 3σ    μ - 2σ    μ - 1σ     μ      μ + 1σ    μ + 2σ    μ + 3σ
   |         |         |        |         |         |         |
   |<--0.15%-->|<--2.35%-->|<--13.5%-->|<--34%-->|<--34%-->|<--13.5%-->|<--2.35%-->|<--0.15%-->|
   |           |<-----95%----->|         |         |
   |<-------------99.7%---------------->|
```

---

## **Standard Normal Distribution (Z-Distribution)**

A **special case** where:

- **Mean (μ) = 0**
- **Standard Deviation (σ) = 1**
- Notation: **Z ~ N(0, 1)**

### **Z-Score Formula**

To convert any normal distribution to standard normal:



```
Z = (X - μ) / σ
```

Where:

- **Z** = standard score (Z-score)
- **X** = raw score
- **μ** = mean
- **σ** = standard deviation

**Why Z-scores?** They allow us to:

1. Compare values from different distributions
2. Use standard normal tables to find probabilities
3. Determine how unusual a value is

---

## **Example 1: Student Test Scores**

**Scenario**: Test scores are normally distributed with a mean of 75 and standard deviation of 10.

**Given**:

- μ = 75
- σ = 10
- Distribution: X ~ N(75, 100)

---

### **(a) What percentage of students score between 65 and 85?**

**Solution**:

These values are exactly 1 standard deviation from the mean:

- Lower bound: 75 - 10 = 65
- Upper bound: 75 + 10 = 85

Using the **Empirical Rule**: 68% of data falls within μ ± 1σ

**Answer**: **68%** of students score between 65 and 85.

---

### **(b) What is the Z-score for a student who scored 90?**

**Solution**:



```
Z = (X - μ) / σ
Z = (90 - 75) / 10
Z = 15 / 10
Z = 1.5
```

**Answer**: The Z-score is **1.5**, meaning the score is 1.5 standard deviations above the mean.

---

### **(c) What percentage of students score below 55?**

**Solution**:

**Step 1**: Calculate Z-score



```
Z = (55 - 75) / 10
Z = -20 / 10
Z = -2.0
```

**Step 2**: Use standard normal table or empirical rule

- A Z-score of -2.0 means 2 standard deviations below the mean
- From empirical rule: 95% fall within μ ± 2σ
- Therefore, 5% fall outside this range
- Since it's symmetrical: 2.5% below and 2.5% above

**Answer**: **2.5%** of students score below 55.

---

### **(d) What score represents the 84th percentile?**

**Solution**:

**Step 1**: Understand the empirical rule

- 50% score below the mean (75)
- 34% score between μ and μ + 1σ
- Total below μ + 1σ = 50% + 34% = 84%

**Step 2**: Calculate the score



```
Score at 84th percentile = μ + 1σ
Score = 75 + 10
Score = 85
```

**Answer**: A score of **85** represents the 84th percentile.

---

## **Example 2: Heights of Adult Males**

**Scenario**: Heights of adult males are normally distributed with mean 70 inches and standard deviation 3 inches.

**Given**:

- μ = 70 inches
- σ = 3 inches
- Distribution: X ~ N(70, 9)

---

### **(a) What proportion of men are between 64 and 76 inches tall?**

**Solution**:

**Step 1**: Check standard deviations

- Lower: 70 - 6 = 64 → This is μ - 2σ
- Upper: 70 + 6 = 76 → This is μ + 2σ

**Step 2**: Apply empirical rule

- Within 2 standard deviations = 95%

**Answer**: **95%** of men are between 64 and 76 inches tall.

---

### **(b) A man is 67 inches tall. What is his Z-score?**

**Solution**:



```
Z = (X - μ) / σ
Z = (67 - 70) / 3
Z = -3 / 3
Z = -1.0
```

**Answer**: Z-score is **-1.0** (1 standard deviation below the mean).

---

### **(c) What percentage of men are taller than 73 inches?**

**Solution**:

**Step 1**: Calculate Z-score



```
Z = (73 - 70) / 3
Z = 3 / 3
Z = 1.0
```

**Step 2**: Use empirical rule

- 68% fall within μ ± 1σ
- This means 32% fall outside
- Since symmetrical: 16% below μ - 1σ and 16% above μ + 1σ

**Answer**: **16%** of men are taller than 73 inches.

---

### **(d) What height corresponds to a Z-score of -1.5?**

**Solution**:

Rearrange the Z-score formula:



```
Z = (X - μ) / σ
X = μ + Z × σ
X = 70 + (-1.5) × 3
X = 70 - 4.5
X = 65.5 inches
```

**Answer**: A height of **65.5 inches** corresponds to Z = -1.5.