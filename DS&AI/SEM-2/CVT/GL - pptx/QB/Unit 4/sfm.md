# Q: Two-frame Structure from Motion (SfM) and Triangulation

---

## 1. Definition

**Structure from Motion (SfM)** is a technique in computer vision that recovers:
- The **3D structure** of a scene (positions of points in 3D space), and
- The **camera motion** (position and orientation of the camera)

from a sequence of 2D images.

**Two-frame SfM** specifically uses just **two images** taken from different viewpoints to estimate both the 3D structure and the relative camera motion between those two views.

---

## 2. Why Two Frames?

When we take two photos of the same scene from different positions, the same real-world point appears at different pixel locations in each image. By analyzing how matched pixels moved between the two images, we can figure out:

1. How the camera moved (rotation $R$ and translation $t$)
2. Where each point is in 3D space

---

## 3. Mathematical Background

### Camera Projection Model

A 3D point $X$ is projected to a 2D image point $x$ by:

$$x \sim K [R \mid t] X$$

where:
- $K$ = camera intrinsic matrix (focal length, principal point)
- $R$ = rotation matrix (camera orientation)
- $t$ = translation vector (camera position)
- $\sim$ means equal up to a scale factor (homogeneous coordinates)

### Fundamental Matrix $F$

When a 3D point is seen in two cameras, its projections in the two images satisfy:

$$x_2^T F\, x_1 = 0$$

$F$ encodes the geometric relationship between the two views. It can be estimated from 8 or more matched point pairs using the **8-point algorithm**.

### Essential Matrix $E$

If the camera intrinsics $K$ are known, the Essential Matrix $E$ gives the same relationship but in normalized camera coordinates:

$$E = K^T F K$$

From $E$, we can recover the camera rotation $R$ and translation $t$ up to scale.

---

## 4. Step-by-Step Process

```
Image 1 ──► Detect features ──┐
                               ├──► Match ──► RANSAC ──► F / E ──► R, t ──► Triangulate ──► 3D Points
Image 2 ──► Detect features ──┘
```

**Step 1 — Feature Detection**

Find distinctive points (keypoints) in both images.
- **SIFT** (Scale-Invariant Feature Transform) — robust to scale and rotation changes.
- **ORB** (Oriented FAST and Rotated BRIEF) — faster, good for real-time use.

**Step 2 — Feature Matching**

Match keypoints from Image 1 to Image 2 using descriptor similarity.

**Step 3 — Remove Outliers (RANSAC)**

Wrong matches (outliers) are removed using RANSAC (Random Sample Consensus). Only geometrically consistent matches are kept.

**Step 4 — Estimate Fundamental Matrix $F$**

Using the cleaned matches, compute $F$ with the 8-point algorithm. $F$ captures the epipolar geometry.

**Step 5 — Recover Camera Motion**

If intrinsics $K$ are known, compute Essential Matrix $E$ and decompose it to get rotation $R$ and translation $t$. This gives the relative pose of Camera 2 w.r.t. Camera 1.

**Step 6 — Build Projection Matrices**

Set Camera 1 at the origin:
$$P_1 = K [I \mid 0]$$
Camera 2 is:
$$P_2 = K [R \mid t]$$

**Step 7 — Triangulation**

For each matched pair $(x_1, x_2)$, find the 3D point $X$ that best fits both projections:
$$x_1 \sim P_1 X, \quad x_2 \sim P_2 X$$

**Step 8 — Bundle Adjustment (Refinement)**

Jointly optimize all camera poses and 3D points to minimize total reprojection error:
$$\min \sum \| x_{ij} - \pi(P_i, X_j) \|^2$$

---

## 5. How Triangulation Works

Each matched 2D point gives one **ray** from each camera. The 3D point lies where these two rays intersect.

```
     Camera 1            Camera 2
         O                   O
          \                 /
           \               /
            \             /
             \           /
              \         /
               ●  ← X (3D Point)
```

In real data, rays do not intersect exactly due to noise. So we find the point $X$ that **minimizes reprojection error** — the distance between the projected point and the observed point in both images.

---

## 6. Advantages

| Advantage | Explanation |
|-----------|-------------|
| No special hardware | Works with any standard camera |
| Passive method | No structured light or laser needed |
| Dense reconstruction possible | With many features, a dense 3D map can be built |
| Scalable | Extend to multi-view SfM easily |

---

## 7. Limitations

| Limitation | Explanation |
|------------|-------------|
| Scale ambiguity | Translation $t$ is recovered only up to scale |
| Degenerate cases | Fails if scene is planar or camera only rotates |
| Needs good initialization | RANSAC may fail with too many outliers |
| Slow for large scenes | Bundle adjustment is computationally expensive |

---

## 8. Applications

- **Robotics** — building maps from camera images for autonomous navigation
- **Augmented Reality** — estimating camera pose to overlay virtual objects correctly
- **Autonomous Vehicles** — 3D scene understanding from dashcam footage
- **Cultural Heritage** — 3D digitization of monuments and artifacts from photos
- **Industrial Inspection** — measuring shapes of manufactured parts from images
- **Medical Imaging** — 3D reconstruction from endoscope video frames

---

## 9. Summary

Two-frame SfM is the foundation of 3D reconstruction from images. Given just two photographs, it recovers camera motion and scene structure by matching features, estimating epipolar geometry, and triangulating 3D points. The key mathematical tools are the Fundamental Matrix, Essential Matrix, and triangulation. The result is a sparse 3D point cloud that represents the real-world scene.

**Quick memory flow:**
**Detect → Match → Clean → Epipolar Geometry → Camera Motion → Triangulate → Refine**
