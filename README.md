# 🐾 PawPal+  
A smart, AI-assisted pet care management system built with Python OOP, Streamlit, and automated testing. PawPal+ helps pet owners track feedings, walks, medications, appointments, and recurring routines — all organized through an intelligent scheduling engine.

---

## 📌 Overview
PawPal+ is designed using a **CLI-first workflow**, ensuring the backend logic is fully verified before connecting to the UI. The system uses Python classes to model Owners, Pets, Tasks, and a Scheduler that provides sorting, filtering, conflict detection, and recurring task automation.

This project was built as part of CodePath’s AI110 course, practicing AI-assisted engineering, UML design, algorithmic reasoning, and verification.

---

## 🧱 System Architecture
### **Core Classes**
- **Task** — Represents a single activity with description, time, frequency, and completion status.
- **Pet** — Stores pet details and its list of tasks.
- **Owner** — Manages multiple pets and provides unified access to all tasks.
- **Scheduler** — The “brain” that organizes tasks across pets, sorts them, detects conflicts, and handles recurrence.

See `diagrams/uml_final.mmd` for the final UML diagram.

---

## 🚀 Features

### **Core Functionality**
- Add pets and tasks  
- View all tasks across pets  
- CLI demo script (`main.py`)  
- Streamlit UI integration (`app.py`)  

### **Smart Scheduling**
- **Sorting by time**  
  - Implemented in `Scheduler.sort_by_time()`
- **Filtering by pet or completion status**  
  - Implemented in `Scheduler.filter_tasks()`
- **Conflict detection**  
  - Implemented in `Scheduler.detect_conflicts()`
- **Recurring tasks (daily/weekly)**  
  - Implemented in `Task.mark_complete()` and Scheduler recurrence helpers

---

## 🖥️ Demo Walkthrough

### **Example Workflow**
1. Add a pet  
