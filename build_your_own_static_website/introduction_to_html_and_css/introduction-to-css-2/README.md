# 🎨 **Introduction to CSS – Part 2 (Complete Notes + Analogies)**

---

# ⭐ 1. CSS Text Property — **color**

### ✅ **Definition**

The `color` property sets the **text color** of an HTML element.

### 🎯 **What it does**

- Changes how the text appears visually.
- Can take named colors, HEX codes, RGB, HSL, etc.

### 🔍 **Examples of color values**

- `blue`
- `grey`
- `lightblue`
- `orange`
- `red`
- `green`

### 📘 Example

```css
.main-heading {
  color: blue;
}

.paragraph {
  color: grey;
}
```

### 🎨 **Analogy**

The `color` property is like choosing the **ink color** for writing text on a paper.

You choose:

- Blue ink
- Red ink
- Black ink
- etc.

That’s exactly what CSS does for text on your page.

---

# ⭐ 2. CSS Background Property — **background-color**

### ✅ **Definition**

The `background-color` property sets the **background color** of any HTML element.

This includes:

- div containers
- headings
- paragraphs
- buttons
- or any other block or inline element

### 🎯 **What it does**

- Fills the entire box area of the element with color.
- Makes content visually stand out.

### 📘 Example

```css
.card {
  background-color: lightblue;
}
```

### 🔍 **More clarity**

If you apply `background-color` to a container (like `<div>`), everything inside it will sit on that color.

### 🧩 **Analogy**

Think of `background-color` as the **color of the paper** you are writing on.

- If the paper is light blue → text stands out differently
- Changing paper color gives a different visual appearance

---

# ⭐ 3. Combined Example (HTML + CSS)

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .main-heading {
        color: blue;
      }
      .paragraph {
        color: grey;
      }
      .card {
        background-color: lightblue;
      }
    </style>
  </head>

  <body>
    <div class="card">
      <h1 class="main-heading">Tourism</h1>
      <p class="paragraph">Plan your trip wherever you want to go</p>
    </div>
  </body>
</html>
```

### ✔️ What this does:

- The `<div>` with class `card` gets a **light blue background**
- `<h1>` text becomes **blue**
- `<p>` text becomes **grey**

---

# 🎯 **Learning Checkpoints — Part 2 Completed**

### ✅ You understand the `color` property

### ✅ You know how to set text colors using CSS

### ✅ You know what `background-color` does

### ✅ You can apply background colors to containers or any elements

### ✅ You can combine text color + background color properly

---
