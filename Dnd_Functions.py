from Dnd_Structures import *
def add_object(item):
	new_item = html_object(item['name'],
				item['desc'],
				item['higher_level'],
				item['range'],
				item['components'],
				item['material'],
				item['ritual'],
				item['duration'],
				item['concentration'],
				item['casting_time'],
				item['level'],
				item['attack_type'])
	return new_item
