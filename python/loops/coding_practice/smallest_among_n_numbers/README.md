# ✅ **Smallest Among N Numbers**

---

## **1️⃣ Question**

Given a number **N**, read **N integers** and print the **smallest number** among them.

---

## **1️⃣.5️⃣ Category**

For Loop → Comparison → Minimum Value

---

## **2️⃣ Outline**

- Read N
- Read the first number and store it as smallest
- Read remaining numbers one by one
- Compare each number with smallest
- Update smallest if needed
- Print smallest

---

## **3️⃣ Objective**

To find the **minimum value** from multiple inputs using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- comparing numbers
- maintaining a running minimum
- using loop-based input handling

---

## **5️⃣ Theory**

To find the smallest number:

- Assume the **first input** is the smallest
- Compare it with every next number
- Replace it if a smaller number is found

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Read the first number → store in `smallest`
3. Loop from 2nd input to Nth input
4. If current number < smallest

   - update smallest

5. Print smallest

---

## **7️⃣ Method**

Use:

- for loop
- comparison operator `<`
- variable to track smallest value

---

## **8️⃣ Constraints**

- N ≥ 1
- Inputs can be positive or negative integers

---

## **9️⃣ Common Mistakes**

❌ Initializing smallest as 0
❌ Not reading first input separately
❌ Printing smallest inside loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

smallest = int(input())

for i in range(N - 1):
    number = int(input())
    if number < smallest:
        smallest = number

print(smallest)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
8
11
96
49
25
```

### Output

```
8
```

---

## **1️⃣3️⃣ Dry Run**

Inputs: `8, 11, 96, 49, 25`

- smallest = 8
- 11 > 8 → no change
- 96 > 8 → no change
- 49 > 8 → no change
- 25 > 8 → no change

Final smallest → **8**

---

## **1️⃣4️⃣ Test Cases Table**

| Input Numbers | Output |
| ------------- | ------ |
| 8 11 96 49 25 | 8      |
| 10 10 10      | 10     |
| -5 -2 -9      | -9     |
