from room import Room
from player import Player
from item import Item
import textwrap
import msvcrt


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items
items = {
    "rock": Item("Rock", "hard object that can be used to inflict minimal damage"),
    "wood": Item("Wooden Stick", "used with fire to create light inside caves"),
    "bed": Item("Bed", "wooden frame with soft mattress used for sleeping"),
    "blanket": Item("Blanket", "useless when warm"),
    "telescope": Item("Telescope", "used to look at something from afar"),
    "repellant": Item("Insect Repellant", "used to keep mosquitoes away"),
    "gold": Item("Gold", "reason why people use stones to kill each other")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Add items to rooms
room['outside'].items = [items["rock"], items["wood"]]
room['foyer'].items = [items["bed"], items["blanket"]]
room['overlook'].items = [items["telescope"]]
room['narrow'].items = [items["repellant"]]
room['treasure'].items = [items["gold"]]


# global vars

#  for wrapping paragraphs of room description
wrapper = textwrap.TextWrapper(width=50)

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Tabby", room["outside"])


# function to take care of those repetitive code
def room_exists(player, u_input):
    direction = {"w": player.current_room.n_to, "s": player.current_room.s_to,
                 "a": player.current_room.w_to, "d": player.current_room.e_to}

    # If the user enters "q", quit the game.
    if u_input == "q":
        print("Thanks for playing!")
        exit()

    # If the user enters a cardinal direction, attempt to move to the room there.
    if direction[u_input] != None:
        player.current_room = direction[u_input]

        # * Prints the current room name
        print(f"Current Room: {player.current_room.name}")

        # * Prints the current description (the textwrap module might be useful here).
        word_list = wrapper.wrap(text=player.current_room.description)
        for elem in word_list:
            print(f"Description: {elem}")

        item_list = player.current_room.items

        for item in item_list:
            print(item.name)

    else:

        print("No room in that direction")

# Main


# Write a loop that:
while True:

    # user input
    user_input = msvcrt.getwch().lower()
    #  inputs list
    allowed_inputs = ["w", "a", "s", "d", "q"]

    # * Waits for user input and decides what to do.
    if user_input in allowed_inputs:

        room_exists(new_player, user_input)
        continue

    else:
        # Print an error message if the movement isn't allowed.
        print("Input invalid. Only 'W'/'S'/'A'/'D'/'Q' are allowed")
