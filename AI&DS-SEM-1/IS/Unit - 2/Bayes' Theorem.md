	Bayes' Theorem is a mathematical formula in probability theory that describes how to update the probability of a hypothesis when new evidence becomes available. it tells us how to rationally change our minds when we learn new

(OR)

	Bayes' theorem is a mathematical formula that describes the probability of an event based on prior knowledge of conditions that might be related to that event. It is fundamental in probability theory and statistics, providing a way to update probabilities as new evidence becomes available.

### **Formula**

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


---

### **The Logic Behind the Formula**

Bayes' Theorem works on the principle of **updating beliefs with evidence**:

1. **Start with a prior belief**: P(H)
2. **Observe some evidence**: E
3. **Calculate updated belief**: P(H | E)

The formula tells us:

```
Updated Belief = (How well evidence supports hypothesis / How common evidence is overall) × Initial Belief
```

### **Why We Divide by P(E)?**

The division by P(E) is a **normalization step**:

- If evidence is **rare** (small P(E)), seeing it is more significant and increases the posterior probability more
- If evidence is **common** (large P(E)), seeing it is less meaningful and increases the posterior probability less

---

### **Detailed Example: Medical Testing**

**Scenario**: Testing for a rare disease

**Given Information**:

- **P(Disease) = 0.01** → 1% of population has the disease (PRIOR)
- **P(Positive | Disease) = 0.99** → Test correctly identifies 99% of sick people (LIKELIHOOD)
- **P(Positive | No Disease) = 0.05** → Test incorrectly shows positive for 5% of healthy people (False Positive Rate)

**Question**: If you test positive, what's the probability you actually have the disease?

**Step 1**: Calculate P(Positive) - the total probability of testing positive

Code

```
P(Positive) = P(Positive | Disease) × P(Disease) + P(Positive | No Disease) × P(No Disease)
P(Positive) = 0.99 × 0.01 + 0.05 × 0.99
P(Positive) = 0.0099 + 0.0495
P(Positive) = 0.0594
```

**Step 2**: Apply Bayes' Theorem

Code

```
P(Disease | Positive) = [P(Positive | Disease) / P(Positive)] × P(Disease)
P(Disease | Positive) = [0.99 / 0.0594] × 0.01
P(Disease | Positive) = 16.67 × 0.01
P(Disease | Positive) = 0.167 or 16.7%
```

**Result**: Even with a positive test, there's only a **16.7%** chance you have the disease!

**Why?** Because the disease is so rare (1%), most positive tests are false positives from the 99% of healthy people.


--- 

### **Spam Filter Example**

**Scenario**: Determining if an email is spam based on the word "FREE"

**Given**:

- **H** = Email is spam
- **E** = Email contains "FREE"
- **P(H) = 0.3** → 30% of emails are spam
- **P(E | H) = 0.8** → 80% of spam contains "FREE"
- **P(E) = 0.35** → 35% of all emails contain "FREE"

**Calculate**:

Code

```
P(H | E) = [P(E | H) / P(E)] × P(H)
P(H | E) = [0.8 / 0.35] × 0.3
P(H | E) = 2.286 × 0.3
P(H | E) ≈ 0.686 or 68.6%
```

**Result**: If an email contains "FREE", there's a **68.6%** chance it's spam.

The probability increased from 30% (prior) to 68.6% (posterior) because we observed relevant evidence.


---

**Question**

In an armament production station, the explosion can occur due to short circuit, fault in the machinery, negligence of workers. From experience, the chances of these causes are 0.1, 0.3, 0.6 respectively. The chief engineer feels that an explosion can occur with probability:

- 0.3 if there is a short circuit
- 0.2 if there is a fault in the machinery
- 0.25 if the workers are negligent

Given that an explosion has occurred, determine the most likely cause of it?

### **Step 1: Identify and Define Variables**

Let's define:

- **A₁** = Short circuit occurs
- **A₂** = Fault in machinery occurs
- **A₃** = Worker negligence occurs
- **B** = Explosion occurs

---

### **Step 2: List Given Information**

**Prior Probabilities (chances of each cause):**

- P(A₁) = 0.1 (10% chance of short circuit)
- P(A₂) = 0.3 (30% chance of machinery fault)
- P(A₃) = 0.6 (60% chance of worker negligence)

**Conditional Probabilities (probability of explosion given each cause):**

- P(B | A₁) = 0.3 (30% chance explosion occurs if short circuit)
- P(B | A₂) = 0.2 (20% chance explosion occurs if machinery fault)
- P(B | A₃) = 0.25 (25% chance explosion occurs if worker negligence)

---

### **Step 3: Calculate P(B) - Total Probability of Explosion**

Using the law of total probability:

Code

```
P(B) = P(A₁)·P(B|A₁) + P(A₂)·P(B|A₂) + P(A₃)·P(B|A₃)
```

**Substitute values:**

Code

```
P(B) = (0.1 × 0.3) + (0.3 × 0.2) + (0.6 × 0.25)
P(B) = 0.03 + 0.06 + 0.15
P(B) = 0.24
```

**P(B) = 0.24** (24% overall chance of explosion)

---

### **Step 4: Apply Bayes' Theorem for Each Cause**

Now we calculate the probability of each cause **given that** an explosion has occurred.

#### **For A₁ (Short Circuit):**

Code

```
P(A₁|B) = [P(A₁) × P(B|A₁)] / P(B)
P(A₁|B) = [0.1 × 0.3] / 0.24
P(A₁|B) = 0.03 / 0.24
P(A₁|B) = 0.125 or 12.5%
```

---

#### **For A₂ (Machinery Fault):**

Code

```
P(A₂|B) = [P(A₂) × P(B|A₂)] / P(B)
P(A₂|B) = [0.3 × 0.2] / 0.24
P(A₂|B) = 0.06 / 0.24
P(A₂|B) = 0.25 or 25%
```

---

#### **For A₃ (Worker Negligence):**

Code

```
P(A₃|B) = [P(A₃) × P(B|A₃)] / P(B)
P(A₃|B) = [0.6 × 0.25] / 0.24
P(A₃|B) = 0.15 / 0.24
P(A₃|B) = 0.625 or 62.5%
```

---

### **Step 5: Summary of Results**

|Cause|Prior Probability|Explosion Likelihood|Posterior Probability (Given Explosion)|
|---|---|---|---|
|**Short Circuit (A₁)**|10%|30%|**12.5%**|
|**Machinery Fault (A₂)**|30%|20%|**25%**|
|**Worker Negligence (A₃)**|60%|25%|**62.5%**|

---

### **Step 6: Verification**

Check that probabilities sum to 1:

Code

```
P(A₁|B) + P(A₂|B) + P(A₃|B) = 0.125 + 0.25 + 0.625 = 1.0 ✓
```

---

## **Final Answer**

The most likely cause of the explosion is Worker Negligence (A₃) with a probability of 62.5%

------
---

