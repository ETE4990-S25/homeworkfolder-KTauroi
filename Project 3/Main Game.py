import item_initalization
import stat_generator
import Encounters

def main():
    # Prompt player for name and class
    player_name = input('Enter your name: ')

    # Create player with name and class
    player = stat_generator.Player(player_name, player_class)

    # Generate inventory and add it to player's inventory
    gear, gold = item_initalization.generate_inventory()
    player._gold += gold
    player.inventory.add_items(gear)  # Use `add_items` if it's an Inventory class

    # Display player stats and inventory
    player.display_stats()
    player.display_inventory()

    # Start the encounter loop (this is where the player can start the game)
    Encounters.encounter(player)  # Pass player to the encounter

if __name__ == "__main__":
    main()

