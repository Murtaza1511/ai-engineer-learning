Goal today:

> Understand **vectors as containers of data** and why **AI represents everything as vectors**.

---

# 1. The Core Idea (Very Important)

Almost everything in AI becomes **numbers**.

Examples:

| Real World Thing | AI Representation |
| ---------------- | ----------------- |
| Height           | 180               |
| Weight           | 75                |
| Age              | 24                |

Combined together:

```
[180, 75, 24]
```

This list of numbers is called a **vector**.

### Definition (Simple)

A **vector = an ordered list of numbers**.

Example:

```
[3, 5, 7]
```

In AI this might represent:

```
[height, weight, age]
```

---

# 2. Why Vectors Are Used in AI

Computers cannot understand:

```
images
text
audio
video
```

So AI converts everything into **vectors of numbers**.

Examples:

### Image

A 28×28 pixel image becomes:

```
784 numbers
```

Vector representation:

```
[0, 255, 123, 54, ...]
```

---

### Text

Word:

```
"king"
```

Embedding vector:

```
[0.21, -0.54, 0.88, 0.10, ...]
```

---

### Audio

Audio waveform becomes:

```
[0.01, -0.02, 0.45, ...]
```

---

### Key Insight

```
AI does not see images
AI does not read words
AI only processes vectors
```

This idea will appear **again and again** in your AI journey.

---

# 3. Scalar vs Vector

You must understand this clearly.

### Scalar

A **single number**.

Example:

```
5
```

Example meaning:

```
temperature = 25
```

---

### Vector

Multiple numbers grouped together.

Example:

```
[25, 60, 1013]
```

Meaning:

```
[temperature, humidity, pressure]
```

---

# 4. Visual Intuition

Scalar:

```
5
```

Vector:

```
[5, 7, 9]
```

Or conceptually:

```
Vector = container of features
```

Example:

```
person = [height, weight, age]
```

---

# 5. Coding Exercise (Python)

Open **VSCode / terminal / Jupyter** and run this.

```python
vector = [3, 5, 7]

print(vector[0])
print(vector[1])
print(vector[2])
```

Output:

```
3
5
7
```

What you just did:

```
Access elements of a vector
```

---

# 6. Exercise 2 — Represent Real Data

Create vectors representing a person.

Example:

```python
person = [170, 65, 25]

height = person[0]
weight = person[1]
age = person[2]

print("Height:", height)
print("Weight:", weight)
print("Age:", age)
```

Think:

```
person = [height, weight, age]
```

This is **exactly how datasets are represented in ML**.

---

# 7. Exercise 3 — Vector Length

Add this code:

```python
vector = [3,5,7,9,11]

print(len(vector))
```

Output:

```
5
```

Meaning:

```
Vector dimension = 5
```

In AI you will often hear:

```
embedding dimension = 768
```

Meaning:

```
vector length = 768
```

---

# 8. Real AI Example

Imagine a **movie recommendation system**.

Movie features:

```
[action, romance, comedy]
```

Movie vector:

```
[0.9, 0.1, 0.2]
```

Another movie:

```
[0.8, 0.05, 0.1]
```

AI compares these vectors to determine **similar movies**.

You will implement this **later this week**.

---

# 9. Video Resource (Watch Carefully)

Watch this (15 minutes):

**3Blue1Brown – Essence of Linear Algebra (Vectors)**

[https://www.youtube.com/watch?v=fNk_zzaMoSs](https://www.youtube.com/watch?v=fNk_zzaMoSs)

This is one of the **best math intuition series ever created**.

Focus on:

```
vectors as arrows
vectors as data
```

Do NOT worry about heavy math yet.

---

# 10. Optional Extra (Highly Recommended)

Karpathy-style learning means **visual intuition**.

If you want deeper understanding:

Watch:

```
StatQuest – Vectors
```

[https://www.youtube.com/watch?v=H0Ek86IH-3Y](https://www.youtube.com/watch?v=H0Ek86IH-3Y)

---

# 11. Reflection Questions (Important)

Write answers in your notes.

### Question 1

If a dataset has:

```
height
weight
age
salary
```

What is the **vector representation**?

---

### Question 2

If an embedding has **768 dimensions**, what does that mean?

---

### Question 3

Why must vectors contain **numbers only**?

---

# 12. Micro Challenge (5 minutes)

Write code for a **student vector**.

Features:

```
math_score
science_score
english_score
```

Example vector:

```
[90, 85, 88]
```

Write code to print each value.

---

# 13. What You Should Understand After Day 1

If today's lesson worked, you should clearly understand:

```
vector = list of numbers
vector = representation of data
AI systems operate on vectors
```

This is the **foundation of everything in AI**.

Neural networks are basically:

```
vector in
vector out
```

---

# Your Task Now

Complete the following:

1️⃣ Watch the **3Blue1Brown vector video**
2️⃣ Run the **Python exercises**
3️⃣ Write answers to the **reflection questions**

This should take **~1 hour**.

---

# After You Finish

Reply with:

```
Day 1 Completed
```

Then I will give you **Day 2 — Vector Operations**.

And Day 2 is where the math **starts becoming interesting**, because you will learn the operation that powers:

```
neural networks
embeddings
transformers
similarity search
```

(the **dot product**).
