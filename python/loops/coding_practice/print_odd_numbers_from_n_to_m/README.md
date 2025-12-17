# ✅ **Print Odd Numbers from N to M**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print all the **odd numbers from N to M** separated by a space.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Reverse Order

---

## **2️⃣ Outline**

- Read M
- Read N
- Start from N and go till M
- Check if a number is odd
- Store odd numbers in order
- Print them in one line separated by space

---

## **3️⃣ Objective**

To print **odd numbers in reverse order** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- reverse looping
- odd number checking
- building output using strings

---

## **5️⃣ Theory**

- A number is **odd** if `number % 2 != 0`
- To move from bigger to smaller numbers, we loop **backwards**
- Since output must be in **one line**, we can build a string

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Create an empty string to store output
3. Start a loop from N to M (reverse)
4. Check if the number is odd
5. If odd, add it to the output string with a space
6. After loop ends, print the final string

---

## **7️⃣ Method**

Use:

- input()
- for loop
- modulo operator (%)
- string concatenation
- print()

---

## **8️⃣ Constraints**

- N is greater than or equal to M
- Output should be in one line
- Numbers must be space-separated

---

## **9️⃣ Common Mistakes**

❌ Printing even numbers
❌ Looping in the wrong direction
❌ Printing each number on a new line

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

result = ""

for i in range(N, M - 1, -1):
    if i % 2 != 0:
        result = result + str(i) + " "

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
1
10
```

### Output

```
9 7 5 3 1
```

---

## **1️⃣3️⃣ Dry Run**

M = 1, N = 6

Loop values: 6 → 1

- 6 → even → skip
- 5 → odd → add
- 4 → skip
- 3 → add
- 2 → skip
- 1 → add

Final output → `5 3 1 `

---

## **1️⃣4️⃣ Test Cases Table**

| Input (M N) | Output    |
| ----------- | --------- |
| 1 10        | 9 7 5 3 1 |
| 5 9         | 9 7 5     |
| 2 7         | 7 5 3     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Reverse loops use a negative step
- Odd numbers are checked using `% 2`
- Strings help avoid advanced printing

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering data in reverse order
- Backward range processing
- Number pattern generation

---

## **1️⃣7️⃣ Practice Questions**

1. Print even numbers from N to M
2. Print numbers divisible by 3 from N to M
3. Count odd numbers from N to M

---

## **1️⃣8️⃣ Result**

The program correctly prints **odd numbers from N to M** in one line.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **reverse looping**, **condition checking**, and **string building** using only basic concepts.

---
