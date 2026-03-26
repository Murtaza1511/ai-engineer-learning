# 🎯 Goal of Day 6

Build:

> A system that compares two vectors and tells **how similar they are**

---

# 🔥 Why This Matters (Very Important)

This exact idea is used in:

* ChatGPT embeddings
* Semantic search
* Recommendation systems
* RAG pipelines

---

# 1. Problem Statement

We want:

```text
Input: Two vectors  
Output: Similarity score
```

---

# 2. What We Learned So Far

We will use:

* Dot product ✔
* NumPy ✔
* Vector understanding ✔

---

# ⚠️ Important (No Hallucination Rule Applied)

### ❌ Wrong:

```text
Dot product = similarity
```

---

### ✅ Correct:

```text
Dot product is related to similarity but depends on magnitude
```

---

# 3. Step 1 — Basic Similarity Engine

---

## Code

```python
import numpy as np

def similarity_engine(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    score = np.dot(v1, v2)
    
    return score

# Test
print(similarity_engine([1,2,3], [4,5,6]))
```

---

## Output

```text
32
```

---

# 🧠 Interpretation

```text
Higher score → more aligned (but magnitude also affects it)
```

---

# 4. Step 2 — Normalize Vectors (IMPORTANT UPGRADE)

To fix magnitude issue, we use:

---

## Cosine Similarity Formula

\text{cosine similarity} = \frac{A \cdot B}{|A||B|}

---

## Why?

```text
Removes magnitude influence
Focuses only on direction (true similarity)
```

---

# 5. Step 3 — Implement Cosine Similarity

---

## Code

```python
import numpy as np

def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    dot = np.dot(v1, v2)
    
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    similarity = dot / (norm_v1 * norm_v2)
    
    return similarity

# Test
print(cosine_similarity([1,2,3], [4,5,6]))
```

---

## ✅ Verified Behavior

* Value will be between:

```text
-1 to 1
```

---

## Interpretation

| Value | Meaning             |
| ----- | ------------------- |
| 1     | identical direction |
| 0     | unrelated           |
| -1    | opposite            |

---

# 6. Real AI Example

---

## Example: User Similarity

```python
user1 = [25, 50000, 2]
user2 = [26, 52000, 2]
```

---

## Compute

```python
print(cosine_similarity(user1, user2))
```

👉 High value → similar users

---

# 7. Upgrade — Make It User Friendly

---

## Code

```python
def analyze_similarity(v1, v2):
    sim = cosine_similarity(v1, v2)
    
    print("Similarity Score:", sim)
    
    if sim > 0.9:
        print("→ Highly similar")
    elif sim > 0.7:
        print("→ Moderately similar")
    elif sim > 0.5:
        print("→ Slightly similar")
    else:
        print("→ Not similar")

# Test
analyze_similarity([1,2,3], [4,5,6])
```

---

# 8. Experiments (VERY IMPORTANT)

Try these:

---

### Experiment 1 — Same direction

```python
cosine_similarity([1,2,3], [2,4,6])
```

Expected:

```text
≈ 1
```

---

### Experiment 2 — Perpendicular

```python
cosine_similarity([1,0], [0,1])
```

Expected:

```text
0
```

---

### Experiment 3 — Opposite

```python
cosine_similarity([1,2,3], [-1,-2,-3])
```

Expected:

```text
≈ -1
```

---

# 9. Real-World Thinking (Critical)

---

## Imagine:

```text
Movie vectors:
[action, romance, comedy]
```

---

## Query:

```text
User likes action → [1,0,0]
```

---

## Compare:

```text
dot or cosine similarity
```

👉 Recommend closest movies

---

# 10. Mini Project Deliverable (What You Must Build)

---

## Final Version Should:

* Take two vectors
* Compute:

  * dot product
  * cosine similarity
* Print interpretation

---

# 11. Reflection Questions

---

### Q1

Why is cosine similarity better than dot product for similarity?

---

### Q2

What problem does normalization solve?

---

### Q3 (IMPORTANT)

Where can this system be used in real products?

---

# 12. What You Just Built

```text
A primitive version of:
- embedding similarity
- recommendation engine
- semantic search
```

---

# 🧠 Mentor Insight

This is the **first real AI system you built**.

Even though it looks simple:

```text
This is EXACTLY what powers:
- ChatGPT retrieval
- vector databases
- search ranking
```

---

# ✅ Your Task

* Build final version
* Run experiments
* Answer reflection questions