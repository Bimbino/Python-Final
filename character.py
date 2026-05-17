class character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.strength = 10
        self.level = 1
        self.gold = 0
        self.magic = 0
        self.inventory = ["Fungal Fritter", "Water"]
        self.location = (0, 0)
        self.quests = {}
        self.equipped_weapon = ["Rusty Sword"]
        self.shield = None
        self.armor = {"Helmet": None, "Chestplate": None, "Leggings": None, "Boots": None}
