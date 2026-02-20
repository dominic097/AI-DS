# Connected Components (4- / 8-Connectivity) — Answer Sheet

> Convention used in this answer sheet:
> - Background pixels are `0`
> - Each connected component (object/cluster) is labeled as `1, 2, 3, ...`
> - Connectivity is exactly as asked in the question (4- or 8-neighborhood)

---

## Exercise 1

### Problem statement
Using **8-connectivity**, label all connected components in the same binary image, count the total number of objects present, and display the labeled matrix as output.

Binary image:
```
0 1 1 0
1 1 0 0
0 0 1 1
```

### Answer (8-connectivity)
Here the top-left group of `1`s is **diagonally connected** to the bottom-right `1`s, so they form **one single object** under 8-connectivity.

- **Total objects = 1**

Labeled output matrix:
```
0 1 1 0
1 1 0 0
0 0 1 1
```

---

## Exercise 2

### Problem statement
A satellite captures a binary image of a farmland where `1` represents regions of crop growth and `0` represents barren land.
Using **4-connectivity**, identify distinct crop clusters.

Binary image:
```
0 1 1 0 1 0 1
0 1 1 0 1 0 1
0 0 1 1 0 0 0
1 1 0 0 1 1 1
```

### Answer (4-connectivity)
- **Total crop clusters = 5**

Labeled output matrix (4-connectivity):
```
0 1 1 0 2 0 3
0 1 1 0 2 0 3
0 0 1 1 0 0 0
4 4 0 0 5 5 5
```

---

## Exercise 3

### Problem statement
A drone captures a binary image (11×11) of a forest region where `1` represents trees and `0` represents empty ground.
Using **4-connectivity**, identify distinct tree clusters.

Binary image (11×11):
```
0 0 1 1 0 0 0 1 0 0 0
0 1 1 1 0 0 0 1 0 1 0
0 1 0 0 0 1 1 1 0 1 0
0 0 0 0 0 0 0 0 0 1 0
1 1 0 0 1 1 0 0 0 0 0
1 1 0 0 0 1 0 0 1 1 0
0 0 0 0 0 0 0 0 1 1 0
0 0 0 1 1 1 0 0 0 0 0
0 0 0 1 0 1 0 0 0 0 0
0 0 0 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

### Answer (4-connectivity)
- **Total tree clusters = 7**

Labeled output matrix (4-connectivity):
```
0 0 1 1 0 0 0 2 0 0 0
0 1 1 1 0 0 0 2 0 3 0
0 1 0 0 0 2 2 2 0 3 0
0 0 0 0 0 0 0 0 0 3 0
4 4 0 0 5 5 0 0 0 0 0
4 4 0 0 0 5 0 0 6 6 0
0 0 0 0 0 0 0 0 6 6 0
0 0 0 7 7 7 0 0 0 0 0
0 0 0 7 0 7 0 0 0 0 0
0 0 0 7 7 7 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```
