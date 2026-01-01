# Nested Loops

An inner loop within the repeating block of an outer loop is called **Nested Loop**.

The **Inner Loop** will be executed **one time for each iteration** of the **Outer Loop**.

---

### Structure

```
for item in sequence A:      → Outer Loop
    Block 1
    for item in sequence B:  → Inner Loop
        Block 2
    Block 3
Block 4
```

---

## Code

```python
for i in range(2):
    print("Outer: " + str(i))
    for j in range(2):
        print("Inner: " + str(j))
```

---

## Output

```
Outer: 0
Inner: 0
Inner: 1
Outer: 1
Inner: 0
Inner: 1
```

---

# Nested Repeating Block

The one highlighted in the blue dotted line is the **repeating block of the inner loop**.

```
for item in sequence A:      → Outer Loop
    Block 1
    for item in sequence B:  → Inner Loop
        Block 2              → Repeating Block
    Block 3
Block 4
```

---

## Code

```python
for i in range(2):
    print("Outer: " + str(i))
    for j in range(2):
        print("Inner: " + str(j))
print("END")
```

---

## Repeating Block of Nested Loop

```python
print("Inner: " + str(j))
```

---

## Output

```
Outer: 0
Inner: 0
Inner: 1
Outer: 1
Inner: 0
Inner: 1
END
```

---

# Examples – Nested Loops

---

## Example – 1: While loop inside a For loop

```
for item in
    Block 1
    while condition:
        Block 2
    Block 3
Block 4
```

---

## Example – 2: While loop inside a while loop

```
while condition:
    Block 1
    while condition:
        Block 2
    Block 3
Block 4
```

---
