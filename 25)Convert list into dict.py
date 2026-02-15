a=['surya','swetha','priyanka']
b=[98,92,87]
student_marks=dict(zip(a,b))
print("Students Marks Dictionary:",student_marks)


a = [10, 20, 30, 40]

# Convert list into dict with index as key
result = {i: a[i] for i in range(len(a))}
print("Dictionary:", result)

a = ["apple", "banana", "cherry"]

result = dict(enumerate(a))
print("Dictionary:", result)
