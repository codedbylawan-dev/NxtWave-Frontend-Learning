# Compare Last Three Characters — Solved

**Medium**

---

## Outline

**Question:** Compare Last Three Characters
**Approach**
Step 1: Read the input strings
Step 2: Extract the last three characters
Step 3: Compare them
Step 4: Print the result

---

## Approach

To solve this problem:

1. Read both strings.
2. Slice the last three characters using `[-3:]`.
3. Compare both slices.
4. Print **True** if equal, otherwise **False**.

---

## Step-by-Step Explanation

### **Step 1: Read the input strings**

```python
str1 = input()
str2 = input()
```

### **Step 2: Extract the last three characters**

```python
part1 = str1[-3:]
part2 = str2[-3:]
```

### **Step 3: Compare**

```python
result = part1 == part2
```

### **Step 4: Print**

```python
print(result)
```

---

## Solution

```python
str1 = input()
str2 = input()

part1 = str1[-3:]
part2 = str2[-3:]

result = part1 == part2
print(result)
```

---

# DRY RUN (Tabular Format)

---

## **Sample Input 1**

```
apple
pimple
```

| Step | Operation                    | Value                       |
| ---- | ---------------------------- | --------------------------- |
| 1    | Read str1                    | "apple"                     |
| 2    | Read str2                    | "pimple"                    |
| 3    | Extract last 3 chars of str1 | "ple"                       |
| 4    | Extract last 3 chars of str2 | "ple"                       |
| 5    | Compare                      | `"ple" == "ple"` → **True** |
| 6    | Output                       | True                        |

**Output**

```
True
```

---

## **Sample Input 2**

```
meals
deal
```

| Step | Operation                    | Value                        |
| ---- | ---------------------------- | ---------------------------- |
| 1    | Read str1                    | "meals"                      |
| 2    | Read str2                    | "deal"                       |
| 3    | Extract last 3 chars of str1 | "als"                        |
| 4    | Extract last 3 chars of str2 | "eal"                        |
| 5    | Compare                      | `"als" == "eal"` → **False** |
| 6    | Output                       | False                        |

**Output**

```
False
```

---
