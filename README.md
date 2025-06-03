# Utlib - Utility Library

**utlib** is a lightweight and customizable utility library designed to simplify everyday Python programming.  
Created by Myroslav Repin, the project is in **active development** and will continue to grow with new features and improvements.

---

## ✨ Current Features

- `digit_sum(n)`

  - Returns the sum of all digits in an integer.
  - Example: `digit_sum(1234)` → `10`

- `is_palindrome(text)`

  - Checks if a given string is a palindrome (reads the same forwards and backwards).
  - Example: `is_palindrome("level")` → `True`

- `vowels(lang='eng', consonants=False)`

  - Returns the list of vowels of supported languages including: English (eng), Russian (ru), Spanish (es), French (fr), German (de)
  - Using secong parametr of the function you can select which list you want to return: vowels or consonants

- `average_value(values, decimal, get_nearest_value)`

  - Returns the average of a list of numbers, rounded to the given decimal places.
  - Can return nearest value from the list to average
  - Currently `average_value()` is supporting floats
  - Example:

    ```python
    average_value([1, 2, 3, 4, 5], 2)        # → 3.00
    average_value([1, 2, 3, 4, 5], 5)  # → 3.00000
    ```

- `remove_vowels(text, lang, consonants)`
  - Returns the string without vowels
  - Using `consonants=True` function return string with vowels only
  - Function returning now **lower case** only
  - `lang` by default is **eng**, supporting languages: **eng, ru, fr, es, de**
- `count_words(text, min_lenght, max_lenght)`
  - Number of words in `text` with length greater than or equal to `min_lenght`.
  - Now supporting `max_lenght` as an atribute.
  - `text` — input string.
  - `min_lenght` — minimum word length (integer).
- `get_size(path)`
  - Returns the size of a file or directory

---

## 🚧 Planned Features

- **Advanced math helpers**
- Filtering tools
- Custom data structures
- Useful decorators and wrappers
- Useful function

---

## 📦 Installation

To install the latest version from [PyPI](https://pypi.org/project/utlib), use:

```bash
pip install utlib
```

---

## 📄 Documentation

Official documentation is coming soon.
For now, explore the source code and **README** and **Docs** understand available functionality.

If you have any ideas or requests for the documentation, feel free to share!

---

## 💌 Feedback & Contact

If you find a bug or want to request a feature:

📧 Email: [myroslavrepin@gmail.com](mailto:myroslavrepin@gmail.com)
📁 GitHub: [github.com/MyroslavRepin/utlib](https://github.com/MyroslavRepin/utlib)

---

## 📌 License

> This project is licensed under the [MIT License](LICENSE).
