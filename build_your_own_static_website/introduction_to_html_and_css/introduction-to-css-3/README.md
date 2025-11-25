# 🎨 **Introduction to CSS – Part 3 (Complete Notes + Analogies)**

---

# ⭐ 1. **Font Family (`font-family`)**

### ✅ **Definition**

The `font-family` property specifies **which font style** should be used for the text of an HTML element.

### 🎯 **What it does**

- Changes the visual style of text
- Makes the content feel modern, playful, professional, artistic, etc.
- Helps in improving readability and aesthetics

### 🔠 **Examples of font families**

- `"Roboto"`
- `"Open Sans"`
- `"Bree Serif"`
- `"Lobster"`
- `"Playfair Display"`
- `"Work Sans"`

### 📌 **Important Notes**

- You must **import** fonts from Google Fonts (or another source) before using them.
- Font name must be inside **quotation marks** `" "`.
- Be careful of **spelling mistakes** — even a small mistake breaks the font.

### ✔️ Example Code

```css
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");

.main-heading {
  font-family: "Roboto";
}

.paragraph {
  font-family: "Roboto";
}
```

### 🎨 **Analogy**

Choosing a `font-family` is like choosing the **handwriting style** for your notebook.

- Roboto → clean handwriting
- Lobster → fancy handwriting
- Bree Serif → stylish and artistic handwriting

Each handwriting style gives a different feel to the text.

---

# ⭐ 2. **Font Size (`font-size`)**

### ✅ **Definition**

The `font-size` property sets the **size of the text**.

### 🎯 **What it does**

- Controls how big or small the text appears
- Helps create clear visual hierarchy (headings vs paragraphs)

### 📏 **Common Units**

- `px` → pixels (most commonly used)

### 📌 **Important Rules**

- Must add **px** after the number
- No space between number and px → `20px` (correct), `20 px` (wrong)
- Do not use quotation marks

### ✔️ Example Code

```css
.main-heading {
  font-size: 36px;
}

.paragraph {
  font-size: 28px;
}
```

### 📖 **Analogy**

Font-size is like choosing the **font size in MS Word or Google Docs** —
You choose 36px for big headings, 20px for normal text, etc.

---

# ⭐ 3. **Font Style (`font-style`)**

### ✅ **Definition**

The `font-style` property specifies the **stylized effect** of the text.

### 📝 **Possible Values**

| Value     | Description                         |
| --------- | ----------------------------------- |
| `normal`  | Regular text                        |
| `italic`  | Slanted/italic text                 |
| `oblique` | Slightly slanted text (less common) |

### ✔️ Example Code

```css
.main-heading {
  font-style: italic;
}

.paragraph {
  font-style: normal;
}
```

### 📌 **Important Notes**

- No quotation marks for values
- Spelling must be accurate → _italic_, _normal_, _oblique_

### ✍️ **Analogy**

Font-style is like choosing the **style of writing**:

- _normal_ → regular writing
- _italic_ → slanted writing
- _oblique_ → slanted but less fancy

It adds personality to your text.

---

# ⭐ 4. **Full Example Combining All Font Properties**

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");

      .main-heading {
        font-family: "Roboto";
        font-size: 36px;
        font-style: italic;
      }

      .paragraph {
        font-family: "Roboto";
        font-size: 28px;
        font-style: normal;
      }
    </style>
  </head>

  <body>
    <h1 class="main-heading">Tourism</h1>
    <p class="paragraph">Plan your trip wherever you want to go</p>
  </body>
</html>
```

---

# 🎯 **Learning Checkpoints — Part 3 Completed**

### ✅ You understand what `font-family` does

### ✅ You know how to import Google Fonts

### ✅ You know the rules for using fonts correctly

### ✅ You can apply font sizes using `px`

### ✅ You know different font styles (normal, italic, oblique)

### ✅ You can combine all font properties in real code

---
