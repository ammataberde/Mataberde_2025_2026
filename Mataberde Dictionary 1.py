student = { }


student_record = {
"name": str(input("Enter your name: ")),
"age": int(input("Enter your age: ")),
"favorite_subject": str(input("Enter your favorite subject: ")),
}

print ("Student Record:")
print("name",student_record["name"])
print("age",student_record["age"])
print("favorite subject",student_record["favorite_subject"])
