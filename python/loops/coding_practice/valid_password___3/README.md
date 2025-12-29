# ✅ **Valid Password – 3**

---

## **1️⃣ Question**

Given a password string, check whether it is **valid**.

A password is considered **valid** if it contains:

- at least **one uppercase letter**
- at least **one lowercase letter**
- at least **one digit**

Print **Valid Password** if it satisfies all conditions.
Otherwise, print **Invalid Password**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Validation

---

## **2️⃣ Outline**

- Read the password
- Initialize three flags
- Traverse each character
- Check for uppercase, lowercase, and digit
- Print result based on all flags

---

## **3️⃣ Objective**

To verify password strength using **multiple character rules**.

---

## **4️⃣ Purpose**

This problem trains you in:

- multi-condition validation
- combining multiple checks
- building strong input rules

---

## **5️⃣ Theory**

Character checks:

```python
ch.isupper()
ch.islower()
ch.isdigit()
```

A password is valid only when **all three conditions** are True.

---

## **6️⃣ Step-by-Step Explanation**

1. Read input string
2. Set:

   - `has_upper = False`
   - `has_lower = False`
   - `has_digit = False`

3. Loop through characters
4. Update flags using `isupper()`, `islower()`, `isdigit()`
5. After loop, check all flags
6. Print result

---

## **7️⃣ Method**

- One `for` loop
- Three flag variables
- Three string methods

---

## **8️⃣ Constraints**

- Output must be exactly:

  - `Valid Password`
  - `Invalid Password`

---

## **9️⃣ Common Mistakes**

❌ Using `elif` instead of independent checks
❌ Printing inside loop
❌ Forgetting one of the rules

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

has_upper = False
has_lower = False
has_digit = False

for ch in s:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True

if has_upper and has_lower and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")
```

---

## **1️⃣2️⃣ Example**

### Input

```
Qwerty00
```

### Output

```
Valid Password
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"Dashboard"`

Uppercase → True
Lowercase → True
Digit → False

Final → `Invalid Password`

---

## **1️⃣4️⃣ Test Cases Table**

| Input     | Output           |
| --------- | ---------------- |
| Qwerty00  | Valid Password   |
| Dashboard | Invalid Password |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Multi-rule validation is a professional-level pattern
- Independent checks prevent logical errors
- Flags simplify complex decisions

---

## **1️⃣6️⃣ Real-Life Application**

- Secure login systems
- Password policy enforcement
- Account security validation

---

## **1️⃣7️⃣ Practice Questions**

1. Add rule: at least one special character
2. Check minimum length
3. Count how many rules passed

---

## **1️⃣8️⃣ Result**

The program correctly validates passwords using all required conditions.

---

## **1️⃣9️⃣ Conclusion**

This problem upgrades your validation logic from **basic** to **real-world ready**.

---
