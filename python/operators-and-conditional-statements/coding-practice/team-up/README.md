# 🔹 **Question: Team Up**

You are given the scores of two players **A** and **B**.
You must print:

- **Can team up** → if
  ✔ One of the scores is greater than **300**
  **AND**
  ✔ The **sum** of the scores is **less than 500**

- Otherwise print **Cannot team up**

---

# 🟦 **1. Approach**

1. Read A and B
2. Compute the sum
3. Check:

   - Condition 1 → one score > 300
   - Condition 2 → sum < 500

4. Combine both using **and**
5. Print the result

---

# 🟨 **2. Step-by-Step Explanation**

### **Step 1: Input**

```python
score_1 = int(input())
score_2 = int(input())
```

### **Step 2: Sum of scores**

```python
sum_of_scores = score_1 + score_2
```

### **Step 3: First condition — one score > 300**

```python
is_one_score_greater = (score_1 > 300) or (score_2 > 300)
```

### **Step 4: Second condition — sum < 500**

```python
is_sum_less = sum_of_scores < 500
```

### **Step 5: Final condition**

```python
can_team_up = is_one_score_greater and is_sum_less
```

### **Step 6: Print result**

```python
if can_team_up:
    print("Can team up")
else:
    print("Cannot team up")
```

---

# 🟧 **3. Final Code**

```python
score_1 = int(input())
score_2 = int(input())

sum_of_scores = score_1 + score_2

is_one_score_greater = (score_1 > 300) or (score_2 > 300)
is_sum_less = sum_of_scores < 500

if is_one_score_greater and is_sum_less:
    print("Can team up")
else:
    print("Cannot team up")
```

---

# 🟥 **4. Dry Run Table**

### **Input**

```
350
134
```

| Step | Description | Evaluation       | Result |
| ---- | ----------- | ---------------- | ------ |
| 1    | score_1     | 350              | —      |
| 2    | score_2     | 134              | —      |
| 3    | Sum         | 350 + 134        | 484    |
| 4    | One > 300?  | 350 > 300 → True | True   |
| 5    | Sum < 500?  | 484 < 500 → True | True   |
| 6    | Final check | True AND True    | True   |
| 7    | Output      | Can team up      | ✔      |

### **Output**

```
Can team up
```

---
