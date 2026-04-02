# 🏗️ Module 01: Python Object-Oriented Programming (OOP)

This module marks the beginning of Phase 1. Before building autonomous agents, it is critical to master the art of designing modular, reusable, and scalable code. This folder documents my journey from basic class definitions to complex system architecture.

## 📁 Daily Learning & Implementations

### Day 1: Classes & Objects
- **Key Concept:** `__init__` constructor, instance attributes, and methods.
- **Deliverable:** `bank_account.py` — A functional class handling deposits, withdrawals, and balance tracking.

### Day 2: Inheritance & Polymorphism
- **Key Concept:** Single/Multiple inheritance and method overriding.
- **Deliverable:** `animal_hierarchy.py` — Modeling specialized behaviors (Dog, Cat) from a base Animal class.

### Day 3: Encapsulation & Properties
- **Key Concept:** Private attributes (`_`, `__`) and the `@property` decorator for data validation.
- **Deliverable:** `validated_account.py` — A secure banking system that prevents negative balances and invalid inputs.

### Day 4: Magic (Dunder) Methods
- **Key Concept:** Operator overloading (`__str__`, `__add__`, `__eq__`, `__repr__`).
- **Deliverable:** `vector_2d.py` — A mathematical utility allowing direct addition and comparison of vector objects.

### Day 5: Class/Static Methods & Decorators
- **Key Concept:** `@classmethod` for alternative constructors and `@dataclass` for boilerplate-free data structures.
- **Deliverable:** `refactored_account.py` — A modern, optimized version of the banking system using Pythonic decorators.

### Day 6: Abstract Base Classes (ABC)
- **Key Concept:** Defining strict interfaces and blueprints using the `abc` module.
- **Deliverable:** `shape_system.py` — A geometry framework ensuring all shapes implement required `area()` and `perimeter()` methods.

---

## 🏆 Week 1 Milestone: Library Management System
The capstone project for this module is a full-featured CLI application that integrates every concept learned this week.

**System Architecture:**
- **`Book` Class:** Handles metadata and availability status.
- **`Member` Class:** Manages user data and borrowing history.
- **`Library` Class:** The central orchestrator for CRUD operations (Create, Read, Update, Delete).

**Technical Highlights:**
- Data persistence via JSON.
- Encapsulation for secure book tracking.
- Inheritance for different membership tiers (e.g., Student vs. Teacher).


---
*Status: Week 1 Complete ✅ | Next: Data Structures & Algorithms*
