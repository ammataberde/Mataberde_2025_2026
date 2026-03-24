import numpy as np

data = np.array([[2, 3, 1, 2, 4], [1, 0, 2, 1, 0], [0, 1, 2, 1, 3]])
anime_names = ["Dandadan", "Jujutsu Kaisen", "Spy x Family"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def print_data():
    for i, anime in enumerate(anime_names):
        print(f"{anime} - {data[i]}")

def update_data():
    print("\nSelect an anime to update:")
    for i, anime in enumerate(anime_names):
        print(f"[{i}] {anime}")
    anime_idx = int(input("Enter anime choice: "))

    print("\nSelect a day to update:")
    for i, day in enumerate(days):
        print(f"[{i}] {day}")
    day_idx = int(input("Enter day choice: "))

    new_episodes = int(input(f"Enter new number of episodes watched on {days[day_idx]} to "))
    data[anime_idx][day_idx] = new_episodes
    print(f"Updating number of episodes of {anime_names[anime_idx]} watched on {days[day_idx]} to {new_episodes}")
    print(f"Updated data: {anime_names[anime_idx]} - {data[anime_idx]}")


def summarize_data():
    print("\nSummary:")
    for i, anime in enumerate(anime_names):
        row = data[i]
        total = np.sum(row)
        avg = np.mean(row)
        min_val = np.min(row)
        max_val = np.max(row)
        print(f"{anime} - Total Episodes Watched: {total} | Average: {avg:.1f} | Min: {min_val} | Max: {max_val}")

while True:
    print("\n[1] Print all data")
    print("[2] Select anime")
    print("[3] Update data")
    print("[4] Summarize data")
    print("[5] Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        print_data()
    elif choice == '2':
        print("\nSelect an anime:")
        for i, anime in enumerate(anime_names):
            print(f"[{i}] {anime}")
        anime_choice = int(input("Enter choice: "))
        print(f"\n{anime_names[anime_choice]} - {data[anime_choice]}")
    elif choice == '3':
        update_data()
    elif choice == '4':
        summarize_data()
    else:
        break
