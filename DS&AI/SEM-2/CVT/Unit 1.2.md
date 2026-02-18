# Scale Invariant Feature Transform (SIFT)

SIFT is a **feature detection + description** algorithm that finds distinctive **keypoints** in an image and builds a **descriptor** that is robust to:
- **Scale changes** (zoom in/out)
- **Rotation**
- Moderate **illumination changes**
- Small viewpoint changes / affine distortion (partial robustness)

It is widely used for matching the same object/scene across different images.

---

## Big picture
SIFT outputs:
1) **Keypoints**: locations $(x,y)$ + a scale $\sigma$ + an orientation $\theta$
2) **Descriptors**: a vector (classically **128-D**) describing the local patch around each keypoint

Typical pipeline:
1. Scale-space extrema detection
2. Keypoint localization
3. Orientation assignment
4. Keypoint descriptor

---

## 1) Scale-space extrema detection
Goal: detect keypoints that are **invariant to scale**.

### Gaussian scale space
Construct progressively blurred images:

$$L(x,y,\sigma)=G(x,y,\sigma) * I(x,y)$$

where $G$ is a Gaussian with standard deviation $\sigma$, $*$ is convolution.

### Difference of Gaussians (DoG)
SIFT uses DoG as an efficient approximation of the scale-normalized Laplacian:

$$D(x,y,\sigma) = L(x,y,k\sigma) - L(x,y,\sigma)$$

Keypoints are detected as **local extrema** (max/min) of $D$ across:
- **Space**: neighbors in $(x,y)$
- **Scale**: neighboring scales $(\sigma)$

Practical note: images are organized into **octaves** (downsampled levels) and several scales per octave.

---

## 2) Keypoint localization
Goal: keep only stable, well-localized keypoints.

SIFT refines candidate keypoints by:
- **Sub-pixel / sub-scale refinement** (fit a quadratic model around the extremum)
- Removing **low-contrast** points (weak extrema)
- Removing **edge-like** points that are unstable (strong response along an edge but poorly localized across the edge)

Edge rejection is commonly done using a Hessian-based test (ratio of principal curvatures).

---

## 3) Orientation assignment
Goal: make descriptors **rotation invariant**.

For each keypoint, compute gradient magnitude and direction in a local neighborhood:

$$m(x,y)=\sqrt{(I_x)^2+(I_y)^2}$$
$$\theta(x,y)=\tan^{-1}\left(\frac{I_y}{I_x}\right)$$

Then build an **orientation histogram** (weighted by gradient magnitude and a Gaussian window).

The dominant peak(s) define the keypoint orientation(s):
- One keypoint may produce **multiple orientations** if there are multiple strong peaks.

---

## 4) Keypoint descriptor
Goal: create a compact vector that uniquely describes the local patch and is robust to small changes.

### Descriptor construction (classic SIFT)
- Take a neighborhood around the keypoint (aligned to its assigned orientation)
- Divide it into a **4×4 grid** of cells
- For each cell compute an **8-bin** orientation histogram
- Concatenate all histograms:

$$4\times 4\times 8 = 128\text{-D descriptor}$$

### Normalization (illumination robustness)
- Normalize the 128-D vector (e.g., to unit length)
- Often **clip large values** then renormalize

This reduces sensitivity to overall brightness/contrast changes.

---

## Matching (how SIFT is used)
Given descriptors from two images:
1) Find nearest neighbor matches (usually Euclidean distance)
2) Apply **ratio test** (Lowe’s test): accept a match if

$$\frac{d_1}{d_2} < \tau$$

where $d_1$ is the distance to the best match and $d_2$ to the second best (typical $\tau\approx 0.75$).
3) Optionally use **RANSAC** to estimate geometry (homography/fundamental matrix) and remove outliers.

---

## Applications of SIFT
- **Object recognition** (matching object features across images)
- **Image stitching / panorama** (find correspondences, estimate homography)
- **3D reconstruction / SfM** (feature matching across views)

---

## Quick exam points
- SIFT is **scale + rotation invariant** by design (scale-space + orientation assignment).
- DoG finds extrema across **space + scale**.
- Descriptor is typically **128 dimensions** (4×4 cells, 8 bins each).
- Keypoint localization removes **low contrast** and **edge responses**.