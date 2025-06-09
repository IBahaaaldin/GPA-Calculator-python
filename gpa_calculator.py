"""
Ultimate GPA Calculator (CLI Version)
Author: IBahaaaldin

Features:
- Load previous courses from CSV
- Add new courses
- Edit or remove courses
- Calculate GPA
- Export GPA report
"""

import os
import csv

GRADE_SCALE = {
    'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0
}

def get_grade_point(grade):
    return GRADE_SCALE.get(grade.upper())

def load_courses(filename="courses.csv"):
    courses = []
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    try:
                        courses.append((row[0], row[1].upper(), float(row[2])))
                    except:
                        continue
    return courses

def save_courses(courses, filename="courses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for course in courses:
            writer.writerow(course)

def export_to_txt(courses, gpa, filename="gpa_report.txt"):
    with open(filename, "w") as f:
        f.write("Student GPA Report\n")
        f.write("="*40 + "\n")
        f.write(f"{'Course':<25}{'Grade':<10}{'Credits':<10}\n")
        f.write("-"*40 + "\n")
        for name, grade, credit in courses:
            f.write(f"{name:<25}{grade:<10}{credit:<10.1f}\n")
        f.write("="*40 + "\n")
        f.write(f"Final GPA: {gpa:.2f}\n")

def display_courses(courses):
    print("\nCurrent Courses:")
    print(f"{'ID':<4}{'Course':<25}{'Grade':<10}{'Credits':<10}")
    for i, (name, grade, credit) in enumerate(courses):
        print(f"{i:<4}{name:<25}{grade:<10}{credit:<10}")

def main():
    courses = []
    if input("Load previous courses from file? (y/n): ").lower() == 'y':
        courses = load_courses()
        print(f"✅ Loaded {len(courses)} courses.")

    while True:
        print("\nOptions:")
        print("1. Add course")
        print("2. Edit course")
        print("3. Remove course")
        print("4. Display courses")
        print("5. Calculate GPA")
        print("6. Save and Exit")
        choice = input("Choose: ").strip()

        if choice == '1':
            name = input("Course name: ").strip()
            grade = input("Grade (e.g., A, B+): ").strip().upper()
            if get_grade_point(grade) is None:
                print("⚠️  Invalid grade.")
                continue
            try:
                credit = float(input("Credit hours: "))
                if credit <= 0:
                    raise ValueError
            except:
                print("⚠️  Invalid credits.")
                continue
            courses.append((name, grade, credit))
            print("✅ Course added.")

        elif choice == '2':
            display_courses(courses)
            idx = input("Enter course ID to edit: ")
            if not idx.isdigit() or int(idx) >= len(courses):
                print("⚠️  Invalid ID.")
                continue
            idx = int(idx)
            name = input("New name (leave empty to keep): ").strip() or courses[idx][0]
            grade = input("New grade (leave empty to keep): ").strip().upper() or courses[idx][1]
            credit = input("New credits (leave empty to keep): ").strip()
            try:
                credit = float(credit) if credit else courses[idx][2]
            except:
                print("⚠️  Invalid credits.")
                continue
            courses[idx] = (name, grade, credit)
            print("✅ Course updated.")

        elif choice == '3':
            display_courses(courses)
            idx = input("Enter course ID to remove: ")
            if not idx.isdigit() or int(idx) >= len(courses):
                print("⚠️  Invalid ID.")
                continue
            courses.pop(int(idx))
            print("✅ Course removed.")

        elif choice == '4':
            display_courses(courses)

        elif choice == '5':
            if not courses:
                print("⚠️  No courses available.")
                continue
            total_points = sum(get_grade_point(grade) * credit for _, grade, credit in courses)
            total_credits = sum(credit for _, _, credit in courses)
            gpa = total_points / total_credits if total_credits else 0.0
            print(f"🎯 GPA: {gpa:.2f}")
            export_to_txt(courses, gpa)

        elif choice == '6':
            save_courses(courses)
            print("📦 Courses saved to courses.csv")
            break

if __name__ == "__main__":
    main()
