
student_marks = {
    "Surya": 85,
    "Arun": 92,
    "Priya": 78,
    "Kumar": 88,
    "Divya": 95
}

# Print the dictionary
print("Student Marks Dictionary:", student_marks)

highest_student=max(student_marks,key=student_marks.get)
highest_marks=student_marks[highest_student]
print(highest_marks)
print(highest_student)

