"""
Student GPA Calculator (GUI Version)
Author: IBahaaaldin
Description: A GUI-based GPA calculator using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import csv
import os

GRADE_SCALE = {
    'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0
}

courses = []

def add_course():
    name = entry_name.get().strip()
    grade = entry_grade.get().strip().upper()
    credits = entry_credits.get().strip()

    if not name or grade not in GRADE_SCALE:
        messagebox.showerror("Input Error", "Invalid course name or grade.")
        return
    try:
        credits = float(credits)
        if credits <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Invalid credit hours.")
        return

    courses.append((name, grade, credits))
    tree.insert("", tk.END, values=(name, grade, credits))
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    entry_credits.delete(0, tk.END)

def calculate_gpa():
    if not courses:
        messagebox.showwarning("No Data", "No courses entered.")
        return
    total_points = sum(GRADE_SCALE[grade] * credit for _, grade, credit in courses)
    total_credits = sum(credit for _, _, credit in courses)
    gpa = total_points / total_credits if total_credits else 0.0
    messagebox.showinfo("GPA Result", f"Your GPA is: {gpa:.2f}")
    export_report(gpa)

def export_report(gpa):
    with open("gpa_gui_report.txt", "w") as f:
        f.write("Student GPA Report (GUI)\n")
        f.write("="*40 + "\n")
        f.write(f"{'Course':<15}{'Grade':<10}{'Credits':<10}\n")
        f.write("-"*40 + "\n")
        for name, grade, credit in courses:
            f.write(f"{name:<15}{grade:<10}{credit:<10.1f}\n")
        f.write("="*40 + "\n")
        f.write(f"Final GPA: {gpa:.2f}\n")

def load_from_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not filename:
        return
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 3:
                try:
                    credit = float(row[2])
                    if row[1].upper() in GRADE_SCALE:
                        courses.append((row[0], row[1].upper(), credit))
                        tree.insert("", tk.END, values=(row[0], row[1].upper(), credit))
                except:
                    continue

# GUI setup
root = tk.Tk()
root.title("Student GPA Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Course Name").grid(row=0, column=0)
tk.Label(frame, text="Grade (e.g. A, B+)").grid(row=0, column=1)
tk.Label(frame, text="Credit Hours").grid(row=0, column=2)

entry_name = tk.Entry(frame)
entry_grade = tk.Entry(frame)
entry_credits = tk.Entry(frame)
entry_name.grid(row=1, column=0)
entry_grade.grid(row=1, column=1)
entry_credits.grid(row=1, column=2)

tk.Button(frame, text="Add Course", command=add_course).grid(row=1, column=3, padx=5)
tk.Button(frame, text="Load Courses", command=load_from_file).grid(row=1, column=4, padx=5)

columns = ("Course", "Grade", "Credits")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.pack(padx=10, pady=10)

tk.Button(root, text="Calculate GPA", command=calculate_gpa).pack(pady=10)

root.mainloop()
