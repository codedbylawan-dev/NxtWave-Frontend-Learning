# ✅ **Print Word**

---

## **1️⃣ Question**

Given a string, write a program to **print only the alphabets** present in the given string.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods

---

## **2️⃣ Outline**

- Read the input string
- Initialize an empty string
- Traverse each character using a `for` loop
- Check if the character is an alphabet
- Append it to the result
- Print the result

---

## **3️⃣ Objective**

To extract and print **only alphabet characters** from a string.

---

## **4️⃣ Purpose**

This problem helps in learning:

- string traversal using `for` loop
- filtering characters
- using the `isalpha()` string method
- building a new string step by step

---

## **5️⃣ Theory**

Python provides a built-in string method called **`isalpha()`**.

- `isalpha()` returns **True** if the character is an alphabet
- Returns **False** for digits, spaces, and special characters

Examples:

- `"c".isalpha()` → True
- `"R".isalpha()` → True
- `"1".isalpha()` → False
- `"#".isalpha()` → False

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Create an empty string `result`
3. Loop through each character in the string
4. Check if the character is an alphabet using `isalpha()`
5. If true, add it to `result`
6. After the loop, print `result`

---

## **7️⃣ Method**

- One `for` loop
- One `if` condition
- `isalpha()` string method
- String concatenation

---

## **8️⃣ Constraints**

- Input may contain special characters and symbols
- Output must contain **only alphabets**
- Order of characters must be preserved

---

## **9️⃣ Common Mistakes**

❌ Using ASCII comparisons unnecessarily
❌ Printing inside the loop
❌ Forgetting to initialize result string

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

result = ""

for ch in s:
    if ch.isalpha():
        result = result + ch

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
-c--a--r--
```

### Output

```
car
```

---

## **1️⃣3️⃣ Dry Run**

Input → `-p@t#h$o!n-`

- `p` → alphabet → result = `p`
- `t` → alphabet → result = `pt`
- `h` → alphabet → result = `pth`
- `o` → alphabet → result = `ptho`
- `n` → alphabet → result = `python`

Final Output → `python`

---

## **1️⃣4️⃣ Test Cases Table**

| Input               | Output |
| ------------------- | ------ |
| -c--a--r--          | car    |
| -p@@y--t##h@@o--n-- | python |
| ##c--o--d--e--r##   | coder  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `isalpha()` is the safest and cleanest check for letters
- Loop + condition + accumulation is a core pattern
- No extra concepts required

---

## **1️⃣6️⃣ Real-Life Application**

- Cleaning usernames
- Extracting words from noisy input
- Text preprocessing

---

## **1️⃣7️⃣ Practice Questions**

1. Print only digits from a string
2. Count alphabets in a string
3. Separate alphabets and special characters

---

## **1️⃣8️⃣ Result**

The program correctly prints **only alphabet characters** from the input string.

---

## **1️⃣9️⃣ Conclusion**

This problem perfectly reinforces **string traversal, conditions, and string methods** using only the concepts you’ve learned so far.
