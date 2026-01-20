# Probability Concepts

## Independent Events
Events where the outcome of one does not affect the outcome of another.

**Criteria:** P(A|B) = P(A) and P(B|A) = P(B)

**Formula:** P(A∩B) = P(A) × P(B)

**Explanation:** When events are independent, knowing the outcome of one event gives no information about the other event. The probability of both occurring is simply the product of their individual probabilities.

**Example:** Rolling a die and flipping a coin. Getting heads doesn't affect the die roll. P(heads and 6) = 1/2 × 1/6 = 1/12

## Mutually Exclusive Events
Events that cannot occur at the same time.

**Criteria:** P(A∩B) = 0 (no overlap possible)

**Formula:** P(A∪B) = P(A) + P(B)

**Explanation:** Since mutually exclusive events cannot happen simultaneously, there is no intersection to consider. The probability of either event occurring is simply the sum of their individual probabilities.

**Example:** Rolling a 3 and rolling a 5 on a single die roll. These cannot happen simultaneously. P(3 or 5) = 1/6 + 1/6 = 2/6 = 1/3

## Union (A∪B)
The probability that event A or B or both will occur.

**Formula:** P(A∪B) = P(A) + P(B) - P(A∩B)

**Explanation:** We add the individual probabilities but subtract the intersection to avoid double counting events that satisfy both conditions.

**Example:** The probability of rolling a 2 or 4 on a single die = 1/6 + 1/6 = 2/6 = 1/3

## Intersection (A∩B)
The probability that event A and B will both occur.

**Formula:** P(A∩B) = P(A) × P(B) (for independent events)

**Explanation:** For independent events, multiply the individual probabilities. For dependent events, use conditional probability.

**Example:** The probability of rolling an even number and a number greater than 4 = P(even ∩ >4) = P(6) = 1/6

## At Least
Means that number or more.

**Formula:** P(X ≥ k) = 1 - P(X < k)

**Explanation:** Often easier to calculate the complement (less than) and subtract from 1.

**Example:** The probability of rolling at least 5 means rolling a 5 or 6 = 2/6 = 1/3

## At Most
Means that number or less.

**Formula:** P(X ≤ k) = P(X = 1) + P(X = 2) + ... + P(X = k)

**Explanation:** Sum all probabilities from the minimum value up to and including k.

**Example:** The probability of rolling at most a 2 means rolling a 1 or 2 = 1/6 + 1/6 = 2/6 = 1/3

## Only
Means exactly that event and no others occur.

**Formula:** P(only A) = P(A) - P(A∩B) - P(A∩C) - ... (excluding overlaps)

**Explanation:** Calculate the probability of the event minus any intersections with other specified events.

**Example:** If we want only event A to occur (not B or C), we take P(A) and subtract the probability that A occurs with any other events. For instance, if P(A) = 0.6, P(A∩B) = 0.2, and P(A∩C) = 0.1, then P(only A) = 0.6 - 0.2 - 0.1 = 0.3

---

## 🎲 **Two Dice Problem: Sum of At Least 10**

### **Problem Statement:**
When you roll two standard six-sided dice and add their numbers together, what is the probability of getting a sum of at least 10?

### **Step-by-Step Solution:**

#### **Step 1: Identify the Sample Space**
```
Total possible outcomes when rolling two dice = 6 × 6 = 36
Each outcome: (die 1, die 2)
```

#### **Step 2: Define the Event**
```
Event A: Sum ≥ 10
This means: Sum = 10, 11, or 12
```

#### **Step 3: Find All Favorable Outcomes**

**Sum = 10:**
```
(4,6), (5,5), (6,4) → 3 ways
```

**Sum = 11:**
```
(5,6), (6,5) → 2 ways
```

**Sum = 12:**
```
(6,6) → 1 way
```

**Total favorable outcomes = 3 + 2 + 1 = 6**

#### **Step 4: Calculate Probability**
```
P(sum ≥ 10) = Favorable outcomes / Total outcomes
P(sum ≥ 10) = 6/36 = 1/6 ≈ 0.167 or 16.67%
```

### **Alternative Method: Using Complement**

Instead of finding P(sum ≥ 10), we can find P(sum < 10) and subtract from 1.

#### **Sum < 10 means sum = 2, 3, 4, 5, 6, 7, 8, or 9**

**Counting outcomes for each sum:**
- Sum = 2: (1,1) → 1 way
- Sum = 3: (1,2), (2,1) → 2 ways  
- Sum = 4: (1,3), (2,2), (3,1) → 3 ways
- Sum = 5: (1,4), (2,3), (3,2), (4,1) → 4 ways
- Sum = 6: (1,5), (2,4), (3,3), (4,2), (5,1) → 5 ways
- Sum = 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → 6 ways
- Sum = 8: (2,6), (3,5), (4,4), (5,3), (6,2) → 5 ways
- Sum = 9: (3,6), (4,5), (5,4), (6,3) → 4 ways

**Total outcomes for sum < 10 = 1+2+3+4+5+6+5+4 = 30**

```
P(sum < 10) = 30/36 = 5/6
P(sum ≥ 10) = 1 - P(sum < 10) = 1 - 5/6 = 1/6 ✓
```

### **Verification Table:**

| Sum | Outcomes | Count | Probability |
|-----|----------|-------|-------------|
| 2   | (1,1) | 1 | 1/36 |
| 3   | (1,2), (2,1) | 2 | 2/36 |
| 4   | (1,3), (2,2), (3,1) | 3 | 3/36 |
| 5   | (1,4), (2,3), (3,2), (4,1) | 4 | 4/36 |
| 6   | (1,5), (2,4), (3,3), (4,2), (5,1) | 5 | 5/36 |
| 7   | (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) | 6 | 6/36 |
| 8   | (2,6), (3,5), (4,4), (5,3), (6,2) | 5 | 5/36 |
| 9   | (3,6), (4,5), (5,4), (6,3) | 4 | 4/36 |
| **10** | **(4,6), (5,5), (6,4)** | **3** | **3/36** |
| **11** | **(5,6), (6,5)** | **2** | **2/36** |
| **12** | **(6,6)** | **1** | **1/36** |

### **Final Answer:**
```
P(sum ≥ 10) = 6/36 = 1/6 ≈ 0.167 or 16.67%
```

### **Key Learning Points:**
1. **Systematic counting** is crucial for dice problems
2. **Complement method** can be useful for verification
3. **Sum ≥ 10** is equivalent to **sum = 10 OR sum = 11 OR sum = 12**
4. Since these are mutually exclusive events, we add their probabilities
5. The answer 1/6 makes intuitive sense - it's relatively uncommon to get high sums

---

## 🫙 **Marble Selection Problem: At Most One Red Marble**

### **Problem Statement:**
A jar contains 5 red, 4 blue, and 1 green marble (total 10 marbles). You randomly select 3 marbles from the jar. What is the probability of selecting at most one red marble?

### **Step-by-Step Solution:**

#### **Step 1: Understand the Setup**
```
Total marbles = 5 red + 4 blue + 1 green = 10 marbles
Selection = 3 marbles (without replacement)
Event: At most 1 red marble = 0 red OR 1 red marble
```

#### **Step 2: Calculate Total Possible Outcomes**
```
Total ways to select 3 marbles from 10 = C(10,3)
C(10,3) = 10!/(3! × 7!) = (10 × 9 × 8)/(3 × 2 × 1) = 720/6 = 120
```

---

## 🧮 **Combination Formula Explained**

### **Formula: C(n,r) or "n choose r"**

**Full Formula:**
```
C(n,r) = n! / (r! × (n-r)!)
```

**Where:**
- **n** = total number of items
- **r** = number of items being selected
- **!** = factorial (e.g., 5! = 5×4×3×2×1)

### **Simplified Calculation Method:**
Instead of calculating large factorials, use:
```
C(n,r) = (n × (n-1) × (n-2) × ... × (n-r+1)) / r!
```

### **Example Breakdown: C(10,3)**

#### **Method 1: Full Factorial**
```
C(10,3) = 10! / (3! × 7!)
C(10,3) = 3,628,800 / (6 × 5,040)
C(10,3) = 3,628,800 / 30,240 = 120
```

#### **Method 2: Simplified (Recommended)**
```
C(10,3) = (10 × 9 × 8) / (3 × 2 × 1)
C(10,3) = 720 / 6 = 120
```

### **Why the Simplified Method Works:**
```
10! = 10 × 9 × 8 × 7!
So: 10!/7! = 10 × 9 × 8

Therefore: C(10,3) = (10!/7!) / 3! = (10×9×8) / 3!
```

### **Key Properties:**
1. **C(n,0) = 1** (one way to select nothing)
2. **C(n,n) = 1** (one way to select everything)
3. **C(n,r) = C(n,n-r)** (symmetry property)
4. **Order doesn't matter** (unlike permutations)

### **Common Combinations Quick Reference:**
```
C(5,0) = 1      C(5,1) = 5      C(5,2) = 10
C(5,3) = 10     C(5,4) = 5      C(5,5) = 1

C(10,0) = 1     C(10,1) = 10    C(10,2) = 45
C(10,3) = 120   C(10,4) = 210   C(10,5) = 252
```

### **When to Use Combinations:**
- **Selection problems** (choosing items from a group)
- **Order doesn't matter** (ABC = BAC = CAB)
- **Without replacement** (can't pick same item twice)
- **Probability calculations** with multiple outcomes

---

#### **Step 3: Find Favorable Outcomes (At Most 1 Red)**

**Case 1: 0 Red Marbles**
- Must select all 3 marbles from non-red marbles (4 blue + 1 green = 5 marbles)
```
C(5,3) = 5!/(3! × 2!) = (5 × 4 × 3)/(3 × 2 × 1) = 60/6 = 10 ways
```

**Case 2: Exactly 1 Red Marble**
- Select 1 red from 5 red marbles: C(5,1) = 5
- Select 2 non-red from 5 non-red marbles: C(5,2) = 10
```
C(5,1) × C(5,2) = 5 × 10 = 50 ways
```

#### **Step 4: Calculate Total Favorable Outcomes**
```
Favorable outcomes = Case 1 + Case 2 = 10 + 50 = 60 ways
```

#### **Step 5: Calculate Probability**
```
P(at most 1 red) = Favorable outcomes / Total outcomes
P(at most 1 red) = 60/120 = 1/2 = 0.5 or 50%
```

### **Detailed Breakdown by Cases:**

#### **Case 1: 0 Red Marbles (3 from 5 non-red)**
Possible combinations:
- 3 blue, 0 green: C(4,3) × C(1,0) = 4 × 1 = 4 ways
- 2 blue, 1 green: C(4,2) × C(1,1) = 6 × 1 = 6 ways
- **Total: 4 + 6 = 10 ways** ✓

#### **Case 2: 1 Red Marble (1 red + 2 from 5 non-red)**
Possible combinations:
- 1 red, 2 blue, 0 green: C(5,1) × C(4,2) × C(1,0) = 5 × 6 × 1 = 30 ways
- 1 red, 1 blue, 1 green: C(5,1) × C(4,1) × C(1,1) = 5 × 4 × 1 = 20 ways
- **Total: 30 + 20 = 50 ways** ✓

### **Verification Using Complement Method:**

**Alternative approach: Use P(at most 1 red) = 1 - P(at least 2 red)**

#### **Case: 2 Red Marbles**
```
C(5,2) × C(5,1) = 10 × 5 = 50 ways
```

#### **Case: 3 Red Marbles**
```
C(5,3) × C(5,0) = 10 × 1 = 10 ways
```

#### **Total for "at least 2 red":**
```
P(at least 2 red) = (50 + 10)/120 = 60/120 = 1/2
```

#### **Using complement:**
```
P(at most 1 red) = 1 - P(at least 2 red) = 1 - 1/2 = 1/2 ✓
```

### **Summary Table:**

| Scenario | Red | Blue | Green | Combinations | Count |
|----------|-----|------|-------|--------------|-------|
| **0 Red** | 0 | 3 | 0 | C(5,0)×C(4,3)×C(1,0) | 4 |
| **0 Red** | 0 | 2 | 1 | C(5,0)×C(4,2)×C(1,1) | 6 |
| **1 Red** | 1 | 2 | 0 | C(5,1)×C(4,2)×C(1,0) | 30 |
| **1 Red** | 1 | 1 | 1 | C(5,1)×C(4,1)×C(1,1) | 20 |
| | | | **Total Favorable** | | **60** |
| **2 Red** | 2 | 1 | 0 | C(5,2)×C(4,1)×C(1,0) | 40 |
| **2 Red** | 2 | 0 | 1 | C(5,2)×C(4,0)×C(1,1) | 10 |
| **3 Red** | 3 | 0 | 0 | C(5,3)×C(4,0)×C(1,0) | 10 |
| | | | **Total Unfavorable** | | **60** |
| | | | **Grand Total** | | **120** |

### **Final Answer:**
```
P(at most 1 red marble) = 60/120 = 1/2 = 0.5 or 50%
```

### **Key Learning Points:**
1. **"At most 1"** means **0 OR 1** (use addition rule for mutually exclusive events)
2. **Combination formula** C(n,r) is essential for selection problems
3. **Without replacement** changes the probability calculations
4. **Systematic case analysis** ensures all scenarios are covered
5. **Complement method** provides excellent verification
6. The **1/2 probability** is surprisingly high - this occurs because we have many non-red marbles (5 out of 10)
7. **Hypergeometric distribution** applies when sampling without replacement from finite populations
