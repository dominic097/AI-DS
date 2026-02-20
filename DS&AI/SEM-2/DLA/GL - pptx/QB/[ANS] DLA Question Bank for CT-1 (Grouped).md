# DLA Question Bank — Answer Sheet (CT-1) — Grouped by Topic
> Questions reorganised into 9 topic groups for easier study and memorisation.
> Each header shows the **new question number** and the **original question number** in brackets.
> All answer content is unchanged from the original file.

---

# ━━━ Group A: Foundations — What is Deep Learning? ━━━

## Q1. [Originally Q6] Compare Machine Learning and Deep Learning with suitable examples (5 Marks)

**Answer:**

### Definitions

**Machine Learning (ML)** is a branch of artificial intelligence where algorithms learn patterns from data to make predictions or decisions. The critical characteristic of traditional ML is that it requires **human experts to manually design features** — meaningful representations of the raw data that the algorithm can work with. For example, to classify images of cats and dogs using a traditional ML algorithm, a human would first need to extract features like edge histograms, colour distributions, and texture patterns from the images.

**Deep Learning (DL)** is a specialised subset of ML that uses **artificial neural networks with many layers**. The defining advantage of DL is that it **automatically learns features directly from raw data** — no manual feature engineering is needed. The network itself discovers which features are important, at multiple levels of abstraction. Given the same raw pixels, a deep learning model will learn to detect edges, then shapes, then object parts, then full objects — entirely on its own.

---

### Comparison Table

| Aspect | Machine Learning | Deep Learning |
|--------|-----------------|---------------|
| **Feature Engineering** | Manual — requires domain expertise | Automatic — learned by the network |
| **Data Requirement** | Works well with hundreds to thousands of samples | Needs large datasets (tens of thousands to millions) |
| **Computational Cost** | Low to moderate — runs on CPU | High — requires GPUs or TPUs |
| **Interpretability** | Models like Decision Trees are interpretable | Neural networks are largely "black boxes" |
| **Performance on Images/Audio** | Limited — depends on quality of manual features | Excellent — state of the art |
| **Performance on Tabular/Structured Data** | Often better — less data, faster, interpretable | Not always superior for small structured datasets |
| **Training Time** | Fast | Slow |
| **Example Algorithms** | SVM, Random Forest, Decision Tree, KNN | CNN, RNN, LSTM, Transformer |

---

### Suitable Examples

| Task | ML Approach | DL Approach |
|------|-------------|-------------|
| **Image Classification** | SVM trained on manually extracted HOG (Histogram of Gradients) features | CNN trained directly on raw pixels — automatically learns filters |
| **Sentiment Analysis** | TF-IDF bag-of-words + Logistic Regression | LSTM or Transformer (BERT) trained on raw token sequences |
| **Fraud Detection** | Random Forest on hand-crafted transaction features (amount, time, location) | Deep neural network that discovers patterns in raw transaction sequences |

---

### Key Insight: The Data Size Factor
The relationship between data size and performance is the defining factor in choosing between ML and DL. With small datasets, traditional ML methods are often better because they generalise well with less data and are faster to train. As dataset size grows into the millions, deep learning's ability to automatically extract rich features causes it to significantly outperform traditional ML.

```
Performance
    │          Deep Learning ↗
    │        ╱
    │      ╱
    │    ╱ Machine Learning (plateaus)
    │__╱________________________________
                   Data Size →
```

---

## Q2. [Originally Q13] Define Deep Learning. Why is it called "deep"? Explain with architecture details (5 Marks)

**Answer:**

### Definition
**Deep Learning** is a subfield of Machine Learning that uses **artificial neural networks with many layers** to learn hierarchical representations from raw data automatically. Deep Learning has revolutionised fields like computer vision, natural language processing, and speech recognition by achieving human-level or superhuman performance on tasks that were previously intractable.

---

### Why is it Called "Deep"?
The term "deep" refers to the **number of hidden layers** in the neural network — its depth. A traditional "shallow" neural network might have just 1 hidden layer. A **deep** neural network has many hidden layers — commonly 10, 50, or even hundreds.

The depth is not just about quantity; it fundamentally changes what the network can learn. Each layer transforms the data into a **more abstract representation**. The network learns a **hierarchy of features** — simple features in early layers, complex concepts in later layers.

**Hierarchical Feature Learning (example: face recognition)**

```
Layer              What it Detects
──────────────────────────────────────────────────────
Input              Raw pixel values (brightness numbers)
Hidden Layer 1     Simple edges — horizontal, vertical, diagonal lines
Hidden Layer 2     Corners, curves, basic textures
Hidden Layer 3     Eyes, nose, mouth shapes, hair patterns
Hidden Layer 4     Full face regions — forehead, jaw, cheekbones
Output             Identity: "This is Person A"
```

No human programmed these intermediate representations — the network discovered them entirely on its own from millions of labelled examples.

---

### Architecture of a Deep Neural Network

A deep neural network consists of three types of layers:

**1. Input Layer**
Receives the raw data. The number of neurons equals the dimensionality of the input. For a 28×28 grayscale image, the input layer has 784 neurons (one per pixel). For a sentence, it might be token embeddings.

**2. Hidden Layers (the "deep" part)**
Multiple layers of neurons, each applying a weighted transformation followed by a non-linear activation function. Each layer receives the output of the previous layer and produces a new, more abstract representation. The network learns what representations to form — we do not specify them manually.

**3. Output Layer**
Produces the final prediction. For classification, it has one neuron per class; for regression, one neuron for the continuous value. Activation functions here depend on the task (Softmax for multi-class, Sigmoid for binary, linear for regression).

---

### Common Deep Architectures

| Architecture | Typical Depth | Primary Use Case |
|-------------|--------------|-----------------|
| **DNN** (Dense Deep NN) | 3–20 layers | Tabular/structured data |
| **CNN** (Convolutional NN) | 10–150+ layers | Images, video |
| **RNN / LSTM** | Variable | Sequences, time series, speech |
| **Transformer** | 12–96 layers | NLP, vision (BERT, GPT, ViT) |

---

### Why Depth Matters
- The **Universal Approximation Theorem** states that a sufficiently deep (or wide) network can approximate any continuous function to arbitrary precision.
- Depth provides **exponential expressiveness** — a deep network can represent functions that would require exponentially more neurons in a shallow network.
- Depth enables **transfer learning** — lower layers learn general features (edges, textures) that are reusable across tasks; only upper layers need retraining for new tasks.

---

## Q3. [Originally Q17] Explain the biological motivation of Artificial Neural Networks. Illustrate the mapping between biological neuron and ANN components (5 Marks)

**Answer:**

### Biological Motivation
The human brain is the most sophisticated information-processing system known. It contains approximately **86 billion neurons**, each connected to thousands of others through structures called **synapses**, forming a vast interconnected network. The brain learns by strengthening or weakening these synaptic connections based on experience — a principle captured by Hebb's rule: "neurons that fire together, wire together."

Artificial Neural Networks (ANNs) are a **mathematical abstraction inspired by this biological architecture**. The goal was not to perfectly simulate biology, but to capture the essential computational principles: distributed processing, parallel computation, learning through connection adjustment, and the ability to generalise from examples.

---

### Structure of a Biological Neuron

```
Dendrites ──► Cell Body (Soma) ──► Axon Hillock ──► Axon ──► Synaptic Terminals
(receive        (integrate all           (threshold        (transmit     (connect to
 signals)        incoming signals)         decision)         signal)       next neuron)
```

- **Dendrites:** Tree-like branches that receive incoming electrical signals from other neurons through synapses.
- **Cell Body (Soma):** Integrates (sums) all incoming signals. If the total stimulus exceeds the neuron's firing threshold, it generates an action potential.
- **Axon:** A long fibre that carries the action potential signal away from the cell body toward the output.
- **Synaptic Terminals:** At the end of the axon, these release neurotransmitters that pass the signal to the dendrites of the next neuron.
- **Synaptic Strength (Synapse):** The strength of the connection between two neurons. Strong synapses pass more signal; weak ones pass less. **Learning in the brain involves adjusting synaptic strengths.**

---

### Mapping: Biological Neuron ↔ ANN Components

| Biological Component | ANN Equivalent | Explanation |
|---------------------|---------------|-------------|
| **Dendrites** | **Inputs** $x_1, x_2, ..., x_n$ | Receive numerical signals from previous layer neurons |
| **Synaptic strength** | **Weights** $w_1, w_2, ..., w_n$ | Determine how much each input signal is amplified or suppressed. Learning = adjusting weights |
| **Cell Body (Soma)** | **Weighted summation** $z = \sum w_i x_i + b$ | Integrates all weighted input signals into a single value |
| **Firing threshold** | **Activation function** $f(z)$ | Decides whether and how strongly to "fire" — passes the signal forward if it exceeds a threshold |
| **Axon / Output signal** | **Neuron output** $a = f(z)$ | The signal passed forward to the next layer |
| **Synapse (connection)** | **Edge / Connection weight** | The mathematical link between two neurons in adjacent layers |
| **Neurotransmitters** | **Bias** $b$ | Acts as a baseline adjustment to the threshold — shifts when the neuron activates, independently of the inputs |

---

### ANN Neuron Diagram

```
   x₁ ──(w₁)──┐
   x₂ ──(w₂)──┤
   x₃ ──(w₃)──┼──► z = Σwᵢxᵢ + b ──► a = f(z) ──► (to next layer)
    b ──────── ┘
```

---

### Key Differences Between Biological and Artificial Neurons
- **Biological neurons** fire asynchronously, in continuous time, and use complex chemical signalling. ANNs use discrete timesteps and simple arithmetic.
- **Biological learning** involves complex molecular mechanisms (LTP, LTD). ANNs learn via gradient descent and backpropagation.
- A biological neuron can have **tens of thousands of synaptic connections** and complex dendritic computation. ANN neurons perform a simple weighted sum.
- ANNs are **highly simplified models**, designed to capture useful computational properties of biological networks, not to simulate them accurately. Despite this simplification, they achieve remarkable results.

---

# ━━━ Group B: Neural Network Architecture ━━━

## Q4. [Originally Q8] Explain the perceptron model with neat diagram and mathematical expression (5 Marks)

**Answer:**

### What is a Perceptron?
A **Perceptron** is the simplest and most fundamental model of an artificial neuron. It was proposed by Frank Rosenblatt in 1958 and is the conceptual building block of all modern neural networks. A perceptron takes multiple numerical inputs, multiplies each by a learned weight, sums them up, adds a bias, and then passes this sum through a simple threshold function to produce a binary output (0 or 1).

---

### Diagram

```
   x₁ ──(w₁)──┐
   x₂ ──(w₂)──┤
   x₃ ──(w₃)──┼──► Σ (weighted sum + bias) ──► Step function f(z) ──► ŷ (0 or 1)
    ⋮          │
   xₙ ──(wₙ)──┤
   bias b ─────┘
```

---

### Mathematical Expression

**Step 1 — Compute the weighted sum:**

$$z = \sum_{i=1}^{n} w_i x_i + b$$

**What this means:**
- We take each input $x_i$ and multiply it by its corresponding weight $w_i$.
- The weight represents the **importance** or **influence** of that input on the final decision. A larger weight means that input has a stronger effect.
- We sum all these weighted inputs together and add a bias $b$.
- The bias is like an adjustable threshold — it allows the decision boundary to shift left or right, independent of the inputs.

| Symbol | Meaning |
|--------|---------|
| $x_i$ | The $i$-th input feature (e.g., pixel brightness, temperature, etc.) |
| $w_i$ | The weight for the $i$-th input — learned during training |
| $b$ | The bias — shifts the activation threshold; also learned during training |
| $z$ | The net input or pre-activation value |
| $n$ | Total number of inputs |

---

**Step 2 — Apply the step activation function:**

$$\hat{y} = f(z) = \begin{cases} 1 & \text{if } z \geq 0 \\ 0 & \text{if } z < 0 \end{cases}$$

**What this means:** If the weighted sum exceeds zero (the threshold), the perceptron "fires" and outputs 1. Otherwise, it remains silent and outputs 0. This mimics how a biological neuron either fires an action potential or does not.

---

### Perceptron Learning Rule

The perceptron learns by comparing its prediction $\hat{y}$ with the true label $y$ and adjusting its weights:

$$w_i \leftarrow w_i + \eta \cdot (y - \hat{y}) \cdot x_i, \quad b \leftarrow b + \eta \cdot (y - \hat{y})$$

**What this means:**
- If the prediction was correct ($y = \hat{y}$), then $y - \hat{y} = 0$ and **no update is made**.
- If the prediction was 0 but should have been 1 ($y - \hat{y} = +1$): weights are **increased** proportionally to the input values — the perceptron needs to fire more strongly for this input pattern.
- If the prediction was 1 but should have been 0 ($y - \hat{y} = -1$): weights are **decreased** — the perceptron was firing when it shouldn't have.

The **learning rate** $\eta$ controls how large each correction step is.

**Convergence Theorem:** If the data is linearly separable (can be divided by a straight line), the perceptron is mathematically guaranteed to converge to a correct solution in a finite number of steps.

---

### Limitations
- A single perceptron can only classify data that is **linearly separable** — it draws a single straight line (or hyperplane) to separate classes. If the classes cannot be separated by a straight line, the perceptron fails.
- The classic example is the **XOR problem** — which cannot be solved by a single perceptron.
- This limitation is resolved by using a **Multi-Layer Perceptron (MLP)**, which stacks multiple layers of perceptrons to form a network capable of non-linear decision boundaries.

---

## Q5. [Originally Q18] Describe the Perceptron learning rule. Why can a single perceptron not solve the XOR problem? (5 Marks)

**Answer:**

### The Perceptron Learning Rule
The perceptron learning rule is a simple supervised learning algorithm that **iteratively adjusts the weights** of a perceptron based on its mistakes. It was one of the first formal learning algorithms in the history of artificial intelligence.

The core philosophy: if the perceptron predicted correctly, do nothing. If it made an error, adjust the weights to push the output in the correct direction.

$$w_i \leftarrow w_i + \eta \cdot (y - \hat{y}) \cdot x_i$$
$$b \leftarrow b + \eta \cdot (y - \hat{y})$$

**What each symbol means:**

| Symbol | Meaning |
|--------|---------|
| $w_i$ | Current weight for input $x_i$ |
| $\eta$ | Learning rate — controls how aggressively we correct errors (e.g., 0.1) |
| $y$ | The true correct label (0 or 1) |
| $\hat{y}$ | The perceptron's predicted label (0 or 1) |
| $(y - \hat{y})$ | The **error** — can be 0 (correct), +1 (predicted 0 but should be 1), or −1 (predicted 1 but should be 0) |
| $x_i$ | The $i$-th input feature for the current training sample |

**The three update cases:**
- **Correct prediction** $(y = \hat{y})$: Error = 0, no weight change. The model was right — don't fix what isn't broken.
- **False negative** $(y = 1, \hat{y} = 0)$: Error = +1. Weights are **increased** by $\eta \cdot x_i$. The perceptron needs to fire more strongly for this input pattern in the future.
- **False positive** $(y = 0, \hat{y} = 1)$: Error = −1. Weights are **decreased** by $\eta \cdot x_i$. The perceptron was firing when it shouldn't have; we damp it down.

**Perceptron Convergence Theorem:** If the two classes are linearly separable (separable by a straight line in 2D, or a hyperplane in higher dimensions), the perceptron learning rule is mathematically **guaranteed to converge** — to find a correct set of weights — in a finite number of update steps.

---

### Why a Single Perceptron Cannot Solve XOR

The XOR (Exclusive OR) function outputs 1 only when the two inputs differ:

| $x_1$ | $x_2$ | XOR Output |
|-------|-------|-----------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

A perceptron always creates a **linear decision boundary** — in 2D, a straight line of the form $w_1 x_1 + w_2 x_2 + b = 0$ that separates the plane into two half-planes.

**Plotting XOR on a 2D grid:**
```
x₂
 1  │  ● (0,1) → 1     ○ (1,1) → 0
    │
 0  │  ○ (0,0) → 0     ● (1,0) → 1
    └─────────────────────────── x₁
        0                  1
```

The circles (●) represent class 1 (XOR = 1) and empty circles (○) represent class 0 (XOR = 0). Notice that the two class-1 points are at diagonally opposite corners, and the two class-0 points are at the other two corners.

**The geometric impossibility:** No matter how you draw a straight line through this 2D space, you cannot separate the two filled circles from the two empty circles. One class is always "mixed" with the other. The XOR pattern is **not linearly separable**.

Since the perceptron's decision boundary is always linear, and XOR requires a non-linear boundary, the convergence theorem does not apply — no solution exists, and the algorithm oscillates forever without converging.

**The solution:** A **Multi-Layer Perceptron (MLP)** with at least one hidden layer can create non-linear (curved) decision boundaries by combining multiple linear boundaries. With one hidden layer of two neurons, XOR can be solved exactly.

---

## Q6. [Originally Q2] Explain Feedforward Neural Networks (FNN) and the role of backpropagation using chain rule (5 Marks)

**Answer:**

### What is a Feedforward Neural Network?
A **Feedforward Neural Network (FNN)** is the most fundamental type of artificial neural network. In an FNN, information travels in **one direction only** — from the input layer through one or more hidden layers to the output layer — with no cycles, loops, or feedback connections. This "one-way flow" is what earns it the name "feedforward."

```
Input Layer     Hidden Layer(s)     Output Layer
   x₁ ──┐
   x₂ ──┼──► [Hidden neurons] ──► [Hidden neurons] ──► ŷ (prediction)
   x₃ ──┘
```

Every neuron in one layer is connected to every neuron in the next layer (this is called a "fully connected" or "dense" layer). Each connection carries a **weight** that determines how much influence that connection has.

---

### How the Forward Pass Works
In the forward pass, each layer transforms its input into a new representation. For layer $l$:

$$z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}, \quad a^{(l)} = f\left(z^{(l)}\right)$$

**What this means:**
- $z^{(l)}$ is the raw weighted sum of inputs from the previous layer plus a bias — it's the "pre-activation" value.
- $a^{(l)}$ is the output after applying the activation function $f$ — this is what gets passed to the next layer.
- $W^{(l)}$ contains all the weights connecting layer $l-1$ to layer $l$.
- $b^{(l)}$ is the bias vector for layer $l$.
- The input to the very first hidden layer is the raw input data: $a^{(0)} = x$.

Each hidden layer learns to represent the data at a different level of abstraction. Earlier layers detect low-level features (edges, tones); later layers combine these into higher-level concepts (shapes, objects).

---

### How Backpropagation Works — 4 Steps

**Backpropagation** is an efficient algorithm that computes the gradient of the loss with respect to every weight in the network. It works by applying the **chain rule of calculus backwards** — starting from the output layer and propagating error signals back toward the input layer.

Think of it like tracing responsibility for a mistake down a chain of people: the last person made the final error, but they were influenced by the person before them, and so on all the way back.

---

**Step 1 — Forward Pass**
- Raw inputs flow through the network: Input → Hidden Layers → Output.
- Each layer applies a weighted transformation and activation function.
- The final layer produces the **predicted output** $\hat{y}$.

---

**Step 2 — Loss Computation**
- Measure the error between prediction $\hat{y}$ and true label $y$ using a **loss function**: based on the following task:

| Task | Loss Function |
|------|--------------|
| Regression | Mean Squared Error (MSE) |
| Binary classification | Binary Cross-Entropy |
| Multi-class classification | Categorical Cross-Entropy |

---

**Step 3 — Backward Pass (Chain Rule)**
- Apply the **chain rule** to compute the gradient of the loss with respect to each weight:

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}$$

**What this means:** The gradient of the loss w.r.t. a weight is computed by multiplying three local derivatives:
- $\frac{\partial L}{\partial a}$ — how much the loss changes with the neuron's output
- $\frac{\partial a}{\partial z}$ — how much the output changes with the pre-activation (the activation function's derivative)
- $\frac{\partial z}{\partial w}$ — how much the pre-activation changes with the weight (equals the input $x$)

This chain of derivatives propagates backwards from the output layer to the input layer.

---

**Step 4 — Weight Update (Gradient Descent)**

$$w_{new} = w_{old} - \eta \frac{\partial L}{\partial w}$$

**What this means:** Each weight is nudged in the direction that reduces the loss. $\eta$ is the **learning rate** — it controls the size of each update step.

---

### Simple Mathematical View (Single Neuron)

For a single neuron, the entire backpropagation process simplifies to:

**Error:**
$$E = \frac{1}{2}(y - \hat{y})^2$$

The $\frac{1}{2}$ is a convenience factor that cancels the exponent when differentiating. $y$ is the true label, $\hat{y}$ is the prediction.

**Gradient (weight update):**
$$\Delta w = -\eta (y - \hat{y}) f'(z) x$$

| Symbol | Meaning |
|--------|---------|
| $\Delta w$ | The change to apply to the weight |
| $\eta$ | Learning rate |
| $(y - \hat{y})$ | The prediction error — how far off we were |
| $f'(z)$ | Derivative of the activation function — how sensitive the neuron's output was to its input |
| $x$ | The input that came into this weight — scales the update proportionally |

This repeats for every mini-batch until the network converges.

---

# ━━━ Group C: Gradient Descent & Training ━━━

## Q7. [Originally Q3] Explain the Gradient Descent algorithm with mathematical formulation and working steps (5 Marks)

**Answer:**

### What is Gradient Descent?
**Gradient Descent** is the core optimization algorithm used to train neural networks. Its purpose is to **minimise the loss function** — the measure of how wrong the model's predictions are — by iteratively adjusting the model's parameters (weights and biases).

### The Intuition: Descending a Hill
Imagine you are standing on a hilly terrain in thick fog and want to find the lowest valley (the minimum loss). You cannot see far, but you can feel the slope under your feet. The strategy is simple: **always take a small step in the direction that goes downhill**. Repeat this until you can no longer go lower — you have found the minimum.

In mathematics, the "direction uphill" is called the **gradient** of the loss function. Since we want to go downhill, we move in the **opposite direction of the gradient** (the negative gradient).

---

### Update Rule

$$\theta_{t+1} = \theta_t - \eta \cdot \nabla_\theta L(\theta_t)$$

**What this means — symbol by symbol:**

| Symbol | Meaning |
|--------|---------|
| $\theta_t$ | The current parameters (all weights and biases) at iteration $t$ |
| $\theta_{t+1}$ | The updated parameters after one step |
| $\eta$ | The **learning rate** — controls the size of each step. Small = careful but slow; large = fast but risky |
| $\nabla_\theta L(\theta_t)$ | The **gradient** of the loss function — a vector pointing in the direction of steepest increase in loss. We subtract it to go downhill |
| $L(\theta_t)$ | The loss function evaluated at the current parameters — the number we want to minimize |

The subtraction ($-\eta \cdot \nabla$) ensures we always move **against the gradient** — toward lower loss.

---

### Working Steps
1. **Initialize** all weights and biases to small random values.
2. **Forward pass** — compute predictions using current parameters and calculate loss $L$.
3. **Compute gradients** — find $\frac{\partial L}{\partial \theta}$ for every parameter using backpropagation.
4. **Update parameters** — apply the update rule: $\theta \leftarrow \theta - \eta \cdot \nabla_\theta L$.
5. **Repeat** steps 2–4 for every batch of data, for many epochs, until the loss stops decreasing (convergence).

---

### Types of Gradient Descent

| Type | Data Used Per Update | Speed | Stability | Best For |
|------|---------------------|-------|-----------|---------|
| **Batch GD** | Entire dataset ($N$ samples) | Slow | Very stable, smooth path | Small datasets |
| **Stochastic GD (SGD)** | 1 sample at a time | Fast | Noisy, erratic | Online/streaming learning |
| **Mini-Batch GD** | Small batch (32–256 samples) | Moderate | Balanced — most used | Deep learning (default) |

Mini-Batch GD is the practical standard because it balances the accuracy of Batch GD with the speed of SGD, and enables efficient GPU parallelism.

---

### Effect of Learning Rate $\eta$

| Learning Rate | What Happens |
|--------------|-------------|
| **Too large** | Steps are too big — you overshoot the valley and bounce around, possibly diverging (loss increases) |
| **Too small** | Steps are tiny — training takes forever; may get trapped in a shallow local minimum |
| **Optimal** | Smooth, steady descent to the minimum |
| **Decaying** | Starts large to move quickly, then reduces as we get close to the minimum for fine-tuning |

---

## Q8. [Originally Q21] Derive the gradient descent update rule and explain the effect of learning rate (5 Marks)

**Answer:**

### Objective
The goal of training a neural network is to find the parameters $\theta$ (all weights and biases) that **minimise the loss function** $L(\theta)$. This is a mathematical optimisation problem.

---

### Derivation Using First-Order Taylor Expansion

We want to find a change $\Delta\theta$ to apply to the current parameters $\theta_t$ such that the loss decreases:

$$L(\theta_t + \Delta\theta) < L(\theta_t)$$

Using the **first-order Taylor series expansion** — a mathematical tool that approximates how a function changes near a point — we can write:

$$L(\theta_t + \Delta\theta) \approx L(\theta_t) + \nabla_\theta L(\theta_t)^T \cdot \Delta\theta$$

**What this means:** This says the new loss is approximately the old loss plus a term that depends on the **dot product** of the gradient $\nabla_\theta L$ and the parameter change $\Delta\theta$. For the loss to decrease, we need this extra term to be **negative**.

**The dot product $\nabla_\theta L^T \cdot \Delta\theta$ is negative when $\Delta\theta$ points in the opposite direction from the gradient.**

The gradient $\nabla_\theta L$ is a vector that points in the direction of steepest **increase** in loss. So the direction of steepest **decrease** is $-\nabla_\theta L$.

We choose:

$$\Delta\theta = -\eta \cdot \nabla_\theta L(\theta_t)$$

**What this means:** We take a step of size $\eta$ (the learning rate) in the direction of the negative gradient. Substituting back:

$$L(\theta_t + \Delta\theta) \approx L(\theta_t) - \eta \cdot \|\nabla_\theta L(\theta_t)\|^2$$

Since $\|\nabla_\theta L\|^2 \geq 0$ always, and $\eta > 0$, this guarantees $L(\theta_t + \Delta\theta) \leq L(\theta_t)$ for small enough $\eta$. The loss is guaranteed to decrease (or stay the same if already at a minimum).

---

### The Derived Update Rule

$$\boxed{\theta_{t+1} = \theta_t - \eta \cdot \nabla_\theta L(\theta_t)}$$

**What this means — symbol by symbol:**

| Symbol | Meaning |
|--------|---------|
| $\theta_{t+1}$ | The new (updated) parameters after one gradient descent step |
| $\theta_t$ | The current parameters |
| $\eta$ | Learning rate — the step size; controls how far we move per iteration |
| $\nabla_\theta L(\theta_t)$ | The gradient of the loss with respect to all parameters at $\theta_t$ — the "direction uphill" in loss space |
| The minus sign | We move **against** the gradient (downhill) |

---

### Effect of Learning Rate $\eta$ on Training

| Value of $\eta$ | Behaviour | Outcome |
|----------------|-----------|---------|
| **Too large** | $\Delta\theta$ is large — overshoots the minimum, landing further up on the other side. Next step overshoots back. | Oscillation; loss may increase; model may diverge entirely |
| **Too small** | $\Delta\theta$ is tiny — progress per step is minuscule | Convergence is extremely slow; may get stuck in poor local minima; wastes computation |
| **Optimal** | Steps are appropriately sized — make meaningful progress without overshooting | Smooth, steady decrease in loss; converges efficiently |
| **Decaying schedule** | Start with a larger $\eta$ for fast initial progress; gradually reduce as training approaches convergence | Combines fast early training with precise final tuning |

```
Loss │ η too large: ↗↘↗↘ (diverges or oscillates)
     │ η optimal:   ↘↘↘  (smooth convergence)
     │ η too small: ─────────↘ (very slow)
     └──────────────────────────── Epoch →
```

---

## Q9. [Originally Q14] Differentiate Batch Gradient Descent, Stochastic Gradient Descent, and Mini-Batch Gradient Descent (5 Marks)

**Answer:**

### Overview
All three methods train a model by minimising a loss function using the same update rule:

$$\theta_{t+1} = \theta_t - \eta \cdot \nabla_\theta L$$

The fundamental difference between them is **how much of the training data is used to compute the gradient $\nabla_\theta L$ at each update step**. This choice creates important trade-offs between computational efficiency, memory usage, and training stability.

---

### 1. Batch Gradient Descent (BGD)

In Batch Gradient Descent, every single training sample is used to compute the gradient before making one parameter update. The gradient is the exact gradient of the loss over the entire dataset.

**Intuition:** Before taking any step, you survey the entire landscape from a helicopter to determine the perfect direction downhill. Every step is optimal but takes enormous time to compute.

**Characteristics:**
- Produces the most accurate gradient estimate — the direction of update is always correct.
- But: for a dataset with millions of examples, computing the gradient over all samples before taking one step is prohibitively slow.
- Requires loading the entire dataset into memory simultaneously.
- Since the gradient is exact (no noise), convergence is smooth and monotonic.
- One complete pass through the dataset = one parameter update.

---

### 2. Stochastic Gradient Descent (SGD)

In Stochastic Gradient Descent, a **single randomly chosen training sample** is used to compute the gradient and immediately update the parameters.

**Intuition:** Instead of surveying the whole landscape, you look at the slope directly under your feet right now and take a step. You update instantly after each sample, so updates are extremely fast — but based on a single, noisy measurement.

**Characteristics:**
- Very fast updates — the model parameters change after every single example.
- The gradient from one sample is a noisy estimate of the true gradient. This noisiness causes the training path to zigzag erratically rather than descend smoothly.
- This noise can actually be **beneficial** — it helps the model escape sharp local minima and find flatter, more generalisable minima (an effect called "implicit regularization").
- Memory efficient — only one sample in memory at a time.
- Used in online learning, where data arrives as a stream.

---

### 3. Mini-Batch Gradient Descent

In Mini-Batch Gradient Descent, a **small random subset** (a "mini-batch", typically 32–256 samples) is used to compute the gradient at each step. This is the standard method used in all modern deep learning.

**Intuition:** Instead of the whole landscape or just one footstep, you sample a small local region — enough to get a reasonable direction without needing the full dataset.

**Characteristics:**
- The gradient is a good (though not perfect) approximation of the true gradient. Less noisy than SGD, less expensive than Batch GD.
- Allows **GPU parallelism** — modern GPUs are designed to process batches of data simultaneously, making mini-batch computation very efficient.
- Offers the noise benefits of SGD (helping escape local minima) while being more stable and directional.
- The batch size is a hyperparameter: smaller batches → noisier but faster; larger batches → more stable but slower.

---

### Comparison Table

| Aspect | Batch GD | Stochastic GD | Mini-Batch GD |
|--------|----------|---------------|---------------|
| **Data per update** | Full dataset ($N$ samples) | 1 sample | Batch of $B$ samples (32–256) |
| **Gradient quality** | Exact (no noise) | Very noisy | Good approximation |
| **Updates per epoch** | 1 | $N$ | $N / B$ |
| **Convergence path** | Smooth | Erratic, zigzag | Mostly smooth |
| **Memory requirement** | High (entire dataset) | Very low | Moderate |
| **GPU utilisation** | Good | Poor (too small) | Excellent |
| **Typical use** | Small datasets | Online learning | Deep learning (default) |

---

## Q10. [Originally Q12] Explain the concepts of underfitting and overfitting. How does learning rate influence model performance? (5 Marks)

**Answer:**

### Overfitting: The Memoriser
**Overfitting** occurs when a model learns the training data **too precisely** — including its noise, random fluctuations, and irrelevant details — and as a result, fails to generalise to new, unseen data.

Think of it like a student who memorises the exact questions and answers from last year's exam without understanding the underlying concepts. They score perfectly on those exact questions but fail when even slightly different questions appear.

**Signs of overfitting:**
- Very high training accuracy but significantly lower test accuracy
- The gap between training and validation loss grows over time
- The model has **high variance** — small changes in training data lead to large changes in the model

---

### Underfitting: The Under-Learner
**Underfitting** occurs when a model is **too simple** to capture the underlying patterns in the data. It fails even on the training data.

Think of it like a student who barely studied — they cannot answer even the basic training questions correctly, let alone new ones.

**Signs of underfitting:**
- Both training accuracy and test accuracy are low
- The model has **high bias** — it makes systematic errors because its assumptions are too simplistic

---

### The Bias-Variance Trade-off

$$\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$$

| | Underfitting | Good Model | Overfitting |
|--|-------------|------------|------------|
| **Bias** | High — wrong assumptions | Low | Low |
| **Variance** | Low | Low | High — too sensitive to training data |
| **Training loss** | High | Low | Very low |
| **Test loss** | High | Low | High |

The goal of training is to find the **sweet spot** where both bias and variance are low — neither too simple nor too complex.

**Solutions:**
- **Overfitting:** Use more training data, apply Dropout, use L1/L2 regularization, apply Early Stopping, reduce model complexity.
- **Underfitting:** Use a more complex model (more layers/neurons), train for more epochs, reduce regularization, add more features.

---

### How Learning Rate Influences Model Performance

The learning rate $\eta$ directly controls how large each parameter update step is during gradient descent. It is one of the most important hyperparameters to tune.

| Learning Rate | What Happens Geometrically | Outcome |
|--------------|---------------------------|---------|
| **Too large** | Steps are so big that they overshoot the loss minimum and land on the other side — potentially higher than where we started. The model oscillates back and forth and may diverge entirely | Loss increases or oscillates; model fails to converge |
| **Too small** | Steps are microscopically tiny. Progress toward the minimum is real but incredibly slow | Training takes extremely long; may get stuck in a poor local minimum |
| **Optimal** | Steps are appropriately sized — large enough to make good progress, small enough not to overshoot | Smooth, steady decrease in loss; converges to a good solution |
| **Adaptive** (Adam, RMSProp) | The learning rate is adjusted automatically per parameter based on gradient history | More robust; less sensitive to the initial choice of $\eta$ |

```
Loss │ Too large: /\/\/\ (bounces, diverges)
     │ Too small: ──────────────────↘ (very slow)
     │ Optimal:   ↘↘↘↘ (converges smoothly)
     └──────────────────────────────── Epochs →
```

---

# ━━━ Group D: Optimizers ━━━

## Q11. [Originally Q1] Explain the working of Adagrad optimizer with mathematical formulation (5 Marks)

**Answer:**

### What is Adagrad?
**Adagrad** (Adaptive Gradient Algorithm) is an optimization algorithm that solves a key problem with standard gradient descent: it uses the **same learning rate for every parameter**, regardless of how often or how strongly that parameter has been updated.

Adagrad introduces **per-parameter learning rates** that automatically adapt based on the history of gradients seen for each parameter. The core insight is simple:
- A parameter that receives **large or frequent gradients** is already being trained a lot — slow it down by reducing its learning rate.
- A parameter that receives **small or rare gradients** has barely been trained — speed it up by keeping its learning rate large.

This makes Adagrad particularly powerful for **sparse data problems**, such as word embeddings in NLP, where most words appear rarely but a few words appear very often. Without Adagrad, the rare words would be undertrained.

---

### Core Idea: Accumulating History
Adagrad tracks the **sum of squared gradients** for each parameter over all past training steps. The larger this accumulated sum, the smaller the effective learning rate becomes. Think of it as a "budget" — the more you've already updated a parameter, the less aggressively you update it going forward.

---

### Mathematical Formulation

**Step 1 — Accumulate squared gradients:**

$$G_t = G_{t-1} + \left(\frac{\partial L}{\partial \theta_t}\right)^2$$

**What this means:** At each time step $t$, we add the square of the current gradient to a running total $G_t$. This accumulates the entire training history of how large the gradients were for this parameter.

| Symbol | Meaning |
|--------|---------|
| $G_t$ | Running sum of squared gradients from step 1 to step $t$ — grows over time |
| $G_{t-1}$ | The accumulated sum from the previous step |
| $\frac{\partial L}{\partial \theta_t}$ | The gradient of the loss with respect to parameter $\theta$ at step $t$ — tells us the direction and magnitude of the error signal |
| Initialized | $G_0 = 0$ for all parameters at the start |

---

**Step 2 — Parameter update:**

$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{G_t + \varepsilon}} \cdot \frac{\partial L}{\partial \theta_t}$$

**What this means:** Instead of dividing by a fixed learning rate, Adagrad divides by the square root of the accumulated history. Parameters with large history get a smaller effective step; parameters with small history get a larger step.

| Symbol | Meaning |
|--------|---------|
| $\theta_t$ | The current value of the parameter (weight or bias) at step $t$ |
| $\eta$ | The global base learning rate (e.g., 0.01) — same for all parameters initially |
| $\sqrt{G_t + \varepsilon}$ | The adaptive denominator — larger when gradients have been historically large, smaller when they've been small |
| $\varepsilon$ | A tiny constant (typically $10^{-8}$) added purely to prevent division by zero when $G_t \approx 0$ |
| $\frac{\partial L}{\partial \theta_t}$ | The gradient of the loss — tells us which direction to move the parameter |

---

### Algorithm Steps
1. Initialize all parameters $\theta$ randomly and set $G = 0$ for each parameter.
2. For each training iteration $t$:
   - Compute the forward pass to get predictions.
   - Calculate the loss $L$.
   - Compute the gradient $g_t$ for each parameter.
   - Accumulate: $G_t = G_{t-1} + g_t^2$
   - Update each parameter: $\theta_{t+1} = \theta_t - \dfrac{\eta}{\sqrt{G_t + \varepsilon}} \cdot g_t$
3. Repeat until training converges.

---

### Advantages and Disadvantages

| Advantages | Disadvantages |
|-----------|--------------|
| No manual per-parameter tuning of learning rates | $G_t$ grows **monotonically** — it never decreases, so the learning rate eventually shrinks to near zero, causing training to stall |
| Works very well for sparse data (NLP, recommendation) | Not suitable for non-convex deep networks in long runs |
| Simple to implement and understand | This limitation is directly addressed by RMSProp (which uses a decaying average instead of a cumulative sum) and Adam |

---

## Q12. [Originally Q9] Describe RMSProp optimizer and explain how it overcomes Adagrad limitations (5 Marks)

**Answer:**

### Adagrad's Limitation: The Dying Learning Rate
Before understanding RMSProp, it's important to understand **why Adagrad fails** in practice for deep networks.

Adagrad accumulates the **sum of all squared gradients** from the very beginning of training into a variable $G_t$. This sum only ever grows — it never decreases. As training continues over thousands of iterations, $G_t$ becomes very large. Since the effective learning rate is $\frac{\eta}{\sqrt{G_t}}$, a very large $G_t$ makes this fraction extremely small. Eventually, the learning rate shrinks so close to zero that **the model essentially stops learning** — even if it hasn't converged yet. This is particularly damaging in deep learning where training runs for many epochs.

---

### RMSProp: The Fix

**RMSProp (Root Mean Square Propagation)** was proposed by Geoffrey Hinton to fix this exact problem. Instead of accumulating all past squared gradients into a growing sum, RMSProp uses an **Exponential Moving Average (EMA)** — a weighted average that gives **more importance to recent gradients** and gradually forgets old ones.

Think of it like a memory with **fading recollection**: what happened 10,000 steps ago barely affects the current learning rate, but what happened 10 steps ago matters a lot. This prevents the denominator from growing indefinitely.

---

### Mathematical Formulation

**Step 1 — Compute the Exponential Moving Average of squared gradients:**

$$E[g^2]_t = \rho \cdot E[g^2]_{t-1} + (1 - \rho) \cdot g_t^2$$

**What this means:**
- At each step, we combine the **old average** (multiplied by $\rho$, which keeps most of it) with the **new squared gradient** (multiplied by $1 - \rho$, which adds a small new contribution).
- The decay rate $\rho$ controls the "memory window." With $\rho = 0.9$, about 10 recent steps contribute meaningfully; with $\rho = 0.99$, about 100 steps contribute.
- Crucially, this value **stays bounded** — it cannot grow to infinity because old values are continuously discounted.

| Symbol | Meaning |
|--------|---------|
| $E[g^2]_t$ | The moving average of squared gradients at step $t$ — bounded, unlike Adagrad's $G_t$ |
| $\rho$ | Decay rate, typically 0.9 — how much of the old average to keep |
| $(1 - \rho)$ | How much weight to give the current gradient — typically 0.1 |
| $g_t$ | The gradient of the loss at step $t$ |
| $g_t^2$ | Squared gradient — always positive, capturing gradient magnitude |

---

**Step 2 — Parameter update:**

$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{E[g^2]_t + \varepsilon}} \cdot g_t$$

**What this means:** The update rule looks identical to Adagrad's, but the denominator uses the **bounded moving average** instead of the ever-growing cumulative sum. This keeps the effective learning rate stable throughout training.

| Symbol | Meaning |
|--------|---------|
| $\eta$ | Global learning rate (e.g., 0.001) |
| $\varepsilon$ | Small constant (~$10^{-8}$) to prevent division by zero |

---

### Head-to-Head: Adagrad vs RMSProp

| Aspect | Adagrad | RMSProp |
|--------|---------|---------|
| Gradient history | Cumulative sum of all squared gradients — monotonically increases | Exponential moving average — stays bounded |
| Effective learning rate | Shrinks toward zero over time | Remains stable throughout training |
| Suited for | Short training, sparse/convex problems | Long training, non-convex deep networks |
| Memory of old gradients | Permanent | Fades over time (controlled by $\rho$) |

---

## Q13. [Originally Q19] Describe the Adam optimizer and explain how it combines momentum and RMSProp (5 Marks)

**Answer:**

### What is Adam?
**Adam (Adaptive Moment Estimation)** is the most widely used optimizer in modern deep learning. It was introduced by Diederik Kingma and Jimmy Ba in 2014 and combines the strengths of two previously developed techniques: **Momentum** and **RMSProp**.

The key insight is that both of those techniques address different issues with vanilla SGD:
- **Momentum** helps the optimizer move faster in consistent directions and smooths out oscillations.
- **RMSProp** adapts the learning rate per parameter based on gradient history, handling sparse and dense features appropriately.

Adam combines both, creating a powerful optimizer that works well on a wide variety of problems with minimal hyperparameter tuning.

---

### Mathematical Formulation (4 Steps)

**Step 1 — First Moment: Momentum (gradient direction)**

$$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$$

**What this means:** $m_t$ is an exponential moving average of the **gradients themselves** (not their squares). It captures the **direction and trend** of recent gradients. If gradients have been consistently pointing in the same direction across many steps, $m_t$ will be large in that direction — the optimizer builds up "momentum" and takes larger steps. $\beta_1 = 0.9$ means we keep 90% of the old momentum and add 10% from the current gradient. This smooths out the zigzagging that plagues plain SGD.

| Symbol | Meaning |
|--------|---------|
| $m_t$ | First moment estimate — running average of gradients at step $t$ |
| $\beta_1$ | Decay rate for first moment, typically 0.9 |
| $g_t$ | Gradient of loss at step $t$ |

---

**Step 2 — Second Moment: Variance (gradient magnitude, RMSProp-style)**

$$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$

**What this means:** $v_t$ is an exponential moving average of the **squared gradients** — exactly like RMSProp. It captures the **magnitude and variability** of recent gradients. Parameters with consistently large gradients will have a large $v_t$, which will reduce their effective learning rate. Parameters with small or infrequent gradients will have a small $v_t$, which allows larger steps. $\beta_2 = 0.999$ gives a very smooth, slowly changing estimate of gradient variance.

| Symbol | Meaning |
|--------|---------|
| $v_t$ | Second moment estimate — running average of squared gradients at step $t$ |
| $\beta_2$ | Decay rate for second moment, typically 0.999 |
| $g_t^2$ | Squared gradient — always positive, measures gradient magnitude |

---

**Step 3 — Bias Correction**

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$

**What this means:** Both $m$ and $v$ are initialised to zero. In the very early training steps, these estimates are heavily biased toward zero because the decay terms ($\beta_1^t$, $\beta_2^t$) are still close to 1. The bias correction divides by $(1 - \beta^t)$, which is small when $t$ is small, effectively **amplifying the early estimates** to compensate for the initialisation bias. As $t$ grows large, $\beta^t \rightarrow 0$ and the correction factor approaches 1 (no correction needed).

---

**Step 4 — Parameter Update**

$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \varepsilon} \cdot \hat{m}_t$$

**What this means:** The update uses the bias-corrected momentum $\hat{m}_t$ as the direction, scaled by the adaptive learning rate $\frac{\eta}{\sqrt{\hat{v}_t} + \varepsilon}$. Parameters with large gradient variance get a smaller effective step (stabilised), and parameters with small gradient variance get a larger effective step.

| Symbol | Meaning | Typical Value |
|--------|---------|--------------|
| $\eta$ | Global learning rate | 0.001 |
| $\varepsilon$ | Small constant to prevent division by zero | $10^{-8}$ |
| $\beta_1$ | First moment decay | 0.9 |
| $\beta_2$ | Second moment decay | 0.999 |

---

### How Adam Combines Momentum + RMSProp

| Component | Origin | Role in Adam |
|-----------|--------|-------------|
| **Momentum ($m_t$)** | Momentum optimizer | Provides smooth direction of update; accumulates directional inertia |
| **Adaptive scaling ($v_t$)** | RMSProp | Normalises update magnitude per parameter; prevents any single parameter from updating too aggressively |
| **Bias correction** | Adam's original contribution | Fixes initialisation bias in the early training steps |

---

# ━━━ Group E: Activation Functions & Gradient Problems ━━━

## Q14. [Originally Q4] Discuss the role of activation functions in neural networks and compare any three activation functions (5 Marks)

**Answer:**

### Why Activation Functions are Essential
An activation function is applied to the output of each neuron before passing it to the next layer. The critical reason they exist is to introduce **non-linearity** into the network.

Without activation functions, no matter how many layers a neural network has, the entire network would collapse into a single linear operation — equivalent to just one layer. It could only model straight-line (linear) relationships between inputs and outputs. Real-world data (images, speech, language) has deeply non-linear structure, so a purely linear network would be fundamentally incapable of learning it.

Activation functions also mimic the **biological firing behaviour** of neurons: a biological neuron only "fires" (sends a signal) if the incoming stimulus crosses a threshold. Similarly, an artificial activation function decides how strongly a neuron responds to its input.

---

### Comparison of Three Activation Functions

| Property | Sigmoid | Tanh | ReLU |
|----------|---------|------|------|
| **Formula** | $\sigma(x) = \dfrac{1}{1+e^{-x}}$ | $\tanh(x) = \dfrac{e^x - e^{-x}}{e^x + e^{-x}}$ | $f(x) = \max(0, x)$ |
| **Output Range** | $(0, 1)$ | $(-1, 1)$ | $[0, \infty)$ |
| **Zero-centered output** | No — always positive | Yes — centred at 0 | No |
| **Vanishing Gradient** | Yes — severe at extremes | Yes — at $\pm$ large values | No (for positive inputs) |
| **Dead Neurons** | No | No | Yes — can occur for $x \leq 0$ |
| **Typical Use** | Binary output layer | Hidden layers in RNNs | Hidden layers in CNNs, DNNs |

---

### 1. Sigmoid

$$\sigma(x) = \frac{1}{1+e^{-x}}$$

The sigmoid function produces an S-shaped curve that squashes any real number into the range $(0, 1)$. This makes it perfect for modelling **probabilities** — the output can be interpreted as "the probability of class 1."

**Problem — Vanishing Gradient:** When $x$ is very large (positive or negative), the sigmoid curve becomes nearly flat. Its derivative at these points is nearly zero. During backpropagation, multiplying near-zero derivatives across many layers causes gradients to shrink exponentially, so early layers learn almost nothing. This is the **vanishing gradient problem**.

---

### 2. Tanh (Hyperbolic Tangent)

$$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

Tanh is essentially a rescaled version of sigmoid, with output ranging from $(-1, 1)$. The key advantage over sigmoid is that its output is **zero-centred** — meaning roughly half the outputs are positive and half negative. This leads to more stable gradient updates because weight updates don't all push in the same direction.

**Problem:** Like sigmoid, tanh also saturates at large values, causing vanishing gradients in very deep networks.

---

### 3. ReLU (Rectified Linear Unit)

$$f(x) = \max(0, x)$$

ReLU is the most widely used activation function in modern deep learning. It is elegantly simple: output the input if it is positive, otherwise output zero. For positive inputs, the derivative is exactly 1 — **gradients flow through without shrinking**, solving the vanishing gradient problem that plagued sigmoid and tanh.

ReLU is also computationally very cheap — just a comparison with zero — which matters when training networks with millions of neurons.

**Problem — Dead ReLU:** If a neuron receives a large negative weight update, its input will always be negative, so it always outputs zero and receives zero gradient. The neuron is "dead" and never recovers during training. This is solved by **Leaky ReLU**, which allows a small negative slope (e.g., $0.01 \times x$) instead of clamping to zero.

---

## Q15. [Originally Q22] Discuss the problem of unit saturation in deep neural networks (5 Marks)

**Answer:**

### What is Unit Saturation?
**Unit saturation** occurs when a neuron's input falls in the region where its activation function has an extremely small derivative — the **"flat" or "saturated" region** of the function's curve. Because backpropagation computes gradients by multiplying the activation function's derivative, a near-zero derivative means **nearly zero gradient flows through that neuron**. The weights connected to a saturated neuron receive almost no update signal and effectively stop learning.

---

### Saturation in Sigmoid

The sigmoid function $\sigma(x) = \frac{1}{1+e^{-x}}$ produces an S-shaped curve. Its derivative is:

$$\sigma'(x) = \sigma(x)(1 - \sigma(x))$$

The maximum possible value of this derivative is 0.25 (at $x = 0$, where $\sigma(0) = 0.5$). For large positive or negative values of $x$, the output is near 1 or near 0, and the derivative becomes nearly zero.

| Input $x$ | Sigmoid output $\sigma(x)$ | Derivative $\sigma'(x)$ |
|-----------|--------------------------|------------------------|
| 0 | 0.5 | 0.25 (maximum) |
| 3 | 0.95 | ~0.045 |
| 5 | ~1.0 | ~0.006 (near zero) |
| -5 | ~0.0 | ~0.006 (near zero) |

**Consequence:** When neuron inputs are large in magnitude, the derivative is near zero. During backpropagation, multiplying near-zero derivatives across many saturated layers causes the gradient to virtually vanish by the time it reaches the early layers. Those layers learn almost nothing.

**Why inputs become large:** Poor weight initialisation, or as training proceeds and weights grow, can push pre-activation values far from zero, driving neurons into the saturated region.

---

### Saturation in Tanh
Tanh similarly saturates at $\pm 1$ for large inputs, producing near-zero derivatives. The situation is somewhat better than sigmoid (tanh's derivative peaks at 1 compared to sigmoid's 0.25), but the same fundamental problem exists.

---

### The Dead ReLU Problem
ReLU ($f(x) = \max(0, x)$) was designed to avoid saturation for positive inputs — its derivative is exactly 1 when $x > 0$. However, for $x \leq 0$, the derivative is exactly 0. If a neuron consistently receives negative pre-activation values (which can happen after a large, bad weight update), it will **permanently output zero** and have **zero gradient**. The neuron is "dead" — it cannot recover because no gradient flows to update its incoming weights. This is the **Dead ReLU problem**.

---

### Summary Table

| Activation | Where it Saturates | Gradient in Saturation | Problem |
|-----------|-------------------|----------------------|---------|
| **Sigmoid** | $|x|$ large (both sides) | ~0 | Vanishing gradients in deep networks |
| **Tanh** | $|x|$ large (both sides) | ~0 | Vanishing gradients (less severe than sigmoid) |
| **ReLU** | $x \leq 0$ | Exactly 0 | Dead neurons — permanent silence |

---

### Solutions

| Solution | How it Prevents Saturation |
|----------|--------------------------|
| **Leaky ReLU** $f(x) = \max(\alpha x, x)$ where $\alpha \approx 0.01$ | Allows a small negative slope, so neurons receiving negative inputs still pass a small gradient and never "die" |
| **ELU (Exponential Linear Unit)** | Smooth negative region that asymptotes to a small negative value; eliminates dead neurons while maintaining mean activations close to zero |
| **Proper Weight Initialisation** (Xavier for Sigmoid/Tanh, He for ReLU) | Scales initial weights so that pre-activation values remain in the non-saturating central region of the activation function |
| **Batch Normalisation** | Re-centres and rescales layer inputs to have zero mean and unit variance, keeping them in the non-saturating region of the activation function throughout training |

---

## Q16. [Originally Q10] Discuss vanishing and exploding gradient problems in deep neural networks (5 Marks)

**Answer:**

### Background: Gradients Flow Through Many Layers
Training a deep neural network requires computing gradients at every layer using backpropagation. The gradient at an early layer is computed by **multiplying together the local gradients of all layers between it and the output**. In a network with $n$ layers:

$$\frac{\partial L}{\partial W^{(1)}} = \frac{\partial L}{\partial a^{(n)}} \cdot \prod_{l=2}^{n} \frac{\partial a^{(l)}}{\partial a^{(l-1)}}$$

**What this means:** The gradient for the very first layer is the product of many small numbers (the local gradients of each layer). If each of these numbers is less than 1, multiplying many of them together causes the product to approach zero. If each is greater than 1, the product grows exponentially large. This is where both problems originate.

---

### 1. Vanishing Gradient Problem

**What happens:** The gradient signal becomes **exponentially smaller** as it travels from the output layer back toward the input layers. By the time it reaches the first few layers, the gradient is so close to zero that the weights in those layers barely change during training. These early layers effectively stop learning.

**Why it happens with Sigmoid and Tanh:** The maximum derivative of the sigmoid function is 0.25 (at $x = 0$). For large positive or negative inputs, the derivative drops to nearly zero. Multiplying 0.25 by itself across 10 layers gives $0.25^{10} \approx 0.000001$ — essentially zero.

```
Layer:      L      L-1      L-2      L-3      L-4
Gradient: 0.1  →  0.025 → 0.006 → 0.001 → 0.0003 → ≈ 0
         (each layer multiplies by sigmoid derivative ≤ 0.25)
```

**Consequence:** The network cannot learn long-range dependencies. In a language model, early layers that should learn grammar structure get no useful gradient signal.

**Solutions and why they work:**
- **ReLU activation:** For positive inputs, the ReLU derivative is exactly 1 — multiplying by 1 leaves the gradient unchanged, so it doesn't shrink.
- **Batch Normalization:** Keeps layer inputs in a range where activation derivatives are not near zero.
- **Skip connections (ResNets):** Create "shortcut" paths that let gradients bypass layers entirely, arriving at early layers without being multiplied down.
- **Xavier/He weight initialization:** Initializes weights so that the variance of activations is preserved across layers, keeping derivatives in a healthy range from the start.

---

### 2. Exploding Gradient Problem

**What happens:** The gradient signal becomes **exponentially larger** as it propagates back, resulting in enormous weight updates. The weights change so drastically each step that the model becomes unstable — loss values jump around wildly and may become NaN (Not a Number).

**Why it happens:** If the weights are initialized large, the local gradients at each layer can be greater than 1. Multiplying numbers greater than 1 together across many layers causes exponential growth. This is especially common in **Recurrent Neural Networks (RNNs)** processing long sequences, where the same weight matrix is multiplied by itself many times.

**Solutions and why they work:**
- **Gradient Clipping:** The most common fix. Before applying the update, we check if the gradient's magnitude exceeds a threshold $\tau$. If it does, we scale it down proportionally:

$$g \leftarrow g \cdot \frac{\tau}{\|g\|} \quad \text{if } \|g\| > \tau$$

  This caps the maximum step size without changing the direction of the update.
- **Careful weight initialization:** Starting with smaller weight values reduces the chance of large local gradients.
- **Batch Normalization:** Normalizing intermediate outputs prevents any single layer's activations from growing excessively large.

---

### Summary Table

| Problem | Root Cause | Symptom | Primary Solutions |
|---------|-----------|---------|-----------------|
| **Vanishing Gradient** | Product of many values $< 1$ | Early layers don't train; network seems stuck | ReLU, Batch Norm, skip connections, better initialization |
| **Exploding Gradient** | Product of many values $> 1$ | Unstable training, NaN loss, large oscillations | Gradient clipping, initialization, Batch Norm |

---

# ━━━ Group F: Loss Functions ━━━

## Q17. [Originally Q11] Describe Binary Cross-Entropy and Categorical Cross-Entropy loss functions (5 Marks)

**Answer:**

### What is a Loss Function?
A **loss function** (also called a cost function or objective function) quantifies how wrong a model's predictions are compared to the true labels. It produces a single number that the optimizer tries to minimise. Cross-entropy loss functions are based on **information theory** — specifically, they measure how surprised we would be by the true label given the model's predicted probabilities. A model that is very confident and correct has low loss; a model that is confident but wrong is severely penalised.

**Key intuition:** The logarithm in cross-entropy is what makes it penalise confident wrong predictions so heavily. $\log(0.01) \approx -4.6$, but $\log(0.99) \approx -0.01$. Being confidently wrong is penalised nearly 460× more than being confidently correct.

---

### 1. Binary Cross-Entropy (BCE)

Used when there are exactly **two classes** (0 or 1). The output neuron uses a **Sigmoid** activation to produce a probability between 0 and 1.

$$L_{BCE} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$

**What this means — symbol by symbol:**

| Symbol | Meaning |
|--------|---------|
| $N$ | Total number of training samples being averaged over |
| $y_i$ | The true label for sample $i$ — either 0 (negative class) or 1 (positive class) |
| $\hat{y}_i$ | The model's predicted probability that sample $i$ belongs to class 1 (output of sigmoid) |
| $\log(\hat{y}_i)$ | The term that applies when $y_i = 1$ — penalises the model for low predicted probability when the true label is 1 |
| $\log(1 - \hat{y}_i)$ | The term that applies when $y_i = 0$ — penalises the model for high predicted probability when the true label is 0 |

**How the two terms work together:** The formula cleverly switches between two terms depending on the true label. When $y_i = 1$, the second term vanishes ($1 - 1 = 0$) and only $\log(\hat{y}_i)$ matters. When $y_i = 0$, the first term vanishes and only $\log(1 - \hat{y}_i)$ matters. We never compute both terms for the same sample.

**Worked example (spam detection):**
- True label: spam ($y = 1$), Prediction: $\hat{y} = 0.95$ → Loss $= -\log(0.95) \approx 0.05$ — correctly confident, low penalty.
- True label: spam ($y = 1$), Prediction: $\hat{y} = 0.05$ → Loss $= -\log(0.05) \approx 3.0$ — confidently wrong, high penalty.

---

### 2. Categorical Cross-Entropy (CCE)

Used when there are **more than two classes**. The output layer uses **Softmax** activation, which converts raw scores into a probability distribution over all classes (all probabilities sum to 1). Labels are typically **one-hot encoded** (e.g., class 3 out of 5 → `[0, 0, 0, 1, 0]`).

$$L_{CCE} = -\frac{1}{N} \sum_{i=1}^{N} \sum_{c=1}^{C} y_{ic} \log(\hat{y}_{ic})$$

**What this means:**

| Symbol | Meaning |
|--------|---------|
| $C$ | Total number of classes (e.g., 10 for digit recognition) |
| $y_{ic}$ | 1 if sample $i$ truly belongs to class $c$, else 0 (one-hot encoding — only one class is 1 per sample) |
| $\hat{y}_{ic}$ | The predicted probability that sample $i$ belongs to class $c$ (output of Softmax) |

**Simplification:** Because $y_{ic}$ is one-hot, for any given sample, only the term corresponding to the true class is non-zero. The loss reduces to $-\log(\hat{y}_{i, \text{true class}})$ — penalising the model for assigning low probability to the correct class.

**Example:** In handwritten digit recognition (classes 0–9), if the true digit is 3 and the model gives 3 only a 5% probability while giving 7 a 70% probability, the loss will be very high: $-\log(0.05) \approx 3.0$.

---

### Comparison

| Aspect | Binary Cross-Entropy | Categorical Cross-Entropy |
|--------|---------------------|--------------------------|
| Number of classes | 2 (binary) | $C > 2$ (multi-class) |
| Output activation | Sigmoid (produces one probability) | Softmax (produces C probabilities summing to 1) |
| Label format | Single scalar: 0 or 1 | One-hot vector of length $C$ |
| Example use case | Spam vs not spam, disease vs healthy | Digit recognition, object classification |

---

# ━━━ Group G: Regularization ━━━

## Q18. [Originally Q7] Discuss Dropout and Early Stopping as regularization techniques (5 Marks)

**Answer:**

### What is Regularization?
**Regularization** refers to any technique that prevents a model from **overfitting** — the problem where a model learns the training data so well (including its noise and random quirks) that it fails to generalise to new, unseen data. An overfitted model has high training accuracy but poor test accuracy.

---

### 1. Dropout

**Dropout** is a regularization technique where during each training step, a randomly selected fraction of neurons are **temporarily "switched off"** (set to zero). These neurons do not participate in the forward pass or the backward pass for that iteration.

**Why does randomly switching off neurons help?**

Without Dropout, neurons in the network can become **co-dependent** — a phenomenon called "co-adaptation." For example, neuron A might learn to always correct the mistakes of neuron B. If neuron A is always available, neuron B never needs to become individually useful. This makes the network fragile — if A were missing at test time, B would fail.

Dropout **breaks this co-dependency** by forcing every neuron to learn to be useful on its own, without relying on any specific other neuron being present. This has a second powerful effect: since we are training on a different random subset of neurons at each step, it is equivalent to training **many different "sub-networks"** simultaneously. The final model behaves like an **ensemble** of these sub-networks, which is known to be more robust than any single model.

**How it works in practice:**
- During training, each neuron is kept active with probability $p$ (e.g., $p = 0.5$ for hidden layers) and deactivated with probability $1 - p$.
- During inference (testing), all neurons are active, but their outputs are scaled by the retention probability $p$ to account for the fact that more neurons are active than during training.
- Typical values: $p = 0.5$ for hidden layers, $p = 0.8$ for input layers (we don't want to lose too much raw input data).

---

### 2. Early Stopping

**Early Stopping** is the practice of **halting the training process at the right moment** — before the model starts overfitting — by monitoring performance on a validation set.

During training, the training loss consistently decreases as the model fits the data more and more closely. Initially, the validation loss (on data the model has never seen) also decreases — the model is genuinely learning useful patterns. However, at some point, the training loss continues to decrease while the validation loss **starts to increase**. This is the signature of overfitting: the model is now memorising training-specific noise rather than learning generalisable patterns.

```
Loss
  │  Training Loss ↘___________
  │                             \___
  │  Validation Loss ↘___    ↗ (starts rising — overfitting begins)
  │                       ★ ← STOP HERE (best model)
  │_________________________________
                      Epochs →
```

**How it works:**
1. Split data into training, validation, and test sets.
2. After each epoch, evaluate the model on the validation set.
3. Keep track of the **best validation loss** seen so far and save the corresponding model weights.
4. If the validation loss has not improved for $k$ consecutive epochs (called the **patience** parameter), stop training.
5. Restore the saved weights from the best epoch as the final model.

The patience parameter prevents stopping too early due to small fluctuations in validation loss — you wait to see if the model might recover before deciding to stop.

---

### Comparison

| Aspect | Dropout | Early Stopping |
|--------|---------|----------------|
| **How it prevents overfitting** | Forces neurons to learn independently; ensemble effect | Stops training before memorisation sets in |
| **When applied** | During every training step | Monitored after each epoch |
| **Key hyperparameter** | Dropout rate $p$ | Patience $k$ (epochs to wait) |
| **Computational cost** | Slight overhead per step | No extra computation — just monitoring |
| **Additional effect** | Acts as implicit ensemble | Also saves training time |

---

## Q19. [Originally Q15] Explain any two regularization techniques used in neural networks (5 Marks)

**Answer:**

### What is Regularization and Why is it Needed?
When a neural network is trained, it minimises the loss on the training data. If the network is large and the training dataset is relatively small, the network can **overfit** — essentially memorising the training examples rather than learning generalisable patterns. It achieves near-zero training loss but performs poorly on new data.

**Regularization** techniques add a constraint or penalty that discourages the model from becoming overly complex, pushing it toward **simpler, more generalisable solutions**. The underlying principle is **Occam's Razor**: among models that explain the training data equally well, prefer the simpler one.

---

### 1. L2 Regularization (Ridge Regression / Weight Decay)

**Core idea:** Add a penalty equal to the sum of the squares of all weights to the loss function. This discourages any single weight from becoming very large.

$$L_{total} = L_{data} + \frac{\lambda}{2} \sum_j w_j^2$$

**What this means:**

| Symbol | Meaning |
|--------|---------|
| $L_{data}$ | The original loss (cross-entropy, MSE, etc.) — how wrong the predictions are |
| $\lambda$ | The regularization strength — a hyperparameter. Larger $\lambda$ = stronger regularization. Typical values: $10^{-4}$ to $10^{-2}$ |
| $\sum_j w_j^2$ | The sum of squares of all weights in the network — the regularization penalty |
| $\frac{1}{2}$ | A scaling factor added for convenience (makes the derivative cleaner) |

**How it works intuitively:** The optimizer now has two objectives: minimise the data loss AND minimise the size of the weights. These two objectives compete — the model cannot make the data loss zero by making weights arbitrarily large, because that would increase the regularization penalty. The result is that weights are pushed toward **small but non-zero values**. A model with many small weights is smoother and generalises better than one with a few enormous weights.

This is also called **weight decay** because at each update step, every weight is multiplied by a factor slightly less than 1 (shrunk or "decayed") before the gradient update is applied.

---

### 2. L1 Regularization (Lasso)

**Core idea:** Add a penalty equal to the sum of the **absolute values** of all weights.

$$L_{total} = L_{data} + \lambda \sum_j |w_j|$$

**What this means:**

| Symbol | Meaning |
|--------|---------|
| $\lambda \sum_j |w_j|$ | The L1 penalty — sum of absolute values of weights |

**How it differs from L2:** The absolute value function has a constant slope of $+1$ or $-1$ (it does not decrease as $w$ gets close to zero). This means the penalty always pushes weights toward zero by the same fixed amount each step, regardless of how small the weight already is. Consequently, L1 regularization drives many weights to become **exactly zero**, effectively removing those connections from the network entirely.

**Sparsity:** A model regularised with L1 has many zero weights — a property called **sparsity**. This is equivalent to automatic **feature selection**: the model identifies which inputs are irrelevant and ignores them by setting their weights to exactly zero.

---

### Comparison

| Aspect | L2 Regularization | L1 Regularization |
|--------|------------------|------------------|
| **Penalty term** | $\lambda \sum w_j^2$ | $\lambda \sum |w_j|$ |
| **Effect on weights** | Shrinks all weights toward small non-zero values | Drives many weights to exactly zero |
| **Result** | Dense model — all features contribute a little | Sparse model — only key features contribute |
| **Analogy** | Student penalised for any extreme opinion | Student forced to say "I don't know" about uncertain topics |
| **Best for** | When all features may be relevant (general use) | When many features are irrelevant (feature selection) |

---

# ━━━ Group H: Normalization ━━━

## Q20. [Originally Q16] Explain the role of normalization techniques in improving deep network training (5 Marks)

**Answer:**

### The Problem: Internal Covariate Shift
When a deep neural network is trained, the parameters of each layer change at every training step. This means that not only the input data to the entire network changes (which we can handle by normalising the raw data), but the **distribution of inputs flowing into each hidden layer also changes continuously** throughout training.

This phenomenon is called **Internal Covariate Shift**: the statistical distribution (mean, variance) of a layer's inputs shifts as the layers before it are updated. This is problematic because each layer has to constantly re-adapt to a changing input distribution, slowing down training significantly and requiring very careful, conservative learning rates.

**Analogy:** Imagine trying to learn to catch a ball when someone keeps randomly changing the rules of gravity mid-catch. You would have to constantly re-learn your catching strategy instead of refining it.

---

### What Normalization Does
Normalization techniques standardise the input to each layer — forcing the distribution to have a consistent mean and variance. This provides each layer with a **stable, predictable input**, allowing it to focus on learning its own transformation rather than adapting to distributional changes from previous layers.

---

### 1. Batch Normalization
Normalises the inputs to each layer by computing the **mean and variance across the current mini-batch**. It then standardises the inputs to have zero mean and unit variance, followed by learnable scale ($\gamma$) and shift ($\beta$) parameters that allow the network to undo the normalization if beneficial.

**When to use:** Large mini-batches (32+). Very effective for CNNs in image classification. Less suitable for small batches or RNNs, because with fewer samples, the batch statistics become unreliable estimates of the true data statistics.

---

### 2. Layer Normalization
Normalises across the **feature dimension of a single sample**, independently of the batch size. Each sample is normalised using its own mean and variance. This means Layer Normalization works identically whether the batch size is 1 or 1000 — it does not depend on other samples in the batch.

**When to use:** Recurrent Neural Networks (RNNs) and Transformer architectures, where sequences have variable lengths and batch sizes are often small. Layer Normalization is the standard in BERT, GPT, and other large language models.

---

### 3. Instance Normalization
Normalises each sample independently, and each channel independently — computing statistics over only the **spatial dimensions** of a single feature map in a single image.

**When to use:** Image style transfer and image generation tasks. The intuition is that by normalising per-instance per-channel, we remove the colour and contrast information that is specific to the image content, allowing the network to focus on transferring artistic style.

---

### Benefits of Normalization in Deep Network Training

| Benefit | Why it Happens |
|---------|---------------|
| **Faster convergence** | Stable input distributions allow higher learning rates without divergence |
| **Less sensitive to weight initialisation** | Even poorly initialised weights are normalised before causing problems |
| **Smoother loss landscape** | Gradients are more consistent, reducing oscillation during training |
| **Mild regularization** | Batch statistics introduce a small amount of noise, which has a regularizing effect similar to Dropout |
| **Enables very deep networks** | Without normalization, training networks with 50+ layers is impractical due to vanishing/exploding gradients |

---

## Q21. [Originally Q24] Describe Batch Normalization and its advantages in deep learning training (5 Marks)

**Answer:**

### Definition and Motivation
**Batch Normalization (BN)** is a technique introduced by Ioffe and Szegedy (2015) to stabilise and accelerate the training of deep neural networks. It addresses the **Internal Covariate Shift** problem — the fact that as network weights are updated during training, the statistical distribution (mean and variance) of the inputs to each layer continuously changes. Each layer must constantly adapt to a shifting input distribution, which slows down learning.

The solution: at the end of each layer, before (or after) the activation function, **re-normalise the activations** so they always have a consistent mean and variance, regardless of how the weights of previous layers have changed.

---

### Mathematical Formulation (4 Steps)

Given a mini-batch of activations $x_1, x_2, ..., x_B$ (one value per sample for a given neuron):

**Step 1 — Compute batch mean:**

$$\mu_B = \frac{1}{B} \sum_{i=1}^{B} x_i$$

**What this means:** Calculate the arithmetic average of all $B$ values in the current mini-batch. This represents the "centre" of the current distribution.

---

**Step 2 — Compute batch variance:**

$$\sigma_B^2 = \frac{1}{B} \sum_{i=1}^{B} (x_i - \mu_B)^2$$

**What this means:** Calculate the average squared deviation from the mean. This measures how "spread out" the distribution is. A large variance means activations are very spread; small variance means they are tightly clustered.

---

**Step 3 — Normalise:**

$$\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \varepsilon}}$$

**What this means:** Subtract the batch mean (to centre the distribution around zero) and divide by the standard deviation (to scale the spread to approximately 1). After this step, the activations have approximately zero mean and unit variance.

| Symbol | Meaning |
|--------|---------|
| $\hat{x}_i$ | The normalised activation for sample $i$ |
| $\mu_B$ | Batch mean — subtracted to centre the distribution |
| $\sigma_B^2$ | Batch variance |
| $\varepsilon$ | A tiny constant (e.g., $10^{-5}$) added inside the square root to prevent division by zero when variance is very small |

---

**Step 4 — Scale and Shift (learnable parameters):**

$$y_i = \gamma \hat{x}_i + \beta$$

**What this means:** After normalisation, we apply two **learnable parameters** $\gamma$ (scale) and $\beta$ (shift). These are learned during training via backpropagation, just like weights. They allow the network to **undo the normalisation** if it turns out that the best representation for a particular layer is not zero-mean and unit-variance. Without $\gamma$ and $\beta$, the network would be forced to always have zero-mean activations, which is an unnecessary constraint.

---

### Training vs Inference Behaviour

| Phase | How mean and variance are computed |
|-------|-----------------------------------|
| **Training** | Computed fresh from each mini-batch — statistics are noisy, which provides regularization |
| **Inference** | Uses **running averages** of mean and variance accumulated during training. These are fixed (not updated during inference), ensuring deterministic, consistent predictions |

---

### Advantages of Batch Normalization

| Advantage | Detailed Explanation |
|-----------|---------------------|
| **Faster training** | Stable, normalised activations allow the use of much higher learning rates. Without BN, high learning rates cause unstable gradient updates. With BN, training converges in fewer epochs |
| **Reduces sensitivity to initialisation** | Even with poor weight initialisation, BN immediately re-centres and re-scales the activations, preventing the bad initialisation from causing vanishing/exploding gradients |
| **Acts as a regularizer** | Because batch statistics vary slightly from batch to batch (due to random sampling), each activation is perturbed slightly during training. This noise has a regularizing effect similar to Dropout, often reducing the need for Dropout |
| **Mitigates vanishing/exploding gradients** | By keeping activations in a well-scaled range, BN prevents activations from entering the saturated regions of activation functions (like Sigmoid's tails), ensuring healthy gradient flow |
| **Enables training of very deep networks** | Without BN, training networks with 50+ layers is practically infeasible. ResNets, which enabled training of 100–1000 layer networks, use BN extensively |

---

### Where BN is Placed in the Network

BN is typically inserted **after the linear transformation and before the activation function**:

$$\text{Input} \rightarrow \text{Dense/Conv layer} \rightarrow \text{Batch Norm} \rightarrow \text{Activation (ReLU)} \rightarrow \text{Next layer}$$

Some modern architectures place it after the activation. Empirically, pre-activation BN (before ReLU) tends to work slightly better for very deep residual networks.

---

## Q22. [Originally Q23] Compare Batch Normalization, Group Normalization, and Instance Normalization (5 Marks)

**Answer:**

### The Core Difference
All three techniques normalise activations in a neural network by subtracting the mean and dividing by the standard deviation. The key distinction is: **which set of values do we compute the mean and variance over?**

For a 4D feature map with shape $N \times C \times H \times W$ (where $N$ is batch size, $C$ is number of channels, $H$ and $W$ are spatial height and width):

```
N (batch)
▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼
[  Sample 1  ][  Sample 2  ][  Sample 3  ] ... (C channels × H × W each)
 ─────────── BN: averages ACROSS the batch (all N) for each channel
 ─────────── GN: averages within each GROUP of channels, per sample
 ─────────── IN: averages within each H×W spatial map, per channel, per sample
```

---

### 1. Batch Normalization (BN)
BN computes statistics **across the entire mini-batch**. For each channel, it computes the mean and variance of that channel's values across all $N$ samples and all spatial positions $H \times W$.

**Strength:** Very effective for large batches (e.g., 32+). Provides strong regularization because batch statistics act as noise. Widely used in CNNs for image classification (VGG, ResNet, etc.).

**Weakness:** The quality of the normalisation depends heavily on having a reasonably large batch size. With small batches (e.g., 2–4), the batch statistics are unreliable estimates of the population statistics, and training becomes unstable. This makes BN unsuitable for memory-intensive tasks like high-resolution object detection, where only 1–2 images fit per GPU.

---

### 2. Group Normalization (GN)
GN divides the channels into **fixed groups** and computes statistics within each group **for each sample independently**. For example, with 32 channels and 8 groups, each group contains 4 channels; normalisation is computed over those 4 channels × $H$ × $W$ for each sample separately.

**Strength:** Completely **independent of batch size** — works just as well with batch size 1 as with batch size 128. This makes it ideal for high-resolution tasks like object detection and instance segmentation (Mask R-CNN), where GPU memory constraints force very small batch sizes.

**Weakness:** Requires choosing the number of groups as a hyperparameter. Not always superior to BN for large-batch classification tasks.

---

### 3. Instance Normalization (IN)
IN computes statistics over the **spatial dimensions (H, W) for each sample and each channel individually**. Every single channel of every single sample gets its own mean and variance.

**Strength:** By normalising each channel of each image independently, IN removes the contrast and colour information that is specific to the content of each image, leaving only structural (style) information. This makes it excellent for **neural style transfer** — transforming the artistic style of one image while preserving the content of another.

**Weakness:** Does not capture cross-sample or cross-channel statistics. Not useful for tasks where global statistics across the batch carry meaningful information.

---

### Comparison Table

| Aspect | Batch Normalization | Group Normalization | Instance Normalization |
|--------|-------------------|--------------------|-----------------------|
| **Normalises over** | All $N$ samples, all $H \times W$, per channel | $H \times W$ within each channel group, per sample | $H \times W$, per channel, per sample |
| **Batch size dependency** | Yes — degrades with small batches | No — batch size independent | No — batch size independent |
| **Best for** | Large-batch image classification (CNNs) | Object detection, segmentation (small batch tasks) | Style transfer, image generation |
| **Requires grouping** | No | Yes — group size is a hyperparameter | No |
| **Introduced for** | Reducing covariate shift in general DL | Replacing BN in small-batch settings | Neural artistic style transfer |

---

# ━━━ Group I: TensorFlow ━━━

## Q23. [Originally Q5] Explain the TensorFlow data structures and types of tensors with examples (5 Marks)

**Answer:**

### What is TensorFlow?
**TensorFlow** is an open-source deep learning framework developed by Google. Every computation in TensorFlow — from storing data to performing matrix multiplications to updating weights — is built around a single fundamental data structure: the **tensor**.

---

### What is a Tensor?
A **tensor** is a generalisation of numbers, vectors, and matrices to any number of dimensions. The "rank" of a tensor describes how many dimensions it has. You can think of tensors as containers that hold numbers arranged in a particular shape.

---

### Types of Tensors by Rank

| Rank | Name | Shape | Real-World Example |
|------|------|-------|-------------------|
| **0** | **Scalar** | No dimensions | A single number — e.g., the loss value `0.35`, a temperature reading, or a single accuracy score |
| **1** | **Vector** | `(n,)` — a list | A row of features — e.g., `[age, height, weight]` for one patient; or one word embedding |
| **2** | **Matrix** | `(m, n)` — rows × columns | A table of data — e.g., a weight matrix connecting 128 neurons to 64 neurons; a batch of 32 samples each with 10 features |
| **3+** | **n-D Tensor** | `(batch, h, w, c)` | An image batch — e.g., 32 colour images of size 224×224 with 3 channels (RGB) stored as a 4D tensor |

**Key insight:** The rank tells you how many indices you need to point to a single number inside the tensor. A scalar needs zero indices; a vector needs one; a matrix needs two; an image batch needs four.

---

### TensorFlow Tensor Types (by mutability)

**1. tf.constant — Immutable Tensor**
A `tf.constant` is a tensor whose value is **fixed** once created and can never be changed. It is used for data that should not be modified during training, such as input features, labels, or pre-defined lookup tables. Example: storing the raw training images as a constant ensures they are not accidentally modified.

**2. tf.Variable — Mutable Tensor**
A `tf.Variable` is a tensor whose value **can be updated** during training. It is the primary way TensorFlow stores **trainable parameters** — weights and biases. After each training step, gradient descent updates the Variable's value. The Variable "remembers" its value across multiple operations.

**3. tf.SparseTensor — Sparse Tensor**
A `tf.SparseTensor` is designed for tensors where **most values are zero**. Instead of storing every zero explicitly (which wastes memory), it stores only the non-zero values along with their positions (indices). This is very useful in NLP — for example, a one-hot encoded vocabulary of 50,000 words is mostly zeros.

**4. tf.RaggedTensor — Variable-Length Tensor**
A `tf.RaggedTensor` handles data where **rows have different lengths**. For example, sentences in a text dataset are of different lengths: one sentence has 8 words, another has 20. A regular tensor would need padding to make all rows equal length. A RaggedTensor stores them as-is, saving memory and preserving the original structure.

---

### Key Properties of Every Tensor

- **dtype** (Data Type): Specifies what kind of numbers the tensor holds — floating point (`float32`), integer (`int32`), boolean (`bool`), etc. Choosing the right dtype affects both memory usage and numerical precision.
- **shape**: Describes the size of each dimension — e.g., `(32, 224, 224, 3)` means 32 images, each 224×224 pixels, with 3 colour channels.
- **rank**: The number of dimensions — `len(shape)`.

---

## Q24. [Originally Q20] Explain TensorFlow workflow and its key components (5 Marks)

**Answer:**

### What is TensorFlow?
**TensorFlow** is an open-source end-to-end machine learning framework developed by Google Brain. It is designed to make it easy to build, train, evaluate, and deploy deep learning models at scale — from research experiments to production applications serving millions of users.

The name reflects its core architecture: **tensors** (multi-dimensional arrays) **flow** through a computational graph of mathematical operations.

---

### TensorFlow Workflow

```
1. Data Preparation
       ↓
2. Model Definition
       ↓
3. Model Compilation (optimizer + loss + metrics)
       ↓
4. Model Training
       ↓
5. Evaluation
       ↓
6. Prediction / Deployment
```

---

### Step-by-Step Explanation

**Step 1 — Data Preparation:**
Raw data (images, text, tabular records) must be loaded, cleaned, and formatted into tensors. TensorFlow provides the `tf.data` API to build efficient data pipelines: loading data from disk, shuffling, batching, prefetching, and applying transformations (resizing images, normalising pixel values, tokenising text). A well-built data pipeline ensures the GPU is never idle waiting for data.

**Step 2 — Model Definition:**
The model architecture is defined as a sequence or graph of layers. TensorFlow's high-level Keras API makes this intuitive: you specify the number of layers, the type of each layer (Dense, Convolutional, Dropout, Batch Normalisation, etc.), the number of neurons in each layer, and the activation function. The model definition does not yet involve any data — it is a blueprint.

**Step 3 — Model Compilation:**
Before training, the model must be configured with three things:
- **Optimizer** (e.g., Adam, SGD) — the algorithm that will update the weights.
- **Loss function** (e.g., cross-entropy, MSE) — what we are trying to minimise.
- **Metrics** (e.g., accuracy) — what we track to monitor training progress.

**Step 4 — Model Training:**
The `fit` operation runs the training loop: for each epoch, it iterates through all mini-batches, performs a forward pass, computes the loss, runs backpropagation, and updates weights via the optimizer. Training progress (loss, accuracy) is printed after each epoch, along with validation metrics if a validation set is provided.

**Step 5 — Evaluation:**
After training, the model is evaluated on the held-out test set to measure true generalisation performance. This gives an unbiased estimate of how well the model will perform on completely new data.

**Step 6 — Prediction and Deployment:**
The trained model is used to make predictions on new data. TensorFlow provides tools to save the model in the `SavedModel` format, which can then be deployed to servers (TensorFlow Serving), mobile devices (TensorFlow Lite), or browsers (TensorFlow.js).

---

### Key Components of TensorFlow

| Component | Role |
|-----------|------|
| **Tensors** | The fundamental data structure — multi-dimensional arrays carrying all data and parameters |
| **Operations (Ops)** | Mathematical functions applied to tensors — addition, matrix multiplication, convolution, etc. |
| **Computational Graph** | A directed acyclic graph (DAG) representing the sequence of operations. TF2 builds this implicitly |
| **Eager Execution** | TF2's default mode — operations execute immediately, like standard Python code, making debugging easy |
| **Keras API** | TensorFlow's high-level API for building and training models with minimal boilerplate code |
| **tf.data API** | High-performance data input pipelines — loading, preprocessing, batching, and prefetching data |
| **tf.GradientTape** | Records operations during the forward pass to enable automatic differentiation during backpropagation |
| **SavedModel** | A portable format for saving trained models for deployment across different platforms and languages |

---
