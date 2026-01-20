


[[Bayes' Theorem]]

Given a hypothesis _H_ and evidence _E_, Bayes' theorem states:

```
P(H | E) = [P(E | H) / P(E)] × P(H)
```

**In words**: The probability of the hypothesis after getting the evidence equals the probability of the evidence given the hypothesis, divided by the probability of the evidence, times the probability of the hypothesis before getting the evidence.

### Components:

- **P(H | E)** = **Posterior Probability** - The probability of the hypothesis H after observing evidence E
- **P(H)** = **Prior Probability** - The probability of hypothesis H before observing the evidence
- **P(E | H)** = **Likelihood** - The probability of observing evidence E given that hypothesis H is true
- **P(E)** = **Marginal Probability** - The total probability of observing evidence E (normalizing constant)

----


[[Binomial Distribution]]

The probability of getting exactly **x** successes in **n** trials is:


![[Pasted image 20251104113906.png]]


```
P(X = x) = C(n,x) × p^x × (1-p)^(n-x)
```

Or written with binomial coefficient notation:


```
P(X = x) = (n choose x) × p^x × q^(n-x)
```

Where:

- **n** = number of trials
- **x** = number of successes
- **p** = probability of success on a single trial
- **q** = probability of failure = 1 - p
- **C(n,x)** or **(n choose x)** 
	- = is the number of ways in which x success can take place  out of n trials 
	- = n! / [x!(n-x)!] 
	- = binomial coefficient **C(n,x)**

----

[[Poisson Distribution]]

The probability of observing exactly **x** events in a given interval is:

```
P(X = x) = (λ^x × e^(-λ)) / x!
```

Or written more clearly:

```
P(X = x) = (e^(-λ) × λ^x) / x!
```

Where:

- **x** = number of events (0, 1, 2, 3, ...)
- **λ** (lambda) = average number of events in the interval (mean rate)
- **e** = Euler's number ≈ 2.71828
- **x!** = factorial of x

---

**[[Normal Distribution]]**

The probability density function of a normal distribution is:

```
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)²/(2σ²))
```

![[Pasted image 20251106233903.png]]

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

### 1) **Z-Score Formula**

To convert any normal distribution to standard normal:

```
Z = (X - μ) / σ
```

Where:

- **Z** = standard score (Z-score)
- **X** = raw score
- **μ** = mean
- **σ** = standard deviation

## **2) Standard Normal Distribution**

When μ = 0 and σ = 1:

```
φ(z) = (1/√(2π)) × e^(-z²/2)
```

**Where**:

- **φ(z)** = standard normal probability density
- **z** = standard normal variable

---

## **4. Cumulative Distribution Function (CDF)**

The probability that X is less than or equal to x:

```
P(X ≤ x) = Φ((x - μ)/σ)
```

**Where**:

- **Φ** = standard normal cumulative distribution function
- Uses Z-score to find cumulative probability

**Standard Normal CDF**:

Code

```
Φ(z) = ∫[from -∞ to z] (1/√(2π)) e^(-t²/2) dt
```

---

## **5. Mean (Expected Value)**


```
μ = E(X)
```

For normal distribution, the mean is simply **μ**.

## **6. Variance**

```
σ² = Var(X) = E[(X - μ)²]
```

 
## **7. Standard Deviation**
 
```
σ = √(Variance)
```


## **8. Probability Between Two Values**

Probability that X falls between a and b:

```
P(a < X < b) = P(X < b) - P(X < a)
```

**Using Z-scores**:

```
P(a < X < b) = Φ((b-μ)/σ) - Φ((a-μ)/σ)
```

---

## **9. Percentile Formula**

To find the value x at the pth percentile:

```
x = μ + z_p × σ
```

**Where**:

- **z_p** = Z-score corresponding to the pth percentile
- Look up z_p in standard normal table

---

## **9. Empirical Rule Formulas**

**68% Rule** (within 1 standard deviation):

Code

```
P(μ - σ < X < μ + σ) ≈ 0.68
```

**95% Rule** (within 2 standard deviations):

Code

```
P(μ - 2σ < X < μ + 2σ) ≈ 0.95
```

**99.7% Rule** (within 3 standard deviations):

Code

```
P(μ - 3σ < X < μ + 3σ) ≈ 0.997
```

---

## **10. Standard Error (for Sample Mean)**

When dealing with sample means:

Code

```
SE = σ / √n
```

**Where**:

- **SE** = standard error
- **σ** = population standard deviation
- **n** = sample size

**Z-score for sample mean**:

Code

```
Z = (X̄ - μ) / (σ/√n)
```

---

## **11. Coefficient of Variation**

Measure of relative variability:

Code

```
CV = (σ / μ) × 100%
```

---


**[[Population & Sampling]]**


### **Sample Mean**


![[Pasted image 20251107022636.png]]
### **Standard Error**


![[Pasted image 20251107022643.png]]
