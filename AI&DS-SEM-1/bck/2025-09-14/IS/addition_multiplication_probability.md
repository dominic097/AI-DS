# Addition and Multiplication Probability Theorems

## Overview

The **Addition and Multiplication Rules** are fundamental theorems in probability theory that allow us to calculate probabilities of complex events by combining simpler events. These rules form the foundation for all probability calculations.

---

## 🔢 **Addition Rule (OR Probability)**

### **Definition**
The Addition Rule calculates the probability that **at least one** of two events occurs (A OR B).

### **General Addition Rule**
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

Where:
- `P(A ∪ B)` = Probability of A OR B occurring
- `P(A)` = Probability of event A
- `P(B)` = Probability of event B  
- `P(A ∩ B)` = Probability of BOTH A AND B occurring

### **Special Case: Mutually Exclusive Events**
When events A and B cannot occur simultaneously:
```
P(A ∪ B) = P(A) + P(B)
```
(Since P(A ∩ B) = 0 for mutually exclusive events)

---

## ✖️ **Multiplication Rule (AND Probability)**

### **Definition**
The Multiplication Rule calculates the probability that **both** events occur (A AND B).

### **General Multiplication Rule**
```
P(A ∩ B) = P(A) × P(B|A) = P(B) × P(A|B)
```

Where:
- `P(A ∩ B)` = Probability of A AND B occurring
- `P(B|A)` = Probability of B given A has occurred
- `P(A|B)` = Probability of A given B has occurred

### **Special Case: Independent Events**
When events A and B are independent:
```
P(A ∩ B) = P(A) × P(B)
```
(Since P(B|A) = P(B) and P(A|B) = P(A) for independent events)

---

## 🛒 **Product Purchase Example: Addition Rule Applications**

### **Problem Setup**
Using our market research data with additional product categories:

| Income Level | Smartphones | Laptops | Tablets | No Purchase | Total |
|-------------|------------|---------|---------|-------------|-------|
| **Low Income** | 80 | 20 | 40 | 160 | 300 |
| **Middle Income** | 150 | 100 | 80 | 170 | 500 |
| **High Income** | 90 | 70 | 30 | 10 | 200 |
| **Total** | 320 | 190 | 150 | 340 | 1,000 |

### **Addition Rule Example 1: Smartphone OR Laptop Purchase**

**Question:** What's the probability a customer buys a smartphone OR a laptop?

**Step 1: Identify individual probabilities**
```
P(Smartphone) = 320/1,000 = 0.32
P(Laptop) = 190/1,000 = 0.19
P(Smartphone AND Laptop) = 0 (mutually exclusive - can't buy both)
```

**Step 2: Apply Addition Rule**
```
P(Smartphone OR Laptop) = P(Smartphone) + P(Laptop) - P(Smartphone AND Laptop)
P(Smartphone OR Laptop) = 0.32 + 0.19 - 0 = 0.51 = 51%
```

**Interpretation:** 51% of customers buy either a smartphone or laptop.

### **Addition Rule Example 2: High Income OR Middle Income Customer**

**Question:** What's the probability a customer is high income OR middle income?

**Step 1: Identify probabilities**
```
P(High Income) = 200/1,000 = 0.20
P(Middle Income) = 500/1,000 = 0.50
P(High Income AND Middle Income) = 0 (mutually exclusive - can't be both)
```

**Step 2: Apply Addition Rule**
```
P(High Income OR Middle Income) = 0.20 + 0.50 - 0 = 0.70 = 70%
```

**Interpretation:** 70% of customers are either high income or middle income.

### **Addition Rule Example 3: Any Purchase (Non-Mutually Exclusive)**

Let's consider a different scenario where customers can have multiple interests:

**Survey Setup:** Customers were asked about product interest (not actual purchases):
- 40% interested in smartphones
- 30% interested in laptops  
- 15% interested in BOTH smartphones and laptops

**Question:** What's the probability a customer is interested in smartphones OR laptops?

**Step 1: Identify probabilities**
```
P(Smartphone Interest) = 0.40
P(Laptop Interest) = 0.30
P(Both Interests) = 0.15
```

**Step 2: Apply General Addition Rule**
```
P(Smartphone OR Laptop Interest) = P(Smartphone) + P(Laptop) - P(Both)
P(Smartphone OR Laptop Interest) = 0.40 + 0.30 - 0.15 = 0.55 = 55%
```

**Interpretation:** 55% of customers are interested in smartphones, laptops, or both.

---

## 🔄 **Multiplication Rule Applications**

### **Example 1: Sequential Customer Purchases (Dependent Events)**

**Problem Setup:** A customer service representative calls customers who didn't purchase initially.

**Given information:**
- P(Customer answers call) = 0.60
- P(Customer purchases | Customer answers) = 0.25
- P(Customer purchases | Customer doesn't answer) = 0.05

**Question:** What's the probability a customer both answers the call AND makes a purchase?

**Step 1: Identify the events**
```
A = Customer answers call
B = Customer makes purchase
```

**Step 2: Apply Multiplication Rule**
```
P(Answers AND Purchases) = P(Answers) × P(Purchases | Answers)
P(Answers AND Purchases) = 0.60 × 0.25 = 0.15 = 15%
```

**Interpretation:** 15% of customers both answer the call and make a purchase.

### **Example 2: Independent Marketing Channels**

**Problem Setup:** Company uses two independent marketing channels:
- Email campaign: 30% response rate
- Social media campaign: 25% response rate
- Channels are independent (one doesn't affect the other)

**Question:** What's the probability a customer responds to BOTH email AND social media campaigns?

**Step 1: Identify events and independence**
```
A = Responds to email (P(A) = 0.30)
B = Responds to social media (P(B) = 0.25)
Events are independent
```

**Step 2: Apply Multiplication Rule for Independent Events**
```
P(Email AND Social Media) = P(Email) × P(Social Media)
P(Email AND Social Media) = 0.30 × 0.25 = 0.075 = 7.5%
```

**Interpretation:** 7.5% of customers respond to both marketing channels.

### **Example 3: Quality Control (Conditional Dependence)**

**Problem Setup:** Manufacturing process with two-stage quality control:
- P(Product passes Stage 1) = 0.85
- P(Product passes Stage 2 | Passed Stage 1) = 0.92
- P(Product passes Stage 2 | Failed Stage 1) = 0.30

**Question:** What's the probability a product passes BOTH stages?

**Step 1: Apply Multiplication Rule**
```
P(Pass Stage 1 AND Pass Stage 2) = P(Pass Stage 1) × P(Pass Stage 2 | Pass Stage 1)
P(Both Stages) = 0.85 × 0.92 = 0.782 = 78.2%
```

**Interpretation:** 78.2% of products pass both quality control stages.

---

## 🎯 **Extended Customer Analysis Example**

### **Complex Scenario: Customer Journey Analysis**

**Setup:** E-commerce customer behavior analysis:
- 60% of visitors browse products
- 40% of browsers add items to cart
- 70% of cart users complete purchase
- 20% of purchasers become repeat customers

**Questions and Solutions:**

#### **Question 1:** Probability of browsing OR adding to cart?
```
P(Browse) = 0.60
P(Add to Cart) = P(Browse) × P(Add | Browse) = 0.60 × 0.40 = 0.24
P(Browse ∩ Add to Cart) = P(Add to Cart) = 0.24 (cart users must browse first)

P(Browse OR Add to Cart) = P(Browse) + P(Add to Cart) - P(Browse ∩ Add to Cart)
P(Browse OR Add to Cart) = 0.60 + 0.24 - 0.24 = 0.60 = 60%

Note: Since adding to cart requires browsing, this equals just P(Browse)
```

#### **Question 2:** Probability of browsing AND purchasing?
```
P(Browse AND Purchase) = P(Browse) × P(Add | Browse) × P(Purchase | Add)
P(Browse AND Purchase) = 0.60 × 0.40 × 0.70 = 0.168 = 16.8%
```

#### **Question 3:** Probability of becoming a repeat customer (full journey)?
```
P(Full Journey) = P(Browse) × P(Add | Browse) × P(Purchase | Add) × P(Repeat | Purchase)
P(Full Journey) = 0.60 × 0.40 × 0.70 × 0.20 = 0.0336 = 3.36%
```

### **Business Insights:**
1. **60% engagement rate** at the browsing level
2. **16.8% conversion rate** from visitor to purchaser
3. **3.36% rate** for complete customer journey to repeat purchase
4. **Major drop-off points:** Browse to cart (40%) and cart to purchase (70%)

---

## 🧮 **Practical Calculation Methods**

### **Addition Rule Checklist:**

#### **Step 1: Determine if events are mutually exclusive**
```
Mutually Exclusive: P(A ∩ B) = 0
- Use: P(A ∪ B) = P(A) + P(B)
- Example: Buying smartphone OR laptop (can't buy both)

Non-Mutually Exclusive: P(A ∩ B) > 0  
- Use: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- Example: Being interested in smartphones OR laptops (can be both)
```

#### **Step 2: Apply appropriate formula**
```
Always subtract the overlap for non-mutually exclusive events
Verify: P(A ∪ B) ≤ 1 and P(A ∪ B) ≥ max(P(A), P(B))
```

### **Multiplication Rule Checklist:**

#### **Step 1: Determine if events are independent**
```
Independent: P(A|B) = P(A) and P(B|A) = P(B)
- Use: P(A ∩ B) = P(A) × P(B)
- Example: Response to different marketing channels

Dependent: P(A|B) ≠ P(A) or P(B|A) ≠ P(B)
- Use: P(A ∩ B) = P(A) × P(B|A) = P(B) × P(A|B)
- Example: Sequential customer actions
```

#### **Step 2: Apply appropriate formula**
```
Always use conditional probabilities for dependent events
Verify: P(A ∩ B) ≤ min(P(A), P(B))
```

---

## 📊 **Advanced Applications**

### **Combining Both Rules: Complex Probability Calculations**

#### **Example: Marketing Campaign Analysis**

**Setup:** Company runs three marketing campaigns:
- Email (E): 30% response rate
- Social Media (S): 25% response rate  
- Direct Mail (D): 20% response rate

**Independence assumptions:**
- Email and Social Media are independent
- Direct Mail depends on other responses: P(D|E∪S) = 0.35, P(D|(E∪S)ᶜ) = 0.15

**Question:** Probability of response to at least one campaign?

**Step 1: Calculate P(E ∪ S) using Addition Rule**
```
P(E ∪ S) = P(E) + P(S) - P(E ∩ S)
P(E ∪ S) = 0.30 + 0.25 - (0.30 × 0.25) = 0.30 + 0.25 - 0.075 = 0.475
```

**Step 2: Calculate P(D) using Law of Total Probability**
```
P(D) = P(D|E∪S) × P(E∪S) + P(D|(E∪S)ᶜ) × P((E∪S)ᶜ)
P(D) = 0.35 × 0.475 + 0.15 × (1 - 0.475) = 0.35 × 0.475 + 0.15 × 0.525
P(D) = 0.16625 + 0.07875 = 0.245
```

**Step 3: Calculate P(At least one response)**
```
P(E ∪ S ∪ D) = P(E ∪ S) + P(D) - P((E ∪ S) ∩ D)

P((E ∪ S) ∩ D) = P(D|E∪S) × P(E∪S) = 0.35 × 0.475 = 0.16625

P(E ∪ S ∪ D) = 0.475 + 0.245 - 0.16625 = 0.55375 ≈ 55.4%
```

**Business Insight:** 55.4% of customers respond to at least one marketing campaign.

---

## 🎲 **Classic Probability Examples**

### **Example 1: Card Drawing**

**Setup:** Drawing cards from a standard 52-card deck.

#### **Addition Rule Application:**
**Question:** Probability of drawing a King OR a Heart?

```
P(King) = 4/52 = 1/13
P(Heart) = 13/52 = 1/4  
P(King ∩ Heart) = 1/52 (King of Hearts)

P(King ∪ Heart) = P(King) + P(Heart) - P(King ∩ Heart)
P(King ∪ Heart) = 1/13 + 1/4 - 1/52 = 4/52 + 13/52 - 1/52 = 16/52 = 4/13 ≈ 30.8%
```

#### **Multiplication Rule Application:**
**Question:** Probability of drawing two Kings in a row (without replacement)?

```
P(First King) = 4/52 = 1/13
P(Second King | First King) = 3/51 = 1/17

P(Two Kings) = P(First King) × P(Second King | First King)
P(Two Kings) = 1/13 × 1/17 = 1/221 ≈ 0.45%
```

### **Example 2: Dice Rolling**

#### **Addition Rule Application:**
**Question:** Probability of rolling a sum of 7 OR 11 with two dice?

```
P(Sum = 7) = 6/36 = 1/6 (ways: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1)
P(Sum = 11) = 2/36 = 1/18 (ways: 5+6, 6+5)
P(Sum = 7 ∩ Sum = 11) = 0 (mutually exclusive)

P(Sum = 7 OR Sum = 11) = 1/6 + 1/18 = 3/18 + 1/18 = 4/18 = 2/9 ≈ 22.2%
```

#### **Multiplication Rule Application:**
**Question:** Probability of rolling two 6s in a row with one die?

```
P(First 6) = 1/6
P(Second 6) = 1/6 (independent events)

P(Two 6s) = P(First 6) × P(Second 6) = 1/6 × 1/6 = 1/36 ≈ 2.78%
```

---

## 🧮 **Practice Problems**

### **Problem 1: Student Performance**

A university study shows:
- 60% of students pass Math
- 70% of students pass English  
- 45% of students pass both Math and English

**Calculate:**
1. P(Pass Math OR Pass English)
2. P(Pass English | Pass Math)
3. P(Pass neither subject)

**Solutions:**
```
1. P(Math ∪ English) = P(Math) + P(English) - P(Math ∩ English)
   P(Math ∪ English) = 0.60 + 0.70 - 0.45 = 0.85 = 85%

2. P(English | Math) = P(Math ∩ English) / P(Math)
   P(English | Math) = 0.45 / 0.60 = 0.75 = 75%

3. P(Neither) = 1 - P(Math ∪ English) = 1 - 0.85 = 0.15 = 15%
```

### **Problem 2: Medical Testing**

A medical screening has:
- 5% of population has disease
- Test correctly identifies 95% of diseased patients (sensitivity)
- Test correctly identifies 90% of healthy patients (specificity)

**Calculate:**
1. P(Positive test)
2. P(Disease | Positive test)
3. P(Healthy AND Negative test)

**Solutions:**
```
1. P(Positive) = P(Positive | Disease) × P(Disease) + P(Positive | Healthy) × P(Healthy)
   P(Positive) = 0.95 × 0.05 + 0.10 × 0.95 = 0.0475 + 0.095 = 0.1425 = 14.25%

2. P(Disease | Positive) = P(Positive | Disease) × P(Disease) / P(Positive)
   P(Disease | Positive) = (0.95 × 0.05) / 0.1425 = 0.0475 / 0.1425 ≈ 33.3%

3. P(Healthy ∩ Negative) = P(Healthy) × P(Negative | Healthy)
   P(Healthy ∩ Negative) = 0.95 × 0.90 = 0.855 = 85.5%
```

---

## 💡 **Key Takeaways**

### **Addition Rule Essentials:**
1. **Use for "OR" probability questions** - at least one event occurs
2. **Check for mutual exclusivity** - determines if you subtract overlap
3. **Formula: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)**
4. **Always ≤ 1 and ≥ max(P(A), P(B))**

### **Multiplication Rule Essentials:**
1. **Use for "AND" probability questions** - both events occur
2. **Check for independence** - determines if you use conditional probabilities
3. **Formula: P(A ∩ B) = P(A) × P(B|A) = P(B) × P(A|B)**
4. **Always ≤ min(P(A), P(B))**

### **Business Applications:**
1. **Marketing:** Response rates to multiple campaigns
2. **Quality Control:** Multiple-stage testing success
3. **Customer Analytics:** Journey stage completion rates
4. **Risk Assessment:** Multiple factor probability analysis

### **Common Mistakes to Avoid:**
1. **Forgetting to subtract overlap** in Addition Rule
2. **Assuming independence** when events are dependent
3. **Confusing conditional probability** direction in Multiplication Rule
4. **Not checking if probabilities sum correctly** for exhaustive events

### **Connection to Other Concepts:**
1. **Links to conditional probability** through P(A|B) in Multiplication Rule
2. **Foundation for Bayes' theorem** and complex probability calculations
3. **Essential for understanding independence** and dependence
4. **Basis for statistical inference** and hypothesis testing

The Addition and Multiplication Rules are fundamental tools that, combined with your marginal and conditional probability knowledge, provide complete foundation for probability analysis in business and data science! 📊

---

## 🔗 **Integration with Your Other Probability Notes**

### **Building on Marginal Probability:**
- **Marginal probabilities** are the individual P(A) and P(B) used in Addition/Multiplication Rules
- **Your income level example** provides the base probabilities for complex calculations

### **Connecting to Conditional Probability:**
- **Multiplication Rule directly uses** conditional probabilities P(A|B)
- **Your customer purchase analysis** can be extended using these rules for multi-stage scenarios

### **Complete Probability Toolkit:**
1. **Marginal Probability** → Individual event probabilities
2. **Conditional Probability** → Dependent event relationships  
3. **Addition/Multiplication Rules** → Complex event combinations
4. **Together** → Complete business intelligence framework

This creates a comprehensive probability analysis system for data-driven decision making! 🎯
