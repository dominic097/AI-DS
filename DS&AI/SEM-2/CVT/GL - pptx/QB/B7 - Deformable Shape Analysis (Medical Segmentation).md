# B7 — Deformable Shape Analysis for Medical Image Segmentation
**CVT Unit 2 | Part B | 15 Marks | Exam Notes**

---

## The Core Problem — Why Not Just Threshold?

In medical images (MRI, CT, X-ray), you want to isolate organs like the heart, liver, or tumour.
Simple thresholding fails because:

- Organs look different in every patient (different size, shape, position)
- Tissues next to each other have very similar pixel intensities
- Images have noise and low contrast

**Solution → Deformable models:** Start with a rough boundary, then let it flex and adapt until it fits the organ perfectly.

---

## The Big Idea in One Line

> Place a model near the organ → let it deform under two forces → it snaps onto the boundary.

**Two forces always acting on the model:**
- **Image force** — pulls the model toward strong edges (organ boundary)
- **Shape constraint** — stops the model from deforming into unrealistic shapes

---

## 3 Types of Deformable Models (Know All 3)

---

### Type 1 — Active Contours / Snakes (2D)

**What it is:** A flexible curve placed around an organ that contracts until it fits the boundary.

**How it works:**
1. Draw a rough contour around the organ manually or automatically.
2. The snake minimizes: **E = E_internal + E_external**
   - E_internal → keeps the curve smooth (no wild spikes)
   - E_external → pulls the curve toward organ edges (image gradient)
3. The curve iterates until it stops moving.

**Used for:** Heart ventricle boundary in MRI, tumour edges in CT.

**Remember:** Snake = rubber band around the organ. It tightens until it fits.

---

### Type 2 — Active Shape Models / ASM (Statistical)

**What it is:** A "smart" model trained on many patient images — it has learned what shapes are normal, so it only deforms into realistic shapes.

**Two phases:**

**Training (done once):**
- Take many images of the same organ (e.g., 100 heart scans)
- Mark key landmark points on each (e.g., 40 points on the heart boundary)
- Compute the **mean shape** (average of all 100)
- Use **PCA** to find the main ways the shape varies across patients
- Result: a model that knows "this organ can look like THIS range of shapes"

**Fitting (done on new patient):**
1. Start with the mean shape placed on the new image
2. Move each landmark toward the nearest strong edge
3. Check: is the new shape still realistic? If not, pull it back toward the allowed range
4. Repeat until stable

**Used for:** Vertebra detection in X-rays, heart shape fitting in echocardiograms.

**Remember:** ASM = "I've seen 100 hearts — I know what a heart looks like. I'll only deform within that range."

---

### Type 3 — Level Set Methods (3D capable)

**What it is:** Instead of tracking a curve directly, track a mathematical surface. The organ boundary is the "zero level" of that surface — wherever it equals zero is the contour.

**How it works:**
- Represent the boundary as: **φ(x, y, t) = 0** (zero level set of a 3D function)
- The surface evolves over time based on image forces
- The contour = wherever the surface crosses zero

**Key advantage:** The boundary can split or merge automatically. If one organ boundary splits into two parts, the level set handles it naturally. A curve-based snake cannot do this.

**Used for:** 3D organ segmentation in full CT volumes (liver, prostate, brain).

**Remember:** Level set = track a surface, not a curve. Zero crossing = boundary. Handles topology changes.

---

## Workflow — Same 5 Steps for All Models

```
1. Pre-process    → Gaussian smoothing, contrast enhancement
2. Initialize     → Place model near organ (manual or atlas-based guess)
3. Compute forces → Image gradient + internal shape forces
4. Iterate        → Deform model, minimize energy, repeat
5. Post-process   → Smooth result, compute area/volume
```

---

## Applications Table (Easy to Write in Exam)

| Application | Model Used | Image Type |
|---|---|---|
| Heart ventricle segmentation | Active Contour (Snake) | MRI / Echo |
| Tumour boundary detection | Active Contour | CT / MRI |
| Vertebra detection | ASM | X-ray |
| Cardiac shape fitting | ASM | Echocardiogram |
| Full 3D liver segmentation | Level Set | CT |
| Brain tumour delineation | Level Set | MRI |
| Prostate boundary | Level Set / Snake | Ultrasound |

---

## Advantage Over Simple Methods

| Simple Methods | Deformable Models |
|---|---|
| Same threshold for all patients | Adapts to each patient |
| Breaks on noisy images | Robust — shape constraint prevents wild results |
| Can't handle shape variation | Trained on real shape variation (ASM) |
| 2D only (thresholding) | Works in 3D (Level Set) |

---

## Quick Recall Summary

| Model | Key word | What it does |
|---|---|---|
| Snake | Rubber band | Flexible curve → minimizes E_internal + E_external |
| ASM | Trained memory | Knows valid shapes → fits landmarks to edges within learned range |
| Level Set | Zero crossing | Tracks a surface, not a curve → handles splits/merges in 3D |
