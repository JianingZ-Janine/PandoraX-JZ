import json
import random

# File to store wardrobe data
WARDROBE_FILE = "wardrobe.json"

# Load wardrobe from file
def load_wardrobe():
    try:
        with open(WARDROBE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"clothing": [], "outfits": []}

# Save wardrobe to file
def save_wardrobe(wardrobe):
    with open(WARDROBE_FILE, "w") as file:
        json.dump(wardrobe, file)

# Add a clothing item
def add_clothing(wardrobe):
    item = {
        "type": input("Enter type (e.g., shirt, pants, dress): ").strip().lower(),
        "color": input("Enter color: ").strip().lower(),
        "season": input("Enter season (e.g., summer, winter): ").strip().lower(),
    }
    wardrobe["clothing"].append(item)
    print(f"Added {item['color']} {item['type']} for {item['season']}.")

# View all clothing items
def view_wardrobe(wardrobe):
    if not wardrobe["clothing"]:
        print("Your wardrobe is empty.")
    else:
        for i, item in enumerate(wardrobe["clothing"], 1):
            print(f"{i}. {item['color'].capitalize()} {item['type']} ({item['season'].capitalize()})")

# Create an outfit
def create_outfit(wardrobe):
    view_wardrobe(wardrobe)
    outfit = []
    while True:
        choice = input("Enter the number of an item to add to the outfit (or 'done' to finish): ").strip().lower()
        if choice == "done":
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(wardrobe["clothing"]):
                outfit.append(wardrobe["clothing"][index])
                print(f"Added {wardrobe['clothing'][index]['color']} {wardrobe['clothing'][index]['type']} to the outfit.")
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
    if outfit:
        wardrobe["outfits"].append(outfit)
        print("Outfit saved!")

# Suggest a random outfit
def suggest_outfit(wardrobe):
    if not wardrobe["clothing"]:
        print("Your wardrobe is empty.")
    else:
        outfit = random.sample(wardrobe["clothing"], min(3, len(wardrobe["clothing"])))  # Suggest 3 items
        print("Suggested outfit:")
        for item in outfit:
            print(f"- {item['color'].capitalize()} {item['type']} ({item['season'].capitalize()})")

# Filter clothing items
def filter_wardrobe(wardrobe):
    print("Filter by:")
    print("1. Type")
    print("2. Color")
    print("3. Season")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        type_filter = input("Enter type to filter by: ").strip().lower()
        filtered = [item for item in wardrobe["clothing"] if item["type"] == type_filter]
    elif choice == "2":
        color_filter = input("Enter color to filter by: ").strip().lower()
        filtered = [item for item in wardrobe["clothing"] if item["color"] == color_filter]
    elif choice == "3":
        season_filter = input("Enter season to filter by: ").strip().lower()
        filtered = [item for item in wardrobe["clothing"] if item["season"] == season_filter]
    else:
        print("Invalid choice.")
        return
    if filtered:
        print("Filtered items:")
        for item in filtered:
            print(f"- {item['color'].capitalize()} {item['type']} ({item['season'].capitalize()})")
    else:
        print("No items match the filter.")

# Main menu
def main():
    wardrobe = load_wardrobe()
    while True:
        print("\nVirtual Wardrobe Organizer")
        print("1. Add a clothing item")
        print("2. View wardrobe")
        print("3. Create an outfit")
        print("4. Suggest a random outfit")
        print("5. Filter wardrobe")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_clothing(wardrobe)
        elif choice == "2":
            view_wardrobe(wardrobe)
        elif choice == "3":
            create_outfit(wardrobe)
        elif choice == "4":
            suggest_outfit(wardrobe)
        elif choice == "5":
            filter_wardrobe(wardrobe)
        elif choice == "6":
            save_wardrobe(wardrobe)
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()