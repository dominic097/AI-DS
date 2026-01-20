# Conditional Probability

## Definition

**Conditional Probability** is the probability of an event occurring given that another event has already occurred. It measures how the probability of one event changes when we have information about another related event.

**Mathematical Definition:**
```
P(A|B) = P(A ∩ B) / P(B)
```

Where:
- `P(A|B)` = Probability of event A given event B has occurred
- `P(A ∩ B)` = Joint probability of both A and B occurring
- `P(B)` = Marginal probability of event B
- **Note:** P(B) > 0 (event B must be possible)

## Key Characteristics

### **1. Dependency on Given Information**

- Conditional probability changes based on the given condition
- The condition restricts the sample space to only cases where the given event occurred
- Always expressed as "probability of A given B"

### **2. Relationship to Joint and Marginal Probabilities**

- **Rearranged formula:** `P(A ∩ B) = P(A|B) × P(B)`
- Uses both joint probabilities and marginal probabilities
- Foundation for Bayes' theorem and independence testing

### **3. Restricted Sample Space**

- Original sample space gets reduced to only cases where condition B is true
- Probabilities are recalculated within this restricted space
- All conditional probabilities within the restricted space sum to 1

---

## 🛒 **Product Purchase Example: Income-Based Analysis**

### **Problem Statement:**
Using the same market research data from our marginal probability study, calculate conditional probabilities to understand purchase behavior within specific income groups.

### **Original Survey Data:**

| Income Level | Bought Product | Did Not Buy | Row Total |
|-------------|---------------|-------------|-----------|
| **Low Income** | 120 | 180 | 300 |
| **Middle Income** | 280 | 220 | 500 |
| **High Income** | 150 | 50 | 200 |
| **Column Total** | 550 | 450 | **1,000** |

### **Converting to Probability Table:**

| Income Level | Bought Product | Did Not Buy | **Marginal P(Income)** |
|-------------|---------------|-------------|----------------------|
| **Low Income** | 0.12 | 0.18 | **0.30** |
| **Middle Income** | 0.28 | 0.22 | **0.50** |
| **High Income** | 0.15 | 0.05 | **0.20** |
| **Marginal P(Purchase)** | **0.55** | **0.45** | **1.00** |

---

## 📊 **Step-by-Step Conditional Probability Calculations**

### **Question 1: Given someone bought the product, what's the probability they're high income?**

**Mathematical Setup:**
```
P(High Income | Bought Product) = P(High Income ∩ Bought Product) / P(Bought Product)
```

**Step-by-Step Calculation:**
```
P(High Income | Bought) = 0.15 / 0.55 = 0.273 = 27.3%
```

**Interpretation:** Among all customers who bought the product, 27.3% are high-income customers.

### **Question 2: Given someone is high income, what's the probability they bought the product?**

**Mathematical Setup:**
```
P(Bought Product | High Income) = P(Bought Product ∩ High Income) / P(High Income)
```

**Step-by-Step Calculation:**
```
P(Bought | High Income) = 0.15 / 0.20 = 0.75 = 75%
```

**Interpretation:** Among high-income customers, 75% bought the product.

### **Question 3: Given someone didn't buy the product, what's the probability they're low income?**

**Mathematical Setup:**
```
P(Low Income | Did Not Buy) = P(Low Income ∩ Did Not Buy) / P(Did Not Buy)
```

**Step-by-Step Calculation:**
```
P(Low Income | Did Not Buy) = 0.18 / 0.45 = 0.40 = 40%
```

**Interpretation:** Among customers who didn't buy, 40% are low-income customers.

---

## 🔍 **Complete Conditional Probability Analysis**

### **Purchase Behavior Given Income Level:**

#### **Given Low Income:**
```
P(Bought | Low Income) = 0.12 / 0.30 = 0.40 = 40%
P(Did Not Buy | Low Income) = 0.18 / 0.30 = 0.60 = 60%
Verification: 40% + 60% = 100% ✓
```

#### **Given Middle Income:**
```
P(Bought | Middle Income) = 0.28 / 0.50 = 0.56 = 56%
P(Did Not Buy | Middle Income) = 0.22 / 0.50 = 0.44 = 44%
Verification: 56% + 44% = 100% ✓
```

#### **Given High Income:**
```
P(Bought | High Income) = 0.15 / 0.20 = 0.75 = 75%
P(Did Not Buy | High Income) = 0.05 / 0.20 = 0.25 = 25%
Verification: 75% + 25% = 100% ✓
```

### **Income Distribution Given Purchase Decision:**

#### **Given Bought Product:**
```
P(Low Income | Bought) = 0.12 / 0.55 = 0.218 = 21.8%
P(Middle Income | Bought) = 0.28 / 0.55 = 0.509 = 50.9%
P(High Income | Bought) = 0.15 / 0.55 = 0.273 = 27.3%
Verification: 21.8% + 50.9% + 27.3% = 100% ✓
```

#### **Given Did Not Buy:**
```
P(Low Income | Did Not Buy) = 0.18 / 0.45 = 0.40 = 40.0%
P(Middle Income | Did Not Buy) = 0.22 / 0.45 = 0.489 = 48.9%
P(High Income | Did Not Buy) = 0.05 / 0.45 = 0.111 = 11.1%
Verification: 40.0% + 48.9% + 11.1% = 100% ✓
```

---

## 📈 **Business Insights from Conditional Probabilities**

### **Purchase Rates by Income Level:**

#### **Key Findings:**
```
Low Income: 40% purchase rate (below average)
Middle Income: 56% purchase rate (above average)
High Income: 75% purchase rate (highest)
Overall Average: 55% purchase rate
```

#### **Strategic Implications:**
1. **High-income customers are most likely to purchase** (75% vs 55% average)
2. **Low-income customers need special attention** (40% vs 55% average)
3. **Middle-income customers slightly exceed average** (good target segment)

### **Customer Composition by Purchase Decision:**

#### **Among Buyers:**
```
21.8% Low Income    } 78.2% Non-High Income
50.9% Middle Income }
27.3% High Income   } More diverse customer base
```

#### **Among Non-Buyers:**
```
40.0% Low Income    } 88.9% Non-High Income
48.9% Middle Income }
11.1% High Income   } Heavily skewed toward lower income
```

### **Marketing Strategy Insights:**
1. **Target high-income customers** for highest conversion rates
2. **Develop budget-friendly options** for low-income segment
3. **Focus retention efforts** on existing middle-income buyers
4. **Investigate barriers** preventing low-income purchases

---

## 🆚 **Conditional vs Marginal Probability Comparison**

### **Example Comparison:**

| Probability Type | Question | Calculation | Result |
|-----------------|----------|-------------|---------|
| **Marginal** | What's the overall purchase rate? | P(Bought) = 550/1000 | 55% |
| **Conditional** | What's the purchase rate among high-income customers? | P(Bought\|High Income) = 150/200 | 75% |
| **Marginal** | What proportion are high-income customers? | P(High Income) = 200/1000 | 20% |
| **Conditional** | Among buyers, what proportion are high-income? | P(High Income\|Bought) = 150/550 | 27.3% |

### **Key Differences:**

#### **Marginal Probability:**
- **Context:** Entire population
- **Sample space:** All 1,000 customers
- **Purpose:** Overall patterns and distributions
- **Example:** "55% of all customers bought the product"

#### **Conditional Probability:**
- **Context:** Specific subgroup only
- **Sample space:** Restricted to condition (e.g., only high-income customers)
- **Purpose:** Behavior within specific conditions
- **Example:** "75% of high-income customers bought the product"

---

## 🧮 **Practical Calculation Methods**

### **Method 1: Using Joint and Marginal Probabilities**
```
P(A|B) = P(A ∩ B) / P(B)

Example:
P(Bought | High Income) = P(Bought ∩ High Income) / P(High Income)
P(Bought | High Income) = 0.15 / 0.20 = 0.75
```

### **Method 2: Direct Counting (from tables)**
```
P(A|B) = Count(A and B) / Count(B)

Example:
P(Bought | High Income) = 150 / 200 = 0.75
```

### **Method 3: Using Conditional Probability Tables**

Create a table showing probabilities within each condition:

**Purchase Behavior by Income Level:**

| Income Level | P(Bought\|Income) | P(Did Not Buy\|Income) | Total |
|-------------|------------------|----------------------|-------|
| **Low Income** | 40% | 60% | 100% |
| **Middle Income** | 56% | 44% | 100% |
| **High Income** | 75% | 25% | 100% |

---

## 🎯 **Extended Example: Multi-Product Analysis**

### **Conditional Analysis for Product Categories:**

Using the extended data from marginal probability notes:

| Income Level | Smartphones | Laptops | Tablets | No Purchase | Total |
|-------------|------------|---------|---------|-------------|-------|
| **Low Income** | 80 | 20 | 40 | 160 | 300 |
| **Middle Income** | 150 | 100 | 80 | 170 | 500 |
| **High Income** | 90 | 70 | 30 | 10 | 200 |
| **Total** | 320 | 190 | 150 | 340 | 1,000 |

### **Conditional Probabilities by Income Level:**

#### **Given Low Income (300 customers):**
```
P(Smartphones | Low Income) = 80/300 = 26.7%
P(Laptops | Low Income) = 20/300 = 6.7%
P(Tablets | Low Income) = 40/300 = 13.3%
P(No Purchase | Low Income) = 160/300 = 53.3%
Total: 100% ✓
```

#### **Given Middle Income (500 customers):**
```
P(Smartphones | Middle Income) = 150/500 = 30.0%
P(Laptops | Middle Income) = 100/500 = 20.0%
P(Tablets | Middle Income) = 80/500 = 16.0%
P(No Purchase | Middle Income) = 170/500 = 34.0%
Total: 100% ✓
```

#### **Given High Income (200 customers):**
```
P(Smartphones | High Income) = 90/200 = 45.0%
P(Laptops | High Income) = 70/200 = 35.0%
P(Tablets | High Income) = 30/200 = 15.0%
P(No Purchase | High Income) = 10/200 = 5.0%
Total: 100% ✓
```

### **Business Insights from Multi-Product Analysis:**

#### **Product Preferences by Income:**
1. **High-income customers:** Prefer smartphones (45%) and laptops (35%), very low non-purchase rate (5%)
2. **Middle-income customers:** Balanced across products, moderate non-purchase rate (34%)
3. **Low-income customers:** High non-purchase rate (53.3%), prefer smartphones when buying

#### **Strategic Implications:**
1. **Smartphones appeal across all income levels** but highest among high-income
2. **Laptops are luxury items** with high-income preference (35% vs 6.7% low-income)
3. **Tablets have consistent appeal** across income levels (~13-16%)
4. **Non-purchase rates vary dramatically** by income level

---

## 🧮 **Practice Problems**

### **Problem 1: Medical Testing**

A medical test has the following accuracy:
- 95% of sick patients test positive
- 98% of healthy patients test negative
- 2% of the population is actually sick

**Calculate:**
1. P(Test Positive | Sick)
2. P(Test Negative | Healthy)
3. P(Sick | Test Positive) using Bayes' theorem

**Solutions:**
```
1. P(Test Positive | Sick) = 0.95 = 95% (given)

2. P(Test Negative | Healthy) = 0.98 = 98% (given)

3. P(Sick | Test Positive) = ?
   Using Bayes' theorem:
   P(Sick | Test Positive) = P(Test Positive | Sick) × P(Sick) / P(Test Positive)
   
   First, find P(Test Positive):
   P(Test Positive) = P(Test Positive | Sick) × P(Sick) + P(Test Positive | Healthy) × P(Healthy)
   P(Test Positive) = 0.95 × 0.02 + 0.02 × 0.98 = 0.019 + 0.0196 = 0.0386
   
   Therefore:
   P(Sick | Test Positive) = (0.95 × 0.02) / 0.0386 = 0.019 / 0.0386 = 49.2%
```

### **Problem 2: Employee Performance**

Company data shows:
- 60% of employees received training
- Among trained employees, 80% received promotions
- Among untrained employees, 40% received promotions

**Calculate:**
1. P(Promotion | Trained)
2. P(Promotion | Untrained)
3. P(Trained | Promotion)

**Solutions:**
```
Given information:
P(Trained) = 0.60, so P(Untrained) = 0.40
P(Promotion | Trained) = 0.80
P(Promotion | Untrained) = 0.40

1. P(Promotion | Trained) = 0.80 = 80% (given)

2. P(Promotion | Untrained) = 0.40 = 40% (given)

3. P(Trained | Promotion) = ?
   First, find P(Promotion):
   P(Promotion) = P(Promotion | Trained) × P(Trained) + P(Promotion | Untrained) × P(Untrained)
   P(Promotion) = 0.80 × 0.60 + 0.40 × 0.40 = 0.48 + 0.16 = 0.64
   
   Therefore:
   P(Trained | Promotion) = P(Promotion | Trained) × P(Trained) / P(Promotion)
   P(Trained | Promotion) = (0.80 × 0.60) / 0.64 = 0.48 / 0.64 = 75%
```

---

## 🔗 **Relationship to Other Probability Concepts**

### **1. Independence Testing**

Two events A and B are independent if:
```
P(A|B) = P(A)  AND  P(B|A) = P(B)
```

**From our product purchase example:**
```
Check if income and purchase behavior are independent:
P(Bought) = 0.55 (marginal probability)
P(Bought | High Income) = 0.75 (conditional probability)

Since 0.75 ≠ 0.55, income and purchase behavior are NOT independent
High income customers are more likely to purchase than average
```

### **2. Bayes' Theorem**

Bayes' theorem relates conditional probabilities:
```
P(A|B) = P(B|A) × P(A) / P(B)
```

**Example from our data:**
```
We know: P(Bought | High Income) = 0.75
We want: P(High Income | Bought)

P(High Income | Bought) = P(Bought | High Income) × P(High Income) / P(Bought)
P(High Income | Bought) = 0.75 × 0.20 / 0.55 = 0.273 = 27.3%
```

### **3. Law of Total Probability**

Used to find marginal probabilities from conditional probabilities:
```
P(A) = Σ P(A|Bi) × P(Bi) for all mutually exclusive events Bi
```

**Example:**
```
P(Bought) = P(Bought | Low) × P(Low) + P(Bought | Middle) × P(Middle) + P(Bought | High) × P(High)
P(Bought) = 0.40 × 0.30 + 0.56 × 0.50 + 0.75 × 0.20
P(Bought) = 0.12 + 0.28 + 0.15 = 0.55 ✓
```

---

## 💡 **Key Takeaways**

### **Essential Concepts:**
1. **Conditional probability changes the sample space** to only include cases where the condition is met
2. **Always verify conditional probabilities within each condition sum to 1**
3. **Conditional ≠ Marginal**: P(A|B) is usually different from P(A)
4. **Use for testing independence**: If P(A|B) = P(A), then A and B are independent

### **Business Applications:**
1. **Customer segmentation**: Behavior within specific demographic groups
2. **Risk assessment**: Probability of outcomes given certain conditions
3. **Marketing effectiveness**: Response rates within target segments
4. **Quality control**: Defect rates given specific production conditions

### **Calculation Tips:**
1. **Identify the condition clearly** (what comes after the "|")
2. **Restrict your sample space** to only cases where the condition is true
3. **Use joint probability divided by marginal probability** of the condition
4. **Verify results make intuitive sense** in business context

### **Common Applications in Data Science:**
1. **Machine Learning**: Feature importance and prediction accuracy
2. **A/B Testing**: Conversion rates within treatment groups
3. **Medical Diagnosis**: Disease probability given test results
4. **Finance**: Default probability given credit score ranges
5. **Marketing**: Click-through rates given customer segments

Conditional probability is fundamental for understanding how different factors influence outcomes and is essential for making data-driven business decisions! 📊

---

## 🔍 **Connection to Your Marginal Probability Notes**

### **Using Both Concepts Together:**

From your marginal probability file, we learned:
- **Marginal probabilities** show overall patterns (e.g., 55% purchase rate)
- **Conditional probabilities** reveal behavior within specific groups (e.g., 75% purchase rate among high-income customers)

### **Complete Probability Analysis Framework:**
1. **Start with marginal probabilities** to understand overall distributions
2. **Calculate conditional probabilities** to understand relationships between variables
3. **Test for independence** using conditional vs marginal comparisons
4. **Apply Bayes' theorem** to reverse conditional relationships
5. **Make business decisions** based on comprehensive probability analysis

This combination of marginal and conditional probability provides the complete foundation for statistical analysis and business intelligence! 🎯




## 🎲 **Dice Problem: Conditional Probability with Product Constraint**

### **Problem Statement:**
A pair of fair dice is rolled. Given that the product of the numbers that appear is 6, find the probability that the second die shows an even number.

### **Mathematical Setup:**
We need to find: **P(Second die is even | Product = 6)**

Using the conditional probability formula:
```
P(Second die is even | Product = 6) = P(Second die is even ∩ Product = 6) / P(Product = 6)
```

### **Step 1: Find all outcomes where the product equals 6**

**Possible factor pairs of 6:**
- 1 × 6 = 6
- 2 × 3 = 6
- 3 × 2 = 6
- 6 × 1 = 6

**All outcomes where product = 6:**
```
(1,6), (2,3), (3,2), (6,1)
```

**Total favorable outcomes for condition:** 4 outcomes

### **Step 2: Find outcomes where both conditions are met**

We need: **Product = 6 AND Second die is even**

**Check each outcome:**
- (1,6): Product = 6 ✓, Second die = 6 (even) ✓
- (2,3): Product = 6 ✓, Second die = 3 (odd) ✗
- (3,2): Product = 6 ✓, Second die = 2 (even) ✓
- (6,1): Product = 6 ✓, Second die = 1 (odd) ✗

**Outcomes satisfying both conditions:** (1,6) and (3,2)
**Count:** 2 outcomes

### **Step 3: Calculate the conditional probability**

```
P(Second die is even | Product = 6) = 2/4 = 1/2 = 0.5 = 50%
```

### **Alternative Verification Method:**

**Within the restricted sample space (product = 6):**
- Total outcomes: {(1,6), (2,3), (3,2), (6,1)}
- Outcomes with even second die: {(1,6), (3,2)}
- Probability = 2/4 = 50%

### **Answer:**
The probability that the second die shows an even number, given that the product is 6, is **1/2 or 50%**.

### **Key Insight:**
Even though we started with 36 possible outcomes when rolling two dice, the condition "product = 6" restricts our sample space to only 4 outcomes, making the calculation much simpler.
