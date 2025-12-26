# ✅ **Sum of N Terms in the Series**

---

## **1️⃣ Question**

Given two numbers **X** and **N**, print the **sum of N terms** in the following series:

```
X, -X³, X⁵, -X⁷, X⁹, ...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Series → Power → Conditional Logic

---

## **2️⃣ Objective**

To calculate the **sum of a power series** where:

- powers are **odd numbers**
- signs **alternate (+, −, +, −, …)**

---

## **3️⃣ Pattern Understanding (VERY IMPORTANT)**

### 🔹 Power pattern

- 1st term → power = `1`
- 2nd term → power = `3`
- 3rd term → power = `5`
- 4th term → power = `7`

👉 Power formula:

```
power = 2 * term_number - 1
```

---

### 🔹 Sign pattern

- Odd term → **positive**
- Even term → **negative**

---

## **4️⃣ Step-by-Step Logic**

1. Read `X` and `N`
2. Initialize `total = 0`
3. Loop from `1` to `N`
4. For each term:

   - Find power = `2*i - 1`
   - Calculate value = `X ** power`
   - If term number is even → make it negative

5. Add value to `total`
6. Print `total`

---

## **5️⃣ Code (BEGINNER-SAFE & CORRECT)**

```python
X = int(input())
N = int(input())

total = 0

for i in range(1, N + 1):
    power = 2 * i - 1
    value = X ** power

    if i % 2 == 0:
        value = -value

    total = total + value

print(total)
```

---

## **6️⃣ Example 1**

### Input

```
2
5
```

### Terms

```
2¹   = 2
-2³  = -8
2⁵   = 32
-2⁷  = -128
2⁹   = 512
```

### Output

```
410
```

---

## **7️⃣ Example 2**

### Input

```
3
2
```

### Terms

```
3¹  = 3
-3³ = -27
```

### Output

```
-24
```

---

## **8️⃣ Dry Run (X = 2, N = 3)**

| i   | power | value | sign | total |
| --- | ----- | ----- | ---- | ----- |
| 1   | 1     | 2     | +    | 2     |
| 2   | 3     | 8     | −    | -6    |
| 3   | 5     | 32    | +    | 26    |

---

## **9️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **🔟 Common Mistakes**

❌ Using even powers
❌ Forgetting sign change
❌ Using nested loops unnecessarily

---

## **1️⃣1️⃣ Key Takeaways**

✔ Odd powers increase by `+2`
✔ Sign depends on term position
✔ Simple `if` + `for` loop is enough
✔ No advanced math required

---

If you want, next we can do:

- **Same series using a running power**
- **Series with factorial**
- **Series with alternating numbers**
