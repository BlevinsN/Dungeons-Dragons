from Dnd_Structures import *
import requests


def quick_search():
	quick_options = {'1':"classes",
					 '2':"races",
					 '3':"equipment-categories",
					 '4':"custom search"}
	print("QUICK SEARCH")
	print("____________")
	for key,value in quick_options.items():
		print(key, " : ", value)
	user_selection = input("Make a selection: ")
	if user_selection != 4:
		r = requests.get('https://www.dnd5eapi.co/api/' + quick_options[user_selection])
		results_check(r.json())
	else:
		custom_search = input("Search: ")
		r = requests.get('https://www.dnd5eapi.co/api/' + custom_search)




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

def list_results(results_dict):
	item_dict = {}
	for item in results_dict['results']:
		item_dict.update({item['name']:item['url']})
	return item_dict

def get_details(item_dict):
	print("Would you like to see more details about one of the items?")
	user_selection = input("If not, respond 'No':" )
	if user_selection != "No":
		while user_selection != "No":
			print('https://www.dnd5eapi.co' + item_dict[user_selection])
			element_details = requests.get('https://www.dnd5eapi.co' + item_dict[user_selection])
			print(element_details.text)
			print("Would you like to see more details about one of the items?")
			user_selection = input("If not, respond 'No':" )


def results_check(results_dict):
	item_dict = list_results(results_dict)
	print("RESULTS")
	print("_______")
	for element in item_dict:
		print(" - ", element)
	get_details(item_dict)