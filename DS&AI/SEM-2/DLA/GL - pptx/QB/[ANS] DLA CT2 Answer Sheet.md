# DLA CT-2 Answer Sheet
**Each question carries 20 marks**

---

## Q1. CNN for Automated Pneumonia Detection from Chest X-Rays *(20 Marks)*

> A hospital is developing an automated system to detect pneumonia from chest X-ray images. The system must accurately identify infected regions and assist doctors in diagnosis. Explain how a Convolutional Neural Network (CNN) can be designed for this task with various architecture components, feature extraction process, training strategy and evaluation metrics. Explain the challenges in medical image classification and how CNN overcomes them.

---

### 1. Introduction

A **Convolutional Neural Network (CNN)** is a class of deep neural networks most commonly applied to analyzing visual data such as images and videos. CNNs are designed to automatically and adaptively learn spatial hierarchies of features from input images. For pneumonia detection, a CNN can learn to distinguish healthy lung tissue from infected areas directly from raw pixel values — without manual feature engineering.

CNNs are particularly effective for this task because:
- They detect **local patterns** (edges, textures, shapes) pixel by pixel and build up to more complex features as you go deeper.
- They use **weight sharing** — the same filter slides across the entire image — making the model invariant to where the infection appears in the X-ray.
- They use **local/sparse connectivity** — each neuron connects only to a small region of the input (the receptive field), reducing parameters and preventing overfitting.

---

### 2. CNN Architecture Components for Pneumonia Detection

The CNN is designed as a sequence of the following layers:

#### a) Input Layer
The raw X-ray image is fed into the network. For example, a grayscale chest X-ray resized to **224 × 224 pixels** is represented as a 2D grid of pixel values.

#### b) Convolutional Layer
This is the core layer. A set of learnable **filters (kernels)** — typically **3×3** or **5×5** — are applied to the input image, producing **feature maps** that highlight local patterns such as edges, textures, and opacities. Each filter slides across the image, performing element-wise multiplication followed by a sum. For pneumonia detection, early filters learn to detect edges of lung boundaries; deeper filters detect complex opacity patterns characteristic of infection.

**Key parameters in convolution:**
- **Filter size**: 3×3 (computationally efficient, captures local detail)
- **Number of filters**: Increases with depth (e.g., 32 → 64 → 128)
- **Stride**: How many pixels the filter shifts at each step (usually 1)
- **Padding**: Adds zero-pixels around the border to control output size

#### c) Activation Function — ReLU
After each convolution, a **Rectified Linear Unit (ReLU)** is applied:

$$\text{ReLU}(x) = \max(0, x)$$

This introduces **non-linearity**, allowing the network to learn complex patterns beyond simple linear combinations. Without non-linearity, the entire network collapses to a single linear transformation regardless of depth.

#### d) Pooling Layer
Pooling reduces spatial dimensions, making the network computationally efficient and less sensitive to small translations. **Max Pooling** (takes the maximum value in each region) is commonly used:
- **Max Pooling 2×2 with stride 2** halves the height and width of the feature map.
- Retains the most prominent features while discarding less relevant information.
- Helps the model recognize pneumonia whether it appears in the upper or lower lung region.

#### e) Flattening Layer
After several conv + pool blocks, the 2D feature maps are **flattened** into a 1D vector. For example, a 7×7×128 feature map becomes a 6272-dimensional vector. This converts spatial features into a format that the fully connected layers can process.

#### f) Fully Connected Layer (Dense Layer)
The flattened vector is passed through one or more **Dense layers**, where every neuron connects to every neuron in the previous layer. These layers learn the high-level combination of features required for classification (e.g., "these patterns together suggest pneumonia").

#### g) Output Layer
The final layer has **2 neurons** (Pneumonia / Normal) with a **Softmax** activation that outputs probabilities for each class:

$$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$$

The class with the highest probability is the model's prediction.

---

### 3. Feature Extraction Process

CNNs learn features in a **hierarchical manner**, which is especially powerful for medical imaging:

| Layer Depth | Features Learned | Medical Relevance |
|---|---|---|
| **Early layers** | Edges, lines, textures | Lung boundary edges, rib outlines |
| **Middle layers** | Shapes, blobs | Lobar patterns, opacity clusters |
| **Deep layers** | High-level patterns | Consolidation patterns indicating pneumonia |

This mirrors the biological visual cortex, where simple cells detect edges and complex cells combine them to recognize objects — mapped directly to conv layers (detect features) and pooling layers (position invariance).

---

### 4. Training Strategy

Training a CNN follows a structured pipeline:

1. **Dataset Collection & Preparation** — Gather labeled chest X-rays (Pneumonia / Normal). Split into train (70%), validation (15%), and test (15%) sets.
2. **Data Preprocessing** — Resize to 224×224, normalize pixel values to [0, 1].
3. **Data Augmentation** — Apply random flips, rotations, zoom, and brightness adjustments to artificially expand the dataset and prevent overfitting. Medical datasets are often small — augmentation is critical.
4. **Architecture Selection** — Use a pretrained model like **VGG16 or ResNet** (transfer learning) or design a custom CNN. Transfer learning uses weights learned on millions of images, then fine-tunes them on the X-ray dataset.
5. **Model Initialization** — Initialize weights using Xavier or He initialization. Set hyperparameters: learning rate (e.g., 0.001), batch size (32), optimizer (Adam).
6. **Forward Propagation** — Input X-ray passes through conv → ReLU → pool → flatten → dense → softmax.
7. **Loss Calculation** — Compare prediction to the true label using **Binary Cross-Entropy Loss** (for binary classification):
   $$\mathcal{L} = -[y \log(\hat{y}) + (1-y)\log(1-\hat{y})]$$
8. **Backpropagation** — Compute gradients of the loss with respect to each weight using the chain rule. Update weights using Adam optimizer.
9. **Validation** — Evaluate on the validation set after each epoch to detect overfitting. Apply **early stopping** if validation loss stops improving.
10. **Testing** — Evaluate final performance on the unseen test set.

---

### 5. Evaluation Metrics

For medical classification, accuracy alone is insufficient due to class imbalance. The following metrics are used:

| Metric | Formula | Relevance |
|---|---|---|
| **Accuracy** | (TP + TN) / Total | Overall correctness |
| **Sensitivity (Recall)** | TP / (TP + FN) | Critical — missing a pneumonia case is dangerous |
| **Specificity** | TN / (TN + FP) | Avoiding false alarms |
| **Precision** | TP / (TP + FP) | How reliable a positive prediction is |
| **F1 Score** | 2 × (Precision × Recall) / (Precision + Recall) | Balanced metric |
| **AUC-ROC** | Area under ROC curve | Model's ability to distinguish classes |

A high **Sensitivity** is prioritised — a missed pneumonia case (false negative) is far more dangerous than a false alarm.

---

### 6. Challenges in Medical Image Classification and How CNN Overcomes Them

| Challenge | Description | CNN Solution |
|---|---|---|
| **Limited labeled data** | Annotating medical images requires expert radiologists; datasets are small | Data augmentation + Transfer learning from ImageNet pretrained models |
| **Class imbalance** | More normal cases than pneumonia cases | Weighted loss functions, oversampling (SMOTE) |
| **Subtle features** | Pneumonia patterns are subtle and can resemble other conditions | Deep hierarchical feature learning extracts minute texture differences |
| **Positional variability** | Infection can appear anywhere in the lung | Pooling layers provide spatial invariance |
| **High-dimensional input** | Raw X-ray images are large (e.g., 2000×2000 pixels) | Local connectivity and weight sharing massively reduce parameters |
| **Overfitting** | Small dataset causes memorization | Dropout layers, L2 regularization, and augmentation combat overfitting |
| **Interpretability** | Doctors need to understand why the model predicted pneumonia | Grad-CAM visualizes which regions activated the prediction |

**Conclusion:** CNNs are the gold standard for medical image classification because they automatically learn spatial, hierarchical features without manual feature engineering, are robust to positional variance through pooling, and can be enhanced via transfer learning when labeled data is scarce.

---

## Q2. GRU-Based Model for ICU Patient Monitoring *(20 Marks)*

> A hospital is developing a smart monitoring system to track ICU patients using continuous data such as heart rate, blood pressure, and oxygen levels over time. The goal is to predict critical conditions early. Explain how a GRU model can be designed for this task, including its architecture and gating mechanisms. Discuss how it processes time-series data, captures dependencies, and how the model is trained and evaluated. Also explain the challenges in sequential medical data and how GRU helps address them.

---

### 1. Introduction

Patient vitals in an ICU are **sequential time-series data** — the order and timing of readings matter critically. A reading taken now is influenced by readings from the past hour. To predict critical conditions like cardiac arrest, the model must:
- Understand **temporal dependencies** (how past values influence future ones).
- Handle **variable-length sequences** (some patients may have more readings than others).
- Retain only the **most relevant past information** — not all history matters equally.

A **Gated Recurrent Unit (GRU)** is a streamlined variant of LSTM designed exactly for this kind of efficient sequential processing.

---

### 2. What is a GRU?

GRUs are a simplified version of LSTMs — same core idea, fewer parameters, faster to train. They:
- **Merge the cell state and hidden state** into a single hidden state.
- Use only **two gates** (Reset and Update) instead of three (Forget, Input, Output in LSTM).

| Property | LSTM | GRU |
|---|---|---|
| Gates | 3 (Forget, Input, Output) | 2 (Reset, Update) |
| States | Cell state + Hidden state | Single hidden state |
| Parameters | More | Fewer |
| Training speed | Slower | Faster |
| Performance | Slightly better on long sequences | Comparable on most tasks |

---

### 3. GRU Architecture and Gating Mechanisms

At each time step $t$, the GRU receives:
- $X_t$ — the current input (e.g., heart rate, blood pressure, SpO₂ at time $t$)
- $h_{t-1}$ — the previous hidden state (memory of past readings)

#### a) Reset Gate
The **Reset Gate** decides how much of the **past hidden state** to forget when computing the candidate (proposed) new state:

$$r_t = \sigma(W_r X_t + U_r h_{t-1})$$

- $\sigma$ = sigmoid, output in $[0, 1]$
- $r_t \approx 0$: completely ignore the past → start fresh
- $r_t \approx 1$: use all of the past memory

This allows the GRU to drop irrelevant past context (e.g., ignore a temporarily elevated heart rate from physical therapy when predicting cardiac risk).

#### b) Candidate Hidden State (New Memory)
Using the reset gate, a **candidate state** $\tilde{h}_t$ is proposed — what the model *wants* the new memory to be:

$$\tilde{h}_t = \tanh(W_h X_t + U_h (r_t \odot h_{t-1}))$$

- $\odot$ = element-wise multiplication
- When $r_t = 0$, the past state is erased from this calculation
- $\tanh$ squashes output to $[-1, 1]$, keeping values stable

#### c) Update Gate
The **Update Gate** decides how much of the **old hidden state** to keep versus how much of the **new candidate** to use:

$$z_t = \sigma(W_z X_t + U_z h_{t-1})$$

- $z_t \approx 1$: keep old memory (ignore new input)
- $z_t \approx 0$: replace old memory with new candidate

#### d) New Hidden State
The final hidden state combines the old memory and the candidate, controlled by the update gate:

$$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$

This formula is elegant: when $z_t = 0$, $h_t = h_{t-1}$ (nothing changes); when $z_t = 1$, $h_t = \tilde{h}_t$ (completely updated). In practice, each element of $z_t$ takes a different value, allowing the GRU to partially update some dimensions while leaving others unchanged.

---

### 4. How GRU Processes Time-Series ICU Data

**Input Design:**
Each time step $t$ represents one monitoring interval (e.g., every 5 minutes). The input vector $X_t$ contains:
- Heart rate, Blood pressure (systolic, diastolic), SpO₂, Temperature, etc.

**Sequence of operations:**
```
t=0: X₀ (vitals at 00:00) + h₋₁ (zeros) → [GRU] → h₀
t=1: X₁ (vitals at 00:05) + h₀           → [GRU] → h₁
t=2: X₂ (vitals at 00:10) + h₁           → [GRU] → h₂
...
t=T: X_T (latest vitals)  + h_{T-1}       → [GRU] → h_T → Output
```

The final hidden state $h_T$ is a compressed representation of the entire patient history up to time $T$. This is passed to a Dense output layer that predicts the probability of a critical event (e.g., cardiac arrest within the next 30 minutes).

**Capturing dependencies:**
- The **reset gate** helps the GRU forget transient spikes (noise).
- The **update gate** helps the GRU retain long-term trends (e.g., gradually declining SpO₂ over hours).

---

### 5. Model Architecture for ICU Monitoring

```
Input: (batch_size, time_steps, features)
         → GRU Layer (128 units, return_sequences=True)
         → GRU Layer (64 units, return_sequences=False)
         → Dense Layer (32 units, ReLU)
         → Dropout (0.3)
         → Output Dense Layer (1 unit, Sigmoid)
         → Output: probability of critical event
```

A **stacked GRU** (multiple layers) captures more complex temporal patterns. The first GRU returns sequences (one output per time step); the second returns only the final state.

---

### 6. Training Strategy

1. **Data Preprocessing**: Normalize each vital sign to [0, 1] using Min-Max scaling. Create overlapping windows of length $T$ (e.g., 60 time steps = 5 hours of 5-minute readings).
2. **Label creation**: Binary label — 1 if a critical event occurs within the next 30 minutes, 0 otherwise.
3. **Loss function**: **Binary Cross-Entropy** (for binary outcome prediction).
4. **Optimizer**: Adam with learning rate 0.001.
5. **Class imbalance**: Use class weights or oversampling — critical events are rare.
6. **Training loop**: Forward pass → Loss → Backpropagation Through Time (BPTT) → Weight update.
7. **Validation**: Monitor on a held-out patient set after each epoch.

---

### 7. Evaluation Metrics

| Metric | Importance |
|---|---|
| **Sensitivity / Recall** | Must be very high — missing a critical event is life-threatening |
| **Specificity** | Avoid excessive false alarms that cause alert fatigue |
| **AUC-ROC** | Overall discrimination ability |
| **F1 Score** | Balanced metric under class imbalance |

---

### 8. Challenges and How GRU Addresses Them

| Challenge | GRU Solution |
|---|---|
| **Long-term dependencies** (e.g., slow SpO₂ decline over hours) | Update gate preserves relevant long-term patterns without vanishing gradients |
| **Noisy measurements** (transient spikes in vitals) | Reset gate allows the model to ignore or downweight noise |
| **Missing data / irregular intervals** | Preprocessing with imputation; GRU handles variable-length sequences via padding |
| **Vanishing gradient** (standard RNN limitation) | Gating mechanism prevents gradient from vanishing — gradient flow is controlled |
| **Computational efficiency** | GRU uses 2 gates vs. LSTM's 3, requiring fewer parameters — faster training on large patient databases |

---

## Q3. RNN-Based Model for ICU Patient Monitoring *(20 Marks)*

> A hospital is developing a system to monitor ICU patients using continuous data such as heart rate, blood pressure, and oxygen levels recorded over time. The goal is to predict critical conditions like cardiac arrest in advance. Since the data is sequential, an RNN is proposed. Explain how an RNN-based model can be designed for this task. Discuss how the model learns from time-based data, handles long-term dependencies, and how it is trained and evaluated. Also explain the challenges in processing sequential medical data.

---

### 1. Introduction

Patient vital signs form a **sequential time series** — each reading at time $t$ is influenced by all preceding readings. To predict critical conditions, the model must understand how patterns evolve over time. A **Recurrent Neural Network (RNN)** is designed precisely for this: it maintains a **hidden state** that acts as memory, carrying information from previous time steps into the current one.

---

### 2. Why RNN for Sequential Medical Data?

A standard Dense (feedforward) network treats all inputs as an independent, flat vector — it has no concept of which reading came first. An RNN processes data **one time step at a time**, maintaining context:

```
DNN:
All vitals at once → [Dense] → Prediction (ignores temporal order)

RNN:
Vitals at t=0 → [RNN] → h₀
Vitals at t=1 → [RNN] → h₁   (using h₀ as memory)
Vitals at t=2 → [RNN] → h₂   (using h₁ as memory)
...
Vitals at t=T → [RNN] → h_T → [Dense Output] → Prediction
```

The hidden state $h_t$ is the model's "memory" — it encodes everything the model has learned from the sequence so far.

---

### 3. RNN Cell Structure and Mathematics

At each time step $t$, the RNN cell computes:

$$s_t = \tanh(W \cdot S_{t-1} + b_w + U \cdot X_t + b_u)$$

| Symbol | Meaning |
|---|---|
| $X_t$ | Current input vector (heart rate, BP, SpO₂ at time $t$) |
| $S_{t-1}$ | Previous hidden state (memory from past readings) |
| $W$ | Weight matrix for the recurrent (memory) path |
| $U$ | Weight matrix for the input path |
| $b_w, b_u$ | Bias terms |
| $s_t$ | New hidden state — updated memory |
| $\tanh$ | Squashes output to $[-1, 1]$, keeping values stable |

The two-part formula means:
- $W \cdot S_{t-1}$ — how much the **previous memory** contributes
- $U \cdot X_t$ — how much the **current reading** contributes

These are added together and squashed by $\tanh$ to produce the new hidden state.

---

### 4. How the RNN Learns from Time-Based Data — Step by Step

**Initialization:** At $t = 0$, the hidden state is initialized to zeros — no prior knowledge.

**Step $t=0$** — First reading, no memory yet:
```
S_{t-1} = [0, 0, ..., 0]         ← empty memory
X_{t=0} = [72, 120/80, 98%]      ← first vital reading
            ↓
      [ RNN Cell ]
            ↓
S_t = tanh(W·S_{t-1} + U·X_t)   ← updated memory: knows first reading
```

**Step $t=1$** — Second reading, memory carries forward:
```
S_t     = [memory of t=0]         ← looped back
X_{t=1} = [75, 118/80, 97%]      ← second vital reading
            ↓
      [ RNN Cell ]
            ↓
S_{t+1} = tanh(W·S_t + U·X_{t+1})  ← memory: knows t=0 and t=1
```

This continues for every time step. By the final step $T$, the hidden state $h_T$ is a compressed summary of the patient's entire vital history, which is fed to a Dense output layer to predict critical risk.

**Making a prediction:**
```
h_T → Dense (Output Layer) → Sigmoid → P(critical event)
```

---

### 5. Handling Long-Term Dependencies — The Vanishing Gradient Problem

Training an RNN requires **BackPropagation Through Time (BPTT)** — the gradient must travel backwards through every time step. At each step, the gradient is multiplied by $W$ (and the $\tanh$ derivative):

$$\frac{dLoss}{dW} = \frac{dLoss}{dO_T} \cdot \frac{dO_T}{dS_T} \cdot W \cdot W \cdot W \cdots \cdot \frac{dS_0}{dW}$$

**The problem:** If $|W| < 1$, repeated multiplication drives the gradient exponentially toward zero. The model "forgets" what happened early in the sequence — gradients from 4 hours ago vanish before they can update the weights. This is the **Vanishing Gradient Problem**.

**For ICU monitoring, this is serious:** A gradual SpO₂ decline over 3 hours is a critical early warning. If the RNN's gradient vanishes over those 36 time steps (every 5 minutes), the model loses that long-range signal entirely.

**Impact:**
- RNN develops effectively **short-term memory only**
- Cannot reliably capture trends that develop over hours
- Gradients can also explode if $|W| > 1$, making training unstable

This is why LSTM and GRU (described in Q2 and Q4) were developed — they use gating mechanisms that prevent gradient collapse.

---

### 6. Model Architecture for ICU Monitoring

```
Input: (batch_size, time_steps=60, features=5)
         → Embedding/Dense preprocessing
         → RNN Layer (128 units)
         → Dense Layer (64 units, ReLU)
         → Dropout (0.3) — prevents overfitting
         → Output Dense (1 unit, Sigmoid)
         → Output: P(critical event in next 30 minutes)
```

The hidden state size (128) is a **hyperparameter** — it stays fixed throughout the sequence. Only the *values* inside those 128 numbers change at every time step, as the model continuously rewrites its memory to encode the most relevant context.

---

### 7. Training and Evaluation

**Training:**
- **Loss function**: Binary Cross-Entropy (predicting critical / not critical)
- **Optimizer**: Adam (learning rate 0.001)
- **Data splitting**: Train / Validation / Test by patient (not by time step, to avoid data leakage)
- **Preprocessing**: Normalize all vitals to [0, 1]; pad shorter sequences to uniform length
- **Class imbalance**: Use class weights — critical events are rare

**Evaluation Metrics:**

| Metric | Relevance |
|---|---|
| **Sensitivity (Recall)** | Most critical — must not miss cardiac arrest events |
| **Specificity** | Avoid false alarms that overwhelm ICU staff |
| **AUC-ROC** | Overall model discrimination |
| **F1 Score** | Balanced performance under class imbalance |
| **Early Warning Lead Time** | How many minutes in advance the model correctly predicts the event |

---

### 8. Challenges in Sequential Medical Data and RNN Limitations

| Challenge | Impact | Mitigation |
|---|---|---|
| **Vanishing gradient** | Cannot learn long-term trends (e.g., 3-hour SpO₂ decline) | Use LSTM or GRU instead of vanilla RNN |
| **Irregular time intervals** | Readings may not arrive at exact 5-minute intervals | Imputation or time-aware RNN variants |
| **Missing data** | Sensor failures, patient transport gaps | Mean imputation, masking layers |
| **Noisy measurements** | Artifact spikes in heart rate monitors | Preprocessing filters + model robustness |
| **Sequential training (no parallelism)** | RNN cannot be parallelized — slow training on long sequences | Gradient checkpointing, truncated BPTT |
| **Class imbalance** | Critical events are rare | Oversampling (SMOTE), weighted loss |

**Conclusion:** While an RNN provides a foundational sequential model for ICU monitoring, its core limitation — the vanishing gradient problem — makes it inadequate for capturing long-range medical trends. In practice, **LSTM or GRU** architectures are preferred for this task, as they were designed specifically to overcome this limitation through gating mechanisms.

---

## Q4. LSTM for IoT-Based Healthcare Real-Time Prediction *(20 Marks)*

> An IoT-based healthcare system continuously monitors patient vitals (heart rate, ECG, oxygen levels) to predict critical health events in advance. Explain how a Long Short-Term Memory (LSTM) network can be used for this task. Include: Internal structure (input, forget, output gates), Handling long-term dependencies, Advantages over traditional RNN, and Application workflow for real-time prediction.

---

### 1. Introduction

IoT healthcare devices continuously stream patient vitals — heart rate, ECG waveforms, blood oxygen levels (SpO₂) — as time-series data. The challenge is to learn from this **sequential, continuous stream** and predict critical events like cardiac arrest or respiratory failure early enough to intervene.

A **Long Short-Term Memory (LSTM)** network is ideal for this task. It is a specialized RNN that solves the core limitation of vanilla RNNs — the vanishing gradient problem — through a carefully designed gating architecture that allows information to flow across many time steps without decay.

---

### 2. Internal Structure of LSTM — Cell State and Hidden State

Unlike a standard RNN (which only has a hidden state), an LSTM maintains **two separate memory streams**:

| State | Role |
|---|---|
| **Cell State ($C_t$)** | Long-term memory — carries information across many steps with minimal modification. Like a conveyor belt. |
| **Hidden State ($h_t$)** | Short-term / working memory — a filtered, gated snapshot of the cell state, passed to the output layer and fed back as $h_{t-1}$ at the next step. |

This separation is the key innovation. The cell state acts as an information **highway** — it can carry critical long-range signals (e.g., a slow drop in SpO₂ over hours) without being overwritten at every step.

---

### 3. The Three Gates

Each gate is a **sigmoid-activated Dense layer** whose output lies in $[0, 1]$, acting as a soft switch — 0 means "block completely", 1 means "let through completely". All three gates take the same inputs: the current input $X_t$ and the previous hidden state $h_{t-1}$.

---

#### a) Forget Gate — "What to erase from long-term memory"

$$f_t = \sigma(U_f X_t + W_f h_{t-1})$$

The forget gate inspects the current vital reading and the previous memory. It outputs a value between 0 and 1 for each element of the cell state. This is then multiplied element-wise with $C_{t-1}$:

$$C_{t-1} \odot f_t$$

- $f_t[i] \approx 0$: erase position $i$ from long-term memory (irrelevant past info)
- $f_t[i] \approx 1$: keep position $i$ unchanged

**Medical example:** A patient's elevated heart rate from exercise therapy is no longer relevant 2 hours later. The forget gate learns to erase this stale information so it doesn't pollute future predictions.

---

#### b) Input Gate — "What new information to write into long-term memory"

The input gate works in two parallel steps:

**Step 1 — How much to write** (Input gate output $i_t$):
$$i_t = \sigma(U_i X_t + W_i h_{t-1})$$

Controls *which positions* in the cell state will be updated (output in $[0, 1]$).

**Step 2 — What to write** (Candidate cell state $\hat{c}_t$):
$$\hat{c}_t = \tanh(U_c X_t + W_c h_{t-1})$$

Proposes the actual *new content* for the cell state (output in $[-1, 1]$).

The actual update to the cell state is the element-wise product:
$$i_t \odot \hat{c}_t$$

**Medical example:** A sudden drop in SpO₂ from 98% to 90% is important new information. The input gate activates strongly to write this critical reading into long-term memory.

---

#### c) New Cell State — Combining Forget + Input

$$C_t = C_{t-1} \odot f_t + i_t \odot \hat{c}_t$$

This formula combines what was **kept** from the old long-term memory (via the forget gate) with what is **newly written** (via the input gate). The result $C_t$ is the updated long-term memory that flows forward to the next step.

---

#### d) Output Gate — "What to expose from long-term memory as the working state"

$$o_t = \sigma(U_o X_t + W_o h_{t-1})$$

The output gate decides which parts of the updated cell state $C_t$ to expose as the new hidden state $h_t$:

$$h_t = o_t \odot \tanh(C_t)$$

The cell state is first squashed by $\tanh$ (to bound values), then gated by $o_t$. The result $h_t$ is:
- Passed to the **output layer** for prediction
- Fed back as $h_{t-1}$ for the **next time step**

**Medical example:** Even though the cell state may carry many aspects of the patient's history, the output gate selectively exposes only the features most relevant to the current prediction task (e.g., current oxygen trend).

---

### 4. End-to-End LSTM Flow (One Time Step)

**Input:** $X_t$ (current vitals), $h_{t-1}$ (previous hidden state), $C_{t-1}$ (previous cell state)

| Step | Operation | Result |
|---|---|---|
| Forget gate | $f_t = \sigma(U_f X_t + W_f h_{t-1})$ | What to erase |
| Input gate | $i_t = \sigma(U_i X_t + W_i h_{t-1})$ | How much to write |
| Candidate | $\hat{c}_t = \tanh(U_c X_t + W_c h_{t-1})$ | What to write |
| New cell state | $C_t = C_{t-1} \odot f_t + i_t \odot \hat{c}_t$ | Updated long-term memory |
| Output gate | $o_t = \sigma(U_o X_t + W_o h_{t-1})$ | What to expose |
| New hidden state | $h_t = o_t \odot \tanh(C_t)$ | Working memory / output |

---

### 5. Handling Long-Term Dependencies — Why LSTM Solves the Vanishing Gradient Problem

In a **standard RNN**, the gradient flows back through time as:

$$\frac{dLoss}{dW} = \frac{dLoss}{dO_T} \cdot W \cdot W \cdot W \cdots$$

Repeated multiplication by the same $W$ causes gradients to vanish (if $|W| < 1$) or explode (if $|W| > 1$).

In an **LSTM**, the gradient flows back through the **cell state** instead:

$$\frac{dC_t}{dC_{t-1}} = f_t + \frac{d(i_t \cdot \hat{c}_t)}{dC_{t-1}}$$

This is **never the same fixed number repeated**. Each step has a different, learned $f_t$ value. This diversity breaks the geometric decay pattern:
- When $f_t \approx 1$, the gradient passes through almost unchanged — the LSTM can learn dependencies spanning hundreds of time steps.
- The model learns to set $f_t$ appropriately depending on what needs to be remembered.

**For IoT healthcare:** A patient's SpO₂ declining gradually over 4 hours (48 time steps at 5-minute intervals) can be reliably captured by the LSTM's cell state, whereas a standard RNN would have essentially lost that signal after ~10 steps.

---

### 6. Advantages of LSTM Over Traditional RNN

| Property | Traditional RNN | LSTM |
|---|---|---|
| **Memory mechanism** | Single hidden state | Cell state + Hidden state (two streams) |
| **Long-term dependencies** | Cannot retain (vanishing gradient) | Preserves via cell state highway |
| **Gradient behavior** | Vanishes or explodes with depth | Controlled by learned forget gate |
| **Information control** | No selective memory | Three gates provide fine-grained control |
| **Applications** | Short sequences only | Long sequences (paragraphs, hours of vitals) |
| **Medical suitability** | Poor for ICU long-horizon prediction | Excellent for multi-hour patient monitoring |

---

### 7. Application Workflow for Real-Time Prediction

**Step 1 — Data Ingestion**
IoT sensors (ECG patches, SpO₂ monitors, BP cuffs) stream readings every 5 minutes. Readings are stored in a time-series database.

**Step 2 — Preprocessing**
- Normalize all vital sign values to [0, 1] using Min-Max scaling.
- Create a **sliding window** of the last $T$ time steps (e.g., $T = 60$ → last 5 hours of readings).
- Handle missing sensor readings through imputation.

**Step 3 — LSTM Model Inference**
```
Input: (1, 60, 5)  ← batch=1, steps=60, features=5 (HR, BP_sys, BP_dia, SpO₂, Temp)
         ↓
  LSTM Layer (128 units)
         ↓
  LSTM Layer (64 units)
         ↓
  Dense (32, ReLU)
         ↓
  Dense (1, Sigmoid)
         ↓
  Output: P(critical event within 30 min)
```

**Step 4 — Alert Generation**
If $P > 0.7$ (configurable threshold), the system triggers an alert to nursing staff with the prediction confidence and the patient's recent vital trend.

**Step 5 — Continuous Retraining**
As new patient data is collected and outcomes are confirmed, the model is periodically retrained to improve accuracy over time.

---

## Q5. Convolution Operation, Output Size, Stride and Padding *(20 Marks)*

> A 5×5 grayscale image and a 3×3 filter is given. Elaborate on how the convolution operation is performed and calculate the size of the output feature map. Also, explain the role of stride and padding in determining the output size with examples.

---

### 1. Convolution Operation — Concept

The **convolution operation** is the fundamental computation in CNNs. A learnable **filter (kernel)** — a small matrix of weights — slides across the input image. At each position, it performs an **element-wise multiplication** between the filter values and the overlapping image pixels, then **sums** all the products to produce a single output value. The collection of all such output values forms a **feature map** (also called an activation map).

**Purpose:** Each filter is designed (through training) to detect a specific feature — edges, textures, or complex patterns. The feature map shows *where* in the image that feature is present.

---

### 2. Step-by-Step Convolution on a 5×5 Image with a 3×3 Filter

**Given:**
- Input image: 5×5 grayscale
- Filter: 3×3
- Stride: 1 (filter moves 1 pixel at a time)
- Padding: 0 (no padding — "valid" convolution)

**Example Input (5×5):**
```
 1   2   3   4   5
 6   7   8   9  10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25
```

**Filter (3×3) — Edge detector example:**
```
 1   0  -1
 1   0  -1
 1   0  -1
```

**Position (0,0):** Filter overlaps top-left 3×3 region of the image:
```
Image region:     Filter:         Products:
1   2   3         1   0  -1       1×1 + 2×0 + 3×(-1) = -2
6   7   8    ×    1   0  -1  →    6×1 + 7×0 + 8×(-1) = -2
11  12  13        1   0  -1       11×1 + 12×0 + 13×(-1) = -2

Sum = -2 + (-2) + (-2) = -6
```

The filter then **slides one pixel to the right** (stride = 1) and the calculation repeats for the new overlapping region. This continues until the filter has covered the entire image.

---

### 3. Output Feature Map Size Formula

The output size is determined by:

$$\text{Output Size} = \frac{I - F + 2P}{S} + 1$$

Where:
- $I$ = Input size (one dimension)
- $F$ = Filter size
- $P$ = Padding (number of zeros added on each side)
- $S$ = Stride

**Calculation for our example:**
$$\text{Output Size} = \frac{5 - 3 + 2(0)}{1} + 1 = \frac{2}{1} + 1 = 3$$

So the output feature map is **3×3**.

**Verification:** Starting from position (0,0), with a 3×3 filter on a 5×5 image and stride 1:
- Horizontally: positions 0, 1, 2 → 3 positions ✓
- Vertically: positions 0, 1, 2 → 3 positions ✓

---

### 4. Role of Stride

**Stride** is the number of pixels the filter moves at each step. It controls the overlap between filter positions and directly determines the output size.

**Effect of Stride on Output Size:**

| Input | Filter | Padding | Stride | Output Size |
|---|---|---|---|---|
| 5×5 | 3×3 | 0 | **1** | $\frac{5-3+0}{1}+1 = 3$ → **3×3** |
| 5×5 | 3×3 | 0 | **2** | $\frac{5-3+0}{2}+1 = 2$ → **2×2** |
| 7×7 | 3×3 | 0 | **1** | $\frac{7-3+0}{1}+1 = 5$ → **5×5** |
| 7×7 | 3×3 | 0 | **2** | $\frac{7-3+0}{2}+1 = 3$ → **3×3** |

**Key insight:**
- **Stride = 1**: Overlapping windows, maximum information capture, larger output.
- **Stride = 2**: Non-overlapping windows, downsampling without pooling, smaller output.
- A larger stride reduces the output size and computational cost, but may miss fine details.

**Example with Stride = 2:**
On a 5×5 image with a 3×3 filter, the filter positions are:
```
Row 0: cols 0, 2       (moves 2 pixels → 2 positions)
Row 2: cols 0, 2       (moves 2 pixels down → 2 positions)
→ Output: 2×2
```

---

### 5. Role of Padding

**Padding** adds rows and columns of zeros around the border of the input image before applying the filter. It serves two critical purposes:

**a) Controlling output size** — preventing excessive shrinkage through many conv layers.
**b) Preserving border information** — without padding, pixels at the edges are visited by the filter far fewer times than center pixels, causing information loss at the boundaries.

**Types of Padding:**

| Type | Description | Output Size (5×5 input, 3×3 filter, stride 1) |
|---|---|---|
| **Valid (P=0)** | No padding — output shrinks | $\frac{5-3+0}{1}+1 = 3$ → **3×3** |
| **Same (P=1)** | Pad to keep output = input size | $\frac{5-3+2}{1}+1 = 5$ → **5×5** |

**"Same" Padding formula:** $P = \frac{F-1}{2}$ → for F=3: $P = 1$

**Example with Padding = 1:**
The 5×5 image is padded with zeros on all sides to become 7×7:
```
0  0  0  0  0  0  0
0  1  2  3  4  5  0
0  6  7  8  9  10 0
0 11 12 13 14 15  0
0 16 17 18 19 20  0
0 21 22 23 24 25  0
0  0  0  0  0  0  0
```

Output size: $\frac{7 - 3 + 0}{1} + 1 = 5$ → **5×5** (same as input — "same" padding)

---

### 6. Combined Effect Summary

$$\text{Output} = \frac{I - F + 2P}{S} + 1$$

| Scenario | Parameters | Output |
|---|---|---|
| No padding, stride 1 | I=5, F=3, P=0, S=1 | **3×3** |
| Same padding, stride 1 | I=5, F=3, P=1, S=1 | **5×5** |
| No padding, stride 2 | I=5, F=3, P=0, S=2 | **2×2** |
| Same padding, stride 2 | I=5, F=3, P=1, S=2 | **3×3** |

**Design principle in CNN architectures:**
- Use **Same padding + Stride 1** in convolutional layers to preserve spatial dimensions.
- Use **Valid padding + Stride 2** or **Pooling layers** to intentionally downsample and reduce spatial dimensions while increasing feature depth.

---

## Q6. CNN + LSTM for Video Clip Classification *(20 Marks)*

> The task assigned to you is developing an AI system to classify short video clips into categories such as "running," "dancing," or "playing guitar." Each clip is a sequence of 30 image frames (grayscale). Describe how you would build a model that combines CNN and LSTM to solve this problem. What part of the model would use CNN and why?

---

### 1. Problem Analysis

A 30-frame grayscale video clip needs to be classified into one of several action categories. This problem has two simultaneous challenges:
- **Spatial understanding** — what is happening within a single frame (shapes, body posture)
- **Temporal understanding** — how the frames relate over time (motion, sequence of movements)

Neither a CNN alone (which processes a single image) nor an LSTM alone (which processes sequences but lacks spatial processing) is sufficient. Combining them creates a powerful model that handles both aspects.

---

### 2. Role of CNN — Spatial Feature Extraction

**CNN is used to process each individual frame.**

A video clip is a sequence of images. For each frame:
- Raw pixel values encode spatial information (edges, body shape, motion blur)
- A CNN extracts compact **spatial feature vectors** — numerical summaries of what's visible in the frame

The CNN processes each frame **independently**, producing a fixed-size feature vector for each one. For example, a CNN might transform a 64×64 grayscale frame into a 256-dimensional feature vector.

**Why CNN for this?**
- CNNs are explicitly designed to capture **spatial hierarchies** in images.
- They detect low-level features (edges of limbs) → mid-level features (arm positions) → high-level features (body posture) through convolutional + pooling layers.
- Weight sharing across spatial positions means the CNN can detect a dancing arm whether it's on the left or right side of the frame.
- CNNs are far more parameter-efficient than a flat Dense layer on raw pixels.

---

### 3. Role of LSTM — Temporal Sequence Learning

**LSTM is used to process the sequence of CNN feature vectors across time.**

After the CNN extracts a feature vector from each of the 30 frames, we have a sequence:

```
Frame 1 → CNN → f₁ (256-dim vector)
Frame 2 → CNN → f₂
Frame 3 → CNN → f₃
...
Frame 30 → CNN → f₃₀
```

This sequence $[f_1, f_2, ..., f_{30}]$ is fed into the LSTM as a time series. The LSTM processes it step by step, maintaining a hidden state that captures **temporal dynamics**:
- How does the pose change from frame to frame? (motion)
- What is the pattern of movement over time? (e.g., "running" has a cyclic leg pattern)
- What is the overall temporal structure of the action?

The final LSTM hidden state $h_{30}$ encodes both the spatial content (via CNN features) and the temporal evolution (via LSTM memory) of the entire clip.

---

### 4. Full Model Architecture

```
Input Video Clip: (30 frames, 64×64, grayscale)

For each frame in the sequence:
    Frame_t (64×64×1)
         ↓
    Conv2D (32 filters, 3×3, ReLU)
         ↓
    MaxPooling2D (2×2)
         ↓
    Conv2D (64 filters, 3×3, ReLU)
         ↓
    MaxPooling2D (2×2)
         ↓
    Flatten → Dense (256, ReLU)
         ↓
    Feature vector f_t (256-dim)

Sequence of features: [f₁, f₂, ..., f₃₀]
         ↓
    LSTM Layer (128 units, return_sequences=False)
         ↓
    Dense Layer (64 units, ReLU)
         ↓
    Dropout (0.4)
         ↓
    Output Dense (num_classes, Softmax)
         ↓
    Predicted class: "running" / "dancing" / "playing guitar"
```

**In Keras, this is implemented using `TimeDistributed`:**
```python
model = Sequential([
    TimeDistributed(Conv2D(32, (3,3), activation='relu'), input_shape=(30, 64, 64, 1)),
    TimeDistributed(MaxPooling2D(2,2)),
    TimeDistributed(Conv2D(64, (3,3), activation='relu')),
    TimeDistributed(MaxPooling2D(2,2)),
    TimeDistributed(Flatten()),
    TimeDistributed(Dense(256, activation='relu')),
    LSTM(128),
    Dense(64, activation='relu'),
    Dropout(0.4),
    Dense(num_classes, activation='softmax')
])
```

`TimeDistributed` applies the same CNN to each of the 30 frames independently, using **shared CNN weights** across time — the same spatial feature extractor operates on every frame.

---

### 5. Why CNN and Not Just LSTM Directly on Pixels?

If raw pixel values (64×64 = 4096 pixels/frame × 30 frames = 122,880 inputs) were fed directly into an LSTM:
- The LSTM would need to process an enormous number of inputs.
- It has no concept of spatial locality — adjacent pixels are treated no differently from distant pixels.
- Training would be extremely slow and prone to overfitting.

CNN reduces each 64×64 frame to a 256-dimensional semantic vector, preserving spatial meaning in a compact form that the LSTM can efficiently process.

---

### 6. Training and Evaluation

- **Loss**: Categorical Cross-Entropy (multi-class)
- **Optimizer**: Adam
- **Data augmentation**: Random horizontal flip, brightness jitter applied per-frame
- **Evaluation**: Accuracy, Confusion Matrix per class, F1 per class (to detect if any action category is particularly hard to classify)

---

## Q7. LSTM After CNN — Input Shape, Preprocessing, and Combined Benefits *(20 Marks)*

> How would LSTM be used after CNN? Illustrate the input shape and data preprocessing steps. What is the benefit of combining CNN with LSTM instead of using either one alone?

---

### 1. How LSTM is Used After CNN

The combination works in two stages:

**Stage 1 — CNN as spatial feature extractor:**
The CNN processes each frame (image) and converts it from raw pixel space to a compact **semantic feature vector**. This extraction uses convolutional layers, pooling, and a final Dense/Flatten step.

**Stage 2 — LSTM as temporal sequence learner:**
The sequence of CNN feature vectors (one per frame) is treated as a **time series**. The LSTM reads this sequence step by step, maintaining a hidden state that captures how the spatial features evolve over time.

The CNN and LSTM are connected end-to-end and trained jointly via backpropagation — the CNN weights are updated based on how well the temporal classification performs.

---

### 2. Input Shape and Data Preprocessing

#### a) Raw Input Shape
```
Video clip: (num_frames, height, width, channels)
Example:    (30, 64, 64, 1)   ← 30 grayscale frames of 64×64 pixels
```

For a batch of videos:
```
Batch input shape: (batch_size, 30, 64, 64, 1)
```

#### b) Preprocessing Steps

**Step 1 — Frame extraction:**
Extract exactly 30 frames from each video clip. If the clip has more frames, sample at uniform intervals. If fewer, duplicate the last frame to pad.

**Step 2 — Resize:**
Resize each frame to a fixed spatial size (e.g., 64×64) using bilinear interpolation.

**Step 3 — Grayscale conversion:**
Convert RGB frames to grayscale (single channel) if the color information is not needed, reducing input dimensionality by 3×.

**Step 4 — Normalization:**
Divide pixel values by 255 to scale to [0, 1]:
```python
frames = frames.astype('float32') / 255.0
```

**Step 5 — CNN Feature Extraction (per frame):**
Each frame of shape (64, 64, 1) passes through the CNN:
```
(64, 64, 1)
    → Conv2D(32, 3×3, ReLU)   → (62, 62, 32)
    → MaxPooling2D(2×2)        → (31, 31, 32)
    → Conv2D(64, 3×3, ReLU)   → (29, 29, 64)
    → MaxPooling2D(2×2)        → (14, 14, 64)
    → Flatten                  → (12544,)
    → Dense(256, ReLU)         → (256,)
```

After processing all 30 frames, the CNN produces:
```
CNN output shape: (batch_size, 30, 256)
                   ↑           ↑    ↑
               batch size   frames  features per frame
```

**Step 6 — LSTM Input:**
The shape `(batch_size, 30, 256)` is the correct format for LSTM input:
```
LSTM input: (batch_size, time_steps, features)
            (batch_size,     30,      256    )
```
At each time step $t \in [1, 30]$, the LSTM receives a 256-dimensional feature vector representing frame $t$.

**Step 7 — LSTM Processing:**
```
LSTM processes sequence: [f₁, f₂, ..., f₃₀]   each f_t ∈ R^256
LSTM output: h₃₀ ∈ R^128  (final hidden state)
```

**Step 8 — Classification Output:**
```
h₃₀ → Dense(64, ReLU) → Dense(num_classes, Softmax) → class probabilities
```

---

### 3. Benefits of Combining CNN + LSTM vs. Using Either Alone

#### CNN Alone — Limitations
A CNN processes a **single image** — it has no concept of time or sequence. To use CNN alone on a video, you would need to either:
- Process just one frame — losing all temporal information about motion
- Flatten all frames and process as one giant image — destroying temporal order and creating a parameter explosion

**CNN alone cannot understand motion, temporal rhythm, or the order of events.** A CNN cannot distinguish "running" from a static pose of a person mid-stride without understanding the sequence of frames.

#### LSTM Alone — Limitations
An LSTM processes sequences efficiently but expects a **feature vector** at each step. If raw pixels are fed directly:
- Input dimensionality is enormous (64×64 = 4096 per step × 30 steps)
- LSTM has no spatial understanding — treats pixel at position (0,0) the same as pixel at position (32,32)
- Cannot detect spatially local features like edges, body contours, or limb positions
- Training would be extremely slow and would likely fail to generalize

**LSTM alone has no spatial intelligence — it cannot extract meaningful visual features from raw image pixels.**

#### CNN + LSTM — Best of Both Worlds

| Capability | CNN | LSTM | CNN + LSTM |
|---|---|---|---|
| Spatial feature extraction | ✓ | ✗ | ✓ (CNN stage) |
| Temporal sequence modeling | ✗ | ✓ | ✓ (LSTM stage) |
| Motion understanding | ✗ | ✗ alone | ✓ (combined) |
| Parameter efficiency | ✓ | Moderate | ✓ (shared CNN weights across time) |
| Long-range temporal dependencies | N/A | ✓ (with LSTM gating) | ✓ |

**Specific benefits:**
1. **Compact representation**: CNN reduces 4096-dimensional pixel space to 256-dimensional semantic features before LSTM — making temporal learning tractable.
2. **Spatial invariance**: CNN's pooling layers make features robust to small position shifts within frames.
3. **Temporal dynamics**: LSTM captures how spatial features evolve — the rhythm of running, the pattern of guitar strumming.
4. **Shared spatial weights**: The same CNN weights are applied to all 30 frames via `TimeDistributed` — the model learns a single spatial feature extractor that generalizes across all time steps.
5. **End-to-end training**: Both CNN and LSTM weights are trained together via backpropagation, allowing the CNN to learn spatial features that are specifically useful for temporal classification.

**Conclusion:** CNN + LSTM is the standard architecture for action recognition in videos because it elegantly divides the problem — CNN solves "what is in each frame" and LSTM solves "how does what we see evolve over time" — neither architecture can solve both aspects alone.

---

## Q8. Autoencoders and Decoders in Transformer Models *(20 Marks)*

> Describe in detail how the autoencoders and decoders operate in Transformer models.

---

### 1. Background — Autoencoders (Standalone Architecture)

Before discussing Transformers, it is important to understand the standalone **Autoencoder** architecture, as the Transformer's encoder-decoder structure shares conceptual similarities.

An **Autoencoder** is a neural network designed to learn a compressed representation of its input and then reconstruct the original from that compression. It consists of:

- **Encoder**: Maps the input to a compressed latent space (bottleneck)
- **Latent Space (Bottleneck)**: A lower-dimensional representation encoding the most essential information
- **Decoder**: Reconstructs the original input from the latent representation

**Training objective:** Minimize the reconstruction error between the original input $x$ and the reconstructed output $\hat{x}$:

$$\mathcal{L} = \|x - \hat{x}\|^2 \quad \text{(MSE)} \quad \text{or} \quad \mathcal{L} = -\sum x_i \log \hat{x}_i \quad \text{(Binary Cross-Entropy)}$$

Since the target output *is* the input itself, autoencoders are **self-supervised** — no labels required.

The encoder learns to compress: $z = f_{\theta}(x)$ (input → latent code)
The decoder learns to reconstruct: $\hat{x} = g_{\phi}(z)$ (latent code → output)

---

### 2. Transformer Architecture — Encoder-Decoder Overview

The **Transformer** (introduced in "Attention Is All You Need", Vaswani et al., 2017) uses an **encoder-decoder** structure for sequence-to-sequence tasks. Unlike standalone autoencoders (which reconstruct the same input), the Transformer encoder-decoder is designed to **transform** one sequence into another (e.g., English → French translation).

The key innovation is that **Transformers replace all recurrence and convolution with attention mechanisms**, processing the entire sequence in parallel rather than step by step.

```
Input Sequence                    Output Sequence
   (Source)                          (Target)
       ↓                                 ↑
┌─────────────┐           ┌──────────────────────┐
│   ENCODER   │  →  r₁,r₂,...,rₙ  →  │   DECODER   │
└─────────────┘           └──────────────────────┘
```

---

### 3. The Transformer Encoder — How it Operates

The encoder reads the full input sequence and produces a **rich contextual representation** for every token. It consists of **6 stacked identical encoder layers** (in the original Transformer).

Each encoder layer has two sublayers:

#### a) Multi-Head Self-Attention

Self-attention allows every token to "attend to" every other token in the same sequence — capturing relationships regardless of distance.

**For each token, three vectors are computed:**
- **Query (Q)**: "What am I looking for?"
- **Key (K)**: "What do I offer to others?"
- **Value (V)**: "What information do I pass on?"

**Self-Attention computation for token $i$:**

$$\text{Attention}(Q, K, V) = \text{Softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

**Step-by-step example** ("Who is Tendulkar"):
1. Compute dot products of token $i$'s query against every key: `q₁·k₁, q₁·k₂, q₁·k₃`
2. Scale by $\sqrt{d_k}$ (e.g., divide by 8 if $d_k = 64$) to prevent large dot products
3. Apply Softmax → attention weights (sum to 1)
4. Multiply each Value vector by its weight and sum → context-aware representation of token $i$

**Example:** For "Who" in "Who is Tendulkar?":
- "Who" assigns high attention weight to "Tendulkar" (0.99) — making sense, "Who" asks about a person
- The output for "Who" now contains strong information from "Tendulkar"

**Multi-Head Attention:** The encoder runs this process with **multiple independent attention heads** (e.g., 8), each with different Q, K, V weight matrices. Different heads learn different relationship types:
- Head 1: subject-object relationships
- Head 2: grammatical dependencies
- Head 3: positional proximity

Outputs of all heads are concatenated and projected to produce the final representation.

#### b) Feed-Forward Network (FFN)

After self-attention, each token's representation passes through the same **position-wise Feed-Forward Network** (applied independently to each token):

$$\text{FFN}(x) = \text{ReLU}(xW_1 + b_1)W_2 + b_2$$

This is a two-layer Dense network that provides additional non-linear transformation capacity — a "refinement" step after context has been gathered.

#### c) Add & Normalize (Residual Connections + Layer Normalization)

Both sublayers use **residual (skip) connections** and **Layer Normalization**:

$$\text{Output} = \text{LayerNorm}(\text{input} + \text{SubLayer(input)})$$

This stabilizes training, helps gradients flow, and enables stacking 6 deep layers without gradient problems.

**Encoder Output:**
After 6 stacked encoder layers, every input token has a **rich contextual embedding** $r_1, r_2, ..., r_n$ — representing not just the token's own meaning but its full context within the sentence. These are passed to every decoder layer.

---

### 4. The Transformer Decoder — How it Operates

The decoder **generates the output sequence token by token**, using both its own previously generated tokens and the encoder's contextual representations. It also consists of **6 stacked decoder layers**, each with three sublayers.

#### a) Masked Multi-Head Self-Attention

The decoder processes its own output sequence (the previously generated tokens). However, during training, it uses **causal masking** — each token can only attend to tokens that have been generated *before* it (not future tokens):

```
Generating token 4 → can attend to tokens 1, 2, 3
                  → cannot attend to tokens 5, 6, ...
```

This masking prevents the decoder from "cheating" by looking at the correct future tokens during training. It ensures the model generates each token auto-regressively (one at a time, conditioned on all previous outputs).

#### b) Encoder-Decoder Attention (Cross-Attention)

This is the critical bridge between encoder and decoder. For each decoder position:
- **Queries (Q)** come from the **decoder's current hidden state** (what is being generated)
- **Keys (K) and Values (V)** come from the **encoder's output** (the source sentence representations $r_1, ..., r_n$)

$$\text{CrossAttention}(Q_{dec}, K_{enc}, V_{enc}) = \text{Softmax}\!\left(\frac{Q_{dec} K_{enc}^T}{\sqrt{d_k}}\right) V_{enc}$$

This allows the decoder to dynamically **focus on different parts of the source sequence** when generating each output token:

**Example:** Translating "Siddharth played football and he scored a goal":
- When generating "goal", the cross-attention assigns high weights to the encoder states for "scored" and "football"
- When generating the pronoun translation for "he", cross-attention focuses on the encoder state for "Siddharth"
- Each output token gets a **custom context vector** from the source, built from exactly the relevant source words

This mechanism solves the **bottleneck problem** of earlier Seq2Seq models (which compressed the entire source into a single vector).

#### c) Feed-Forward Network (FFN)
Same as in the encoder — applied position-wise after cross-attention for further transformation.

**Decoder Output:**
The final decoder layer's output at each position passes through a **Linear + Softmax** layer to produce a probability distribution over the vocabulary:
```
Decoder output → Linear (vocab_size) → Softmax → P(next token)
```

---

### 5. Comparing Autoencoder and Transformer Encoder-Decoder

| Aspect | Standalone Autoencoder | Transformer Encoder-Decoder |
|---|---|---|
| **Goal** | Reconstruct input (self-supervised) | Transform input sequence to output sequence |
| **Encoder** | Compresses to bottleneck latent vector | Produces contextual representation per token (no bottleneck) |
| **Bottleneck** | Fixed-size latent code | No bottleneck — all encoder states are preserved |
| **Decoder** | Reconstructs from latent code | Generates new sequence using cross-attention |
| **Attention** | Not used (traditional AE) | Self-attention + Cross-attention |
| **Training signal** | Reconstruction loss ($x$ vs $\hat{x}$) | Sequence generation loss (e.g., cross-entropy per token) |
| **Parallelism** | Full | Encoder is fully parallel; decoder is sequential at inference |
| **Applications** | Denoising, dimensionality reduction, anomaly detection | Machine translation, summarization, question answering |

---

### 6. Autoencoder-Based Transformer Variants

Several Transformer models draw directly on autoencoder principles:

#### BART (Bidirectional and Auto-Regressive Transformers)
BART explicitly trains as a **denoising autoencoder**:
- **Encoder**: Reads corrupted input (tokens masked, deleted, sentences shuffled) — like a denoising AE encoder
- **Decoder**: Reconstructs the original clean text — like a denoising AE decoder
- Used for: Summarization, translation, text generation

This is the closest Transformer variant to a true autoencoder — it literally learns to denoise corrupted text.

#### BERT (Encoder-only Transformer)
BERT uses **Masked Language Modeling (MLM)** — a form of denoising autoencoding:
- Random tokens are replaced with `[MASK]`
- The model must predict the original masked tokens
- Like a denoising autoencoder operating at the token level

#### Variational Autoencoder + Transformer
VAE-Transformers combine the probabilistic latent space of a VAE with the Transformer's attention mechanism, producing models capable of controlled text generation.

---

### 7. Summary of Information Flow

```
SOURCE SEQUENCE
      ↓
[Positional Encoding + Token Embedding]
      ↓
┌─────────────────────────────────┐
│      ENCODER (6 layers)         │
│  ┌─────────────────────────┐    │
│  │ Multi-Head Self-Attention│    │  ← every token attends to every source token
│  │ + Add & Normalize        │    │
│  ├─────────────────────────┤    │
│  │ Feed Forward Network     │    │  ← further transforms each token's representation
│  │ + Add & Normalize        │    │
│  └─────────────────────────┘    │
└───────────────┬─────────────────┘
   r₁, r₂, ..., rₙ (contextual encoder embeddings — one per source token)
                │
                ↓ (fed to ALL decoder layers via Cross-Attention)
┌─────────────────────────────────┐
│      DECODER (6 layers)         │
│  ┌─────────────────────────┐    │
│  │ Masked Self-Attention    │    │  ← attends only to previously generated tokens
│  │ + Add & Normalize        │    │
│  ├─────────────────────────┤    │
│  │ Encoder-Decoder          │    │  ← cross-attention: Q from decoder, K/V from encoder
│  │ Cross-Attention          │    │    dynamically focuses on relevant source tokens
│  │ + Add & Normalize        │    │
│  ├─────────────────────────┤    │
│  │ Feed Forward Network     │    │
│  │ + Add & Normalize        │    │
│  └─────────────────────────┘    │
└───────────────┬─────────────────┘
                ↓
    Linear Projection + Softmax
                ↓
    TARGET SEQUENCE (generated token by token)
```

**Conclusion:** In Transformer models, the **encoder** acts as a sophisticated contextual feature extractor — analogous to an autoencoder's encoder but without a fixed bottleneck, preserving full resolution representations for every source token. The **decoder** acts as a conditional generator — using cross-attention to draw on these representations while generating the target sequence. This architecture enables Transformers to surpass both traditional autoencoders (in generative power) and RNN-based seq2seq models (in handling long-range dependencies and training parallelism).

---

*End of DLA CT-2 Answer Sheet*
