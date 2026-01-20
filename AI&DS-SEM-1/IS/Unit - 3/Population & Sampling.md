### **Population**

- A **collection of ALL individuals or objects** of interest in a study
- Represents the **entire group** you want to draw conclusions about
- Denoted by **N** (population size)
- **Parameters** are used to describe populations (e.g., μ for mean, σ for standard deviation)

### **Sample**

- A **subset of the population** selected for study
- Should be **representative** of the population
- Denoted by **n** (sample size)
- **Statistics** are used to describe samples (e.g., x̄ for mean, s for standard deviation)

---

## 🎯 Key Differences

| Aspect       | Population            | Sample             |
| ------------ | --------------------- | ------------------ |
| **Size**     | Complete/entire group | Subset/portion     |
| **Symbol**   | N                     | n                  |
| **Mean**     | μ (mu)                | x̄ (x-bar)         |
| **Variance** | 𝜎2                   | 𝑠2                |
| **Std Dev**  | σ (sigma)             | s                  |
| **Purpose**  | Target of inference   | Used for inference |
| **Cost**     | Expensive/impractical | Cost-effective     |
| **Time**     | Time-consuming        | Faster             |

---
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)

# Simple Random Sampling (SRS)

**Simple Random Sampling (SRS)** is a sampling method where:

- Every member of the population has an **equal chance** of being selected
- Every possible sample of size _n_ has an **equal probability** of being chosen
- Selection is **independent** and **unbiased**

> **Think of it as**: Drawing names from a hat where everyone's name has equal opportunity to be picked!

---

### **Sample Mean**


![[Pasted image 20251107022636.png]]
### **Standard Error**


![[Pasted image 20251107022643.png]]

---
## 🎯 Key Characteristics

✅ **Random selection** - No systematic bias ✅ **Equal probability** - Each unit has same chance (probability = n/N) ✅ **Independence** - Selection of one doesn't affect others ✅ **Representative** - Likely to represent population well ✅ **Foundation** - Basis for statistical inference

---

## 🔢 Probability Formula

**Probability of selecting any individual:**

```
P = n / N
```


Where:

- **n** = sample size
- **N** = population size

**Example**: If N = 1000 students and n = 100 sample size P=1001000=0.10=10

```python
import random
import numpy as np

# Method 1: Using random.sample()
population = list(range(1, 101))  # Population: 1 to 100
sample_size = 10

simple_random_sample = random.sample(population, sample_size)
print(f"Simple Random Sample: {simple_random_sample}")

# Method 2: Using numpy
np_sample = np.random.choice(population, size=sample_size, replace=False)
print(f"NumPy Random Sample: {np_sample}")

# Method 3: Random sampling with seed (reproducible)
random.seed(42)
reproducible_sample = random.sample(population, sample_size)
print(f"Reproducible Sample: {reproducible_sample}")
```

There are two way in SRM 
- Without replacement - If selected unit is not returned to the population 
- With replacement - If selected unit is returned to the population


# Resampling Methods

**Resampling** is a statistical technique that involves:

- **Repeatedly drawing samples** from a dataset
- Using the **original data** to generate new samples
- **Estimating** properties of a population or validating models
- **Non-parametric** approach (doesn't assume specific distribution)

> **Think of it as**: Using your existing data to create many "new" datasets to understand variability and make inferences!

---

## 🎯 Why Resampling?

### **Traditional Statistics Limitations:**

- ❌ Requires assumptions (normality, etc.)
- ❌ Complex mathematical formulas
- ❌ Limited by small sample sizes
- ❌ Difficult for complex statistics

### **Resampling Advantages:**

- ✅ **Few assumptions** needed
- ✅ **Computationally intensive** but simple concept
- ✅ Works with **small samples**
- ✅ Applies to **any statistic**
- ✅ **Distribution-free** methods
- ✅ Provides **confidence intervals** and **significance tests**

---

## 🔄 Types of Resampling Methods

Code

```
RESAMPLING METHODS
│
├─ 1. BOOTSTRAP (Most Common)
│   ├─ Sampling WITH replacement
│   ├─ From original sample
│   └─ Estimate sampling distribution
│
├─ 2. JACKKNIFE
│   ├─ Leave-one-out method
│   ├─ Systematic resampling
│   └─ Bias and variance estimation
│
├─ 3. PERMUTATION TESTS
│   ├─ Rearrange existing data
│   ├─ Test hypotheses
│   └─ No assumptions about distribution
│
├─ 4. CROSS-VALIDATION
│   ├─ Model validation
│   ├─ Train-test splits
│   └─ K-fold validation
│
└─ 5. MONTE CARLO
    ├─ Random simulation
    ├─ Generate new data
    └─ Complex probability problems
```

---

## BOOTSTRAP METHOD 🥾

**Bootstrap** is a powerful resampling technique where:

- You **sample WITH replacement** from your original data
- Create many "bootstrap samples" (each same size as original)
- Calculate statistics for each bootstrap sample
- Use these to estimate **sampling distribution**, **confidence intervals**, and **standard errors**

> **Etymology**: "Pulling yourself up by your bootstraps" - using your own data to make inferences!

---

## 🎯 Key Concept

Code

```
┌─────────────────────────────────────────────────────┐
│  ORIGINAL SAMPLE (n=5)                              │
│  [10, 15, 20, 25, 30]                              │
└─────────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   Bootstrap 1     Bootstrap 2     Bootstrap 3
   [10,10,20,     [15,15,15,      [10,20,25,
    25,30]         20,30]          25,30]
    Mean=19        Mean=19         Mean=22
        │               │               │
        └───────────────┼───────────────┘
                        ▼
            Distribution of Means
            Standard Error
            Confidence Intervals
```

**Key Point**: Sample **WITH REPLACEMENT** (same element can appear multiple times)

---

## 🔑 Core Principles

### **1. Sampling WITH Replacement**

- Each element has equal chance of selection
- Can be selected multiple times
- Sample size = Original sample size

### **2. The Bootstrap Assumption**

> "The sample represents the population"

- Your original sample is treated as a "mini-population"
- Resampling mimics drawing new samples from the population

### **3. Large Number of Resamples**

- Typically: **1,000 to 10,000 bootstrap samples**
- More samples → More accurate estimates
- Computer does the heavy lifting!

---

## 📋 Step-by-Step Process

### **Step 1: Collect Original Sample**

Code

```
Original Sample: [12, 15, 18, 20, 22, 25, 28, 30]
n = 8
Original Mean = 21.25
Original Median = 21
```

### **Step 2: Draw Bootstrap Sample #1**

Code

```
Randomly select 8 values WITH replacement:
Bootstrap Sample 1: [12, 15, 18, 18, 22, 25, 28, 30]
                         ↑       ↑
                    (18 appears twice, 20 missing)
Mean₁ = 21.00
```

### **Step 3: Draw Bootstrap Sample #2**

Code

```
Bootstrap Sample 2: [12, 12, 15, 20, 22, 25, 28, 30]
                         ↑   ↑
                    (12 appears twice, 18 missing)
Mean₂ = 20.50
```

### **Step 4: Repeat Many Times (B times)**

Code

```
Bootstrap Sample 3: Mean₃ = 22.125
Bootstrap Sample 4: Mean₄ = 20.875
...
Bootstrap Sample 1000: Mean₁₀₀₀ = 21.50
```

### **Step 5: Analyze Bootstrap Distribution**

Code

```
Bootstrap Means: [21.00, 20.50, 22.125, 20.875, ..., 21.50]

Calculate:
- Standard Error (SE)
- Confidence Intervals
- Bias
- Distribution shape
```

jackknife

## JACKKNIFE METHOD 🥾

The jackknife works by systematically leaving out one observation at a time from your dataset, calculating your estimate on each reduced subsample, and then using those results to analyze variability and bias.

**How Jackknife Works:**

- Given a dataset of n observations, you create n new subsamples, each leaving out a different single observation.
- You then compute your statistic of interest (like the mean, variance, regression coefficient, etc.) for each subsample.
- These n estimates are called "jackknife replicates." By analyzing their distribution, you can estimate the bias and variance of your original statistic.

**Mathematical Formulation:**

1. Remove observation i from your dataset (for i = 1 to n).
2. Compute the statistic θ^(i) for the reduced dataset.
3. The jackknife estimate is the average of these, and bias/variance can be derived from the spread and differences of these values[[1]](https://www.geeksforgeeks.org/data-science/jackknife-resampling/)[[2]](https://www.statology.org/jackknife-resampling-explained-estimating-bias-and-variance/)[[3]](https://rajivgopinath.com/blogs/statistics-and-data-science-hub/jackknife-resampling-concept-steps-applications).

**Example:** For the mean, you'd leave out one value at a time, calculate the mean of the remaining values, and repeat until each value has been left out once. The average of those means gives the jackknife estimate, and the variability among them gives an estimate of the standard error.

**Applications:**

- Bias and variance estimation for statistics (especially when theoretical solutions are hard or unavailable).
- Used in cross-validation and model stability analysis.
- Suitable for small datasets or when data collection is expensive.

**Pros:**

- Simple and conceptually easy to implement.
- Provides reliable variance and bias estimates without complex calculations.
- Useful for complex or unknown distributions.

**Cons:**

- Not suitable for highly non-smooth statistics (e.g., medians in small samples).
- Can be computationally intensive for very large datasets, though less so than bootstrap methods.
- Assumes data points are independent and identically distributed (i.i.d), which may not always be the case[[4]](https://statisticseasily.com/glossario/what-is-jackknife-resampling/)[[5]](https://vyasenov.github.io/blog/jackknife-vs-bootstrap.html).

**Jackknife vs. Bootstrap:**

- Jackknife works by removing one observation at a time; bootstrap resamples with replacement to form new datasets.
- Bootstrap is more flexible (works for more types of statistics), but jackknife is simpler and often computationally cheaper for moderate sample sizes[[6]](https://www.wallstreetmojo.com/jackknife-resampling/)[[5]](https://vyasenov.github.io/blog/jackknife-vs-bootstrap.html).

Jackknife resampling is widely used in statistics, data science, ecology, machine learning, and finance to enhance the reliability of estimates, reduce bias, and calculate standard errors when traditional methods are not applicable[[3]](https://rajivgopinath.com/blogs/statistics-and-data-science-hub/jackknife-resampling-concept-steps-applications)[[7]](https://www.numberanalytics.com/blog/ultimate-jackknife-resampling-guide).


----


## **Sampling Variability**

**Sampling Variability** is a fundamental concept in statistics that refers to the natural variation that occurs in sample statistics (like the mean, median, or standard deviation) when different samples are drawn from the same population.

## Key Points:

**What It Demonstrates:**

- When you draw multiple random samples from a population, each sample will likely produce a slightly different sample mean
- In the example shown, the population mean is **15.125**
- Four different samples were drawn, producing sample means of: **15.20, 15.250, 15.150, and 15.225**
- These sample means are all close to the population mean but vary slightly from each other

## Why Sampling Variability Occurs:

1. **Random chance** - Different observations are selected in each sample
2. **Sample size** - Smaller samples tend to have more variability
3. **Population variability** - More variable populations lead to more variable samples

## Important Implications:

- **No sample is perfect** - Even with proper random sampling, your sample statistic will rarely equal the population parameter exactly
- **Predictable patterns** - While individual samples vary, the distribution of sample means follows predictable patterns (Central Limit Theorem)
- **Standard error** - We can measure and quantify sampling variability using the standard error

---


## **Sampling Error**

**Sampling Error** (often called **sampling error**, not "sample error") refers to the difference between a sample statistic (like the mean, proportion, or other measures computed from a sample) and the corresponding true population parameter. This error arises naturally because, rather than measuring every member of a population, researchers use a subset (sample) to make inferences about the whole. As a result, the sample may not perfectly reflect all the characteristics of the population, causing discrepancies between the sample results and the actual population values[[1]](https://statisticsbyjim.com/hypothesis-testing/sampling-error/)[[2]](https://www.geeksforgeeks.org/maths/sampling-error-definition-and-formula/)[[3]](https://en.wikipedia.org/wiki/Sampling_error)[[4]](https://www.britannica.com/science/sampling-error).


## Key Points about Sampling Error:

**Definition:**

- **Inevitability**: Sampling error is inherent whenever a sample is used, because samples are just approximations of the full population.
- **Formula**: Sampling Error = Sample Statistic - Population Parameter

**Connecting to Your Image:** Using your earlier example where the population mean is **15.125**:

- Sample 1 mean: 15.20 → Sampling error = 15.20 - 15.125 = **+0.075**
- Sample 2 mean: 15.250 → Sampling error = 15.250 - 15.125 = **+0.125**
- Sample 3 mean: 15.150 → Sampling error = 15.150 - 15.125 = **+0.025**
- Sample 4 mean: 15.225 → Sampling error = 15.225 - 15.125 = **+0.100**

## Important Characteristics:

**Magnitude**: The amount of sampling error depends on:

- **Sample size**: Larger samples → smaller error
- **Population variability**: More variable populations → larger error
- **Sampling method**: Random sampling tends to produce less systematic error

**Measurement**:

- **Standard error** measures the expected amount of sampling error
- **Confidence intervals** quantify the range where the true parameter likely lies[[3]](https://en.wikipedia.org/wiki/Sampling_error)

**Types**:

- **Random sampling error**: Arises from chance variation (unavoidable but predictable)
- **Systematic error (bias)**: Happens when the sampling process is flawed

## Reducing Sampling Error:

1. **Increase sample size** - Larger samples are more representative
2. **Use proper sampling methods** - Random or stratified sampling
3. **Minimize non-sampling errors** - Careful measurement and data collection

## Important Distinction:

**Sampling error ≠ Non-sampling error**

- **Sampling error**: Natural difference due to using a sample instead of the entire population
- **Non-sampling error**: Mistakes in data collection, measurement errors, survey biases, data entry errors[[4]](https://www.britannica.com/science/sampling-error)

## Relationship to Earlier Concepts:

- **Sampling variability** describes the phenomenon that samples vary
- **Sampling error** quantifies how far off a particular sample is from the truth


---


## **Sampling distribution**

**sampling distribution** in statistics is the probability distribution of a statistic (like the mean, median, proportion, or standard deviation) calculated from repeated random samples of a certain size drawn from the same population. Rather than focusing on just one sample, a sampling distribution lets us analyze what would happen if we took many random samples from a population and calculated the same statistic for each one.

## Simple Example:

Imagine wanting to know the average height of students in a school. Instead of measuring every student, you might randomly choose 30 students and calculate their mean height. If you did this repeatedly—each time with a different group of 30 students—you'd get slightly different means each time. **Plotting all these sample means would give you the sampling distribution of the mean.**