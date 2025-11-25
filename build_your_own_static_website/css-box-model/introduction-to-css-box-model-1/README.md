# 🌐 **CSS Box Model — Introduction (Part 1)**

---

# 🎁 **What is the CSS Box Model? (Simple Overview)**

Every HTML element is treated like a **box**.

This box has:

- Width
- Height
- Background
- Padding
- Border
- Margin

In this part, we focus on **height, width, background-image, background-size, viewport units**.

Analogy:
Think of each HTML element as a **cardboard box** that can have:

- a fixed size,
- an image printed on it,
- and can fill the entire screen.

---

# ⭐ 1. **Height (`height`)**

### ✅ **Definition**

The `height` property sets how **tall** an HTML element will be.

### ✔️ Example

```css
.card {
  height: 200px;
}
```

### 🎨 Analogy

The height of a box is like deciding **how tall your container should be**.

---

# ⭐ 2. **Width (`width`)**

### ✅ **Definition**

The `width` property sets how **wide** an HTML element will be.

### ✔️ Example

```css
.card {
  width: 250px;
}
```

### 🎨 Analogy

Width is like deciding **how wide your box should be**.

---

# ⭐ 3. **Background Image (`background-image`)**

### ✅ **Definition**

The `background-image` property sets an **image** behind the content of an HTML element.

### ✔️ Example

```css
.card {
  background-image: url("https://d2clawv67efefq.cloudfront.net/ccbp-static-website/ocean.jpg");
}
```

### 📌 Important Notes

- If **height is not specified**, the image height depends on content height.
- The URL _must be valid_.
- Image appears **behind** the text.

### 🎨 Analogy

`background-image` is like **wrapping your box with a printed design**.

---

# ⭐ 4. **Background Size (`background-size`)**

### ✅ **Definition**

The `background-size` property defines **how large the background image should appear**.

### ✔️ Example

```css
.card {
  background-size: cover;
}
```

### 📌 Value: `cover`

- Maintains **aspect ratio**
- Image fills the **entire width and height**
- May crop parts of the image

### 📏 **Aspect Ratio**

The ratio of image width to height (width ÷ height).

### 🎨 Analogy

Imagine sticking a large photo on a box —
You stretch it so it **covers the whole surface**, even if a little part gets cut off.

---

# ⭐ 5. **Viewport Units (`vh` & `vw`)**

## 🔹 **Viewport Height (`vh`)**

### ✅ **Definition**

- `1vh` = 1% of the browser's height
- `100vh` = complete height of the screen

### ✔️ Example

```css
.card {
  height: 50vh;
}
```

### 📌 Note

`100vh` makes the element take **the full screen height**.

### 🎨 Analogy

`vh` means “take this much percentage of the screen’s height”.

---

## 🔹 **Viewport Width (`vw`)**

### ✅ **Definition**

- `1vw` = 1% of the browser's width
- `100vw` = complete width of the screen

### ✔️ Example

```css
.card {
  width: 100vw;
}
```

### 📌 Note

`100vw` makes the element cover the **entire screen width**.

### 🎨 Analogy

`vw` means “take this much percentage of the screen’s width”.

---

# ⭐ 6. **Combined Example (Height, Width, Background)**

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .card {
        height: 200px;
        width: 250px;
        background-image: url("https://d2clawv67efefq.cloudfront.net/ccbp-static-website/ocean.jpg");
        background-size: cover;
      }
    </style>
  </head>

  <body>
    <div class="card">
      <h1>Tourism</h1>
      <p>Plan your trip wherever you want to go</p>
      <button>Get Started</button>
    </div>
  </body>
</html>
```

---

# 🎯 **Learning Checkpoints — Part 1 Completed**

### ✅ You understand height & width

### ✅ You know how to apply background images

### ✅ You understand why background-size: cover is used

### ✅ You know how viewport units (vh & vw) work

### ✅ You understand that HTML elements behave like boxes

---
