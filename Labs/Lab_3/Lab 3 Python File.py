# %% [markdown]
# # Lab 3 - Files and Functions
# 

# %% [markdown]
# ## Warm-up 
# 
# Part 1:
# Write a python file that can be imported.
# 
# 
# 

# %%
# Code goes here
from data import dude, get_name, names
print(dude)
print(names)

# %% [markdown]
# 
# Part 2: 
# Using the following as a starting point create a python file that will take in a a name and
# a list of names and tell you if that name is in the list.

# %%
# Code goes here
matches = []
main_list = ["Frank", "John", "Harold", "Kenobi"] #New list
name = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print(name)
print(main_list)
for name in main_list: #Name in main list 
    if name in names: #If it's also in imported list
        print("match found: ", name) #Say what the match was
        matches.append(name) #add name match to list of matching names

print("Final Matches", matches)




# %% [markdown]
# # Main Lab
# 
# Take time to begin working with your partner on your project. Begin to plan out how you would like your game to feel. Remember this is a text-based game. This can be any game you would like 
# 
#     Please stay away from games or software like poker or 21 as these tend to be boring to code and hard to add more to later on, and obviously games that may get you reported by the university.
# 
# 
# ## Part 1:
# 
# Divide up your code and begin  writing the code.
# 
# Keep in mind that when you write your code you will need to be interfacing with your partners code, loading in your player, tools/items/etc, interfacing with the world, monsters and so on. So plan accordingly.
# 
# 
# While we have not gotten to classes take some time to try and code some simple classes. 
# Here is an example:
# ```python 
# 
# #Good
# class Sharps(object):
#     """Create a sharp weapon"""
#     def __init__(self, name, length, age=1, damage=0):
#         """ Initialize name, age, and length damage attributes."""
#         self.name = name
#         self.age = age
#         self.length = length
#         self.damage = damage
#     def do_damage(self, target):
#         target = target - self.damage
# 
# class dager(Sharps):
#     """ makes a dager"""
#     def __init__(self, name, length, age=1, damage=0):
#         """sets up a dagger"""
#         super().__init__(self, name, length, age, damage))
#         self.poision = True
# ```
#         
# 
# 

# %% [markdown]
# 

# %% [markdown]
# # Game Code

# %% [markdown]
# + Backpack
#     + Items
#         + info & remove/add to backpack
#             + 3 tiers for each weapon (Warrior, Assassin, Bard, Mage, Cleric) - (Sword, Dagger, Staff, Instrument, Mace/Staff)
# 
# + Combat
#     + Health totals IE 4/16 hp
#     + Melee and magic with damage
# 
# + Character
#     + Health and Stats
# 
# + Encounters
#     + User Guided Promts
#     + Combat and Conversations
# 
# + Currency
#     + Capatilism......profit????????????????????? 💸💸💸

# %% [markdown]
# ## Items Importing 🏦

# %% [markdown]
# ## Thats a lot of items💀💀💀

# %% [markdown]
# ### loop to generate weapon based on rarity

# %%
# List of strings for dictionary keys and values
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
occupations = ["Engineer", "Artist", "Doctor", "Scientist", "Writer"]

# Initialize an empty list to store dictionaries
list_of_dicts = []

# Use a for loop to generate a dictionary for each name-occupation pair
for i in range(len(names)):
    # Create a dictionary for each person
    person_dict = {
        "name": names[i],
        "occupation": occupations[i]
    }
    # Append the dictionary to the list
    list_of_dicts.append(person_dict)

# Print the list of dictionaries
for person_dict in list_of_dicts:
    print(person_dict)

# %% [markdown]
#     Import item data
#     look for specific words
#     create new list of items
#     give random damage and value

# %%
run  ItemData.json

# %%
Weapons = ["Sword", "Dagger", "Staff", "Instrument", "Mace"]

Damage = [5, 10, 15]

Value = []

# %%
import random

# %%
Items = [
    {"Name": "Sword" "Description": "Blade fit for adventurers" "Damage": 5 "Value": }
]


