from room import Room
from player import Player
import textwrap
import msvcrt


# global vars

#  for wrapping paragraphs of room description
wrapper = textwrap.TextWrapper(width=50)


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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Tabby", room["outside"])


# Write a loop that:
#

while True:

    # user input
    user_input = msvcrt.getwch().lower()
    #  inputs list
    allowed_inputs = ["w", "a", "s", "d", "q"]

    # * Prints the current room name
    # print(f"{room[new_player.current_room].name}")

    # * Prints the current description (the textwrap module might be useful here).
    # word_list = wrapper.wrap(text=room[new_player.current_room].description)
    # for elem in word_list:
    #     print(elem)

    # * Waits for user input and decides what to do.

    try:

        if user_input in allowed_inputs:

            if user_input == 'w':

                if new_player.current_room.n_to != None:

                    new_player.current_room = new_player.current_room.n_to
                    print(new_player.current_room.name)

                    # * Prints the current description (the textwrap module might be useful here).
                    word_list = wrapper.wrap(
                        text=new_player.current_room.description)
                    for elem in word_list:
                        print(elem)

                else:
                    print("No room in that direction")

            elif user_input == 's':

                if new_player.current_room.s_to != None:

                    new_player.current_room = new_player.current_room.s_to
                    print(new_player.current_room.name)

                    # * Prints the current description (the textwrap module might be useful here).
                    word_list = wrapper.wrap(
                        text=new_player.current_room.description)
                    for elem in word_list:
                        print(elem)

                else:
                    print("No Room in that direction")

            elif user_input == 'a':

                if new_player.current_room.w_to != None:
                    new_player.current_room = new_player.current_room.w_to
                    print(new_player.current_room.name)

                    # * Prints the current description (the textwrap module might be useful here).
                    word_list = wrapper.wrap(
                        text=new_player.current_room.description)
                    for elem in word_list:
                        print(elem)

                else:
                    print("No Room in that direction")

            elif user_input == 'd':

                if new_player.current_room.e_to != None:
                    new_player.current_room = new_player.current_room.e_to
                    print(new_player.current_room.name)

                    # * Prints the current description (the textwrap module might be useful here).
                    word_list = wrapper.wrap(
                        text=new_player.current_room.description)
                    for elem in word_list:
                        print(elem)
                else:
                    print("No Room in that direction")

            else:
                print("Thanks for playing!")
                break
        else:
            print("Input invalid. Only 'W'/'S'/'A'/'D'/'Q' are allowed")

    except ValueError:
        print("Input invalid. Only 'W'/'S'/'A'/'D'/'Q' are allowed")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
