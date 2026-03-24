import json
from pathlib import Path
script_path = Path(_file_)
# print(f"Script path: {script_path}")
script_dir = script_path.parent
# print(f"Script directory: {script_dir}")
json_file = script_dir / 'database.json'


FILE_NAME = 'database.json'

def save_file(data):
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)

def load_file():
    if not os.path.exists(FILE_NAME):
        
        return {"snacks": [], "students": [], "sales": []}
    with open(FILE_NAME, 'r') as f:
        return json.load(f)


def initialize_database():
    """Enters the specific data from the activity guide."""
    db = {
        "snacks": [
            {"snack_id": 1, "name": "Piattos", "category": "chips", "price": 20},
            {"snack_id": 2, "name": "Nova", "category": "chips", "price": 18},
            {"snack_id": 3, "name": "Oreo", "category": "cookies", "price": 15},
            {"snack_id": 4, "name": "KitKat", "category": "chocolate", "price": 25},
            {"snack_id": 5, "name": "Skyflakes", "category": "crackers", "price": 12}
        ],
        "students": [
            {"student_id": 1, "name": "Alice Cruz", "grade_level": 10},
            {"student_id": 2, "name": "Brian Santos", "grade_level": 9},
            {"student_id": 3, "name": "Carla Reyes", "grade_level": 10},
            {"student_id": 4, "name": "David Lim", "grade_level": 11},
            {"student_id": 5, "name": "Ella Tan", "grade_level": 10}
        ],
        "sales": [
            {"sale_id": 1, "student_id": 1, "snack_id": 1, "quantity": 2, "total_price": 40, "date": "2026-03-14", "day": "Saturday"},
            {"sale_id": 2, "student_id": 3, "snack_id": 3, "quantity": 1, "total_price": 15, "date": "2026-03-14", "day": "Saturday"},
            {"sale_id": 3, "student_id": 2, "snack_id": 2, "quantity": 3, "total_price": 54, "date": "2026-03-15", "day": "Sunday"},
            {"sale_id": 4, "student_id": 5, "snack_id": 4, "quantity": 1, "total_price": 25, "date": "2026-03-15", "day": "Sunday"},
            {"sale_id": 5, "student_id": 1, "snack_id": 1, "quantity": 1, "total_price": 20, "date": "2026-03-16", "day": "Monday"},
            {"sale_id": 6, "student_id": 4, "snack_id": 5, "quantity": 2, "total_price": 24, "date": "2026-03-16", "day": "Monday"}
        ]
    }
    save_file(db)
    print(">>> Database initialized and saved to database.json")


def generate_reports():
    data = load_file()
    sales = data.get("sales", [])
    snacks = data.get("snacks", [])
    students = data.get("students", [])
    
    print("\n================================")
    print("   CANTEEN DATABASE REPORTS")
    print("================================")

    total_rev = sum(s['total_price'] for s in sales)
    print(f"1. Total Revenue: P{total_rev}")

   
    snack_qty = {}
    for s in sales:
        sid = s['snack_id']
        snack_qty[sid] = snack_qty.get(sid, 0) + s['quantity']
    
    if snack_qty:
        best_id = max(snack_qty, key=snack_qty.get)
        snack_name = "Unknown"
        for sn in snacks:
            if sn['snack_id'] == best_id:
                snack_name = sn['name']
        print(f"2. Most Popular Snack: {snack_name} ({snack_qty[best_id]} units sold)")

    
    day_sales = {}
    for s in sales:
        day = s['day']
        day_sales[day] = day_sales.get(day, 0) + s['total_price']
    
    print("3. Sales Distribution:")
    for day, total in day_sales.items():
        print(f"   - {day}: P{total}")


    student_spending = {}
    for s in sales:
        st_id = s['student_id']
        student_spending[st_id] = student_spending.get(st_id, 0) + s['total_price']
    
    if student_spending:
        top_st_id = max(student_spending, key=student_spending.get)
        st_name = "Unknown"
        for st in students:
            if st['student_id'] == top_st_id:
                st_name = st['name']
        print(f"4. Top Spender: {st_name} (P{student_spending[top_st_id]})")
    print("================================\n")

initialize_database()
generate_reports()

input("Press Enter to close...")
