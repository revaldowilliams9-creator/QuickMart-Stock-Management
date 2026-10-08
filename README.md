# QuickMart Grocery - Stock Management System

A modular, console-based stock management application built in Python. This program was developed to help store staff capture inventory data efficiently, calculate product stock values automatically, and generate structured inventory reports.

This project was completed as part of the **Programming 1A** curriculum for the **Higher Certificate / Diploma in Systems Development** at **Boston City Campus**.

## 🚀 Features
* **Automated Data Management:** Utilizes modern Python data structures (`@dataclass`) to handle product attributes seamlessly without manual boilerplate code.
* **Robust Input Validation:** Implements modular helper functions with exception handling (`try-except` blocks) to prevent system crashes caused by invalid data entry.
* **Edge-Case Handling:** Strips accidental whitespace and prevents users from entering blank product names.
* **Dynamic Inventory Control:** Uses conditional loops allowing staff to continuously capture multiple products in a single tracking session.
* **Pythonic Financial Reporting:** Outputs a clean summary of the store's inventory, applying currency formatting and utilizing optimized native aggregation functions to calculate the grand total.

## 🛠️ Tech Stack & Concepts Demonstrated
* **Language:** Python 3
* **Object-Oriented Programming (OOP):** Python `@dataclass` decorator for data modeling, featuring encapsulated instance methods for behavior management.
* **Functional Refactoring:** Reusable input validation modules to enforce the **DRY (Don't Repeat Yourself)** principle.
* **Control Flow:** `while` loops and conditional statements (`if-else`).
* **Error Handling:** Robust user-input sanitation using `ValueError` exception trapping.
* **Data Structures & Generators:** Python lists for runtime database management, paired with generator expressions for memory-efficient mathematical calculations (`sum()`).

## 📋 How To Run the Project
1. Ensure you have Python 3 installed on your system.
2. Clone this repository or download the source files.
3. Open your terminal or command prompt, navigate to the project directory, and run:
   ```bash
   python main.py
   ```

