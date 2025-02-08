# %% [markdown]
# # Lab 2 - Refactoring
# ## Refactoring is:
# 
# Refactoring is the process of restructuring or rewriting code, while not changing its original functionality. The goal of refactoring is to improve internal code by making many small changes without altering the code's external behavior. 
# 
# It is easier said than done. 

# %% [markdown]
# ### Part 1 - Warm-up
# 
# You will refactor the following code:

# %%
#stolen from https://realpython.com/python-refactoring/
#yes you can go there and look at what they did no do it yourself
x = 5
value = input("Enter a number: ")
y = int(value)
if x < y:
    print(f"{x} is less than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is more than {y}")

# %%
# put your refactored code here
solution = 5
ans = input(int)
if solution < int(ans) :
    print(solution,"is greater than", ans)
elif solution == int(y):
    print(solution, "is equal to", ans)
else:
    print(solution, "is greater than", ans)

# %% [markdown]
# ## Part 2
# Refactor the following

# %%
def a(x, y):
    if x == "wizard":
        if y == "fireball":
            return "casts fireball"
        elif y == "lightning":
            return "casts lightning"
        else:
            return "does nothing"
    elif x == "warrior":
        if y == "slash":
            return "slashes with sword"
        elif y == "bash":
            return "bashes with shield"
        else:
            return "does nothing"
    else:
        return "does nothing"

def b(z):
        if z == "dragon":
            return "fights dragon"
        elif z == "goblin":
            return "fights goblin"
        elif z == "orc":
            return "fights orc"
        else:
            return "does nothing"

def c():
    for i in range(5):
        print("exploring dungeon")
    print("finding treasure")

print(a("wizard", "fireball"))
print(a("warrior", "slash"))
print(b("dragon"))
c()


# %%
#dictionaries with key value pairs being classes with nested dictionary giving actions and what their perform flavor is IE: cast perform
def character(job, move):
    job_moves = {
        "wizard": {
            "moves": ["lightning", "fireball"],
            "action": "casts"
        },
        "fighter": {
            "moves": ["slash", "menancing strike"],
            "action": "uses"
        },
        "rogue": {
            "moves": ["stab", "poison dart"],
            "action": "performs"
        },
        "cleric": {
            "moves": ["healing ward", "bless"],
            "action": "uses"
        }, 
        "paladin": {
            "moves": ["thunderous smite", "healing hands"],
            "action": "uses"
        },
        "bard": {
            "moves": ["bardic inspiration", "the song of rest"],
            "action": "performs"
    }
    }

    if job in job_moves and move in job_moves[job]["moves"]:
        return f"{job} {job_moves[job]['action']} {move}"
    
    return "does nothing"

#list of mobs and their encounter phrase
def mob(enemy):
    encounters = {
        "dragon": "Party defends against dragon",
        "goblin": "Party challenges goblin Chief",
        "orc": "Party an orc band"
    }
    
    return encounters.get(enemy, "does nothing")

#Adventuring loop
def adventure():
    for i in range(1):
        print("exploring dungeon")
    for j in range(1):
        print("finding treasure")

#pass classfunction - job/class - action/move
#pass mobfunction - dictionary key which is a mob name which returns their phrase
print(mob("dragon"))
print(character("wizard", "fireball"))
print(character("fighter", "slash"))
print(character("rogue", "poison dart"))
print(character("cleric", "healing ward"))
print(character("bard","the song of rest"))

# %% [markdown]
# # Part 3
# Refactor your partners lab 1 code so it is a clean function. Look at part 4 and see how you can adapt the code to fit project one. 

# %%
# put your refactored code here
import random

def roll_dice(num_dice=5, sides=6):
    """Rolls num_dice dice with a given number of sides and returns a list of results."""
    return [random.randint(1, sides) for _ in range(num_dice)]

def display_rolls(player, rolls):
    """Displays the dice roll results and the total score."""
    total = sum(rolls)
    print(f"{player} rolled: {rolls} (Total: {total})")
    return total

def play_round():
    """Plays a single round and returns the result (win/loss/tie)."""
    user_rolls = roll_dice()
    computer_rolls = roll_dice()

    user_total = display_rolls("You", user_rolls)
    computer_total = display_rolls("Computer", computer_rolls)

    if user_total > computer_total:
        print("You won!\n")
        return "win"
    elif user_total < computer_total:
        print("You lost!\n")
        return "loss"
    else:
        print("It's a tie!\n")
        return "tie"

def main():
    print("Welcome to Dice Battle! Roll 5 dice against the computer and see who wins!")

    user_wins = 0
    user_losses = 0
    rounds_played = 0

    while True:
        input("Press Enter to roll... ")
        result = play_round()
        
        if result == "win":
            user_wins += 1
        elif result == "loss":
            user_losses += 1
        
        rounds_played += 1

        if input("Play again? (yes/no): ").strip().lower() != "yes":
            win_rate = (user_wins / rounds_played) * 100 if rounds_played else 0
            print("\nGame Over! Here are your stats:")
            print(f"Total Rounds: {rounds_played}")
            print(f"Wins: {user_wins}, Losses: {user_losses}, Win Rate: {win_rate:.2f}%")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

# %% [markdown]
# ## Part 4 - take home but start in class                  
# # Project #1  introduction 
# 
# 
# Your task is to develop a text-based video game focusing on the player profile, inventory system, and combat mechanics. Create a realistic player character with at least 10 inventory items, each with a description and an associated trait. Enjoy the process!
# 
# Incorporate all the concepts we've covered so far, including files (read and write), JSON, operators, lists, optional tuples, functions, modules, and classes.
# 
# ### Requirements:
# - **Player Type Selection**: Allow players to choose their character type. Set attributes based on the choice (e.g., wizard: magic = 10, knight: magic = 0).
# - **Inventory Display**: Implement a function to show the player's inventory.
# - **Item Details**: Write a function to provide detailed information about an inventory item (e.g., Knife: "forged in the depths of Polymar", +5 magic, edged weapon, one-handed).
#   - Bonus: Calculate bonuses when equipping and unequipping items.
# - **Inventory Management**: Create functions to add and remove items from the inventory.
# - **Persistence**: Ensure the game can save and reload the player's character using files.
# 
# Focus on building the player and inventory system for your text-based adventure game (similar to Zork). The map and gameplay can be developed later.
# 
# ### Game Features:
# - **Player Profile**: Include player stats.
# - **Inventory System**: Implement a bag to hold items.
# - **Items**: Include 10 items, each with a description and trait (e.g., +5 magic).
# - **Concepts**: Utilize functions, loops, arrays, classes, and constants. You may also use files and structs if desired.
# - **Player Type Selection**: Allow players to choose their character type and set attributes accordingly (e.g., wizard: magic = 10, knight: magic = 0).
# - **Inventory Display**: Implement a function to show the player's inventory.
# - **Code Quality**: Keep your code clean and consider various player needs, as this project will be handed off to a partner for further development.
# 
# 

# %% [markdown]
# # Project 1 - Part 1
# Spend time planning out your code. You may work with your partner to plan out your code. How would you like your game to play? 
# 
# Use a UML planner like: 
# 
# 
# https://miro.com/
# 

# %%



