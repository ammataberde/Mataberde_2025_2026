import json
import os

DATABASE_FILE = "database.json"


# Initial student data
INITIAL_DATA = [
    {
        "name": "Joross",
        "age": 14,
        "favorite_subject": "chem",
        "favorite_color": "blue",
        "favorite_song": "Lupang Hinirang"
    },
    {
        "name": "Rocco",
        "age": 14,
        "favorite_subject": "chem",
        "favorite_color": "orange",
        "favorite_song": "Happy Birthday"
    },
    {
        "name": "Zach",
        "age": 14,
        "favorite_subject": "math3",
        "favorite_color": "chartreuse",
        "favorite_song": "Haus of Holbein"
    },
    {
        "name": "Adrian",
        "age": 14,
        "favorite_subject": "pe",
        "favorite_color": "blue",
        "favorite_song": "Lay All Your Love On Me"
    },
    {
        "name": "Rain",
        "age": 14,
        "favorite_subject": "recess",
        "favorite_color": "pink",
        "favorite_song": "Ulan"
    }
]


# Make sure database.json exists
def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as file:
            json.dump(INITIAL_DATA, file, indent=4)


# Load data
def load_data():
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


# Save data
def save_data(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)


# CREATE
def create_student():
    data = load_data()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    subject = input("Favorite subject: ")
    color = input("Favorite color: ")
    song = input("Favorite song: ")

    student = {
        "name": name,
        "age": age,
        "favorite_subject": subject,
        "favorite_color": color,
        "favorite_song": song
    }

    data.append(student)
    save_data(data)

    print("Student successfully added!\n")


# READ
def read_students():
    data = load_data()

    if len(data) == 0:
        print("No students in database.\n")
        return

    print("\nStudent List:\n")

    for i, student in enumerate(data, start=1):
        print(f"Student {i}")
        for key, value in student.items():
            print(f"{key}: {value}")
        print()


# UPDATE
def update_school():
    data = load_data()

    campus = input("Enter PSHS Campus: ")

    for student in data:
        student["school"] = campus

    save_data(data)

    print("All students updated with school campus!\n")


# DELETE
def delete_students():
    data = load_data()

    delete_colors = ["red", "blue", "yellow"]

    new_data = []
    removed = 0

    for student in data:
        if student["favorite_color"].lower() in delete_colors:
            removed += 1
        else:
            new_data.append(student)

    save_data(new_data)

    print(f"{removed} student(s) deleted.\n")


# Menu
def menu():
    while True:
        print("ADDRESS BOOK MENU")
        print("1 - Add Student (CREATE)")
        print("2 - View Students (READ)")
        print("3 - Add School Campus (UPDATE)")
        print("4 - Delete by Favorite Color (DELETE)")
        print("5 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_student()

        elif choice == "2":
            read_students()

        elif choice == "3":
            update_school()

        elif choice == "4":
            delete_students()

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.\n")


initialize_database()
menu()