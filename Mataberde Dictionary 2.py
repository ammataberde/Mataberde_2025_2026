students = []

for i in range(3):
    name1 = input("Enter name: ")
    age1 = input("Enter age: ")
    grade1 = input("Enter grade: ")
    student_info = { }
    student_info["Name"] = name1
    student_info["Age"] = age1
    student_info["Grade"] = grade1
    print("\n")
    students.append(student_info)


print("Class Directory:")
for i in students:
    print("Name:",i["Name"],"|Age:", i["Age"], "|Grade:",i["Grade"])
