# Student Grade System

A lightweight, beginner-friendly Python console application that calculates and assigns letter grades based on a student's numerical score (0–100). The program incorporates boundary checks and robust exception handling to ensure valid input.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Grading Scale](#grading-scale)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Installation & Execution](#installation--execution)
- [Example Usage & Test Cases](#example-usage--test-cases)
- [Technical Notes](#technical-notes)
- [Potential Enhancements](#potential-enhancements)
- [License](#license)

---

## Overview

The **Student Grade System** is designed to accept user input representing a student's exam or assignment score. It validates whether the score is within the accepted range (0 to 100), handles invalid inputs (such as non-numeric characters) without crashing, and assigns the appropriate letter grade based on standard institutional thresholds.

---

## Features

- **Input Validation**: Ensures that marks fall strictly within the inclusive range of `0` to `100`.
- **Exception Handling**: Uses Python's `try...except` construct to catch `ValueError` exceptions when non-numeric values are entered.
- **Decimal Support**: Accepts floating-point values initially, converting them safely for grading logic.
- **Clear Feedback**: Provides descriptive error messages if the input is out-of-range or malformed.

---

## Grading Scale

The program evaluates marks based on the following standard scale:

| Mark Range | Grade | Description |
| :---: | :---: | :--- |
| **90 – 100** | **A** | Excellent |
| **80 – 89**  | **B** | Very Good |
| **70 – 79**  | **C** | Good / Satisfactory |
| **60 – 69**  | **D** | Pass |
| **0 – 59**   | **E** | Fail / Unsatisfactory |

---

## How It Works

1. **Prompt for Input**: The program prompts the user with `Enter Your Mark (0-100): `.
2. **Float Parsing**: The input string is converted into a `float` to permit decimal entries.
3. **Range Checking**:
   - If the score is `< 0` or `> 100`, an out-of-bounds error message is printed.
4. **Type Casting**:
   - Valid numbers are cast to integers (`int(user_input)`), truncating any decimal portion.
5. **Conditional Branching (`if-elif-else`)**:
   - The program checks thresholds from highest to lowest (`>= 90`, `>= 80`, etc.) to assign the correct grade.
6. **Error Handling (`ValueError`)**:
   - If non-numeric characters (e.g., letters, symbols) are entered, the program catches the exception and notifies the user.

---

## Prerequisites

- **Python**: Version `3.6` or higher installed on your system.
- No third-party packages or external dependencies required.

---

## Installation & Execution

1. **Clone or Download the Project**:
   Save the Python script to your local machine as `student_grade_system.py`.

2. **Open Terminal / Command Prompt**:
   Navigate to the directory containing the file:
   ```bash
   cd path/to/directory
   ```

3. **Run the Script**:
   ```bash
   python student_grade_system.py
   ```
   *(On macOS/Linux, you may need to use `python3 student_grade_system.py`)*

---

## Example Usage & Test Cases

### 1. Standard Passing Grade
```text
Enter Your Mark (0-100): 85
Mark: 85 -> Grade: B
```

### 2. High Score / Upper Boundary
```text
Enter Your Mark (0-100): 100
Mark: 100 -> Grade: A
```

### 3. Decimal Input (Truncated by `int()`)
```text
Enter Your Mark (0-100): 74.8
Mark: 74 -> Grade: C
```

### 4. Lowest Score / Lower Boundary
```text
Enter Your Mark (0-100): 0
Mark: 0 -> Grade: E
```

### 5. Out-of-Bounds Error (Greater than 100)
```text
Enter Your Mark (0-100): 105
Invalid mark. Please enter a number between 0 and 100.
```

### 6. Out-of-Bounds Error (Negative)
```text
Enter Your Mark (0-100): -12
Invalid mark. Please enter a number between 0 and 100.
```

### 7. Non-Numeric Error
```text
Enter Your Mark (0-100): eighty
Invalid input. Please enter a valid number.
```

---

## Technical Notes

- **Truncation Behavior**: Because the script converts `user_input` to an integer using `int(user_input)`, floating-point values are truncated downwards (e.g., `89.9` becomes `89`, resulting in Grade `B`). If rounding is preferred, consider using `round(user_input)`.

---

## Potential Enhancements

- [ ] Add a `while` loop so users can calculate marks for multiple students without restarting the program.
- [ ] Add support for finer-grained grading (e.g., `A+`, `A-`, `B+`, etc.).
- [ ] Include standard rounding for decimal marks (`round()`).
- [ ] Implement class average and summary report generation.
- [ ] Store student records and grades in a CSV or JSON file.

---

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to modify and adapt it for educational or personal use.
