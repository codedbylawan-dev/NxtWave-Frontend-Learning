# ✅ **Denominations**

---

## **1️⃣ Question**

Given an amount **N**, find the **minimum number of notes** needed using these denominations:

**1000, 500, 100, 50, 20, 5, 1**

Print the count of each note in the exact required format.

---

## **1.5️⃣ Category**

Math → Division & Remainder → Greedy Note Calculation

---

## **2️⃣ Outline**

- Read amount
- Find number of 1000 notes
- Subtract used amount
- Repeat for: 500 → 100 → 50 → 20 → 5 → 1
- Print counts

---

## **3️⃣ Objective**

Break an amount into the least number of currency notes.

---

## **4️⃣ Purpose**

Teaches greedy selection and remainder-based calculations.

---

## **5️⃣ Theory**

For each note:

```
count = amount // denomination
remaining = amount - (count * denomination)
```

Always subtract before moving to the next denomination.

---

## **6️⃣ Step-by-Step Explanation**

1. Divide N by 1000 → get count
2. Subtract (count × 1000)
3. Continue with 500
4. Continue with 100
5. Continue with 50
6. Continue with 20
7. Continue with 5
8. Remaining amount = 1 notes

---

## **7️⃣ Method**

Sequential division using integer division (`//`) and subtraction.

---

## **8️⃣ Constraints**

- N ≥ 0
- Output format must match exactly

---

## **9️⃣ Common Mistakes**

❌ Forgetting to update remaining amount
❌ Printing notes in wrong order
❌ Using float division

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

a = N // 1000
N = N - a * 1000

b = N // 500
N = N - b * 500

c = N // 100
N = N - c * 100

d = N // 50
N = N - d * 50

e = N // 20
N = N - e * 20

f = N // 5
N = N - f * 5

g = N // 1
N = N - g * 1

print("1000:" + str(a))
print("500:" + str(b))
print("100:" + str(c))
print("50:" + str(d))
print("20:" + str(e))
print("5:" + str(f))
print("1:" + str(g))
```

---

## **1️⃣2️⃣ Example**

### Input

```
8593
```

### Output

```
1000:8
500:1
100:0
50:1
20:2
5:0
1:3
```

---

## **1️⃣3️⃣ Dry Run**

Amount = 4

- 4 // 1000 → 0
- 4 // 500 → 0
- 4 // 100 → 0
- 4 // 50 → 0
- 4 // 20 → 0
- 4 // 5 → 0
- 4 // 1 → 4

Output:

```
1000:0
500:0
100:0
50:0
20:0
5:0
1:4
```

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Expected Output (1:line) |
| ----- | ------------------------ |
| 0     | all zeros                |
| 5     | 5:1, rest 0              |
| 1520  | 1000:1 500:1 20:1 etc.   |
| 9999  | 1000:9 500:1 100:4 ...   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use greedy from **largest to smallest** note
- Always subtract after each step
- Exact output format is important

---

## **1️⃣6️⃣ Real-Life Application**

- ATM note distribution
- Cashier systems
- Currency breakdown calculators

---

## **1️⃣7️⃣ Practice Questions**

1. Do the same logic for coins: 10, 5, 2, 1
2. Add 2000 denomination
3. Reverse: calculate maximum number of notes

---

## **1️⃣8️⃣ Result**

You can now compute currency note breakdown efficiently.

---

## **1️⃣9️⃣ Conclusion**

Greedy logic + simple arithmetic = perfectly optimized solution.

---
