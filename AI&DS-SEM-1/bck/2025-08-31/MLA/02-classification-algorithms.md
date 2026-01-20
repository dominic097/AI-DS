# Classification Algorithms - 31 Aug 2025

## Classification Algorithms

### Linear Algorithms

- **Logistic Regression**: Uses logistic function for probability-based classification

#### Logistic Regression Applications:

**Binary Classification:**
- Medical Diagnosis (disease/no disease)
- Email Spam Detection (spam/not spam)
- Marketing (buy/don't buy)
- Credit Approval (approve/reject)
- Fraud Detection (fraudulent/legitimate)

**Multiclass Classification (with extensions):**
- Image Classification
- Text Classification (topic categorization)
- Multi-level Sentiment Analysis

**Probability Estimation:**
- Risk Assessment in finance
- A/B Testing conversion rates
- Clinical trial success probability

**When to use Logistic Regression:**
- Need probability estimates, not just classifications
- Interpretability is important
- Small to medium datasets
- Features have linear relationship with log-odds
- As baseline before complex algorithms

- **Linear Discriminant Analysis (LDA)**: Finds linear combinations of features for class separation
- **Support Vector Machine (SVM)**: Creates optimal hyperplane to separate classes

### Tree-Based Algorithms

- **Decision Trees**: Uses tree-like model of decisions and their consequences
- **Random Forest**: Ensemble of decision trees with voting mechanism
- **Gradient Boosting**: Sequential ensemble that corrects previous model errors
- **XGBoost**: Optimized gradient boosting framework
- **AdaBoost**: Adaptive boosting that focuses on misclassified examples

### Probabilistic Algorithms

- **Naive Bayes**: Based on Bayes' theorem with independence assumption
- **Gaussian Naive Bayes**: For continuous features with normal distribution
- **Multinomial Naive Bayes**: For discrete features (text classification)

### Instance-Based Algorithms

- **K-Nearest Neighbors (KNN)**: Classifies based on majority vote of k nearest neighbors
- **K-Means**: Clustering algorithm adapted for classification

### Neural Network Algorithms

- **Perceptron**: Single-layer neural network for linearly separable data
- **Multi-Layer Perceptron (MLP)**: Deep neural network with hidden layers
- **Convolutional Neural Networks (CNN)**: Specialized for image classification
- **Recurrent Neural Networks (RNN)**: For sequential data classification

### Ensemble Methods

- **Bagging**: Bootstrap aggregating with parallel model training
- **Voting Classifier**: Combines predictions from multiple algorithms
- **Stacking**: Uses meta-learner to combine base model predictions
