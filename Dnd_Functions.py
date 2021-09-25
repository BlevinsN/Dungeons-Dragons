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

def list_classes_races(results_dict):
	item_dict = {}
	for item in results_dict['results']:
		item_dict.update({item['name']:item['url']})
	return item_dict

def get_details(item_dict):
	print("FIXME")


def class_race_check(request, results_dict):
	if (request == "races") | (request == "classes"):
		item_dict = list_classes_races(results_dict)
		print("RESULTS")
		print("_______")
		for element in item_dict:
			print(" - ", element)
		return True

