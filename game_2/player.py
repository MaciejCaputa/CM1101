from items import *
from map import rooms

# Player can only carry 5kg
WEIGHT_LIMIT = 5

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]
