# Unit 3 & 4 — Question Bank
**(5 × 20 = 100 Marks) | Answer any 5 Questions**

---

## Q1. Ex-OR Problem using Multi-Layer Neural Network *(20 Marks, BL 3)*

> "You decide to use a multi-layer neural network with one hidden layer to solve the Ex-OR problem". Specify the activation function and number of neurons required in the hidden layer to solve the Ex-OR problem. Why is non-linearity important in this context?

### The Ex-OR Problem

The XOR (Exclusive-OR) truth table is:

| X1 | X2 | Output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR is **not linearly separable** — no single straight line can separate the 0s from the 1s in 2D space. A single-layer perceptron (which only draws linear boundaries) **cannot** solve it. A hidden layer with non-linear activation is required.

### Architecture

- **Input Layer**: 2 neurons (X1 and X2)
- **Hidden Layer**: **2 neurons** with **Sigmoid activation**
- **Output Layer**: 1 neuron with Sigmoid activation

**Why 2 neurons in the hidden layer?**  
Each hidden neuron learns one linear boundary (like a half-plane). Two such boundaries together define a region that correctly separates XOR outputs. One neuron detects "at least one input is 1"; the other detects "both inputs are 1". The output neuron combines them to implement XOR.

### Activation Function

**Sigmoid** is used: $\sigma(x) = \frac{1}{1 + e^{-x}}$

Output range: $(0, 1)$ — perfect for binary classification. Alternatively, **ReLU** ($\max(0,x)$) can be used in the hidden layer for faster training, with Sigmoid in the output layer.

### Why Non-Linearity is Essential

Without a non-linear activation function, every layer of a neural network performs only a **linear transformation**. Stacking multiple linear layers is mathematically equivalent to a single linear layer — regardless of depth, the network can only learn linear decision boundaries.

XOR output cannot be separated by any line, plane, or hyperplane. A non-linear activation function **bends and warps the feature space**, allowing the network to create curved or piecewise decision boundaries that can separate XOR.

| Model | Activation | Can solve XOR? |
|---|---|---|
| Single-layer perceptron | None / Linear | ✗ No |
| Multi-layer (1 hidden) | Linear | ✗ No |
| Multi-layer (1 hidden) | Sigmoid / ReLU | ✓ Yes |

> **Conclusion:** At least **2 hidden neurons** with **Sigmoid (or ReLU)** activation are required. Non-linearity transforms the input space so that XOR becomes linearly separable in the hidden representation — this is the fundamental power of multi-layer neural networks.

---

## Q2. Underfitting Analysis and Solutions *(20 Marks, BL 4)*

> Training a neural network on a complex dataset shows high training and validation errors, indicating underfitting. Analyze potential reasons for underfitting related to model complexity, activation functions, and learning rate.

### What is Underfitting?

Underfitting occurs when the model is **too simple** to capture the underlying patterns in the data. Both training and validation loss remain high — the model has not learned even the training data adequately.

### Causes of Underfitting

**1. Insufficient Model Complexity**
- Too few hidden layers — the network cannot learn hierarchical or non-linear patterns
- Too few neurons per layer — the representational capacity is too low
- The model is essentially a linear classifier trying to learn a non-linear problem

**2. Poor Activation Functions**
- Using a **linear activation** throughout — no non-linearity means the model collapses to a linear transformation regardless of depth
- **Sigmoid/Tanh** in deep networks can cause vanishing gradients in early layers, effectively making those layers stop learning

**3. Low Learning Rate**
- The optimizer takes very small steps during gradient descent
- Weights update so slowly that the model barely converges within the training budget
- Training loss may decrease, but extremely slowly — it appears "stuck" at a high error

**4. Insufficient Training (Epochs)**
- The model hasn't been exposed to the data long enough to learn the patterns

**5. Over-regularization**
- Excessive dropout or L2 regularization penalizes the model too heavily, preventing it from even fitting the training data

### Architectural Modifications to Fix Underfitting

| Modification | Effect |
|---|---|
| Add more hidden layers | Enables learning of deeper, more abstract feature hierarchies |
| Increase neurons per layer | More parameters → greater representational capacity |
| Switch to ReLU / Leaky ReLU | Avoids vanishing gradients; allows gradients to flow effectively in deep networks |
| Remove or reduce regularization | Allows the model to fit the training data more closely |
| Add Batch Normalization | Stabilizes training, allows higher learning rates, speeds convergence |

### Effect of Increasing Learning Rate

A higher learning rate causes the optimizer to take **larger steps** in the direction of the gradient:

- **Positive effect**: The model learns faster and reaches lower loss values in fewer epochs — can help escape underfitting
- **Risk**: If the learning rate is too high, the optimizer may overshoot the minimum and diverge, causing training to become unstable

**Practical recommendation:** Use a **learning rate scheduler** (e.g., reduce on plateau) or **adaptive optimizers** like Adam, which automatically adjust the effective learning rate per parameter. Start with a moderate rate (e.g., 0.001) and increase if convergence is too slow.

> **Summary:** Underfitting is a problem of insufficient capacity or insufficient training. Fix it by building a deeper/wider network, switching to better activations (ReLU), and ensuring the learning rate is high enough to actually learn from the data.

---

## Q3. Convolution Operation on a 5×5 Image with a 3×3 Filter *(20 Marks, BL 3)*

> Consider a 5×5 grayscale image and a 3×3 filter. Describe how the convolution operation is performed and calculate the size of the output feature map. Explain the role of stride and padding.

### The Convolution Operation

Convolution is the core operation in a CNN. A small **filter (kernel)** slides across the input image, computing an **element-wise multiplication** at each position and summing the results to produce one value in the output **feature map**.

**Example: 5×5 input, 3×3 filter, Stride = 1, No Padding**

```
Input (5×5):               Filter (3×3):
  1  2  3  4  5             1  0 -1
  5  4  3  2  1             1  0 -1
  2  1  0  1  2             1  0 -1
  3  2  1  0  1
  4  3  2  1  0
```

At position (0,0), the filter covers the top-left 3×3 patch:

```
Patch:    1  2  3       Filter:   1  0 -1
          5  4  3                 1  0 -1
          2  1  0                 1  0 -1

Output value = (1×1)+(2×0)+(3×-1) + (5×1)+(4×0)+(3×-1) + (2×1)+(1×0)+(0×-1)
             = (1 + 0 - 3) + (5 + 0 - 3) + (2 + 0 - 0)
             = -2 + 2 + 2 = 2
```

The filter shifts one step right, computes the next value, and so on — producing a complete feature map.

### Output Size Formula

$$\text{Output Size} = \frac{W - F + 2P}{S} + 1$$

Where:
- $W$ = Input size
- $F$ = Filter size
- $P$ = Padding
- $S$ = Stride

**For our example** (W=5, F=3, P=0, S=1):

$$\text{Output} = \frac{5 - 3 + 0}{1} + 1 = 2 + 1 = 3$$

**Output feature map size = 3×3**

### Role of Stride

**Stride** controls how many pixels the filter moves at each step.

| Stride | Output size (5×5 input, 3×3 filter, P=0) | Effect |
|---|---|---|
| S = 1 | $\frac{5-3}{1}+1 = 3$ → **3×3** | Fine-grained, captures more positions |
| S = 2 | $\frac{5-3}{2}+1 = 2$ → **2×2** | Coarser, downsamples the feature map |

A larger stride downsamples the spatial dimensions, reducing computational cost but potentially missing detail.

### Role of Padding

**Padding** adds extra rows/columns (usually zeros) around the input before convolution.

**Zero Padding (P=1) on 5×5 input becomes 7×7:**

$$\text{Output} = \frac{5 - 3 + 2(1)}{1} + 1 = \frac{4}{1} + 1 = 5$$

Output size = **5×5** — same as input! This is called **"same" padding** — it preserves spatial dimensions.

| Padding | P=0 (valid) | P=1 (same) |
|---|---|---|
| Output (5×5, 3×3 filter, S=1) | 3×3 | 5×5 |
| Use case | Reduce size intentionally | Preserve size across layers |

> **Summary:** Convolution applies a sliding filter over the input, computing local dot products. Output size = $(W - F + 2P)/S + 1$. Stride controls downsampling speed; padding controls whether the spatial dimensions shrink.

---

## Q4. LSTM — Vanishing Gradient Solution and Three Gates *(20 Marks, BL 4)*

> "You are building a system to predict the next word in long English sentences". Justify how an LSTM helps solve the vanishing gradient problem and retains long-term dependencies. Describe the three gates of an LSTM with their function.

### The Problem: Vanishing Gradients in RNNs

In a standard RNN, training requires **Backpropagation Through Time (BPTT)**. The gradient of the loss must flow backwards through every time step, multiplying by the weight matrix $W$ at each step:

$$\frac{dLoss}{dW} = \frac{dLoss}{dO_{t+3}} \cdot \frac{dO_{t+3}}{dS_{t+3}} \cdot W \cdot W \cdot W \cdot \frac{dS_t}{dW}$$

- If $|W| < 1$ → gradients **vanish** → early words contribute nothing to learning
- If $|W| > 1$ → gradients **explode** → training diverges

For next-word prediction in long sentences (e.g., 50+ words), the RNN forgets the beginning of the sentence entirely. Words like *"The"* or *"She"* at the start have zero influence on the prediction at the end.

### How LSTM Solves This

LSTM introduces a **cell state** $C_t$ — a separate memory highway that runs through the entire sequence. The gradient through the cell state is:

$$\frac{dC_t}{dC_{t-1}} = f_t + \frac{d(i_t \cdot \hat{c}_t)}{dC_{t-1}}$$

Unlike the RNN (which always multiplies by the same $W$), this term is **different at every time step** and is controlled by the forget gate $f_t$ which the model **learns**. The model can learn to keep $f_t \approx 1$ when important information must be preserved — allowing gradients to flow back across many steps without vanishing.

### The Three Gates

#### 1. Forget Gate — "What to erase from long-term memory"

$$f_t = \sigma(U_f X_t + W_f h_{t-1})$$

- Takes current input $X_t$ and previous hidden state $h_{t-1}$
- Sigmoid output in $[0, 1]$: **0 = forget completely, 1 = keep completely**
- Applied element-wise to the previous cell state $C_{t-1}$

*Example:* While predicting the next word in *"The cat sat..."*, the forget gate can erase information about a topic mentioned many words ago if it's no longer relevant.

#### 2. Input Gate — "What new information to write"

Works in two parallel steps:

$$i_t = \sigma(U_i X_t + W_i h_{t-1}) \quad \text{(how much to write, } [0,1]\text{)}$$
$$\hat{c}_t = \tanh(U_c X_t + W_c h_{t-1}) \quad \text{(what to write, } [-1,1]\text{)}$$

The actual update is: $i_t \odot \hat{c}_t$ — gating the candidate values by the input gate

*Example:* When a new subject is introduced in the sentence, the input gate writes the new subject's identity into the cell state.

#### 3. Output Gate — "What to expose as the hidden state"

$$o_t = \sigma(U_o X_t + W_o h_{t-1})$$
$$h_t = o_t \odot \tanh(C_t)$$

- Decides which parts of the updated cell state $C_t$ to surface as the hidden state $h_t$
- $h_t$ is both passed to the output layer and looped back to the next step

*Example:* Even if the cell state holds a lot of stored information, the output gate filters what is relevant *right now* for predicting the next word.

### Cell State Update (Full Step)

$$C_t = C_{t-1} \odot f_t + i_t \odot \hat{c}_t$$

| Step | Operation | Meaning |
|---|---|---|
| $C_{t-1} \odot f_t$ | Forget | Erase irrelevant old memory |
| $i_t \odot \hat{c}_t$ | Input | Add relevant new information |
| $C_t$ | New cell state | Updated long-term memory |

> **Conclusion:** LSTM solves the vanishing gradient problem through the cell state highway — gradients flow back through $C_t$ with variable, learned scaling factors rather than repeated multiplication by a fixed $W$. The three gates (forget, input, output) give the model fine-grained control over what to remember, write, and read at every step, enabling it to retain context across hundreds of words.

---

## Q5. Variational Autoencoders vs Denoising Autoencoders *(20 Marks, BL 3)*

> Show the application of Variational auto-encoders in dimensionality reduction of data. Illustrate its differences from the denoising auto-encoder with a suitable example.

### Autoencoders — Background

An **Autoencoder** is a neural network that learns a compressed representation of data (encoding) and then reconstructs the original data from it (decoding). It has two parts:

```
Input X  →  [Encoder]  →  Latent z (compressed)  →  [Decoder]  →  Reconstructed X'
```

The bottleneck (latent space) forces the model to learn only the most essential features.

---

### Variational Autoencoder (VAE)

A **VAE** is a generative model that learns a **probabilistic latent space**. Instead of encoding the input to a fixed point, the encoder outputs a **mean** $\mu$ and **variance** $\sigma^2$, and the latent vector $z$ is sampled from the distribution $\mathcal{N}(\mu, \sigma^2)$.

**Architecture:**

```
Input X  →  [Encoder]  →  μ, σ²  →  z ~ N(μ, σ²)  →  [Decoder]  →  X'
```

**Loss Function:**

$$\mathcal{L} = \underbrace{\|X - X'\|^2}_{\text{Reconstruction loss}} + \underbrace{D_{KL}(\mathcal{N}(\mu, \sigma^2) \| \mathcal{N}(0, 1))}_{\text{KL Divergence (regularization)}}$$

The KL Divergence term forces the latent space to be smooth and continuous — nearby points in latent space decode to similar outputs.

**Application in Dimensionality Reduction:**

VAEs can compress high-dimensional data (e.g., 28×28 = 784-dimensional MNIST images) into a low-dimensional latent space (e.g., 2D or 10D) while preserving structure:
- Points in the latent space that are close together correspond to visually similar images
- You can interpolate between two images in latent space and generate meaningful intermediate images
- The continuous latent space allows **generating new data** by sampling random $z \sim \mathcal{N}(0, 1)$

*Example:* A VAE trained on face images maps all faces to a 64-dimensional latent space. The dimensions might encode attributes like age, gender, hair color. Changing one dimension gradually changes only that attribute in the reconstructed face.

---

### Denoising Autoencoder (DAE)

A **DAE** takes a **corrupted/noisy version** of the input and learns to reconstruct the **clean original**.

```
Clean X  →  Add noise  →  Corrupted X̃  →  [Encoder]  →  z  →  [Decoder]  →  X' ≈ X
```

**Loss:** $\|X - X'\|^2$ — minimize the difference between the clean input and reconstruction from the noisy version.

The model is forced to learn **robust representations** that capture the true signal rather than noise.

*Example:* A DAE trained on handwritten digits receives digit images with random pixel dropout (30% pixels set to 0). The network learns to fill in missing pixels and reconstruct the complete digit correctly.

---

### VAE vs Denoising Autoencoder — Comparison

| Feature | Variational Autoencoder (VAE) | Denoising Autoencoder (DAE) |
|---|---|---|
| **Goal** | Learn a generative, smooth latent space | Learn robust, noise-invariant features |
| **Input** | Clean data | Corrupted/noisy version of data |
| **Latent space** | Probabilistic: $z \sim \mathcal{N}(\mu, \sigma^2)$ | Deterministic: fixed latent vector |
| **Can generate new data?** | ✓ Yes — sample from $\mathcal{N}(0,1)$ and decode | ✗ No |
| **Loss function** | Reconstruction + KL Divergence | Reconstruction only |
| **Use cases** | Generative modeling, image synthesis, interpolation, dimensionality reduction | Denoising, feature learning, anomaly detection |
| **Example** | Generate new face images by sampling latent space | Reconstruct a corrupted MRI scan |

> **Conclusion:** VAEs learn a structured, continuous latent space suitable for generation and meaningful dimensionality reduction — two points close in latent space give similar decoded outputs. DAEs learn noise robustness by training on corrupted inputs, making them better for feature extraction and denoising tasks but not for generation.

---

## Q6. GAN Architecture and Applications in Medical Imaging *(20 Marks, BL 4)*

> Statement: "GANs enhance medical diagnostics by generating high-quality synthetic medical images". Elucidate the detailed architecture of GAN and its various types of networks used in applications.

### What is a GAN?

A **Generative Adversarial Network (GAN)** consists of two neural networks trained simultaneously in an adversarial game:

- **Generator (G)**: Creates fake data from random noise, trying to fool the discriminator
- **Discriminator (D)**: Distinguishes between real and fake data

```
Random Noise z  →  [Generator G]  →  Fake Image
                                          ↓
Real Images   ──────────────────→  [Discriminator D]  →  Real / Fake
```

### Detailed Architecture

**Generator:**
- Input: Random noise vector $z \sim \mathcal{N}(0, 1)$ (e.g., 100-dimensional)
- Architecture: Fully connected or transposed convolutional layers (upsampling)
- Output: Synthetic data (e.g., a 256×256 RGB image)
- Activation: ReLU in hidden layers, Tanh in output layer

**Discriminator:**
- Input: Either a real image (from training set) or a fake image (from Generator)
- Architecture: Convolutional layers followed by fully connected layers
- Output: Single scalar probability — 1 = real, 0 = fake
- Activation: LeakyReLU in hidden layers, Sigmoid in output

### Training Objective (Minimax Game)

$$\min_G \max_D \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$

- Discriminator maximizes its ability to detect fakes
- Generator minimizes the discriminator's ability — tries to generate images $G(z)$ such that $D(G(z)) \approx 1$

Training alternates: one step updates $D$, the next updates $G$.

### Types of GANs and Applications

| GAN Type | Key Innovation | Application |
|---|---|---|
| **DCGAN** (Deep Convolutional GAN) | Uses conv/deconv layers instead of fully connected | High-quality image generation |
| **CGAN** (Conditional GAN) | Generator and Discriminator conditioned on class label $y$ | Targeted generation — generate only "lung X-ray" or "chest CT" |
| **CycleGAN** | Unpaired image-to-image translation | MRI → CT conversion without paired training data |
| **StyleGAN** | Controls style at different scales of generation | Photorealistic face synthesis |
| **Pix2Pix** | Paired image-to-image translation | Sketch → realistic image |
| **WGAN** (Wasserstein GAN) | Uses Wasserstein distance for stable training | More stable training, avoids mode collapse |

### Medical Imaging Applications

**1. Synthetic Data Generation:**  
Medical datasets are small and expensive to label. GANs generate synthetic MRI, CT, and X-ray images to augment training data — reducing the need for real patient data and preserving privacy.

**2. Disease-Specific Image Generation (CGAN):**  
A Conditional GAN can be trained to generate images conditioned on disease type (e.g., "generate a chest X-ray with pneumonia"). This provides diverse, labeled training examples for diagnostic classifiers.

**3. Image-to-Image Translation (CycleGAN):**  
Translate MRI scans to CT scans (or vice versa) without paired training examples — useful when one modality is expensive or unavailable.

**4. Data Balancing:**  
Medical datasets are often imbalanced (far fewer diseased cases than normal). GANs oversample the rare class with realistic synthetic examples.

> **Conclusion:** GANs are powerful generative tools that have found significant application in medical imaging. The adversarial training forces the generator to produce highly realistic images. Conditional variants (CGAN, Pix2Pix, CycleGAN) extend this to targeted generation, making them particularly useful in medical AI where labeled, diverse data is scarce.

---

## Q7. Visual QA, Visual Dialog, and Pixel RNN *(20 Marks, BL 2)*

> With a neat sketch, explain about the role of Visual QA and Visual Dialog with real time scenarios. Also describe the Pixel RNN for the learning process.

### Visual Question Answering (VQA)

**Visual QA** is a task where a model is given an **image** and a **natural language question** about that image, and must produce a **natural language answer**.

**Architecture:**

```
Image  →  [CNN Encoder]  →  Visual Features (v)
                                     ↓
Question  →  [LSTM/Transformer]  →  Text Features (q)
                                     ↓
                          [Attention / Fusion Layer]
                          (align visual & text features)
                                     ↓
                          [Dense + Softmax]
                                     ↓
                               Answer ("Yes" / "Red" / "3")
```

**Key Components:**
- **CNN** extracts spatial feature maps from the image
- **LSTM or Transformer** encodes the question into a vector
- **Attention mechanism** helps the model focus on the relevant image regions when answering (e.g., for "What color is the car?", attend to the car region)
- **Output layer** predicts the answer from a fixed vocabulary or generates it as text

**Real-time Scenarios:**
- **Medical imaging**: "Does this chest X-ray show any abnormalities?" — helps radiologists triage scans
- **Accessibility (visually impaired)**: A smartphone camera takes a photo, the user asks "What is in front of me?" and the system answers verbally
- **Autonomous vehicles**: "Is there a pedestrian at the crossing?" — real-time perception queries
- **E-commerce**: "What color is this product?" or "What brand logo is shown?"

---

### Visual Dialog

**Visual Dialog** extends VQA to a **multi-turn conversation** about an image. The model must maintain the history of the dialogue and answer each new question in context.

**Architecture:**

```
Image  →  [CNN]  →  v (visual features)
                           ↓
Question_t + History  →  [LSTM / Transformer]  →  [Fusion]  →  Answer_t
   (current Q)    (Q1, A1, Q2, A2, ...)
```

**Difference from VQA:** Each answer is conditioned not just on the image + current question, but on all previous question-answer pairs (dialogue history). This requires the model to maintain **context** across turns.

**Real-time Scenarios:**
- **Customer support chatbot with product image**: User sends a photo of a product and has a multi-turn conversation — "What is this?" → "Is it available in blue?" → "How do I assemble it?"
- **Medical consultation**: Doctor uploads an X-ray and asks follow-up questions about different regions — the model responds coherently across the conversation
- **Robots and assistants**: A home robot receives an image from its camera and engages in conversation about what it sees

---

### Pixel RNN

**Pixel RNN** is a generative model that generates images **one pixel at a time**, treating image generation as a sequential prediction problem.

**Core Idea:**  
Each pixel is conditioned on all previously generated pixels:

$$P(x) = \prod_{i=1}^{n^2} P(x_i \mid x_1, x_2, \ldots, x_{i-1})$$

The model generates pixel $x_i$ using an RNN that processes all pixels from left-to-right and top-to-bottom.

**Architecture (Row LSTM / Diagonal BiLSTM):**

```
Pixel (0,0) → Pixel (0,1) → Pixel (0,2) → ...
                                              ↓
               Pixel (1,0) → Pixel (1,1) → ...
                                              ↓
                              ...each pixel generated autoregressively
```

For each pixel position $(i, j)$:
- The LSTM hidden state encodes all pixels above and to the left
- The model predicts the intensity (or RGB values) of the next pixel using a softmax over 256 values
- The generated value is fed back as input for the next step

**Learning Process:**
1. Train on real images using maximum likelihood — maximize $\log P(x)$ over the dataset
2. At each step, the model sees the true pixel (teacher forcing during training) and learns to predict the next one
3. At inference, pixels are generated one at a time — each generated pixel is fed in to predict the next

**Variants:**
- **Row LSTM**: Uses a row-by-row LSTM — fast but captures only limited context
- **Diagonal BiLSTM**: Scans diagonally, capturing context from all directions — more powerful but slower
- **PixelCNN**: Replaces the RNN with masked convolutions for faster, parallelizable training

**Applications:**
- Image generation and completion (fill in missing parts of an image)
- Image compression (learn the natural pixel distribution)
- Density estimation (assign likelihood to images — useful for anomaly detection)

> **Summary:** Pixel RNN treats an image as a sequence of pixels and learns to model their joint probability autoregressively. Though slow at generation (must generate pixel-by-pixel), it produces very high-quality, coherent images because it conditions every pixel on all preceding context.
