# Deformable Shape Analysis 

- Deformable Shape Analysis is a set of computational techniques used to represent, detect, and track objects that can change their form, such as human bodies, organs, or flexible materials. Unlike rigid body analysis, it accounts for non-rigid variations caused by movement, growth, or external forces.

### Core Approaches
Deformable models are typically categorized by how they represent shape and the "forces" that drive their evolution:

- **Active Contour Models (Snakes)**: These are curves or surfaces that evolve to minimize an energy function.
    - **Mechanism**: The contour is a spline (a flexible curve) that evolves by minimizing an energy function. This function typically consists of:
        - **Internal Energy**: Controls the curve's own properties, such as elasticity (resistance to stretching) and rigidity (resistance to bending) to keep the shape smooth.
        - **External Energy**: Derived from the image data (e.g., gradients or edges) to pull the contour toward the actual object boundaries.
        - **Constraint Energy**: Optional forces, often provided by a user, that guide the snake toward or away from specific regions.

- **Fourier Descriptors**: These represent shapes in the frequency domain, allowing for compact representation and easy manipulation of shape features.
    - **Mechanism**: The shape boundary is represented as a complex function, and its Fourier transform is computed to obtain a set of coefficients. These coefficients capture the shape's characteristics, and by manipulating them, one can achieve transformations such as scaling, rotation, or deformation.
    - **Representation**:
        - **Low-frequency coefficients**: Capture the global, coarse properties of the shape (its general outline).
        - **High-frequency coefficients**: Capture fine details and sharp features.

---

## Harris Corner Detection

### Problem Statement
Given a 5×5 image matrix, apply Harris corner detection algorithm to identify corner points. Use the Sobel operators for gradient computation and analyze the corner response at the center pixel of a 3×3 window.

**Given Image:**
```
| 0  | 0  | 1  | 4  | 9  |
| 1  | 0  | 5  | 7  | 11 |
| 1  | 4  | 9  | 12 | 16 |
| 3  | 8  | 11 | 14 | 16 |
| 8  | 10 | 15 | 16 | 20 |
```

**Window of Interest (3×3):** Center region highlighted in red
```
| 0  | 5  | 7  |
| 4  | 9  | 12 |
| 8  | 11 | 14 |
```

### Harris Corner Detection Algorithm

#### **Overview**
Harris corner detection identifies regions in an image where there are significant variations in intensity in multiple directions. Corners are points where the gradient changes significantly in both x and y directions.

#### **Mathematical Foundation**

The Harris corner detector is based on analyzing the structure tensor (also called second moment matrix):

$$M = \sum_{x,y} w(x,y) \begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix}$$

Where:
- $I_x$ = gradient in x-direction (horizontal)
- $I_y$ = gradient in y-direction (vertical)
- $w(x,y)$ = window function (Gaussian or simple box filter)

The **Harris Response** is computed as:

$$R = \det(M) - k \cdot \text{trace}(M)^2$$

Where:
- $\det(M) = (I_x^2)(I_y^2) - (I_x I_y)^2$
- $\text{trace}(M) = I_x^2 + I_y^2$
- $k$ = Harris constant (typically 0.04 to 0.06)

**Decision Criteria:**
- $R > 0$ and large → Corner
- $R < 0$ → Edge
- $R \approx 0$ → Flat region

---

### Step-by-Step Solution

#### **Step 0: Understanding Sobel Operators (Why These Specific Values?)**

Before we begin computing gradients, it's important to understand that **Sobel operators are predefined, standard kernels** invented by Irwin Sobel in 1968. They are NOT calculated from your image—think of them like mathematical constants (like $\pi$ or $e$) that we use as-is.

**The Sobel Kernels:**

$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix} \quad \text{(Horizontal gradients)}$$

$$G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix} \quad \text{(Vertical gradients)}$$

---

**Design Principles:**

**1. Horizontal Gradient Detection ($G_x$):**
- **Left column** $(-1, -2, -1)$: Negative weights detect dark-to-bright transitions
- **Center column** $(0, 0, 0)$: Ignored (no contribution)
- **Right column** $(1, 2, 1)$: Positive weights detect bright areas

**2. Why ±2 in the middle row/column?**

The center has **double weight** (±2 instead of ±1) because:
- Gives more importance to the central pixel's neighbors
- Reduces noise by averaging in the perpendicular direction (Gaussian smoothing)
- The weights approximate the derivative of a Gaussian function

**3. Mathematical Derivation:**

The Sobel operator combines two operations:
- **Derivative** (detects edges)
- **Gaussian smoothing** (reduces noise)

For $G_x$ (horizontal gradient):
- Derivative in x-direction: $[-1, 0, 1]$
- Smoothing in y-direction: $[1, 2, 1]^T$

Taking the **outer product**:

$$G_x = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \times \begin{bmatrix} -1 & 0 & 1 \end{bmatrix} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$

Similarly for $G_y$ (vertical gradient):
- Smoothing in x-direction: $[1, 2, 1]$
- Derivative in y-direction: $[-1, 0, 1]^T$

$$G_y = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \times \begin{bmatrix} 1 & 2 & 1 \end{bmatrix} = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

---

**Key Takeaway:**
- Sobel kernels are standard, predefined operators
- You simply apply them to your image using convolution
- They are designed to detect edges while reducing noise
- Use them as-is—no need to derive them each time!

---

#### **Step 1: Compute Image Gradients**

We use Sobel operators to compute gradients:

**Sobel X-kernel (for horizontal gradients $I_x$):**
$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$

**Sobel Y-kernel (for vertical gradients $I_y$):**
$$G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

#### **Step 2: Apply Sobel Operators to the 3×3 Window**

**Our 3×3 Window:**
```
| 0  | 5  | 7  |
| 4  | 9  | 12 |
| 8  | 11 | 14 |
```

The Sobel operator works by **element-wise multiplication** followed by summation (convolution operation). We overlay the kernel on the window, multiply each corresponding pair of values, and sum all products.

---

**Computing $I_x$ (horizontal gradient):**

We overlay $G_x$ on the window and perform element-wise multiplication:

**Step-by-step breakdown:**

$$
\begin{array}{|c|c|c|}
\hline
\text{Window} & \text{Position} & G_x \text{ kernel} & \text{Multiplication} \\
\hline
0 & \text{top-left} & -1 & 0 \times (-1) = 0 \\
5 & \text{top-center} & 0 & 5 \times 0 = 0 \\
7 & \text{top-right} & 1 & 7 \times 1 = 7 \\
\hline
4 & \text{mid-left} & -2 & 4 \times (-2) = -8 \\
9 & \text{mid-center} & 0 & 9 \times 0 = 0 \\
12 & \text{mid-right} & 2 & 12 \times 2 = 24 \\
\hline
8 & \text{bottom-left} & -1 & 8 \times (-1) = -8 \\
11 & \text{bottom-center} & 0 & 11 \times 0 = 0 \\
14 & \text{bottom-right} & 1 & 14 \times 1 = 14 \\
\hline
\end{array}
$$

**Visual representation:**

$$
\begin{bmatrix} 0 & 5 & 7 \\ 4 & 9 & 12 \\ 8 & 11 & 14 \end{bmatrix}
\odot
\begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}
=
\begin{bmatrix} 0 & 0 & 7 \\ -8 & 0 & 24 \\ -8 & 0 & 14 \end{bmatrix}
$$

**Sum all products:**

$$I_x = 0 + 0 + 7 + (-8) + 0 + 24 + (-8) + 0 + 14 = 29$$

**Interpretation:** The positive value indicates intensity increases from left to right.

---

**Computing $I_y$ (vertical gradient):**

We overlay $G_y$ on the window and perform element-wise multiplication:

**Step-by-step breakdown:**

$$
\begin{array}{|c|c|c|}
\hline
\text{Window} & \text{Position} & G_y \text{ kernel} & \text{Multiplication} \\
\hline
0 & \text{top-left} & -1 & 0 \times (-1) = 0 \\
5 & \text{top-center} & -2 & 5 \times (-2) = -10 \\
7 & \text{top-right} & -1 & 7 \times (-1) = -7 \\
\hline
4 & \text{mid-left} & 0 & 4 \times 0 = 0 \\
9 & \text{mid-center} & 0 & 9 \times 0 = 0 \\
12 & \text{mid-right} & 0 & 12 \times 0 = 0 \\
\hline
8 & \text{bottom-left} & 1 & 8 \times 1 = 8 \\
11 & \text{bottom-center} & 2 & 11 \times 2 = 22 \\
14 & \text{bottom-right} & 1 & 14 \times 1 = 14 \\
\hline
\end{array}
$$

**Visual representation:**

$$
\begin{bmatrix} 0 & 5 & 7 \\ 4 & 9 & 12 \\ 8 & 11 & 14 \end{bmatrix}
\odot
\begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
=
\begin{bmatrix} 0 & -10 & -7 \\ 0 & 0 & 0 \\ 8 & 22 & 14 \end{bmatrix}
$$

**Sum all products:**

$$I_y = 0 + (-10) + (-7) + 0 + 0 + 0 + 8 + 22 + 14 = 27$$

**Interpretation:** The positive value indicates intensity increases from top to bottom.

---

**Key Insight:**
- Sobel operators use **weighted differences** between opposite sides
- $G_x$ compares left vs. right columns (with center having weight 2)
- $G_y$ compares top vs. bottom rows (with center having weight 2)
- The middle row/column in each kernel has zeros to focus on the perpendicular direction

#### **Step 3: Compute Products of Derivatives**

$$I_x^2 = (29)^2 = 841$$

$$I_y^2 = (27)^2 = 729$$

$$I_x I_y = (29)(27) = 783$$

#### **Step 4: Construct the Structure Tensor Matrix**

For a single pixel (without Gaussian weighting):

$$M = \begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix} = \begin{bmatrix} 841 & 783 \\ 783 & 729 \end{bmatrix}$$

#### **Step 5: Compute Harris Response**

**Determinant calculation:**

$$\det(M) = I_x^2 \cdot I_y^2 - (I_x I_y)^2$$

$$\det(M) = (841)(729) - (783)^2$$

Let's verify each term:
- $841 \times 729 = 613,089$
- $783^2 = 783 \times 783 = 613,089$

$$\det(M) = 613,089 - 613,089 = 0$$

> **📝 Note:** The determinant equals zero because the gradients are perfectly proportional. This occurs when:
> $$I_x^2 \cdot I_y^2 = (I_x \cdot I_y)^2$$
> 
> Which happens when the ratio $\frac{I_x}{I_y}$ is constant across the window. Mathematically:
> $$\frac{29}{27} \approx 1.074$$
> 
> This indicates a **linear edge** rather than a corner (where gradients would vary in multiple directions).

**Trace calculation:**

$$\text{trace}(M) = I_x^2 + I_y^2 = 841 + 729 = 1,570$$

**Harris Response (using $k = 0.04$):**

$$R = \det(M) - k \cdot \text{trace}(M)^2$$

$$R = 0 - 0.04 \times (1,570)^2$$

$$R = 0 - 0.04 \times 2,464,900$$

$$R = -98,596$$

> **✓ Verification:**
> - Determinant: $\det(M) = 0$ ✓ (verified)
> - Trace: $\text{trace}(M) = 1,570$ ✓
> - k value: $0.04$ (standard Harris constant)
> - Final response: $R = -98,596$ (large negative value)

#### **Step 6: Interpretation**

Since $R < 0$ and significantly negative, this indicates an **edge** rather than a corner at the center pixel.

**Analysis:**
- The large negative Harris response suggests this region has strong gradients predominantly in one direction
- Both $I_x$ and $I_y$ are large and nearly equal, but their product creates a determinant close to zero
- This is characteristic of an edge region where intensity changes consistently in one direction

### Summary

- **Gradients:** $I_x = 29$, $I_y = 27$
- **Structure Tensor:** $M = \begin{bmatrix} 841 & 783 \\ 783 & 729 \end{bmatrix}$
- **Harris Response:** $R = -98,596$
- **Classification:** **Edge** (not a corner)

### Key Formulas Reference

#### **1. Sobel Operators (Gradient Computation)**
$$I_x = \text{Image} \otimes G_x, \quad I_y = \text{Image} \otimes G_y$$

Where $\otimes$ denotes convolution:
$$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$

#### **2. Structure Tensor (Second Moment Matrix)**
$$M = \begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix}$$

#### **3. Matrix Properties**
- **Determinant:** $\det(M) = I_x^2 \cdot I_y^2 - (I_x I_y)^2$
- **Trace:** $\text{trace}(M) = I_x^2 + I_y^2$

#### **4. Harris Corner Response**
$$R = \det(M) - k \cdot \text{trace}(M)^2$$

Where $k \in [0.04, 0.06]$ (typically 0.04)

#### **5. Decision Rules**
- **Corner:** $R > 0$ and $R$ is large
- **Edge:** $R < 0$ 
- **Flat region:** $|R|$ is small (close to 0)

---

### 📌 Quick Calculation Check
For our problem:
- ✓ $I_x = 29$, $I_y = 27$
- ✓ $I_x^2 = 841$, $I_y^2 = 729$, $I_x I_y = 783$
- ✓ $\det(M) = 613,089 - 613,089 = 0$
- ✓ $\text{trace}(M) = 1,570$
- ✓ $R = 0 - 0.04(1,570)^2 = -98,596$
- ✓ **Result: Edge** (large negative R)

---

## Hough Transform for Line Detection

### Problem Statement
Using the Hough Transform, prove that the following points are **collinear** (lie on the same straight line). Also, find the equation of the line.

**Given Points:** $(1, 2)$, $(2, 3)$, $(3, 4)$

### Hough Transform Algorithm

#### **Overview**
The Hough Transform is a feature extraction technique used in image analysis and computer vision to detect geometric shapes, particularly lines, circles, and other parametric curves. It transforms points from the **image space** (x, y coordinates) to a **parameter space** where lines are represented as points.

**Key Concept:**
- In image space: A line is represented by the equation $y = mx + c$
- In parameter space: Each point $(x_i, y_i)$ generates a line in the $(m, c)$ parameter space
- If points are collinear in image space, their corresponding lines in parameter space will **intersect at a single point** representing the line parameters $(m, c)$

#### **Mathematical Foundation**

**Line Representation:**
$$y = mx + c$$

Where:
- $m$ = slope of the line
- $c$ = y-intercept

**Transform from Image Space to Parameter Space:**

For each point $(x_i, y_i)$ in image space, we rearrange the line equation:

$$c = -mx_i + y_i$$

This equation represents a **line in parameter space** $(m, c)$ for the point $(x_i, y_i)$.

**Collinearity Test:**
- Plot all transformed lines in $(m, c)$ space
- If the original points are collinear, all lines will intersect at a single point $(m_0, c_0)$
- This intersection point gives the parameters of the line passing through all points

---

### Step-by-Step Solution

#### **Step 1: Transform Points to Parameter Space**

For each point $(x, y)$, we use the transformation equation:

$$c = -mx + y$$

This creates a line in the $(m, c)$ parameter space.

---

#### **Point 1: $(1, 2)$**

Substitute $(x, y) = (1, 2)$:

$$c = -m(1) + 2$$
$$c = -m + 2$$

**Find boundary points for plotting:**
- When $c = 0$: $0 = -m + 2 \Rightarrow m = 2$ → Point $(2, 0)$
- When $m = 0$: $c = -0 + 2 = 2$ → Point $(0, 2)$

**Parameter space line:** Passes through $(m, c)$ points $(2, 0)$ and $(0, 2)$

---

#### **Point 2: $(2, 3)$**

Substitute $(x, y) = (2, 3)$:

$$c = -m(2) + 3$$
$$c = -2m + 3$$

**Find boundary points:**
- When $c = 0$: $0 = -2m + 3 \Rightarrow m = \frac{3}{2} = 1.5$ → Point $(1.5, 0)$
- When $m = 0$: $c = -2(0) + 3 = 3$ → Point $(0, 3)$

**Parameter space line:** Passes through $(m, c)$ points $(1.5, 0)$ and $(0, 3)$

---

#### **Point 3: $(3, 4)$**

Substitute $(x, y) = (3, 4)$:

$$c = -m(3) + 4$$
$$c = -3m + 4$$

**Find boundary points:**
- When $c = 0$: $0 = -3m + 4 \Rightarrow m = \frac{4}{3} \approx 1.33$ → Point $(1.33, 0)$
- When $m = 0$: $c = -3(0) + 4 = 4$ → Point $(0, 4)$

**Parameter space line:** Passes through $(m, c)$ points $(1.33, 0)$ and $(0, 4)$

---

#### **Step 2: Find Intersection Point in Parameter Space**

To find where all three lines intersect, we solve any two equations simultaneously.

**Using Point 1 and Point 2:**

From Point 1: $c = -m + 2$ ... (1)
From Point 2: $c = -2m + 3$ ... (2)

Set them equal:
$$-m + 2 = -2m + 3$$

Add $2m$ to both sides:
$$-m + 2m + 2 = 3$$
$$m + 2 = 3$$
$$m = 1$$

Substitute $m = 1$ into equation (1):
$$c = -1 + 2 = 1$$

**Intersection point:** $(m, c) = (1, 1)$

---

#### **Step 3: Verify with Point 3**

Check if Point 3's equation passes through $(1, 1)$:

$$c = -3m + 4$$

Substitute $m = 1$:
$$c = -3(1) + 4$$
$$c = -3 + 4$$
$$c = 1$$ ✓

**Conclusion:** All three lines in parameter space intersect at the single point $(1, 1)$, confirming that the original points are **collinear**.

---

#### **Step 4: Write the Line Equation**

The intersection point $(m, c) = (1, 1)$ gives us:
- Slope: $m = 1$
- Y-intercept: $c = 1$

**Equation of the line:**
$$\boxed{y = x + 1}$$

---

### Verification

## What's Happening in Verification:

We found that the line equation is y=x+1y=x+1. Now we're checking if all three original points actually satisfy this equation:

**Point (1, 2):**

- Substitute x=1x=1 into y=x+1y=x+1
- y=1+1=2y=1+1=2 ✓
- This matches the actual y-coordinate of the point

**Point (2, 3):**

- Substitute x=2x=2 into y=x+1y=x+1
- y=2+1=3y=2+1=3 ✓
- This matches the actual y-coordinate of the point

**Point (3, 4):**

- Substitute x=3x=3 into y=x+1y=x+1
- y=3+1=4y=3+1=4 ✓
- This matches the actual y-coordinate of the point

Let's verify that all three points satisfy the equation $y = x + 1$:

**Point $(1, 2)$:**
$$y = 1 + 1 = 2$$ ✓

**Point $(2, 3)$:**
$$y = 2 + 1 = 3$$ ✓

**Point $(3, 4)$:**
$$y = 3 + 1 = 4$$ ✓

All points satisfy the equation, confirming our result.

---

### Visual Representation

**Image Space (Original Points):**
```
y
4 |       • (3,4)
3 |     • (2,3)
2 |   • (1,2)
1 | 
0 |_____________
  0 1 2 3 4   x
```
All points lie on the line $y = x + 1$

**Parameter Space (Hough Space):**
```
c
4 |•                Line from (3,4)
3 |  •           Line from (2,3)
2 |    •       Line from (1,2)
1 |     ✱     ← All lines intersect at (1,1)
0 |______________________________
  0  1  2  3  4   m
```

The diagram shows:
- Each point in image space creates a line in parameter space
- All three lines intersect at a single point $(1, 1)$
- This intersection represents the parameters $(m=1, c=1)$ of the original line

---

### Summary

**Transformation Equations:**
- Point $(1, 2)$: $c = -m + 2$
- Point $(2, 3)$: $c = -2m + 3$
- Point $(3, 4)$: $c = -3m + 4$

**Intersection in Parameter Space:** $(m, c) = (1, 1)$

**Line Equation:** $y = x + 1$

**Conclusion:** The three points $(1, 2)$, $(2, 3)$, and $(3, 4)$ are **collinear** and lie on the line $y = x + 1$

---

### Key Formulas Reference

#### **1. Line Equation (Slope-Intercept Form)**
$$y = mx + c$$

Where $m$ is the slope and $c$ is the y-intercept.

#### **2. Hough Transform (Image to Parameter Space)**
$$c = -mx + y$$

For a point $(x_i, y_i)$, this creates a line in $(m, c)$ parameter space.

#### **3. Collinearity Test**
- Transform each point to a line in parameter space
- Find the intersection point of all lines
- If a unique intersection exists, points are collinear
- The intersection coordinates give the line parameters

#### **4. Alternative: Normal Form (Polar Representation)**
$$\rho = x \cos\theta + y \sin\theta$$

Where:
- $\rho$ = perpendicular distance from origin to the line
- $\theta$ = angle of the perpendicular from x-axis

This form is often preferred in practice because:
- Avoids the problem of infinite slope (vertical lines)
- Better numerical stability
- More uniform parameter space

---

### 📝 Practice Exercise

**Problem:** Using Hough transform, show that the points $(1, 1)$, $(2, 2)$, and $(3, 3)$ are collinear and find the equation.

**Solution Steps:**
1. Transform each point to parameter space:
   - $(1, 1)$: $c = -m + 1$
   - $(2, 2)$: $c = -2m + 2$
   - $(3, 3)$: $c = -3m + 3$

2. Find intersection of first two lines:
   - $-m + 1 = -2m + 2$
   - $m = 1$, $c = 0$

3. Verify with third line:
   - $c = -3(1) + 3 = 0$ ✓

**Answer:** $\boxed{y = x}$ (slope $m = 1$, y-intercept $c = 0$)