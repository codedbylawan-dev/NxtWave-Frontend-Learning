# 🎁 **CSS Box Model — Part 2 (Borders Explained Clearly)**

---

# ⭐ 1. **Border Width (`border-width`)**

### ✅ **Definition**

The `border-width` property specifies **how thick** the border of an element should be.

### ✔️ Example

```css
.button {
  border-width: 2px;
}
```

### 📘 Special Case: Remove Border

```css
border-width: 0px;
```

This removes the border completely.

### ⚠️ Important Warning

To make borders visible, you **must** set:

- `border-style`
- (optional) `border-color`
- (optional) `border-width`

If `border-style` is missing, **the border will not appear**, even if color or width is provided.

### ✔️ Exception

The `<button>` element has a border by default, so it shows even without manual `border-style`.

### 🎨 **Analogy**

Border width is like deciding **how thick the outline** of a card or box should be.

---

# ⭐ 2. **Border Radius (`border-radius`)**

### ✅ **Definition**

The `border-radius` property makes the **corners of an element rounded**.

### ✔️ Example

```css
.button {
  border-radius: 20px;
}
```

### 🔍 **Specific Corner Rounding**

You can round each corner separately:

| Property                     | Corner              |
| ---------------------------- | ------------------- |
| `border-top-left-radius`     | Top-left corner     |
| `border-top-right-radius`    | Top-right corner    |
| `border-bottom-left-radius`  | Bottom-left corner  |
| `border-bottom-right-radius` | Bottom-right corner |

### 📌 Quick Tip

Applying a **background color** makes rounded corners more visible.

### 🎨 **Analogy**

Border radius is like trimming the sharp corners of a photo or ID card to make it look smooth.

---

# ⭐ 3. **Border Color (`border-color`)**

### ✅ **Definition**

The `border-color` property sets the **color** of an element’s border.

### ✔️ Example

```css
.button {
  border-color: orange;
}
```

### ⚠️ Important Warning

You **must** specify `border-style` or else:

- `border-width` will not show
- `border-color` will not show
- The border becomes invisible

Example of visible border:

```css
.button {
  border-style: solid;
  border-color: orange;
  border-width: 2px;
}
```

### ✔️ Exception

HTML `<button>` automatically has a visible border.

### 🎨 **Analogy**

Border color is like choosing the **ink color** for drawing a rectangle outline around something.

---

# ⭐ 4. **Full Example Using All Border Properties**

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .button {
        height: 50px;
        width: 150px;
        background-color: lightblue;

        /* Border Properties */
        border-style: solid;
        border-width: 3px;
        border-color: orange;
        border-radius: 20px;
      }
    </style>
  </head>

  <body>
    <button class="button">Get Started</button>
  </body>
</html>
```

### 🎯 What this code does

- Height + width → size of button
- Background color → makes border radius visible
- Border width → thickness
- Border color → orange border
- Border radius → smooth, rounded corners

---

# 🎯 **Learning Checkpoints — Part 2 Completed**

### ✅ You understand `border-width`

### ✅ You know border won’t show unless `border-style` is set

### ✅ You understand how to round corners using `border-radius`

### ✅ You know how to round individual corners

### ✅ You can apply `border-color` properly

### ✅ You can combine all border properties in code

---
