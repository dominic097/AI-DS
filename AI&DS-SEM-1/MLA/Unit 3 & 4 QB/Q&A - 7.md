
![[Pasted image 20251114202540.png]]


## **i) Explain why decision stumps are used as weak learners in AdaBoost. (4 marks)**

Decision stumps are used as weak learners in AdaBoost for several reasons:

- **Simplicity**: Decision stumps are the simplest form of decision trees with only one split, making them computationally efficient and fast to train.
- **Weak learner requirement**: AdaBoost requires weak learners that perform slightly better than random guessing (>50% accuracy). Decision stumps naturally fulfill this criterion.
- **Low overfitting risk**: Since they make decisions based on a single feature, decision stumps have low complexity and are less prone to overfitting individual training samples.
- **Complementary nature**: Different stumps focus on different features, and when combined, they create a strong ensemble classifier that captures complex patterns in the data.

---

## **ii) Describe how sample weights are updated after each iteration. (4 marks)**

Sample weights are updated in AdaBoost as follows:

- **Initial weights**: All samples start with equal weights (1/N, where N is the number of samples).
- **After each iteration**:
    - **Correctly classified samples**: Their weights are **decreased** (multiplied by e^(-α)), making them less important in the next iteration.
    - **Misclassified samples**: Their weights are **increased** (multiplied by e^(α)), forcing the next weak learner to focus more on these difficult cases.
- **Normalization**: All weights are normalized so they sum to 1.
- **Effect**: This adaptive reweighting ensures that subsequent weak learners focus on samples that previous learners found difficult to classify.

---

## **iii) Suppose a stump misclassifies 10% of samples — explain how its error and alpha (importance weight) are computed. (4 marks)**

**Error Calculation:**

- The weighted error (ε) is calculated as: **ε = (sum of weights of misclassified samples) / (sum of all weights)**
- Given 10% misclassification rate: **ε = 0.10**

**Alpha Calculation:**

- The importance weight (α) is computed using: **α = 0.5 × ln((1 - ε) / ε)**
- Substituting ε = 0.10: **α = 0.5 × ln((1 - 0.10) / 0.10) = 0.5 × ln(9) ≈ 1.10**

**Interpretation:**

- Low error (0.10) results in high alpha (1.10), meaning this stump gets significant weight in the final ensemble.
- Alpha determines how much this stump contributes to the final classification decision.

---

## **iv) Discuss how boosting reduces bias but can sometimes increase variance. (4 marks)**

**Bias Reduction:**

- Boosting sequentially adds weak learners that focus on previously misclassified samples, progressively reducing training errors.
- The ensemble becomes increasingly complex, capturing intricate patterns that individual stumps cannot detect.
- This reduces **underfitting** (high bias) by creating a more flexible model.

**Variance Increase:**

- As boosting continues for many iterations, the model may become too sensitive to the training data, including noise.
- **Overfitting risk**: The model memorizes training samples rather than learning generalizable patterns.
- Misclassified samples (which might be outliers or noisy) receive increasingly high weights, causing the model to overfit to these specific cases.
- This increases **variance**, making predictions less stable on new, unseen data.

**Trade-off**: Early stopping or limiting the number of iterations helps balance bias and variance.

---

## **v) If the dataset has missing values in the "Device ID" feature, explain how AdaBoost handles this situation. (4 marks)**

AdaBoost handles missing values in features like "Device ID" through several approaches:

**1. Surrogate Splits:**

- When a decision stump cannot split on Device ID due to missing values, it uses an alternative (surrogate) feature that produces similar splits.

**2. Separate Branch:**

- Create a third branch in the decision stump specifically for missing values, treating "missing" as a distinct category.

**3. Skip Affected Samples:**

- Samples with missing Device ID are excluded when training stumps that use this feature, but included for other stumps.

**4. Imputation:**

- Missing values can be filled before training using methods like:
    - Most frequent value (mode)
    - A special "Unknown" category
    - Prediction based on other features

The specific handling depends on implementation, but AdaBoost's flexibility allows it to work around missing data by either treating it as a category or using alternative features.