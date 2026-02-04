# Python OOP Project – Almost a Circle

## Overview
This project demonstrates strong use of Object-Oriented Programming (OOP) principles in Python through the implementation of a small geometry system using base and derived classes. It emphasizes clean design, validation, testing, and serialization.

---

## Concepts Covered

This project applies core Python concepts including:

- Importing modules
- Exception handling
- Object-Oriented Programming (OOP)
  - Classes and inheritance
  - Private attributes
  - Getters and setters
  - Class methods and static methods
- Unit testing
- File input/output (read/write)

It also includes more advanced topics such as:

- Variable-length arguments (`*args`, `**kwargs`)
- Serialization and deserialization
- Working with JSON data

---

## Project Structure

- `models/` – Core classes and serialization logic
- `tests/` – Unit tests for all functionalities

---

## Key Features

- A `Base` class that manages object IDs and JSON serialization
- A `Rectangle` class with:
  - Attribute validation
  - Area calculation
  - Custom string representation
  - Display logic with positional offsets
  - Dynamic attribute updates using `*args` and `**kwargs`
- A `Square` class that inherits from `Rectangle`
  - Size property with getter and setter
  - Dictionary representation support
- Full JSON file persistence and restoration
- Comprehensive unit tests for reliability

---

## Development Guidelines

- All features are fully tested
- Code follows Python best practices
- Commit messages follow clear conventions:
  - `ADD` – new features
  - `UPD` – updates
  - `DEL` – removals

> If it’s not tested, it doesn’t work.
