# String Processor — Python Unit Testing

A beginner-friendly Python project that performs basic string operations and uses the built-in `unittest` framework to test the functions.

## Features

- **Reverse a String:** Reverses a string using Python slicing.
- **Count Vowels:** Counts uppercase and lowercase vowels (`a`, `e`, `i`, `o`, `u`).
- **Count Words:** Counts words in a string using Python's `split()` method.
- **Unit Testing:** Tests function outputs, return types, and error handling.

## Project Structure

```text
String-Processor/
├── main.py
├── test.py
└── README.md
```

## Requirements

- Python 3.x
- No external libraries required.

## How to Run

### 1. Run the main program

Open a terminal in the project directory and run:

```bash
python main.py
```

Expected output:

```text
dlrow olleH
3
2
```

### 2. Run the unit tests

Execute the following command:

```bash
python -m unittest -v
```

This runs the test cases in `test.py` and displays which tests pass or fail.

## Functions

### `reverse(string)`

Reverses the characters in a string.

```python
reverse("Python")
# Output: nohtyP
```

### `count_vowels(string)`

Counts all uppercase and lowercase vowels in a string.

```python
count_vowels("Hello world")
# Output: 3
```

Passing `None` raises a `TypeError` because `None` cannot be iterated over.

### `count_words(text)`

Counts the words separated by whitespace. An empty string returns `0`.

```python
count_words("Python is great")
# Output: 3
```

## Unit Tests

The `test.py` file contains three test methods:

| Test Method | What It Tests |
|---|---|
| `test_reverse()` | String reversal, empty strings, and return type |
| `test_count_vowels()` | Vowel count, return type, and error handling |
| `test_count_words()` | Word count, empty strings, and return type |

The project uses these `unittest` assertions:

- `assertEqual()` — checks whether two values are equal.
- `assertNotEqual()` — checks whether two values differ.
- `assertIsInstance()` — checks the result's data type.
- `assertRaises()` — checks whether a function raises an expected exception.

## Technologies Used

- Python 3
- Python `unittest` module

## Learning Objectives

This project demonstrates:

- Python functions and string manipulation.
- String slicing and loops.
- Conditional statements.
- Exception testing.
- Writing and running unit tests.
- Verifying expected results with assertions.

## License

Free to use for educational and personal learning purposes.
