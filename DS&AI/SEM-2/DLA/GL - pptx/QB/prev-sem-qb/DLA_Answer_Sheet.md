# DLA — Deep Learning Applications  
## Previous Year Question Bank — Answer Sheet  
**Course Code:** 21CSC558J

---

# Paper 1 — 14-07-2025 FN

---

### Q1. Design a neural network in TensorFlow to perform multiclass classification of handwritten digits. Describe the network structure, activation functions, and how categorical cross-entropy is used. How does backpropagation update weights in this context?

**Network Structure:**

A multi-layer feedforward neural network (MLP) is used for classifying handwritten digits (e.g., MNIST — 10 classes, 0–9). The structure is:

- **Input Layer** — 784 neurons (28×28 flattened pixel values)
- **Hidden Layer 1** — 128 neurons, ReLU activation
- **Hidden Layer 2** — 64 neurons, ReLU activation
- **Output Layer** — 10 neurons, Softmax activation

**TensorFlow/Keras Implementation:**

```python
from tensorflow.keras import layers, models

model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

**Activation Functions:**

- **ReLU** (hidden layers): `f(x) = max(0, x)`. It avoids the vanishing gradient problem and introduces non-linearity, allowing the network to learn complex patterns.
- **Softmax** (output layer): Converts raw scores (logits) into a probability distribution across 10 classes. Defined as:

$$f(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{K} e^{x_j}}$$

*In plain English: For each class, raise e to the power of its raw score, then divide by the sum of all those values. This turns any set of numbers into probabilities that add up to 1.*

All output probabilities sum to 1, making it ideal for multiclass classification.

**Categorical Cross-Entropy Loss:**

Categorical Cross-Entropy measures the difference between the predicted probability distribution (softmax output) and the true label (one-hot encoded):

$$\mathcal{L} = -\sum_{i=1}^{K} y_i \log(\hat{y}_i)$$

Where `y_i` is 1 for the correct class and 0 otherwise. The network is penalised more heavily when it assigns a low probability to the correct class. This loss is used in conjunction with softmax.

**How Backpropagation Updates Weights:**

Backpropagation (BPN) propagates the error from the output layer back to the input layer using the chain rule of calculus:

1. **Forward Pass** — Input passes through all layers to produce a prediction.
2. **Compute Loss** — Categorical Cross-Entropy is computed between prediction and true label.
3. **Backward Pass** — The gradient of the loss with respect to each weight is computed:

$$\frac{\partial L}{\partial w_{ij}} = \delta_j \cdot a_i$$

*In plain English: The gradient for a weight = (how wrong neuron j was) × (how strongly neuron i activated). Weights that contributed more to the error get adjusted more.*

Where `δ_j` is the error term for neuron `j` and `a_i` is the activation from neuron `i`.

4. **Weight Update** — Weights are adjusted in the direction that reduces the loss:

$$w_{ij} = w_{ij} - \eta \cdot \frac{\partial L}{\partial w_{ij}}$$

*In plain English: New weight = Old weight − (learning rate × gradient). The learning rate controls how big each step is. Small steps = slow but stable. Large steps = fast but risky.*

Where `η` is the learning rate. This iterative process continues over many epochs until the loss converges.

---

### Q2. A team working on autonomous vehicles faces exploding gradient issues during model training. Explain how vanishing and exploding gradients occur and propose strategies using normalization (Batch/Group) and optimization (Adam, Adagrad). Include visual interpretation using loss curves.

**Vanishing and Exploding Gradients:**

During training, gradients are calculated using Backpropagation Through Time (BPTT) by applying the chain rule across many layers (or time steps). At each step, the gradient is multiplied by the weight matrix `W` and the derivative of the activation function:

$$\frac{dLoss}{dW} = \frac{dLoss}{dO_{t+n}} \cdot \frac{dO_{t+n}}{dS_{t+n}} \cdot W \cdot W \cdot W \cdots \frac{dS_t}{dW}$$

*What this means: To update weights in early layers, the error signal must be multiplied by W at every step going backward. If W is small (< 1), this product shrinks to near zero — early layers learn nothing. If W is large (> 1), the product explodes — training becomes unstable.*

- **Vanishing Gradient**: When `|W| < 1` (common with sigmoid/tanh), repeated multiplication causes gradients to shrink exponentially toward zero. Early layers stop learning — the network cannot capture long-range dependencies.
- **Exploding Gradient**: When `|W| > 1`, gradients grow exponentially and cause unstable updates (NaN loss, weight divergence). This is more common in deep networks and RNNs used in autonomous vehicle perception tasks.

**Strategy 1 — Batch Normalization:**

Batch Normalization normalises the activations of each mini-batch to have zero mean and unit variance before applying them to the next layer:

$$\hat{x} = \frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$

This keeps activations in a stable range, reduces the risk of vanishing/exploding gradients, and allows higher learning rates. It is applied between the linear transformation and the activation function.

**Group Normalization** divides channels into groups and normalises within each group — it is more robust than Batch Normalization when the batch size is small, which is common in object detection tasks (used in autonomous vehicles).

**Strategy 2 — Adagrad Optimizer:**

Adagrad adapts the learning rate for each parameter individually based on the history of gradients. Parameters that receive large gradients get a smaller learning rate (preventing explosion), while infrequent ones get a larger rate:

```
G = G + (dL/dw)²
w = w - (learning_rate / (sqrt(G) + ε)) × dL/dw
```

This helps stabilise training for models with sparse or variable gradient magnitudes.

**Strategy 3 — Adam Optimizer:**

Adam (Adaptive Moment Estimation) combines the ideas of Adagrad (tracks squared gradients) and momentum (tracks the direction of gradients). It maintains both a first moment (mean) and second moment (variance) of the gradients:

- `m_t = β₁ · m_{t-1} + (1 - β₁) · g_t` (first moment)
- `v_t = β₂ · v_{t-1} + (1 - β₂) · g_t²` (second moment)
- `w = w - η · m̂_t / (sqrt(v̂_t) + ε)` (update)

Adam is highly effective for deep networks — it converges faster and handles both vanishing and exploding gradients better than standard SGD.

**Visual Interpretation — Loss Curves:**

| Situation | Loss Curve |
|---|---|
| **Normal training** | Smooth, steadily decreasing loss over epochs |
| **Vanishing gradients** | Loss stalls early and barely decreases — model is not learning |
| **Exploding gradients** | Loss spikes, oscillates wildly, or becomes NaN |
| **After Batch Norm + Adam** | Smooth, fast convergence with stable, monotonically decreasing loss |

---

### Q3. A company wants to develop a mobile app that classifies short video clips based on user activity (walking, running, jumping). Design a model using CNNs for spatial feature extraction and Bi-directional LSTM for sequence modeling. Explain how you would handle training difficulties with RNNs.

**Model Design — CNN + Bi-directional LSTM:**

Video clips are sequences of frames. Each frame contains spatial information (what a person looks like), and the sequence carries temporal information (how movement evolves over time).

**Step 1 — Spatial Feature Extraction with CNN:**

Each individual video frame is passed through a CNN to extract spatial features. The CNN architecture includes:

- **Convolutional Layers** — Apply learnable filters to detect edges, textures, and body shapes in each frame.
- **Pooling Layers** — Reduce spatial dimensions, retaining only the most prominent features.
- **Flattening Layer** — Converts the 2D feature map into a 1D feature vector per frame.

The CNN acts as a frame-level feature extractor, producing a sequence of feature vectors: `[v₁, v₂, v₃, ..., vT]` where `T` is the number of frames.

**Step 2 — Temporal Modeling with Bi-directional LSTM:**

The sequence of CNN feature vectors is fed into a Bi-directional LSTM (BiLSTM). A standard LSTM processes the sequence forward (past → future), but for activity recognition, context from future frames (e.g., the follow-through of a jump) also matters.

- **Forward LSTM** — reads the sequence left to right: `[v₁ → v₂ → ... → vT]`
- **Backward LSTM** — reads the sequence right to left: `[vT → ... → v₂ → v₁]`
- The outputs from both directions are concatenated at each time step, giving the model awareness of both past and future context for each frame.

This gives the model understanding of both what happened before and what happens after each frame.

**Step 3 — Classification:**

The final BiLSTM output is passed through fully connected Dense layers with Softmax activation to classify the activity (walking / running / jumping).

**Handling RNN Training Difficulties:**

The core difficulty with RNNs is the **vanishing gradient problem**. During Backpropagation Through Time (BPTT), gradients are multiplied by the weight matrix at every step. When `|W| < 1`, the gradient shrinks exponentially and early frames contribute nothing to learning.

| Problem | Solution |
|---|---|
| Vanishing gradient | Use LSTM with gating mechanism (forget, input, output gates control gradient flow) |
| Exploding gradient | Apply gradient clipping — cap gradients above a threshold |
| Overfitting | Add Dropout between LSTM layers |
| Slow convergence | Use Adam optimizer with adaptive learning rates |
| Short video sequences | Adjust sequence length and use padding/masking for variable-length clips |

The LSTM's cell state acts as a highway that carries information across many time steps with minimal modification, solving the vanishing gradient problem that plagues standard RNNs.

---

### Q4. How would you use transformers to perform sentiment classification on movie reviews? Outline the architecture using attention mechanisms and pretrained BERT embeddings. Discuss how fine-tuning improves performance over static word embeddings.

**Transformer Architecture for Sentiment Classification:**

A Transformer processes the entire input sequence in parallel using a mechanism called **self-attention**, which allows every word to directly attend to every other word regardless of distance — unlike RNNs that process step by step.

```
"The movie was brilliant"
    ↕      ↕     ↕      ↕
   [  Self-Attention across all tokens  ]
         ↓
   Context-aware representations
         ↓
   Classification Head (Dense + Softmax)
         ↓
   Sentiment: Positive / Negative
```

**Self-Attention Mechanism:**

For each token, three vectors are computed — Query (Q), Key (K), and Value (V) — using learned weight matrices. The attention score tells the model how much each word should influence the representation of every other word:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

*In plain English:*
- *Q (Query) = "What am I looking for?" — represents the current word's need*
- *K (Key) = "What do I offer?" — represents each word's identity*
- *V (Value) = "What will I actually contribute?" — the information to pass forward*
- *QKᵀ computes a relevance score for every word pair*
- *Dividing by √dₖ prevents scores from growing too large (keeps softmax stable)*
- *Softmax turns scores into attention weights (probabilities)*
- *Multiplying by V gives a weighted blend of all word information based on relevance*

The score is scaled by `√d_k` to prevent softmax from saturating at extreme values, ensuring stable gradients.

**Using Pretrained BERT Embeddings:**

BERT (Bidirectional Encoder Representations from Transformers) is pre-trained on massive text corpora using:
- **Masked Language Modeling** — predict missing words in a sentence
- **Next Sentence Prediction** — predict whether two sentences are consecutive

This pretraining gives BERT deep contextual word representations — unlike static embeddings (Word2Vec/GloVe), BERT generates different embeddings for the same word in different contexts (e.g., "bank" in "river bank" vs. "savings bank").

For sentiment classification, the special `[CLS]` token's final hidden state is used as the sentence-level representation and passed to a classification head.

**Fine-tuning vs. Static Embeddings:**

| Aspect | Static Embeddings (Word2Vec) | Fine-tuned BERT |
|---|---|---|
| Context sensitivity | Same vector for every context | Adapts per context |
| Training signal | Fixed — not updated during task training | Updated end-to-end |
| Task adaptation | General purpose | Specialised for sentiment |
| Performance | Good baseline | State-of-the-art |

Fine-tuning updates all of BERT's pre-learned weights on the specific movie review dataset with a small learning rate, allowing the model to specialise its language understanding for sentiment detection. Even a small number of labelled examples is sufficient because the model already understands language structure from pre-training.

---

### Q5. You are developing a visual question answering (VQA) system for educational content. Describe how multi-modal data from images and natural language can be used using CycleGAN and vision-language transformers. Illustrate the pipeline with intermediate output examples.

**Visual Question Answering (VQA) System:**

VQA combines three areas — Computer Vision (to understand images), Natural Language Processing (to understand questions), and Reasoning (to connect both and produce an answer).

**Full Pipeline:**

```
Image (diagram/chart) + Question (text)
         ↓                    ↓
  Image Encoder          Question Encoder
  (CNN / ViT)            (LSTM / Transformer)
         ↓                    ↓
  Image Features        Question Embeddings
              ↓        ↓
           Feature Fusion
           (Cross-Attention)
                 ↓
            Reasoning Layer
                 ↓
          Answer Prediction
          (Classification / Generation)
```

**Intermediate Example:**

- Input Image: A bar chart showing student scores
- Question: "Which student scored the highest?"
- Image Feature Vector: Encodes bars, heights, labels
- Question Embedding: Encodes the meaning of "highest" and "student"
- Fused Representation: Aligns bar heights with student labels
- Output: "Student C"

**Role of CycleGAN in Educational VQA:**

CycleGAN (Cycle-Consistent Generative Adversarial Network) enables unpaired image-to-image translation. In educational contexts it can be used to:
- Convert hand-drawn diagrams into clean digital diagrams (so the VQA model can better process them)
- Translate images across domains (e.g., sketch → realistic image) without needing paired training data

CycleGAN uses two generators (G: domain A → B, F: domain B → A) and two discriminators. The key is the **cycle consistency loss** — if you translate A→B→A, you should get back the original. This constraint forces the generators to preserve the content of the original image. Combined with an adversarial loss (which ensures the output looks realistic in the target domain), CycleGAN can transform images across domains without needing paired training data.

**Vision-Language Transformers:**

Models like ViLBERT and CLIP use transformer architecture to jointly encode images and text. Cross-attention layers allow text tokens to attend to image regions and vice versa, creating a rich multimodal understanding essential for VQA in educational settings (e.g., understanding diagrams, equations, maps).

---

### Q6. A sentiment analysis task involves predicting mood trends over time based on diary entries. Combine TensorFlow models using embeddings, CNNs, and LSTM to build a hybrid text classification model. Justify the use of each component.

**Hybrid Text Classification Pipeline:**

```
Raw Diary Text → Tokenization → Embedding Layer → CNN → LSTM → Dense → Output
```

**Component 1 — Embedding Layer:**

Each word is converted from a vocabulary index into a dense vector representation. The Embedding layer has a weight matrix of shape `(vocab_size × embedding_dim)` that is learned during training.

- Each word becomes a vector (e.g., 50 or 100 numbers)
- Semantically similar words end up close in the embedding space
- For a sentence of 300 words with embedding size 50, the output is `(300 × 50)`

Without embeddings, the model cannot understand word meaning — raw indices are meaningless to a neural network.

**Component 2 — CNN (1D Convolution):**

1D convolutional filters slide across the sequence of word embeddings to detect local patterns — phrases, n-grams, and mood-indicating expressions like "felt happy", "couldn't sleep", "everything went wrong".

- Filters of different sizes (e.g., 2, 3, 4 words) capture short-range semantic patterns
- ReLU activation followed by max-pooling extracts the most prominent mood signals

CNNs are fast and excellent at detecting local linguistic patterns regardless of position.

**Component 3 — LSTM:**

The output of the CNN is passed into an LSTM, which processes the sequence over time and captures long-range mood trends — for example, noticing that entries earlier in the week mentioned anxiety and that this persists across days.

The LSTM maintains a hidden state that accumulates context across all diary entries, allowing the model to track mood evolution over time. Its gating mechanism (forget, input, output gates) prevents the vanishing gradient problem.

**Component 4 — Dense Output Layer:**

The final LSTM hidden state is passed through a Dense layer with Softmax or Sigmoid activation to predict the mood label (e.g., positive / negative / neutral) or a continuous mood score.

**TensorFlow Implementation Sketch:**

```python
model = models.Sequential([
    layers.Embedding(vocab_size, 50, input_length=max_len),
    layers.Conv1D(64, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.LSTM(64, return_sequences=False),
    layers.Dense(3, activation='softmax')  # 3 mood classes
])
```

Each component handles a different aspect: embeddings convert words to meaning, CNNs detect local patterns, and LSTM captures temporal mood evolution.

---

### Q7. A film production studio wants to generate cartoon-style animations from live-action footage. Explain how Pix2Pix or StyleGAN can be used for this task. Describe training the GAN, handling instability, and improving output realism using transformers or attention networks.

**GAN Architecture Overview:**

A GAN consists of two competing neural networks:
- **Generator (G)** — takes input (noise or real image) and generates a fake/stylised image
- **Discriminator (D)** — distinguishes between real target-style images and generator outputs

The adversarial training is a minimax game: the Generator tries to produce images so convincing that the Discriminator cannot tell them apart from real cartoons, while the Discriminator tries to catch fakes. Both networks improve each other through this competition.

**Pix2Pix for Live-Action to Cartoon Translation:**

Pix2Pix is a conditional GAN (cGAN) for paired image-to-image translation. Given paired examples of (live-action frame, cartoon frame), it learns the mapping:
- The Generator (a U-Net) takes a live frame and produces a cartoon-style version
- The Discriminator receives both the original and the generated cartoon and judges realism
- Loss = Adversarial loss + L1 reconstruction loss (ensures the output matches the paired target closely)

**StyleGAN for High-Quality Cartoon Style:**

StyleGAN uses a style-based generator that separates content from style via Adaptive Instance Normalisation (AdaIN). For cartoon generation:
- A style vector (representing the cartoon aesthetic) is injected at multiple resolution levels
- Coarse levels control overall cartoon style (colour palette, outline shading)
- Fine levels control texture and detail (shading patterns, line thickness)

**Training the GAN:**

1. Initialize both Generator and Discriminator with random weights.
2. Train Discriminator on real cartoon frames (label = real) and generated frames (label = fake).
3. Train Generator to produce images that fool the Discriminator (maximise D(G(x)) → 1).
4. Alternate updates: do not update G and D simultaneously.
5. Repeat for many iterations until generated cartoons are visually convincing.

**Handling Training Instability:**

| Problem | Solution |
|---|---|
| Mode collapse (G generates only one type of output) | Use mini-batch discrimination; use Wasserstein GAN loss |
| Discriminator becomes too strong too fast | Train G more steps per D step; use label smoothing |
| Training oscillation | Use learning rate scheduling; lower the learning rate |
| Gradient vanishing in G | Use Spectral Normalization on D |

**Improving Output Realism with Attention:**

Transformer-based attention and self-attention layers can be added to the Generator:
- **Self-attention** allows the Generator to ensure long-range spatial consistency (e.g., the colour of a character's hair in one part of the frame matches another)
- Cross-attention can allow the model to condition the cartoon style on a reference image
- This is particularly important for animation — ensuring visual consistency across frames

---

---

# Paper 2 — 17-11-2025 AN

---

### Q1. You are working on a multi-class classification problem with three classes. The model outputs raw scores {3, 2, 0.1} for each class. Convert these into a probability distribution using the Softmax function. Also, calculate the Categorical Cross-Entropy Loss.

**Step 1 — Apply Softmax:**

The softmax function converts raw logits into probabilities:

$$f(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{K} e^{x_j}}$$

Given logits: `z = [3, 2, 0.1]`

Calculate the exponentials:

| Class | Logit | e^z |
|---|---|---|
| Class 1 | 3 | e³ = 20.086 |
| Class 2 | 2 | e² = 7.389 |
| Class 3 | 0.1 | e^0.1 = 1.105 |
| **Sum** | | **28.580** |

Softmax probabilities:

$$P(\text{Class 1}) = \frac{20.086}{28.580} \approx 0.703 \quad (70.3\%)$$

$$P(\text{Class 2}) = \frac{7.389}{28.580} \approx 0.259 \quad (25.9\%)$$

$$P(\text{Class 3}) = \frac{1.105}{28.580} \approx 0.039 \quad (3.9\%)$$

**Verification:** `0.703 + 0.259 + 0.039 = 1.001 ≈ 1.0` ✓

**Step 2 — Categorical Cross-Entropy Loss:**

Assuming the true class is Class 1 (one-hot label: `y = [1, 0, 0]`):

$$\mathcal{L} = -\sum_{i=1}^{K} y_i \log(\hat{y}_i) = -(1 \times \log(0.703) + 0 \times \log(0.259) + 0 \times \log(0.039))$$

$$\mathcal{L} = -\log(0.703) = -(-0.352) = \mathbf{0.352}$$

**Interpretation:** The loss is 0.352. Since the model correctly assigned the highest probability (70.3%) to the true class (Class 1), the loss is relatively low. If the model were wrong and assigned low probability to the true class, the loss would be much higher (e.g., `-log(0.039) = 3.24`).

---

### Q2. Implement the Adagrad optimization algorithm. Initial parameter θ₀ = 1.5, G₀ = 0, η = 0.01, ε = 10⁻⁸. Gradients: g₁ = 0.8, g₂ = 0.6, g₃ = 0.4. Compute Gₜ and updated θₜ at each step.

**Adagrad Update Rules:**

```
G_t = G_{t-1} + g_t²
θ_t = θ_{t-1} - (η / (sqrt(G_t) + ε)) × g_t
```

The key idea is that `G_t` accumulates squared gradients, making the effective learning rate smaller for parameters that receive large gradients.

---

**Iteration 1 (g₁ = 0.8):**

$$G_1 = G_0 + g_1^2 = 0 + (0.8)^2 = 0.64$$

$$\theta_1 = \theta_0 - \frac{\eta}{\sqrt{G_1} + \varepsilon} \times g_1 = 1.5 - \frac{0.01}{\sqrt{0.64} + 10^{-8}} \times 0.8$$

$$= 1.5 - \frac{0.01}{0.8} \times 0.8 = 1.5 - 0.01 = \mathbf{1.490}$$

---

**Iteration 2 (g₂ = 0.6):**

$$G_2 = G_1 + g_2^2 = 0.64 + (0.6)^2 = 0.64 + 0.36 = 1.00$$

$$\theta_2 = \theta_1 - \frac{\eta}{\sqrt{G_2} + \varepsilon} \times g_2 = 1.490 - \frac{0.01}{\sqrt{1.00}} \times 0.6$$

$$= 1.490 - \frac{0.01}{1.0} \times 0.6 = 1.490 - 0.006 = \mathbf{1.484}$$

---

**Iteration 3 (g₃ = 0.4):**

$$G_3 = G_2 + g_3^2 = 1.00 + (0.4)^2 = 1.00 + 0.16 = 1.16$$

$$\theta_3 = \theta_2 - \frac{\eta}{\sqrt{G_3} + \varepsilon} \times g_3 = 1.484 - \frac{0.01}{\sqrt{1.16}} \times 0.4$$

$$= 1.484 - \frac{0.01}{1.077} \times 0.4 = 1.484 - 0.00371 = \mathbf{1.480}$$

---

**Summary Table:**

| Iteration | Gradient gₜ | Accumulated Gₜ | √Gₜ | Effective LR | Updated θₜ |
|---|---|---|---|---|---|
| 0 (initial) | — | 0 | — | — | 1.500 |
| 1 | 0.8 | 0.64 | 0.800 | 0.01/0.800 = 0.0125 | 1.490 |
| 2 | 0.6 | 1.00 | 1.000 | 0.01/1.000 = 0.010 | 1.484 |
| 3 | 0.4 | 1.16 | 1.077 | 0.01/1.077 = 0.009 | 1.480 |

**Key Observation:** As training progresses, `G_t` accumulates and the effective learning rate decreases. This is the adaptive nature of Adagrad — parameters that receive larger gradients get smaller updates, preventing overshooting.

---

### Q3. You are building a system to predict the next word in long English sentences. Explain how an LSTM helps solve the vanishing gradient problem and retains long-term dependencies. Describe the three gates of an LSTM with their function.

**Why Standard RNN Fails:**

In a standard RNN, the hidden state at each step is computed from the current word and the previous hidden state. During training (Backpropagation Through Time), the error signal must travel back through every time step. At each step it gets multiplied by the weight matrix. If the weights are small — which they often are with tanh — the signal shrinks exponentially and early words contribute nothing to learning. This is the **vanishing gradient problem**.

**How LSTM Solves This:**

LSTM introduces a **cell state** — a separate memory lane that runs alongside the hidden state. Unlike the hidden state which is compressed at every step, the cell state is updated by simple addition: new information is added to what is already stored. Gradients can flow backward through this additive path without shrinking, so the network can remember information from early in a long sentence. The cell state carries memory almost unchanged unless the Forget Gate decides to erase it.

**The Three Gates:**

**1. Forget Gate** — "What to erase from long-term memory"

Takes the current word and the previous hidden state as input and outputs a value between 0 and 1 for each piece of stored memory. Close to 1 means keep, close to 0 means erase.

- Example: When the sentence starts fresh with a new subject, the forget gate erases the old subject from memory so it doesn’t interfere with the next prediction.

**2. Input Gate** — "What new information to write"

Two parts work together: one part decides *how much* new information to write, and another part computes *what* the new information is (based on the current word and previous hidden state). Together they control what new knowledge gets added to the cell state.

- Example: When the word “Paris” appears, the input gate stores it as the current location or subject.

**3. Output Gate** — "What to expose as the hidden state"

Decides which parts of the cell state are relevant right now and filters the cell state to produce the hidden state — which represents what the network “thinks” at this step.

- Example: When predicting a verb, the output gate surfaces the stored subject so the model can produce grammatically correct predictions.

**Summary — How LSTM Retains Long-Term Dependencies for Next-Word Prediction:**

For a sentence like *"The student who studied all night for the physics exam finally passed the..."*, the LSTM can:
- Store "student" in the cell state early in the sentence
- Keep it through many intermediate words via a high forget gate value
- Use it at the end to correctly predict "exam" → helping predict the next word "with" or "successfully"

---

### Q4. Given input matrix X and weight matrices Wq, Wk, Wv, compute Self-Attention step by step and comment on the final output.

**Given:**

$$X = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 1 & 2 & 1 \end{bmatrix}, \quad W_Q = \begin{bmatrix} 1 & 0 & -1 \\ 2 & -1 & 1 \\ 0 & 1 & 1 \end{bmatrix}, \quad W_K = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 0 & -1 \\ 2 & 1 & 0 \end{bmatrix}, \quad W_V = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 1 & 0 \\ 0 & 1 & -1 \end{bmatrix}$$

**Step 1 — Compute Q, K, V (Q = X·Wq, K = X·Wk, V = X·Wv):**

$$Q = X \cdot W_Q = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 2 & 4 \\ 5 & -1 & 2 \end{bmatrix}$$

$$K = X \cdot W_K = \begin{bmatrix} 4 & 3 & 2 \\ 7 & 3 & -1 \\ 4 & 2 & 0 \end{bmatrix}$$

$$V = X \cdot W_V = \begin{bmatrix} 1 & 4 & -1 \\ 2 & 4 & -3 \\ 5 & 5 & 0 \end{bmatrix}$$

**Step 2 — Compute Scaled Dot-Product Scores (QKᵀ / √dₖ):**

`dₖ = 3`, so `√dₖ = √3 ≈ 1.732`

$$QK^T = \begin{bmatrix} 12 & 12 & 8 \\ 22 & 16 & 12 \\ 21 & 30 & 18 \end{bmatrix}$$

$$\text{Scaled:} \quad \frac{QK^T}{\sqrt{3}} \approx \begin{bmatrix} 6.93 & 6.93 & 4.62 \\ 12.70 & 9.24 & 6.93 \\ 12.12 & 17.32 & 10.39 \end{bmatrix}$$

**Step 3 — Apply Softmax (row-wise) to get Attention Weights (A):**

$$A = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) \approx \begin{bmatrix} 0.476 & 0.476 & 0.047 \\ 0.967 & 0.030 & 0.003 \\ 0.006 & 0.993 & 0.001 \end{bmatrix}$$

**Step 4 — Compute Output (A · V):**

$$\text{Output} = A \cdot V \approx \begin{bmatrix} 1.66 & 4.04 & -1.90 \\ 1.04 & 4.00 & -1.06 \\ 1.99 & 4.00 & -2.98 \end{bmatrix}$$

**Comment on the Final Output:**

- **Token 1** (Row 1): Attention is distributed equally between Tokens 1 and 2 (both ~47.6%), with minimal weight on Token 3. The output is a blend of V rows 1 and 2.
- **Token 2** (Row 2): Strongly attends to Token 1 (96.7%), meaning Token 2 is mostly contextualised by Token 1's information.
- **Token 3** (Row 3): Strongly attends to Token 2 (99.3%), meaning Token 3's representation is dominated by Token 2's information.

The self-attention mechanism allows each token to gather relevant context from other tokens — tokens that are semantically related (based on Q-K compatibility) receive higher attention weights. The final output is a weighted combination of Value vectors that captures rich contextual relationships across all positions in the sequence simultaneously.

---

### Q5. Explain the architecture and working principles of CycleGANs in detail. How do they enable unpaired image-to-image translation, and what role do cycle consistency loss and adversarial loss play?

**What is CycleGAN?**

CycleGAN (Cycle-Consistent Generative Adversarial Network) enables image-to-image translation between two domains without needing paired training examples. For example: converting photos to paintings, horses to zebras, summer to winter — without needing a matched photo for every image.

This is a major advance over Pix2Pix, which requires paired training data (e.g., a photo next to its exact cartoon version).

**Architecture:**

CycleGAN has two generators and two discriminators:

| Component | Role |
|---|---|
| **Generator G: A → B** | Translates images from Domain A to Domain B (e.g., photo → painting) |
| **Generator F: B → A** | Translates images from Domain B back to Domain A (e.g., painting → photo) |
| **Discriminator Dₐ** | Tells apart real Domain A images from F(B) generated images |
| **Discriminator D_B** | Tells apart real Domain B images from G(A) generated images |

**Working Principle — Adversarial Training:**

Each generator tries to fool its corresponding discriminator, just like a standard GAN. This makes the generated images look realistic in the target domain.

**The Key Innovation — Cycle Consistency Loss:**

The adversarial loss alone cannot guarantee that the translated image preserves the original content (a model could learn to map all photos to a single painting style, losing identity). Cycle consistency enforces that if you translate A → B → A, you should get back the original A:

- **Forward cycle:** `x → G(x) → F(G(x)) ≈ x`
- **Backward cycle:** `y → F(y) → G(F(y)) ≈ y`

The cycle consistency loss measures how different the round-tripped image is from the original (pixel-by-pixel). Combined with the adversarial loss (which makes outputs look realistic) and weighted by a factor λ (typically 10), the total training loss keeps both generators honest — they must preserve content while still producing realistic translations.

This constraint forces the generators to preserve semantic content and structure across the translation — the shape of a horse stays consistent when it becomes a zebra and is translated back.

**Challenges in Training CycleGANs:**

1. **Mode collapse** — Generator produces limited variety of outputs; addressed using diverse noise inputs
2. **Training instability** — Two generators and two discriminators must be balanced; use equal learning rates
3. **Checkerboard artifacts** — Common in generated images; use nearest-neighbor upsampling instead of transposed convolutions
4. **High computational cost** — Training four networks simultaneously requires significant GPU memory
5. **Semantic violations** — Cycle consistency constrains pixel-level content but not always semantic meaning; can lead to undesired texture transfers

**Applications:** Photo to painting (Monet style), medical image synthesis (MRI → CT), satellite to map translation.

---

### Q6. Training a neural network shows high training and validation errors (underfitting). Analyze reasons and propose architectural modifications. How would increasing the learning rate affect underfitting?

**What is Underfitting?**

Underfitting occurs when a model is too simple to capture the patterns in the data — it performs poorly on both training and validation sets. It is the opposite of overfitting.

**Root Causes and Analysis:**

**1. Insufficient Model Complexity:**

If the network has too few layers or too few neurons, it lacks the capacity to represent complex relationships in the data. A single hidden layer with 4 neurons cannot classify complex non-linear boundaries.

*Fix:* Add more hidden layers (deep network) and increase the number of neurons per layer. Use architectures like ResNet or DenseNet for complex tasks.

**2. Wrong Activation Functions:**

Linear activation functions in hidden layers prevent the network from learning non-linear patterns — no matter how many layers are stacked, a sequence of linear transformations is still linear.

*Fix:* Use non-linear activations — ReLU is the standard for hidden layers. Leaky ReLU avoids the "dying ReLU" problem (where neurons output zero for all inputs). For classification, use Softmax in the output layer.

**3. Learning Rate Too Low:**

An extremely small learning rate causes very tiny weight updates — the model converges too slowly or gets stuck in a local minimum far from the global optimum, never achieving good performance.

*Fix:* Increase the learning rate or use an adaptive optimizer like Adam or Adagrad that dynamically adjusts the learning rate per parameter.

**4. Too Few Training Epochs:**

The model may simply not have trained long enough — it hasn't had enough iterations to adjust its weights sufficiently.

*Fix:* Train for more epochs, use early stopping based on validation loss.

**5. Input Features Not Expressive Enough:**

If the raw input features are too sparse or uninformative, even a complex model will underfit.

*Fix:* Use feature engineering, richer embeddings, or pretrained representations.

**Architectural Modifications:**

| Modification | Effect |
|---|---|
| Add more layers (deeper network) | Increases model capacity to learn hierarchical features |
| Increase neurons per layer | Gives more parameters to represent complex boundaries |
| Use ReLU instead of Linear | Introduces non-linearity essential for complex pattern learning |
| Add skip connections (ResNet style) | Enables very deep networks to train without degradation |
| Use Batch Normalization | Stabilises training and allows higher learning rates |

**Effect of Increasing Learning Rate on Underfitting:**

Increasing the learning rate means larger weight updates per iteration, which can help in these ways:
- The model explores the loss landscape more aggressively, escaping flat regions and local minima faster
- Training converges in fewer epochs, reducing the risk of the model being "undertrained"

However, if the learning rate is increased too much, it causes overshooting — the model jumps over the optimal weights and the loss oscillates or diverges. The ideal approach is to use a moderate learning rate with a learning rate scheduler (warm-up then decay) or use Adam which adapts the learning rate automatically.

---

### Q7. Discuss the generative capabilities of VAEs and the role of KL divergence in modeling complex data distributions. Why do VAEs minimize KL divergence between q(z|x) and p(z), and what happens if this term is removed?

**What is a Variational Autoencoder (VAE)?**

A VAE is a generative model based on the autoencoder framework. Unlike a standard autoencoder that encodes input to a fixed point in latent space, a VAE encodes input as a **probability distribution** — specifically a Gaussian with mean `μ` and variance `σ²`.

This probabilistic encoding means the model can **generate new data** by sampling from the latent distribution, making VAEs generative models.

```
Input x → Encoder → [μ, σ²] → Sample z ~ N(μ, σ²) → Decoder → Reconstructed x̂
```

**Generative Capabilities:**

- By sampling `z ~ N(0, 1)` (the prior) and passing through the decoder, the VAE generates entirely new data points
- The latent space is continuous and structured — interpolating between two latent codes produces smooth, meaningful transitions (e.g., morphing between two faces)
- Can be used for image generation, data augmentation, anomaly detection, and dimensionality reduction

**The Role of KL Divergence:**

The VAE has two training objectives: (1) the **reconstruction loss** ensures the decoder can reproduce the input from the latent code; (2) the **KL divergence term** is a regularisation penalty that keeps the encoder's output distribution close to a standard Gaussian N(0, 1).

KL divergence (Kullback-Leibler divergence) measures how far apart two probability distributions are. In a VAE, it measures how different the encoder's distribution (what the encoder outputs for each input) is from the standard Gaussian prior. Minimising it pushes the encoder toward producing a well-organised, consistent latent space.

**Why Minimise KL Divergence:**

1. **Forces a structured latent space** — Without regularisation, the encoder could map each input to a very narrow, non-overlapping region in latent space. Sampling from random regions would then produce meaningless outputs.

2. **Enables smooth interpolation** — By keeping `q(z|x)` close to a standard Gaussian `N(0,1)`, the latent space is smooth and continuous. Similar inputs have overlapping distributions, so interpolation between them produces meaningful results.

3. **Prevents memorisation** — If the encoder could use any point in a high-dimensional space, it would simply memorise training examples. KL divergence forces the model to generalise.

4. **Enables sampling at test time** — You can sample `z ~ N(0, 1)` and generate valid new data because the decoder was trained to handle latent codes from this distribution.

**What Happens if KL Divergence is Removed:**

If only the reconstruction loss is used (no KL term), the VAE degenerates into a standard deterministic autoencoder:

- The encoder maps each input to a **single fixed point**, not a distribution
- The latent space becomes **disorganised** — unoccupied gaps exist between data points
- Sampling `z ~ N(0,1)` produces **meaningless or broken** outputs because the decoder has never seen random latent codes during training
- The model **loses its generative capability** — it can reconstruct training inputs but cannot generate new samples

In short, the KL term is what makes a VAE "variational" and generative. Without it, the model is just a standard autoencoder with no generative power.

---

---

# Paper 3 — 21-05-2025 FN

---

### Q1. You decide to use a multi-layer neural network with one hidden layer to solve the XOR problem. Specify the activation function and number of neurons required in the hidden layer. Why is non-linearity important?

**The XOR Problem:**

XOR is not linearly separable — you cannot draw a single straight line to correctly separate the four input-output pairs:

| x₁ | x₂ | XOR Output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

A single-layer perceptron (linear classifier) cannot solve XOR because there is no linear decision boundary that separates the 0-class from the 1-class.

**Network Architecture Required:**

- **Input Layer** — 2 neurons (x₁, x₂)
- **Hidden Layer** — **2 neurons** with **sigmoid** (or ReLU) activation
- **Output Layer** — 1 neuron with sigmoid activation (binary output)

**Minimum configuration:** 2 neurons in the hidden layer is sufficient. The hidden neurons can learn to compute intermediate features:
- Neuron 1: learns `x₁ OR x₂` (fires if either is 1)
- Neuron 2: learns `x₁ AND x₂` (fires only if both are 1)
- Output: `OR AND NOT(AND)` = XOR

**Activation Function — Why Sigmoid or ReLU:**

The **Sigmoid** activation function:

$$f(x) = \frac{1}{1 + e^{-x}}$$

maps inputs to `(0, 1)`. It is differentiable and introduces the non-linearity needed to create curved decision boundaries.

**ReLU** (`f(x) = max(0, x)`) is also effective — it is computationally simpler and avoids the vanishing gradient problem.

**Why Non-Linearity is Essential:**

Without a non-linear activation function, no matter how many layers are stacked, the entire network is equivalent to a single linear transformation. Stacking three linear layers is the same as having one big layer — the weight matrices just multiply together into one. You can go as deep as you want, but without non-linearity you can only draw straight-line decision boundaries.

This is simply a linear operation — incapable of solving XOR.

By introducing non-linearity (sigmoid or ReLU), the hidden layer can create curved, non-linear decision boundaries. The hidden neurons transform the input space into a new representation where the data becomes linearly separable — and the output layer can then correctly classify it.

This is the key insight: **non-linearity enables universal function approximation** — with enough non-linear neurons, any function can theoretically be approximated.

---

### Q2. Training a neural network on a complex dataset shows high training and validation errors (underfitting). Analyze reasons for underfitting and propose fixes. How would increasing the learning rate affect the problem?

*(This question is identical to Paper 2, Q6. The complete answer is provided above in Paper 2 Q6.)*

**Summary of Key Points:**

- **Insufficient model complexity** → Add more layers and neurons
- **Wrong activation functions** → Use ReLU for hidden layers (not linear/identity)
- **Learning rate too low** → Increase it or use Adam optimizer
- **Too few epochs** → Train longer with early stopping

**Effect of Increasing Learning Rate:**

Increasing the learning rate leads to larger weight updates, helping the model escape flat regions of the loss surface and converge faster. For an underfitting model that is "stuck" making tiny adjustments, a higher learning rate can kickstart learning. However, if it is too high, the model overshoots the minimum and training becomes unstable. Using adaptive optimizers like Adam is the safest approach — they automatically find the right effective learning rate for each parameter.

---

### Q3. Consider a 5×5 grayscale image and a 3×3 filter. Describe how the convolution operation is performed and calculate the output feature map size. Explain the role of stride and padding with examples.

**What is Convolution in CNN?**

Convolution is the core operation of a CNN's feature extraction layer. A small learnable filter (kernel) slides across the input image, performing element-wise multiplication at each position and summing the results to produce a single output value. This produces a **feature map** that highlights where certain features (edges, textures) appear in the image.

**Example — 5×5 image with 3×3 filter:**

Say the input image is:

```
Input (5×5):         Filter (3×3):
1  2  3  4  5        1  0 -1
6  7  8  9  10   ×   1  0 -1
11 12 13 14 15       1  0 -1
16 17 18 19 20
21 22 23 24 25
```

The filter is placed at the top-left 3×3 region, element-wise multiplication is performed, and the sum becomes the top-left value of the output feature map. The filter then slides one step right (stride = 1), repeats the operation, and continues across and down the image.

**Calculating Output Feature Map Size:**

The output size formula is:

$$O = \frac{I - F + 2P}{S} + 1$$

Where:
- `I` = Input size (5)
- `F` = Filter size (3)
- `P` = Padding (default = 0, no padding)
- `S` = Stride (default = 1)

Without padding, stride = 1:

$$O = \frac{5 - 3 + 2(0)}{1} + 1 = \frac{2}{1} + 1 = 3$$

**Output feature map size = 3×3**

**Role of Stride:**

Stride determines how many pixels the filter moves at each step.

- **Stride = 1**: Filter moves one pixel at a time → Output is `3×3` (for 5×5 input, 3×3 filter)
- **Stride = 2**: Filter jumps 2 pixels → Output is `(5-3)/2 + 1 = 2`

Larger strides reduce the output size more aggressively, making the computation faster but losing spatial resolution.

**Role of Padding:**

Padding adds extra rows/columns of zeros around the input border.

- **No padding (valid padding)**: Input 5×5, filter 3×3 → Output 3×3. Spatial dimensions shrink. Pixels at the border are processed fewer times.
- **Same padding (zero padding = 1)**: Input 5×5, filter 3×3, P=1 → Output = `(5-3+2)/1 + 1 = 5`. Output size equals input size. Preserves spatial dimensions and ensures border pixels are processed equally.

**Example with padding P=1, stride S=1:**

$$O = \frac{5 - 3 + 2(1)}{1} + 1 = \frac{4}{1} + 1 = 5$$

Output = **5×5** — same as input. This is called "same" padding and is commonly used in deep networks to prevent rapid spatial shrinking.

---

### Q4. You are building a system to predict the next word in long English sentences. Justify how an LSTM helps solve the vanishing gradient problem and retains long-term dependencies. Describe the three gates with their function.

*(This question is identical to Paper 2, Q3. The complete answer is provided above in Paper 2 Q3.)*

**Summary for Next-Word Prediction Context:**

For a sentence like *"The student who missed all lectures and submitted no assignments still expected to pass the..."*, a standard RNN would forget "student" by the time it reaches "pass the ___", because gradients vanish over many time steps.

The LSTM:
- **Forget Gate** keeps relevant long-range context (the subject "student") and erases irrelevant details
- **Input Gate** writes new information at each step (e.g., "missed", "submitted", "expected")
- **Output Gate** exposes the relevant memory at the prediction step (the subject and verb context to predict "exam" or "course")

The additive cell state update (`Ct = Ct-1 ⊙ ft + it ⊙ ĉt`) ensures gradients can flow backwards without exponential decay, making long-range next-word prediction possible.

---

### Q5. Show the application of Variational Autoencoders (VAEs) in dimensionality reduction. Illustrate its differences from the Denoising Autoencoder with a suitable example.

**VAE for Dimensionality Reduction:**

A VAE compresses high-dimensional data into a low-dimensional latent space while learning a smooth, structured representation. Unlike PCA (linear method), VAE can capture non-linear structure in data.

**Process:**

1. Input high-dimensional data `x` (e.g., a 28×28=784-dimensional MNIST image)
2. Encoder maps it to mean `μ` and log-variance `log σ²` — two vectors of the desired latent size (e.g., 2D)
3. Sample a latent vector using the reparameterisation trick: add scaled random noise to the mean, producing a point in the latent space that is slightly different each time but still centred around the encoder’s output.
4. Decoder reconstructs `x̂` from `z`
5. Loss = Reconstruction loss + KL divergence (regularises the latent space to be Gaussian)

**Application — MNIST Digit Compression:**

```
784-dim image → Encoder → z (2D latent code) → Decoder → 784-dim reconstruction
```

When you plot the 2D latent codes of all test images, digits naturally cluster by class (0–9) in a continuous, organised manifold. You can sample any point in the 2D space and decode it to generate a new digit that smoothly interpolates between digit classes.

This is dimensionality reduction from 784 → 2 dimensions while preserving the structure of the data.

**Comparison — VAE vs Denoising Autoencoder (DAE):**

| Aspect                     | Variational Autoencoder (VAE)                                 | Denoising Autoencoder (DAE)                                         |        |     |
| -------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- | ------ | --- |
| **Core Goal**              | Learn a structured probabilistic latent space for generation  | Learn robust features by reconstructing clean data from noisy input |        |     |
| **Encoder Output**         | Mean `μ` and variance `σ²` — a Gaussian distribution          | A fixed latent code (deterministic)                                 |        |     |
| **Latent Space**           | Continuous, smooth, organised — enables sampling              | Not structured for sampling; just a compressed representation       |        |     |
| **Training Input**         | Clean data                                                    | Corrupted/noisy data: `x̃ = x + noise`                              |        |     |
| **Training Target**        | Reconstruct the original `x`                                  | Reconstruct the clean original `x`                                  |        |     |
| **Loss Function**          | Reconstruction loss + KL divergence                           | Only reconstruction loss: `                                         | x - x̂ | ²`  |
| **Can Generate New Data?** | Yes — sample `z ~ N(0,1)` → Decoder → new data                | No — not designed for generation                                    |        |     |
| **Application**            | Image generation, data augmentation, dimensionality reduction | Noise removal in images, robust feature learning                    |        |     |
| **Regularisation**         | KL divergence forces Gaussian posterior                       | Noise injection forces learning structure, not noise                |        |     |

**Example:**

- **VAE**: Given 5000 face images, the VAE learns a 2D latent space. Sampling the point `z = (0.5, 0.3)` generates a new realistic face that never existed in the training set.
- **DAE**: Given clean face images, Gaussian noise is added. The model learns to reconstruct clean faces from noisy ones. If a security camera captures blurry faces, the DAE can clean them up — but it cannot generate new faces.

---

### Q6. "GANs enhance medical diagnostics by generating high-quality synthetic medical images." Elucidate the detailed architecture of GAN and its various types used in applications.

**Detailed GAN Architecture:**

A GAN consists of two neural networks that compete against each other in an adversarial training process:

**Generator (G):**
- Takes random noise vector `z` as input (sampled from a prior distribution like Gaussian)
- Passes it through transposed convolutional (upsampling) layers to generate a synthetic image
- Goal: produce images so realistic that the Discriminator cannot distinguish them from real images
- No access to real data during its forward pass

**Discriminator (D):**
- Takes an image as input (either real from the dataset or fake from Generator)
- Passes it through convolutional layers, pooling, and a final sigmoid neuron
- Outputs a probability `D(x) ∈ [0,1]` — close to 1 for real, close to 0 for fake
- Goal: correctly classify real and fake images

**Adversarial Objective (Minimax Game):**

The Discriminator tries to maximise its ability to tell real from fake. The Generator tries to minimise this — producing images so convincing that the Discriminator marks them as real. This competition is called a minimax game and both networks improve each other through it.

- Discriminator is trained to correctly label real images as real and generated images as fake
- Generator is trained to produce images that fool the Discriminator into labelling them as real

**Training Process:**

1. Initialise G and D with random weights
2. Train D: Feed real images (label=1) and fake images from G (label=0); update D weights
3. Train G: Generate fake images; update G weights to maximise `D(G(z))` (fool D)
4. Alternate steps 2 and 3 for many iterations until equilibrium

**Types of GANs and Their Applications:**

**1. Vanilla GAN (Standard GAN):**
- Original architecture — one generator, one discriminator
- Application: Basic image synthesis, data augmentation for small datasets

**2. Conditional GAN (cGAN):**
- Both G and D receive a conditioning label (e.g., class label or target image)
- G generates class-specific images: "generate an X-ray showing pneumonia"
- Application: Generating MRI or CT scans of specific diseases for training diagnostic models

**3. Pix2Pix:**
- Conditional GAN for paired image-to-image translation using U-Net as Generator
- Application: MRI → CT synthesis (generates CT scans from MRI scans, reducing patient radiation)

**4. CycleGAN:**
- Unpaired image-to-image translation using cycle consistency loss
- Application: Converting low-quality microscopy images to high-quality; style transfer between imaging modalities

**5. DCGAN (Deep Convolutional GAN):**
- Uses convolutional layers instead of Dense layers in both G and D
- More stable training, higher image quality
- Application: Generating synthetic histopathology slides for training cancer detection models

**6. Wasserstein GAN (WGAN):**
- Uses Wasserstein distance instead of JS divergence as the loss metric
- Solves mode collapse and training instability
- Application: Generating diverse synthetic medical images without mode collapse

**7. StyleGAN / StyleGAN2:**
- Style-based generator that controls image generation at different scales
- Produces photorealistic, highly detailed images
- Application: Generating synthetic patient face images for privacy-preserving datasets; virtual histology

**GANs in Medical Diagnostics — How They Help:**

1. **Data Augmentation** — Medical datasets are small and expensive to label. GANs generate synthetic MRI, CT, X-ray, and retinal images to balance class distributions (e.g., generating more rare-disease examples).

2. **Privacy-Preserving Datasets** — Real patient images contain identifiable information. GAN-generated synthetic images can share the statistical properties of real data without revealing any actual patient.

3. **Cross-Modality Translation** — Pix2Pix and CycleGAN translate between imaging modalities (MRI ↔ CT), reducing the need for expensive multi-modal scans on every patient.

4. **Disease Simulation** — Generating images with specific pathological features (tumours, lesions) helps train detection models even when real cases are scarce.

---

### Q7. With a neat sketch, explain the role of Visual QA and Visual Dialog with real-time scenarios. Also describe Pixel RNN for the learning process.

**Visual Question Answering (VQA):**

VQA is an AI task where the system receives an image and a natural language question and generates a text answer. It combines Computer Vision, NLP, and Reasoning.

**Architecture:**

```
      Image Input          Question Input
          ↓                     ↓
   Image Encoder           Question Encoder
   (CNN / ViT)          (LSTM / Transformer)
          ↓                     ↓
   Image Features       Question Embeddings
              ↓         ↓
           Cross-Attention / Feature Fusion
                    ↓
              Reasoning Layer
                    ↓
            Answer Prediction
        (Classification / Text Generation)
```

**Real-Time Scenarios:**

- **Education**: A student uploads a photo of a chemistry equation. The VQA system answers "What type of reaction is this?" → "Oxidation-Reduction"
- **Healthcare**: A doctor uploads an MRI scan. The system answers "Is there any visible anomaly?" → "Possible lesion in the frontal lobe"
- **E-Commerce**: A user uploads a product photo. System answers "Does this shirt have pockets?" → "Yes, two side pockets"
- **Accessibility**: A visually impaired user photos a document. System answers "What is the title of the document?" → "Annual Financial Report 2025"

---

**Visual Dialog (VisDial):**

Visual Dialog extends VQA to multi-turn conversation — the model answers a sequence of related questions about the same image while remembering previous dialogue.

**Architecture:**

```
     Image + Dialog History + Current Question
          ↓              ↓              ↓
   Image Encoder  History Encoder  Question Encoder
          ↓              ↓              ↓
              Multimodal Fusion (Cross-Attention)
                         ↓
                     Reasoning
                         ↓
                  Answer Decoder
                         ↓
                   Final Answer
```

**Example Real-Time Scenario — Robotic Assistant:**

Given an image of a kitchen:
- Q1: "What room is this?" → A1: "Kitchen"
- Q2: "What is on the counter?" → A2: "A cutting board and vegetables"
- Q3: "Is the stove on?" → A3: "No, the burners are off"
- Q4: "Is there anyone there?" → A4: "Yes, a person near the sink" ← uses full conversation history to answer in context

**Key difference from VQA**: Visual Dialog must remember Q1, A1, Q2, A2... to give contextually aware answers to each new question. This makes it suitable for smart home assistants, interactive robots, and educational tutoring systems.

---

**Pixel RNN — Learning Process:**

Pixel RNN is a generative model that generates images pixel by pixel in a sequential order, using the context of all previously generated pixels to predict the next one.

**Core Idea:**

An image is treated as a sequence of pixels read in order — left to right, top to bottom (raster scan order). Each pixel is predicted using all the pixels that came before it. This is exactly like next-word prediction in language models: just as a model predicts the next word given all previous words, Pixel RNN predicts the next pixel given all previous pixels.

This is an auto-regressive model — each step depends on the outputs of all previous steps.

**Architecture:**

Two main variants:
- **Row LSTM**: Processes the image row by row using an LSTM; captures context along each row
- **Diagonal BiLSTM**: Processes diagonals of the image in both directions; captures context from all above and left pixels

Each LSTM cell receives the previously generated pixel value as input and outputs a probability distribution over the 256 possible intensity values (0–255) for the next pixel.

**Learning Process:**

1. During training, real images are used. The model is given the true pixel at position `i` and trained to predict pixel at position `i+1` (teacher forcing).
2. Cross-entropy loss is computed between the predicted pixel distribution and the actual pixel value.
3. Gradients backpropagate through the LSTM chain to update weights.
4. At inference time, pixels are sampled sequentially — each generated pixel is fed back as input to generate the next.

**Application in Real-Time:**

- **Image completion** — Given the top half of an image, Pixel RNN generates the bottom half pixel by pixel
- **Image synthesis** — Generates new, realistic images from scratch without needing a discriminator (unlike GAN)
- **Anomaly detection** — Pixels that are unlikely given their context (high cross-entropy) indicate anomalies

**Limitation:** Very slow at generation time because pixels must be generated strictly sequentially — this is the main practical drawback compared to GANs, which generate entire images in one forward pass.

---

*End of Answer Sheet — All answers derived primarily from course notes (M1–M5). Additional content provided for Adam optimizer, BERT fine-tuning, BiLSTM, CycleGAN details, Pixel RNN, and KL divergence where notes were insufficient.*
