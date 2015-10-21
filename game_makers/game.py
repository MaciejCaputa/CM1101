#!/usr/bin/python3
"""
MAJOR CHANGES:
    -> backpack substitutes inventory
    -> location substitutes room
    -> locations substitutes rooms
"""

import msvcrt

from map import locations, ascii_map
from player import *
from items import *
from input import *
from goals import *
import time
import sys


def higher_lower():
    """
    Higher or lower game when guessing the group's number
    """
    while True:
        user_input = input("Input your team number: ")
        try:
            user_input = int(user_input)

            if user_input == 20:
               print("Lucky guess")
               break
            elif user_input > 20:
                print("Too high")
            else:
               print("Too low")
        except:
            print("Invalid input")


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    string = ""

    for i, j in enumerate(items):
        string = string + j["name"]
        if i != (len(items) - 1):
            string = string + ", "
    return string


# this function is used on command LOOK AROUND
def print_room_items(location):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(locations["accommodation"])
    There is door keys, a notebook, a map of Cardiff here.
    <BLANKLINE>

    >>> print_room_items(locations["labs"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(locations["tutor"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if len(location["items"]) != 0:
        print("There is " + list_of_items(location["items"]) + " here.")
    else:
        print("There are no items in this room.")

    print()


def print_backpack_items(items):
    """
    This function takes a list of backpack items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_backpack_items(backpack)
    You have id card, laptop, feta cheese, memory stick.
    <BLANKLINE>

    """

    print("You have " + list_of_items(items) + ".")
    print()

def print_slow(text, delay = 0.063):
    "This function takes text and cause a delay in printing it."
    for ch in text:
        print(ch, end="")
        sys.stdout.flush()
        time.sleep(delay)

        if msvcrt.kbhit():
            delay = 0


def print_room(location):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(locations["accommodation"])
    <BLANKLINE>
    YOUR ACCOMMODATION
    <BLANKLINE>
    Sarah's description
    <BLANKLINE>
    There is door keys, a notebook, a map of Cardiff here.
    <BLANKLINE>

    >>> print_room(locations["lecture"])
    <BLANKLINE>
    LECTURE THEATRE
    <BLANKLINE>
    Sarah's description
    <BLANKLINE>

    >>> print_room(locations["labs"])
    <BLANKLINE>
    LABS
    <BLANKLINE>
    Sarah's description
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print_slow(location["name"].upper())
    print()
    # Display room description
    print_slow(location["description"])
    print()
    # Display exits
    print_menu(location["exits"])
    print()
    # room's item are now printed on command LOOK AROUND
    # print_room_items(location)


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(locations["accommodation"]["exits"], "south")
    'lecture theatre'
    >>> exit_leads_to(locations["lecture"]["exits"], "south")
    'labs'
    >>> exit_leads_to(locations["tutor"]["exits"], "north")
    'IT room'
    """
    return locations[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "Robs' room")
    GO SOUTH to Robs' room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits):
    """
    This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print


    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    What do you want to do?

    """
    print("EXITS:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    """
    *** DROP AND TAKE ITEMS ARE ONLY DISPLAYD ON COMMANDS ***

    # Iterate over room's items
    for take_item in room_items:
        print("TAKE " + take_item["id"] + " to take " + take_item["name"])

    # Iterate over inventory items
    for drop_item in inv_items:
        print("DROP " + drop_item["id"] + " to drop " + drop_item["name"])

        # Show option to use item if required
        if drop_item["id"] == "laptop" or drop_item["id"] == "map":
            print("USE " + drop_item["id"] + " to use " + drop_item["name"])
    """
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """
    This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(locations["accommodation"]["exits"], "south")
    True
    >>> is_valid_exit(locations["lecture"]["exits"], "up")
    False
    >>> is_valid_exit(locations["labs"]["exits"], "north")
    True
    >>> is_valid_exit(locations["it"]["exits"], "east")
    False
    """
    return chosen_exit in exits


def print_goal(goal):
    """
    This function prints out a congratulations message upon completing a goal
    """
    global current_goal

    progress = str(current_goal + 1) + "/" + str(len(goals))
    dashes = "-" * (16 + len(progress) + len(goal["name"]))

    print()
    print(dashes)
    print("ACHIEVED GOAL " + progress + ": " + goal["name"])
    print(goal["text"])
    print(dashes)


def complete_goal(goal):
    """
    This function is called when a goal is completed. It prints out a message
    and moves the player onto the next goal
    """
    global current_goal
    global previous_location

    # Print out a message
    print_goal(goal)

    # Move on to next goal
    current_goal += 1

    # Reset previous_location if player has just completed contact george goal
    # so that the room information is shown again
    if goal == goal_contact_george:
        previous_location = ""

    print("Press enter to continue...")
    input()


def execute_go(direction):
    """
    This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_location
    global current_goal

    if is_valid_exit(current_location["exits"], direction):
        exits = current_location["exits"]
        current_location = move(exits, direction)

        # Check if player has completed a location-based goal
        for goal in current_location["goals"]:
            if goals.index(goal) == current_goal:
                complete_goal(goal)
                break

    else:
        print("You cannot go there.")


def backpack_mass():
    """
    This function returns the total mass of all the items in the player's
    backpack
    """
    return sum([item["mass"] for item in backpack])


def use_laptop():
    """
    The function 'uses' the laptop. The message printed out depends on what
    goal the player is currently on
    """
    global current_goal

    if current_goal < 1:
        print("Not sure what to use laptop for...")
    elif current_goal == 1:
        print("Going on www.facebook.com")
        complete_goal(goal_contact_george)
    else:
        print("Worked on the game for a bit")


def execute_take(item_id):
    """
    This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's backpack. However, if
    there is no such item in the room, this function prints
    "You cannot take that."

    """
    # Find the item in the list of items in the current room
    for item in current_location["items"]:
        if item["id"] == item_id:
            # Check that taking this item will not put player over the weight
            # limit
            weight = backpack_mass() + item["mass"]
            if weight > WEIGHT_LIMIT:
                print("You can only carry " + str(WEIGHT_LIMIT) + "kg!")
                return

            #
            current_location["items"].remove(item)
            backpack.append(item)
            return


def execute_drop(item_id):
    """
    This function takes an item_id as an argument and moves this item from the
    player's backpack to list of items in the current room. However, if there is
    no such item in the backpack, this function prints "You cannot drop that."
    """

    for item in backpack:
        if item["id"] == item_id:
            backpack.remove(item)
            current_location["items"].append(item)
            return

    print("You cannot drop that.")  # This message will only be displayed if item was not found.


def execute_use(item_id):
    """
    This function uses an item
    """

    for item in backpack:
        # Find the item in the backpack
        if item["id"] == item_id:

            if item_id == "laptop":
                use_laptop()
                return
            elif item_id == "map":
                print(ascii_map)
                return

    print("You cannot use that.")


def execute_help():
    print('''
    \t\tSupported commands:

    MOVEMENT:
      GO NORTH
      GO EAST
      GO SOUTH
      GO WEST

    TAKE, DROP, USE:
      TAKE                - shows all items in the room
      TAKE [name of item] - takes specific item
      DROP                - shows all items in your backpack that you can drop
      DROP [name of item] - drops specific item
      USE [name of item]  - uses specific item

    OTHER COMMANDS:
      BACKPACK \t\t- shows content of your backpack
      HELP \t\t- prints all supported commands
      LOOK AROUND \t- prints all items available in the room

    You can alway type HELP to print supported commands.
    ''')

    print("Press enter to continue...")
    input()

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if len(command) == 0:
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            if len(current_location["items"]) > 0:
                print("Take what? You can type:")

                for item in current_location["items"]:
                    print("  TAKE " + item["id"] + " to take " + item["name"])
            else:
                print("There is nothing to take")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            if len(backpack) > 0:
                print("Drop what? You can type:")
                for item in backpack:
                    print("  DROP " + item["id"] + " to drop " + item["name"])
            else:
                print("You have nothing to drop")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")

    elif command[0] == "backpack":
        print_backpack_items(backpack)

    elif command[0] == "help":
        execute_help()

    elif len(command) >= 2 and (command[0] == "look") and (command[1] == "around"):
        print_room_items(current_location)

    else:
        print("This makes no sense.")

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """



    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """
    This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(locations["labs"]["exits"], "north") == locations["it"]
    False
    >>> move(locations["lecture"]["exits"], "north") == locations["accommodation"]
    True
    >>> move(locations["gym"]["exits"], "east") == locations["accommodation"]
    True
    """

    # Next location to go to
    return locations[exits[direction]]


def end_game():
    """
    This function is called when the game ends
    """
    print("Well done, you have completed the game!")

def game_makers():
    """
    This function prints title of the game.
    """
    print("\n\n\n\n\t\t\t-=GAME MAKERS=-\n\n\n\n")

    print("Press enter to continue...")
    input()


previous_location = ""

# This is the entry point of our program
def main():
    global previous_location

    game_makers()

    # Instructions for user at first
    execute_help()
    # Main game loop - keep going whilst there are goals left
    while current_goal < len(goals):

        # Start higher or lower game straight away if on this goal
        if goals[current_goal] == goal_pick_number:
            higher_lower()
            complete_goal(goal_pick_number)

        # Display game status (room description)
        if previous_location != current_location:
            print_room(current_location)

        # content of backpack is now printed only on command BACKPACK
        # print_backpack_items(backpack)

        # Show the menu with possible actions and ask the player
        command = menu(current_location["exits"], current_location["items"], backpack)

        previous_location = current_location

        # Execute the player's command
        execute_command(command)


    # End game when leaving the while loop
    end_game()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
