from map import *


"""
GENERAL STRUCTURE OF GOALS:
    -> name - displayed name
    -> text  - message shown upon completion of the goal
"""

goal_lecture = {
    "name": "Attend lecture",
    "text": """
You arrive at LECTURE THEATRE. You sit next to your JOINT HONOURS friend
Sarah. The lecture begins and you proceed to listen about using Python and
possibly implementing a game.

George was late as usual, he says that you should contact him via Facebook
to fill him in with the information he missed."""
}

goal_contact_george = {
    "name": "Contact George",
    "text": """
You have successfully contacted George. He says "lets meet in the labs at
12:00, bring your homemade feta"."""
}

goal_labs1 = {
    "name": "Go to labs",
    "text": """
You meet everyone at 12:00 in the labs, George is late, as usual. Two tutors
approach your group and say they want to chat. They introduce themselves as
Kirill & Matt.
Upon a brief introduction about themselves they explain that your group must
create a game. However as you are a JOINT HONOURS student you don't have to do
as much, but they want you to pick a team number."""
}

goal_pick_number = {
    "name": "Pick group number",
    "text": """
They approve your number. They explain that they have an obssession with the
number 20, as it is the number of vertices a Dodecahedron has, how bizarre!!

All of a sudden the wi-fi goes down, your group panics, and Maciej worsens the
situation by telling your group he's going back to Poland on wednesday. You
need to ask your tutor for to do the presentation early."""
}

goal_tutor = {
    "name": "Visit tutor",
    "text": """
You arrive at your tutors room, panting after a quick sprint down the corridor.
Maciej explains the situation. Kirill and Matt move the deadline of the
presenation 1 day earlier.

You try to start working on the game, but the Wi-fi is down..."""
}

goal_it = {
    "name": "Go to IT",
    "text": """
Arriving at the IT room you explain the eduroam is crumbling (much like feta)
and you can't connect to the Wi-fi. They reset your connection and all of a
sudden the Wi-fi is working again.

Now you're ready to start working on the game."""
}

goal_labs2 = {
    "name": "Go to labs",
    "text": """
You arrive at the labs and split the task into seperate chunks for individuals.
Harder tasks designated to more experienced members, lesser tasks designated to
less experienced. You work at the game non stop for the next 48 hours,
consisting of a full blown montage of programming so amazing that it couldn't
be coded in this game (what are the chances?)

Now you're ready for the presentation."""
}

goal_presentation = {
    "name": "Attend presentation",
    "text": """
You pull of your presentation with amazing finesse and recieve many
commendations from your peers and teaching staff. Knowing you don't have much
more during the week you treat yourself to a night out with your group.

You head to the SU. YOLO is on and you get absolutely plastered!!"""
}

# This list defines the order in which goals must be completed
goals = [
    goal_lecture,
    goal_contact_george,
    goal_labs1,
    goal_pick_number,
    goal_tutor,
    goal_it,
    goal_labs2,
    goal_presentation
]
