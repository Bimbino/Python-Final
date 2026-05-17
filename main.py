SCREEN_WIDTH = 80
title = "Adventure Quest"

from character import character
from locations import game_map, items_at_location
from quests import quests
from save_load import save_game_state, load_game_state

#HEADER / main menu and character creation
if __name__ == "__main__":
    print("================================================================================")
    print("                                Adventure Quest")
    print("================================================================================")
    print("Welcome to Adventure Quest!")
    print()
    print("In this mystical land, you will embark on a thrilling journey to find the Enchanted Castle, rescue allies, and rebuild communities. Along the way, you will encounter various challenges, meet different characters, and collect valuable resources. Good luck on your adventure!")
    print()
    print("================================================================================")
    print("| Main Menu:                                                                    |")
    print("| 1. Start New Game                                                             |")
    print("| 2. Load Game                                                                  |")
    print("| 3. Quit                                                                       |")
    print("================================================================================")
    choice = input("Please select an option: ").strip()

    if choice == "1":
        print("================================================================================")
        print("                                Adventure Quest")
        print("================================================================================")
        print("Create your Character!")
        print()
        while True:
            raw = input("Enter your character's name: ").strip()
            if not raw:
                print("Name cannot be blank. Please enter a name.")
                continue
            if any(ch.isdigit() for ch in raw):
                print("Names cannot contain numbers. Please try again.")
                continue
            if not raw[0].isalpha():
                print("Name must start with a letter. Please try again.")
                continue
            name = raw[0].upper() + raw[1:]
            break
        player = character(name)

        print()
        print(f"Character created! Name: {player.name}, Health: {player.health}, Strength: {player.strength}")
        print()
        print(f"Welcome, {player.name}! You stand at the edge of the Uncharted Territory, where danger and opportunity lurk at every turn. Your journey to the Enchanted Castle begins here. To the east lies an Abandoned Village shrouded in mystery, and to the south, a Haunted Forest beckons with eerie silence.")
        print()
        input("Press Enter to continue...")
        
        # Save initial game state
        save_game_state(player, quests, items_at_location)

    #OTHER CHOICES LOAD
    elif choice == "2":
        print("Load game not implemented yet.")
    elif choice == "3":
        print("Goodbye.")
    else:
        print("Invalid selection.")

"""
#HEADER 2.1 GAME INTERFACE
================================================================================
                                Adventure Quest
                      Location: 
================================================================================
| Name:             Health:              Strength:                     |
| Level:               Gold:                  Magic:                         |
================================================================================

#HEADER 2.2 AVAILABLE COMMANDS
| Available Commands:                                                           |
| - Move: north (n), south (s), east (e), west (w)                              |
| - Actions: inspect (c), interact (t)                                          |
| - Item Actions - add [item_name]: pick up (p), drop (d), use (u)              |
| - View Inventory (i)                                                          |
| - View Map (m)                                                                |
| - Quit (q)                                                                    |
================================================================================
"""

def build_status_screen(player, location_name: str, coords: tuple[int, int]) -> str:
    border = "=" * SCREEN_WIDTH
    title = "Adventure Quest"
    loc_line = f"Location: {location_name}  ({coords[0]}, {coords[1]})"
    def get_attr(p, key):
        if isinstance(p, dict):
            return p.get(key, "")
        return getattr(p, key, "")
    col1 = f"Name: {get_attr(player, 'name')}"
    col2 = f"Health: {get_attr(player, 'health')}"
    col3 = f"Strength: {get_attr(player, 'strength')}"
    line1 = f"| {col1:<20}{col2:<20}{col3:<30}|"
    col4 = f"Level: {get_attr(player, 'level')}"
    col5 = f"Gold: {get_attr(player, 'gold')}"
    col6 = f"Magic: {get_attr(player, 'magic')}"
    line2 = f"| {col4:<20}{col5:<20}{col6:<30}|"
    return "\n".join([
        border,
        title.center(SCREEN_WIDTH),
        loc_line.center(SCREEN_WIDTH),
        border,
        line1,
        line2,
        border
    ])

# Example: use the `player` character object created earlier
try:
    current_location_name = "Uncharted Territory"
    current_coords = (0, 0)

    status_screen = build_status_screen(player, current_location_name, current_coords)
    # print(status_screen)
except NameError:
    pass






