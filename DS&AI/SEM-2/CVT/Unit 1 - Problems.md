# Histogram Equalization Drill

## Problem Statement
Given an image that is quantized to 3-bit gray levels (0 through 7), the observed histogram below is rather peaked around a few intensities:

| Gray level (k) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pixels `n_k` | 0 | 100 | 400 | 50 | 200 | 50 | 200 | 0 |

Total pixels `n = 1000`.

Task: draw/standardize this histogram via global histogram equalization and report the mapping as well as the equalized histogram values.

## Solution (step-by-step)
Let `L = 8` gray levels and `m = L - 1 = 7`.

| k | `n_k` | Probability `p_r(k)=n_k/n` | CDF `cdf(k)` | Mapped level `s_k = round(m * cdf(k))` |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0.00 | 0.00 | 0 |
| 1 | 100 | 0.10 | 0.10 | 1 |
| 2 | 400 | 0.40 | 0.50 | 4 |
| 3 | 50 | 0.05 | 0.55 | 4 |
| 4 | 200 | 0.20 | 0.75 | 5 |
| 5 | 50 | 0.05 | 0.80 | 6 |
| 6 | 200 | 0.20 | 1.00 | 7 |
| 7 | 0 | 0.00 | 1.00 | 7 |

Notes:
- Probabilities sum to 1.00 (within rounding) and the CDF is monotonically increasing.
- Rounding is to the nearest integer; using `floor` would simply drop level 1 back to 0 and level 2 to 3, but rounding provides slightly better spreading here. Adjust if your implementation uses `floor`.

## Equalized Histogram (standardized counts)
Group pixels by their new levels:

| Equalized level | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total pixels | 0 | 100 | 0 | 0 | 450 | 200 | 50 | 200 |

- Levels 2 and 3 in the equalized space receive no pixels because no original bin mapped to them after rounding.
- The previously sharp peak at level 2 is now spread over levels 4 through 7, creating a flatter (more standardized) histogram, as expected from equalization.
- If you need a visual “drawn” histogram, plot the original counts and the equalized counts side by side; both lists above can be pasted directly into plotting software or a notebook.

## Graph and Interpretation
The screenshot you attached shows exactly the same numbers: the “Old Gray Level / New Gray Level” table is a visual restatement of the mapping table above, while the two bar charts display the original and equalized histograms. To keep everything self-contained here, below is a quick ASCII rendering (each `#` ≈ 50 pixels) you can copy into your notes or slide deck:

```
Original Histogram (counts)
Level 0: 
Level 1: ## (100)
Level 2: ######## (400)
Level 3: # (50)
Level 4: #### (200)
Level 5: # (50)
Level 6: #### (200)
Level 7: 

Equalized Histogram (after mapping)
Level 0: 
Level 1: ## (100)
Level 2: 
Level 3: 
Level 4: ######### (450)
Level 5: #### (200)
Level 6: # (50)
Level 7: #### (200)
```

Explanation:
- The mapping table drives the “New Gray Level” column in your figure, so each original bar simply relocates to its new level before we re-count pixels.
- Because levels 2 and 3 both map to 4, their tall bars collapse into the single tall equalized bar at level 4 (450 pixels). The lower bars from levels 4, 5, and 6 spread across 5–7, giving a much less skewed distribution that still preserves total energy (area under the histogram).
- Any plotting tool (Excel, matplotlib, etc.) that ingests the above count lists will generate the same charts as in the screenshot; this confirms the correlation between the analytical solution and the provided visual.

