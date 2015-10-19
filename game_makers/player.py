# *** FILE CONTAINS DEFINITION OF PLAYER ***

from items import *
from map import locations

# Player can only carry 5kg of stuff in his or her backpack
WEIGHT_LIMIT = 5

'''
CONTENT OF BACKPACK:
	-> student id
	-> laptop
	-> feta cheese
	-> memory stick
 '''

backpack = [item_id, item_laptop, item_cheese, item_memory_stick]


# Start game at the student's accommodation
current_location = locations["accommodation"]
