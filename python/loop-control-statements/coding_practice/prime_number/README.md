# 🧩 **Prime Number**

---

## **1️⃣ Question**

Given an integer **N**, check whether it is a **Prime Number**.

Print
`Prime Number` if it is prime, otherwise print
`Not a Prime Number`.

---

## **2️⃣ Category**

**Numbers → Loops → Conditions**

---

## **3️⃣ Outline**

- Read **N**
- Count how many numbers divide **N**
- If count is `2` → Prime
- Else → Not Prime

---

## **4️⃣ Objective**

Learn how to **find factors** using a loop.

---

## **5️⃣ Purpose**

This teaches you:

- How to test divisibility
- How to count conditions using loops
- How to take a math rule and turn it into code

---

## **6️⃣ Theory**

A prime number has **only two divisors**:

- `1`
- the number itself

So if a number has **exactly 2 divisors**, it is prime.

---

## **7️⃣ Step-by-Step Explanation**

1. Read the number **N**
2. Set `count = 0`
3. Loop from `1` to `N`
4. If `N % i == 0`, increase `count`
5. After loop:

   - If `count == 2` → Prime
   - Else → Not Prime

---

## **8️⃣ Method**

Use a **for loop** and a **counter**.

---

## **9️⃣ Constraints**

Works for all positive integers.

---

## **🔟 Common Mistakes**

- Forgetting to include `1` in the loop
- Not resetting `count`
- Checking wrong condition at the end

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
n = int(input())

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
```

---

## **1️⃣3️⃣ Example**

### Input

```
5
```

### Output

```
Prime Number
```

---

## **1️⃣4️⃣ Dry Run**

For `n = 6`

Divisors found:
1, 2, 3, 6 → count = 4

Since `count != 2`
Output:

```
Not a Prime Number
```

---

## **1️⃣5️⃣ Test Cases Table**

| Input | Output             |
| ----- | ------------------ |
| 5     | Prime Number       |
| 6     | Not a Prime Number |
| 2     | Prime Number       |
| 1     | Not a Prime Number |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Prime = exactly **2 divisors**
- Loops can implement math rules
- Counting conditions is powerful

---

## **1️⃣7️⃣ Real-Life Application**

Prime logic is used in:

- Security systems
- Encryption
- Hashing
- Banking software

---

## **1️⃣8️⃣ Practice Questions**

1. Count primes between 1 and 50
2. Find the smallest prime greater than a given number
3. Check if two numbers are both prime

---

## **1️⃣9️⃣ Result**

You can now convert **math definitions into code**.

---

## **2️⃣0️⃣ Conclusion**

This is the foundation of algorithmic thinking.
You didn’t memorize.
You **built** the rule.

---
