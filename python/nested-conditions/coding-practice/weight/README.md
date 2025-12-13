# ✅ **Weight**

---

## **1️⃣ Question**

Read the weight **W** of a box and check:

1. If **W ≥ 100**, print **"Box is Heavier"**
2. Else if **W ≥ 30**, print **"Box is Heavy"**

---

## **1.5️⃣ Category**

Conditional Statements → Range Classification

---

## **2️⃣ Outline**

- Read W
- If W ≥ 100 → print "Box is Heavier"
- Else if W ≥ 30 → print "Box is Heavy"

---

## **3️⃣ Objective**

To categorize the weight of a box based on two thresholds.

---

## **4️⃣ Purpose**

This problem strengthens understanding of ordered conditional checks.

---

## **5️⃣ Theory**

Two separate ranges:

[
W \ge 100
]

Else:

[
30 \le W < 100
]

Each condition produces a different output.

---

## **6️⃣ Step-by-Step Explanation**

1. Read W
2. If W ≥ 100 → print "Box is Heavier"
3. Else if W ≥ 30 → print "Box is Heavy"
4. End

---

## **7️⃣ Method**

- Use `if` + `elif`
- Use ≥ operator
- Print exact strings

---

## **8️⃣ Constraints**

- W is an integer
- Only one line of output
- Strings must match exactly

---

## **9️⃣ Common Mistakes**

❌ Using `>` instead of `>=`
❌ Printing both messages
❌ Checking the 30-condition before the 100-condition
❌ Wrong capitalization

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
W = int(input())

if W >= 100:
    print("Box is Heavier")
elif W >= 30:
    print("Box is Heavy")
```

---

## **1️⃣2️⃣ Example**

### Input

```
60
```

### Output

```
Box is Heavy
```

---

## **1️⃣3️⃣ Dry Run**

| W   | W ≥ 100 | W ≥ 30 | Output         |
| --- | ------- | ------ | -------------- |
| 60  | No      | Yes    | Box is Heavy   |
| 150 | Yes     | —      | Box is Heavier |
| 20  | No      | No     | _(no output)_  |

---

## **1️⃣4️⃣ Test Cases Table**

| W   | Output               |
| --- | -------------------- |
| 150 | Box is Heavier       |
| 100 | Box is Heavier       |
| 60  | Box is Heavy         |
| 30  | Box is Heavy         |
| 25  | _(nothing required)_ |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Order ensures correct category
- ≥ 100 overrides ≥ 30
- Only one message should be printed

---

## **1️⃣6️⃣ Real-Life Application**

- Categorizing parcel weights
- Shipping charges classification
- Industrial equipment sorting

---

## **1️⃣7️⃣ Practice Questions**

1. Print "Large", "Medium", or "Small" based on volume thresholds.
2. Check if speed is fast (>100), moderate (>60), or slow.
3. Categorize age into adult, teen, or child.

---

## **1️⃣8️⃣ Result**

The program correctly determines whether the box is _Heavy_ or _Heavier_.

---

## **1️⃣9️⃣ Conclusion**

A simple yet foundational conditional logic problem helping build structured decision-making in programs.

---

Say **Next** for the next problem.

# Weight

Problem description: _Add the problem statement here._

## How to run

```
python index.py
```

## Notes

- Fill input/output format and examples.
