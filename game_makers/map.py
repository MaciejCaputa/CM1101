# *** THIS FILE CONTAINS MAP OF ALL LOCATIONS ***

from items import *
from goals import *

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

ascii_map = """
              STUDENT'S UNION
                     |
                     |
    GYM ------ ACCOMMODATION ------ TOWN
                     |
                     |
                LECTURE HALL ------ IT
                     |              |
                     |              |
                   LABS        TUTOR'S OFFICE
"""

location_accommodation = {
    "name": "your accommodation",
    "description":
    """You live in Senghennydd court, one of the closest halls to the Computer Science building. The laundry is close, you can wake up late and still make it to lectures on time (unless you're George). Life is good.""",
    "exits":  {"west": "gym", "north": "su", "east": "town", "south": "lecture"},
    "items": [item_keys, item_notebook, item_map],
    "goals": []
}

location_su = {
    "name": "student union",
    "description":
    """The SU towers above you, with 4 floors of fun packed things to do (if you can find your way around that is). Society meetings, concerts and nights out are held here, as well as the odd pub quiz on a Wednesday night. There is a vast selection of food as well (which is obviously the reason why you decided to come here).""",
    "exits":  {"south": "accommodation"},
    "items": [],
    "goals": []
}

location_town = {
    "name": "town",
    "description":
    """You are standing on Queen Street, one of the main high streets in Cardiff City Centre. The streets are full of people and you can hear out of tune singing in the distance.""",
    "exits":  {"west": "accommodation"},
    "items": [],
    "goals": []
}

location_gym = {
    "name": "gym",
    "description":
    """You arrive at the Gym. You can see people doing squats, lifting dumbells, running on treadmills and Kirill is lifting weights in the corner. You decide to join him.""",
    "exits":  {"east": "accommodation"},
    "items": [],
    "goals": []
}

location_lecture = {
    "name": "lecture theatre",
    "description":
    """You are standing in the lecture theature T\\2.09. Most of the seats are already taken, but you can see Joe waving wildly at you from the far side of the room. You make your way over and take your seat with the rest of your team. The lights start flashing (the cinema mode gone mad) and Kirill does not look impressed.""",
    "exits":  {"north": "accommodation", "east": "it", "south": "labs"},
    "items": [],
    "goals": [goal_lecture]
}

location_labs = {
    "name": "labs",
    "description":
    """You scan your ID card and enter the labs, making sure to sign in.""",
    "exits":  {"north": "lecture"},
    "items": [item_pen],
    "goals": [goal_labs1, goal_labs2]
}

location_it = {
    "name": "IT room",
    "description":
    """You walk inside the IT room. The maintenance staff look up at you questioningly.""",
    "exits":  {"south": "tutor", "west": "lecture"},
    "items": [],
    "goals": [goal_it]
}

location_tutor = {
    "name": "tutor's room",
    "description":
    """You enter your tutor's room. There are lots of cacti growing on the windowsill.""",
    "exits":  {"north": "it"},
    "items": [],
    "goals": [goal_tutor, goal_presentation]
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
