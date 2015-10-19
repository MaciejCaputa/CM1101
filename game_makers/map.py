# *** THIS FILE CONTAINS MAP OF ALL LOCATIONS ***

from items import *

'''
LOCATIONS:
    -> student's accommodation
    -> Student Union
    -> Town
    -> Gym
    -> Lecture
    -> Labs
    -> IT maintanance
    -> Tutor's Office


GENERAL STRUCTURE OF LOCATION:
    -> name         - name which is displayed in command prompt
    -> description  - description of the room which is displayed in command prompt
    -> exits        - dict consisting possible exits from the room
    -> items        - list of consisting item accesible in particular room
    -> goals        - list of consisting index of goals that need to be achieve in particular room
'''

location_accommodation = {
    "name": "your accommodation",
    "description":
    """Sarah's description""",
    "exits":  {"west": "gym", "north": "su", "east": "town", "south": "lecture"},
    "items": [item_keys, item_notebook, item_map],
    "goals": []
}

location_su = {
    "name": "student union",
    "description":
    """Sarah's description""",
    "exits":  {"south": "accommodation"},
    "items": [],
    "goals": []
}

location_town = {
    "name": "town",
    "description":
    """Sarah's description""",
    "exits":  {"west": "accommodation"},
    "items": [],
    "goals": []
}

location_gym = {
    "name": "gym",
    "description":
    """Sarah's description""",
    "exits":  {"east": "accommodation"},
    "items": [],
    "goals": []
}

location_lecture = {
    "name": "lecture theatre",
    "description":
    """Sarah's description""",
    "exits":  {"north": "su", "east": "it", "south": "labs"},
    "items": [],
    "goals": [1]
}

location_labs = {
    "name": "labs",
    "description":
    """Sarah's description""",
    "exits":  {"north": "lecture"},
    "items": [item_pen],
    "goals": [3,7]
}

location_it = {
    "name": "IT room",
    "description":
    """Sarah's description""",
    "exits":  {"south": "tutor", "west": "lecture"},
    "items": [],
    "goals": []
}

location_tutor = {
    "name": "tutor's room",
    "description":
    """Sarah's description""",
    "exits":  {"north": "it"},
    "items": [],
    "goals": [5,8]
}

# Combining all seperate locations together
locations = {
    "accommodation": location_accommodation,
    "su": location_su,
    "town": location_town,
    "gym": location_gym,
    "lecture": location_lecture,
    "labs": location_labs,
    "it": location_it,
    "tutor": location_tutor
}