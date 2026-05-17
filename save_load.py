from locations import game_map, items_at_location
from quests import quests
from character import character

def save_game_state(player, current_quests, game_items, filename="game_state.txt"):
    """
    Save the entire game state to a text file in the specified format.
    
    Args:
        player: character object with attributes (name, health, strength, etc.)
        current_quests: dict of quests with their statuses
        game_items: dict of items at each location
        filename: output file name
    """
    lines = []
    
    # CHARACTER section
    lines.append("Character")
    inventory_str = ",".join(player.inventory)
    lines.append(f"{player.name},{player.health},{player.strength},{player.level},{player.gold},{player.magic},{len(player.inventory)},{len(current_quests)}")
    
    # INVENTORY section
    lines.append("Inventory")
    for item in player.inventory:
        lines.append(item)
    
    # ITEMS AT LOCATION section
    lines.append("ItemsAtLocation")
    for coords in sorted(game_items.keys()):
        items = game_items[coords]
        items_str = ",".join(items) if items else ""
        lines.append(f"{coords[0]},{coords[1]},{items_str}")
    
    # QUESTS section
    lines.append("Quests")
    for quest_name, quest_data in sorted(current_quests.items()):
        status = quest_data.get("status", "Not Started")
        lines.append(f"{quest_name},{status}")
    
    lines.append("---")
    
    # Write to file
    with open(filename, "w") as f:
        f.write("\n".join(lines))


def load_game_state(filename="game_state.txt"):
    """
    Load the game state from a text file.
    Returns a dict with keys: player_data, inventory, items_at_location, quests
    """
    try:
        with open(filename, "r") as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"Save file {filename} not found.")
        return None
    
    sections = {}
    current_section = None
    section_data = []
    
    for line in content.split("\n"):
        line = line.strip()
        if not line or line == "---":
            if current_section and section_data:
                sections[current_section] = section_data
            section_data = []
            current_section = None
            continue
        
        if line in ["Character", "Inventory", "ItemsAtLocation", "Quests"]:
            if current_section and section_data:
                sections[current_section] = section_data
            current_section = line
            section_data = []
        else:
            section_data.append(line)
    
    if current_section and section_data:
        sections[current_section] = section_data
    
    # Parse sections
    result = {}
    
    # Parse Character line
    if "Character" in sections and sections["Character"]:
        char_line = sections["Character"][0]
        parts = char_line.split(",")
        result["player_data"] = {
            "name": parts[0],
            "health": int(parts[1]),
            "strength": int(parts[2]),
            "level": int(parts[3]),
            "gold": int(parts[4]),
            "magic": int(parts[5])
        }
    
    # Parse Inventory
    result["inventory"] = sections.get("Inventory", [])
    
    # Parse ItemsAtLocation
    items_dict = {}
    if "ItemsAtLocation" in sections:
        for line in sections["ItemsAtLocation"]:
            parts = line.split(",")
            coords = (int(parts[0]), int(parts[1]))
            items = [item.strip() for item in parts[2:] if item.strip()]
            items_dict[coords] = items
    result["items_at_location"] = items_dict
    
    # Parse Quests
    quests_dict = {}
    if "Quests" in sections:
        for line in sections["Quests"]:
            parts = line.split(",", 1)
            if len(parts) == 2:
                quest_name = parts[0].strip()
                quest_status = parts[1].strip()
                quests_dict[quest_name] = {"status": quest_status}
    result["quests"] = quests_dict
    
    return result
