# ✅ **Perfect Squares in a Range (Beginner Version)**

---

## **1️⃣ Question**

Given two numbers **A** and **B**, print the **count of perfect squares** between **A and B** (inclusive).

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Counting

---

## **2️⃣ Outline**

- Read A and B
- Loop through numbers
- Find square using multiplication
- Check range using `if`
- Count valid squares
- Print the count

---

## **3️⃣ Objective**

To count perfect square numbers **without using loop controls** like `break`.

---

## **4️⃣ Purpose**

This problem helps you practice:

- `for` loop
- `if` condition
- number multiplication
- counting logic (same mindset as pattern rows)

---

## **5️⃣ Theory**

A **perfect square** looks like:

```
1 × 1 = 1
2 × 2 = 4
3 × 3 = 9
...
```

We generate square numbers and check if they fall between **A and B**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read A and B
2. Set `count = 0`
3. Loop `i` from 1 to B
4. Calculate `square = i * i`
5. If `square` is between A and B → increase count
6. After loop ends, print count

---

## **7️⃣ Method**

- Simple `for` loop
- Simple `if` condition
- No early stopping
- No loop control keywords

---

## **8️⃣ Constraints**

- A ≤ B
- A, B ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using `break`
❌ Using square root
❌ Checking every number in range

✅ Correct: generate squares using multiplication

---

## **🔟 Complexity**

- **Time:** O(B)
- **Space:** O(1)

(acceptable for learning stage)

---

## **1️⃣1️⃣ Code (ONLY what you learned)**

```python
A = int(input())
B = int(input())

count = 0

for i in range(1, B + 1):
    square = i * i
    if square >= A and square <= B:
        count = count + 1

print(count)
```

---

## **1️⃣2️⃣ Example**

### Input

```
9
100
```

### Output

```
8
```

---

## **1️⃣3️⃣ Dry Run**

For `A = 9`, `B = 100`

| i   | square | counted |
| --- | ------ | ------- |
| 1   | 1      | ❌      |
| 2   | 4      | ❌      |
| 3   | 9      | ✅      |
| 4   | 16     | ✅      |
| 5   | 25     | ✅      |
| 6   | 36     | ✅      |
| 7   | 49     | ✅      |
| 8   | 64     | ✅      |
| 9   | 81     | ✅      |
| 10  | 100    | ✅      |

Final count = **8**

---

## **1️⃣4️⃣ Notes / Key Takeaways**

- We **did not stop the loop**
- We only **filtered using if**
- Same logic as “print row only when condition matches”
- This matches your pattern-learning mindset

---

## **1️⃣5️⃣ Real-Life Application**

- Counting valid values
- Range filtering
- Data validation logic

---

## **1️⃣6️⃣ Practice Questions**

1. Count cubes (`i*i*i`) between A and B
2. Count even squares only
3. Print the squares instead of counting

---

## **1️⃣7️⃣ Result**

The program correctly counts perfect squares using **only basic concepts**.

---

## **1️⃣8️⃣ Conclusion**

This is **100% aligned** with what you’ve learned so far.
No shortcuts. No advanced tricks. Fully safe for your stage.
