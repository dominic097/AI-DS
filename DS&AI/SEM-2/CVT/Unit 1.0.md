# Introduction to Computer Vision
- is a field of artificial intelligence that enables computers to interpret and understand visual information from the world, such as images and videos. 

- It involves the development of algorithms and techniques that allow machines to analyze, process, and make decisions based on visual data. 

- Computer vision has applications in various domains, including image recognition, object detection, facial recognition, autonomous vehicles, medical imaging, and more. The goal of computer vision is to enable machines to see and understand the visual world in a way that is similar to human vision.

# Common Computer Vision Tasks
- Image Classification: Assigning a label or category to an entire image based on its content.

- Object Detection: Identifying and locating specific objects within an image, often by drawing bounding boxes.
- Image Segmentation: Dividing an image into multiple segments/regions to separate objects/areas.
- Facial Recognition: Identifying and verifying individuals based on facial features.
- Optical Character Recognition (OCR): Converting images of text into machine-readable text.
- Motion Detection: Detecting and tracking moving objects in video sequences.

---

# Image Representation - Gray

## 1. Grayscale Conversion

### What it does
- Converts a color image (**RGB: 3 channels**) into **grayscale (1 channel)**.
- Output pixel value represents **brightness/intensity** only.

### Why we use it
- **Less computation + memory:** 1 value/pixel instead of 3.
- Many algorithms depend mainly on **intensity changes** (edges/texture), not color.
- Makes later processing simpler (thresholding, edges, morphology, etc.).

### Helps CV how?
- Preserves structure (shapes, boundaries) while removing color distraction.
- Commonly used before: **OCR**, **face detection**, **edge detection**, **segmentation**.

### Formula (standard weighted)
$$\text{Gray} = 0.299R + 0.587G + 0.114B$$

**Why weighted?** Human eyes are most sensitive to **green**, so it gets the highest weight.

### Quick example
- A colored pixel like $(255, 0, 0)$ (pure red) becomes a single gray intensity value.

### When to use
- Use grayscale when **color is not a key feature** and speed matters.
- Keep color when **color itself** separates classes (traffic lights, fruit sorting, etc.).

---

## 2. Histogram Equalization

### What it does
- Improves **contrast** of a grayscale image.

### Problem
- Image is **too dark**, **too bright**, or **low contrast** (details hidden).

### Core idea (easy to remember)
- If many pixels lie in a small intensity range, the image looks flat.
- Histogram equalization **spreads intensities** to use the full range better.

### How it works (one-line intuition)
- Uses the **CDF (cumulative distribution)** of the histogram to remap intensities.

If intensity levels are $0..(L-1)$, a common mapping is:
$$s = (L-1)\,\text{CDF}(r)$$

### Helps CV how?
- Objects become clearer → features easier to detect.
- Often helps: **face recognition**, **medical imaging**, **night vision**.

### Note (important)
- Can also **amplify noise** in very noisy images.
- For local improvement, use **CLAHE** (adaptive histogram equalization).

---

## 3. Smoothing / Blurring

### What it does
- Reduces **noise** (random dots/grain) and small variations.

### Why
- Noise creates **false edges** and affects segmentation/detection accuracy.

### Key idea
- Replace each pixel by a value based on its **neighbors** (filtering/convolution).

### Filters used (when to pick which)
- **Mean filter:** simple averaging (smooths, but blurs edges more).
- **Gaussian blur:** weighted average (good general-purpose smoothing).
- **Median filter:** best for **salt-and-pepper** noise (preserves edges better).

### Helps CV how?
- Makes shapes cleaner; reduces unwanted details.
- Often used before: **edge detection**, **thresholding**, **segmentation**.

### Trade-off
- More blur → less noise, but also **loss of fine details/edges**.

---

## 4. Thresholding

### What it does
- Converts a grayscale image into **binary** (0 or 255).

### Why
- Separates **object** from **background**.

### Rule (most common)
$$g(x,y)=\begin{cases}
255 & f(x,y)\ge T\\
0 & f(x,y)<T
\end{cases}$$

**Inverse threshold:** swap the outputs (useful when object is darker than background).

### Helps CV how?
- Easy to: **count objects**, **detect shapes**, **detect text**.

### Example / where used
- White object on black background.
- Useful for: **OCR**, **fingerprint detection**, **document scanning**.

### Note
- If lighting changes across the image, use **adaptive thresholding** or **Otsu’s method**.

---

## 5. Edge Detection

### What it does
- Finds **boundaries of objects** (where intensity changes sharply).

### Why
- Edges capture structure (shape) → models focus on important features, not uniform areas.

### Methods
- **Sobel:** gradient-based (fast, simple).
- **Canny:** strong edge detector (less noise, thin edges).
- **Laplacian:** second-derivative method (often used with smoothing + zero-crossings).

### Canny (memory steps)
1) Blur (reduce noise)  2) Gradient  3) Non-max suppression  4) Hysteresis thresholding

### Used for
- **Shape detection**, **lane detection**, **object tracking**, **face recognition**.

---

# Basic Image Processing Techniques - Segmentation

## What is Segmentation?

### Simple meaning
- **Segmentation** = dividing an image into **meaningful parts** (regions/objects).
- Goal: **separate object pixels from background pixels**.

### Easy way to remember
- Instead of treating the image as a single block, we ask: **“Where is the object?”**
- Example idea: “Where is the tiger?” → find tiger pixels → separate from grass/sky/ground → that is segmentation.

---

## Why do we need segmentation?
- Without segmentation: computer sees only **pixels** (no object understanding).
- With segmentation: computer understands **objects/regions**.

### It helps in
- **Object detection** (better localization)
- **Counting objects**
- **Tracking** (follow object across frames)
- **Measurement** (area, perimeter, size)
- **Recognition** (classify object after isolating it)

---

## Types of Segmentation

### 1) Thresholding (Basic)
- Separates based on **intensity** (brightness).
- Example rule:
	- pixel $> 128$ → white (object)
	- pixel $< 128$ → black (background)
- Used in: **document scanning**, **OCR**.
- Notes:
	- Simple + fast
	- Limited when lighting is uneven or object/background intensities overlap

### 2) Edge-based Segmentation
- Uses **edges** to find object boundaries.
- Typical steps:
	1) Detect edges
	2) Connect edges
	3) Form/close object boundary
- Used in: **shape detection**.
- Problem: can be **noisy** (broken edges, false edges) → often needs smoothing + linking.

### 3) Region-based Segmentation
- Groups **similar pixels** into regions.
- Similarity can be based on: **color**, **texture**, **intensity**.
- Example: all green pixels → grass region.
- Used in: **medical imaging**, **satellite images**.
- Notes:
	- Works well when regions are consistent
	- Can struggle when texture/illumination varies a lot

### 4) Clustering (K-means)
- ML-based method that groups pixels automatically into $K$ clusters.
- Example: $K = 3$ → sky, grass, tiger.
- Notes:
	- Very popular baseline method
	- Needs choice of $K$; sensitive to initialization; assumes clusters are separable in feature space

### 5) Deep Learning Segmentation (Modern)
- Uses CNN models to learn segmentation directly from data.

**Types:**
- **Semantic segmentation (class-wise):** every pixel gets a class label (all cars = one “car” class).
- **Instance segmentation (object-wise):** separates different objects of same class (car #1, car #2).

**Common models:**
- **U-Net**
- **Mask R-CNN**
- **YOLO-seg**

**Used in:**
- **Self-driving cars**
- **Medical tumor detection**
- **Robotics**


