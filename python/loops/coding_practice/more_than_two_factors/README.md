# ✅ **More Than Two Factors**

---

## **1️⃣ Question**

Given a number **N**, find the **count of its factors**.

- If the count of factors is **greater than 2**, print
  👉 **`Number has more than 2 factors`**
- Otherwise, print
  👉 **`Number doesn't have more than 2 factors`**

---

## **1️⃣.5️⃣ Category**

For Loop → Factors → Conditional Check

---

## **2️⃣ Objective**

To check whether a number has **more than two factors** using a loop.

---

## **3️⃣ Important Concept (VERY CLEAR)**

👉 A **factor** of a number is a number that divides it **exactly**.

Example:

- Factors of `6` → `1, 2, 3, 6` → **4 factors**
- Factors of `13` → `1, 13` → **2 factors**

---

## **4️⃣ Logic Explanation**

1. Read the number `N`
2. Initialize `count = 0`
3. Loop from `1` to `N`
4. If `i` divides `N` exactly → it is a factor → increase count
5. After loop:

   - If `count > 2` → print **has more than 2 factors**
   - Else → print **doesn't have more than 2 factors**

---

## **5️⃣ Step-by-Step Explanation**

- We check **all numbers from 1 to N**
- Every time `N % i == 0`, we found a factor
- We only care **how many**, not which ones

---

## **6️⃣ Code (BEGINNER-SAFE & CORRECT)**

```python
N = int(input())

count = 0

for i in range(1, N + 1):
    if N % i == 0:
        count = count + 1

if count > 2:
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")
```

---

## **7️⃣ Example 1**

### Input

```
6
```

### Factors

```
1, 2, 3, 6
```

### Count

```
4
```

### Output

```
Number has more than 2 factors
```

---

## **8️⃣ Example 2**

### Input

```
13
```

### Factors

```
1, 13
```

### Count

```
2
```

### Output

```
Number doesn't have more than 2 factors
```

---

## **9️⃣ Dry Run (N = 4)**

| i   | 4 % i | factor? | count |
| --- | ----- | ------- | ----- |
| 1   | 0     | yes     | 1     |
| 2   | 0     | yes     | 2     |
| 3   | 1     | no      | 2     |
| 4   | 0     | yes     | 3     |

👉 `count = 3` → **more than 2 factors**

---

## **🔟 Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Common Mistakes**

❌ Forgetting to reset count
❌ Looping only till `N/2` without logic
❌ Printing inside the loop

---

## **1️⃣2️⃣ Key Takeaways**

✔ Prime numbers → **exactly 2 factors**
✔ Composite numbers → **more than 2 factors**
✔ Loop + modulo is enough
✔ Very common interview logic

---

If you want, next we can do:

- **Prime number check**
- **Count of prime numbers in a range**
- **Perfect number**
- **Sum of factors**
