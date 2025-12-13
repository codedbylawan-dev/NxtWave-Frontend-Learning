# ✅ **Hand Game**

---

## **1️⃣ Question**

Given two strings showing what **Abhinav** and **Anjali** selected in Rock–Paper–Scissors, print:

- **Abhinav Wins**
- **Anjali Wins**
- **Tie**

based on the game rules.

---

## **1.5️⃣ Category**

Conditional Statements → Multi-condition Decision Making → String Comparison

---

## **2️⃣ Outline**

- Read Abhinav’s choice
- Read Anjali’s choice
- Check if both are the same → Tie
- Otherwise check winning combinations for Abhinav
- Otherwise Anjali wins

---

## **3️⃣ Objective**

To determine the winner of the Rock–Paper–Scissors game using conditional logic.

---

## **4️⃣ Purpose**

Improves ability to handle multiple condition checks and compare string inputs logically.

---

## **5️⃣ Theory**

Game rules:

- **Rock beats Scissors**
- **Scissors beats Paper**
- **Paper beats Rock**
- Same symbol → **Tie**

---

## **6️⃣ Step-by-Step Explanation**

1. Read both inputs
2. Compare them:

   - If equal → Tie

3. If not equal → check Abhinav's winning cases
4. Otherwise → Anjali Wins

---

## **7️⃣ Method**

Use:

- `if`
- `elif`
- `else`
- string equality (`==`)

---

## **8️⃣ Constraints**

- Inputs will be valid words: Rock, Paper, Scissors
- Case-sensitive (use exact text)

---

## **9️⃣ Common Mistakes**

❌ Misspelling input words
❌ Confusing winning rules
❌ Not checking tie first

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
abhinav = input()
anjali = input()

if abhinav == anjali:
    print("Tie")
elif (abhinav == "Rock" and anjali == "Scissors") or \
     (abhinav == "Scissors" and anjali == "Paper") or \
     (abhinav == "Paper" and anjali == "Rock"):
    print("Abhinav Wins")
else:
    print("Anjali Wins")
```

---

## **1️⃣2️⃣ Example**

### Input

```
Rock
Paper
```

### Output

```
Anjali Wins
```

---

## **1️⃣3️⃣ Dry Run**

For:

```
Scissors
Rock
```

- Not a tie
- Check Abhinav’s winning cases → Scissors beating Rock? ❌
- So → **Anjali Wins**

---

## **1️⃣4️⃣ Test Cases Table**

| Abhinav  | Anjali   | Winner       |
| -------- | -------- | ------------ |
| Rock     | Paper    | Anjali Wins  |
| Rock     | Scissors | Abhinav Wins |
| Paper    | Paper    | Tie          |
| Scissors | Paper    | Abhinav Wins |
| Paper    | Rock     | Abhinav Wins |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always check tie first
- Game is based on 3 fixed comparisons
- Use OR (`or`) for multiple winning cases

---

## **1️⃣6️⃣ Real-Life Application**

- Game logic
- Decision-making systems
- Validating rule-based outcomes

---

## **1️⃣7️⃣ Practice Questions**

1. Create a game for Odd–Even.
2. Create a 3-choice game with custom rules.
3. Write a program to compare two cards (rank-based).

---

## **1️⃣8️⃣ Result**

The program correctly identifies the winner or tie for any valid input.

---

## **1️⃣9️⃣ Conclusion**

A clear conditional-logic problem that strengthens your ability to compare multiple choices and apply rule-based decisions.

---
