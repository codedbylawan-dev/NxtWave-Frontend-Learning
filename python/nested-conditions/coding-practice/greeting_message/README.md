# ✅ **Greeting Message**

---

## **1️⃣ Question**

Read an integer representing the **time of day** and print the correct greeting:

- **4 ≤ time < 12** → “Good Morning”
- **12 ≤ time < 16** → “Good Afternoon”
- **16 ≤ time < 20** → “Good Evening”
- **time ≥ 20 or time < 4** → “Good Night”

---

## **1.5️⃣ Category**

Conditional Statements → Time-based Greetings → Range Checking

---

## **2️⃣ Outline**

- Read time
- Check which time range it belongs to
- Print the corresponding greeting

---

## **3️⃣ Objective**

To classify a number into one of four time ranges and print the correct greeting.

---

## **4️⃣ Purpose**

This strengthens range-checking logic and ordered condition evaluation.

---

## **5️⃣ Theory**

Time ranges are **mutually exclusive**:

### Morning

[
4 \leq T < 12
]

### Afternoon

[
12 \leq T < 16
]

### Evening

[
16 \leq T < 20
]

### Night

[
T \geq 20 \quad \text{or} \quad T < 4
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read the time value
2. Check if between 4 and 12 → Morning
3. Else check if between 12 and 16 → Afternoon
4. Else check if between 16 and 20 → Evening
5. Else → Night
6. Print greeting

---

## **7️⃣ Method**

- Use ordered `if–elif–else`
- Combine comparisons with `>=` and `<`
- Use OR (`or`) for Night condition

---

## **8️⃣ Constraints**

- Input is an integer time
- Output must be exactly one greeting
- No extra text

---

## **9️⃣ Common Mistakes**

❌ Mixing up `<` and `<=`
❌ Incorrect Night condition placement
❌ Printing multiple greetings
❌ Typos in greeting strings

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
T = int(input())

if T >= 4 and T < 12:
    print("Good Morning")
elif T >= 12 and T < 16:
    print("Good Afternoon")
elif T >= 16 and T < 20:
    print("Good Evening")
else:
    print("Good Night")
```

---

## **1️⃣2️⃣ Example**

### Input

```
9
```

### Output

```
Good Morning
```

---

## **1️⃣3️⃣ Dry Run**

| Time | Morning? | Afternoon? | Evening? | Output         |
| ---- | -------- | ---------- | -------- | -------------- |
| 9    | Yes      | No         | No       | Good Morning   |
| 14   | No       | Yes        | No       | Good Afternoon |
| 18   | No       | No         | Yes      | Good Evening   |
| 2    | No       | No         | No       | Good Night     |
| 22   | No       | No         | No       | Good Night     |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output         |
| ----- | -------------- |
| 9     | Good Morning   |
| 14    | Good Afternoon |
| 18    | Good Evening   |
| 22    | Good Night     |
| 1     | Good Night     |
| 4     | Good Morning   |
| 12    | Good Afternoon |
| 16    | Good Evening   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Check ranges in ascending order
- Use `else` to cover the night condition
- Time-based mapping is a common pattern

---

## **1️⃣6️⃣ Real-Life Application**

- UI greeting messages
- Automated scheduling systems
- Smart home assistants reacting to time

---

## **1️⃣7️⃣ Practice Questions**

1. Print meal type based on time (Breakfast, Lunch, Snacks, Dinner).
2. Categorize temperature into Cold, Warm, Hot.
3. Print traffic-light color based on a given number.

---

## **1️⃣8️⃣ Result**

The program accurately prints the greeting based on the given time range.

---

## **1️⃣9️⃣ Conclusion**

A perfect exercise to practice range-based conditional logic — essential for many decision-making programs.

---
