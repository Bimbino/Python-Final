
npcs = {
    (0, 1): {
        "name": "Elder",
        "dialogue": "\"Greetings, adventurer! I have an important task for you.\"",
        "quest": "Retrieve Ancient Scroll",
        "when_exit": "\"Good luck out there... It's dangerous beyond these walls.\""
    },
    (0,2): {   
        "name": "Suspicious Frog",
        "dialogue": "Something about this frog seems... off.",
        "quest": None,
        "list_of_items": {"Gold Coin":30},
        "when_exit": "The frog croaks ominously as you leave."
    },
    (0,4): {
        "name": "Guard Stevens",
        "dialogue": "The guard speaks, \"My cousin's out fighting dragons, and what do I get? Guard duty.\"",
        "quest": None,
        "when_exit": "Guard Stevens sighs and kicks at the gravel as you walk away."
    }, 
    (0,4): {
        "name": "Manny the Mage",
        "dialogue": "\"Looking to buy something? I have the good stuff!\"",
        "quest": None,
        "list_of_items": {"Health Potion": 5, "Super Health Potion": 2, "Mana Potion": 3, "Gold Coin": 250},
        "when_exit": "Manny hums to himself as you leave."
    },
    (0,4): {
        "name": "Tony the Average",
        "dialogue": "\"Looking for some new wares? I've got just the thing.\"",
        "quest": None,
        "list_of_items": {"Simple Wooden Sword": 1, "Boots": 1, "Gold Coin": 50},
        "when_exit": "\"Keep an eye out for my brothers! They tend to stick to the cities!\""
    },
    (0, 4): {
        "name": "Paper Boy", 
        "dialogue": "\"Paper! Get your daily paper!\"",
        "quest": None,
        "list_of_items": {"Daily Newspaper": 1},
        "when_exit": "\"Knowledge is power!\""
    },
    (0,4): {
        "name": "Crispy the Clown",
        "dialogue": "\"Hiya there, huhha! How would you like to see a trick?\" A tall, lanky clown with dirty clothes grinned.",
        "quest": None,
        "when_exit": "The clown directed you to smell a flower pinned to his lapel. You did, and it squirted water in your face... How embarrassing."
    },
    (1,3): {
        "name": "Spring Sprite",
        "dialogue": "\"The spring's waters are said to have healing properties. Would you like to take a soak?\"",
        "quest": None,
        "health": 10,
        "when_exit": "\"May the spring's magic guide you on your journey.\""
    },
    (3,0): {
        "name": "Guard Winter",
        "dialogue": "\"You look suspicious... Don't you have somewhere else to be?\"",
        "quest": None,
        "when_exit": "The guard crinkles his nose as you leave."
    },
    (2,0): {
        "name": "Strange Squirrel",
        "dialogue": "\"The magical springs are a place of tranquility. Would you like to rest here?\"",
        "quest": None,
        "health": 10,
        "when_exit": "\"May the springs' magic rejuvenate you on your journey.\""
    },
    (1, 1): {
        "name": "Scholar",
        "dialogue": "\"Ah, a curious mind! Can you help me gather rare items for my research?\"",
        "quest": "The Scholar's Collection",
        "when_exit": "The scholar thanks you for your help and returns to his studies."
    },
    (3,0): {
        "name": "Tony the Small",
        "dialogue": "\"Hey there, I'm Tony. I've got some stuff for sale if you're interested.\"",
        "quest": None,
        "list_of_items": {"Leggings": 1, "Helmet": 1, "Gold Coin": 30},
        "when_exit": "\"Tell Big Tony I said hi!\""
    },
    (3,0): {
        "name": "Belmond the Baker",
        "dialogue": "\"Baked goods? I've got plenty!\"",
        "quest": None,
        "list_of_items": {"Sweetroll": 5, "Fungal Fritter": 2, "Carton of Milk": 2, "Gold Coin": 20},
        "when_exit": "\"Come back anytime you have a sweet tooth!\""
    },
    (3,0): {
        "name": "Florence the Farmer",
        "dialogue": "\"You there! Are you a traveler? Do you think you could help me with some pests?\"",
        "quest": "Find the Pests",
        "when_exit": "\"Be careful out there! There's danger lurking around every corner!\""
    },
    (3,0): {
        "name": "Whiskers the Cat",
        "dialogue": "The cat eyes you strangely, eventually letting out a small meow, and uncurling its tail to reveal a small foreign drink.",
        "quest": None,
        "list_of_items": {"Dr. Pepper": 1},
        "when_exit": "Whiskers begins to groom themselves as you leave."
    },
    (3, 0): {
        "name": "Nick the Nasty",
        "dialogue": "\"What do you want? Can't you see I'm busy?\" He spoke... He had a foul stench about him, and you could see flies buzzing around his head. You quickly decide to end the conversation.",
        "quest": None,
        "when_exit": "Wow, Nick smells bad... You quickly walk away to avoid the stench."
    },
    (3,2): {
        "name": "Tony the Large",
        "dialogue": "",
        "quest": None,
        "list_of_items": {"Chestplate": 1, "Iron Longsword": 1, "Gold Coin": 150},
        "when_exit": "\"Thanks for stopping by!\""
    },
    (3, 2): {
        "name": "Healer",
        "dialogue": "\"I can help restore your health if you need aid.\"",
        "quest": None,
        "health": 30,
        "when_exit": "The healer smiles warmly as you leave."
    },
    (3, 2): {
        "name": "Mipsy the Mage",   
        "dialogue": "\"Welcome! Are you interested in some magic items?\"",
        "quest": None,
        "list_of_items": {"Magic Scroll": 1, "Mana Potion": 4, "Health Potion": 4, "Super Health Potion": 3, "Gold Coin": 100},
        "when_exit": "\"Stay safe out there, adventurer!\""
    },
    (3,2): {
        "name": "Gorath the Giant",
        "dialogue": "\"Leave me be.\"",
        "quest": None,
        "when_exit": "Gorath grumbles as you walk away... Someone is in a bad mood."
    },
    (3,2): {
        "name": "Rhomulus the Rogue",
        "dialogue": "\"Psst... Hey, you look like you could use some help. I have some items for sale, if you're interested.\"",
        "quest": None,
        "list_of_items": {"Shield": 1, "Sweet Roll": 1, "Gold Coin": 20},
        "when_exit": "\"I have more items if you ever need them...\""
    },
    (2,4): {
        "name": "Campfire Cook",
        "dialogue": "\"Care for some food? I can cook up something tasty for you.\"",
        "quest": None,
        "list_of_items": {"Wheel of Cheese": 1, "Carton of Milk": 1, "Gold Coin": 15},
        "when_exit": "\"Enjoy your meal!\""
    },
    (2,4): {
        "name": "Mysterious Stranger",
        "dialogue": "\"I have some rare items for sale, if you're interested.\"",
        "quest": None, 
        "list_of_items": {"Magic Scroll": 1, "Ancient Scroll": 1, "Gold Coin": 200},
        "when_exit": "\"I have more rare items if you ever need them...\""
    },
    (4,2): {
        "name": "Forest Hermit",
        "dialogue": "\"Welcome to my humble abode. I have some items that might be of use to you.\"",
        "quest": None,
        "list_of_items": {"Rusty Sword": 1, "Gold Coin": 5},
        "when_exit": "\"Safe travels, adventurer.\""
    },
    (4,2): {
        "name": "Wandering Merchant",
        "dialogue": "\"Looking for something specific? I might have it in my inventory.\"",
        "quest": None,
        "list_of_items": {"Health Potion": 3, "Magic Scroll": 1, "Gold Coin": 50},
        "when_exit": "\"Thanks for stopping by!\""
    },
    (4,3): {
        "name": "Stock Villager",
        "dialogue": "\"Did you hear about the dragon that's been sighted near the mountains? Sounds scary!\"",
        "quest": None,
        "when_exit": "\"Farewell.\""
    },
    (4,3): {
        "name": "Guard Mark",
        "dialogue": "\"Let me guess... Someone stole your sweetroll.\"",
        "quest": None,
        "when_exit": "Thieves are more common than you think... Watch your belongings!"
    },
    (4,3): {
        "name": "Lunk the Monk",
        "dialogue": "A strange monk looks to you, then gestures towards his stand... What is he selling?",
        "quest": None,
        "list_of_items": {"Mana Potion": 2, "Health Potion": 2, "Gold Coin": 20},
        "when_exit": "Lunk nods and returns to his meditation as you leave."
    },
    (4,3): {
        "name": "Old Man Jenkins",
        "dialogue": "\"Back in my day, we didn't have all these fancy potions and scrolls. We had to make do with what we had!\"",
        "quest": None,
        "when_exit": "\"Kids these days have it so easy...\""
    },
    (4,3): {
        "name": "Volo the Bard",
        "dialogue": "\"Ah! My good fellow! Did you hear about the news?\"",
        "quest": "Save Your Allies",
        "when_exit": "\"Stay well!\""
    }
}