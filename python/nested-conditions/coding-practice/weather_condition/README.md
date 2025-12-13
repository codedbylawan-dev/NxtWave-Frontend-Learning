# ✅ **Weather Condition**

---

## **1️⃣ Question**

Given a real number **T** representing temperature, print the correct weather condition:

- **T < 0** → _Freezing weather_
- **0 ≤ T < 10** → _Very Cold weather_
- **10 ≤ T < 20** → _Cold weather_
- **20 ≤ T < 30** → _Normal_
- **30 ≤ T < 40** → _Hot_
- **T ≥ 40** → _Very Hot_

---

## **1.5️⃣ Category**

Conditional Statements → Temperature Classification → Ranged Logic

---

## **2️⃣ Outline**

- Read T
- Check temperature range
- Print corresponding message

---

## **3️⃣ Objective**

To classify temperature into correct weather categories using range-based conditions.

---

## **4️⃣ Purpose**

This builds confidence in handling multiple ordered ranges with chained conditions.

---

## **5️⃣ Theory**

Ranges must be checked **in order**:

| Range    | Output            |
| -------- | ----------------- |
| T < 0    | Freezing weather  |
| 0–9.9…   | Very Cold weather |
| 10–19.9… | Cold weather      |
| 20–29.9… | Normal            |
| 30–39.9… | Hot               |
| ≥ 40     | Very Hot          |

---

## **6️⃣ Step-by-Step Explanation**

1. Read T as a float
2. If T < 0 → print Freezing weather
3. Else if T < 10 → print Very Cold weather
4. Else if T < 20 → print Cold weather
5. Else if T < 30 → print Normal
6. Else if T < 40 → print Hot
7. Else → print Very Hot

---

## **7️⃣ Method**

Use chained comparisons with `if–elif–else` ensuring order from smallest to largest.

---

## **8️⃣ Constraints**

- T is a float
- Output text must match exactly
- Temperature ranges do not overlap

---

## **9️⃣ Common Mistakes**

❌ Checking ranges in wrong order
❌ Missing equality or adding unnecessary boundaries
❌ Misspelling output strings

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
T = float(input())

if T < 0:
    print("Freezing weather")
elif T < 10:
    print("Very Cold weather")
elif T < 20:
    print("Cold weather")
elif T < 30:
    print("Normal")
elif T < 40:
    print("Hot")
else:
    print("Very Hot")
```

---

## **1️⃣2️⃣ Example**

### Input

```
-50.0
```

### Output

```
Freezing weather
```

---

## **1️⃣3️⃣ Dry Run**

| T     | Condition Met | Output            |
| ----- | ------------- | ----------------- |
| -50.0 | T < 0         | Freezing weather  |
| 5.7   | T < 10        | Very Cold weather |
| 15.0  | T < 20        | Cold weather      |
| 25.3  | T < 30        | Normal            |
| 33.8  | T < 40        | Hot               |
| 42.0  | T ≥ 40        | Very Hot          |

---

## **1️⃣4️⃣ Test Cases Table**

| T     | Output            |
| ----- | ----------------- |
| -50.0 | Freezing weather  |
| 5.7   | Very Cold weather |
| 12.3  | Cold weather      |
| 28.9  | Normal            |
| 35.0  | Hot               |
| 40.0  | Very Hot          |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always sort your conditions from smallest to largest range
- Ranged conditions are much simpler with ordered comparisons
- Float comparisons work the same as integer comparisons

---

## **1️⃣6️⃣ Real-Life Application**

- Weather reporting systems
- Sensor threshold classification
- Smart home heating and cooling automation

---

## **1️⃣7️⃣ Practice Questions**

1. Categorize speed into Slow/Normal/Fast/Very Fast ranges.
2. Categorize BMI into Underweight/Normal/Overweight/Obese.
3. Categorize marks into Grade A–F based on ranges.

---

## **1️⃣8️⃣ Result**

The program accurately prints the correct weather condition based on temperature.

---

## **1️⃣9️⃣ Conclusion**

A perfect problem for mastering ordered range conditions—an essential skill for real-world decision-making programs.

---
