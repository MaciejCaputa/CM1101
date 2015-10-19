#!/usr/bin/python3
'''
MAJOR CHANGES:
    -> backpack substitutes inventory
    -> location substitutes room
    -> locations substitutes rooms
'''

from map import locations
from player import *
from items import *
from input import *

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
        if i != (len(items) -1):
            string = string + ", "
    return string


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
        print()


def print_backpack_items(items):
    """This function takes a list of backpack items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_backpack_items(backpack)
    You have id card, laptop, feta cheese, memory stick.
    <BLANKLINE>

    """
    
    print("You have " + list_of_items(items) + ".")
    print()


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
    print(location["name"].upper())
    print()
    # Display room description
    print(location["description"])
    print()
    print_room_items(location)



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

def print_menu(exits, room_items, inv_items):
    """
    This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the backpack print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Iterate over room's items
    for take_item in room_items:
        print("TAKE " + take_item["id"] + " to take " + take_item["name"])

    # Iterate over incentory items
    for drop_item in inv_items:
        print("DROP " + drop_item["id"] + " to drop " + drop_item["name"])

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


def execute_go(direction):
    """
    This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_location
    
    if is_valid_exit(current_location["exits"],direction):
        exits = current_location["exits"]
        current_location =  move(exits, direction)
    else:
        print("You cannot go there.")


def backpack_mass():
    """
    This function returns the total mass of all the items in the player's
    backpack
    """
    return sum([item["mass"] for item in backpack])

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

    pass


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

    print("You cannot drop that.") # This communicat will only be displayed if item was not found.




def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

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
    >>> move(locations["lecture"]["exits"], "north") == locations["su"]
    True
    >>> move(locations["gym"]["exits"], "east") == locations["accommodation"]
    True
    """

    # Next location to go to
    return locations[exits[direction]]


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        # Display game status (room description, backpack etc.)
        print_room(current_location)
        print_backpack_items(backpack)

        # Show the menu with possible actions and ask the player
        command = menu(current_location["exits"], current_location["items"], backpack)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

