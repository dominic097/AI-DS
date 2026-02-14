# Image Processing Methods 

## 1) Spatial Domain

### Meaning
- Works **directly on image pixels** in the $(x, y)$ plane - A techniqe involves the direct manipulation of pixel values to achieve a desired effect.
- This model operates on individual pixels values and their neighboring pixels.
- An Image can be represented in the form of a 2D matrix where each elements of the matrix represnets pixel intensity value.

### Mathematical model (Spatial domain)

Spatial domain processes are denoted by:
$$g(x,y) = T\,[f(x,y)]$$

Where:
- $f(x,y)$ = **input image** (original pixel at location $(x,y)$)
- $T$ = an **operator** applied on $f$ (the processing rule)
  - $T$ can use only the pixel value at $(x,y)$ (**point operation**) OR
  - $T$ can use a **neighborhood** around $(x,y)$ (e.g., a $3\times3$ or $5\times5$ window) (**spatial filtering**)
- $g(x,y)$ = **processed/output image**

Quick link to examples:
- Point operation: $g(x,y) = f(x,y) + c$ (brightness change), thresholding
- Neighborhood operation: $g(x,y)$ = average/weighted average of neighbors (mean/Gaussian blur)

### How it works (idea)
- Apply operations on:
	- a **single pixel** (point processing), or
	- a **small neighborhood** around a pixel (spatial filtering / convolution).

### Types of Spatial Domain Methods
- **Intensity Transformation or Point operations:** 
    - Operates on single pixel values to enhance contrast, adjust brightness, or apply thresholding.
    - Applying the same transformation to each pixel in a grayscale image, based on its original pixel value and independent of its location or neighboring pixels.
    - Transformation Function of point processing  
        s = T ( r ) -> Transformation function
        - where r is the pixels of the input image and s is the pixels of the output image.
        - T is a transformation function that maps each value of r to each value of s.

- **Image Negation:**
    - Inverts the pixel values of an image, creating a negative effect.
    - For an 8-bit grayscale image, the transformation is given by:
        $$s = L - 1 - r$$
        where $L$ is the number of possible intensity levels (e.g., 256 for 8-bit images) and $r$ is the pixel value of the input image.

- **Spatial Filtering / Convolution:**
    - Uses a kernel (small matrix) to compute a new pixel value based on the neighborhood of the original pixel.
    - Common for smoothing (blurring) and sharpening.



### Example
- **Blur**: replace each pixel with the average of its neighbors.
- **Edge detection**: use Sobel/Canny to detect strong intensity changes.

### When to use
- Best when you want **simple + fast** improvements or local changes.
- Good for preprocessing: denoise → threshold → edges/segmentation.

---

## 2) Frequency Domain

### Meaning
- Works on the image in terms of **spatial frequencies** (how fast intensity changes).
- Convert image to frequency domain using **Fourier Transform**.

### Key idea
- Smooth areas → **low frequency** components.
- Edges / fine details / noise → **high frequency** components.

### Typical workflow
1) Compute Fourier transform: $F(u,v) = \mathcal{F}\{f(x,y)\}$
2) Multiply by a filter (in frequency domain): $G(u,v) = H(u,v)\,F(u,v)$
3) Inverse transform to get processed image: $g(x,y) = \mathcal{F}^{-1}\{G(u,v)\}$

### Common filters
- **Low-pass filter (LPF):** removes high frequencies → smoothing / blur.
- **High-pass filter (HPF):** keeps high frequencies → sharpening / edge enhancement.
- **Band-pass / band-stop:** keep/remove a range of frequencies.

### Example (easy to remember)
- Remove periodic noise (like stripes) by suppressing specific frequency peaks.

### When to use
- Useful when the problem is easier to describe as **frequency components**:
	- periodic noise removal
	- controlled smoothing/sharpening
	- analysis of texture patterns

---

### Quick difference (exam point)
- **Spatial domain:** change pixels directly (local operations).
- **Frequency domain:** change frequency components (global view via Fourier transform).



## Log Transformation
- **Log transformation** is a point operation that maps pixel intensity values using a logarithmic function. It is defined as:
$$s = c \cdot \log(1 + r)$$
Where:
- $s$ is the output pixel value.
- $r$ is the input pixel value.
- $c$ is a scaling constant that can be used to adjust the output intensity range.

- This transformation is particularly effective for enhancing details in dark regions of an image while compressing the intensity range of brighter areas. It is commonly used in applications such as medical imaging and remote sensing to improve the visibility of features in low-light conditions.


## Inverse Log Transformation
- The **inverse log transformation** is the reverse operation of the log transformation, defined as:
$$s = c \cdot (e^{r/c} - 1)$$
Where:
- $s$ is the output pixel value.
- $r$ is the input pixel value.

- This transformation is used to expand the intensity range of an image, particularly in cases where the log transformation has compressed the intensity values. It can be useful for enhancing details in bright regions of an image while compressing the intensity range of darker areas.

## Gamma transformation


- The **gamma transformation** is a point operation that maps pixel intensity values using a power-law function. It is defined as:
$$s = c \cdot r^\gamma$$
Where:
- $s$ is the output pixel value.
- $r$ is the input pixel value.
- $c$ is a scaling constant that can be used to adjust the output intensity range.
- $\gamma$ is the gamma value that controls the shape of the transformation curve.

- This transformation is commonly used for gamma correction, which adjusts the brightness of an image. A gamma value less than 1 will brighten the image, while a gamma value greater than 1 will darken the image. It is widely used in display systems and image processing applications to achieve desired brightness levels.

## Contrast Stretching
- **Contrast stretching** is a point operation that enhances the contrast of an image by stretching the range of intensity values. It is defined as:
$$s = \frac{(r - r_{min}) \cdot (s_{max} - s_{min})}{r_{max} - r_{min}} + s_{min}$$
Where:
- $s$ is the output pixel value.
- $r$ is the input pixel value.
- $r_{min}$ and $r_{max}$ are the minimum and maximum pixel values in the input image, respectively.
- $s_{min}$ and $s_{max}$ are the desired minimum and maximum pixel values in the output image, respectively.   

- This transformation is used to improve the contrast of an image by stretching the intensity values to fill the desired range. It is particularly effective for images with low contrast, where the pixel values are clustered in a narrow range. 
- Contrast stretching can enhance the visibility of features in an image and is commonly used in applications such as medical imaging and remote sensing.


# Thresholding 
    - **Thresholding** is a fundamental technique in image processing used to segment an image into different regions based on pixel intensity values. It is commonly used in edge detection to classify pixels as either edge or non-edge based on their gradient magnitude, and more broadly to separate objects from backgrounds or to distinguish between multiple objects with different intensity levels.
    -- continue in Unit 1.1


## Spatial Filters (Spatial Filtering)

### Meaning
- A **spatial filter** computes a new pixel value from a **neighborhood** around that pixel.
- In practice we slide a small matrix called a **kernel / mask** over the image.

### Linear filtering (convolution)
- Replace each pixel with a **linear combination** of its neighbors.
- For an image $f$ of size $M\times N$ and a mask $w$ of size $m\times n$:

$$g(x,y)=\sum_{s=-a}^{a}\sum_{t=-b}^{b} w(s,t)\,f(x+s,y+t)$$

where $a=\frac{m-1}{2}$ and $b=\frac{n-1}{2}$.

---

### Types of spatial filters

#### 1) Smoothing filters (Low-pass filters)
Used for **noise reduction / blurring** (remove high-frequency details).

- **Mean / Box filter (linear)**

$$\frac{1}{9}\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}$$

- **Gaussian filter (weighted average, linear)**

$$\frac{1}{16}\begin{bmatrix}
1&2&1\\
2&4&2\\
1&2&1
\end{bmatrix}$$

- **Order-statistics filters (non-linear)**
    - **Median filter:** replace pixel with the **median** of its neighborhood (very good for *salt & pepper* noise).
    - **Mode filter:** replace pixel with the **most frequent** value in the neighborhood (useful for some discrete/intensity-quantized images).

---

#### 2) Sharpening filters (High-pass filters)
Used for **edge enhancement / detail enhancement** (emphasize high-frequency components).

- **Laplacian (2nd derivative) kernels**
    - 4-neighbour Laplacian:

$$\begin{bmatrix}
0&1&0\\
1&-4&1\\
0&1&0
\end{bmatrix}$$

    - 8-neighbour Laplacian:

$$\begin{bmatrix}
1&1&1\\
1&-8&1\\
1&1&1
\end{bmatrix}$$

- **Basic high-pass kernel** (highlights center, subtracts surrounding average)

$$\begin{bmatrix}
-1&-1&-1\\
-1&8&-1\\
-1&-1&-1
\end{bmatrix}$$

- **LoG (Laplacian of Gaussian)**
    - Smooth with Gaussian, then apply Laplacian (helps reduce noise sensitivity of Laplacian).

$$\operatorname{LoG}(x,y)=-\frac{1}{\pi\sigma^{4}}\left(1-\frac{x^{2}+y^{2}}{2\sigma^{2}}\right)e^{-\frac{x^{2}+y^{2}}{2\sigma^{2}}}$$

---

### Edge detection (high-pass / derivative operators)

- **Sobel operator (1st derivative / gradient)**

$$G_x=\begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix},\quad
G_y=\begin{bmatrix}
-1&-2&-1\\
0&0&0\\
1&2&1
\end{bmatrix}$$

- **Prewitt operator**

$$G_x=\begin{bmatrix}
-1&0&1\\
-1&0&1\\
-1&0&1
\end{bmatrix},\quad
G_y=\begin{bmatrix}
-1&-1&-1\\
0&0&0\\
1&1&1
\end{bmatrix}$$

- **Roberts Cross operator** (fast 2×2 gradient, diagonal emphasis)

$$G_x=\begin{bmatrix}
1&0\\
0&-1
\end{bmatrix},\quad
G_y=\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}$$

- Gradient magnitude (common):

$$|\nabla f|=\sqrt{G_x^2+G_y^2}\quad\text{(or }|G_x|+|G_y|\text{)}$$


    
