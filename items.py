class item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    item_effects = {
    "Health Potion": {"health": 20, "value": 10},
    "Super Health Potion": {"health": 50, "value": 25},
    "Mana Potion": {"magic": 20, "value": 10},
    "Magic Scroll": {"magic": 10, "value": 25},
    "Shield": {"message": "Shield has no effect outside of combat.","strength": 10, "value": 8},
    "Rusty Sword": {"message": "Rusty sword has no effect outside of combat.", "strength": 10, "value": 10},
    "Simple Wooden Sword": {"message": "Simple wooden sword has no effect outside of combat.","strength": 15, "value": 15},
    "Iron Longsword": {"message": "Iron longsword has no effect outside of combat.", "strength": 25, "value": 50},
    "Chestplate": {"maxhealth": 20, "value": 15},
    "Leggings": {"maxhealth": 15, "value": 12},
    "Boots": {"maxhealth": 5, "value": 5},
    "Helmet": {"maxhealth": 10, "value": 7},
    "Ancient Scroll": {"level": 1, "value": 100},
    "Gold Coin": {"gold": 1, "value": 1},
    "Sweetroll": {"message": "You ate the sweetroll.", "health": 5, "value": 4},
    "Wheel of Cheese": {"message": "You ate the wheel of cheese... Wow, that was a lot.", "health": 10, "value": 8},
    "Fungal Fritter": {"message": "You ate the fungal fritter. Surprisingly tasty!", "health": 8, "value": 5},
    "Carton of Milk": {"message": "You drank the milk.", "health": 5, "value": 2},
    "Dr. Pepper": {"message": "You drank the Dr. Pepper.", "health": 5, "value": 3},
    "Water": {"message": "You drank the water.", "health": 2, "value": 2},
    "Daily Newspaper": {"message": "It wasn't much good... Mostly just advertisements and political campaign gossip.", "value": 2}

}