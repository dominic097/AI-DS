# Co-occurrence - 31 Aug 2025

## Introduction to Co-occurrence

**Co-occurrence** is a statistical measure that quantifies how often two events, items, or features appear together within a specific context or dataset. Unlike covariance which measures linear relationships between continuous variables, co-occurrence deals with the frequency of joint appearances.

### Definition

Co-occurrence measures the simultaneous presence or joint frequency of two or more elements in a given context. It's fundamental in text analysis, market basket analysis, bioinformatics, and social network analysis.

## Mathematical Formulas

### Basic Co-occurrence Count

```
Co-occurrence(A,B) = Count of instances where A and B appear together

Simple Formula:
Co-occ(A,B) = |{instances where both A and B are present}|
```

### Co-occurrence Probability

```
P(A,B) = Co-occurrence(A,B) / Total instances

Where:
- P(A,B) = Probability of A and B occurring together
- Total instances = All possible instances in the dataset
```

### Conditional Co-occurrence

```
P(B|A) = Co-occurrence(A,B) / Count(A)

Where:
- P(B|A) = Probability of B given A is present
- Count(A) = Total occurrences of A
```

### Normalized Co-occurrence (Jaccard Similarity)

```
Jaccard(A,B) = Co-occurrence(A,B) / (Count(A) + Count(B) - Co-occurrence(A,B))

Range: 0 to 1
- 0 = Never co-occur
- 1 = Always co-occur together
```

## Step-by-Step Calculation

### Classroom Example: Text Analysis Co-occurrence

Let's analyze word co-occurrence in a text mining scenario using the blackboard example:

**Problem:** Calculate co-occurrence matrix of three key documents
- Doc1: "the cat sat"  
- Doc2: "the dog ran"
- Doc3: "the cat ran"

**Goal:** Find how often words appear together across these documents

### Step 1: Define the List of Items

From our three documents, we identify the unique words:
**Items:** the, cat, sat, dog, ran

### Step 2: Create an Empty Co-occurrence Matrix

We need a 5×5 matrix for our 5 unique words:

```
        the  cat  sat  dog  ran
the     [ 0   0    0    0    0  ]
cat     [ 0   0    0    0    0  ]
sat     [ 0   0    0    0    0  ]
dog     [ 0   0    0    0    0  ]
ran     [ 0   0    0    0    0  ]
```

### Step 3: Count Co-occurrences Document by Document

**Document 1: "the cat sat"**
- Word pairs in same document:
  - (the, cat) ✓
  - (the, sat) ✓  
  - (cat, sat) ✓
  - (cat, the) ✓ (symmetric)
  - (sat, the) ✓ (symmetric)
  - (sat, cat) ✓ (symmetric)

**Document 2: "the dog ran"**
- Word pairs in same document:
  - (the, dog) ✓
  - (the, ran) ✓
  - (dog, ran) ✓
  - (dog, the) ✓ (symmetric)
  - (ran, the) ✓ (symmetric)
  - (ran, dog) ✓ (symmetric)

**Document 3: "the cat ran"**
- Word pairs in same document:
  - (the, cat) ✓
  - (the, ran) ✓
  - (cat, ran) ✓
  - (cat, the) ✓ (symmetric)
  - (ran, the) ✓ (symmetric)
  - (ran, cat) ✓ (symmetric)

### Step 4: Fill the Co-occurrence Matrix

**Counting each pair across all documents:**

| Word Pair | Doc1 | Doc2 | Doc3 | Total Count |
|-----------|------|------|------|-------------|
| (the, cat) | ✓ | - | ✓ | 2 |
| (the, sat) | ✓ | - | - | 1 |
| (the, dog) | - | ✓ | - | 1 |
| (the, ran) | - | ✓ | ✓ | 2 |
| (cat, sat) | ✓ | - | - | 1 |
| (cat, dog) | - | - | - | 0 |
| (cat, ran) | - | - | ✓ | 1 |
| (sat, dog) | - | - | - | 0 |
| (sat, ran) | - | - | - | 0 |
| (dog, ran) | - | ✓ | - | 1 |

### Step 5: Complete Co-occurrence Matrix

```
        the  cat  sat  dog  ran
the     [ 0   2    1    1    2  ]
cat     [ 2   0    1    0    1  ]
sat     [ 1   1    0    0    0  ]
dog     [ 1   0    0    0    1  ]
ran     [ 2   1    0    1    0  ]
```

### Step 6: Interpret the Results

**Key Insights from the Matrix:**

1. **"the" and "ran" co-occur most frequently (2 times)**
   - Appear together in Doc2: "the dog ran"
   - Appear together in Doc3: "the cat ran"

2. **"the" and "cat" co-occur 2 times**
   - Appear together in Doc1: "the cat sat"  
   - Appear together in Doc3: "the cat ran"

3. **Words that never co-occur (0 count):**
   - "cat" and "dog" (never appear in same document)
   - "sat" and "dog" (never appear in same document)
   - "sat" and "ran" (never appear in same document)

**Business/Research Applications:**
- **High co-occurrence** suggests semantic similarity
- **Zero co-occurrence** might indicate opposite contexts or unrelated topics
- **"the"** appears with all other words (common stop word pattern)

### Alternative Example: Student Course Enrollment

Let's also analyze which courses students take together in a semester:

**Dataset - 8 Students and Their Course Enrollments:**
- Student 1: [Math, Physics, Chemistry]
- Student 2: [Math, Computer Science, Statistics]  
- Student 3: [Physics, Chemistry, Biology]
- Student 4: [Math, Statistics, Economics]
- Student 5: [Computer Science, Statistics, Math]
- Student 6: [Physics, Chemistry, Math]
- Student 7: [Biology, Chemistry, Physics]
- Student 8: [Math, Economics, Statistics]

### Step 1: Create Co-occurrence Matrix

First, let's count how many times each pair of courses appears together:

**Manual Counting Process:**

**Math & Physics:**
- Student 1: ✓ (has both Math and Physics)
- Student 2: ✗ (has Math but no Physics)
- Student 3: ✗ (has Physics but no Math)
- Student 4: ✗ (has Math but no Physics)
- Student 5: ✗ (has Math but no Physics)
- Student 6: ✓ (has both Math and Physics)
- Student 7: ✗ (has Physics but no Math)
- Student 8: ✗ (has Math but no Physics)

**Count: Math & Physics = 2**

**Math & Chemistry:**
- Student 1: ✓ (has both)
- Student 2: ✗ (has Math but no Chemistry)
- Student 3: ✗ (has Chemistry but no Math)
- Student 4: ✗ (has Math but no Chemistry)
- Student 5: ✗ (has Math but no Chemistry)
- Student 6: ✓ (has both)
- Student 7: ✗ (has Chemistry but no Math)
- Student 8: ✗ (has Math but no Chemistry)

**Count: Math & Chemistry = 2**

### Step 2: Complete Co-occurrence Matrix

| Course Pair | Co-occurrence Count | Students |
|-------------|-------------------|----------|
| Math & Physics | 2 | Student 1, 6 |
| Math & Chemistry | 2 | Student 1, 6 |
| Math & Computer Science | 2 | Student 2, 5 |
| Math & Statistics | 3 | Student 2, 4, 5, 8 |
| Math & Economics | 2 | Student 4, 8 |
| Math & Biology | 0 | None |
| Physics & Chemistry | 3 | Student 1, 3, 6, 7 |
| Physics & Biology | 2 | Student 3, 7 |
| Physics & Computer Science | 0 | None |
| Physics & Statistics | 0 | None |
| Physics & Economics | 0 | None |
| Chemistry & Biology | 2 | Student 3, 7 |
| Chemistry & Computer Science | 0 | None |
| Chemistry & Statistics | 0 | None |
| Chemistry & Economics | 0 | None |
| Computer Science & Statistics | 2 | Student 2, 5 |
| Computer Science & Biology | 0 | None |
| Computer Science & Economics | 0 | None |
| Statistics & Economics | 2 | Student 4, 8 |
| Statistics & Biology | 0 | None |
| Biology & Economics | 0 | None |

### Step 3: Calculate Co-occurrence Probabilities

**Total number of students = 8**

**Example Calculations:**

**P(Math, Statistics):**
```
P(Math, Statistics) = Co-occurrence(Math, Statistics) / Total students
P(Math, Statistics) = 3 / 8 = 0.375 = 37.5%
```

**P(Physics, Chemistry):**
```
P(Physics, Chemistry) = Co-occurrence(Physics, Chemistry) / Total students
P(Physics, Chemistry) = 3 / 8 = 0.375 = 37.5%
```

### Step 4: Calculate Conditional Probabilities

**How many students take Math?**
Students with Math: 1, 2, 4, 5, 6, 8 = **6 students**

**P(Statistics | Math) = "If a student takes Math, what's the probability they also take Statistics?"**
```
P(Statistics | Math) = Co-occurrence(Math, Statistics) / Count(Math)
P(Statistics | Math) = 3 / 6 = 0.5 = 50%
```

**P(Chemistry | Physics) = "If a student takes Physics, what's the probability they also take Chemistry?"**

Students with Physics: 1, 3, 6, 7 = **4 students**
```
P(Chemistry | Physics) = Co-occurrence(Physics, Chemistry) / Count(Physics)
P(Chemistry | Physics) = 3 / 4 = 0.75 = 75%
```

### Step 5: Calculate Normalized Co-occurrence (Jaccard)

**Jaccard Similarity for Math and Statistics:**
```
Students with Math: 6
Students with Statistics: 4 (Students 2, 4, 5, 8)
Students with both Math AND Statistics: 3
Students with Math OR Statistics: 6 + 4 - 3 = 7

Jaccard(Math, Statistics) = 3 / 7 = 0.429 = 42.9%
```

**Jaccard Similarity for Physics and Chemistry:**
```
Students with Physics: 4
Students with Chemistry: 4 (Students 1, 3, 6, 7)
Students with both Physics AND Chemistry: 3
Students with Physics OR Chemistry: 4 + 4 - 3 = 5

Jaccard(Physics, Chemistry) = 3 / 5 = 0.6 = 60%
```

## Types of Co-occurrence Analysis

### 1. Text Co-occurrence (Word Pairs)

**Example: Analyzing Restaurant Reviews**

**Sample Reviews:**
- Review 1: "Great food and excellent service"
- Review 2: "Amazing food but slow service"  
- Review 3: "Good food and friendly staff"
- Review 4: "Excellent food and quick service"
- Review 5: "Tasty food and poor service"

**Word Co-occurrence Within Same Review:**

| Word Pair | Co-occurrence Count | Reviews |
|-----------|-------------------|---------|
| food & service | 4 | 1, 2, 4, 5 |
| food & excellent | 2 | 1, 4 |
| food & good/great/amazing | 3 | 1, 2, 3 |
| service & excellent | 1 | 1 |
| service & slow/poor | 2 | 2, 5 |

### 2. Market Basket Analysis

**Example: Grocery Store Transactions**

**Transaction Data:**
- Transaction 1: [Bread, Butter, Milk]
- Transaction 2: [Bread, Jam, Milk]
- Transaction 3: [Butter, Cheese, Milk]
- Transaction 4: [Bread, Butter, Cheese]
- Transaction 5: [Milk, Cheese, Yogurt]

**Item Co-occurrence:**

| Item Pair | Co-occurrence Count | Support (%) |
|-----------|-------------------|-------------|
| Bread & Butter | 2 | 40% |
| Bread & Milk | 2 | 40% |
| Butter & Milk | 2 | 40% |
| Milk & Cheese | 2 | 40% |
| Butter & Cheese | 2 | 40% |
| Bread & Jam | 1 | 20% |
| Bread & Cheese | 1 | 20% |
| Cheese & Yogurt | 1 | 20% |

**Business Insight:** Bread and Butter co-occur in 40% of transactions - good candidates for promotional bundling!

### 3. Social Network Co-occurrence

**Example: Friend Connections on Social Media**

**User Friendship Data:**
- Alice: friends with [Bob, Charlie, Diana]
- Bob: friends with [Alice, Charlie, Eve]
- Charlie: friends with [Alice, Bob, Diana, Frank]
- Diana: friends with [Alice, Charlie]
- Eve: friends with [Bob, Frank]
- Frank: friends with [Charlie, Eve]

**Mutual Friend Co-occurrence:**

| User Pair | Mutual Friends | Co-occurrence Strength |
|-----------|----------------|----------------------|
| Alice & Charlie | [Bob, Diana] | 2 |
| Alice & Bob | [Charlie] | 1 |
| Bob & Charlie | [Alice] | 1 |
| Charlie & Diana | [Alice] | 1 |
| Bob & Eve | [Frank] | 1 |
| Charlie & Frank | [Eve] | 1 |

## Co-occurrence Matrix Representation

### Binary Co-occurrence Matrix

For our course example, we can represent co-occurrence as a symmetric matrix:

```
        Math  Phys  Chem  CS    Stats Econ  Bio
Math    [ -    2     2     2     3     2    0  ]
Phys    [ 2    -     3     0     0     0    2  ]
Chem    [ 2    3     -     0     0     0    2  ]
CS      [ 2    0     0     -     2     0    0  ]
Stats   [ 3    0     0     2     -     2    0  ]
Econ    [ 2    0     0     0     2     -    0  ]
Bio     [ 0    2     2     0     0     0    -  ]
```

**Matrix Properties:**
- **Diagonal = 0 or undefined** (item with itself)
- **Symmetric**: Matrix[i,j] = Matrix[j,i]
- **Values represent co-occurrence counts**

## Applications and Use Cases

### 1. Natural Language Processing

**Word Embeddings:**
- Co-occurrence matrices help create word vectors
- Words that co-occur frequently have similar meanings
- Used in Word2Vec, GloVe algorithms

**Example Application:**
```python
# Pseudo-code for word co-occurrence
def build_cooccurrence_matrix(texts, window_size=2):
    for text in texts:
        words = text.split()
        for i, word1 in enumerate(words):
            for j in range(max(0, i-window_size), 
                          min(len(words), i+window_size+1)):
                if i != j:
                    word2 = words[j]
                    cooccurrence_matrix[word1][word2] += 1
```

### 2. Recommendation Systems

**Collaborative Filtering:**
- Items purchased/viewed together
- User behavior co-occurrence
- "Customers who bought X also bought Y"

**Example:**
- If users often buy [Phone, Phone Case] together
- High co-occurrence suggests recommending phone cases to phone buyers

### 3. Bioinformatics

**Gene Co-expression:**
- Genes expressed together in same conditions
- Protein-protein interactions
- Disease symptom co-occurrence

**Example:**
- Gene A and Gene B co-occur in 80% of cancer samples
- Suggests potential functional relationship

### 4. Social Media Analysis

**Hashtag Co-occurrence:**
- Which hashtags appear together in posts
- Topic clustering and trend analysis
- Community detection

**Example:**
- #MachineLearning and #AI co-occur in 70% of posts
- Indicates strong topical relationship

## Measuring Co-occurrence Strength

### 1. Point-wise Mutual Information (PMI)

```
PMI(A,B) = log₂(P(A,B) / (P(A) × P(B)))

Where:
- PMI > 0: A and B co-occur more than expected by chance
- PMI = 0: A and B are independent
- PMI < 0: A and B co-occur less than expected
```

**Example Calculation:**
Using our course data:
- P(Math) = 6/8 = 0.75
- P(Statistics) = 4/8 = 0.5  
- P(Math, Statistics) = 3/8 = 0.375

```
PMI(Math, Statistics) = log₂(0.375 / (0.75 × 0.5))
                      = log₂(0.375 / 0.375)
                      = log₂(1) = 0
```
**Interpretation:** Math and Statistics co-occur exactly as expected by chance.

### 2. Lift (Association Rule Mining)

```
Lift(A → B) = P(B|A) / P(B)

Where:
- Lift = 1: A and B are independent
- Lift > 1: A increases probability of B
- Lift < 1: A decreases probability of B
```

**Example:**
```
Lift(Physics → Chemistry) = P(Chemistry|Physics) / P(Chemistry)
                           = (3/4) / (4/8)
                           = 0.75 / 0.5 = 1.5
```
**Interpretation:** Students taking Physics are 1.5× more likely to also take Chemistry.

### 3. Chi-Square Test for Co-occurrence

```
χ² = Σ ((Observed - Expected)² / Expected)

Tests if co-occurrence is statistically significant
```

## Python Implementation

### Basic Co-occurrence Counter

```python
from collections import defaultdict, Counter
import numpy as np

def calculate_cooccurrence(data, window_size=1):
    """
    Calculate co-occurrence matrix from data
    
    Args:
        data: List of lists (e.g., [['Math', 'Physics'], ['Math', 'Stats']])
        window_size: For sequential data, how far to look for co-occurrences
    
    Returns:
        Co-occurrence dictionary
    """
    cooccurrence = defaultdict(lambda: defaultdict(int))
    
    for items in data:
        # For each pair of items in the same record
        for i, item1 in enumerate(items):
            for j, item2 in enumerate(items):
                if i != j:  # Don't count item with itself
                    cooccurrence[item1][item2] += 1
    
    return cooccurrence

# Example usage with our course data
course_data = [
    ['Math', 'Physics', 'Chemistry'],
    ['Math', 'Computer Science', 'Statistics'],
    ['Physics', 'Chemistry', 'Biology'],
    ['Math', 'Statistics', 'Economics'],
    ['Computer Science', 'Statistics', 'Math'],
    ['Physics', 'Chemistry', 'Math'],
    ['Biology', 'Chemistry', 'Physics'],
    ['Math', 'Economics', 'Statistics']
]

cooccurrence_matrix = calculate_cooccurrence(course_data)

# Print results
for item1 in cooccurrence_matrix:
    for item2 in cooccurrence_matrix[item1]:
        count = cooccurrence_matrix[item1][item2]
        print(f"{item1} & {item2}: {count}")
```

### Pandas Implementation

```python
import pandas as pd
import numpy as np

def create_cooccurrence_matrix(transactions):
    """
    Create co-occurrence matrix using pandas
    """
    # Create binary matrix (1 if item in transaction, 0 otherwise)
    all_items = set()
    for transaction in transactions:
        all_items.update(transaction)
    
    all_items = sorted(list(all_items))
    
    # Create binary matrix
    binary_matrix = []
    for transaction in transactions:
        row = [1 if item in transaction else 0 for item in all_items]
        binary_matrix.append(row)
    
    df = pd.DataFrame(binary_matrix, columns=all_items)
    
    # Calculate co-occurrence matrix
    cooccurrence_matrix = df.T.dot(df)
    
    return cooccurrence_matrix

# Example usage
df_cooccurrence = create_cooccurrence_matrix(course_data)
print("Co-occurrence Matrix:")
print(df_cooccurrence)
```

### Scikit-learn Implementation

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def text_cooccurrence(documents, ngram_range=(1,1)):
    """
    Calculate word co-occurrence from text documents
    """
    # Create term-document matrix
    vectorizer = CountVectorizer(ngram_range=ngram_range, stop_words='english')
    term_doc_matrix = vectorizer.fit_transform(documents)
    
    # Co-occurrence matrix = term-document matrix × its transpose
    cooccurrence_matrix = term_doc_matrix.T.dot(term_doc_matrix)
    cooccurrence_matrix.setdiag(0)  # Remove self-co-occurrence
    
    # Get feature names
    feature_names = vectorizer.get_feature_names_out()
    
    return cooccurrence_matrix.toarray(), feature_names

# Example with restaurant reviews
reviews = [
    "Great food and excellent service",
    "Amazing food but slow service", 
    "Good food and friendly staff",
    "Excellent food and quick service",
    "Tasty food and poor service"
]

cooccurrence_array, words = text_cooccurrence(reviews)

# Convert to DataFrame for better visualization
import pandas as pd
cooccurrence_df = pd.DataFrame(cooccurrence_array, 
                              index=words, 
                              columns=words)

print("Word Co-occurrence Matrix:")
print(cooccurrence_df)
```

## Co-occurrence vs Other Measures

| Measure | Purpose | Data Type | Output |
|---------|---------|-----------|--------|
| **Co-occurrence** | Frequency of joint appearance | Categorical/Binary | Count/Probability |
| **Covariance** | Linear relationship strength | Continuous | Real number |
| **Correlation** | Standardized linear relationship | Continuous | -1 to +1 |
| **Association Rules** | If-then patterns | Categorical | Rules + metrics |
| **Mutual Information** | Information shared | Any | Non-negative real |

## Common Pitfalls and Best Practices

### Pitfalls to Avoid

1. **Confusing Co-occurrence with Causation**
   - High co-occurrence ≠ causation
   - Example: Ice cream sales and swimming pool accidents co-occur (both increase in summer)

2. **Ignoring Data Sparsity**
   - Large vocabulary → sparse co-occurrence matrices
   - Many zero values can skew analysis

3. **Not Normalizing for Frequency**
   - Common words will have high co-occurrence by chance
   - Use PMI or other normalized measures

4. **Wrong Context Window**
   - In text: too small window misses relationships, too large adds noise
   - Choose window size based on domain knowledge

### Best Practices

✅ **Preprocessing:**
- Remove stop words in text analysis
- Handle rare items appropriately
- Consider minimum co-occurrence thresholds

✅ **Normalization:**
- Use normalized measures (PMI, Jaccard, Cosine similarity)
- Account for item frequency differences

✅ **Statistical Testing:**
- Test for significance (Chi-square, Fisher's exact test)
- Don't rely on raw counts alone

✅ **Domain Knowledge:**
- Choose appropriate context windows
- Validate results with domain experts

## Real-World Case Studies

### Case Study 1: Netflix Recommendation System

**Problem:** Recommend movies to users based on viewing patterns

**Co-occurrence Approach:**
- Movies watched by same users have high co-occurrence
- "Users who watched Movie A also watched Movie B"

**Implementation:**
1. Create user-movie matrix
2. Calculate movie-movie co-occurrence
3. Recommend movies with highest co-occurrence to user's history

**Results:** 
- Improved recommendation accuracy by 15%
- Reduced cold-start problems for new movies

### Case Study 2: Medical Symptom Analysis

**Problem:** Identify disease patterns from patient symptoms

**Data:** Electronic health records with symptom co-occurrence

**Approach:**
1. Extract symptom co-occurrence from patient records
2. Build symptom networks based on co-occurrence strength
3. Identify symptom clusters that suggest specific diseases

**Findings:**
- Fever + cough + fatigue high co-occurrence → flu-like illness
- Chest pain + shortness of breath → cardiac issues
- Enabled early disease detection and treatment

### Case Study 3: Social Media Trend Analysis

**Problem:** Predict trending topics on Twitter

**Method:**
1. Calculate hashtag co-occurrence in real-time
2. Identify emerging hashtag combinations
3. Predict which combinations will trend

**Results:**
- 73% accuracy in predicting trending topics 2 hours early
- Valuable for marketing campaign timing

## Advanced Topics

### 1. Temporal Co-occurrence

**Concept:** How co-occurrence changes over time

**Applications:**
- Seasonal product co-purchases
- Evolving word associations in social media
- Disease outbreak co-occurrence patterns

### 2. Weighted Co-occurrence

**Concept:** Not all co-occurrences are equal

**Examples:**
- TF-IDF weighting in text
- Distance-based weighting (closer items weighted more)
- Frequency-based weighting

### 3. Multi-level Co-occurrence

**Concept:** Co-occurrence at different granularities

**Examples:**
- Word-level, sentence-level, document-level
- Individual-level, group-level, population-level
- Product-level, category-level, brand-level

### 4. Negative Co-occurrence

**Concept:** Items that rarely appear together

**Applications:**
- Identifying substitute products
- Finding complementary user behaviors
- Anomaly detection (unusual co-occurrences)

## Summary

### Key Takeaways

✅ **Definition:** Co-occurrence measures how often items appear together  
✅ **Formula:** Basic count, probability, or normalized measures (PMI, Jaccard)  
✅ **Applications:** Recommendation systems, NLP, market basket analysis  
✅ **Implementation:** Python with pandas, scikit-learn, or custom counters  
✅ **Best Practices:** Normalize, test significance, validate with domain knowledge  

### When to Use Co-occurrence

**Use co-occurrence when:**
- Analyzing categorical or binary data
- Finding association patterns
- Building recommendation systems  
- Studying joint behaviors or events
- Text mining and NLP tasks

**Don't use when:**
- Need continuous variable relationships (use correlation)
- Causation analysis required (use causal inference)
- Small sample sizes (unreliable estimates)

### Next Steps

After mastering co-occurrence:
1. Study **Association Rule Mining** (Apriori, FP-Growth)
2. Learn **Network Analysis** for co-occurrence networks
3. Explore **Word Embeddings** for text co-occurrence
4. Study **Collaborative Filtering** for recommendation systems
