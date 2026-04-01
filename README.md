# Mini Database Management System (DBMS)
*This project is a lightweight, Python-based Database Management System designed to emulate core relational database functionalities. Developed as part of Computer Engineering coursework, it demonstrates advanced data structure manipulation, file parsing, and relational logic without the need for an external SQL engine.


## ✨ Features
* Relational Operations: Supports essential SQL-like commands including CREATE_TABLE, INSERT, SELECT, UPDATE, DELETE, and COUNT.

* Table Joins: Capable of performing JOIN operations between two relational tables based on a common column.

* Data Integrity: Includes robust error handling for "table already exists," "missing columns," "invalid table names," and "non-existent columns."

* Advanced Filtering: Supports conditional queries using dictionary-based logic to filter, update, or delete specific rows.

* Visualized Output: Features a custom-built rendering engine that displays results in professionally formatted ASCII tables with dynamic column width calculation.


## 🚀 Usage
* The system processes a batch of commands from a text file provided as a command-line argument:
```python3 database.py commands.txt```

## 🛠️ Technologies Used
* Language: Python 3.x

* Modules: sys (for command-line arguments and file I/O)

* Logic: Dictionary-based table storage and list-based relational data management.

## 📝 Notes
* This project showcases core competencies in back-end logic, algorithmic efficiency, and the fundamental principles of how relational databases manage data in memory.
