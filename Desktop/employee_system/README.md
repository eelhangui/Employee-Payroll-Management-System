# Employee & Payroll Management System 🚀

A clean and robust Python Object-Oriented Programming (OOP) project implementing an Employee and Payroll Management System. This project demonstrates core OOP principles, polymorphism, encapsulation, abstract base classes, and custom magic methods.

## 📋 Features

- **Abstract Base Classes (`ABC`):** Defines a blueprint `Employee` class with mandatory abstract methods.
- **Inheritance & Polymorphism:** Subclasses (`FullTimeEmployee` and `PartTimeEmployee`) implement specific salary calculations.
- **Encapsulation:** Protects internal attributes using naming conventions (`_emp_id`, `_hours_worked`).
- **Magic/Dunder Methods:**
  - `__str__`: Returns a readable string representation of the employee.
  - `__len__`: Returns the integer value of the employee's pay.
  - `__add__`: Allows adding the payroll of two employees using the `+` operator.

## 📂 Project Structure

```text
Employee-Management-System-Python-OOP/
│
└── employee_system.py      # Main script containing all classes and test cases
