# 🎓 Ultimate GPA Calculator

A complete GPA management system for students — includes both a robust **Command-Line Interface (CLI)** and a modern **Graphical User Interface (GUI)**. Built in Python, this tool simplifies academic GPA tracking, enhances productivity, and ensures accuracy through error handling, file integration, and reporting.

---

## 👤 About the Developer

This project was created by **IBahaaaldin**, a second-year Computer Science student with a focus on Artificial Intelligence. Passionate about building practical tools that solve real student problems, IBahaaaldin believes in clean code, useful interfaces, and continuous self-improvement through hands-on learning.

---

## 🧠 Project Overview

The **Ultimate GPA Calculator** was designed for university students who want to:

- Track their GPA with ease
- Save and load their academic data
- Use either a terminal or GUI to manage their progress
- Export clean reports for reference or printing

---

## 🧰 Features

### ✅ CLI Version (`gpa_calculator.py`)

- 📥 Load previous courses from `courses.csv`
- ➕ Add new courses
- ✏️ Edit existing entries (course name, grade, credits)
- ❌ Remove courses by ID
- 📊 Calculate GPA with full letter grade support (A to F)
- 📤 Export GPA summary and course list to `gpa_report.txt`
- 💾 Save progress for future sessions

### ✅ GUI Version (`gpa_calculator_gui.py`)

- 💻 Built with `Tkinter` for modern Python desktops
- 📂 Import courses from CSV
- ✍️ Add course entries with forms
- 📋 Display table of all added courses
- 🎯 Real-time GPA calculation
- 📤 Export report to `gpa_gui_report.txt`

---

## 📂 File Structure

```
Ultimate-GPA-Calculator/
│
├── gpa_calculator.py         # CLI application
├── gpa_calculator_gui.py     # GUI interface (Tkinter)
├── courses.csv               # Sample: preloaded course data
└── README.md                 # Project documentation
```

---

## ▶️ How to Use

### Run CLI Version

```bash
python gpa_calculator.py
```

### Run GUI Version

```bash
python gpa_calculator_gui.py
```

Ensure Python 3 is installed and required modules like `tkinter` are available.

---

## 🚀 Future Ideas

- Add semester/year filtering
- Visual GPA graphs
- GPA prediction feature
- Database integration

---

## 📬 Contact

For feedback or collaboration:  
**GitHub**: [IBahaaaldin](https://github.com/IBahaaaldin)

---

_This project reflects the growth and capabilities of an aspiring software developer with a clear goal: building smart tools for real people._
