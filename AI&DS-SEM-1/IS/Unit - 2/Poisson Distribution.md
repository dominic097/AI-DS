The **Poisson Distribution** is a discrete probability distribution that describes the probability of a given number of events occurring in a fixed interval of time or space, when these events occur with a known constant mean rate and independently of the time since the last event.

It's named after French mathematician Siméon Denis Poisson and is used to model **rare events** that occur randomly over time or space.

---

## **Key Characteristics**

A Poisson process must satisfy these conditions:

1. **Events occur independently** - One event doesn't affect another
2. **Events occur at a constant average rate (λ)** - The mean rate is constant over time
3. **Two events cannot occur at exactly the same instant** - Events are discrete
4. **The probability of an event is proportional to the length of the interval** - Longer intervals = more likely events

---

## **The Formula**

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

## **Understanding Each Component**

### **λ (Lambda) - Average Rate**

- The expected number of events in the interval
- Must be positive (λ > 0)
- Example: Average of 3 customers per hour means λ = 3

### **e^(-λ)**

- Exponential decay factor based on the mean
- Makes probabilities sum to 1
- Always positive and less than 1

### **λ^x**

- Represents the effect of the mean raised to the number of events
- Higher λ means higher probability of more events

### **x!**

- Factorial of the number of events
- Normalizes the probability

---

## **Mean and Variance**

For a Poisson distribution:

- **Mean (Expected Value)**: μ = λ
- **Variance**: σ² = λ
- **Standard Deviation**: σ = √λ

**Important**: In Poisson distribution, **mean = variance** (this is a unique property!)

---

## **Example 1: Customer Arrivals**

**Problem**: A store receives an average of 4 customers per hour. What's the probability that exactly 6 customers arrive in the next hour?

**Given**:

- λ = 4 (average customers per hour)
- x = 6 (number we want to find)
- e ≈ 2.71828

**Solution**:



```
P(X = 6) = (e^(-4) × 4^6) / 6!

Step 1: Calculate e^(-4)
e^(-4) = 1 / e^4 = 1 / 54.598 ≈ 0.0183

Step 2: Calculate 4^6
4^6 = 4,096

Step 3: Calculate 6!
6! = 6 × 5 × 4 × 3 × 2 × 1 = 720

Step 4: Put it together
P(X = 6) = (0.0183 × 4,096) / 720
P(X = 6) = 74.957 / 720
P(X = 6) = 0.1042 or 10.42%
```

**Answer**: There's a **10.42%** chance of exactly 6 customers arriving.

---

## **Example 2: Email Arrivals**

**Problem**: You receive an average of 2 emails per day.

**(a) What's the probability you receive exactly 0 emails today?**

**Given**:

- λ = 2
- x = 0

**Solution**:



```
P(X = 0) = (e^(-2) × 2^0) / 0!

Step 1: e^(-2) ≈ 0.1353
Step 2: 2^0 = 1
Step 3: 0! = 1

P(X = 0) = (0.1353 × 1) / 1
P(X = 0) = 0.1353 or 13.53%
```

**Answer**: **13.53%** chance of receiving no emails.

---

**(b) What's the probability you receive at least 3 emails?**

**Solution**:

It's easier to use the complement:

```
P(X ≥ 3) = 1 - P(X < 3)
P(X ≥ 3) = 1 - [P(X=0) + P(X=1) + P(X=2)]
```

**Calculate P(X = 1)**:

```
P(X = 1) = (e^(-2) × 2^1) / 1!
P(X = 1) = (0.1353 × 2) / 1
P(X = 1) = 0.2707
```

**Calculate P(X = 2)**:

```
P(X = 2) = (e^(-2) × 2^2) / 2!
P(X = 2) = (0.1353 × 4) / 2
P(X = 2) = 0.2707
```

**Total**:

```
P(X ≥ 3) = 1 - (0.1353 + 0.2707 + 0.2707)
P(X ≥ 3) = 1 - 0.6767
P(X ≥ 3) = 0.3233 or 32.33%
```

**Answer**: **32.33%** chance of receiving at least 3 emails.

---

## **Example 3: Call Center**

**Problem**: A call center receives an average of 5 calls per 10 minutes.

**(a) What's the probability of exactly 3 calls in the next 10 minutes?**

**Given**:

- λ = 5
- x = 3

**Solution**:


```
P(X = 3) = (e^(-5) × 5^3) / 3!

e^(-5) ≈ 0.0067
5^3 = 125
3! = 6

P(X = 3) = (0.0067 × 125) / 6
P(X = 3) = 0.8375 / 6
P(X = 3) = 0.1396 or 13.96%
```

---

**(b) What's the expected number of calls in 30 minutes?**

**Solution**:

If λ = 5 calls per 10 minutes, then in 30 minutes:


```
λ₃₀ = 5 × 3 = 15 calls
```

**Important**: When changing the time interval, scale λ proportionally!

---

**(c) What's the probability of exactly 12 calls in 30 minutes?**

**Given**:

- λ = 15 (for 30 minutes)
- x = 12

**Solution**:


```
P(X = 12) = (e^(-15) × 15^12) / 12!

e^(-15) ≈ 3.059 × 10^(-7)
15^12 = 1.29746 × 10^14
12! = 479,001,600

P(X = 12) = (3.059 × 10^(-7) × 1.29746 × 10^14) / 479,001,600
P(X = 12) ≈ 0.0829 or 8.29%
```

---

## **Example 4: Manufacturing Defects**

**Problem**: A textile factory produces fabric with an average of 0.5 defects per square meter.

**(a) What's the probability of finding exactly 1 defect in 2 square meters?**

**Given**:

- λ = 0.5 per square meter
- For 2 square meters: λ = 0.5 × 2 = 1
- x = 1

**Solution**:


```
P(X = 1) = (e^(-1) × 1^1) / 1!

e^(-1) ≈ 0.3679
1^1 = 1
1! = 1

P(X = 1) = 0.3679 or 36.79%
```

---

**(b) What's the probability of no defects in 1 square meter?**

**Given**:

- λ = 0.5
- x = 0

**Solution**:


```
P(X = 0) = (e^(-0.5) × 0.5^0) / 0!

e^(-0.5) ≈ 0.6065
0.5^0 = 1
0! = 1

P(X = 0) = 0.6065 or 60.65%
```

---

## **Probability Distribution Table**

For λ = 3, here's the probability distribution:

|x (Events)|P(X = x)|Percentage|
|---|---|---|
|0|0.0498|4.98%|
|1|0.1494|14.94%|
|2|0.2240|22.40%|
|3|0.2240|22.40%|
|4|0.1680|16.80%|
|5|0.1008|10.08%|
|6|0.0504|5.04%|
|7|0.0216|2.16%|
|8+|0.0120|1.20%|

---

## **Real-World Applications**

1. **Call Centers** - Number of calls per hour
2. **Website Traffic** - Visitors per minute
3. **Manufacturing** - Defects per unit
4. **Healthcare** - Patient arrivals at emergency room
5. **Insurance** - Number of claims per month
6. **Traffic** - Accidents per day on a highway
7. **Biology** - Mutations per DNA sequence
8. **Natural Disasters** - Earthquakes per year
9. **Customer Service** - Complaints per day
10. **Banking** - ATM transactions per hour

---

## **When to Use Poisson Distribution**

✅ **Use Poisson when**:

- Events occur independently
- Events occur at a constant average rate
- You're counting occurrences in an interval
- Dealing with rare events

❌ **Don't use Poisson when**:

- Events are not independent
- Rate changes over time
- Events occur in clusters
- Probability of event is not small

---

## **Poisson vs Binomial Distribution**

|Feature|Binomial|Poisson|
|---|---|---|
|**Number of trials**|Fixed (n)|Unlimited|
|**Probability per trial**|Constant (p)|Very small|
|**Parameters**|n and p|λ only|
|**Use when**|Fixed attempts|Rare events over time/space|

**Poisson approximation to Binomial**: When n is large and p is small (np < 10), use Poisson with λ = np

---

## **Quick Reference: Common Poisson Calculations**

**Exactly x events**:

```
P(X = x) = (e^(-λ) × λ^x) / x!
```

**At most x events**:


```
P(X ≤ x) = P(X=0) + P(X=1) + ... + P(X=x)
```

**At least x events**:

```
P(X ≥ x) = 1 - P(X < x) = 1 - P(X ≤ x-1)
```

**More than x events**:

```
P(X > x) = 1 - P(X ≤ x)
```

**Expected value and variance**:

```
Mean = Variance = λ
Standard Deviation = √λ
```

---

**At Most Event**

**Scenario**: A coffee shop receives an average of 3 customers per hour during the afternoon.

**Question**: What is the probability that **at most 2 customers** arrive in the next hour?

---

### **Solution:**

**Given**:

- λ = 3 (average customers per hour)
- We need P(X ≤ 2)

**Formula**:

Code

```
P(X ≤ 2) = P(X = 0) + P(X = 1) + P(X = 2)
```

---

**Step 1: Calculate P(X = 0)**

Code

```
P(X = 0) = (e^(-3) × 3^0) / 0!

e^(-3) ≈ 0.0498
3^0 = 1
0! = 1

P(X = 0) = (0.0498 × 1) / 1
P(X = 0) = 0.0498
```

---

**Step 2: Calculate P(X = 1)**

Code

```
P(X = 1) = (e^(-3) × 3^1) / 1!

e^(-3) ≈ 0.0498
3^1 = 3
1! = 1

P(X = 1) = (0.0498 × 3) / 1
P(X = 1) = 0.1494
```

---

**Step 3: Calculate P(X = 2)**

Code

```
P(X = 2) = (e^(-3) × 3^2) / 2!

e^(-3) ≈ 0.0498
3^2 = 9
2! = 2

P(X = 2) = (0.0498 × 9) / 2
P(X = 2) = 0.4482 / 2
P(X = 2) = 0.2241
```

---

**Step 4: Add them up**

Code

```
P(X ≤ 2) = P(X = 0) + P(X = 1) + P(X = 2)
P(X ≤ 2) = 0.0498 + 0.1494 + 0.2241
P(X ≤ 2) = 0.4233 or 42.33%
```

---

### **Answer**:

There is a **42.33%** probability that at most 2 customers will arrive in the next hour.

---

## **Problem 2: Hospital Emergency Room**

**Scenario**: A hospital emergency room receives an average of 4 patients per hour during night shifts.

**Question**: What is the probability that **at most 3 patients** arrive in the next hour?

---

### **Solution:**

**Given**:

- λ = 4
- We need P(X ≤ 3)

**Formula**:

Code

```
P(X ≤ 3) = P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3)
```

---

**Step 1: Calculate P(X = 0)**

Code

```
P(X = 0) = (e^(-4) × 4^0) / 0!
P(X = 0) = 0.0183 × 1 / 1
P(X = 0) = 0.0183
```

---

**Step 2: Calculate P(X = 1)**

Code

```
P(X = 1) = (e^(-4) × 4^1) / 1!
P(X = 1) = 0.0183 × 4 / 1
P(X = 1) = 0.0733
```

---

**Step 3: Calculate P(X = 2)**

Code

```
P(X = 2) = (e^(-4) × 4^2) / 2!
P(X = 2) = 0.0183 × 16 / 2
P(X = 2) = 0.2928 / 2
P(X = 2) = 0.1465
```

---

**Step 4: Calculate P(X = 3)**

Code

```
P(X = 3) = (e^(-4) × 4^3) / 3!
P(X = 3) = 0.0183 × 64 / 6
P(X = 3) = 1.1712 / 6
P(X = 3) = 0.1954
```

---

**Step 5: Add them up**

Code

```
P(X ≤ 3) = 0.0183 + 0.0733 + 0.1465 + 0.1954
P(X ≤ 3) = 0.4335 or 43.35%
```

---

### **Answer**:

There is a **43.35%** probability that at most 3 patients will arrive in the next hour.

---

**At least x events**:

**Scenario**: A customer service center receives an average of 3 calls per hour.

**Question**: What is the probability that **at least 5 calls** are received in the next hour?

---

### **Solution:**

**Given**:

- λ = 3 (average calls per hour)
- We need P(X ≥ 5)

**Formula**:

Code

```
P(X ≥ 5) = 1 - P(X < 5)
P(X ≥ 5) = 1 - P(X ≤ 4)
P(X ≥ 5) = 1 - [P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4)]
```

**Why use complement?** It's easier to calculate a few probabilities and subtract from 1 than to calculate infinite probabilities (5, 6, 7, 8, ...).