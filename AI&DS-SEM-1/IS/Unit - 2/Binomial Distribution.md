The **Binomial Distribution** is a discrete probability distribution that describes the number of successes in a fixed number of independent trials, where each trial has only two possible outcomes: **success** or **failure**.

It plays a major role in **quality control and quality assurance** function. Manufacturing units do use the binomial distribution for **defective** analysis.

It's one of the most important and widely used probability distributions in statistics. For instance Binomial distribution is also being used in **service organizations** like banks, and insurance corporations to get an idea of the proportion customers who are satisfied with the service quality.


---

## **Key Characteristics**

A binomial experiment must satisfy these conditions:

1. **Fixed number of trials (n)** - The experiment is repeated a specific number of times
2. **Two possible outcomes** - Each trial results in either "success" or "failure"
3. **Independent trials** - The outcome of one trial doesn't affect another
4. **Constant probability (p)** - The probability of success remains the same for each trial

---

## **The Formula**

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


---
## **Coin Flipping**

**Problem**: Flip a fair coin 5 times. What's the probability of getting exactly 3 heads?

**Given**:

- n = 5 (number of trials)
- x = 3 (number of successes we want)
- p = 0.5 (probability of heads)
- q = 1 - 0.5 = 0.5

**Solution**:

**Step 1**: Calculate binomial coefficient

Code

```
C(5,3) = 5! / (3! × 2!)
C(5,3) = 120 / (6 × 2)
C(5,3) = 10
```

**Step 2**: Apply the formula

Code

```
P(X = 3) = C(5,3) × (0.5)³ × (0.5)²
P(X = 3) = 10 × 0.125 × 0.25
P(X = 3) = 10 × 0.03125
P(X = 3) = 0.3125 or 31.25%
```

**Answer**: There's a **31.25%** chance of getting exactly 3 heads in 5 coin flips.

---
