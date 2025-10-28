import os
"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    stats_tuple = calculate_stats(character_class, 1)
    character_dict = {"name": name, "class": character_class, "level": 1, "strength": stats_tuple[0], "magic": stats_tuple[1], "health": stats_tuple[2], "gold": 100}
    return character_dict

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    standardized_class = character_class.lower()

    str_base, mag_base, hp_base = (40, 40, 40) # Default

    if standardized_class == "mage":
        str_base, mag_base, hp_base = (5, 15, 80)
    elif standardized_class == "warrior":
        str_base, mag_base, hp_base = (15, 5, 100)
    elif standardized_class == "rogue":
        str_base, mag_base, hp_base = (10, 10, 70)
    elif standardized_class == "cleric":
        str_base, mag_base, hp_base = (8, 12, 90)

    # Scale stats with level
    # Example: Add +2 STR, +1 MAG, +10 HP per level for a Warrior
    # You can design your own formulas!
    strength = str_base + (level * 2) 
    magic = mag_base + (level * 1)
    health = hp_base + (level * 10)

    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    try:
        with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        # 'with open' handles closing/flushing
        return True # Add this
    except Exception as e:
        print(f"An error occurred: {e}")
        return False # Add this

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    character_data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Clean up whitespace and split at the colon
                parts = line.strip().split(': ')

                if len(parts) == 2:
                    key, value = parts

                    # Load data into dictionary
                    if key == "Character Name":
                        character_data["name"] = value
                    elif key == "Class":
                        character_data["class"] = value
                    # Convert numbers back to int
                    elif key == "Level":
                        character_data["level"] = int(value)
                    elif key == "Strength":
                        character_data["strength"] = int(value)
                    elif key == "Magic":
                        character_data["magic"] = int(value)
                    elif key == "Health":
                        character_data["health"] = int(value)
                    elif key == "Gold":
                        character_data["gold"] = int(value)

        return character_data # Return the completed dictionary

    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return None
    except Exception as e:
        # Handle other errors like bad data in the file
        print(f"Error reading character file: {e}")
        return None

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character["name"]}")
    print(f"Class: {character["class"]}")
    print(f"Level: {character["level"]}")
    print(f"Strength: {character["strength"]}")
    print(f"Magic: {character["magic"]}")
    print(f"Health: {character["health"]}")
    print(f"Gold: {character["gold"]}")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level

    # 1. Increase the level in the dictionary
    character["level"] += 1 

    # 2. Recalculate stats based on the NEW level and class
    new_stats = calculate_stats(character["class"], character["level"])

    # 3. Update the character dictionary with the new stats
    character["strength"] = new_stats[0]
    character["magic"] = new_stats[1]
    character["health"] = new_stats[2]

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    char = create_character("TestHero", "Warrior")
    display_character(char)

    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")

    leveled_up = level_up(char)
    display_character(char)
